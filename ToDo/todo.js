(function(){
    window.list = document.getElementById('lists');
    var form = document.getElementById('form');
    var input = document.getElementById('task');

    form.addEventListener("submit", function(event){
        var task = input.value
        //while there is text input, create and add a list element
        if (task != '') {
            var li = document.createElement("li");
            var text = document.createTextNode(task);
            li.appendChild(text);
            //window.list.appendChild(li);

            window.list.insertBefore(li, window.list.firstChild);

            input.value = null;
        }
        //prevent empty list elements from being added
        event.preventDefault();
    });

    list.addEventListener('click', function(event){
    var tag = event.target;
    if (tag.tagName === 'LI') {
      tag.parentNode.removeChild(tag);
    };
    event.preventDefault();
    });

})();
