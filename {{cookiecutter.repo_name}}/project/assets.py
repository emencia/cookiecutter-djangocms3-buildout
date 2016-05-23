"""
Available and enabled assets bundles for this project

It uses 'nested bundles' technic in the 'main available bundles' to regroup
app bundles into a single file.

Commonly we don't use Asset bundle for CSS because regrouping is often managed
with Compass.
"""
from django_assets import Bundle, register


"""
BASE BUNDLES, contains common app/components bundles, do not register your
main bundles here. However you can comment/uncomment some app files for your
needs.
"""
AVALAIBLE_BUNDLES = {
    # App bundle for Modernizr, compatible for all Foundation releases
    'app_modernizr_js': Bundle(
        "js/foundation5/vendor/modernizr.js",
        filters='yui_js',
        output='js/modernizr.%(version)s.js'
    ),

    # App bundle for Foundation5
    'app_foundation5_js': Bundle(
        "js/foundation5/vendor/jquery.js",
        #"js/foundation5/vendor/fastclick.js", # for Foundation development
        #"js/foundation5/vendor/lodash.js", # for Foundation development
        #"js/foundation5/vendor/jquery.placeholder.js", # for Foundation development
        "js/foundation5/vendor/jquery.cookie.js",
        "js/foundation5/foundation/foundation.js",
        "js/foundation5/foundation/foundation.abide.js",
        "js/foundation5/foundation/foundation.accordion.js",
        "js/foundation5/foundation/foundation.alert.js",
        "js/foundation5/foundation/foundation.clearing.js",
        "js/foundation5/foundation/foundation.dropdown.js",
        #"js/foundation5/foundation/foundation.equalizer.js",
        "js/foundation5/foundation/foundation.interchange.js",
        "js/foundation5/foundation/foundation.joyride.js",
        "js/foundation5/foundation/foundation.magellan.js",
        "js/foundation5/foundation/foundation.offcanvas.js",
        "js/foundation5/foundation/foundation.reveal.js",
        "js/foundation5/foundation/foundation.slider.js",
        "js/foundation5/foundation/foundation.tab.js",
        "js/foundation5/foundation/foundation.tooltip.js",
        "js/foundation5/foundation/foundation.topbar.js",
        filters='yui_js',
        output='js/app_foundation5.%(version)s.js'
    ),

    # App bundle for Pikaday jquery plugin (a datepicker) and optional
    # jquery.timepicker (a timepicker)
    'app_pikaday_js': Bundle(
        "js/pikaday/pikaday.js",
        "js/pikaday/pikaday.jquery.js",
        #"js/pikaday/jquery.timepicker.js",
        filters='yui_js',
        output='js/app_pikaday.%(version)s.js'
    ),
}


"""
MAIN AVAILABLE BUNDLES, this is where you will register your main Asset bundles
"""
AVALAIBLE_BUNDLES.update({
    # Main CSS bundle
    'main_css': Bundle(
        # Flag CSS map, only usefull for multilingual projects
        'css/flags.css',

        # Main CSS
        'css/app.css',

        filters='yui_css',
        output='css/app.%(version)s.css'
    ),

    # JAVASCRIPT bundle common main frontend script
    'main_js': Bundle(
        # Foundation5 bundle
        AVALAIBLE_BUNDLES['app_foundation5_js'],

        ## Debounce event from jquery-smartresize
        #"js/jquery/jquery.debouncedresize.js",

        ## Throttling event from jquery-smartresize
        #"js/jquery/jquery.throttledresize.js",

        # Image swapping plugin
        "js/jquery/jquery.image-swapper.js",

        # equalize.js library
        "js/jquery/equalize.js",

        # Jquery FitVids library
        #"js/jquery/jquery.fitvids.js",

        # Pikaday bundle with Moment.js script
        #"js/jquery/moment.js",
        #AVALAIBLE_BUNDLES['app_pikaday_js'],

        # Magnific popup library
        #"js/jquery/magnific-popup.js",

        # Slick.js library
        "js/jquery/slick.js",

        # Emencia Cookie Law plugin
        "js/cookie_law/cookie_law.js",

        # Some common various addons you can use
        "js/jquery/addons.js",

        # Main frontend script where you should launch/init/configure all used
        # libraries from bundles
        "js/app.js",

        filters='yui_js',
        output='js/app.%(version)s.js'
    ),
})


"""
ENABLE NEEDED BUNDLE HERE, only these bundles will be used
"""
ENABLED_BUNDLES = [
    'app_modernizr_js',
    'main_css',
    'main_js',
]

# Registering your enabled bundles, don't matter about this
for item in ENABLED_BUNDLES:
    register(item, AVALAIBLE_BUNDLES[item])
