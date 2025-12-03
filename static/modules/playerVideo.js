const path = window.location.pathname;

if(path.includes("/home/video")) {
    console.log("oi")
    const video = document.getElementById('customVideo');
    const playPauseBtn = document.getElementById('playPauseBtn');
    const seekBar = document.getElementById('seekBar');
    const volumeBar = document.getElementById('volumeBar');
    const muteBtn = document.getElementById('muteBtn');
    const fullscreenBtn = document.getElementById('fullscreenBtn');
    const currentTimeDisplay = document.getElementById('currentTime');
    const totalTimeDisplay = document.getElementById('totalTime');
    const videoContainer = document.querySelector('.video-player');

    const formatTime = (timeInSeconds) => {
        const minutes = Math.floor(timeInSeconds / 60);
        const seconds = Math.floor(timeInSeconds % 60);
        return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    };

    const togglePlayPause = () => {
        if (video.paused || video.ended) {
            video.play();
            playPauseBtn.innerHTML = '<img src="/static/Images/pause.png" width=30/>';
        } else {
            video.pause();
            playPauseBtn.innerHTML = '<img src="/static/Images/play.png" width=30/>';
        }
    };
    
    playPauseBtn.addEventListener('click', togglePlayPause);
    video.addEventListener('click', togglePlayPause);

    video.addEventListener('loadedmetadata', () => {
        totalTimeDisplay.textContent = formatTime(video.duration);
        seekBar.max = video.duration;
    });

    video.addEventListener('timeupdate', () => {
        seekBar.value = video.currentTime;
        
        currentTimeDisplay.textContent = formatTime(video.currentTime);
    });

    seekBar.addEventListener('input', () => {
        video.currentTime = seekBar.value;
    });

    volumeBar.addEventListener('input', () => {
        video.volume = volumeBar.value;
        if (video.volume === 0) {
            muteBtn.innerHTML = '<img src="/static/Images/headsetoff.png" width=30/>';
        } else {
            muteBtn.innerHTML = '<img src="/static/Images/headset.png" width=30/>';
        }
    });

    muteBtn.addEventListener('click', () => {
        if (video.muted) {
            video.muted = false;
            muteBtn.innerHTML = '<img src="/static/Images/headset.png" width=30/>';
            volumeBar.value = video.volume > 0 ? video.volume : 1;
        } else {
            video.muted = true;
            muteBtn.innerHTML = '<img src="/static/Images/headsetoff.png" width=30/>';
            volumeBar.value = 0;
        }
    });
    fullscreenBtn.addEventListener('click', async () => {
        if (document.fullscreenElement) {
            await document.exitFullscreen();
            videoContainer.classList.remove('is-fullscreen');
            
            fullscreenBtn.innerHTML = '<img src="/static/Images/fullscreen.png" width=30/>';
        
        } else {
            try {
                await videoContainer.requestFullscreen();
            
                videoContainer.classList.add('is-fullscreen');
                
                fullscreenBtn.innerHTML = '<img src="/static/Images/fullscreenexit.png" width=30/>';
                
            } catch (error) {
                console.error("Erro ao tentar ativar o modo tela cheia:", error);
            }
        }
    });
    document.addEventListener('fullscreenchange', () => {
        if (!document.fullscreenElement) {
            videoContainer.classList.remove('is-fullscreen');
            fullscreenBtn.innerHTML = '<img src="/static/Images/fullscreen.png" width=30/>';
        }
    });
    
    document.addEventListener('fullscreenchange', () => {
        
        if (document.fullscreenElement) {
            fullscreenBtn.innerHTML = '<img src="/static/Images/fullscreenexit.png" width=30/>';
        } else {
            fullscreenBtn.innerHTML = '<img src="/static/Images/fullscreen.png" width=30/>';
        }
    });
}