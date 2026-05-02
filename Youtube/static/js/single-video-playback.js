const videoElements = document.querySelectorAll('video');

function handleVideoPlay(event) {
  // Pause all other videos except the one being played
  videoElements.forEach(video => {
    if (video !== event.target) {
      video.pause();
      console.log('moi')
    }
  });
}

videoElements.forEach(video => {
  video.addEventListener('play', handleVideoPlay);
});