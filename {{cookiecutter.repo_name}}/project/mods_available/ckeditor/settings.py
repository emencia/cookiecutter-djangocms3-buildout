# -*- coding: utf-8 -*-
import os

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'ckeditor', 'djangocms_text_ckeditor', before='cms')

STATICFILES_DIRS += ( os.path.join(MOD_FILE, "static"),)
TEMPLATE_DIRS += (os.path.join(MOD_FILE, "templates"),)

# Defining CKEDITOR configs, note that django_ckeditor use CKEDITOR_CONFIGS 
# settings but cmsplugin_ckeditor use CKEDITOR_SETTINGS so we must mirroring it
CKEDITOR_CONFIGS = CKEDITOR_SETTINGS = {
    'language': '{{ language }}',
    'toolbar': 'CMS',
    'skin': 'moono',
    'toolbarCanCollapse': False,
    'contentsCss': "/static/css/ckeditor.css",
    # To enable showblocks on editor start without to use a button
    'startupOutlineBlocks': True,
    # Disable element filter to enable full HTML5, also this will let 
    # append any code, even bad syntax and malicious code, so be careful
    "removePlugins": "stylesheetparser",
    "allowedContent": True,
    # Enable some plugins
    'extraPlugins': 'cmsplugins,codemirror,blockquote,div,justify,showblocks,templates',
    # Justify text using foundation's dedicated class names
    'justifyClasses': [ 'text-left', 'text-center', 'text-right', 'AlignJustify' ],
    # Uncheck the checkbox that replace whole content with the selected template (if any)
    'templates_replaceContent': False,
    # Link to use for the link "Browse server"
    'filebrowserBrowseUrl': "/admin/filebrowser/browse?pop=3",
    # URLs for Javascripts that define content templates
    'templates_files': [
        '/ckeditor/editor_site_templates.js'
    ],
    
    # Available toolbars
    'toolbar_CMS': [
        ['Undo', 'Redo'],
        ['cmsplugins', '-', 'ShowBlocks'],
        ['Format', 'Styles'],
        ['RemoveFormat', '', '', '', ''],
        ['Maximize', ''],
        '/',
        ['Source', '-', 'searchCode', 'autoFormat', '-', 'CommentSelectedRange', 'UncommentSelectedRange', '', ''],
        '/',
        ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '', ''],
        ['JustifyLeft', 'JustifyCenter', 'JustifyRight', '', '', '', ''],
        ['Link', 'Unlink'],
        ['Image', '-', 'NumberedList', 'BulletedList', '-', 'Table', '-', 'CreateDiv', 'HorizontalRule', 'SpecialChar', '-', 'Templates'],
        # , 'Iframe' # Disabled because djangocms seems to sanitize it from the posted HTML
    ],
    # Zinnia use a contained toolbar that does not herit from defaults, so we much mirror them
    'zinnia-content': {
        # Wider editor
        'width': '100%',
        'height': 400,
        
        'toolbar': 'Zinnia',
        'toolbar_Zinnia': [
            ['Undo', 'Redo'],
            ['Format', 'Styles', '-', 'ShowBlocks'],
            ['RemoveFormat', '', '', '', ''],
            '/',
            ['Maximize', ''],
            '/',
            ['Source', '-', 'searchCode', 'autoFormat', '-', 'CommentSelectedRange', 'UncommentSelectedRange', '', ''],
            '/',
            ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '', ''],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', '', '', '', ''],
            ['Link', 'Unlink'],
            ['Image', '-', 'NumberedList', 'BulletedList', '-', 'Table', '-', 'CreateDiv', 'HorizontalRule', 'SpecialChar', '-', 'Templates'],
            # , 'Iframe' # Disabled because djangocms seems to sanitize it from the posted HTML
        ],
        'contentsCss': "/static/css/ckeditor.css",
        'startupOutlineBlocks': True,
        "removePlugins": "stylesheetparser",
        "allowedContent": True,
        'extraPlugins': 'blockquote,codemirror,div,justify,magicline,showblocks,templates',
        'justifyClasses': [ 'text-left', 'text-center', 'text-right', 'AlignJustify' ],
        'templates_replaceContent': False,
        'filebrowserBrowseUrl': "/admin/filebrowser/browse?pop=3",
        'templates_files': [
            '/ckeditor/editor_site_templates.js'
        ],
    },
}

CKEDITOR_UPLOAD_PATH = "uploads/"
# Relative path to the content templates
CKEDITOR_EDITOR_TEMPLATES_PATH = "ckeditor/editor-site-templates/"
# Relative path to image thumbnails for content template visuals
CKEDITOR_EDITOR_TEMPLATES_IMAGES_PATH = "ckeditor/editor-site-templates/"
# Filepath for content templates manifest, this is relative to CKEDITOR_EDITOR_TEMPLATES_PATH
CKEDITOR_EDITOR_TEMPLATES_NAMES_FILE = "manifest.json"
# Template string for Javascript that inject template definition
CKEDITOR_EDITOR_JS_TEMPLATE = u"""CKEDITOR.addTemplates( 'default', {{imagesPath:"{imagespath}", templates: {json_list}}});"""
