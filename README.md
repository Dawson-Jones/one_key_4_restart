# 配置
### 写在最前
所有的文件路径必须使用 “/” 而不是 “\” ！！！！  
all path must use “/” instead of “\”  !!!!

### config.yml  
- `app_path`  
    执行的app路径
    > 当一键启动的时候，会首先关闭，然后打开  
- `clear_cache_path`  
    清理的缓存路径  
    ***注意！！***
    > 1. 只会清理配置路径下的所有文件  
        ex:   
        `C:/Users/yc-pc/Desktop/dobby/gui_jkus-0.1.4/gui_jkus-0.1.4/resources/app/src/cache` 会保留cache文件夹, 删除cache下的所有文件  
    > 2. 使用缓存路径的时候，请确保路径配置正确。路径配置错误可能会出现不可挽回的后果

                             
