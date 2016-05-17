jQuery(document).ready(function($) {
    /*
     * Slick.js slider with adaptive height, arrows and without dots
     */
    $('.slick-container:not(.dotted)').slick({
        'adaptiveHeight': true,
        'lazyLoad': 'ondemand'
    });

    /*
     * Slick.js slider with adaptive height, with dots and without arrows
     *
     * 1) Container 'slick-container' that have a 'data-dots-title' html
     * attribute, will have it used as a paragraph ('p.slick-dots-title')
     * title added before dot list (if there is at least one dot).
     *
     * 2) Item having attribute 'data-dot-colorclass' will use it has a css
     * classname.
     *
     * 3) If container have 'with-thumbs' class, display thumb image instead
     * of simple dot, using any image with the 'thumb' class within the item
     * container
     */
    $('.slick-container.dotted').on('init', function(event, slick){
        if(slick.$dots){
            // Insert legend title from container attribute 'data-dots-title' if any
            if (slick.$slider.attr('data-dots-title')){
                slick.$dots.before('<p class="slick-dots-title">'+ slick.$slider.attr('data-dots-title') +'</p>');
            }

            // Find slide related to each dot and insert their
            // 'data-dot-colorclass' as a dot item classname if any
            $('li', slick.$dots).each(function() {
                var $thumb,
                    $button_elem = $(this).find('button'),
                    $i = parseInt($button_elem.attr('data-dot-index')),
                    $slide = $(slick.$slides[$i]);

                $(this).addClass( $slide.attr('data-dot-colorclass') );
                // Search for eventual thumbs
                if (slick.$slider.hasClass('with-thumbs')){
                    $thumb = $slide.find('img.thumb');
                    if($thumb) {
                        $button_elem.html( $('<img src="'+ $thumb.attr('src') +'" alt="">') );
                    }
                }
            });

        }
    });
    var custom_dot_paging = function(slider, i) {
        return '<button type="button" data-role="none" role="button" aria-required="false" tabindex="0" data-dot-index="' + i + '">' + (i + 1) + '</button>';
    }
    $('.slick-container.dotted').not('.not-draggable').slick({
        'adaptiveHeight': true,
        'arrows': false,
        'dots': true,
        'customPaging': custom_dot_paging,
        'lazyLoad': 'ondemand'
    });
    $('.slick-container.dotted.not-draggable' ).slick({
        'adaptiveHeight': true,
        'arrows': false,
        'dots': true,
        'draggable': false,
        'customPaging': custom_dot_paging,
        'lazyLoad': 'ondemand'
    });

});