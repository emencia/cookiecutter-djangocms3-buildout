/*
 **
 **
 ** This is the main frontend Javascript where all components will be initialized
 ** 
 ** There is some sample code for some components that are not enabled by default, 
 ** you will have to uncomment them and eventually edit them for your needs.
 ** 
 ** WARNING: Don't enable things that you don't need, keep your frontend script 
 **          clean. You can clean unused stuff but note that uncommented code will 
 **          be removed from final script in production by Javascript compressor.
 **
 */
$(window).load(function () {
    // Equalize some columns after full page loading
    // NOTE: Needed to be in the $.load(), because webkit raise ready() even if it does not have
    //       downloaded all ressources, this cause false dimensions because all images
    //       have not yet be downloaded, so they doesn't set true dimensions on their
    //       parent and etc..
    column_equalizer();
    //AddLinkFromAttribute();
    //LeftMegaMenu( $("#navabsleft") );
});

$(window).resize(function() {
    column_equalizer();
    //LeftMegaMenu( $("#navabsleft") );
});

$(document).ready(function($) {
    var $wallgrid_container = $('#isogrid'),
        $interchanged_content_intro = $('#interchanged-content-intro');

    /*
    * Button dropdown trick
    */
    // We can't use "data-***" html5 attibutes with ckeditor, but Foundation5
    // requires them for Button Dropdown, so we add them on the fly for these
    // buttons that have the "trick" class. Also their "id" is automatically
    // added so you don't have to manage them.
    $('a.button.dropdown.trick').each(function( index ) {
        var dropdown_id = "dropdown-trick-"+index,
            dropdown_menu,
            container;
        if( $( this ).parent().get(0).tagName == 'P' || $( this ).parent().get(0).tagName == 'LI' ) {
            container = $(this).parent();
        } else {
            container = $(this);
        }
        dropdown_menu = container.next("ul.f-dropdown");
        if(dropdown_menu){
            $(this).attr('data-dropdown', dropdown_id);
            dropdown_menu.attr('id', dropdown_id).attr('data-dropdown-content', '');
        }
    });

    /*
     * Apply the trick to swap <img> elements into their container background
     */
    $('img.background').swapImageToBackground();

    /*
     * Pikaday for the common datepicker in form, note this use moment.js also
     * to have correct localized format
     */
    /*$('.datepicker').pikaday({
        format: 'DD/MM/YYYY',
        i18n: {
            previousMonth: 'Mois précédent',
            nextMonth: 'Mois suivant',
            months: ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre'],
            weekdays: ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'],
            weekdaysShort: ['Dim','Lun','Mar','Mer','Jeu','Ven','Sam']
        }
    });*/

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

    /*
    * Initialize Foundation after all event is binded
    */
    $(document).foundation();

    /*
    * Conditionnal contents loading from interchange being
    */
    if($interchanged_content_intro.length>0){
        // Triggered event when Foundation 'interchange' plugin replace the content
        $interchanged_content_intro.on('replace', function (e, new_path, original_path) {
            // Inits postorious contents
            $('#slideshow-container').foundation('orbit');
            // Use socialaggregator lib only if loaded
            $.fn.SocialWallGrid ? $wallgrid_container.SocialWallGrid() : null;
        });
        // Fallback for small resolution which is excluded from the interchange content
        // (and so does not trigger a 'replace')
        if(matchMedia(Foundation.media_queries.small).matches){
            $('#slideshow-container').foundation('orbit');
            // Use socialaggregator lib only if loaded
            $.fn.SocialWallGrid ? $wallgrid_container.SocialWallGrid() : null;
        }

    } else {
        // If there is no interchange content
        // Use socialaggregator lib only if loaded
        $.fn.SocialWallGrid ? $wallgrid_container.SocialWallGrid() : null;
    }
    
    /*
    * Initialize MegaMenu
    */
    /*$("#menu_left").mmenu({
            // options
            classes: "mm-light"
        }, {
            // the configuration
            pageSelector: "#page"
        }
    );*/
    
    /*
     * Finally you can reflow some Foundation component when you have some code that 
     * disturb/change their initial behaviors
     * Don't use it this too much because it can cause some "display blinking".
     */
    //$(document).foundation('accordion', 'reflow');
    //$(document).foundation('orbit', 'reflow');
});
