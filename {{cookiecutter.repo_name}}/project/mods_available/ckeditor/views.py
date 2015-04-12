# -*- coding: utf-8 -*-
"""
Views to customize CKEditor

These views are for admin staff only, we don't want to expose them.
"""
import os, json

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import redirect_to_login
from django.core.urlresolvers import reverse
from django.views.generic import View, TemplateView
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, Http404

class StaffuserRequiredMixin(object):
    """
    Mixin allows you to require a user with `is_staff` set to True.
        
    Taken from django-braces
    """
    login_url = settings.LOGIN_URL  # LOGIN_URL from project settings
    raise_exception = False  # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME  # Set by django.contrib.auth

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:  # If the request's user is not staff,
            if self.raise_exception:  # *and* if an exception was desired
                raise PermissionDenied  # return a forbidden response
            else:
                return redirect_to_login(request.get_full_path(),
                                         self.login_url,
                                         self.redirect_field_name)

        return super(StaffuserRequiredMixin, self).dispatch(request,
            *args, **kwargs)

class EditorTemplatesListView(StaffuserRequiredMixin, View):
    """
    Recursively list all HTML file in settings.CKEDITOR_EDITOR_TEMPLATES_PATH 
    that didn't start with "_" and return the list in a Javascript file :
    
        // Register a templates definition set named "default".
        CKEDITOR.addTemplates( 'default', {
            // The name of sub folder which hold the shortcut preview images of the
            // templates.
            imagesPath: '/static/ckeditor/editor-site-templates/',

            // The templates definitions.
            templates: [
                {
                    title: 'Grid row',
                    image: 'grid_row.gif',
                    description: 'Sample',
                    html: '<div class="row"></div>'
                }
            ]
        }
    
    The Django template loading behaviors should be preserved, so you can overrides them 
    within multiple TEMPLATE_DIRS. Prefix your file names with "_" for included 
    templates that you don't want to see in the editor templates list.
    
    On the root of the settings.CKEDITOR_EDITOR_TEMPLATES_PATH directory, 
    should resides a "manifest.json" file that contain a map to your content templates to 
    declare their optionnal title and description. When a content template has no 
    declared title it take his relative path as title, and the default description is 
    "No description".
    
    Your "manifest.json" file should look like :
    
        {
            "foo.html": {
                "title": "Dummy",
                "image": "grid_row.gif",
                "description": "Dummy template for testing"
            }
        }
        
    The template HTML is taken from the template filename given at the key name.
    
    Take care to make valid JSON, else this will raise exception. Also note that content 
    templates are indexed on their relative path.
    """
    def get(self, request, *args, **kwargs):
        imagespath = os.path.join(settings.STATIC_URL, settings.CKEDITOR_EDITOR_TEMPLATES_IMAGES_PATH)
        return HttpResponse(
                    settings.CKEDITOR_EDITOR_JS_TEMPLATE.format(imagespath=imagespath, json_list=json.dumps(self.get_templates(), indent=4)),
                    content_type="application/javascript"
                )
    
    def get_templates(self):
        manifest, paths = {}, []
        TPL_OBJ = {
            'title': 'Dummy title',
            'image': '',
            'description': '',
            'html': 'Empty'
        }
        
        # Perform scanning on all knowed templates directory
        for dir in settings.TEMPLATE_DIRS:
            templates_dir = os.path.join(dir, settings.CKEDITOR_EDITOR_TEMPLATES_PATH)
            if os.path.exists(templates_dir):
                # Trying to find the optional manifest JSON file that describes templates
                manifest_file = os.path.join(templates_dir, settings.CKEDITOR_EDITOR_TEMPLATES_NAMES_FILE)
                if os.path.exists(manifest_file):
                    manifest.update(json.load(open(manifest_file, 'r')))
                
                for root, dirs, files in os.walk(templates_dir):
                    
                    for name in files:
                        if not name.startswith('_') and name.endswith('.html'):
                            item_obj = TPL_OBJ.copy()
                            absolute = os.path.join(root, name)
                            relative = os.path.relpath(absolute, templates_dir)
                            # Default content
                            item_obj['title'] = name
                            # Get the HTML content
                            fp = open(absolute, "r")
                            item_obj['html'] = fp.read()
                            fp.close()
                            # If the entry is defined in the manifest
                            if relative in manifest:
                                item_obj['title'] = manifest[relative].get('title') or item_obj['title']
                                item_obj['description'] = manifest[relative].get('description') or item_obj['description']
                                item_obj['image'] = manifest[relative].get('image') or item_obj['image']
                                
                                paths.append(item_obj)
        
        return paths
        