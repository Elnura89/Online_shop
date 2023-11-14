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

async function setRating(url, rating, productId){
    await fetch( `${url}?id=${productId}&points=${rating}` , {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value, // Получаем CSRF-токен
        }});

    await fetch(`${url}${productId}`, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value, // Получаем CSRF-токен
        }}) 
        .then(response => response.json())
        .then(data => {
            let linkElement = document.getElementById('RatingPoints');
            //data['points']
            // Дайте новое значение элементу где хранится рейтинг в html
        })
}
