# -*- coding: utf-8 -*-

INSTALLED_APPS = add_to_tuple(INSTALLED_APPS, 'slideshows')

# Available templates to display a slideshow
SLIDESHOWS_TEMPLATES = (
    ("slideshows/slides_show/default.html", "Slider default"),
    ("slideshows/slides_show/royalslider.html", "Royal slider"),
    ("slideshows/slides_show/interchange.html", "Interchange (for cms plugin only)"),
)

# Available config file to initialize your slideshow Javascript stuff
# (Paths are relative to a templates directory)
SLIDESHOWS_CONFIGS = (
    ("slideshows/slides_show/configs/default.html", "Slider default"),
    ("slideshows/slides_show/configs/fade_slider.html", "Slider with fade"),
)

# Available templates for "random slide" mode
SLIDESHOWS_RANDOM_SLIDE_TEMPLATES = (
    ("slideshows/random_slide/default.html", "Random image default"),
    ("slideshows/random_slide/interchange.html", "Interchange (for cms plugin only)"),
)

# Default templates to use in admin forms
DEFAULT_SLIDESHOWS_TEMPLATE = SLIDESHOWS_TEMPLATES[0][0]
DEFAULT_SLIDESHOWS_CONFIG = ""
DEFAULT_SLIDESHOWS_RANDOM_SLIDE_TEMPLATE = SLIDESHOWS_RANDOM_SLIDE_TEMPLATES[0][0]
