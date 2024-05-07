

document.getElementById("nocturne").onmouseover = function() {mouseOver()};
document.getElementById("nocturne").onmouseout = function() {mouseOut()};

function mouseOver() {  
  document.getElementById("nocturne").style.color = "#dea2fe";
  document.getElementById("nocturne").style.backgroundColor="black";
  document.getElementById("nocturne").style.height="28px";
}

function mouseOut() {
  document.getElementById("nocturne").style.color = "black";
  document.getElementById("nocturne").style.backgroundColor="rgba(255, 255, 255, 0)";
  document.getElementById("nocturne").style.height="25px";
}
document.getElementById("art").onmouseover = function() {mouseOver2()};
document.getElementById("art").onmouseout = function() {mouseOut2()};

function mouseOver2() {  
  document.getElementById("art").style.color = "#dea2fe";
  document.getElementById("art").style.backgroundColor="black";
  document.getElementById("art").style.height="28px";
}

function mouseOut2() {
  document.getElementById("art").style.color = "black";
  document.getElementById("art").style.backgroundColor="rgba(255, 255, 255, 0)";
  document.getElementById("art").style.height="25px";
}
document.getElementById("abt").onmouseover = function() {mouseOver3()};
document.getElementById("abt").onmouseout = function() {mouseOut3()};

function mouseOver3() {  
  document.getElementById("abt").style.color = "#dea2fe";
  document.getElementById("abt").style.backgroundColor="black";
  document.getElementById("abt").style.height="28px";
}

function mouseOut3() {
  document.getElementById("abt").style.color = "black";
  document.getElementById("abt").style.backgroundColor="rgba(255, 255, 255, 0)";
  document.getElementById("abt").style.height="25px";
}
document.getElementById("sea").onmouseover = function() {mouseOver4()};
document.getElementById("sea").onmouseout = function() {mouseOut4()};

function mouseOver4() {  
  document.getElementById("sea").style.color = "#dea2fe";
  document.getElementById("sea").style.backgroundColor="black";
  document.getElementById("sea").style.height="28px";
}

function mouseOut4() {
  document.getElementById("sea").style.color = "black";
  document.getElementById("sea").style.backgroundColor="rgba(255, 255, 255, 0)";
  document.getElementById("sea").style.height="25px";
}
document.getElementById("spo").onmouseover = function() {mouseOver5()};
document.getElementById("spo").onmouseout = function() {mouseOut5()};

function mouseOver5() {  
  document.getElementById("spo").style.color = "#dea2fe";
  document.getElementById("spo").style.backgroundColor="black";
  document.getElementById("spo").style.height="28px";
}

function mouseOut5() {
  document.getElementById("spo").style.color = "black";
  document.getElementById("spo").style.backgroundColor="rgba(255, 255, 255, 0)";
  document.getElementById("spo").style.height="25px";
}


document.getElementById("pla").onmouseover = function() {mouseOver6()};
document.getElementById("pla").onmouseout = function() {mouseOut6()};

function mouseOver6() {  
  document.getElementById("pla").style.color = "#dea2fe";
  document.getElementById("pla").style.backgroundColor="black";
  document.getElementById("pla").style.height="28px";
}

function mouseOut6() {
  document.getElementById("pla").style.color = "black";
  document.getElementById("pla").style.backgroundColor="rgba(255, 255, 255, 0)";
  document.getElementById("pla").style.height="25px";
}

const texts = ['ARTIST SPOTLIGHT'];
let word = 0; 
let letterIndex = 0; 
let currentText = ''; 
let letter = ''; 

(function type() {
 
    
  currentText = texts[word];
  letter = currentText.slice(0, ++letterIndex);
  document.querySelector('#typing').textContent = letter;

  if (letter.length == currentText.length) {
    word++;
    letterIndex = 0;
  }
  
  setTimeout(type, 300);
})();


  var countDownDate = new Date("June 30, 2023 00:00:00").getTime();

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();
    
  // Find the distance between now and the count down date
  var distance = countDownDate - now;
    
  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);
    
  // Output the result in an element with id="demo"
  document.querySelector('.days').textContent = days;
  document.querySelector('.hours').textContent = hours;
  document.querySelector('.minutes').textContent = minutes;
  document.querySelector('.seconds').textContent = seconds;
    
  // If the count down is over, write some text 
  if (distance < 0) {
    clearInterval(x);
    document.querySelector("countdown-container").innerHTML = "EXPIRED";
  }
}, 1000);

let rating = localStorage.getItem('rating')
let rev = localStorage.getItem('rev')
let user = localStorage.getItem('user')
let artist = localStorage.getItem('artist')
var dict={}
function returnText() {
    var ele = document.getElementsByName('btn_radio');
    rev = document.getElementById("revInput").value;
    user = document.getElementById("userInput").value;
    artist = document.getElementById("artInput").value;
    for(i = 0; i < ele.length; i++) {
        if(ele[i].checked)
        {rating=ele[i].value;
        }
        }
    
    localStorage.setItem('rating', rating);
    localStorage.setItem('user', user);
    localStorage.setItem('rev', rev);
    localStorage.setItem('artist', artist);
    dict = {
      user: user,
      rev: rev,
      rating: rating,
      artist: artist
    };


    let table = document.getElementById("ratings");

    let row = table.insertRow(-1); 
 
    let c1 = row.insertCell(0);
    let c2 = row.insertCell(1);
    let c3 = row.insertCell(2);
    let c4 = row.insertCell(3);

    c1.innerText = user
    c2.innerText = artist
    c3.innerText = rev
    c4.innerText = rating
        
   document.getElementById('userInput').value="";
   document.getElementById('revInput').value="";
   document.getElementById('artInput').value="";
   for(i = 0; i < ele.length; i++) {
    if(ele[i].checked)
    {ele[i].checked=false;
    }
    }

  
}
console.log(user)

/*
zoomin();
zoomout();
let image = document.querySelector('#zoom img');
function zoomin() {
   let width = image.clientWidth;
   let height = image.clientHeight;
   image.style.width = (width + 5) + "%";
   image.style.height = (height + 5) + "%";
  
}

function zoomout() {
  document.getElementById("nocturne").style.backgroundColor="black";
   let width = image.clientWidth;
   let height = image.clientHeight;
   image.style.width = (width - 50) + "%";
   image.style.height = (height - 50) + "%";
   zoomin();
}

const zoomImg = document.querySelector('#zoom img');
let scale = 1;
let direction = 1;

function zoomInOut() {
  if (scale < 1) {
    direction = 1;
  } else if (scale > 1.2) {
    direction = -1;
  }
  scale += direction * 0.02;
  zoomImg.style.transform = `scale(${scale})`;
  requestAnimationFrame(zoomInOut);
}

zoomInOut();
*/


const picture = document.getElementById("zoom");
 
// Set the initial scale value
let scale = 1;

// Define the animation loop function
function animate() {
  scale = scale === 1 ? 1.1 : 1;
  picture.style.transform = `scale(${scale})`;
  setTimeout(animate, 2000);
}

animate();

