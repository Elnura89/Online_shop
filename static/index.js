function pressLike(url){
    fetch( url , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value, // Получаем CSRF-токен
        }
     })
    .then((response)=>{
        let linkElement = document.getElementById('likesCount');
        let likesCount = parseInt(linkElement.innerText)
        if (response.status == '200'){
            linkElement.innerHTML = `${likesCount+1}`
        }
        else{
            linkElement.innerHTML = `${likesCount-1}`
        }
    })
}

function setRating(url, rating, productId){
    fetch( `${url}?id=${productId}&points=${rating}` , {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value, // Получаем CSRF-токен
        }
     })
}