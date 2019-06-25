var itemarray=[];
var facarray=[];

function additems(){

  var str=document.getElementById('items').value;

  if (str!='')
  {

  itemarray.push(str);
  console.log(itemarray);
  var label=document.createElement("li");
  label.setAttribute('class','list-group-item');
  var labelnode=document.createTextNode(str);
  label.append(labelnode);
  var element=document.getElementById('additems');
  element.append(label);
  document.getElementById('items').value='';
  }

}

function addfacilities(){

  var str=document.getElementById('facility').value;


  if (str!='')
  {

  facarray.push(str);
  console.log(facarray);
  var label=document.createElement("li");
  label.setAttribute('class','list-group-item');
  var labelnode=document.createTextNode(str);
  label.append(labelnode);
  var element=document.getElementById('addfacilities');
  element.append(label);
  document.getElementById('facility').value='';
  }

}
