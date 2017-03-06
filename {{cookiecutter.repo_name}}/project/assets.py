"""
Available and enabled assets bundles for this project

It uses 'nested bundles' technic in the main available bundles to package
app bundles into a single file.

NOTE: For sanity, remember to add a line in Makefile 'assets' action for each
      leading bundle to remove their previous minification file (*.min.*).
"""
from django_assets import Bundle, register

# Register custom webasset filter for RCssMin minifier
from webassets.filter import register_filter
from project.utils.rcssmin_webassets_filter import RCSSMin
register_filter(RCSSMin)


# Available base bundles contains common app/components bundles, do not
# register your main bundles here. However you can comment/uncomment some app
# files for your needs.
AVALAIBLE_BUNDLES = {
    # App bundle for Modernizr, compatible for all Foundation releases
    'app_modernizr_js': Bundle(
        "js/foundation5/vendor/modernizr.js",
        filters='closure_js',
        output='js/modernizr.%(version)s.js'
    ),

    'foundation6_js': Bundle(
        "js/foundation/vendor/jquery.js",
        #"js/foundation/vendor/motion-ui.js",
        "js/foundation/vendor/what-input.js",
        'js/foundation/plugins/foundation.core.js',
        'js/foundation/plugins/foundation.util.box.js',
        'js/foundation/plugins/foundation.util.keyboard.js',
        'js/foundation/plugins/foundation.util.mediaQuery.js',
        'js/foundation/plugins/foundation.util.motion.js',
        'js/foundation/plugins/foundation.util.nest.js',
        'js/foundation/plugins/foundation.util.timerAndImageLoader.js',
        'js/foundation/plugins/foundation.util.touch.js',
        'js/foundation/plugins/foundation.util.triggers.js',
        'js/foundation/plugins/foundation.abide.js',
        'js/foundation/plugins/foundation.accordion.js',
        'js/foundation/plugins/foundation.accordionMenu.js',
        'js/foundation/plugins/foundation.drilldown.js',
        'js/foundation/plugins/foundation.dropdown.js',
        'js/foundation/plugins/foundation.dropdownMenu.js',
        'js/foundation/plugins/foundation.equalizer.js',
        'js/foundation/plugins/foundation.interchange.js',
        'js/foundation/plugins/foundation.magellan.js',
        'js/foundation/plugins/foundation.offcanvas.js',
        'js/foundation/plugins/foundation.orbit.js',
        'js/foundation/plugins/foundation.responsiveMenu.js',
        'js/foundation/plugins/foundation.responsiveToggle.js',
        'js/foundation/plugins/foundation.reveal.js',
        'js/foundation/plugins/foundation.slider.js',
        'js/foundation/plugins/foundation.sticky.js',
        'js/foundation/plugins/foundation.tabs.js',
        'js/foundation/plugins/foundation.toggler.js',
        'js/foundation/plugins/foundation.tooltip.js',
        'js/foundation/plugins/foundation.zf.responsiveAccordionTabs.js',
        filters='closure_js',
        output='js/foundation6.min.js'
    ),

    # App bundle for Pikaday jquery plugin (a datepicker) and optional
    # jquery.timepicker (a timepicker)
    'app_pikaday_js': Bundle(
        "js/pikaday/pikaday.js",
        "js/pikaday/pikaday.jquery.js",
        # "js/pikaday/jquery.timepicker.js",
        filters='closure_js',
        output='js/app_pikaday.%(version)s.js'
    ),
}


"""
MAIN AVAILABLE BUNDLES, this is where you will register your main Asset bundles
"""
AVALAIBLE_BUNDLES.update({
    # Main CSS bundle
    'main_css': Bundle(
        'css/app.css',

        filters='rcssmin',
        output='css/app.%(version)s.css'
    ),

    # Javascript bundle for common main frontend script
    'main_js': Bundle(
        # Foundation5 bundle
        AVALAIBLE_BUNDLES['foundation6_js'],

        # Debounce event from jquery-smartresize
        # "js/jquery/jquery.debouncedresize.js",

        # Throttling event from jquery-smartresize
        # "js/jquery/jquery.throttledresize.js",

        # Cookieconsent plugin
        "js/jquery/cookieconsent.js",

        # Image swapping plugin
        "js/jquery/jquery.image-swapper.js",

        # equalize.js library
        "js/jquery/equalize.js",

        # Jquery FitVids library
        # "js/jquery/jquery.fitvids.js",

        # Pikaday bundle with Moment.js script
        # "js/jquery/moment.js",
        # AVALAIBLE_BUNDLES['app_pikaday_js'],

        # Magnific popup library
        # "js/jquery/magnific-popup.js",

        # Slick.js library
        "js/jquery/slick.js",

        # Some common various addons you can use
        "js/jquery/addons.js",

        # Main frontend script where you should launch/init/configure all used
        # libraries from bundles
        "js/app.js",

        filters='closure_js',
        output='js/app.%(version)s.js'
    ),
})


"""
Enable needed bundle here, only these bundles will be builded
"""
ENABLED_BUNDLES = [
    'app_modernizr_js',
    'main_css',
    'main_js',
]

# Registering your enabled bundles, don't matter about this
for item in ENABLED_BUNDLES:
    register(item, AVALAIBLE_BUNDLES[item])
