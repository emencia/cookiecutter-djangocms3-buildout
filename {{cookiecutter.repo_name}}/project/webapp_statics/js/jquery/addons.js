;(function($) {
    'use strict';

    /*
    * Find current media query to display it in a container
    *
    * - The last matched media query is the current one;
    * - Require debounce event from jquery-smartresize library;
    * - Should be ready to use in your template and app.js;
    * - Should be only enabled when Django debug mode is on;
    * - Can be hided/displayed again using "SHIFT+M";
    */
    // Init key shortcut (SHIFT+M) to show/hide container
    $.fn.initCurrentMediaQuery = function(options) {
        return this.each(function() {
            var $container = $(this);
            $(document).keydown(function( event ) {
                if ( event.which == 13 ) {
                    event.preventDefault();
                } else if ( event.which == 77 && event.shiftKey == true && event.ctrlKey != true && event.metaKey != true ){
                    $container.toggle();
                }
            });
        });
    };
    // Fill/Update current mquery value
    $.fn.watchForCurrentMediaQuery = function(options) {
        return this.each(function() {
            var current,
                $container = $(this),
                matched = [];
            if (matchMedia(Foundation.media_queries['small']).matches){
                matched.push('small');
            };
            if (matchMedia(Foundation.media_queries['medium']).matches){
                matched.push('medium');
            };
            if (matchMedia(Foundation.media_queries['large']).matches){
                matched.push('large');
            };
            if (matchMedia(Foundation.media_queries['xlarge']).matches){
                matched.push('xlarge');
            };
            if (matchMedia(Foundation.media_queries['xxlarge']).matches){
                matched.push('xxlarge');
            };
            matched.reverse();
            current = matched.shift();
            $('.value', $container).html(current);
        });
    };
}( jQuery ));

/*
 * Common method to init all equalize rules
 *
 * Needed to be called in the $.load(), because webkit raise ready() even if it have
 * not download all ressources, this cause false dimensions because all images
 * have not yet be downloaded, so they doesn't set true dimensions on their
 * parent and etc..
 *
 * NOTE: This is not really needed anymore, prefer to use Flexbox on your
 *       container that is pure CSS3.
 */
// function column_equalizer(){
//     // Equalize content text columns to the same height
//     $('.equal-heights').equalize({'equalize':'outerHeight', children: '.equalized-item', reset: true, breakpoint: 750});
//     // Like before but only as a fallback for browser without flexbox support (using Modernizr detection classes)
//     $('html.no-flexbox .equal-noflex-heights').equalize({'equalize':'outerHeight', children: '.equalized-noflex-item', reset: true, breakpoint: 750});
//     return;
// };

/*
 * Use html attribute to add links on elements without to use
 * real <a> href attribute
 *
 * WARNING: Using this is a BAD practice for ergonomy and SEO
 */
// function AddLinkFromAttribute(options) {
//     $('*[data-link]').click(function(event) {
//         window.location.href = $(this).attr('data-link');
//         event.preventDefault();
//     });
// };
