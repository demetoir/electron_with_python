//platform issue need hack
start_project = function(){
    let ps = null
    if(process.platform === 'win32'){
        ps = require('child_process').exec('electron app')
    }else{
        ps = require('child_process').spawn('electron',['app'])
    }
    return ps
}

console.log('platform : '+ process.platform)
let project = start_project()

project.addListener('exit', function (code) {
    console.log('child process exited with code ' + code.toString())
    process.exit()
})

project.stdout.on('data', function (data) {
    console.log(data.toString())
})

project.stderr.on('data', function (data) {
    console.log('stderr: ' + data.toString())
})


