//platform issue need hack
console.log('platform : '+ process.platform)
let child = null
if(process.platform === 'win32'){
    child = require('child_process').exec('electron app')
}else{
    child = require('child_process').spawn('electron',['app'])
}

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


