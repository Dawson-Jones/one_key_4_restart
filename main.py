import time
import os
import shutil
import yaml


def main():
    with open('config.yml') as f:
        config_dict = yaml.load(f)
    # print(config_dict)

    cache_path: dict = config_dict.get('clear_cache_path')
    deal_process = config_dict.get('app_path')
    # cache_pre_wd = cache_path.get('pre_wd')
    # cache_gui = cache_path.get('gui')

    if not all([deal_process, cache_path]):
        return

    for i in deal_process:
        try:
            os.popen('taskkill /im {} -f'.format(os.path.split(i)[-1]))
        except Exception as e:
            print(e)

    for i in cache_path.values():
        if os.path.exists(i):
            shutil.rmtree(i)
            os.makedirs(i)

    for i in deal_process:
        os.startfile(i)


if __name__ == '__main__':
    main()
