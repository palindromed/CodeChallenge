$(function(){


    $('ul').on('click', 'li', function(){
        $(this).addClass('remove');
        $('.remove').remove();
    });

    $('form').on('submit', function(event) {

        var newTask = $('input').val();

        $('<li>'+ newTask + '</li>').prependTo('li');

        event.preventDefault();
    });


});

