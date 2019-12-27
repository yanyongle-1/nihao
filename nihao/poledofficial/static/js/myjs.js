var test = window.location.href;

var a = test.split('http://127.0.0.1:8000/')
var b = a.slice(1,2)
var c = b.toString().split('/')[0]

alert(c)