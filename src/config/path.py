# 获取当前脚本文件的绝对路径
import os,sys

# 获取项目根目录（如果执行的是打包的exe文件，sys会带有frozen属性
def app_path():
    # build环境 pyinstaller打包后的exe目录
    if hasattr(sys, 'frozen'):# Python解释器的完整路径
        path_base = os.path.dirname(sys.executable) #使用pyinstaller打包后的exe目录
    # dev环境
    else:
        current_script_path = os.path.abspath(__file__)
        # 获取当前脚本所在目录的父目录的父目录的路径
        path_base = os.path.dirname(os.path.dirname(os.path.dirname(current_script_path)))
    return path_base
  


# 目录根路径
path_base = app_path()
print('path_base',path_base)

# config 
path_config = os.path.join(path_base, 'source','config','logging.ini' )

# html
path_html = os.path.join(path_base, 'source','html')