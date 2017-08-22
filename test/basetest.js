function BaseTest () {
    this.isEnd = false
    this.testFunction = null
    this.testList = []

}

BaseTest.prototype.setup = function () {
    console.log('setup')
}
BaseTest.prototype.teardown = function () {
    console.log('teardown')
}

BaseTest.prototype.testFunction = function (func) {
    console.log(func)
    func()
}
BaseTest.prototype.addTest = function (func) {
    this.testList.push(func)
}

BaseTest.prototype.begin = function () {

    for (const idx in this.testList) {
        const func = this.testList[idx]
        console.log(func)

        let isError = false
        try{
            func()
        }catch(e){
            console.error(e)
            isError = true
        }finally {
            if (!isError){
                console.log('test success')
            }else{
                console.log('test fail')
            }
        }
    }
}

const test_01 = function () {
    console.log('test 01')

}

const test_02 = function () {
    console.log('test 02')
    a = 1
    console.log(a())
}

const test_03 = function () {
    console.log('test 03')
}

let bt = new BaseTest()
bt.addTest(test_01)
bt.addTest(test_02)
bt.addTest(test_03)
bt.begin()