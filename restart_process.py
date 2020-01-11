import time
import os
import shutil
import yaml
import psutil
import pyautogui
from get_window_and_maximize import cWindow

url_config = dict()


def one_key():
    with open('config.yml') as f:
        config_dict = yaml.load(f, Loader=yaml.Loader)
    global url_config
    url_config = config_dict.get('url_config')
    '''
    {
        'app_path': [
            'C:/Users/yc-pc/Desktop/PLCTest.exe.lnk',
            'C:/Users/yc-pc/Desktop/main.exe.lnk',
            'C:/Users/yc-pc/Desktop/el-jk-us.exe.lnk'],
        'kill_app': ['PLCTest.exe', 'main.exe', 'el-jk-us.exe'],
        'clear_cache_path': [
            'C:/Users/yc-pc/Desktop/dobby/yc_pc/gui_jkus-0.1.4/gui_jkus-0.1.4/resources/app/src/cache',
            'C:/Users/yc-pc/Desktop/dobby/yc_pc/el_panel-jkf5-0.4.0/temp_pic'
        ],
        'url_config': {
            'plc_url': '192.168.1.4:9111/plc',
            'plc_station': 2,
            'el_position': 'D399',
            'revolving_table_position': 'D399'
        }
    }
    '''

    deal_process_path = config_dict.get('app_path')
    kill_app = config_dict.get('kill_app')
    cache_path: list = config_dict.get('clear_cache_path')
    if not all([deal_process_path, cache_path, kill_app]):
        return

    # kill process
    pids = psutil.pids()
    for pid in pids:
        try:
            p = psutil.Process(pid)
            processing_name = p.name()
            if processing_name in kill_app:
                os.system('taskkill /im {} -f'.format(processing_name))
                kill_app.remove(processing_name)
            if not kill_app:
                break
        except Exception as e:
            print(e)

    # clear cache
    try:
        for i in cache_path:
            print(i)
            if os.path.exists(i):
                shutil.rmtree(i)
                os.makedirs(i)
            else:
                print('path not exists')
    except Exception as e:
        print(e)

    # copy file
    copy_file = config_dict.get("copy")
    if copy_file:
        for copy_path in copy_file:
            shutil.copy(copy_path[0], copy_path[1])

    # restart process
    for i in deal_process_path:
        os.system(i)

    # maximize
    app_name = config_dict.get('maximize_app')
    regex = '.*{}.*'.format(app_name)
    cw = cWindow()
    cw.find_window_regex(regex)
    cw.Maximize()
    cw.SetAsForegroundWindow()

    # click
    coord_group = config_dict.get("mouse_click")
    if coord_group:
        for coord in coord_group:
            time.sleep(coord_group[2])
            pyautogui.moveTo(int(coord[0]), int(coord[1]), duration=0.25)
            pyautogui.click(int(coord[0]), int(coord[1]))


if __name__ == '__main__':
    one_key()
