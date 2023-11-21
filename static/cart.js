function deleteShoppingCart(url, productId){
    fetch( `${url}` , {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': document.getElementsByName('csrfmiddlewaretoken')[0].value, // Получаем CSRF-токен
        }})
        .then(()=>{
            var elementToRemove = document.getElementById(productId);
            if (elementToRemove) {
                elementToRemove.parentNode.removeChild(elementToRemove);
              } else {
                console.log('Элемент не найден');
              }
        });
}

function quantityChangeClick(rowId, url){
    // получить измененное количество(фронтенд)
    let quantityHtml = document.getElementById('quantityChange')
    let quantityInt = parseInt(quantityHtml.value)

    // изменить сумму строки с учетом нового количества(фронтенд)
    let priceHtml = document.getElementById(`price_${rowId}`)
    let rowtotalpriceHtml = document.getElementById(`row_total_price_${rowId}`)
    rowtotalpriceHtml.textContent = `${parseFloat(priceHtml.innerText)  * quantityInt}`

    // изменить общую сумму на странице(фронтенд)
    // отправить в базу, сохранить(запрос джанго)
}