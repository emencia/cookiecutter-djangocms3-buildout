# -*- coding: utf-8 -*-
from project.mods_enabled.ckeditor.views import EditorTemplatesListView

urlpatterns = patterns('',
    (r'^ckeditor/', include('ckeditor.urls')),
    url(r'^ckeditor/editor_site_templates.js$', EditorTemplatesListView.as_view(), name="ckeditor-editor-site-templates"),
) + urlpatterns
