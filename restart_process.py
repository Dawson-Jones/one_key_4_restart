import time
import re
import os
import shutil
import yaml
import psutil
import pyautogui

url_config = dict()


def one_key():
    with open('config.yml') as f:
        config_dict = yaml.load(f, Loader=yaml.Loader)
    global url_config
    url_config = config_dict.get('url_config')

    deal_process_path = config_dict.get('app_path')
    cache_path: list = config_dict.get('clear_cache_path')
    if not all([deal_process_path, cache_path]):
        return

    # kill process
    process_name = list()
    for i in deal_process_path:
        temp_name = os.path.split(i)[-1]
        ret = re.match(r'([^\.]+)\.', temp_name)
        process_name.append(ret.group(1) + '.exe')

    pids = psutil.pids()
    for pid in pids:
        try:
            p = psutil.Process(pid)
            processing_name = p.name()
            if processing_name in process_name:
                print(processing_name)
                os.popen('taskkill /im {} -f'.format(processing_name))
                process_name.remove(processing_name)
            if not process_name:
                break
        except Exception as e:
            print(e)

    # clear cache
    for i in cache_path:
        if os.path.exists(i):
            shutil.rmtree(i)
            os.makedirs(i)

    # copy file
    copy_file = config_dict.get("copy")
    if copy_file:
        for copy_path in copy_file:
            shutil.copy(copy_path[0], copy_path[1])

    # restart process
    # print(deal_process_path)
    for i in deal_process_path:
        os.startfile(i)

    # click
    coord_group = config_dict.get("mouse_click")
    if coord_group:
        time.sleep(3)
        for coord in coord_group:
            pyautogui.moveTo(int(coord[0]), int(coord[1]), duration=0.25)
            pyautogui.click(int(coord[0]), int(coord[1]))


if __name__ == '__main__':
    one_key()
