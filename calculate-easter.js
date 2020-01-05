// calculate Easter

var Y = 2020; // year

var a = Y%19;
var b = Math.floor(Y/100);
var c = Y%100;
var d = Math.floor(b/4);
var e = b%4;
var f = Math.floor((b+8)/25);
var g = Math.floor((b-f+1)/3);
var h = (19*a + b - d - g + 15)%30;
var i = Math.floor(c/4);
var k = c%4;
var l = (32 + 2*e + 2*i - h - k)%7;
var m = Math.floor((a+11*h + 22*l)/451);
var month = Math.floor((h+l-7*m+114)/31);
var day = ((h+l-7*m+114)%31) + 1

console.log(month,day);
