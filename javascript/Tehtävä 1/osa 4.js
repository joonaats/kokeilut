const name = prompt('Type your name.')
const random = Math.floor(Math.random() * 4) + 1;

if (random == 1){
    document.querySelector('#name').innerHTML = name + ", you are a part of the Gryffindor house";
}

else if (random == 2){
    document.querySelector('#name').innerHTML = name + ", you are a part of the Slytherin house";
}

else if (random == 3){
    document.querySelector('#name').innerHTML = name + ", you are a part of the Hufflepuff house";
}

else if (random == 4){
    document.querySelector('#name').innerHTML = name + ", you are a part of the Ravenclaw house";
}
