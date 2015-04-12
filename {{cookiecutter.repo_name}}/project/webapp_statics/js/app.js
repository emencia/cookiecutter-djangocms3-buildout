/*
// Part stuff for Emencia Browser Report
*/

function getParameterByName(name) {
    var match = RegExp('[?&]' + name + '=([^&]*)').exec(window.location.search);
    return match && decodeURIComponent(match[1].replace(/\+/g, ' '));
}
function extract_browser_report() {
    var datas = [],
        cookieEnabled=navigator.cookieEnabled?"Yes":"No",
        viewport=window.innerWidth || document.documentElement.clientWidth;

    datas.push("Url: "+ window.location.href);
    datas.push("User agent: "+ navigator.userAgent);
    datas.push("Plateform: "+ navigator.platform);
    datas.push("Language: "+ navigator.language);
    datas.push("Cookies enabled: "+ cookieEnabled);
    datas.push("Viewport width: "+ viewport);

    return datas;
}


$(window).load(function () {
    // Equalize some columns after full page loading
    // NOTE: Needed to be in the $.load(), because webkit raise ready() even if it does not have
    //       downloaded all ressources, this cause false dimensions because all images
    //       have not yet be downloaded, so they doesn't set true dimensions on their
    //       parent and etc..
    column_equalizer();

});

$(window).resize(function() {
    column_equalizer();
});

$(document).ready(function($) {
    var $wallgrid_container = $('#isogrid');

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
//     $('.datepicker').pikaday({
//         format: 'DD/MM/YYYY',
//         i18n: {
//             previousMonth: 'Mois précédent',
//             nextMonth: 'Mois suivant',
//             months: ['Janvier','Février','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre'],
//             weekdays: ['Dimanche','Lundi','Mardi','Mercredi','Jeudi','Vendredi','Samedi'],
//             weekdaysShort: ['Dim','Lun','Mar','Mer','Jeu','Ven','Sam']
//         }
//     });

    // Popin for image/iframe will not display on small media-query
    if($(window).innerWidth()>640){
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
    }

    /*
    * Initialize Foundation after all event is binded
    */
    $(document).foundation();

    /*
    * Conditionnal contents loading from interchange being
    */
    $interchanged_content_intro = $('#interchanged-content-intro');
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

    // EBR: Emencia Browser Report
    if(getParameterByName('ebr')){
        console.log("Emencia Browser Report activated");

        var html = '<div id="ebr_container" style="z-index:9999; position:absolute; top:10px; left:10px; padding:5px; border:2px solid red; background:#ffffff;">'+
            '<p style="color:#000;"><strong>Emencia Browser Report</strong></p>'+
            '<p style="color:#000;">Copy the text below and paste in your message</p>'+
            '<textarea style="color:#000;">'+ extract_browser_report().join("\n") +'</textarea>'+
            '<p style="color:#000;">If you resize your browser, you will have to reload the page again.</p>'+
        '</div>';
        $('body').append(html);
    }
});

// Foundation JavaScript
// Documentation can be found at: http://foundation.zurb.com/docs
$(document).foundation();