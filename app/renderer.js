const zerorpc = require('zerorpc')
let client = new zerorpc.Client()
const electron = require('electron')
const ipcRenderer = electron.ipcRenderer
const remote = electron.remote
const util = require('util')
const EventEmitter = require('events')
const main = remote.require('./main.js')

// connect pyServer
function connect_pyServer () {
    const port = '4242'
    client.connect('tcp://127.0.0.1:' + port)
    client.invoke('echo', 'pyServer ready', function (error, res) {
        if (error || res !== 'pyServer ready') {
            console.error(error)
        } else {
            console.log('pyServer is ready')
        }
    })

    client.invoke('help', function (error, res) {
        console.log(res)
    })
}

connect_pyServer()

function Renderer () {
    this.url = document.querySelector('#url')
    this.html_output = document.querySelector('#html_output')
    this.tag_list = document.querySelector('#tag_list')
    this.btn_go = document.querySelector('#go')
    this.btn_back = document.querySelector('#back')
    this.tag_number = document.querySelector('#tag_number')
    this.trace_stack = document.querySelector('#stack_trace')
    this.btn_set_url = document.querySelector('#btn_set_url')
    this.filter_list = document.querySelector('#filter_list')
    this.filter_input = document.querySelector('#filter_input')
    this.btn_filter_add = document.querySelector('#btn_filter_add')
    this.btn_filter_del = document.querySelector('#btn_filter_del')

    this.temp = null

    this.btn_set_url.addEventListener('click', function () {
        let strUrl = url.value
        console.log(strUrl)
        client.invoke('execute', 'set_root', strUrl, function (error, res) {
            renderer.emit('update_page')
        })
    })

    this.btn_back.addEventListener('click', function () {
        client.invoke('execute', 'move_up', function (err, res) {
            renderer.emit('update_page')
        })
        // ipcRenderer.send('back', 0)
    })

    this.btn_go.addEventListener('click', function () {
        let idx = Number(renderer.tag_number.value)
        client.invoke('execute', 'move_down', idx, function (err, res) {
            renderer.emit('update_page')
        })

        // ipcRenderer.send('go', tag_number.value)
    })

    this.btn_filter_add.addEventListener('click', function () {
        let tag_name = renderer.filter_input.value
        client.invoke('execute', 'add_filter', tag_name, function () {
            renderer.emit('update_page')
        })
    })

    this.btn_filter_del.addEventListener('click', function () {
        let tag_name = renderer.filter_input.value
        client.invoke('execute', 'del_filter', tag_name, function () {
            renderer.emit('update_page')
        })
    })

    this.updatePage = function () {
        //todo need hack

        client.invoke('execute', 'current_html', function (error, res) {
            renderer.html_output.innerHTML = res
        })

        client.invoke('execute', 'children_tag', function (error, res) {
            renderer.tag_list.innerHTML = ''
            for (let i = 0; i < res.length; i++) {
                let idx = res[i][0]
                let tag_name = res[i][1]
                let tag_attrs = res[i][2]

                let attrs = null
                if (tag_attrs) {
                    console.log(tag_attrs)
                    attrs = '{'
                    for (let key in tag_attrs) {
                        let attr = tag_attrs[idx]
                        console.log(attr)
                        attrs += key + ' : ' + tag_attrs[key] + ' , '
                    }
                    attrs += '}'
                }

                let item = idx + ' , ' + tag_name + ' , ' + attrs + '<br/>'
                renderer.tag_list.innerHTML += item
            }
        })

        client.invoke('execute', 'trace_stack', function (error, res) {
            // console.log(res)
            renderer.trace_stack.innerHTML = ''
            for (let key in res) {
                renderer.trace_stack.innerHTML += res[key] + '<br/>'
            }
        })

        client.invoke('execute', 'get_filter', function (error, res) {
            console.log(res)
            renderer.filter_list.innerHTML = ''
            for (let key in res) {
                renderer.filter_list.innerHTML += res[key] + '<br/>'
            }
        })

    }

    this.on('update_page', function () {
        this.updatePage()
    })
}

util.inherits(Renderer, EventEmitter)

let renderer = new Renderer()

// url.addEventListener('input', () => {
//     ipcRenderer.send('update_html_address', url.value)
// })
// // what is purpose of below code?
// // html_input.dispatchEvent(new Event('input'));
//
// ipcRenderer.on('update_page', (event, args) => {
//     console.log('update page')
//     html_output.textContent = args[0]
//     tag_list.textContent = args[1]
// })
//
// // ipc main and renderer
// // http://electron.rocks/different-ways-to-communicate-between-main-and-renderer-process/
// ipcRenderer.send('async', 'to main')
// ipcRenderer.on('async', (event, arg) => {
//     console.log('renderer recv :' + arg)
// })