const zerorpc = require('zerorpc')
let client = new zerorpc.Client()
const electron = require('electron')
const ipcRenderer = electron.ipcRenderer
const remote = electron.remote

const main = remote.require('./main.js')

// connect pyServer
const port = '4242'
client.connect('tcp://127.0.0.1:' + port)
client.invoke('echo', 'pyServer ready', function (error, res) {
    if (error || res !== 'pyServer ready') {
        console.error(error)
    } else {
        console.log('pyServer is ready')
    }
})

client.invoke('help',function (error, res) {
    console.log(res)
})



let html_address = document.querySelector('#html_address')
let html_output = document.querySelector('#html_output')
let tag_list = document.querySelector('#tag_list')
let btn_go = document.querySelector('#go')
let btn_back = document.querySelector('#back')
let tag_number = document.querySelector('#tag_number')
let trace_stack = document.querySelector('#stack_trace')

btn_back.addEventListener('click', () => {
    client.invoke('back', 0)
    // ipcRenderer.send('back', 0)
})

btn_go.addEventListener('click', () => {
    // ipcRenderer.send('go', tag_number.value)
})

html_address.addEventListener('input', () => {
    ipcRenderer.send('update_html_address', html_address.value)
})
// what is purpose of below code?
// html_input.dispatchEvent(new Event('input'));

ipcRenderer.on('update_page', (event, args) => {
    console.log('update page')
    html_output.textContent = args[0]
    tag_list.textContent = args[1]
})

// ipc main and renderer
// http://electron.rocks/different-ways-to-communicate-between-main-and-renderer-process/
ipcRenderer.send('async', 'to main')
ipcRenderer.on('async', (event, arg) => {
    console.log('renderer recv :' + arg)
})



