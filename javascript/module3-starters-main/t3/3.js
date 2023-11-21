'use strict';
const names = ['John', 'Paul', 'Jones'];
let list = ""
for (let i = 0; i < 3; i++) {
    list += "<li>" + names[i] + "</li>"
}
document.querySelector('#target').innerHTML = list;
