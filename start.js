const path = 'electron app'
const
  spawn = require('child_process').exec,
  child = spawn(path)

exitHandler = function (code) {
    console.log('child process exited with code ' + code.toString())
    process.exit()
}

child.addListener('exit', exitHandler)

child.stdout.on('data', function (data) {
    console.log('stdout: ' + data.toString())
})

child.stderr.on('data', function (data) {
    console.log('stderr: ' + data.toString())
})


