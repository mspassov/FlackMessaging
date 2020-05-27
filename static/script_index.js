document.addEventListener('DOMContentLoaded', function(){

	if(!localStorage.getItem('username')){

		document.querySelector('#firstForm').onsubmit = function(){
			let user = document.querySelector('#user_input').value;
			localStorage.setItem('username', user);
			document.querySelector('h3').innerHTML = `Display Name: ${user}`;
			return false;
		}
	}
	else{
		document.querySelector('#user_input').remove();
		document.querySelector('h3').innerHTML = `Display Name: ${localStorage.getItem('username')}`;
	}
})