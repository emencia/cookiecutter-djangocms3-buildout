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
};

/*
 * MegaMenu default usage
 *
 * Attempt argument 'megamenu_container' that should be jQuery selector like:
 * 
 *     LeftMegaMenu($("#navabsleft"));
 *
 * The selector should point to the menu generated from MegaMenu 
 * (usually '#navabsleft'), not the one that was used to trigger and build the 
 * displayed menu
 */
function LeftMegaMenu(megamenu_container) {
    megamenu_container.css('height','auto' );

    if (megamenu_container) {
        var block = [],
            totalHeight = 0,
            totalnavHeight = 0,
            innerblock = [];
        $( ".sectioninner" ).each(function( index ) {
            $('.sectioninner').height('auto');
            block.push($(this).height());
        });
        for (var i  = 0; i < block.length; i++) {
            totalHeight = totalHeight + block[i];
        }

    }

    if (megamenu_container.length > 0) {
        if (megamenu_container.height()< totalHeight) {
            megamenu_container.height(totalHeight);
        }
        megamenu_container.css('left',$('#posNavLeft').position().left+'px' );

        megamenu_container.css('max-height',totalHeight+'px' );

        megamenu_container.css('width',$('#posNavLeft').width()+'px' );

        megamenu_container.nextAll().each(function( index ) {
            innerblock.push($(this).outerHeight()+ parseInt($(this).css('margin-top'))+ parseInt($(this).css('margin-bottom')));
        });

        for (var i  = 0; i < innerblock.length; i++) {
            totalnavHeight = totalnavHeight + innerblock[i];
        }
        if (totalnavHeight > totalHeight) {
            megamenu_container.css('max-height',totalnavHeight+'px' );
            $('.sectioninner').height(totalnavHeight);
        }
    }
};


/*
 * Use html attribute to add links on elements without to use 
 * real <a> href attribute
 */
function AddLinkFromAttribute(options) {
    $('*[data-link]').click(function(event) {
        window.location.href = $(this).attr('data-link');
        event.preventDefault();
    });
};
