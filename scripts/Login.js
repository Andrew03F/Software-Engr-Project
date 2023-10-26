window.onload = function() {
	// makes submitHandler be call ever time submit event happens
    document.getElementById('loginForm').addEventListener("submit", submitHandler);
  };

function submitHandler(event) {
	
	event.preventDefault(event);
	const username = document.getElementById('username').value;
	const password = document.getElementById('password').value;

	console.log('Username:', username);
	console.log('Password:', password);
}


