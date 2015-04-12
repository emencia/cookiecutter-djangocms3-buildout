/*
 * All stuff used by the webapp, it is separated from "foundation/apps.js" so it can 
 * be used elsewhere without Foundation stuff, like the Django admin where Foundation 
 * does not reside.
 */
;(function($) {
    'use strict';
  
    /*
     * Hide targeted images in DOMn then add it as an image background on 
     * their parent, so for example :
     * 
     *      <p><img src="foo.jpg class="swap">Hello world</p>"
     * 
     * With :
     * 
     * $('.wrap').swapImageToBackground();
     * 
     * Will become :
     * 
     *      <p class="with-background" style="background-image: url(foo.jpg);"><img src="foo.jpg class="swap" style="display:none;">Hello world</p>
     * 
     * Also some data-*-* attributes can be used to add some CSS properties to the parent :
     * 
     * - data-imgbg-position for background-position
     * - data-imgbg-repeat for background-repeat
     * - data-imgbg-size for background-size
     */
    $.fn.swapImageToBackground = function() {
        return this.each(function() {
            var $this = $(this),
                url = $this.attr('src'),
                position = $this.attr('data-imgbg-position') || null,
                repeat = $this.attr('data-imgbg-repeat') || null,
                size = $this.attr('data-imgbg-size') || null,
                css_opts = {"background-image": "url('"+url+"')"};
                
                if(position) css_opts['background-position'] = position;
                if(repeat) css_opts['background-repeat'] = repeat;
                if(size) css_opts['background-size'] = size;
                
                $this.css({'display': 'none'}).parent().css(css_opts).addClass('with-background');
                $this.remove();
        });
    };
}( jQuery ));

/*
 * Common method to init all equalize rules in a one shot
 * 
 * Needed to be called in the $.load(), because webkit raise ready() even if it have 
 * not download all ressources, this cause false dimensions because all images 
 * have not yet be downloaded, so they doesn't set true dimensions on their 
 * parent and etc..
 */
function column_equalizer(){
    // Equalize content text columns to the same height
    $('.equal-heights').equalize({'equalize':'outerHeight', children: '.equalized-item', reset: true, breakpoint: 750});
    return;
}
