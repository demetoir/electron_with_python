const zerorpc = require('zerorpc')
let client = new zerorpc.Client()
const electron = require('electron')
const ipcRenderer = electron.ipcRenderer
const remote = electron.remote

const main = remote.require('./main.js')

const port = '4242'
client.connect('tcp://127.0.0.1:' + port)

client.invoke('echo', 'server ready', function (error, res) {
    if (error || res !== 'server ready') {
        console.error(error)
    } else {
        console.log('server is ready')
    }
})

let html_address = document.querySelector('#html_address')
let html_output = document.querySelector('#html_output')

html_address.addEventListener('input', () => {
    html_output.textContent  = html_input.value
})
// what is purpose of below code?
// html_input.dispatchEvent(new Event('input'));



// ipc main and renderer
// http://electron.rocks/different-ways-to-communicate-between-main-and-renderer-process/
ipcRenderer.send('async', 'to main')
ipcRenderer.on('async', (event, arg)=>{
    console.log('renderer recv :'+arg)
})



