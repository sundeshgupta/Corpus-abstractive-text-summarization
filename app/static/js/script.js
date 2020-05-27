document.getElementById('form1').addEventListener('submit', function(event){
	event.preventDefault();
	var xhr = new XMLHttpRequest();
	var url = '/api/summarize';
	xhr.open('POST', url, 'true');
	xhr.onload = function() {
		if(xhr.readyState==4 && xhr.status == '200') {
			var res = JSON.parse(xhr.responseText);
			document.getElementById('summary').innerHTML = res.summary;
		}
		else {
			var res = '{"summary":"sample summary"}';
			var res1 = JSON.parse(res);
			document.getElementById('summary').innerHTML = res1.summary;
		}
	}
	var data = {};
	data.text = document.getElementById('textarea1').value;
	var json = JSON.stringify(data);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(json);
});
