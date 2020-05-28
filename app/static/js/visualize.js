function createtable(res) {
  var table = document.getElementById('table1');
  table.innerHTML='';
  for (var key in res) {
    var tr = document.createElement('tr');
    var td1 = document.createElement('td');
    var td2 = document.createElement('td');
    td1.innerHTML = key;
    td2.innerHTML = res[key];
    tr.appendChild(td1);
    tr.appendChild(td2);
    table.appendChild(tr);
  }
}

function createtable2(res) {
  var table = document.getElementById('table1');
  table.innerHTML='';
  var tr = document.createElement('tr');
  var th = document.createElement('th');
  th.innerHTML = 'PROPERTY';
  tr.appendChild(th);
  table.appendChild(tr);
  for (var key in res['cnn']) {
    var tr = document.createElement('tr');
    var td = document.createElement('td');
    td.innerHTML = key;
    tr.appendChild(td);
    table.appendChild(tr);
  }
  dict = {'cnn': 'CNN_DAILYMAIL', 'free': 'GIGAWORD', 'giga': 'FREE PRESS JOURNAL', 'hindustan': 'HINDUSTAN TIMES'};
  var j = 0;
  for (var key in res) {
    var i = 0;
    var th = document.createElement('th');
    table.rows[i].appendChild(th);
    i++;
    th.innerHTML = dict[key];
    for (var key1 in res[key]) {
      var tr = document.createElement('tr');
      var td = document.createElement('td');
      td.innerHTML = res[key][key1];
      console.log(key1);
      console.log(i);
      table.rows[i].appendChild(td);
      i++;
    }
  }
}

function images(res) {
  list = ['_mean_cmp_ratio.png', '_mean_ext_coverage.png', '_mean_ext_density.png', '_mean_word_article.png', '_mean_word_highlight.png'];
  var staturl = 'static/img/'
  for(var i=0; i < 5; i++) {
    list[i]=staturl+res+list[i];
  }
  console.log(list);
  document.getElementById('img1').src=list[0];
  document.getElementById('img2').src=list[1];
  document.getElementById('img3').src=list[2];
  document.getElementById('img4').src=list[3];
  document.getElementById('img5').src=list[4];
}

function radiobutton()
{
  var dataset = document.querySelector('input[name = dataset]:checked');
  if(!dataset)
  {
    console.log('dataset');
    return false;
  }
  var xhr = new XMLHttpRequest();
  var url = '/api/visualize';
  xhr.open('POST', url, 'true');
  xhr.onload = function() {
    if(xhr.readyState==4 && xhr.status == '200') {
      var res = JSON.parse(xhr.responseText);
      console.log(xhr.responseText);
      console.log(res);
      createtable(res);
      images(dataset.value);
    }
  }
  xhr.setRequestHeader('Content-Type', 'text/plain');
  xhr.send(dataset.value);
}

function compare() {
  var ele = document.getElementsByName("dataset");
  for(var i=0;i<ele.length;i++)
    ele[i].checked = false;
  document.getElementById('img1').src='';
  document.getElementById('img2').src='';
  document.getElementById('img3').src='';
  document.getElementById('img4').src='';
  document.getElementById('img5').src='';
  var xhr = new XMLHttpRequest();
  var url = '/api/visualize';
  xhr.open('POST', url, 'true');
  xhr.onload = function() {
    if(xhr.readyState==4 && xhr.status == '200') {
      var res = JSON.parse(xhr.responseText);
      createtable2(res);
    }
  }
  xhr.setRequestHeader('Content-Type', 'text/plain');
  xhr.send('all');
}

var rad = document.getElementsByName('dataset');
for (var i = 0; i < rad.length; i++) {
    rad[i].addEventListener('change', radiobutton);
}

document.getElementById('button2').addEventListener('click', compare);