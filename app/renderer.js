const zerorpc = require('zerorpc')
let client = new zerorpc.Client()


const port = '4242'
client.connect('tcp://127.0.0.1:' + port)

client.invoke('echo', 'server ready', function (error, res) {
    if (error || res !== 'server ready') {
        console.error(error)
    } else {
        console.log('server is ready')
    }
})

let html_input = document.querySelector('#html_input')
let html_output = document.querySelector('#html_output')

html_input.addEventListener('input', () => {
    html_output.textContent  = html_input.value
})
// what is purpose of below code?
// html_input.dispatchEvent(new Event('input'));


