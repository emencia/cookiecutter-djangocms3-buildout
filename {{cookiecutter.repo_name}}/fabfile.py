from fabric.api import task, hosts, cd, sudo
from fabtools.require.git import working_copy
from fabtools.python import virtualenv

PATH = '~{{ cookiecutter.deploy_user }}/{{ cookiecutter.repo_name }}'
USER = '{{ cookiecutter.deploy_user }}'
DEV_HOST = '{{ cookiecutter.deploy_host }}'
PROD_HOST = '{{ cookiecutter.prod_host }}'
REPO_URI = 'git@{{ cookiecutter.repo_host }}:{{ cookiecutter.repo_username }}/{{ cookiecutter.repo_name }}.git' # noqa
CONF_NAME = "{{ cookiecutter.repo_name }}.conf"


@hosts(PROD_HOST)
@task
def install_prod():
    """To install"""
    with cd("~%s" % USER):
        working_copy(REPO_URI, use_sudo=True, user=USER)
    with cd(PATH):
        sudo('make install_production', user=USER)
        with virtualenv('.'):
            sudo('make assets', user=USER)
        sudo('ln -s %s/etc/nginx.conf /etc/nginx/sites-enabled/%s' %
             (PATH, CONF_NAME))
        sudo('ln -s %s/etc/monit.conf /etc/monit/conf.d/%s' %
             (PATH, CONF_NAME))
        sudo('service nginx reload')
        sudo('monit reload')


@hosts(PROD_HOST)
@task
def deploy_prod():
    """To deploy"""
    import sys
    sys.path.append('')
    from project import __version__
    with cd(PATH):
        with virtualenv('.'):
            sudo('git fetch', user=USER)
            sudo('git checkout %s' % __version__, user=USER)
            sudo('make build_production', user=USER)
            sudo('make delpyc', user=USER)
            sudo('django-instance migrate --no-initial-data', user=USER)
            sudo('make assets', user=USER)
            sudo('make reload', user=USER)
    sudo('service nginx reload')


@hosts(DEV_HOST)
@task
def install_dev():
    """To install"""
    with cd("~%s" % USER):
        working_copy(REPO_URI, use_sudo=True, user=USER)
    with cd(PATH):
        sudo('make install_integration', user=USER)
        with virtualenv('.'):
            sudo('make assets', user=USER)
        sudo('ln -s %s/etc/nginx.conf /etc/nginx/sites-enabled/%s' %
             (PATH, CONF_NAME))
        sudo('ln -s %s/etc/monit.conf /etc/monit/conf.d/%s' %
             (PATH, CONF_NAME))
        sudo('service nginx reload')
        sudo('monit reload')


@hosts(DEV_HOST)
@task
def deploy_dev():
    """To deploy"""
    with cd(PATH):
        with virtualenv('.'):
            sudo('git pull', user=USER)
            sudo('make build_integration', user=USER)
            sudo('make delpyc', user=USER)
            sudo('django-instance migrate --no-initial-data', user=USER)
            sudo('make assets', user=USER)
            sudo('make reload', user=USER)
    sudo('service nginx reload')
