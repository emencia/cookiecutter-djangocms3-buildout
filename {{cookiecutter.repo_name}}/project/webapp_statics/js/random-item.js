/*
jQuery Plugin to do random choice on a given array
 */
(function ( $ ) {

/*
* Plugin extensions calling logic
*/
$.fn.RandomItem = function(method) {
    // Specific public method called
    if ( extensions[method] ) {
        return extensions[method].apply( this, Array.prototype.slice.call( arguments, 1 ));
    // Default public method to init the plugin
    } else if ( typeof method === 'object' || ! method ) {
        return extensions.init.apply( this, arguments );
    // Unknow called method
    } else {
        $.error( 'Method ' +  method + ' does not exist on jQuery.RandomItem' );
    }
};

/*
 * Simple image preloader method
 */
var image_preloader = function(image) {
    var img = new Image();
    img.src = image;
}

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
            "items": {}, // Content items
            "choices": [] // Item names available to select and build as HTML
        }, options);
        
        return this.each(function() {
            var $this = $(this);
            
            // Attach settings to the element
            $this.data("RandomItem", {
                "settings": settings,
            });
            
            // Do the job
            $this.RandomItem('load_item');
        });
    },
 
    /*
    * Select a random content then add it to the DOM using the dedicated template
    */
    load_item : function() {
        return this.each(function(){
            var $this = $(this),
                settings = $this.data("RandomItem").settings,
                rand = settings.choices[Math.floor(Math.random() * settings.choices.length)];
            
            $item = $(ich.slide_block(settings.items[rand])).appendTo($this);
            //console.log("RandomItem selected choice: %s", rand);
        });
    }
};

}( jQuery ));