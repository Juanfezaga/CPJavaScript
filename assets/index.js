import MediaPlayer from './MediaPlayer.js'
import AutoPlay from './plugins/AutoPlay.js'
import AutoPause from './plugins/AutoPause.js'

const buttonM = document.querySelector("#muteButton")
const buttonP = document.querySelector('#playButton');
const video = document.querySelector('video')
const player = new MediaPlayer({ el: video, plugins: [
    new AutoPlay(),
    new AutoPause()
]})


buttonP.onclick = () => player.togglePlay();
buttonM.onclick = () => player.toggleVolume();


if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js').catch(
        e => console.log(e)
    )
}

