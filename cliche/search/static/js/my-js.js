$(document).ready(function(){

   

    $( "body" ).delegate( ".search", "click", function( event ) {
        $('#form-search').submit();
    });
    // $( "body" ).delegate( "#toggle-checkbox", "click", function( event ) {
    //     alert('change')
    //     if($(this).is(":checked") === true){
    //         sessionStorage.setItem("nightMode", "1");
    //         $('body').css('background-image','linear-gradient(hsla(239, 50%, 20%, 1), hsla(251, 54%, 50%, 1),hsla(290,100%,50%,0.3))');
    //         $('.fa-search').css('color','#ffffff');
    //         $('.str').show();
    //         $('#moon-or-sun').removeClass("sun").addClass("moon"); //Adds 'a', removes 'b'
    //     }else{
    //         sessionStorage.setItem("nightMode", "0");
    //         $('body').css('background-image','linear-gradient(hsla(201, 80%, 75%, 1), hsla(164, 97%, 90%, 1), hsla(350, 100%, 96%, 1))');
    //         $('.fa-search').css('color','#000000');
    //         $('.str').hide();
    //         $('#moon-or-sun').removeClass("moon").addClass("sun"); //Adds 'a', removes 'b'
    //     }
    // });
    $( "body" ).delegate( ".home", "click", function( event ) {
        window.location.href = "http://127.0.0.1:8000";
    });
    
    function nightMode(){
        if(localStorage.getItem(COLOR_STORAGE_KEY) == 'dark'){
            $('#moon-or-sun').removeClass("sun").addClass("moon");
            $('.fa-search').css('color','#ffffff');

        }else{
            $('.fa-search').css('color','#000000');

        }
    }
    nightMode();


});