const APP_ID = ""
const CHANNEL = sessionStorage.getItem('room')
const TOKEN = sessionStorage.getItem('token')
let UID = Number(sessionStorage.getItem('UID'))

let NAME = sessionStorage.getItem('name')
const client = AgoraRTC.createClient({ mode: 'rtc', codec: 'vp8' })

let localTracks = []

let remoteUsers = {}

let localScreenTracks;
let sharingScreen = false;


let displayFrame = document.getElementById('video-streambox')
let videoFrames = document.getElementsByClassName('video-container')
let userIdInDisplayFrame = null;

let expandVideoFrame = (e) => {
    let child = displayFrame.children[0]
    if (child) {
        document.getElementById('video-streams').appendChild(child)
    }
    displayFrame.style.display = 'block'
    displayFrame.appendChild(e.currentTarget)
    userIdInDisplayFrame = e.currentTarget.id

}

for (let i = 0; videoFrames.length > i; i++){
    videoFrames[i].addEventListener('click',expandVideoFrame)
}

let hideDisplayFrame = () => {
    userIdInDisplayFrame = null
    displayFrame.style.display = null

    let child = displayFrame.children[0]
    document.getElementById('video-streams').appendChild(child)

}

displayFrame.addEventListener('click', hideDisplayFrame)

let joinAndDisplayLocalStreams = async () => {

    document.getElementById('room-name').innerHTML = CHANNEL

    client.on('user-published', handleUserJoined)
    client.on('user-left',handleUserLeft)
    try {
        await client.join(APP_ID, CHANNEL, TOKEN, UID)
    } catch (error) {
        console.log(error)
        window.open('/videochat/','_self')
    }
    
    localTracks = await AgoraRTC.createMicrophoneAndCameraTracks()

    let member = await createMember()

    let player = `<div  class="video-container" id="user-container-${UID}">
                     <div class="video-player" id="user-${UID}"></div>
                     <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
                  </div>`

    document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
    document.getElementById(`user-container-${UID}`).addEventListener('click', expandVideoFrame)
    localTracks[1].play(`user-${UID}`)

    await client.publish([localTracks[0], localTracks[1]])
}

let handleUserJoined = async (user, mediaType) => {
    remoteUsers[user.uid] = user
    await client.subscribe(user, mediaType)

    if (mediaType === 'video') {
        let player = document.getElementById(`user-container-${user.uid}`)

        if (player != null) {
            player.remove()
        }

        let member = await getMember(user)

        player = `<div  class="video-container" id="user-container-${user.uid}">
            <div class="video-player" id="user-${user.uid}"></div>
            <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
        </div>`


        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
        document.getElementById(`user-container-${user.uid}`).addEventListener('click', expandVideoFrame)

        user.videoTrack.play(`user-${user.uid}`)
    }
    if (mediaType === 'audio') {
        user.audioTrack.play()
    }
}

let handleUserLeft = async(user) =>{
    delete remoteUsers[user.uid]
    document.getElementById(`user-container-${user.uid}`).remove()
}

let leaveAndRemoveLocalStream = async () => {
    for (let i=0; localTracks.length > i; i++){
        localTracks[i].stop()
        localTracks[i].close()
    }

    await client.leave()
    deleteMember()
    window.open('/videochat/', '_self')
}

let toggleCamera = async (e) => {
    console.log('TOGGLE CAMERA TRIGGERED')
    if(localTracks[1].muted){
        await localTracks[1].setMuted(false)
        e.target.style.backgroundColor = '#fff'
    }else{
        await localTracks[1].setMuted(true)
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
    }
}

let toggleMic = async (e) => {
    console.log('TOGGLE MIC TRIGGERED')
    if(localTracks[0].muted){
        await localTracks[0].setMuted(false)
        e.target.style.backgroundColor = '#fff'
    }else{
        await localTracks[0].setMuted(true)
        e.target.style.backgroundColor = 'rgb(255, 80, 80, 1)'
    }
}


let toggleScreen = async (e) => {
    console.log('TOGGLE MICbbb TRIGGERED')
    let screenButton = e.currentTarget
    let cameraButton = document.getElementById('camera-btn')
    if (!sharingScreen) {
        sharingScreen = true
        cameraButton.style.display = 'none'
        screenButton.style.backgroundColor = 'rgb(255, 80, 80, 1)'
        localScreenTracks = await AgoraRTC.createScreenVideoTrack()
        document.getElementById(`user-container-${UID}`).remove()
        let player = `<div  class="video-container" id="user-container-${UID}">
            <div class="video-player" id="user-${UID}"></div>
        </div>`
        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)
        userIdInDisplayFrame = `user-container-${UID}`
        localScreenTracks.play(`user-${UID}`)

        await client.unpublish([localTracks[1]])
        await client.publish([localScreenTracks])

    } else {
        sharingScreen = false 
        cameraButton.style.display = 'block'
        screenButton.style.backgroundColor = '#fff'
        document.getElementById(`user-container-${UID}`).remove()
        await client.unpublish([localScreenTracks])

        let member = await createMember()

        let player = `<div  class="video-container" id="user-container-${UID}">
                        <div class="video-player" id="user-${UID}"></div>
                        <div class="username-wrapper"><span class="user-name">${member.name}</span></div>
                    </div>`

        document.getElementById('video-streams').insertAdjacentHTML('beforeend', player)

        localTracks[1].play(`user-${UID}`)

        await client.publish([localTracks[0], localTracks[1]])
    }
}


let createMember = async () => {
    let response = await fetch('/videochat/create_member/', {
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'name':NAME, 'room_name':CHANNEL, 'UID':UID})
    })
    let member = await response.json()
    return member
}


let getMember = async (user) => {
    let response = await fetch(`/videochat/get_member/?UID=${user.uid}&room_name=${CHANNEL}`)
    let member = await response.json()
    return member
}

let deleteMember = async () => {
    let response = await fetch('/videochat/delete_member/', {
        method:'POST',
        headers: {
            'Content-Type':'application/json'
        },
        body:JSON.stringify({'name':NAME, 'room_name':CHANNEL, 'UID':UID})
    })
    let member = await response.json()
}

window.addEventListener("beforeunload",deleteMember);


joinAndDisplayLocalStreams()


document.getElementById('leave-btn').addEventListener('click', leaveAndRemoveLocalStream)
document.getElementById('camera-btn').addEventListener('click', toggleCamera)
document.getElementById('mic-btn').addEventListener('click', toggleMic)
document.getElementById('screen').addEventListener('click', toggleScreen)