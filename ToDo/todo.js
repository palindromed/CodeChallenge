$(function(){


    $('ul').on('click', 'li', function(){
        $(this).addClass('remove');
        $('.remove').remove();
    });

       $('form').on('submit', function(event) {

        var newTask = $('input').val();
        $("#form").get(0).reset()
        if (newTask != '') {
            var first = document.getElementsByTagName('li')[0]
            $('<li>'+ newTask + '</li>').insertBefore(first);
        };

        event.preventDefault();
    });


});

