jQuery(document).ready(function($) {
    // Popin for image/iframe will not display on small media-query
    /*if($(window).innerWidth()>640){
        // Pop-in gallery for Porticus
        $('.album-grid').magnificPopup({
            delegate: '.row .item a',
            type: 'image',
            gallery:{
                enabled:true
            }
        });
        // Common Pop in, any url is fully passed to the iframe src
        $('.pop-in').magnificPopup({
            type: 'iframe',
            iframe: {
                patterns: {
                    customsource: {
                        index: '',
                        src: '%id%'
                    }
                },
                srcAction: 'iframe_src', // Templating object key. First part defines CSS selector, second attribute. "iframe_src" means: find "iframe" and set attribute "src".
            }
        });
    }*/
});
