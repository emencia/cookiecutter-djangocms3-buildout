"""
Available and enabled assets bundles for this project

This use 'nested bundles' technic in the 'main available bundles' to regroup 
app bundles into single files.
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
        # For Orbit Slider (default used)
        "js/foundation5/foundation/foundation.orbit.js",
        filters='yui_js',
        output='js/app_foundation5.%(version)s.js'
    ),
    
    # App bundle for RoyalSlider instead of Orbit (remember to enable its foundation 
    # component in your js app')
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
    
    # App bundle for SocialAggregator
    'app_socialaggregator_js': Bundle(
        "js/masonry/masonry.pkgd.js",
        "js/socialaggregator.js",
        filters='yui_js',
        output='js/app_socialaggregator.%(version)s.js'
    ),
    
    # App bundle for Pikaday jquery plugin (a datepicker)
    'app_pikaday_js': Bundle(
        "js/pikaday.js",
        "js/jquery/pikaday.jquery.js",
        filters='yui_js',
        output='js/app_pikaday.%(version)s.js'
    ),
}
    

"""
MAIN AVAILABLE BUNDLES, this is where you will register main bundles
"""
AVALAIBLE_BUNDLES.update({
    # CSS bundle For Foundation5
    'main_css': Bundle(
        'css/flags.css',
        'css/app.css',
        filters='yui_css',
        output='css/app.%(version)s.css'
    ),
    
    # Javascript bundle For Foundation5
    'main_js': Bundle(
        AVALAIBLE_BUNDLES['app_foundation5_js'],
        "js/jquery/equalize.js",
        #AVALAIBLE_BUNDLES['app_royalslider_js'],
        #"js/moment.js",
        "js/jquery/magnific-popup.js", # Magnific popup (modal window/pop-in)
        AVALAIBLE_BUNDLES['app_socialaggregator_js'],
        #AVALAIBLE_BUNDLES['app_pikaday_js'],
        "js/jquery/addons.js",
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
