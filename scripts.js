//script

let options = Array.from(document.querySelectorAll('.option'));
let selectedIndex = 0;

function cycleOptions() {
    options[selectedIndex].classList.remove('selected');
    selectedIndex = (selectedIndex + 1) % options.length;
    options[selectedIndex].classList.add('selected');
}

let intervalID = setInterval(cycleOptions, 1000);

window.addEventListener('keydown', function(event) {
    if (event.code === 'Space') {
        clearInterval(intervalID);
    }
});
