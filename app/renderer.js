const zerorpc = require('zerorpc')
let client = new zerorpc.Client()
// const electron = require('electron')
// const ipcRenderer = electron.ipcRenderer
// const remote = electron.remote
const util = require('util')
const EventEmitter = require('events')
// const main = remote.require('./main.js')

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

function deco (str, tag) {
    return '<' + tag + '>' + str + '</' + tag + '>'
}

function decoList (list, tag) {
    let ret = ''
    for (let i in list) {
        ret += deco(list[i], tag)
    }
    return ret
}

//fixme refactoring
const strFilterCard = '<div class="card text-white bg-primary o-hidden h-10 text-center filter-tags_form">' +
  '<span id="deleteFilterTag_%s"> %s <i class="fa fa-window-close"></i></span></div>'

const strBtnAddFilter = '<button class="btn btn-primary" type="button" id="btnAddFilter_%d"><i class="fa fa-plus" ></i></button>'

const strBtnMoveDown = '<button class="btn btn-primary" type="button" id="btnMoveDown_%d"><i class="fa fa-arrow-right" ></i></button>'

function Renderer () {
    this.on('update_page', function () {
        this.updatePage()
    })

    $('#bntTargetURL').click(function () {
        let strUrl = $('#targetURL').val()
        client.invoke('execute', 'set_root', strUrl, function (error, res) {
            console.log('set target url ', strUrl)
            renderer.updatePage()
        })
    })

    this.addBtnAddFilter = function (item) {
        $('#btnAddFilter_' + item).click(function () {
            let strId = $(this).attr('id')
            let idx = Number(strId.slice('#btnAddFilter_'.length - 1, strId.length))
            // console.log(idx, typeof (idx), idx.toString())

            client.invoke('execute', 'children_tag', function (error, res) {
                let tag_name = res.filter(function (value) {
                      return value[0] === idx
                  }
                )[0][1]

                client.invoke('execute', 'add_filter', tag_name, function () {
                    console.log('add filter ' + tag_name)
                    renderer.updatePage()
                })
            })
        })
    }

    this.addBtnMoveDown = function (item) {
        $('#btnMoveDown_' + item).click(function () {
            let strId = $(this).attr('id')
            let idx = strId.slice('#btnMoveDown_'.length - 1, strId.length)
            client.invoke('execute', 'move_down', idx, function () {
                renderer.updatePage()
                console.log('btn move down' + idx)
            })
        })
    }

    this.updatePage = function () {
        //update child tag table
        client.invoke('execute', 'children_tag', function (error, res) {
            let childTagTableBody = $('#childTagTableBody')
            let html = ''
            if (typeof (res) === 'string') {
                childTagTableBody.html(res)
                return
            }

            let list = []
            for (let i = 0; i < res.length; i++) {
                let childTagIdx = res[i][0]
                let tag_name = res[i][1]
                let btnAddFilter = util.format(strBtnAddFilter, childTagIdx)
                let btnMoveDown = util.format(strBtnMoveDown, childTagIdx)
                let tag_attrs = res[i][2]
                let strAttrs = ''
                if (tag_attrs) {
                    for (let key in tag_attrs) {
                        strAttrs += key + ' : ' + tag_attrs[key] + ' | '
                    }
                }

                list.push(decoList([btnAddFilter, btnMoveDown, childTagIdx, tag_name, strAttrs], 'td'))
            }
            html += decoList(list, 'tr')
            childTagTableBody.html(html)

            //add button event
            for (let i in res) {
                let item = res[i][0]
                // btn add filter click event
                renderer.addBtnAddFilter(item)
                renderer.addBtnMoveDown(item)
            }
        })

        //update filter_list
        client.invoke('execute', 'get_filter', function (error, res) {
            let html = ''
            for (let i in res) {
                html += util.format(strFilterCard, res[i], res[i])
            }
            $('#filterTagList').html(html)

            //add delete filter btn
            for (let i in res) {
                let item = res[i]
                $('#deleteFilterTag_' + item).click(function () {
                    let strId = $(this).attr('id')
                    let tag_name = strId.slice('#deleteFilterTag_'.length - 1, strId.length)
                    client.invoke('execute', 'del_filter', tag_name, function () {
                        console.log('del filter' + tag_name)
                        renderer.emit('update_page')
                    })
                })
            }

        })

        //update output html
        client.invoke('execute', 'current_html', function (error, res) {
            // WTF? this make faster and solve zerorpc msg multiplexing error but why ?
            $('#outputHTML')[0].innerHTML = res
            // $('#outputHTML').html(res)
        })

        //TODO  implement this
        // client.invoke('execute', 'trace_stack', function (error, res) {
        //     // console.log(res)
        //     renderer.trace_stack.innerHTML = ''
        //     for (let key in res) {
        //         renderer.trace_stack.innerHTML += res[key] + '<br/>'
        //     }
        // })

    }

    //TODO  implement this
    // this.btn_back.addEventListener('click', function () {
    //     client.invoke('execute', 'move_up', function (err, res) {
    //         renderer.emit('update_page')
    //     })
    //     // ipcRenderer.send('back', 0)
    // })
    //

}

util.inherits(Renderer, EventEmitter)

let renderer = new Renderer()


// TODO ipc to main and renderer
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