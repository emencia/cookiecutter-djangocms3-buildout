/*
jQuery plugin to hide targeted images in DOM then add them as image background on
their parent, so for example :

     <p><img src="foo.jpg" class="background">Hello world</p>

With :

     $('img.background').swapImageToBackground();

Will become :

     <p class="with-background" style="background-image: url(foo.jpg);">
         <img src="foo.jpg class="background" data-imgbg-status="processed" style="display:none;">
     Hello world</p>

Additionally some 'data-*' attributes can be used to modify some behaviors:

data-imgbg-position
     To define 'background-position' on parent

data-imgbg-enforce_height
     Apply a minimal height on container, the height value will be taken from the
     image height in its current display.

data-imgbg-repeat
     To define 'background-repeat' on parent

data-imgbg-size
     To define 'background-size' on parent

data-imgbg-vacuum
     To remove image element when it has been processed,
     just add it anything like 'data-imgbg-vacuum="true"'
*/
(function ( $ ) {

/*
* Plugin extensions calling logic
*/
$.fn.swapImageToBackground = function(method) {
    // Specific public method called
    if ( extensions[method] ) {
        return extensions[method].apply( this, Array.prototype.slice.call( arguments, 1 ));
    // Default public method to init the plugin
    } else if ( typeof method === 'object' || ! method ) {
        return extensions.init.apply( this, arguments );
    // Unknow called method
    } else {
        $.error( 'Method ' +  method + ' does not exist on jQuery.swapImageToBackground' );
    }
};

/*
* Plugin extension methods
*/
var extensions = {
    /*
    * Initialize plugin, default public method, must be called first
    */
    init : function(options) {
        return this.each(function() {
            var $this = $(this);

            // Default action is to apply background swap
            $this.swapImageToBackground('swap', options);
        });
    },

    /*
    * Apply background swapping
    */
    swap : function(options) {
        return this.each(function(){
            var $image = $(this),
                // Settings default can come from element attributes, will be overriden by passed settings if any
                settings = $.extend( {
                    "position": $image.attr('data-imgbg-position') || null,
                    "repeat": $image.attr('data-imgbg-repeat') || null,
                    "size": $image.attr('data-imgbg-size') || null,
                    "enforce_height": $image.attr('data-imgbg-enforce_height') || null
                }, options),
                url = $image.attr('src'),
                css_opts = {"background-image": "url('"+url+"')"};

                if(settings.position) css_opts['background-position'] = settings.position;
                if(settings.repeat) css_opts['background-repeat'] = settings.repeat;
                if(settings.size) css_opts['background-size'] = settings.size;

                if(settings.enforce_height){
                    css_opts['min-height'] = $image.height();
                }

                $image.css({'display': 'none'}).attr('data-imgbg-status', 'processed').parent().css(css_opts).addClass('with-background');
                if($image.attr('data-imgbg-vacuum')){
                    $image.remove();
                }
        });
    },

    /*
     * Refresh min-height from background image
     *
     * NOTE: You should use this method only from a resize event, prefer to use
     *       a "debounced resize" instead of original one that will perform
     *       resizing for each pixel between start size and destination size.
     */
    resize_height: function(options) {
        return this.each(function(options){
            var $image = $(this),
                settings = $.extend( {
                    "enforce_height": $image.attr('data-imgbg-enforce_height') || null
                }, options);

            if(settings.enforce_height){
                $image.parent().css('min-height', $image.height());
            }
        });
    }
};

}( jQuery ));