/*
jQuery Plugin to load social content from socialaggregator : https://github.com/rage2000/emencia-django-socialaggregator

Fill the grid with content block positionned with Masonry, eventually load 
the grid content from a JSON feed.

Actually this is not intended to load multiple backend (like for pagination) 
or add new items after the first load. It's only intended to make only one 
wallgrid build from the backend because masonry is initialized each time 
after the backend is fetched.

How this fuckin' work :

* item width size is defined from css "w-sizer-***" class formulated in percentage;
* item height size is calculated in socialaggregator "extensions.resize_blocks" for each 
  "h-sizer-**" class, the calcul is made from the current item width with some ratio;
* masonry is given the hand, it will places the item in grid with an absolute position;

If the grid container contains a "data-socialaggregator-url" attribute, the 
grid content will be loaded from the given Json feed url and socialaggregator 
will build the html from it. If the attribute is not defined or empty, we assume 
the html content is allready in the DOM.


Requires :
- Masonry
- ICanHaz javascript library : http://icanhazjs.com/ (only if you use the grid with the Json feed)
- Moment.js : http://momentjs.com/

Usage sample :

    $('#myelement').SocialWallGrid();

Or if you want to override some settings :

    $('#myelement').SocialWallGrid({
        'size_classes': {
            'small' : 'grid-item small',
            'medium' : 'grid-item medium',
            'large' : 'grid-item large'
        }
    });
 */
(function ( $ ) {

/*
* Plugin extensions calling logic
*/
$.fn.SocialWallGrid = function(method) {
    // Specific public method called
    if ( extensions[method] ) {
        return extensions[method].apply( this, Array.prototype.slice.call( arguments, 1 ));
    // Default public method to init the plugin
    } else if ( typeof method === 'object' || ! method ) {
        return extensions.init.apply( this, arguments );
    // Unknow called method
    } else {
        $.error( 'Method ' +  method + ' does not exist on jQuery.SocialWallGrid' );
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
        // Default settings that can be overrided
        var settings = $.extend( {
            // CSS classes linked to size mode key name
            'size_classes': {
                'small': 'w-sizer-1 h-sizer-1',
                'default': 'w-sizer-2 h-sizer-1',
                'medium': 'w-sizer-2 h-sizer-1',
                'large': 'w-sizer-2 h-sizer-2'
            },
            // CSS classes linked to social content type key name
            'type_classes': {
                'edsa_article' : 'article',
                'edsa_article-infos': 'article article-infos',
                'edsa_article-facebook': 'article article-facebook',
                'edsa_article-twitter': 'article-twitter',
                'edsa_article-youtube': 'article article-youtube',
                'edsa_facebook_fanpage' : 'facebook',
                'edsa_twitter' : 'twitter',
                'edsa_instagram' : 'instagram',
                'edsa_pinterest' : 'pinterest',
                'edsa_youtube' : 'youtube'
            },
            // CSS classes linked to social content type key name
            'text_display_classes': {
                'default' : '',
                'top' : 'item-top',
                'bottom' : 'item-bottom'
            },
            'spinner_selector': '#isospinner'
        }, options);
        
        return this.each(function() {
            var $this = $(this);
            
            // Attach settings to the element
            $this.data("SocialWallGrid", {
                "settings": settings,
                "feed_url": $this.attr('data-socialaggregator-url'),
                "medias_url": $this.attr('data-socialaggregator-medias_url')
            });
            
            // We have a feed url, proceed to fetch the feed and layout its contents
            if($this.attr('data-socialaggregator-url')){
                $this.bind("socialaggregator:update_wall", events.update_wall);
                $this.SocialWallGrid('load_backend');
            // No given url, just init masonry for existing grid elements in HTML
            } else {
                $this.SocialWallGrid('resize_blocks');
                $this.SocialWallGrid('initMasonry');
            }
        });
    },
 
    /*
    * Load the feed backend
    */
    load_backend : function() {
        return this.each(function(){
            var $this = $(this),
                data = $this.data("SocialWallGrid");
            
            $.ajax({
                url: data.feed_url,
                dataType: "json",
                success: function (backend, textStatus) {
                    $this.trigger("socialaggregator:update_wall", [backend]);
                },
                error: function(XMLHttpRequest, textStatus, errorThrown){
                    //silent pass
                }
            });
        });
    },

    /*
     * Resizing parent
     */

    resize_parent : function() {

        var $container=$(this);
        $container.width('100%');
        var $wCont= $container.width();
        $container.width($wCont - $wCont % 8);

    },

    /*
    * Resizing all wall grid blocks
    */
    resize_blocks : function() {

        return this.each(function(){
            var $this = $(this),
                $grid_gutter = 12,
                $width_1 = $($this).find('.w-sizer-1').first().width(),
                $width_2 = $($this).find('.w-sizer-2').first().width(),
                // Large height is the base, calculated from the width and a ratio
                $large_height = Math.round($width_2/0.76),
                $small_height = $large_height/2,
                $medium_height = $small_height;

            
            /*console.log( "w-sizer-1: %d", $width_1);
            console.log( "w-sizer-2: %d", $width_2);
            console.log( "large_height: %d", $large_height);
            console.log( "small_height: %d", $small_height);
            console.log( "medium_height: %d", $medium_height);*/
            
            // Small and medium size height
            $('.h-sizer-1', $this).each(function( index ) {
                /*console.group("Small and Medium heights");
                console.log("height: %d", $small_height);
                console.groupEnd();*/
                $(this).height( $small_height ).find('.containItem').height( $small_height-$grid_gutter );
            });
            // Large size height
            $('.h-sizer-2', $this).each(function( index ) {
                /*console.group("Large height");
                console.log("height: %d", $large_height);
                console.groupEnd();*/
                $(this).height( $large_height ).find('.containItem').height( $large_height-$grid_gutter );
            });
        });
    },

    /*
    * 
    */
    initMasonry : function() {

        $(this).SocialWallGrid('resize_parent');;

        return this.each(function(){
            var $this = $(this);
            // init masonry
            $this.masonry({
                // options
                columnWidth: '.grid-base',
                itemSelector: '.grid-item',
                gutterWidth: 0,
                isInitLayout: false
            });
            $this.masonry('on', 'layoutComplete', function() {
                $this.css("visibility", "visible");
                $( $this.data("SocialWallGrid").settings.spinner_selector ).hide();
            });
            $this.masonry('bindResize');
            $(window).resize(function() {

                $this.SocialWallGrid('resize_parent');
                $this.SocialWallGrid('resize_blocks');
                $this.masonry('reloadItems');
            });
            $this.masonry('layout');
        });
    }
};

var events = {
    /*
    * Update HTML wall grid from backend entries
    */
    update_wall : function(event, backend) {
        var $this = $(event.target),
            data = $this.data("SocialWallGrid"),
            settings = data.settings;
        // Crawl backend items to push them as content blocks
        $.each(backend, function( index, item ) {
            var $item, button, content_media, context;
            
            // WARNING: When a element with "small" size mode is displayed 
            // (really viewable on screen) it can causes Firefox (25) to have a high 
            // usage of CPU (going to 140-170%) because of a CSS issue.
            // More specifically, the problem is related only to the 'grid-sizer2' 
            // class with the "background-size: cover;" property, seems FF works 
            // too much to resize large image to small size when scrolling over them.
            // Line below drop 'small' items within development (CPU issue is 
            // such annoying..) if needed
            //if(item.fields.view_size=='small') return;

            // Only fill media if media_url is not empty
            if(item.fields.media_url){
                
                content_media = {
                    'url': item.fields.media_url,
                    'kind': item.fields.media_url_type
                };
            }
            
            // Only fill button if label is not empty and media_url is not empty
            if(item.fields.button_label && content_media && content_media.url){
                button = {
                    'label': item.fields.button_label,
                    'color': item.fields.button_color,
                    'url': content_media.url
                };
            }
            
            // Item context to pass to the template
            context = {
                "id": item.pk,
                "slug": item.fields.slug,
                "css_classes": [
                    // use 'medium' size type for 'default' key
                    (item.fields.view_size=='default') ? settings.size_classes['medium'] : settings.size_classes[item.fields.view_size],
                    settings.type_classes[item.fields.social_type],
                    settings.text_display_classes[item.fields.text_display]
                ].join(" "),
               
                "title": null,
                "description": (item.fields.description || item.fields.short_description).replace('\r\n', '<br>'),
                "button": button,
                "has_subblock": (item.fields.author || item.fields.ressource_date),
                "author": item.fields.author,
                "date": moment(item.fields.ressource_date).format("DD MMM"),
                "image": (item.fields.image) ? data.medias_url+item.fields.image : null,
                "media": content_media
            };
            // Content type specific context defines
            if(item.fields.social_type == 'edsa_youtube') {
                context.title = item.fields.name;
                // These ones are not wanted as we can seen it in the mockup, so 
                // drop them
                context.author = null;
                context.date = null;
            } else if(item.fields.social_type == 'edsa_pinterest') {
                context.title = item.fields.name;
            } else if(item.fields.social_type == 'edsa_twitter' || item.fields.social_type == 'edsa_facebook_fanpage' || item.fields.social_type == 'edsa_instagram') {
                // Seems there are nothing to do for these types
            // article is the default
            } else { 
                context.title = item.fields.name;
            }
            
            // See to use precompiled template, seems actually template is 
            // reparsed each time, last mustach version has a precompiled 
            // behavior, there is a patch for this for ICanHaz, also see 
            // ICanHaz-no-mustach
            $item = $(ich.wallgrid_block(context)).appendTo($this);
            
            // If element media_url is given but there are no defined button, 
            // make the element clickable with the media_url
            if(content_media && content_media.url && !button ){
                $item.addClass("clickable");
                $item.click(function(event){
                    document.location.href = content_media.url;
                    return false;
                });
            }
        });
        //alert($container.width());

        // Move all this appart so we can use it when we need and not allways

        $this.SocialWallGrid('resize_blocks');
        $this.SocialWallGrid('initMasonry');
    }
};

}( jQuery ));