
var updateBtns = document.getElementsByClassName('update-cart')


for (i = 0; i < updateBtns.length; i++) {
	updateBtns[i].addEventListener('click', function(){
		var productoId = this.dataset.producto
		var action = this.dataset.action
		console.log('productoId:', productoId, 'action:', action)
        console.log('USER:', user)

		if (user == 'AnonymousUser'){
			
			console.log('User is not authenticated')
			
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
				'Content-Type':'application/json', //este linea importantisima para el post
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