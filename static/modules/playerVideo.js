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
    const videoContainer = document.querySelector('.video-container');

    // Função auxiliar para formatar o tempo (segundos para M:SS)
    const formatTime = (timeInSeconds) => {
        const minutes = Math.floor(timeInSeconds / 60);
        const seconds = Math.floor(timeInSeconds % 60);
        return `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;
    };

    // ===================================
    // 1. Lógica de Play/Pause
    // ===================================
    const togglePlayPause = () => {
        if (video.paused || video.ended) {
            video.play();
            playPauseBtn.innerHTML = '⏸️';
        } else {
            video.pause();
            playPauseBtn.innerHTML = '▶️';
        }
    };
    
    playPauseBtn.addEventListener('click', togglePlayPause);
    video.addEventListener('click', togglePlayPause); // Clique no vídeo também faz Play/Pause

    // ===================================
    // 2. Tempo e Barra de Progresso
    // ===================================

    // Quando o vídeo carrega metadados (duração)
    video.addEventListener('loadedmetadata', () => {
        totalTimeDisplay.textContent = formatTime(video.duration);
        seekBar.max = video.duration;
    });

    // Atualiza o progresso e o tempo enquanto o vídeo toca
    video.addEventListener('timeupdate', () => {
        // Atualiza a barra de busca
        seekBar.value = video.currentTime;
        
        // Atualiza o tempo de exibição
        currentTimeDisplay.textContent = formatTime(video.currentTime);
    });

    // Permite que o usuário busque no vídeo
    seekBar.addEventListener('input', () => {
        video.currentTime = seekBar.value;
    });

    // ===================================
    // 3. Lógica de Volume
    // ===================================

    // Quando o usuário move a barra de volume
    volumeBar.addEventListener('input', () => {
        video.volume = volumeBar.value;
        if (video.volume === 0) {
            muteBtn.innerHTML = '🔇';
        } else {
            muteBtn.innerHTML = '🔊';
        }
    });

    // Lógica do botão Mute
    muteBtn.addEventListener('click', () => {
        if (video.muted) {
            video.muted = false;
            muteBtn.innerHTML = '🔊';
            volumeBar.value = video.volume > 0 ? video.volume : 1;
        } else {
            video.muted = true;
            muteBtn.innerHTML = '🔇';
            volumeBar.value = 0;
        }
    });

    // ===================================
    // 4. Lógica de Tela Cheia
    // ===================================
    fullscreenBtn.addEventListener('click', () => {
        if (document.fullscreenElement) {
            document.exitFullscreen();
            fullscreenBtn.innerHTML = '⛶'; // Icone de entrar em fullscreen
        } else {
            videoContainer.requestFullscreen();
            fullscreenBtn.innerHTML = ' Minimize'; // Ícone de sair do fullscreen
        }
    });
    
    // Atualiza o ícone do botão quando o estado de fullscreen muda (ex: apertando ESC)
    document.addEventListener('fullscreenchange', () => {
        if (document.fullscreenElement) {
            fullscreenBtn.innerHTML = ' Minimize';
        } else {
            fullscreenBtn.innerHTML = '⛶';
        }
    });
}