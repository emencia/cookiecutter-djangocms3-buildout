jQuery(document).ready(function($) {
    // Video clicker
    // When clicked search for facade container with video url then hide the
    // facade and add video container on the fly
    $('.video-facade').on("click", function() {
        var $this = $(this),
            facade_elem = $(this).find('.facade-container'),
            video_elem,
            video_url;

        if(facade_elem && facade_elem.length>0){
            video_url = facade_elem.attr('data-facade-video');
            if(video_url){
                video_elem = $('<div class="flex-video"><iframe width="420" height="315" src="" frameborder="0" allowfullscreen></iframe></div>');
                video_elem.find('iframe').attr('src', video_url);
                facade_elem.hide();
                $this.append(video_elem);
            }
        }

    });
});
