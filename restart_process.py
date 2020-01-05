import time
import os
import shutil
import yaml
import psutil


def one_key():
    with open('config.yml') as f:
        config_dict = yaml.load(f, Loader=yaml.Loader)
    print(config_dict)
    """
    {
        'app_path': ['C:/Users/yc-pc/Desktop/dobby/yc_pc/PLCTest_Kevin/PLCTest_Kevin/PLCTest/bin/Debug/PLCTest.exe',
                     'C:/Users/yc-pc/Desktop/dobby/yc_pc/el_panel-jkf5-0.4.0/main.exe',
                     'C:/Users/yc-pc/Desktop/dobby/yc_pc/gui_jkus-0.1.4/gui_jkus-0.1.4/el-jk-us.exe'],
        'clear_cache_path': ['C:/Users/yc-pc/Desktop/dobby/gui_jkus-0.1.4/gui_jkus-0.1.4/resources/app/src/cache',
                             'C:/Users/yc-pc/Desktop/dobby/el_panel-jkf5-0.4.0/temp_pic']
    }
    """

    # 参数完整性
    deal_process_path = config_dict.get('app_path')
    cache_path: list = config_dict.get('clear_cache_path')
    if not all([deal_process_path, cache_path]):
        return

    # kill process
    deal_process_name = [os.path.split(i)[-1] for i in deal_process_path]
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

    # restart process
    for i in deal_process_path:
        os.startfile(i)


if __name__ == '__main__':
    one_key()
