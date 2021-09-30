//changeColor(): Đổi màu chữ của 3 đoạn văn theo thứ tự xanh, vàng, đỏ.
function changeColor() {
  // var x = document.querySelectorAll("p");
  // var y = document.querySelectorAll("h2");

  // y[0].style.color = "red";
  // y[1].style.color = "blue";
  // y[2].style.color = "purple";
  // x[0].style.color = "red";
  // x[1].style.color = "blue";
  // x[2].style.color = "purple";

  document.getElementById("p1").style.color = "red";
}

function changeBgColor(color) {
  document.body.style.background = color;
}

//Thay đổi nội dung của đoạn văn paragraph1 thành giống nội dung của đoạn văn paragraph2 (tham số truyền vào là id của 2 đoạn văn hoặc thứ tự của đoạn văn).
function copyContent(paragraph1, paragraph2) {
  document.getElementById(paragraph1).innerHTML =
    document.getElementById(paragraph2).innerHTML;
}

//Thay đổi kích thước font chữ của cả 3 đoạn văn thành x pixels (x là một số nguyên).
function changeFontSize(x) {
  document.body.style.fontSize = x + "px";
}

function increaseFontSize(paragraph) {
  var inc = document.getElementById(paragraph);
  var style = window.getComputedStyle(inc, null).getPropertyValue("font-size");
  var fontSize = parseFloat(style);
  if (fontSize == 30) {
    return;
  }
  inc.style.fontSize = fontSize + 1 + "px";
}

function decreaseFontSize(paraph) {
  var el = document.getElementById(paraph);
  var style = window.getComputedStyle(el, null).getPropertyValue("font-size");
  var fontSize = parseFloat(style);
  if (fontSize == 10.0) {
    return;
  }
  el.style.fontSize = fontSize - 1 + "px";
}
