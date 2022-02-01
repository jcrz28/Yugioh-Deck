function deleteCard(cardId){
    fetch('delete-note', {
        method: 'POST',
        body: JSON.stringify({cardId: cardId})
    }).then((_res)=>{
        // reload window
        window.location.href = "/"; 
    })
}