function deleteCard(cardId){
    fetch('delete-card', {
        method: 'POST',
        body: JSON.stringify({cardId: cardId})
    }).then((_res)=>{
        // reload window
        window.location.href = "/"; 
    })
}