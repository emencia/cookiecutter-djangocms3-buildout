#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Post hooks to finish install

When developing on this script, add "test" as first argument to use test mode with
a dummy context else the script will fails (because the context is empty).
"""
import ast, copy, json, os, subprocess, sys

# Sadly for now we dont have any clean way to automatically get the version from the
# template, either using "git describe" or package version because hooks are applied
# from the created project and are unaware of cookiecutter template location
__version__ = "1.4.4"

# Project directory path
PROJECT_DIR = 'project'

# Capture cookiecutter context
COOKIE_CONTEXT = """{{ cookiecutter }}"""

# A sample of cookiecutter context used for test/dev purposes
TEST_CONTEXT = {
    "project_name": "Project name",
    "repo_name": "project-name",
    "repo_username": "emencia",
    "repo_host": "github.com",
    "secret_key": "DUMMY-KEY",
    "_copy_without_render": "yes",
    "enable_accounts": "yes",
    "enable_contact_form": "yes",
    "enable_porticus": "yes",
    "enable_slideshows": "yes",
    "enable_zinnia": "yes",
    "enable_multiple_languages": "no",
    "enable_https": "yes",
}


class Caller(object):
    """
    Simple caller for Popen subprocess
    """
    def __init__(self, cwd=None):
        self.cwd = cwd

    def __call__(self, *args):
        popen = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=self.cwd)
        out, err = popen.communicate()
        if popen.returncode != 0:
            print args
            print 'Exit %d' % popen.returncode
            sys.exit(popen.returncode)
        return out


def print_part_title(title, line_chr='=', surrounded=True):
    """
    Display a nice title like RST style
    """
    if surrounded:
        print line_chr*len(title)
    print title
    print line_chr*len(title)
    print


class AppManager(object):
    """
    Manage apps from given context
    """
    # Base apps are always enabled
    BASE_APPS = [
        # This is the mod name, not the package or module name
        'admin_style',
        'assets', # Used in templates
        'ckeditor', # Used in djangocms and another apps
        'cms',
        'emencia_utils', # Useful utilities
        'filebrowser', # Used in djangocms and another apps
        'google_tools', # Used for almost customer projects
        'icomoon', # For Icomoon webfont
        'logentry', # Admin log entries browser
        'site_metas', # Simple addon to expose some metas in all views
        'sitemap', # Common sitemap for djangocms and another apps
    ]

    # Optional apps enabled if their context value is "yes"
    # Key is the prompt question variable name, Value is the app name to add
    OPTIONAL_APPS = {
        'enable_accounts': 'accounts',
        'enable_contact_form': 'contact_form',
        'enable_porticus': 'porticus',
        'enable_slideshows': 'slideshows',
        'enable_zinnia': 'zinnia',
    }

    # Dependancies that will be added to enabled apps if their dependant is enabled
    # Key is the app name, Value is a list of app names to add
    DEPENDANCIES = {
        'accounts': ['crispy_forms', 'recaptcha'],
        'contact_form': ['crispy_forms', 'recaptcha'],
    }

    def __init__(self, context, project_dir, test_mode=False):
        self.context = context
        self.project_dir = project_dir
        self.test_mode = test_mode

    def get_enabled_apps(self):
        """
        Return a list of all enabled apps from base apps, optional apps,
        dependancies, etc..
        """
        apps = [k for k in self.BASE_APPS]

        # Search for optional app variable name in context
        for varname,appname in self.OPTIONAL_APPS.items():
            if varname in self.context and self.context.get(varname) == 'yes':
                apps.append(appname)

        # Search for dependancies
        for item in apps:
            if item in self.DEPENDANCIES:
                apps.extend(self.DEPENDANCIES.get(item))

        return set(apps)

    def enable_mods(self, apps):
        """
        Enable mods in their dependancies from enabled apps
        """
        mods = set(apps)
        symlink_list = []

        # Build a list of symlink to create for mods
        symlink_list = [(
            os.path.join('..', 'mods_available', name),
            os.path.join(self.project_dir, 'mods_enabled', name)
        ) for name in mods]

        #print json.dumps(symlink_list, indent=4)

        # Create symlinks
        for target, linkfile in symlink_list:
            print "* Symlink TO:", target, 'INTO:', linkfile
            if not self.test_mode:
                os.symlink(target, linkfile)

        return symlink_list


def repository_init(context, project_dir, test_mode=False):
    """
    Repository first initialization with Git
    """
    repository_path = "git@{host}:{username}/{name}.git".format(
        host=context['repo_host'],
        username=context['repo_username'],
        name=context['repo_name'],
    )

    call = Caller('.')
    print "* Init"
    if not test_mode:
        call('git', 'init', '.')
    print "* Adding files"
    if not test_mode:
        call('git', 'add', '.')
    print "* First commit"
    if not test_mode:
        call('git', 'commit', '-m', "First commit from 'cookiecutter-djangocms3-buildout=={}'".format(__version__))
    print "* Configure remote origin on", repository_path
    if not test_mode:
        call('git', 'remote', 'add', 'origin', repository_path)

    return repository_path


def store_project_context(context, project_dir, test_mode=False):
    """
    Store used context to create the project
    """
    c = copy.deepcopy(context)
    del c['secret_key']
    del c['_copy_without_render']
    c.update({
        #'generator': 'cookiecutter-djangocms3-buildout=={}'.format(get_template_version())
        'generator': 'cookiecutter-djangocms3-buildout=={}'.format(__version__)
    })

    destination = os.path.join(project_dir, '__init__.py')

    with open(destination, 'r') as infile:
        content = infile.read().format(cookiecutter_context=json.dumps(c, indent=4))

    if not test_mode:
        print "* Writing context into {}".format(project_dir)
        with open(destination, 'w') as outfile:
            outfile.write(content)
    else:
        print "* Pretending to write context into: {}".format(destination)



def get_template_version():
    """
    Return 'cookiecutter-djangocms3-buildout' version from git tag
    """
    call = Caller('.')
    version = call('git', 'describe', '.')
    return version.strip()


if __name__ == "__main__":
    import sys
    # Get the context to use and enable or not the test mode
    test_mode = False
    if len(sys.argv)>1 and sys.argv[1].strip() == 'test':
        context = TEST_CONTEXT
        PROJECT_DIR = os.path.join('..', '{{cookiecutter.repo_name}}', PROJECT_DIR)
        test_mode = True
    else:
        context = ast.literal_eval(COOKIE_CONTEXT)
        PROJECT_DIR = os.path.join('.', PROJECT_DIR)

    print_part_title("Enable mods")
    apm = AppManager(context, PROJECT_DIR, test_mode)
    apps = apm.get_enabled_apps()
    apm.enable_mods(apps)
    print

    print_part_title("Store context")
    store_project_context(context, PROJECT_DIR, test_mode)
    print

    print_part_title("Init Git repository")
    repository_path = repository_init(context, PROJECT_DIR, test_mode)
    print

    print_part_title("Go ahead")
    print "Your new project should be ready now."
    print
    print "Just enter in '{{cookiecutter.repo_name}}' directory then launch following command to install it:"
    print
    print "    make install"
    print
    print "The project repository has been initialized, committed and configured for origin remote on:"
    print
    print "   ", repository_path
    print
    print "Create its repository on your host server then push it with:"
    print
    print "    git push origin master"
    print
