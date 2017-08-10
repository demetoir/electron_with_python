import subprocess
import time

isKillSignal = False


def spawn_process(query_cmd=None):
    pyServer_cmd = ["python", "PyServer.py"]
    p1 = subprocess.Popen(
        pyServer_cmd,
        stdout=subprocess.PIPE)

    p2 = subprocess.Popen(
        query_cmd,
        stdout=subprocess.PIPE)

    ret = ""
    while True:
        line = str(p2.stdout.readline(), 'utf-8')
        if line == "":
            break
        ret += line
        p2.wait(timeout=3.)

    p1.terminate()
    p2.terminate()

    return ret


def spawn_server_query(cmd, *args):
    # proc.sub
    pass


if __name__ == '__main__':
    cmd = ['zerorpc', 'tcp://127.0.0.1:4242', 'txp_help']
    ret = spawn_process(cmd)
    print(ret)

    cmd = ['zerorpc', 'tcp://127.0.0.1:4242']
    ret = spawn_process(cmd)
    print(ret)
