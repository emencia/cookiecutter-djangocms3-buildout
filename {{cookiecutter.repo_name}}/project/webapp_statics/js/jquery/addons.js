/*
 * Common method to init all equalize rules in a one shot
 *
 * Needed to be called in the $.load(), because webkit raise ready() even if it have
 * not download all ressources, this cause false dimensions because all images
 * have not yet be downloaded, so they doesn't set true dimensions on their
 * parent and etc..
 *
 * NOTE: This is not really needed anymore, prefer to use Flexbox on your
 *       container that is pure CSS3.
 */
function column_equalizer(){
    // Equalize content text columns to the same height
    $('.equal-heights').equalize({'equalize':'outerHeight', children: '.equalized-item', reset: true, breakpoint: 750});
    // Like before but only as a fallback for browser without flexbox support (using Modernizr detection classes)
    $('html.no-flexbox .equal-noflex-heights').equalize({'equalize':'outerHeight', children: '.equalized-noflex-item', reset: true, breakpoint: 750});
    return;
};

/*
 * Use html attribute to add links on elements without to use
 * real <a> href attribute
 *
 * WARNING: Using this is a BAD practice for ergonomy and SEO
 */
function AddLinkFromAttribute(options) {
    $('*[data-link]').click(function(event) {
        window.location.href = $(this).attr('data-link');
        event.preventDefault();
    });
};
