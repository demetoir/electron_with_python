// main.js

const electron = require('electron')
const electronLocalshortcut = require('electron-localshortcut')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const path = require('path')

let mainWindow = null
const createWindow = function () {
    mainWindow = new BrowserWindow({width: 1200, height: 600})
    mainWindow.loadURL(require('url').format({
        pathname: path.join(__dirname, 'index.html'),
        protocol: 'file:',
        slashes: true
    }))
    mainWindow.webContents.openDevTools()
    mainWindow.on('close', function () {
        mainWindow = null
    })
    console.log('electron createWindow')

    //local keyboard shortcut
    electronLocalshortcut.register(mainWindow, 'Up', () => {
        console.log('up pressed')
    })

    electronLocalshortcut.register(mainWindow, 'Down', () => {
        console.log('down pressed')
    })

    electronLocalshortcut.register(mainWindow, 'Left', () => {
        console.log('left pressed')
    })

    electronLocalshortcut.register(mainWindow, 'Right', () => {
        console.log('right pressed')
    })

}
app.on('ready', createWindow)
app.on('window-all-closed', function () {
    console.log('windows all closed')

    if (process.platform !== 'darwin') {
        app.quit()
    }
})
app.on('activate', function () {
    if (mainWindow === null) {
        createWindow()
    }
})

// add these to the end or middle of main.js

let pyProc = null
let pyPort = null

const selectPort = function () {
    pyPort = 4242
    return pyPort
}

const createPyProc = function () {
    let port = '' + selectPort()
    let script = path.join(__dirname, 'my_webcrawler', 'main', 'pyServer.py')
    console.log("python "+script)
    pyProc = require('child_process').spawn('python', [script, port])
    if (pyProc !== null) {
        console.log('child process spawn success')
    }
}

const exitPyProc = function () {
    pyProc.kill()
    pyProc = null
    pyPort = null
    console.log('py proc die')
}

app.on('ready', () => {
    createPyProc()

})

app.on('will-quit', () => {
    exitPyProc()
    electronLocalshortcut.unregisterAll()
})


