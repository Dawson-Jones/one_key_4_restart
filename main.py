import sys
import requests
from PyQt5.Qt import *
from restart_process import one_key
from gui import OneKey


def send_http(flag):
    if flag:
        # requests.post()
        print(flag, type(flag))
    else:
        # requests.post()
        print(flag, type(flag))


if __name__ == '__main__':
    # one_key()
    app = QApplication(sys.argv)
    window = OneKey()
    window.show()
    window.send_info_signal.connect(send_http)
    sys.exit(app.exec_())
