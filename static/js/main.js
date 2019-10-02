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
    console.log("Hello World", searchValue)
    fetch('/api?search=' + searchValue)
}