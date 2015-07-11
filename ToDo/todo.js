$(function(){


    $('li').on('click', 'li', function(){
        $(this).addClass('remove');
        $('.remove').remove();
    });


});

