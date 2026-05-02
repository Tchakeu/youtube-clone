var menuIcon = document.querySelector(".menu-icon");
var sidebar = document.querySelector(".sidebar");
var container = document.querySelector(".container");
var containers = document.querySelector(".containers");
var video = document.querySelector('.video-container video');
var videoid = document.querySelector('.side-video-list video');

menuIcon.onclick = function(){
    sidebar.classList.toggle("small-sidebar");
    container.classList.toggle("large-container")
    containers.classList.toggle("large-containers")
}
function playVideo(videoElement) {
  videoElement.play();
  videoElement.muted = false; // Unmute on play
  videoElement.controls.style.display = 'block'; // Show controls on hover
}

function pauseVideo(videoElement) {
  videoElement.pause();
  videoElement.muted = true; // Mute on pause
  videoElement.controls.style.display = 'none'; // Hide controls on mouseout
}

function playVideoid(videoElement) {
  videoElement.play();
  //videoElement.muted = false; // Unmute on play
  videoElement.controls.style.display = 'block'; // Show controls on hover
}

function pauseVideoid(videoElement) {
  videoElement.pause();
  //videoElement.muted = false; // Mute on pause
  videoElement.controls.style.display = 'none'; // Hide controls on mouseout
}


