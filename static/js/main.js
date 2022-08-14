
const form = document.getElementById('form');
const firstname = document.getElementById('id_first_name');
const lastname = document.getElementById('id_last_name');
const phone = document.getElementById('id_phone');

const email = document.getElementById('id_email');
const password = document.getElementById('id_password1');
const password2 = document.getElementById('id_password2');

// form.addEventListener('submit', e => {
// 	e.preventDefault();
	
// 	checkInputs();
// });

function checkInputs() {
	// trim to remove the whitespaces
	const firstnameValue = firstname.value.trim();
	const lastnameValue = lastname.value.trim();
	const phoneValue = phone.value.trim();

	const emailValue = email.value.trim();
	const passwordValue = password.value.trim();
	const password2Value = password2.value.trim();
	
	if(firstnameValue === '') {
		setErrorFor(firstname, 'First name cannot be blank');
	} else {
		setSuccessFor(firstname);
	}

	if(lastnameValue === '') {
		setErrorFor(lastname, 'Last name cannot be blank');
	} else {
		setSuccessFor(lastname);
	}

	if(phoneValue === '') {
		setErrorFor(phone, 'Last name cannot be blank');
	} else {
		setSuccessFor(phone);
	}
	
	if(emailValue === '') {
		setErrorFor(email, 'Email cannot be blank');
	} else if (!isEmail(emailValue)) {
		setErrorFor(email, 'Not a valid email');
	} else {
		setSuccessFor(email);
	}
	
	if(passwordValue === '') {
		setErrorFor(password, 'Password cannot be blank');
	} else {
		setSuccessFor(password);
	}
	
	if(password2Value === '') {
		setErrorFor(password2, 'Password2 cannot be blank');
	} else if(passwordValue !== password2Value) {
		setErrorFor(password2, 'Passwords does not match');
	} else{
		setSuccessFor(password2);
	}
}

function setErrorFor(input, message) {
	const formControl = input.parentElement;
	const small = formControl.querySelector('small');
	formControl.className = 'form-control error';
	small.innerText = message;
}

function setSuccessFor(input) {
	const formControl = input.parentElement;
	formControl.className = 'form-control success';
}
	
// function isEmail(email) {
// 	return /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/.test(email);
// }

