let json = '{"text": "good text"}';

let obj = JSON.parse(json);

function fix_demo() {
	document.getElementById("demo").innerHTML = obj.text;
}
