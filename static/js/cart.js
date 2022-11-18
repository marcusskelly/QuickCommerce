
var updateBtns = document.getElementsByClassName('update-cart')


for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productoId = this.dataset.producto
		var action = this.dataset.action
		console.log('productoId:', productoId, 'action:', action)
        console.log('USER:', user)

		if (user == 'AnonymousUser'){
			
			addCookieItem(productoId, action)
			
		}else{
			updateUserOrder(productoId, action)
		}

	})
}

function updateUserOrder(productoId, action){
	console.log('User is authenticated, sending data...')
	console.log('User is authenticated, sending data...')
		var url = '/update_item/'

		fetch(url, {
			method:'POST',
			mode: 'cors',
			headers:{
				'Accept': 'application/json, text/plain, */*',
				'Content-Type':'application/json', //esta linea importantisima para el post
				'X-CSRFToken':csrftoken,
			}, 
			body:JSON.stringify({'productoId':productoId, 'action':action})
		})
		.then((response) =>{
		   return response.json();
		})
		.then((data) =>{
		    console.log('data:', data)
			location.reload()
		});
}


function addCookieItem(productoId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productoId] == undefined){
		cart[productoId] = {'cantidad':1}

		}else{
			cart[productoId]['cantidad'] += 1 // this gave me a lot of trouble cos I placed "+" instead of "=+"
		}
	}

	if (action == 'remove'){
		cart[productoId]['cantidad'] -= 1

		if (cart[productoId]['cantidad'] <= 0){
			console.log('Item should be deleted')
			delete cart[productoId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload() // reload in order to update the cart icon
}