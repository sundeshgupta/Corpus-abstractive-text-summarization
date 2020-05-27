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
      createtable(res);
      images(dataset.value);
    }
    else {
      createtable(JSON.parse('{"abcd":"1" }'));
      console.log('hey');
    }
  }
  xhr.setRequestHeader('Content-Type', 'text/plain');
  xhr.send(dataset.value);
}

var rad = document.getElementsByName('dataset');
console.log(rad);
for (var i = 0; i < rad.length; i++) {
    rad[i].addEventListener('change', radiobutton);
}