# -*- coding: utf-8 -*-
INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 
    'slideshows',
    'cmsplugin_slideshows',
)

# Available templates to display a slideshow
SLIDESHOWS_TEMPLATES = (
    ("slideshows/slides_show/default.html", "Slider default"),
    ("slideshows/slides_show/royalslider.html", "Royal slider"),
)

# Available config file to initialize your slideshow Javascript stuff
# (Paths are relative to a templates directory)
SLIDESHOWS_CONFIGS = (
    ("slideshows/slides_show/configs/default.html", "Slider default"),
)

# Available templates for "random slide" mode
SLIDESHOWS_RANDOM_SLIDE_TEMPLATES = (
    ("slideshows/random_slide/default.html", "Random image default"),
)

# Default templates to use in admin forms
DEFAULT_SLIDESHOWS_TEMPLATE = SLIDESHOWS_TEMPLATES[0][0]
DEFAULT_SLIDESHOWS_CONFIG = ""
DEFAULT_SLIDESHOWS_RANDOM_SLIDE_TEMPLATE = SLIDESHOWS_RANDOM_SLIDE_TEMPLATES[0][0]
