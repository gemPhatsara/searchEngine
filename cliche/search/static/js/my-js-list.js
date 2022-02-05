$(document).ready(function(){
    const COLOR_STORAGE_KEY='user-color-scheme';

    function nightMode(){
        if(localStorage.getItem(COLOR_STORAGE_KEY) == 'dark'){
            $('#moon-or-sun').removeClass("sun").addClass("moon");
            $('.fa-search').css('color','#ffffff');
            $('body').css('background-image','linear-gradient(hsla(239, 50%, 20%, 1), hsla(251, 54%, 50%, 1),hsla(290,100%,50%,0.3))');
            $('a.url').css('color','#ffb17a');
            $('li.desc').css('color','#ffffff');
        }else{
            $('body').css('background-image','linear-gradient(hsla(201, 80%, 75%, 1), hsla(164, 97%, 90%, 1), hsla(350, 100%, 96%, 1))');
            $('a.url').css('color','#1a0dab');
            $('li.desc').css('color','#000000');
            $('.fa-search').css('color','#000000');
            $('.str').hide();

        }
    }
    nightMode();

    $('p.title').click(function(){
        window.location.href = "http://127.0.0.1:8000";
    });

    $( "body" ).delegate( ".search", "click", function( event ) {
        $('#form-search').submit();
    });
});
