import MediaPlayer from './MediaPlayer.js'
import AutoPlay from './plugins/AutoPlay.js'

const buttonM = document.querySelector("#muteButton")
const buttonP = document.querySelector('#playButton');
const video = document.querySelector('video')
const player = new MediaPlayer({ el: video, plugins: [
    //new AutoPlay()
]})


buttonP.onclick = () => player.togglePlay();
buttonM.onclick = () => player.toggleVolume();




