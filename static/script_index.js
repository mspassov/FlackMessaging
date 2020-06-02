document.addEventListener('DOMContentLoaded', function(){

	if(!localStorage.getItem('username')){
		document.querySelector('h3').innerHTML = "It's your first time here! Please pick a Display Name: "

		document.querySelector('#firstForm').onsubmit = function(){
			let user = document.querySelector('#user_input').value;
			localStorage.setItem('username', user);
			return true;
		}
	}
	else{
		document.querySelector('h3').innerHTML = `Welcome Back, ${localStorage.getItem('username')}!`;
		document.querySelector('#user_input').value = localStorage.getItem('username');

		document.querySelector('#firstForm').onsubmit = function(){
			let user = document.querySelector('#user_input').value;
			localStorage.setItem('username', user);
			return true;
		}
		
	}
})