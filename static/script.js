var socket = io();
var clientId;
var myName = chance.word({ length: 5 });
var lastName = chance.word({ length: 7 });

myName = myName[0].toUpperCase() + myName.slice(1, myName.length)
lastName = lastName[0].toUpperCase() + lastName.slice(1, lastName.length)

console.log('Your random name is : ', myName, lastName);

const messagesDiv = document.getElementById('messages');
const pingButton = document.getElementById('ping-btn');
const messageButton = document.getElementById('msg-btn');
const messageTextBox = document.getElementById('msg-txtbox');

nameTag = document.createElement('h2')
nameTag.innerText =`${myName} ${lastName}`;
document.querySelector('.profile').appendChild(nameTag);

socket.on('connect', function (d) {
    console.log(d);
    currentTime = moment().format('YYYY-MM-DD hh:mm a')
    socket.emit('room', { message: `${myName} has joined the room`, userName: myName, currentTime: currentTime });
});

socket.on('i-room', function (data) {
    console.log(data);
    currentTime = moment(data.currentTime).format('hh:mm:ss a');
    
    msgP = document.createElement('p');
    msgP.innerText = `[${data.userName} ${currentTime}] : ${data.message}`;
    messagesDiv.insertBefore(msgP, messagesDiv.childNodes[0]);
    messagesDiv.scrollTop = 0;
});



pingButton.addEventListener("click", function () {
    currentTime = moment().format('YYYY-MM-DD hh:mm:ss a')
    socket.emit('room', { message: 'Pinging everyone', clientId: clientId, userName: myName, currentTime: currentTime });
    console.log('btn clicked');
})

// messageButton.addEventListener("click", function(){
//     currentTime = moment().format('YYYY-MM-DD hh:mm:ss a')
//     messageTextBox.innerText
//     socket.emit('room', { message: 'Pinging everyone', clientId: clientId, userName: myName, currentTime: currentTime });
    
// })