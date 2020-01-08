import time
import os
import shutil
import yaml
import psutil
import pyautogui

url_config = dict()


def one_key():
    with open('config.yml') as f:
        config_dict = yaml.load(f, Loader=yaml.Loader)
    print(config_dict)
    global url_config
    url_config = config_dict.get('url_config')

    # 参数完整性
    deal_process_path = config_dict.get('app_path')
    cache_path: list = config_dict.get('clear_cache_path')
    if not all([deal_process_path, cache_path]):
        return

    # kill process
    deal_process_name = [os.path.splitext(os.path.split(i)[-1])[0] + '.exe' for i in deal_process_path]
    print(deal_process_name)

    deal_process_num = len(deal_process_name)
    pids = psutil.pids()
    for pid in pids:
        p = psutil.Process(pid)
        if p.name() in deal_process_name:
            os.popen('taskkill /im {} -f'.format(p.name()))
            deal_process_num -= 1
        if not deal_process_num:
            break

    # clear cache
    for i in cache_path:
        if os.path.exists(i):
            shutil.rmtree(i)
            os.makedirs(i)

    # copy file
    if copy_file := config_dict.get("copy"):
        for copy_path in copy_file:
            shutil.copy(copy_path[0], copy_path[1])

    # restart process
    for i in deal_process_path:
        os.startfile(i)

    # click
    if coord_group := config_dict.get("mouse_click"):
        time.sleep(3)
        for coord in coord_group:
            pyautogui.moveTo(int(coord[0]), int(coord[1]), duration=0.25)
            pyautogui.click(int(coord[0]), int(coord[1]))


if __name__ == '__main__':
    one_key()
