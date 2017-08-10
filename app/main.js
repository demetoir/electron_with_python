// main.js
const electron = require('electron')
const electronLocalshortcut = require('electron-localshortcut')
const app = electron.app
const BrowserWindow = electron.BrowserWindow
const ipcMain = electron.ipcMain
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

//pyServer process spawn and kill
let pyServer = null
const createPyServer = function () {
    let port = '' + '4242'
    let script = path.join(__dirname, 'pyside', 'main', 'server', 'PyServer.py')
    console.log('python ' + script)
    pyServer = require('child_process').spawn('python', [script, port])
    if (pyServer !== null) {
        console.log('pyServer spawn success')
    }
}
const exitPyServer = function () {
    pyServer.kill()
    pyServer = null
    console.log('pyServer kill success')
}

app.on('ready', () => {
    createPyServer()
})

app.on('will-quit', () => {
    exitPyServer()
    electronLocalshortcut.unregisterAll()
})

// ipc main and renderer
// http://electron.rocks/different-ways-to-communicate-between-main-and-renderer-process/
ipcMain.on('async', (event, arg) => {
    console.log('main rec :' + arg)
    event.sender.send('async', 'to renderer')
})