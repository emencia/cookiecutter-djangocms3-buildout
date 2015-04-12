# -*- coding: utf-8 -*-
"""
Enable and define customization for the `CKEditor`_ editor. It is enabled by default and used by `Django CKEditor`_ in the `cms`_ mod, and also in `zinnia`_.

Note that DjangoCMS use it's own app named "djangocms_text_ckeditor", a djangocms plugin to use CKEditor (4.x).

But Zinnia (and some other generic app) use "django_ckeditor" that ship the same ckeditor but without cms addons.

This mod contains configuration for all of them.

And some useful patches/fixes :

* the codemirror plugin that is missing from the ckeditor's django apps;
* A system to use the "template" plugin (see views.EditorTemplatesListView for more usage details);
* Some overriding to have content preview and editor more near to Foundation;
"""