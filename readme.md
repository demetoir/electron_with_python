# electron with python
node.js 기반의 electron 을 프론트로 사용하면서 백엔드를 python 으로 사용하는 방식
electron, python 프로세스를 각각 실행하고 zerorpc 를 사용하여 통신하는
방식으로 구현되었다

참고 사이트
https://www.fyears.org/2017/02/electron-as-gui-of-python-apps-updated.html

zerorpc tcp://localhost:4242 calc "1 + 1"

***2017.07.27***
# setting & start_app.js
https://github.com/electron/electron/blob/master/docs/tutorial/application-distribution.md

issue : zmq(zeromq) or dll
https://stackoverflow.com/questions/44116726/electron-app-using-python-throws-zmq-node-error/44400443#44400443

node.js의 zeromq 를 다시 빌드하면 됨.
electron prebuilt 를 사용했을경우 버전에 맞게 옵션 수정한다.
cmd : npm rebuild zeromq --runtime=electron --target=1.7.5

dll 문제 의 경우 캐시 지우고 다시 설치할고 했으나 이방법으로 zmq 버전에러가
생겨서 이것으로 해결됨
캐시지우는거는 node_modules 폴더만 지우는걸로도 해결되었음

electron prebuilt : electron-v1.7.5-win32-x64


***2017-07-31***
electron prebuilt와 native electron의 버전이 맞지 않아 prebuilt를 제거하고
리포를 정리함.

zmq의 버전을 맞추기 위해 다음과 같은 cmd 사용
cmd : npm rebuild zeromq --runtime=electron --target=1.6.11

더 빠른 디버깅을 위해 start.js의 exit code 받는 속도를 개선함



*** packet-python error ***
reinstall module
pip install packet-python
pip install zeromq


