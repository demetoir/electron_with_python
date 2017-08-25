const path = require('path')
const zerorpc = require('zerorpc')

//pyServer process spawn and kill
let log = console.log
let pyServer = null
const createPyserver = function () {
    let port = '' + '4242'
    let script = path.join(__dirname, 'pyside', 'main', 'pyServer', 'PyServer.py')
    // script = 'C:\\Users\\demetoir_desktop\\WebstormProjects\\electron_with_python\\app\\pyside\\main\\pyServer\\PyServer.py'
    script = '/home/demetoir/WebstormProjects/electron_with_python/app/pyside/main/pyServer/PyServer.py'
    let cmd = 'python3'
    let args = [script, port]

    console.log(cmd + ' ' + script)
    pyServer = require('child_process').spawn(cmd, args)
    if (pyServer !== null) {
        console.log('pyServer spawn success')
    }
    pyServer.stderr.on('data', function (data) {
        console.log('stderr: ' + data.toString())
    })

}

function exitPyServer () {
    pyServer.kill()
    pyServer = null
    console.log('pyServer kill success')
}

const setup = function () {

}
const tearup = function () {

}

const test = function () {
    let client = new zerorpc.Client()
    // connect pyServer
    const port = '4242'
    client.connect('tcp://127.0.0.1:' + port)

    client.invoke('echo', 'pyServer ready', function (error, res) {
        log('echo')
        if (error || res !== 'pyServer ready') {
            console.error(error)
        } else {
            console.log('pyServer is ready')
        }
        log()
    })

    client.invoke('help', function (error, res) {
        log('help')
        console.log(res)
        log()
    })

    let strUrl = 'http://bbs.ruliweb.com/best/humor?&page=1'

    client.invoke('execute', 'current_html', function (error, res) {
        console.log('current html')
        console.log(res)
        log()
    })

    client.invoke('execute', 'set_root', strUrl, function (error, res) {
        log('set_root, current_html')
        console.log(strUrl)

        console.log('set root')
        console.log(res)
        log()

    })

    client.invoke('execute', 'current_html', function (error, res) {
        console.log('current html')
        console.log(res)
        log()

    })

    client.invoke('execute', 'move_down', 7, function (err, res) {
    })

    client.invoke('execute', 'move_down', 5, function (err, res) {
    })

    client.invoke('execute', 'add_filter', 'NavigableString', function (err, res) {
    })

    client.invoke('execute', 'children_tag', function (error, res) {
        for (let key in res) {
            let idx = res[key][0]
            let tag_name = res[key][1]
            let tag_attrs = res[key][2]

            let attrs = null
            if (tag_attrs) {
                attrs = ''
                for (let k in tag_attrs) {
                    console.log(k, ' : ', tag_attrs[k])
                    attrs += k + ' : ' + tag_attrs[k] + '\n'
                }
                console.log(tag_attrs)
            }

            let item = idx + ' , ' + tag_name + ' , ' + attrs
            console.log(item)
        }
    })

    client.invoke('echo_dict', function (error, res) {
        console.log(res)
        for (let key in res) {
            console.log(key, res[key])

        }
    })

}

createPyserver()
test()
// exitPyServer()






