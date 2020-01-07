import sys
import requests
from concurrent import futures
from PyQt5.Qt import *
import restart_process
from gui import OneKey


def send_http(flag):
    params = {
        'op': 'write_int',
        'station': restart_process.url_config['plc_station'],
        'address': restart_process.url_config['panel_incoming_plc_address'],
    }
    if flag:
        params['value'] = 2
        requests.get(url='http://{}'.format(restart_process.url_config['plc_url']), params=params)
    params['value'] = 0
    requests.get(url='http://{}'.format(restart_process.url_config['plc_url']), params=params)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = OneKey()
    window.show()
    window.restart_signal.connect(restart_process.one_key)
    # window.restart_signal.connect(lambda: print("重启"))
    window.send_info_signal.connect(send_http)
    sys.exit(app.exec_())
