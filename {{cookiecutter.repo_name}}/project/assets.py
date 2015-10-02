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
        # For Orbit Slider (deprecated)
        #"js/foundation5/foundation/foundation.orbit.js",
        filters='yui_js',
        output='js/app_foundation5.%(version)s.js'
    ),
    
    # App bundle for RoyalSlider instead of Orbit (remember to enable its foundation 
    # component in your js app and scss')
    'app_royalslider_js': Bundle(
        "js/royalslider/dev/jquery.royalslider.js",
        "js/royalslider/dev/modules/jquery.rs.video.js",
        "js/royalslider/dev/modules/jquery.rs.thumbnails.js",
        "js/royalslider/dev/modules/jquery.rs.auto-height.js",
        "js/royalslider/dev/modules/jquery.rs.deeplinking.js",
        "js/royalslider/dev/modules/jquery.rs.fullscreen.js",
        "js/royalslider/dev/modules/jquery.rs.animated-blocks.js",
        "js/royalslider/dev/modules/jquery.rs.autoplay.js",
        "js/royalslider/dev/modules/jquery.rs.global-caption.js",
        "js/royalslider/dev/modules/jquery.rs.visible-nearby.js",
        "js/royalslider/dev/modules/jquery.rs.tabs.js",
        "js/royalslider/dev/modules/jquery.rs.nav-auto-hide.js",
        "js/royalslider/dev/modules/jquery.rs.autoplay.js",
        "js/royalslider/dev/modules/jquery.rs.bullets.js",
        "js/royalslider/dev/modules/jquery.rs.active-class.js",
        filters='yui_js',
        output='js/app_royalslider.%(version)s.js'
    ),

    # App bundle for jQuery.mmenu plugin
    'mmenu_js': Bundle(
        "js/mmenu/jquery.mmenu.oncanvas.js",
        "js/mmenu/addon/jquery.mmenu.offcanvas.js",
        "js/mmenu/addon/jquery.mmenu.buttonbars.js",
        "js/mmenu/addon/jquery.mmenu.counters.js",
        "js/mmenu/addon/jquery.mmenu.dragopen.js",
        "js/mmenu/addon/jquery.mmenu.fixedelements.js",
        "js/mmenu/addon/jquery.mmenu.footer.js",
        "js/mmenu/addon/jquery.mmenu.header.js",
        "js/mmenu/addon/jquery.mmenu.searchfield.js",
        "js/mmenu/addon/jquery.mmenu.toggles.js",

        filters='yui_js',
        output='js/mmenu.min.js'
    ),
    
    # App bundle for SocialAggregator
    'app_socialaggregator_js': Bundle(
        "js/masonry/masonry.pkgd.js",
        "js/jquery/socialaggregator.js",
        filters='yui_js',
        output='js/app_socialaggregator.%(version)s.js'
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
        
        # equalize.js library
        "js/jquery/equalize.js",
        
        # Jquery FitVids library
        #"js/jquery/jquery.fitvids.js",
        
        # Pikaday bundle with Moment.js script
        #"js/jquery/moment.js",
        #AVALAIBLE_BUNDLES['app_pikaday_js'],
        
        # RoyalSlider bundle
        #AVALAIBLE_BUNDLES['app_royalslider_js'],
        
        # jQuery.mmenu bundle
        #AVALAIBLE_BUNDLES['mmenu_js'],
        
        # Magnific popup library
        #"js/jquery/magnific-popup.js",
        
        # SocialAggregator bundle
        {% if cookiecutter.enable_socialaggregator != 'yes' %}#{% endif %}AVALAIBLE_BUNDLES['app_socialaggregator_js'],
        
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
