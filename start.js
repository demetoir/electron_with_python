const spawn = require('child_process').spawn
const child = spawn('electron', ['app'])

child.addListener('exit', function (code) {
    console.log('child process exited with code ' + code.toString())
    process.exit()
})

child.stdout.on('data', function (data) {
    console.log(data.toString())
})

child.stderr.on('data', function (data) {
    console.log('stderr: ' + data.toString())
})


