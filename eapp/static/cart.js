var updateBtns = document.getElementsByClassName('update-cart')


// from line 1 to 9 we were able to console out the item id after clicking on add to cart btn 
for(i=0;i< updateBtns.length;i++){
    updateBtns[i].addEventListener('click', function(){
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:',productId, "action:",action)

        console.log('USER:',user)
        if (user == 'AnonymousUser') {
            console.log("User is not Authenticated")
        } else {
            updateUserOrder(productId, action)
            
        } 
    })
}

function updateUserOrder(productId, action) {
    console.log("User is authenticated, sending data...")
    var url = '/updateItem/'

    fetch(url,{
        method:"POST",
        headers:{
            'Content-Type':'application/json',
             'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId':productId, 'action':action})
    })
    .then((response)=>{
        return response.json();
    })
    .then((data)=>{
        console.log('data:',data)
        location.reload()
    });
    
}