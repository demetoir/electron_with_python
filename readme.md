---2017.07.27---



# setting & start_app.js
https://github.com/electron/electron/blob/master/docs/tutorial/application-distribution.md


# electron with python
https://www.fyears.org/2017/02/electron-as-gui-of-python-apps-updated.html

issue : zmq(zeromq) or dll
https://stackoverflow.com/questions/44116726/electron-app-using-python-throws-zmq-node-error/44400443#44400443

node.js의 zeromq를 다시 빌드하면 됨.
electron prebuilt 를 사용했을경우 버전에 맞게 옵션 수정한다.
cmd : npm rebuild zeromq --runtime=electron --target=1.7.5

dll 문제 의 경우 캐시 지우고 다시 설치할고 했으나 이방법으로 zmq 버전 에러 생겨서 이것으로 해결됨
캐시지우는거는 node_modules폴더만 지우는걸로도 해결되었음

# version
electron prebuilt : electron-v1.7.5-win32-x64



