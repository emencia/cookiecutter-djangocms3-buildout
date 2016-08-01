/*
 **
 ** This is the main frontend Javascript where all components will be initialized
 **
 ** WARNING: Don't enable things that you don't need, keep your frontend script
 **          clean.
 **
 */
jQuery(window).load(function () {
    /*
    * Apply the trick to swap <img> elements into their container
    * background and set a minimal height from image height
    */
    // Shortcuts using class
    $('img.auto-background-cover').swapImageToBackground({
        "position": '50% 50%',
        "repeat": 'no-repeat',
        "size": 'cover'
    });
    $('img.auto-background-auto').swapImageToBackground({
        "position": '50% 50%',
        "repeat": 'no-repeat',
        "size": 'auto'
    });
    $('img.auto-background-contain').swapImageToBackground({
        "position": '50% 50%',
        "repeat": 'no-repeat',
        "size": 'contain'
    });
    // Normal way using html attributes
    $('img.background').swapImageToBackground();

    // Let the initial image loading, when it's done, replace the initial image with
    // its replacement url given in "data-lazy-replacement" attribute
    $('img.lazy-replacement').each(function() {
        if($(this).attr('data-lazy-replacement')){
            $(this).attr('src', $(this).attr('data-lazy-replacement'));
        }
    });

    /*
     * Init Slick.js slider
     */
    $('.slick-container').slick({
        'adaptiveHeight': true,
        'lazyLoad': 'ondemand'
    });
    // Ensure optional clickable slider
    $('.slick-container .item[data-link-external]').click(function(event) {
        $(this).addClass("clickable");
        if( $(this).attr('data-slide-url-target') && ($(this).attr('data-slide-url-target') == '_blank' || $(this).attr('data-slide-url-target') == 'blank') ){
            window.open($(this).attr('data-slide-url'), '_blank');
        } else {
            window.location.href = $(this).attr('data-slide-url');
        }
        event.preventDefault();
        return false;
    });
});

jQuery(document).ready(function($) {
    // Init MediaQuery watcher (look into addons.js for more infos)
    $('#watch-for-current-mquery').initCurrentMediaQuery();
    $('#watch-for-current-mquery').watchForCurrentMediaQuery();

    /*
    * Initialize Foundation
    */
    $(document).foundation();

    /*
     * Naive stuff for debugging elements
     *
     * Just add element name as prefix on each element.
     */
    /*$('h1,h2,h3,h4,h5,h6,p,li,dd,dt', '.prefix-dom-items').each(function() {
        var $this = $(this),
            prefix = this.tagName;
        if( this.tagName == 'P') {
            if($this.hasClass("title-1")){
                prefix += ".title-1";
            } else if($this.hasClass("title-2")){
                prefix += ".title-2";
            } else if($this.hasClass("title-3")){
                prefix += ".title-3";
            } else if($this.hasClass("title-4")){
                prefix += ".title-4";
            } else if($this.hasClass("title-5")){
                prefix += ".title-5";
            } else if($this.hasClass("title-6")){
                prefix += ".title-6";
            }
        }

        if(prefix){ $this.html(prefix+': '+$this.html()); }
    });*/

    // Reflow the 'swapImageToBackground' plugin on debounced
    // resize event to recalculate min-height for background image container
    $(window).on("debouncedresize", function( event ) {
        $("img[data-imgbg-status='processed']").swapImageToBackground('resize_height');
        // MediaQuery watcher on resize
        $('#watch-for-current-mquery').watchForCurrentMediaQuery();
    });
});
