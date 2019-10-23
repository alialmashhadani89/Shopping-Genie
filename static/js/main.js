(function preLoad(){  /*runs before content is loaded, rest of content won't load until this has completed*/

    window.addEventListener('load', function(){onLoad();}, false);
}());


function onLoad() {
    const form = document.getElementById('search-form');
    form.addEventListener('submit', submitForm);
    //from.document.getElementById('search-form').value='';
}

function submitForm(e) {
    e.preventDefault()
    const searchInput = document.getElementById("search-term");
    const searchValue = searchInput.value;
    const new_searchValue = searchValue.trim()
    if (new_searchValue.split(" ").length < 2)
        alert("Please enter more than one keyword.")
    else
       fetch('/api?search=' + searchValue)
}