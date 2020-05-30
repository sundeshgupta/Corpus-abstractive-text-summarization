document.getElementById('form1').addEventListener('submit', function(event){
	event.preventDefault();
	document.getElementById('summary2').innerHTML = "Processing... (This may take upto 5-10 seconds)";
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
			document.getElementById('summary1').innerHTML = res1.summary;
		}
	}
	var data = {};
	data.text = document.getElementById('textarea1').value;
	data.type = 'extractive';
	var json = JSON.stringify(data);
	xhr.setRequestHeader('Content-Type', 'application/json');
	xhr.send(json);
	var xhr1 = new XMLHttpRequest();
	xhr1.open('POST', url, 'true');
	xhr1.onload = function() {
		if(xhr1.readyState==4 && xhr1.status == '200') {
			var res = JSON.parse(xhr1.responseText);
			document.getElementById('summary2').innerHTML = res.summary;
		}
		else {
			var res = '{"summary":"sample summary"}';
			var res1 = JSON.parse(res);
			document.getElementById('summary').innerHTML = res1.summary;
		}
	}
	var data1 = {};
	data1.text = document.getElementById('textarea1').value;
	data1.type = 'abstractive';
	var json1 = JSON.stringify(data1);
	xhr1.setRequestHeader('Content-Type', 'application/json');
	xhr1.send(json1);
});
