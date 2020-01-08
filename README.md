# 配置
### 写在最前
所有的文件路径必须使用 “/” 而不是 “\” ！！！！  
all path must use “/” instead of “\”  !!!!

### config.yml  
- `app_path` **必选**  
    执行的app路径
    > 当一键启动的时候，会首先关闭，然后打开  
    > 推荐使用**软链接**(快捷方式), 使用exe 依赖文件需按照一键启动目录为根目录
- `clear_cache_path`  **必选**  
    清理的缓存路径  
    ***注意！！***
    > 1. 只会清理配置路径下的所有文件  
        eg:   
        `C:/Users/yc-pc/Desktop/dobby/gui_jkus-0.1.4/gui_jkus-0.1.4/resources/app/src/cache` 会保留cache文件夹, 删除cache下的所有文件  
    > 2. 使用缓存路径的时候，请确保路径配置正确。路径配置错误可能会出现不可挽回的后果
- `copy` **可选** 如果不填就什么都不做  
    eg:
    ```yaml
    copy:
      -
        - /home/ubuntu/Pictures/3.jpg  # 复制文件
        - /home/ubuntu/Pictures/C      # 目标路径
      - 
        - /home/ubuntu/Pictures/2.jpg  # 复制文件
        - /home/ubuntu/Pictures/C      # 目标路径
    ```
    复制文件与目标路径一一对应, 数量不限制
    
- `mouse_click` **可选**  
    eg:
    ```yaml
    mouse_click:
      -
        - 200  # x
        - 400  # y
        - 0    # 点击前的停顿时间
      - 
        - 300  # x
        - 600  # y
        - 0.3  # 点击前的停顿时间
    ```
    每个坐标会点击一次, 数量无限制
    
- `url_config`  **可选**  
    eg:
    ```yaml
    url_config:
      plc_url: localhost:9111/plc         # plc 地址
      plc_station: 2                      # 
      el_position: D399                   # el 位
      revolving_table_position: D399      # 旋转台位
    ```
    
