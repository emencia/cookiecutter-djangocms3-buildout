jQuery(document).ready(function($) {
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
    * Initialize Foundation after all event is binded
    */
    $(document).foundation();
});
