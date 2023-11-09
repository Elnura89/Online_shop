function pressLike(url){
    fetch( url , {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value, // Получаем CSRF-токен
        }
    })
    // .then(data=>{
    //     alert('Запрос успешно принят')
    // })
    // .catch(e => {
    //     alert('Запрос не принят')
    // }) закоментированное это проверка работает или нет лайк
}