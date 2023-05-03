let searchElement = document.getElementById("search-wrapper")

searchElement.addEventListener('keyup', function(e){
    if (e.code === 'Enter') {
        console.log('Enter pressed')
    }
})