//script

var options = Array.from(document.querySelectorAll('.option'));
const undoIndex = options.length - 1;
const message = document.getElementById('message');
var selectedIndex = 0;

function cycleOptions() {
    options[selectedIndex].classList.remove('selected');
    selectedIndex = (selectedIndex + 1) % options.length;
    options[selectedIndex].classList.add('selected');
}

let intervalID = setInterval(cycleOptions, 1000);

window.addEventListener('keydown', function (event) {
    if (event.code === 'Space') {
        if (selectedIndex == undoIndex) {
            message.removeChild(message.lastElementChild);
        } else {
            message.appendChild(options[selectedIndex].cloneNode(true))
        }
    }
});

var threshold = 230;

// Check browser compatibility
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
    // Request access to the microphone
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then(function (stream) {
            // Create an AudioContext
            const audioContext = new (window.AudioContext || window.webkitAudioContext)();

            // Create a MediaStreamAudioSourceNode
            const microphone = audioContext.createMediaStreamSource(stream);

            // Connect to other audio nodes (e.g., AnalyserNode, GainNode, etc.) or do further processing
            // Create an AudioContext and microphone source (as described in the previous answer)

            // Create an AnalyserNode
            const analyser = audioContext.createAnalyser();

            // Set parameters for the AnalyserNode
            analyser.fftSize = 256; // You can adjust the size for your specific needs
            analyser.smoothingTimeConstant = 0.8; // Adjust for smoothing

            // Connect the AnalyserNode to the microphone source
            microphone.connect(analyser);
            var isOn = false;
            // Function to detect peaks
            function detectPeak() {

                const dataArray = new Uint8Array(analyser.frequencyBinCount);
                analyser.getByteFrequencyData(dataArray);

                // Loop through the dataArray and find peaks
                let peakDetected = false;
                for (let i = 0; i < dataArray.length; i++) {
                    if (dataArray[i] > threshold) {
                        // Peak detected
                        peakDetected = true;
                        console.log(dataArray[i])
                        break;
                    }
                }

                if (peakDetected) {
                    if (!isOn) {
                        console.log("Peak detected!");
                        if (selectedIndex == undoIndex) {
                            message.removeChild(message.lastElementChild);
                        } else {
                            message.appendChild(options[selectedIndex].cloneNode(true))
                        }
                    }
                    isOn = true;
                    detectPeakInterval = setTimeout(detectPeak, 100); // Adjust the interval as needed
                } else {
                    isOn = false;
                    detectPeakInterval = setTimeout(detectPeak, 100); // Adjust the interval as needed
                }

                // Call this function periodically using requestAnimationFrame or setInterval
            }

            // Call detectPeak periodically
            detectPeak();
            // Start audio processing or play audio here
        })
        .catch(function (error) {
            console.error('Error accessing microphone:', error);
        });
} else {
    console.error('Web Audio API is not supported in this browser.');
}


// 