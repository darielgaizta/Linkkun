function openMenu(open, close) {
	document.getElementById(open).style.display = 'block';
	document.getElementById(close).style.display = 'none';
	if (open === "signup") {
		document.getElementById('btn-signup').style.backgroundColor = 'skyblue';
		document.getElementById('btn-login').style.backgroundColor = 'initial';
	} else {
		document.getElementById('btn-signup').style.backgroundColor = 'initial';
		document.getElementById('btn-login').style.backgroundColor = 'skyblue';
	}
}

function popForm(id, value) {
	document.getElementById(id).style.display = value;
	if (id === "add" && value === "block"){
		document.getElementsByClassName('down')[0].style.display = 'none';
		document.getElementsByClassName('up')[0].style.display = 'block';
	} else if (id === "add" && value === "none"){
		document.getElementsByClassName('down')[0].style.display = 'block';
		document.getElementsByClassName('up')[0].style.display = 'none';
	}
	if (id === "delete" && value === "block"){
		document.getElementsByClassName('down')[1].style.display = 'none';
		document.getElementsByClassName('up')[1].style.display = 'block';
	} else if (id === "delete" && value === "none"){
		document.getElementsByClassName('down')[1].style.display = 'block';
		document.getElementsByClassName('up')[1].style.display = 'none';
	}
}