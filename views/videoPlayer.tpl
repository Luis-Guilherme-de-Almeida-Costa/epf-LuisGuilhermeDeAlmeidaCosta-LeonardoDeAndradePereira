% include('includes/headerNaoLogado.tpl')
<link rel="stylesheet" href="/static/css/styleGeneral.css">
<link rel="stylesheet" href="/static/css/videoPlayer.css">
% include('includes/nav.tpl')

<div class="video-player">
    <div>
        <video id="customVideo" src="/{{video_path}}" class="video-element"></video>

        <div class="controls">
            <button id="playPauseBtn">▶️</button>

            <input type="range" id="seekBar" value="0" min="0" max="100">

            <span id="currentTime">0:00</span> / 
            <span id="totalTime">0:00</span>

            <input type="range" id="volumeBar" min="0" max="1" step="0.01" value="1">
            <button id="muteBtn">🔊</button>

            <button id="fullscreenBtn">⛶</button>
        </div>
    </div>
</div>

% include('includes/footerSemContato.tpl')