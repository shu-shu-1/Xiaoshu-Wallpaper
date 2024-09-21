### ✨ 导入模块
import ctypes
import mimetypes
import subprocess
import threading
import win32api
import win32con
import win32clipboard
import io
import logging
import time
import requests
import os
import json
import winreg
import math
import re
import webbrowser
import sys
import shutil
import tkinter.filedialog as filedialog
import tkintertools as tkt
import 国行公祭,欢庆春节,清明祭扫,中秋月下,粉花春色,原木秋色,粉雕玉琢,黄昏蓝调
from plyer import notification
from PIL import Image,ImageFile
from colorama import Fore, Style
from itertools import zip_longest
from functools import lru_cache
### ✨ 初始化

have_update=False
print(f"{Fore.BLUE}-----------------------------------------------")
print(f"{Fore.BLUE}欢迎使用小树壁纸开发版本！")
print(f"{Fore.BLUE}这里是开发版本专用命令行\n")
print(f"{Fore.BLUE}剩余信息请查看日志文件（logs文件夹）")
print(f"{Fore.BLUE}-----------------------------------------------")
print(f"{Style.RESET_ALL}\n\n")
print(f"{Fore.YELLOW}⚠️⚠️⚠️")
print(f"{Fore.YELLOW}-----------------------------------------------")
print(f"{Fore.YELLOW}你正在使用未经测试的开发版本，请谨慎使用！")
print(f"{Fore.YELLOW}开发版本禁止外泄！")
print(f"{Fore.YELLOW}测试版本不能代表最终品质，请不要将其分享给他人！")
print(f"{Fore.YELLOW}-----------------------------------------------")
print(f"{Style.RESET_ALL}")


# tkt.core.constants.SYSTEM = "Windows10"
# tkt.dialogs.TkMessage(icon="warning", title="警告", message="你正在使用未经测试的开发版本，请谨慎使用！", detail="请不要作为日常使用！")
# tkt.dialogs.TkMessage(icon="warning", title="警告", message="开发版本禁止外泄！", detail="测试版本不能代表最终品质，请不要将其分享给他人！")
def new_folder(ffffffff):
    folder_name = ffffffff
    if os.path.exists(folder_name):
        pass
    else: 
        os.makedirs(folder_name)

        # print(f"创建文件夹“{folder_name}”成功")
def get_executable_directory():
    if getattr(sys, 'frozen', False):
        # 如果脚本是冻结的（即打包后的可执行文件）
        return os.path.dirname(sys.executable)
    else:
        # 如果脚本是普通的Python脚本
        return os.path.dirname(os.path.abspath(__file__))
new_folder("logs")
new_folder("C:/xiaoshu_wallpaper")
new_folder("temp")
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
LOG_FILE = f'./logs/logs_{time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())}.log'
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format=LOG_FORMAT,encoding='utf-8')
logging.info("------程序启动------")
logging.info("日志加载成功")
# logging.error("hello")
VER = "v6.0.0-beta.3"
software_VER="6.0.0.b.3"
root=tkt.Tk(title=f"小树壁纸{VER}")

logging.info("初始化窗口成功")
root.center()
# root.attributes("-alpha", 0.9)
root.iconbitmap(default="./assets/icon/icon.ico")
# root.attributes("-topmost", True)
# root.attributes("-toolwindow", True)
root.resizable(width=False, height=False)


# https://www.bing.com/hp/api/v1/trivia

canvas = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
back_canvas=tkt.Canvas(canvas)
canvas.place(width=1280, height=720, x=640, y=360, anchor="center")
back_canvas.place(x=50, y=670,width=40,height=40,anchor="center")
logging.info("初始化画布成功")
# 加载字体
if tkt.toolbox.load_font("./assets/fonts/LXGWWenKai-Regular.ttf"):
    tkt.constants.FONT = "霞鹜文楷"
    logging.info("文本加载字体成功")
if tkt.toolbox.load_font("./assets/fonts/SegoeIcons.ttf"):
    # tkt.constants.FONT = "霞鹜文楷"
    logging.info("图标加载字体成功")
tkt.constants.SIZE = -24

# LANG={"中文简体":"zh-CN",
#     "中文繁體": "zh-TW",
#     "English(US)": "en-US",
#     "日本語": "ja-JP",}
ORIGIN_SYSTEM = tkt.constants.SYSTEM
APPDATA = os.path.expandvars("%APPDATA%")
TEMP = os.path.expandvars("%TEMP%")
tkt.style.set_color_mode("light")
tkt.style.customize_window(
    root,
    # style="acrylic",
    # hide_title_bar=True,
    hide_button="maxmin",
    # boarder_type="smallround",
)
tkt.style.set_theme_map(light=粉雕玉琢)

# tkt.style.set_color_mode("dark")

### ✨ 命令行
def get_input():
    while True:
        user_input = input("调试命令行（输入 'exit' 强制退出主程序）：")
        if user_input.lower() == 'exit':
            os._exit(0)
        elif user_input.lower() == 'clear':
            os.system('cls')
        elif user_input.lower() == 'test':
            print("测试消息！")
        elif user_input.startswith("theme "):
            theme_name = user_input.split(" ")[1]
            match theme_name:
                case "light":
                    tkt.style.set_color_mode("light")
                case "dark":
                    tkt.style.set_color_mode("dark")
                case "acrylic":
                    tkt.style.customize_window(
                        root,
                        style="acrylic",
                        # hide_title_bar=True,
                        hide_button="maxmin",
                        # boarder_type="smallround",
                    )
                    tkt.style.set_color_mode("dark")
                case "粉雕玉琢":
                    tkt.style.set_theme_map(light=粉雕玉琢)
                    tkt.style.set_color_mode("light")
                case "原木秋色":
                    tkt.style.set_theme_map(light=原木秋色)
                    tkt.style.set_color_mode("light")
                case "国行公祭":
                    tkt.style.set_theme_map(light=国行公祭)
                    tkt.style.set_color_mode("light")
                case "粉花春色":
                    tkt.style.set_theme_map(light=粉花春色)
                    tkt.style.set_color_mode("light")
                case "中秋月下":
                    tkt.style.set_theme_map(light=中秋月下)
                    tkt.style.set_color_mode("light")
                case "欢庆春节":
                    tkt.style.set_theme_map(light=欢庆春节)
                    tkt.style.set_color_mode("light")
                case "清明祭扫":
                    tkt.style.set_theme_map(light=清明祭扫)
                    tkt.style.set_color_mode("light")
                case "list":
                    print("可选主题：")
                    print("light dark acrylic 原木秋色 粉雕玉琢 粉花春色 中秋月下 欢庆春节 清明祭扫")
                case _:
                    print(f"不存在的主题：{theme_name}")
        else:
            print(f"不存在的命令：{user_input}")
# 启动一个线程来接受用户输入
input_thread = threading.Thread(target=get_input)
input_thread.daemon = True  # 设置为守护线程，这样主程序结束时线程也会结束
input_thread.start()


### ✨ 功能性函数

def run_installer(installer_path):
    if sys.platform == 'win32':
        installer_path = installer_path
        arguments = [
            "/FORCECLOSEAPPLICATIONS",
            "/RESTARTAPPLICATIONS",
            "/SILENT"
        ]

        # 合并路径和参数为一个列表
        command = [installer_path] + arguments

        # 使用 subprocess.Popen() 启动安装程序
        subprocess.Popen(command)
    else:
        subprocess.call(['chmod', '+x', installer_path])
        subprocess.call(['open', installer_path])
def resize_image(image_path, new_height):
    # 打开图片
    original_image = Image.open(image_path)
    # 获取图片的原始宽度和高度
    width, height = original_image.size
    # 计算新的宽度以保持图片比例
    new_width = int(width * new_height / height)
    # 调整图片大小
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
    return tkt.PhotoImage(resized_image)
def copy_and_set_wallpaper(image_path,*args):
    shutil.copyfile(image_path, f"C:\\xiaoshu_wallpaper\\{os.path.basename(image_path)}")
    set_wallpaper(f"C:\\xiaoshu_wallpaper\\{os.path.basename(image_path)}")
def set_wallpaper(filelink):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filelink, 0)
    time.sleep(1)
    Hkey = win32api.RegCreateKey(win32con.HKEY_CURRENT_USER, r'Control Panel\Desktop')
    win32api.RegSetValueEx(Hkey, 'WallPaper', 0, win32con.REG_SZ, filelink)
    win32api.RegCloseKey(Hkey)

def compare_versions(version1, version2):
    # 正则表达式匹配以v开头的版本号，后面跟随主版本号、次版本号、修订号、可选的先行版本号和版本编译信息
    semver_regex = r'^v(\d+)\.(\d+)\.(\d+)(?:-([\dA-Za-z-]+(?:\.[\dA-Za-z-]+)*)(?:\.(\d+))?)?(?:\+([\dA-Za-z-]+(?:\.[\dA-Za-z-]+)*))?$'
    
    # 将版本号转换为整数元组和先行版本号字符串
    def parse_version(version):
        match = re.match(semver_regex, version)
        if not match:
            raise ValueError(f"版本号 '{version}' 格式不正确。")
        major, minor, patch = map(int, match.groups()[:3])
        prerelease = match.group(4) if match.group(4) else None
        prerelease_number = int(match.group(5)) if match.group(5) else None
        return (major, minor, patch, prerelease, prerelease_number)
    
    # 解析两个版本号
    v1 = parse_version(version1)
    v2 = parse_version(version2)
    
    # 比较主版本号、次版本号和修订号
    for i in range(3):
        if v1[i] > v2[i]:
            return 1
        elif v1[i] < v2[i]:
            return -1
    
    # 比较先行版本号
    if v1[3] and v2[3]:
        # 比较先行版本号的每个部分
        for pre1, pre2 in zip_longest(v1[3].split('.'), v2[3].split('.'), fillvalue=''):
            if pre1.isdigit() and pre2.isdigit():
                # 比较数字部分
                if int(pre1) > int(pre2):
                    return 1
                if int(pre1) < int(pre2):
                    return -1
            else:
                # 比较非数字部分（字母或连字符）
                if pre1 > pre2:
                    return 1
                if pre1 < pre2:
                    return -1
    elif v1[3]:
        return -1  # v1有先行版本号，v2没有
    elif v2[3]:
        return 1  # v1没有先行版本号，v2有
    
    # 比较先行版本号后面的数字
    if v1[4] is not None and v2[4] is not None:
        if v1[4] > v2[4]:
            return 1
        if v1[4] < v2[4]:
            return -1
    elif v1[4] is not None:
        return -1  # v1有数字，v2没有
    elif v2[4] is not None:
        return 1  # v1没有数字，v2有
    
    # 版本号完全相等
    return 0
# print(compare_versions("v6.0.0-beta.2", "v6.0.0-beta.1"))
def copy_image_to_clipboard(image_path):
    img = Image.open(image_path)
    
    output = io.BytesIO()
    img.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()
    
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def get_my_pictures_path():
    logging.info("调用读取注册表图片文件夹路径函数")
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                            r"Software\Microsoft\Windows\CurrentVersion\Explorer\User Shell Folders")
        my_pictures_path, _ = winreg.QueryValueEx(key, "My Pictures")
        winreg.CloseKey(key)
        return my_pictures_path
    except OSError as error:
        logging.error(f"读取注册表图片文件夹路径错误 :{error}")
        tkt.dialogs.TkMessage(icon="error", title="读取错误", message="读取注册表图片文件夹路径错误", detail="请尝试以管理员模式重新运行本程序")
        # 优雅地处理退出，可以根据实际情况调整
        raise RuntimeError("无法读取注册表中的图片文件夹路径，详细错误请查看日志")
    
    except Exception as e:
        # 捕获其他未预期的异常
        logging.error(f"发生未知错误: {e}")
        tkt.dialogs.TkMessage(icon="error", title="读取错误", message="发生未知错误", detail="请尝试以管理员模式重新运行本程序")
        raise RuntimeError("发生未知错误，详细错误请查看日志")

### ✨ 设置获取和处理

df_settings = {
        # "lang": "zh-CN",
        # "definition": "HUD",   
        "theme": "auto",
        "window_wallpaper_path": "",
        "temp_path": "",
        "theme_mode": "auto",
        "check_update": 1,
        "bing_auto_start": 0,
        "pic_time": 60,
        "update_channel": "test_update",
        "download_path": "",
        "segmented_download_size": 200,
        "icon" : "./assets/icon/icon1.ico",
        "use_proxy" : 1,
        "proxy_url": "ghproxy.cn",
        "clear_cache_when_360_back": 1,
        "use_proxy_for_wallpaper": 0,
        "proxy_for_wallpaper": {},
}
proxy_list = {
    "ghproxy.cn":"https://www.ghproxy.cn/",
    "ghproxy.cc":"https://cf.ghproxy.cc/",
    "gh-proxy.com":"https://gh-proxy.com/",
    "jiasu.in":"https://gh.jiasu.in/"
}
one=0
# print(f"APPDATA value: {os.path.expandvars('%APPDATA%')}")
event_get=None
cog=None
def callbacks(event):
    global event_get
    event_get=event
def reset():
    logging.info("重置设置")
    global cog
    # print("reset")
    with open(f"{APPDATA}\\xiaoshu_wallpaper\\config\\config.json","w+") as f:     # 创建一个名为"config.json"的文件    
        json.dump(df_settings,f)
        cog = df_settings
def save_cog():
    logging.info("保存设置")
    global cog
    with open(f"{APPDATA}\\xiaoshu_wallpaper\\config\\config.json","w+") as f:     # 创建一个名为"config.json"的文件
        json.dump(cog,f)
if os.path.exists(f"{APPDATA}\\xiaoshu_wallpaper\\config\\config.json") is not True:
    one=1
    if os.path.exists(f"{APPDATA}\\xiaoshu_wallpaper\\config") is not True:
        os.makedirs(f"{APPDATA}\\xiaoshu_wallpaper\\config\\")
    reset()

else:
    with open(f"{APPDATA}\\xiaoshu_wallpaper\\config\\config.json","r") as f:
        try:
            cog = json.load(f)
        except json.decoder.JSONDecodeError:
            # print("JSON格式错误")
            tkt.dialogs.TkMessage(icon="error",title="读取设置错误",message="JSON格式错误")
            tkt.dialogs.TkMessage(icon="question",title="重置设置",message="你确定要重置设置吗？" ,command=callbacks,default="yes",detail="重置后，你的设置将会被重置，是否继续？",type="yesno")
            # print(event_get)
            if event_get == "yes":
                reset()
                one=1
                # print("reset")
            else:
                os._exit(0)
if (list(df_settings.keys()) != list(cog.keys()) and len(df_settings) > len(cog)):
    tkt.dialogs.TkMessage(icon="error",title="读取设置错误",message="设置项缺失")
    tkt.dialogs.TkMessage(icon="question",title="重置设置",message="你确定要重置设置吗？" ,command=callbacks,default="yes",detail="重置后，你的设置将会被清除，是否继续？",type="yesno")
    # print(event_get)
    if event_get == "yes":
        reset()
        # print("reset")
        one=1
    else:
        os._exit(0)
elif (list(df_settings.keys()) != list(cog.keys()) and len(df_settings) < len(cog) and all(x in cog.keys() for x in df_settings.keys())):
    tkt.dialogs.TkMessage(icon="info",title="读取设置异常",message="设置项过多",detail="多余的设置项将会被忽略。您可能使用了旧版本的程序，建议您更新程序。")
    # print("reset")
    # print("reset")
    tkt.dialogs.TkMessage(icon="question",title="重置设置",message="你确定要重置设置吗？" ,command=callbacks,default="yes",detail="重置后，你的设置将会被清除，是否继续？",type="yesno")
    # print(event_get)
    if event_get == "yes":
        reset()
        # print("reset")
        one=1
    else:
        os._exit(0)
elif list(df_settings.keys()) != list(cog.keys()) and len(df_settings) == len(cog):
    tkt.dialogs.TkMessage(icon="info",title="读取设置异常",message="设置文件键不一致",detail="您可能使用了不兼容更新版本的配置文件，设置必须重置。")
    tkt.dialogs.TkMessage(icon="question",title="重置设置",message="你确定要重置设置吗？" ,command=callbacks,default="yes",detail="重置后，你的设置将会被清除，是否继续？",type="yesno")
    if event_get == "yes":
        reset()
        # print("reset")
        one=1
    else:
        os._exit(0)    
if cog["download_path"] == "":
    # 获取图片文件夹路径

    Download_Path = get_my_pictures_path()
    cog["download_path"] = Download_Path
    save_cog()
else:
    Download_Path = cog["download_path"]
cog["proxy_url"] = proxy_list[cog["proxy_url"]]

### ✨ 应用个性化

if cog["window_wallpaper_path"]:
    ...
root.iconbitmap(default=cog["icon"])



### ✨ 启动加载
def bing_index_loading():
    global pb1
    canvas_update.place_forget()
    canvas_loading.place(width=1280, height=720, x=640, y=360, anchor="center")
    pb1 = tkt.ProgressBar(canvas_loading, (420, 260), (380, 8))
    tkt.Text(canvas_loading,(120,50),text="正在加载数据...",fontsize=40,anchor="nw")
    start_task()
def task():
    global fn,b_title,b_copyright,bing_data,pb1
    try:
        # global bing_data_name
        bing_data=getBingImg()
        url=bing_data[0]['url']
        # print(getBingImg())
        root.update() 
        # 自定义用户代理
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
        }

        # 发送HEAD请求以获取文件大小
        response = requests.head(url, headers=headers)
        file_size = int(response.headers.get('Content-Length', 0))

        # 自动识别文件名和扩展名
        filename = url.split('/')[-1] or 'downloaded_file'
        filename = ".\\temp\\"+clean_filename(filename).removeprefix("&pid=hp")


        # 设定分段大小
        chunk_size = 1024 * 200  # 200KB
        num_chunks = (file_size // chunk_size) + 1
        logging.info("开始获取数据")
        logging.info(f"开始下载 {filename}，总大小: {file_size} bytes，分为 {num_chunks} 段。")

        with open(filename, 'wb') as file:
            for i in range(num_chunks):
                pb1.set(i/num_chunks)
                logging.info(f"下载进度更新 {i/num_chunks*100:.2f}%")
                root.update()
                start = i * chunk_size
                end = min(start + chunk_size - 1, file_size - 1)

                # 设置Range请求头
                range_header = {'Range': f'bytes={start}-{end}'}
                chunk_response = requests.get(url, headers={**headers, **range_header}, stream=True)
                root.update()
                if chunk_response.status_code in (200, 206):  # 206表示部分内容
                    file.write(chunk_response.content)
                    logging.info(f"下载段 {i + 1}/{num_chunks} 完成，大小: {len(chunk_response.content)} bytes")
                else:
                    logging.info(f"下载失败，状态码: {chunk_response.status_code}")
                    tkt.dialogs.TkMessage(f"下载失败，状态码: {chunk_response.status_code}", title="错误", icon="error")
                    os._exit(0)
        # print(bing_data_name)
        fn=filename
        b_title=bing_data[0]['title']
        b_copyright=bing_data[0]['copyright']
        logging.info("资源加载完成！")
        main()
    except Exception as e:
        tkt.dialogs.TkMessage(f"资源加载失败，详细错误信息请查看日志", title="错误", icon="error")
        logging.error("资源加载失败")
        logging.error(e)
        fn="./assets/images/no_images.jpg"
        b_title="资源加载失败"
        b_copyright="详细错误信息请查看日志"
        main()

def start_task():
    # 启动任务
    root.after(100, task)  # 使用after方法非阻塞地启动任务
canvas_loading = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
# canvas_loading.place(width=1280, height=720, x=640, y=360, anchor="center")
# progress = tkt.Progressbar(root, orient="horizontal", length=300, mode="determinate")

### ✨ 更新
canvas_index = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas_update = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas_update_download = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
def download_update(update_file_url:str):
    global wallpaper_path
    canvas_update_download.delete("all")
    canvas_update_download.place_forget()
    canvas_update_download.place(x=640, y=205, width=1280, height=395, anchor="n")

    def long_running_task1():
        global wallpaper_path
        try:
            url = update_file_url
            root.update()

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
            }

            s = requests.Session()
            s.headers.update(headers)

            for attempt in range(3):
                
                resp = s.get(url, stream=True)
                if resp.status_code == 200:
                    break
                elif resp.status_code == 521:
                    logging.warning(f"第 {attempt + 1} 次尝试下载失败，状态码：{resp.status_code}")
                    time.sleep(1)  # 等待一段时间后重试
                else:
                    raise Exception(f"下载失败，状态码：{resp.status_code}")

            if resp.status_code != 200:
                raise Exception(f"下载失败，状态码：{resp.status_code}")

            guessed_type = update_available[4]

            filename = f"./temp/update.{guessed_type}"
            wallpaper_path = filename

            # 确保临时目录存在
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            logging.info(f"开始下载 {filename}")
            total_size = int(resp.headers.get('content-length', 0))
            downloaded_size = 0
            chunk_size = 512
            with open(filename, "wb") as f:
                for chunk in resp.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        progress = downloaded_size / total_size * 100
                        pb1.set(progress)  # 更新进度条
                        root.update_idletasks()  # 刷新界面

            logging.info("下载完成！")
            canvas_update_download.place_forget()
            root.withdraw()
            run_installer(f"{get_executable_directory()}\\temp\\update.{update_available[4]}")
            sys.exit()

        except Exception as e:
            logging.error(f"下载失败: {e}")
            tkt.dialogs.TkMessage("下载失败，详细错误信息请查看日志", title="错误", icon="error")
            canvas_update_download.place_forget()
            os._exit(0)

    def start_task1(*args):
        root.after(1000, long_running_task1)

    canvas_update_download.place_forget()
    canvas_update_download.place(width=1280, height=720, x=640, y=360, anchor="center")
    tkt.Text(canvas_update_download, (100, 100), text="正在下载更新安装包...", fontsize=50, anchor="nw")
    pb1 = tkt.ProgressBar(canvas_update_download, (420, 260), (380, 8))

    start_task1()
def update_window():
    canvas_index.place_forget()
    canvas_index.delete("all")
    canvas_update.delete("all")
    canvas_loading.delete("all")
    def go_pass_update(*args):
        bing_index_loading()     
    def update_now():
        
        logging.info("开始更新程序")
        
        if cog["use_proxy"]:
            logging.info(f"使用代理:{cog["proxy_url"]}")
            download_update(cog["proxy_url"]+update_available[3])
            
        else:
            download_update(update_available[3])
        


    # canvas.delete("all")
    canvas_update.place(width=1280, height=720, x=640, y=360, anchor="center")
    tkt.Text(canvas_update,(120,50),text="有可用更新!",fontsize=40,anchor="nw")
    tkt.Text(canvas_update,(120,110),text=f"当前版本：{VER}最新版本：{update_available[1]}",fontsize=20,anchor="nw")
    tkt.Text(canvas_update,(150,150),text="更新日志：\n\n"+update_available[2],fontsize=20,anchor="nw")
    # canvas.create_text(60, 150, text=f"更新日志：\n\n{update_available[2]}", font=25,anchor="nw")
    canvas_pass=tkt.Canvas(canvas_update, zoom_item=True, keep_ratio="min", free_anchor=True)
    canvas_pass.place(x=1250, y=690,width=220,height=30,anchor="center")
    tkt.Text(canvas_pass, (10,10), text="忽略(不推荐)",fontsize=18,anchor="nw")
    canvas_pass.bind("<Button-1>", lambda event: go_pass_update())
    # pass_update=canvas_update.create_text(1200,700,text="忽略(不推荐)",font=18)
    # canvas_update.tag_bind(pass_update, "<Button-1>", lambda event: go_pass_update())
    tkt.Button(canvas_update, [750,550],text="前往官网手动更新", size=[220,100], command=lambda: webbrowser.open("https://shu-shu-1.github.io/wallpaper/"))
    tkt.Button(canvas_update, [1020,550],text="立即更新(推荐)", size=[220,100], command=lambda: update_now())

# def fetch_latest_release(url_primary, url_backup, local_version, update_channel):
#     try:
#         response = requests.get(url_primary)
#         response.raise_for_status()
#     except requests.exceptions.RequestException:
#         try:
#             response = requests.get(url_backup)
#             response.raise_for_status()
#         except requests.exceptions.RequestException:
#             return [False, None, None, None]

#     releases = response.json()

#     # Filter releases based on the update channel
#     if update_channel == "latest":
#         releases = [release for release in releases if not release["prerelease"]]
#     elif update_channel == "prerelease":
#         releases = [release for release in releases if release["prerelease"]]
#     else:
#         return [True, "V6.0.0.1测试版本号","以下为Lorem Ipsum占位文本\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla at ligula vel velit suscipit ultricies. \nAliquam sit amet nisl sit amet metus semper tincidunt. Morbi velit est, auctor in fringilla eu, \ntincidunt non tortor. Mauris molestie felis turpis. Phasellus eu venenatis ante, et venenatis velit. \nMorbi sed faucibus orci. Suspendisse tincidunt risus non hendrerit maximus.\n\n感谢你参与本次测试！(≧∇≦)ﾉ\n\t\t\t\t-更新提示测试-", None]


#     # Sort releases in descending order (latest first)
#     releases.sort(key=lambda x: x["name"], reverse=True)

#     for release in releases:
#         if compare_versions(local_version, release["name"]):
#             # Remove the "国内镜像下载" section from the end of the body
#             body = release["body"]
#             body = body.rsplit("\n", 1)[0]

#             # Get the first asset's download link
#             download_link = release["assets"][0]["browser_download_url"] if release["assets"] else None

#             return [
#                 True,
#                 release["name"],
#                 body,
#                 download_link
#             ]

#     return [False, None, None, None]
def fetch_latest_release(ty : str = cog["update_channel"]):
    # return False
    logging.info(f"开始检查更新，更新渠道：{ty}")
    if ty == "Stable" or ty == "Dev":
        try:
            
            try:
                logging.info("尝试使用第一API获取")
                update_web_json=json.loads(requests.get("https://raw.kkgithub.com/shu-shu-1/API/main/xiaoshu%20wallpaper/v2/update.json").text)
            except:
                logging.info("尝试使用第二API获取")
                update_web_json=json.loads(requests.get("https://fastly.jsdelivr.net/gh/shu-shu-1/API@main/xiaoshu%20wallpaper/v2/update.json").text)
            web_ver=update_web_json["update_channels"][ty]["version"]
            web_download_url=update_web_json["update_channels"][ty]["download_link"]
            web_update_note=update_web_json["update_channels"][ty]["update_content"]
            web_file_format=update_web_json["update_channels"][ty]["file_format"]
            if compare_versions(web_ver,VER) == 1:
                logging.info(f"发现新版本,版本号：{web_ver}，更新内容：{web_update_note}，下载地址：{web_download_url}，文件格式：{web_file_format}")
                return [True,web_ver,web_update_note,web_download_url,web_file_format]
            else:
                logging.info(f"当前版本已是最新版本,最新版本号：{web_ver}")
                return [False,None,None,None,None]
        except Exception as e:
            logging.error(f"更新失败：{e}")
            return ["Error"]
    elif ty == "test_update":
        logging.info("测试更新")
        return [True, "V6.0.0.1测试版本号","以下为Lorem Ipsum占位文本\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla at ligula vel velit suscipit ultricies. \nAliquam sit amet nisl sit amet metus semper tincidunt. Morbi velit est, auctor in fringilla eu, \ntincidunt non tortor. Mauris molestie felis turpis. Phasellus eu venenatis ante, et venenatis velit. \nMorbi sed faucibus orci. Suspendisse tincidunt risus non hendrerit maximus.\n\n感谢你参与本次测试！(≧∇≦)ﾉ\n\t\t\t\t-更新提示测试-", None, None]
def check_update():
    global have_update,update_available
    # 检查更新
    update_available = fetch_latest_release()
    if update_available[0] == False:
        bing_index_loading()
    elif update_available[0] == True:
        # 如果有更新，显示对话框
        # tkt.dialogs.TkMessage(icon="info",title="更新",message="有可用更新",detail="请前往GitHub下载最新版本。")
        have_update=True
        update_window()
if cog["check_update"]:
    # bing_index_loading()
    check_update()
    # image_path2 = fn
else:
    bing_index_loading()
    # image_path2 = fn
is_load_main=False

### ✨ 主界面
def index_window(*args):
    global b_title, b_copyright, is_load_main, cropped_image_cache
    # canvas_index.place(width=1280, height=720, x=640, y=360, anchor="center")
    is_load_main = True
    canvas_loading.place_forget()

    # 初始化裁剪图片的缓存
    if 'cropped_image_cache' not in globals():
        cropped_image_cache = None

    to_setting_icon = tkt.Canvas(canvas_index, zoom_item=True, keep_ratio="min", free_anchor=True)
    to_setting_icon.place(x=50, y=670, width=40, height=50, anchor="center")
    tkt.Text(to_setting_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons", anchor="nw")
    to_setting_icon.bind("<Button-1>", lambda event: setting())

    to_about_icon = tkt.Canvas(canvas_index, zoom_item=True, keep_ratio="min", free_anchor=True)
    to_about_icon.place(x=100, y=670, width=40, height=53, anchor="center")
    tkt.Text(to_about_icon, (0, 10), text="", fontsize=43, family="Segoe Fluent lcons", anchor="nw")
    to_about_icon.bind("<Button-1>", lambda event: about(), add="+")
    to_about_icon.bind("<Button-2>", lambda event: about(), add="+")
    to_about_icon.bind("<Button-3>", lambda event: egg(), add="+")

    go_in_icon = tkt.Canvas(canvas_index, zoom_item=True, keep_ratio="min", free_anchor=True)
    go_in_icon.place(x=1230, y=670, width=40, height=50, anchor="center")
    tkt.Text(go_in_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons", anchor="nw")
    go_in_icon.bind("<Button-1>", lambda event: wallpaper())



    tkt.Text(canvas_index, [50, 70], text="主页", fontsize=40, anchor="w")
    tkt.Text(canvas_index, [50, 110], text="小树壁纸6.0", fontsize=25, anchor="w")

    @lru_cache(maxsize=None)
    def load_and_crop_image(image_path):
        original_image = Image.open(image_path)
        left = (original_image.size[0] - (original_image.size[0] // 2 - 10)) // 2
        right = left + (original_image.size[0] // 2 + 10)
        upper = (original_image.size[1] - 300) // 2
        lower = upper + 200
        upper = max(upper, 0)
        cropped_image = original_image.crop((left, upper, right, lower))
        return cropped_image

    # 使用缓存的裁剪图片
    if cropped_image_cache is None:
        cropped_image_cache = load_and_crop_image(fn)
    
    tkt.Image(canvas_index, [640, 320], image=tkt.PhotoImage(cropped_image_cache),anchor="center")
    tkt.Text(canvas_index, (640, 100), text=f"今日Bing\n{b_title}\n{b_copyright}", fontsize=20, anchor="n", justify='center')

    tkt.Text(canvas_index, (640, 440), text=f"详细信息", fontsize=15, anchor="n", justify='center')

    more_about_pic_icon = tkt.Canvas(canvas_index, zoom_item=True, keep_ratio="min", free_anchor=True)
    more_about_pic_icon.place(x=640, y=490, width=40, height=50, anchor="center")
    tkt.Text(more_about_pic_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons", anchor="nw")
    
    if fn == "./assets/images/no_images.jpg":
        more_about_pic_icon.bind("<Button-1>", lambda event: tkt.dialogs.TkMessage(icon="error", title="没有图片数据", message="数据获取失败，请稍后再试。"))
    else:
        more_about_pic_icon.bind("<Button-1>", lambda event: more_bing())

    if have_update:
            update_icon = tkt.Canvas(canvas_index, zoom_item=True, keep_ratio="min", free_anchor=True)
            update_icon.place(x=1280 // 2, y=670,width=40,height=50,anchor="center")
            tkt.Text(update_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
            update_icon.bind("<Button-1>", lambda event: update_window())



### ✨ 设置面板
canvas_setting = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
# canvas_setting.place(width=1280, height=720, x=640, y=360, anchor="center")
tkt.Switch(canvas_setting, (20, 25), command=lambda b: tkt.style.set_color_mode(
"dark" if b else "light"), default=tkt.style.SYSTEM_DARK_MODE)
back_canvas1 = tkt.Canvas(canvas_setting, zoom_item=True, keep_ratio="min", free_anchor=True)
# back_canvas1.place(x=50, y=670,width=40,height=40,anchor="center")
back_canvas1.place(x=50, y=670,width=40,height=40,anchor="center")
tkt.Text(back_canvas1, (0, 0), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
back_canvas1.bind("<Button-1>", lambda event: main())
tkt.Text(canvas_setting, (100, 50), text="设置", fontsize=50)
tkt.Text(canvas_setting,[1280//2, 720//2-100],text="施工中，请等待后续测试版本〜",fontsize=50, anchor="center")
tkt.SegmentedButton(canvas_setting, [80, 200], texts=["主题", "数据", "关于", "退出"], layout="vertical")
# # 设置目标宽度或高度
# base_width1 = 150  # 你可以根据需要调整这个值
# # 计算比例并调整图片大小
# img1 = Image.open(r"./assets/images/未完成.jpg")
# w_percent1 = base_width1 / float(img1.size[0])
# h_size1 = int(float(img1.size[1]) * float(w_percent1))
# img1 = img1.resize((base_width1, h_size1), Image.Resampling.LANCZOS)
# tkt.Image(canvas_setting,[1280//2, 720//2+50],image=tkt.PhotoImage(img1))

true_del = False
def clear_folder(folder_path, exclude_list=[]):
    """
    清空指定文件夹中的所有文件和子文件夹，但排除指定的文件或文件夹

    参数:
    folder_path (str): 要清空的文件夹路径
    exclude_list (list): 要排除的文件或文件夹名称列表
    """
    logging.info(f"准备清空文件夹: {folder_path}")
    logging.info(f"排除列表: {exclude_list}")

    try:
        for filename in os.listdir(folder_path):
            if filename in exclude_list:
                logging.info(f"跳过排除的文件或文件夹: {filename}")
                continue  # 跳过排除的文件或文件夹
            file_path = os.path.join(folder_path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    logging.info(f"删除文件或链接: {file_path}")
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    logging.info(f"删除子文件夹: {file_path}")
                    shutil.rmtree(file_path)
            except Exception as e:
                logging.warning(f"无法删除 {file_path}。原因: {e}")
        logging.info(f"文件夹 {folder_path} 清理完成")
    except Exception as e:
        logging.warning(f"无法清理文件夹 {folder_path}。原因: {e}")

def return_choice(result):
    global true_del
    logging.info(f"用户选择: {result}")
    if result == "yes":
        true_del = True
        logging.info("用户确认清空文件夹")
    else:
        true_del = False
        logging.info("用户取消清空文件夹")

def del_temp_folder():
    logging.info("请求用户确认清空缓存文件夹")
    tkt.dialogs.TkMessage(
        icon="question", title="警告",
        message="你确定要清空 缓存 文件夹吗？",
        detail="此操作不可恢复！", type="yesno",
        default="no", command=lambda result: return_choice(result)
    )
    if true_del:
        logging.info("开始清空缓存文件夹")
        del_temp.disabled()
        clear_folder("temp", exclude_list=[os.path.basename(fn)])
        tkt.dialogs.TkMessage(icon="info", title="完成", message="缓存清理完成！")
        del_temp.disabled(False)

    else:
        logging.info("清空缓存文件夹操作已取消")

def del_log_folder():
    logging.info("请求用户确认清空日志文件夹")
    tkt.dialogs.TkMessage(
        icon="warning", title="警告",
        message="你确定要清空 日志 文件夹吗？\n你需要知道你正在做什么! \n日志文件对于查找错误非常重要",
        detail="这是一个危险行为，请谨慎操作！", type="yesno",
        default="no", command=lambda result: return_choice(result)
    )
    if true_del:
        logging.info("开始清空日志文件夹")
        del_log.disabled()
        clear_folder("logs", exclude_list=[os.path.basename(LOG_FILE)])
        tkt.dialogs.TkMessage(icon="info", title="完成", message="日志清理完成！")

        del_log.disabled(False)
    else:
        logging.info("清空日志文件夹操作已取消")
del_temp=tkt.Button(canvas_setting, (1280//2-150, 720//2), text="清空缓存", command=lambda: del_temp_folder())

del_log=tkt.Button(canvas_setting, (1280//2+150, 720//2), text="清空日志", command=lambda: del_log_folder())




### ✨ 彩蛋
def set_eggwallpaper():
    shutil.copyfile("./assets/images/egg.jpg", "C:/xiaoshu_wallpaper/bk.jpg")
    set_wallpaper("C:/xiaoshu_wallpaper/bk.jpg")
    tkt.dialogs.TkMessage(icon="info",title="完成",message="设置成功！",detail="已将彩蛋壁纸设置为桌面背景。")
    notification.notify(
        title='壁纸设置完成',
        message=f'壁纸文件位于：C:/xiaoshu_wallpaper\n文件名：bk.jpg\n请勿删除！',
        app_icon="./assets/icon/icon.ico",
        timeout=3,
    )
canvas_egg = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
tkt.Text(canvas_egg, (100, 100), text="彩蛋", fontsize=50)
tkt.Text(canvas_egg, (100, 150), text="恭喜你发现了一个彩蛋！", fontsize=25, anchor="w")
canvas_artistic = tkt.Canvas(canvas_egg, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas_artistic.place(x=50, y=650,width=200,height=40,anchor="nw")
tkt.Text(canvas_artistic, (60, 10), text="画师：灵楼", fontsize=20, anchor="n", underline=True)
canvas_artistic.bind("<Button-1>", lambda event: webbrowser.open("https://space.bilibili.com/3546659155871883"))
back_egg = tkt.Canvas(canvas_egg, zoom_item=True, keep_ratio="min", free_anchor=True)
back_egg.place(x=1200, y=50,width=40,height=50,anchor="center")
tkt.Text(back_egg, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
back_egg.bind("<Button-1>", lambda event: main())
set_wallpaper_egg_icon = tkt.Canvas(canvas_egg, zoom_item=True, keep_ratio="min", free_anchor=True)
set_wallpaper_egg_icon.place(x=1200, y=150,width=40,height=50,anchor="center")
tkt.Text(set_wallpaper_egg_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
set_wallpaper_egg_icon.bind("<Button-1>", lambda event: set_eggwallpaper())
tkt.Text(canvas_egg, (1170, 190), text="设为壁纸", fontsize=15, anchor="w")
# 打开图片
img = Image.open(r"./assets/images/egg.jpg")
# 设置目标宽度或高度
base_width = 300
# 计算比例并调整图片大小
w_percent = base_width / float(img.size[0])
h_size = int(float(img.size[1]) * float(w_percent))
img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)
tkt.Image(canvas_egg, (200, 400), image=tkt.PhotoImage(img))

### ✨ 关于面板
canvas_about = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
# canvas_about.place(width=1280, height=720, x=640, y=360, anchor="center")
back_canvas.place(x=50, y=670,width=40,height=40,anchor="center")
tkt.Text(back_canvas, (0, 0), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
back_canvas.bind("<Button-1>", lambda event: main())
tkt.Text(canvas_about, (100, 100), text="关于", fontsize=50, anchor="center")
tkt.Text(canvas_about, (100, 150), text="小树壁纸", fontsize=35, anchor="w")
tkt.Text(canvas_about, (100, 185), text=f"{VER}(内部版本号：{software_VER})", fontsize=20, anchor="w")
tkt.Text(canvas_about, (100, 250), text="制作：小树\n出品：小树工作室\n感谢所有参与测试的人！\n\n本程序基于AGPL-3.0 license开源", fontsize=20, anchor="nw")
kaiyuan=tkt.Text(canvas_about, (100, 385), text="感谢开源项目tkintertools:https://github.com/Xiaokang2022/tkintertools\n本程序仅供个人学习交流使用，请勿用于商业用途！", fontsize=20, anchor="nw")
canvas_about.tag_bind(kaiyuan, "<Button-1>", lambda event: webbrowser.open("https://github.com/Xiaokang2022/tkintertools"))
back_about = tkt.Canvas(canvas_about, zoom_item=True, keep_ratio="min", free_anchor=True)
back_about.place(x=50, y=670,width=40,height=40,anchor="center")
tkt.Text(back_about, (0, 0), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
back_about.bind("<Button-1>", lambda event: main())

### ✨ 壁纸面板
wallpaper_path = "./assets/images/no_images.jpg"
canvas_wallpaper = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
# canvas_wallpaper_more = tkt.Canvas(canvas_wallpaper, zoom_item=True, keep_ratio="min", free_anchor=True)
# canvas_wallpaper_more.place(x=640, y=205,width=1280,height=395,anchor="n")
canvas_wallpaper_more_unsplash = tkt.Canvas(canvas_wallpaper, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas_wallpaper_more_unsplash.place(x=640, y=205,width=1280,height=395,anchor="n")
canvas_wallpaper_more_wallhaven = tkt.Canvas(canvas_wallpaper, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas_wallpaper_more_wallhaven.place(x=640, y=205,width=1280,height=395,anchor="n")
canvas_wallpaper_more_erciyuan = tkt.Canvas(canvas_wallpaper, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas_wallpaper_more_erciyuan.place(x=640, y=205,width=1280,height=395,anchor="n")
canvas_wallpaper_more_fengjing = tkt.Canvas(canvas_wallpaper, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas_wallpaper_more_fengjing.place(x=640, y=205,width=1280,height=395,anchor="n")
canvas_wallpaper_more_360 = tkt.Canvas(canvas_wallpaper, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas_wallpaper_more_360.place(x=640, y=205,width=1280,height=395,anchor="n")
canvas_wallpaper_more_360_dowload = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
# 1280x720
# canvas_wallpaper.place(width=1280, height=720, x=640, y=360, anchor="center")
tkt.Text(canvas_wallpaper, (50, 50), text="壁纸源", fontsize=50,anchor="nw")
back_wallpaper = tkt.Canvas(canvas_wallpaper, zoom_item=True, keep_ratio="min", free_anchor=True)
back_wallpaper.place(x=50, y=670,width=40,height=40,anchor="center")
tkt.Text(back_wallpaper, (0, 0), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
back_wallpaper.bind("<Button-1>", lambda event: main())
canvas_wallpaper_detail=tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
#### 壁纸面板-壁纸详情
def wallpaper_detail(*args):
    canvas_wallpaper.place_forget()
    def save_as():
        file_path = filedialog.asksaveasfilename(title="保存壁纸", filetypes=[("图片文件", os.path.splitext(wallpaper_path)[1])])
        if file_path:
            shutil.copyfile(wallpaper_path, file_path)
            os.system(f"explorer.exe /select,\"{file_path.replace("/","\\")}\"")

            notification.notify(
                title='壁纸保存成功',
                message=f'壁纸文件已保存至{file_path}\n文件名：{os.path.basename(file_path)}',
                app_icon="./assets/icon/icon.ico",
                timeout=3,
            )
    def download():
        shutil.copyfile(wallpaper_path, f"{cog["download_path"]}\\{os.path.basename(wallpaper_path)}")
        os.system(f"explorer.exe /select,\"{cog["download_path"]}\\{os.path.basename(wallpaper_path)}\"")
        notification.notify(
            title='壁纸下载完成',
            message=f'壁纸文件已保存至{cog["download_path"]}\n文件名：{os.path.basename(wallpaper_path)}',
            app_icon="./assets/icon/icon.ico",
            timeout=3,
        )
    def copy_wallpaper():

        copy_image_to_clipboard(wallpaper_path)
        notification.notify(
            title='壁纸复制成功',
            message='壁纸文件已复制到剪贴板啦~',  
            app_icon="./assets/icon/icon.ico",
            timeout=3,
        )
    def _set_wallpaper():
        copy_and_set_wallpaper(wallpaper_path)

        notification.notify(
            title='壁纸设置完成',
            message=f'壁纸文件位于：C:\\xiaoshu_wallpaper\\\n文件名：{os.path.basename(wallpaper_path)}\n请勿删除！',
            app_icon="./assets/icon/icon.ico",
            timeout=3,
        )

    ImageFile.LOAD_TRUNCATED_IMAGES = True
    # canvas_wallpaper.delete("all")
    canvas_wallpaper_detail.place_forget()
    canvas_wallpaper_detail.delete("all")
    canvas_wallpaper_detail.place(x=640, y=720//2,width=1280,height=720,anchor="center")
    tkt.Text(canvas_wallpaper_detail, (80, 50), text="壁纸详情", fontsize=50,anchor="nw")
    back_wallpaper_detail = tkt.Canvas(canvas_wallpaper_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    back_wallpaper_detail.place(x=50, y=670,width=40,height=40,anchor="center")
    tkt.Text(back_wallpaper_detail, (0, 0), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    back_wallpaper_detail.bind("<Button-1>", lambda event: wallpaper())
    # tkt.Text(canvas_wallpaper_detail, (100, 150), text="壁纸来源：", fontsize=30,anchor="nw")
    # tkt.Text(canvas_wallpaper_detail, (100, 200), text="Unsplash", fontsize=30,anchor="nw")
    # tkt.Text(canvas_wallpaper_detail, (100, 250), text="Wallhaven", fontsize=30,anchor="nw")
    tkt.Image(canvas_wallpaper_detail,[80,120],image=resize_image(wallpaper_path,250),anchor="nw")
    
    # tkt.Button(canvas_wallpaper_detail, (100, 600), text="设为壁纸", command=lambda: copy_and_set_wallpaper(wallpaper_path))

    set_w_bing_icon = tkt.Canvas(canvas_wallpaper_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    set_w_bing_icon.place(x=1230, y=670,width=40,height=50,anchor="center")
    tkt.Text(set_w_bing_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    set_w_bing_icon.bind("<Button-1>", lambda event: _set_wallpaper())
    tkt.Text(canvas_wallpaper_detail,(1230, 705),text="设为壁纸",fontsize=15,anchor="center")
    ll_icon = tkt.Canvas(canvas_wallpaper_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    ll_icon.place(x=1150, y=670,width=40,height=50,anchor="center")
    tkt.Text(ll_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    ll_icon.bind("<Button-1>", lambda event: save_as())
    tkt.Text(canvas_wallpaper_detail,(1150, 705),text="另存为",fontsize=15,anchor="center")
    dd_icon = tkt.Canvas(canvas_wallpaper_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    dd_icon.place(x=1070, y=670,width=40,height=50,anchor="center")
    tkt.Text(dd_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    dd_icon.bind("<Button-1>", lambda event: download())
    tkt.Text(canvas_wallpaper_detail,(1070, 705),text="下载",fontsize=15,anchor="center")
    copy_w_bing_icon = tkt.Canvas(canvas_wallpaper_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    copy_w_bing_icon.place(x=990, y=670,width=40,height=50,anchor="center")
    tkt.Text(copy_w_bing_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    copy_w_bing_icon.bind("<Button-1>", lambda event: copy_wallpaper())
    tkt.Text(canvas_wallpaper_detail,(990, 705),text="复制",fontsize=15,anchor="center")   
    
    # tkt.Text(canvas_wallpaper_detail, (100, 650), text="壁纸来源：", fontsize=30,anchor="nw")

#### 壁纸面板-Unsplash源
# def wallpaper_unsplash():
#     # global wallpaper_source_name
#     # wallpaper_source_name=value
#     # canvas_wallpaper_more.delete("all")
#     canvas_wallpaper_more_erciyuan.place_forget()
#     canvas_wallpaper_more_wallhaven.place_forget()
#     canvas_wallpaper_more_fengjing.place_forget()
#     canvas_wallpaper_more_unsplash.place(x=640, y=205,width=1280,height=395,anchor="n")
#     wallpaper_choose_button.set(0)
#     def random_size():
#         global unsplash_size
#         unsplash_size=0
#     def unsplash_1080P():
#         global unsplash_size
#         unsplash_size=1
#     def download_wallpaper():
#         if unsplash_size:
#             url = f"https://source.unsplash.com/random/1920x1080/"
#         else:
#             url = f"https://source.unsplash.com/random"
#     tkt.SegmentedButton(canvas_wallpaper_more_unsplash, (100, 25),texts= ["随机大小","1920x1080"], commands=(random_size, unsplash_1080P), default=0)
#     tkt.Button(canvas_wallpaper_more_unsplash, (450, 30), text="获取数据", command=lambda: download_wallpaper())

#### 壁纸面板-聚合源通用下载

def download_wallpaper():
    global wallpaper_path
    global api_url
    canvas_download.delete("all")
    canvas_download.place_forget()
    canvas_download.place(x=640, y=205, width=1280, height=395, anchor="n")

    def long_running_task1():
        global wallpaper_path
        try:
            url = api_url
            root.update()

            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
            }

            s = requests.Session()
            s.headers.update(headers)

            for attempt in range(3):
                resp = s.get(url, stream=True)
                if resp.status_code == 200:
                    break
                elif resp.status_code == 521:
                    logging.warning(f"第 {attempt + 1} 次尝试下载失败，状态码：{resp.status_code}")
                    time.sleep(1)  # 等待一段时间后重试
                else:
                    raise Exception(f"下载失败，状态码：{resp.status_code}")

            if resp.status_code != 200:
                raise Exception(f"下载失败，状态码：{resp.status_code}")

            content_type = resp.headers.get('Content-Type')
            guessed_type = mimetypes.guess_extension(content_type)
            if not guessed_type:
                guessed_type = ".webp"  # 默认文件扩展名

            filename = f"./temp/{time.strftime('anime_%Y-%m-%d_%H-%M-%S', time.localtime())}{guessed_type}"
            wallpaper_path = filename

            # 确保临时目录存在
            os.makedirs(os.path.dirname(filename), exist_ok=True)

            logging.info(f"开始下载 {filename}")

            total_size = int(resp.headers.get('content-length', 0))
            downloaded_size = 0
            chunk_size = 512

            with open(filename, "wb") as f:
                for chunk in resp.iter_content(chunk_size=chunk_size):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        progress = downloaded_size / total_size * 100
                        pb1.set(progress)  # 更新进度条
                        root.update_idletasks()  # 刷新界面

            logging.info("下载完成！")
            canvas_download.place_forget()
            wallpaper_detail()

        except Exception as e:
            logging.error(f"下载失败: {e}")
            tkt.dialogs.TkMessage("下载失败，详细错误信息请查看日志", title="错误", icon="error")
            canvas_download.place_forget()
            wallpaper()  # 返回壁纸页面

    def start_task1(*args):
        root.after(1000, long_running_task1)

    canvas_detail.place_forget()
    canvas_download.place(width=1280, height=720, x=640, y=360, anchor="center")
    tkt.Text(canvas_download, (100, 100), text="正在下载...", fontsize=50, anchor="nw")
    # global pb1
    pb1 = tkt.ProgressBar(canvas_download, (420, 260), (380, 8))

    start_task1()
#### 壁纸面板-Wallhaven源
def wallpaper_wallhaven():
    # global wallpaper_source_name
    # wallpaper_source_name=value
    # canvas_wallpaper_more.delete("all")
    global api_url
    canvas_wallpaper_more_unsplash.place_forget()
    canvas_wallpaper_more_erciyuan.place_forget()
    canvas_wallpaper_more_fengjing.place_forget()
    canvas_wallpaper_more_360.place_forget()
    canvas_wallpaper_more_wallhaven.place(x=640, y=205,width=1280,height=395,anchor="n")
    wallpaper_choose_button.set(0)
    api_url="https://api.nguaduot.cn/wallhaven/random"
    def random_wallhaven():
        global api_url
        api_url="https://api.nguaduot.cn/wallhaven/random"
    def today_wallhaven():
        global api_url
        api_url="https://api.nguaduot.cn/wallhaven/today"
    def ch_return(ch1):
        (random_wallhaven, today_wallhaven)[ch1]()
    tkt.SegmentedButton(canvas_wallpaper_more_wallhaven, (100, 25),texts= ["随机","每日"], command=ch_return, default=0)
    tkt.Button(canvas_wallpaper_more_wallhaven, (450, 30), text="获取数据", command=lambda: download_wallpaper())  

#### 壁纸面板-风景源
def wallpaper_风景():
    global api_url
    # global wallpaper_source_name
    # wallpaper_source_name=value
    # canvas_wallpaper_more.delete("all")
    canvas_wallpaper_more_unsplash.place_forget()
    canvas_wallpaper_more_wallhaven.place_forget()
    canvas_wallpaper_more_erciyuan.place_forget()
    canvas_wallpaper_more_360.place_forget()
    canvas_wallpaper_more_fengjing.place(x=640, y=205,width=1280,height=395,anchor="n")
    api_url="https://api.dujin.org/pic/fengjing"
    def 风景_ch(ch1):
        global api_url
        match ch1:
            case 0:
                api_url="https://api.dujin.org/pic/fengjing"
            case 1:
                api_url="https://tu.ltyuanfang.cn/api/fengjing.php"
    tkt.SegmentedButton(canvas_wallpaper_more_fengjing, (100, 25),texts= ["缙哥哥接口","远方接口"], command=风景_ch, default=0)
    tkt.Button(canvas_wallpaper_more_fengjing, (450, 30), text="获取数据", command=lambda: download_wallpaper())    
is_choose=None
#### 壁纸面板-二次元源
def wallpaper_二次元():
    global wallpaper_path
    global api_url
    # global wallpaper_source_name
    # wallpaper_source_name=value
    global is_choose
    if is_choose!=None:
        is_choose.destroy()
    # canvas_wallpaper_more.delete("all")
    canvas_wallpaper_more_unsplash.place_forget()
    canvas_wallpaper_more_wallhaven.place_forget()
    canvas_wallpaper_more_fengjing.place_forget()
    canvas_wallpaper_more_360.place_forget()
    canvas_wallpaper_more_erciyuan.place(x=640, y=205,width=1280,height=395,anchor="n")
    api_url="https://api.paugram.com/wallpaper/?source=sm"
    def paul_wallpaper():
        global is_choose,canvas_wallpaper_more_erciyuan,api_url
        api_url="https://api.paugram.com/wallpaper/?source=sm"
        if is_choose!=None:
            is_choose.destroy()

        def paul_ch(ch1):
            global api_url
            match ch1:
                case 0:
                    api_url="https://api.paugram.com/wallpaper/?source=sm"
                case 1:
                    api_url="https://api.paugram.com/wallpaper/?source=github"

        is_choose=tkt.SegmentedButton(canvas_wallpaper_more_erciyuan, (100, 75),texts= ["sm.ms-白底动漫","github.io-白底动漫"], command=paul_ch, default=0)
    def ciyuan_wallpaper():
        global is_choose,canvas_wallpaper_more_erciyuan,api_url
        api_url="https://t.mwm.moe/ysz"
        if is_choose!=None:
            is_choose.destroy()
        def ciyuan_ch(ch1):
            global api_url
            match ch1:
                case 0:
                    api_url="https://t.mwm.moe/ysz"
                case 1:
                    api_url="https://t.mwm.moe/pc"
                case 2:
                    api_url="https://t.mwm.moe/ai"
                case 3:
                    api_url="https://t.mwm.moe/fj"
                case 4:
                    api_url="https://t.mwm.moe/xhl"
                case 5:
                    api_url="https://t.mwm.moe/moe"

        is_choose=tkt.SegmentedButton(canvas_wallpaper_more_erciyuan, (100, 75),texts= ["原神","随机","AI生成","风景","小狐狸","萌图"], command=ciyuan_ch, default=0)
    def other_wallpaper():
        global is_choose,canvas_wallpaper_more_erciyuan,api_url
        api_url="https://api.imlcd.cn/bg/acg.php"
        if is_choose!=None:
            is_choose.destroy()
        def other_wallpaper_ch(ch1):
            global api_url
            match ch1:
                case 0:
                    api_url="https://api.imlcd.cn/bg/acg.php"
                case 1:
                    api_url="https://img.paulzzh.com/touhou/random"
                case 2:
                    api_url="https://www.dmoe.cc/random.php" 
                
        is_choose=tkt.SegmentedButton(canvas_wallpaper_more_erciyuan, (100, 75),texts= ["[忆云]随机","[PAULZZH]东方","[樱花]随机"], command=other_wallpaper_ch, default=0)


    def 二次元_ch(ch1):
        global api_url
        match ch1:
            case 0:
                paul_wallpaper()
            case 1:
                ciyuan_wallpaper()
            case 2:
                other_wallpaper()
        # print(bing_data)
    tkt.SegmentedButton(canvas_wallpaper_more_erciyuan, (100, 25),texts=["保罗源", "次元源","其他源"], command=二次元_ch, default=0)
    # tkt.SegmentedButton(canvas_wallpaper_more, (100, 25),layout="vertical",texts=["[保罗]sm.ms-动漫", "[保罗]github.io-动漫", "[次元]原神","[次元]随机","[次元]AI生成","[次元]风景","[次元]小狐狸","[次元]萌图","[樱花]随机","[PAULZZH]东方"], commands=(), default=0)
    is_choose=None
    paul_wallpaper()
    tkt.Button(canvas_wallpaper_more_erciyuan, (600, 30), text="获取数据", command=lambda: download_wallpaper()) 

def wallpaper_360():
    global api_url,tid
    canvas_wallpaper_more_unsplash.place_forget()
    canvas_wallpaper_more_wallhaven.place_forget()
    canvas_wallpaper_more_fengjing.place_forget()
    canvas_wallpaper_more_erciyuan.place_forget()
    canvas_wallpaper_more_360.place(x=640, y=205,width=1280,height=395,anchor="n")
    tid=67 
    # print(123456)
    # 精选 tid=67
    # 风景 tid=1
    # 宠物 tid=2
    # 动漫 tid=92
    # 插画 tid=62
    # 游戏 tid=109
    # 风格 tid=6
    # 科幻 tid=4
    # 美女 tid=70
    # 色系 tid=9
    # 汽车 tid=5
    # 影视 tid=86
    def wallpaper_360_get(ch):
        global tid

        match ch:
            case 0:
                tid=67
            case 1:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=1&page={pages.get()}&uid=0"
                tid=1
            case 2:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=2&page={pages.get()}&uid=0"
                tid=2
            case 3:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=92&page={pages.get()}&uid=0"
                tid=92
            case 4:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=62&page={pages.get()}&uid=0"
                tid=62
            case 5:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=109&page={pages.get()}&uid=0"
                tid=109
            case 6:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=6&page={pages.get()}&uid=0"
                tid=6
            case 7:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=4&page={pages.get()}&uid=0"
                tid=4
            case 8:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=70&page={pages.get()}&uid=0"
                tid=70
            case 9:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=9&page={pages.get()}&uid=0"
                tid=9
            case 10:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=5&page={pages.get()}&uid=0"
                tid=5
            case 11:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=86&page={pages.get()}&uid=0"
                tid=86
            case _:
                # data_url=f"https://mini.browser.360.cn/newtab/imgsx?tid=67&page={pages.get()}&uid=0"
                tid=67
        # print(ch,tid)
    def download_306_wallpaper():
        global wallpaper_360_path_list,tid
        canvas_wallpaper.place_forget()
        canvas_wallpaper_more_360.place_forget()
        canvas_wallpaper_more_360_dowload.place(x=0, y=0,width=1280,height=720,anchor="nw")
        canvas_wallpaper_more_360_dowload.delete("all")
        def back_to_360():
            canvas_wallpaper.place(width=1280, height=720, x=640, y=360, anchor="center")
            canvas_wallpaper_more_360.place(x=640, y=205,width=1280,height=395,anchor="n")
            canvas_wallpaper_more_360_dowload.place_forget()
            canvas_wallpaper_more_360_dowload.delete("all")
        tkt.Text(canvas_wallpaper_more_360_dowload, (100, 100), text="正在初步获取数据...", fontsize=50, anchor="nw")
        if pages.get().isdigit() is not True or int(pages.get()) < 1:
            canvas_wallpaper_more_360_dowload.delete("all")
            tkt.Text(canvas_wallpaper_more_360_dowload, (100, 100), text="错误", fontsize=50, anchor="nw")
            tkt.Text(canvas_wallpaper_more_360_dowload, (100, 180), text="页码必须为正整数数字！", fontsize=30, anchor="nw")
            # tkt.dialogs.TkMessage("页码必须为整数数字！", title="错误", icon="error")
            tkt.Button(canvas_wallpaper_more_360_dowload, (1150, 620), text="返回", command=back_to_360)
            # ch_360.set(0)
            return
        
        # if int(pages.get()) < 1:
        #     canvas_wallpaper_more_360_dowload.delete("all")
        #     tkt.Text(canvas_wallpaper_more_360_dowload, (100, 100), text="错误", fontsize=50, anchor="nw")
        #     tkt.Text(canvas_wallpaper_more_360_dowload, (100, 180), text="页码必须为大于等于1的整数数字！", fontsize=30, anchor="nw")
        #     # tkt.dialogs.TkMessage("页码必须为大于等于1的整数数字！", title="错误", icon="error")
        #     tkt.Button(canvas_wallpaper_more_360_dowload, (1150, 620), text="返回", command=back_to_360)
        #     # ch_360.set(0)
        #     return
        # global api_url
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
        }
        reponse = requests.get(f"https://mini.browser.360.cn/newtab/imgsx?tid={tid}&page={pages.get()}&uid=0", headers=headers)
        # print(tid)
        # print(reponse.text)

        if reponse.status_code == 200:
            json_data = reponse.json()

            if json_data["data"]["total_page"] < int(pages.get()):
                canvas_wallpaper_more_360_dowload.delete("all")
                tkt.Text(canvas_wallpaper_more_360_dowload, (100, 100), text="错误", fontsize=50, anchor="nw")
                tkt.Text(canvas_wallpaper_more_360_dowload, (100, 180), text="页码超出范围", fontsize=30, anchor="nw")
                tkt.Text(canvas_wallpaper_more_360_dowload, (100, 220), text=f"请求页码:{pages.get()} | 最大页码:{json_data['data']['total_page']}", fontsize=25, anchor="nw")
                # tkt.dialogs.TkMessage("页码超出范围！", title="错误", icon="error")
                tkt.Button(canvas_wallpaper_more_360_dowload, (1150, 620), text="返回", command=back_to_360)
                # ch_360.set(0)
                return
            else:
                canvas_wallpaper_more_360_dowload.delete("all")
                tkt.Text(canvas_wallpaper_more_360_dowload, (100, 100), text="详细数据获取成功", fontsize=50, anchor="nw")
                tkt.Text(canvas_wallpaper_more_360_dowload, (100, 180), text=f"请求页码:{pages.get()} | 最大页码:{json_data['data']['total_page']}", fontsize=25, anchor="nw")
                tkt.Text(canvas_wallpaper_more_360_dowload, (100, 220), text=f"本页共{len(json_data['data']['list'])}张图片", fontsize=25, anchor="nw")
                tkt.Text(canvas_wallpaper_more_360_dowload, (100, 260), text=f"正在下载图片...", fontsize=25, anchor="nw")
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
                }
                file_name_prefix = f"360_{time.strftime('%Y%m%d %H%M%S')}"
                completed_files = 0
                total_files = len(json_data['data']['list'])
                wallpaper_360_path_list=[]
                # print(list(range(total_files + 1)))
                logging.info(f"开始下载 {total_files} 个文件")
                def update_progress():
                    nonlocal completed_files
                    # 增加已完成文件数量
                    completed_files += 1
                    
                    # 计算总进度
                    progress = completed_files / total_files
                    logging.info(f"已完成 {completed_files} / {total_files}，进度 {progress:.2%}")
                    # print(progress)
                    # 更新进度条
                    pb1.set(progress)
                    def change_img(img_index):
                        nonlocal now_show_img
                        img_show_360.set(resize_image(wallpaper_360_path_list[img_index],270))
                        now_show_img=wallpaper_360_path_list[img_index]
                    if progress >= 1:
                        canvas_wallpaper_more_360_dowload.delete("all")
                        tkt.Text(canvas_wallpaper_more_360_dowload, (100, 50), text="下载完成", fontsize=50, anchor="nw")
                        tkt.Text(canvas_wallpaper_more_360_dowload, (100, 130), text=f"请求页码:{pages.get()} | 最大页码:{json_data['data']['total_page']}", fontsize=25, anchor="nw")
                        tkt.Text(canvas_wallpaper_more_360_dowload, (100, 170), text=f"本页共{total_files}张图片", fontsize=25, anchor="nw")
                        tkt.SegmentedButton(canvas_wallpaper_more_360_dowload,[100, 210],texts=list(range(1,total_files + 1)),command=lambda x: change_img(x),default=0)
                        img_show_360=tkt.Image(canvas_wallpaper_more_360_dowload, (100, 300), image=resize_image(wallpaper_360_path_list[0], 270), anchor="nw")
                        now_show_img=wallpaper_360_path_list[0]
                        def save_as():
                            file_path = filedialog.asksaveasfilename(title="保存壁纸", filetypes=[("图片文件", os.path.splitext(now_show_img)[1])])
                            if file_path:
                                shutil.copyfile(now_show_img, file_path)
                                os.system(f"explorer.exe /select,\"{file_path.replace("/","\\")}\"")

                                notification.notify(
                                    title='壁纸保存成功',
                                    message=f'壁纸文件已保存至{file_path}\n文件名：{os.path.basename(file_path)}',
                                    app_icon="./assets/icon/icon.ico",
                                    timeout=3,
                                )
                        def download():
                            shutil.copyfile(now_show_img, f"{cog["download_path"]}\\{os.path.basename(now_show_img)}")
                            os.system(f"explorer.exe /select,\"{cog["download_path"]}\\{os.path.basename(now_show_img)}\"")
                            notification.notify(
                                title='壁纸下载完成',
                                message=f'壁纸文件已保存至{cog["download_path"]}\n文件名：{os.path.basename(now_show_img)}',
                                app_icon="./assets/icon/icon.ico",
                                timeout=3,
                            )
                        def copy_wallpaper():

                            copy_image_to_clipboard(now_show_img)
                            notification.notify(
                                title='壁纸复制成功',
                                message='壁纸文件已复制到剪贴板啦~',  
                                app_icon="./assets/icon/icon.ico",
                                timeout=3,
                            )
                        def _set_wallpaper():
                            copy_and_set_wallpaper(now_show_img)

                            notification.notify(
                                title='壁纸设置完成',
                                message=f'壁纸文件位于：C:\\xiaoshu_wallpaper\\\n文件名：{os.path.basename(now_show_img)}\n请勿删除！',
                                app_icon="./assets/icon/icon.ico",
                                timeout=3,
                            )
                        def go_back_wallpaper():
                            logging.info("从360壁纸返回壁纸选择页面")
                            
                            if cog["clear_cache_when_360_back"]:
                                logging.info("需要强制清理缓存")
                                clear_folder("./temp", os.path.basename(fn))
                            canvas_wallpaper_more_360_dowload.place_forget()
                            canvas_wallpaper_more_360_dowload.delete("all")
                            wallpaper()
                        ImageFile.LOAD_TRUNCATED_IMAGES = True

                        # tkt.Text(canvas_wallpaper_more_360_dowload, (80, 50), text="壁纸详情", fontsize=50,anchor="nw")
                        back_wallpaper_detail = tkt.Canvas(canvas_wallpaper_more_360_dowload, zoom_item=True, keep_ratio="min", free_anchor=True)
                        back_wallpaper_detail.place(x=50, y=670,width=40,height=40,anchor="center")
                        tkt.Text(back_wallpaper_detail, (0, 0), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
                        back_wallpaper_detail.bind("<Button-1>", lambda event: go_back_wallpaper())
                        
                        set_w_bing_icon = tkt.Canvas(canvas_wallpaper_more_360_dowload, zoom_item=True, keep_ratio="min", free_anchor=True)
                        set_w_bing_icon.place(x=1230, y=670,width=40,height=50,anchor="center")
                        tkt.Text(set_w_bing_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
                        set_w_bing_icon.bind("<Button-1>", lambda event: _set_wallpaper())
                        tkt.Text(canvas_wallpaper_more_360_dowload,(1230, 705),text="设为壁纸",fontsize=15,anchor="center")
                        ll_icon = tkt.Canvas(canvas_wallpaper_more_360_dowload, zoom_item=True, keep_ratio="min", free_anchor=True)
                        ll_icon.place(x=1150, y=670,width=40,height=50,anchor="center")
                        tkt.Text(ll_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
                        ll_icon.bind("<Button-1>", lambda event: save_as())
                        tkt.Text(canvas_wallpaper_more_360_dowload,(1150, 705),text="另存为",fontsize=15,anchor="center")
                        dd_icon = tkt.Canvas(canvas_wallpaper_more_360_dowload, zoom_item=True, keep_ratio="min", free_anchor=True)
                        dd_icon.place(x=1070, y=670,width=40,height=50,anchor="center")
                        tkt.Text(dd_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
                        dd_icon.bind("<Button-1>", lambda event: download())
                        tkt.Text(canvas_wallpaper_more_360_dowload,(1070, 705),text="下载",fontsize=15,anchor="center")
                        copy_w_bing_icon = tkt.Canvas(canvas_wallpaper_more_360_dowload, zoom_item=True, keep_ratio="min", free_anchor=True)
                        copy_w_bing_icon.place(x=990, y=670,width=40,height=50,anchor="center")
                        tkt.Text(copy_w_bing_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
                        copy_w_bing_icon.bind("<Button-1>", lambda event: copy_wallpaper())
                        tkt.Text(canvas_wallpaper_more_360_dowload,(990, 705),text="复制",fontsize=15,anchor="center")   

                
                def long_running_task1():
                    global wallpaper_360_path_list
                    try:
                        for i in range(len(json_data['data']['list'])):
                            url = json_data['data']['list'][i]["img"]


                            headers = {
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
                            }

                            s = requests.Session()
                            s.headers.update(headers)

                            for attempt in range(3):
                                resp = s.get(url, stream=True)
                                if resp.status_code == 200:
                                    break
                                elif resp.status_code == 521:
                                    logging.warning(f"第 {attempt + 1} 次尝试下载失败，状态码：{resp.status_code}")
                                    time.sleep(1)  # 等待一段时间后重试
                                else:
                                    raise Exception(f"下载失败，状态码：{resp.status_code}")

                            if resp.status_code != 200:
                                raise Exception(f"下载失败，状态码：{resp.status_code}")

                            content_type = resp.headers.get('Content-Type')
                            guessed_type = mimetypes.guess_extension(content_type)
                            if not guessed_type:
                                guessed_type = ".webp"  # 默认文件扩展名

                            filename = f"./temp/{file_name_prefix}_{i}{guessed_type}"
                            wallpaper_360_path_list.append(filename)

                            # 确保临时目录存在
                            os.makedirs(os.path.dirname(filename), exist_ok=True)

                            logging.info(f"开始下载 {filename}")

                            # total_size = int(resp.headers.get('content-length', 0))
                            downloaded_size = 0
                            chunk_size = 512

                            with open(filename, "wb") as f:
                                for chunk in resp.iter_content(chunk_size=chunk_size):
                                    if chunk:
                                        f.write(chunk)
                                        downloaded_size += len(chunk)
                                        
                                        root.update_idletasks()

                            logging.info("下载完成！")
                            update_progress()
                            root.update_idletasks()  # 刷新界面
                            # canvas_download.place_forget()
                            # wallpaper_detail()

                    except Exception as e:
                        logging.error(f"下载失败: {e}")
                        tkt.dialogs.TkMessage("下载失败，详细错误信息请查看日志", title="错误", icon="error")
                        # canvas_download.place_forget()
                        canvas_wallpaper_more_360_dowload.place_forget()
                        canvas_wallpaper_more_360_dowload.delete("all")
                        wallpaper()  # 返回壁纸页面

                
                root.after(1000, long_running_task1)


                # global pb1
                pb1 = tkt.ProgressBar(canvas_wallpaper_more_360_dowload, (100, 330), (600, 8))

                # pb1.set(1)
    tkt.SegmentedButton(canvas_wallpaper_more_360, (100, 25),texts= ["精选","风景","动物","动漫","插画","游戏","风格","科幻","美女","色系","汽车","影视"], command=wallpaper_360_get, default=0)
    tkt.Text(canvas_wallpaper_more_360, (100, 100), text="输入页码：", fontsize=20, anchor="nw")
    pages=tkt.InputBox(canvas_wallpaper_more_360, (100, 130))
    pages.set("1")
    # tkt.Text(canvas_wallpaper_more_360, (100, 160), text="输入项数：", fontsize=20, anchor="nw")
    tkt.Button(canvas_wallpaper_more_360, (1150, 350), text="获取数据", command=lambda: download_306_wallpaper())

    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
    # }
    # response = requests.get(data_url, headers=headers)

    # if response.status_code == 200:
    #     json_data = response.json()

    # else:
    #     logging.error(f"请求失败，状态码: {response.status_code}")
    #     tkt.dialogs.TkMessage(f"请求失败，状态码: {response.status_code}", title="错误", icon="error")
    
def wallpaper_choose(ch):
    (wallpaper_wallhaven,wallpaper_风景,wallpaper_二次元,wallpaper_360)[ch]()
    

wallpaper_choose_button=tkt.SegmentedButton(canvas_wallpaper, (100, 150),texts= ["Wallhaven精选", "风景", "二次元", "360壁纸"], command=wallpaper_choose, default=0)


### ✨ Bing壁纸详细信息
canvas_detail = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
canvas_download = tkt.Canvas(root, zoom_item=True, keep_ratio="min", free_anchor=True)
# canvas_detail.place(width=1280, height=720, x=640, y=360, anchor="center")
def bing_detail():
    canvas_detail.delete("all")
    canvas_download.delete("all")
    canvas_download.place_forget()
    global huazhiv
    def huazhi_re1(*args):
        global huazhiv
        huazhiv=0
        # print(1080)
    def huazhi_re2(*args):
        global huazhiv
        huazhiv=1
        # print("UHD")
    def dd(*args):
        def long_running_task1():
            try:
                # global bing_data_name
                url=bing_data[0]['url']
                if(huazhiv):
                    url=bing_data[0]['url'].replace('1920x1080', 'UHD')
                # print(getBingImg())
                root.update() 
                # 自定义用户代理
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
                }

                # 发送HEAD请求以获取文件大小
                response = requests.head(url, headers=headers)
                root.update() 
                file_size = int(response.headers.get('Content-Length', 0))
                root.update() 
                # 自动识别文件名和扩展名
                # filename = url.split('/')[-1] or 'downloaded_file'
                filename = f"{time.strftime('Bing_%Y-%m-%d.jpg', time.localtime())}"
                root.update() 
                if not filename:
                    filename = 'downloaded_file'
                root.update() 
                # 设定分段大小（例如：1MB）
                chunk_size = 1024 * 1024  # 1MB
                num_chunks = (file_size // chunk_size) + 1
                logging.info("开始下载")
                logging.info(f"开始下载 {filename}，总大小: {file_size} bytes，分为 {num_chunks} 段。")

                with open(f"{cog["download_path"]}\\{filename}", 'wb') as file:
                    for i in range(num_chunks):
                        root.update()
                        start = i * chunk_size
                        end = min(start + chunk_size - 1, file_size - 1)

                        # 设置Range请求头
                        range_header = {'Range': f'bytes={start}-{end}'}
                        chunk_response = requests.get(url, headers={**headers, **range_header}, stream=True)
                        root.update()
                        if chunk_response.status_code in (200, 206):  # 206表示部分内容
                            file.write(chunk_response.content)
                            root.update()
                            logging.info(f"下载段 {i + 1}/{num_chunks} 完成，大小: {len(chunk_response.content)} bytes")
                        else:
                            logging.info(f"下载失败，状态码: {chunk_response.status_code}")
                            root.update()
                            tkt.dialogs.TkMessage(f"下载失败，状态码: {chunk_response.status_code}", title="错误", icon="error")
                            os._exit(0)
                # print(bing_data_name)
                
                logging.info("下载完成！")
                os.system(f"explorer.exe /select,\"{cog["download_path"]}\\{filename}\"")
                # tkt.dialogs.TkMessage(f"下载完成，文件位于：{cog['download_path']}\n文件名：{filename}", title="提示", icon="info")
                notification.notify(
                    title='下载完成',
                    message=f'文件位于：{cog['download_path']}\n文件名：{filename}',
                    app_icon="./assets/icon/icon.ico",
                    timeout=3,
                )
                more_bing()
            except Exception as e:
                tkt.dialogs.TkMessage(f"下载失败，详细错误信息请查看日志", title="错误", icon="error")
                logging.error(f"下载失败{e}")

                more_bing()

            # 任务完成后更新窗口
            # label.config(text="任务已完成!")

        def start_task1(*args):

            # label.config(text="任务正在进行中...")
            # 利用after方法调用长时间运行的任务
            root.after(100, long_running_task1)
        canvas_detail.place_forget()
        canvas_download.place(width=1280, height=720, x=640, y=360, anchor="center")    
        tkt.Text(canvas_download, (100, 100), text="正在下载...", fontsize=50, anchor="nw")
        pb1 = tkt.ProgressBar(canvas_download, (420, 260), (380, 8))
        tkt.animation.Animation(2000, tkt.animation.smooth, callback=pb1.set,
                            fps=60, repeat=math.inf).start(delay=1500)
        start_task1()
    def ll(*args):  
        def long_running_task1():
            try:
                # global bing_data_name
                url=bing_data[0]['url']
                if(huazhiv):
                    url=bing_data[0]['url'].replace('1920x1080', 'UHD')
                # print(getBingImg())
                root.update() 
                # 自定义用户代理
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
                }

                # 发送HEAD请求以获取文件大小
                response = requests.head(url, headers=headers)
                root.update() 
                file_size = int(response.headers.get('Content-Length', 0))
                root.update() 
                # 自动识别文件名和扩展名
                # filename = url.split('/')[-1] or 'downloaded_file'
                filename = filedialog.asksaveasfilename(title='Bing-另存为', filetypes=[('JPEG文件', '.jpg')], defaultextension=".jpg")
                root.update() 
                if not filename:
                    
                    while(filename is not True):
                        filename = filedialog.asksaveasfilename(title='Bing-另存为', filetypes=[('JPEG文件', '.jpg')], defaultextension=".jpg")
                root.update() 
                # 设定分段大小（例如：1MB）
                chunk_size = 1024 * 1024  # 1MB
                num_chunks = (file_size // chunk_size) + 1
                logging.info("开始下载")
                logging.info(f"开始下载 {filename}，总大小: {file_size} bytes，分为 {num_chunks} 段。")
                # fnn=filedialog.askdirectory()
                with open(f"{filename}", 'wb') as file:
                    for i in range(num_chunks):
                        root.update()
                        start = i * chunk_size
                        end = min(start + chunk_size - 1, file_size - 1)

                        # 设置Range请求头
                        range_header = {'Range': f'bytes={start}-{end}'}
                        chunk_response = requests.get(url, headers={**headers, **range_header}, stream=True)
                        root.update()
                        if chunk_response.status_code in (200, 206):  # 206表示部分内容
                            file.write(chunk_response.content)
                            root.update()
                            logging.info(f"下载段 {i + 1}/{num_chunks} 完成，大小: {len(chunk_response.content)} bytes")
                        else:
                            logging.info(f"下载失败，状态码: {chunk_response.status_code}")
                            root.update()
                            tkt.dialogs.TkMessage(f"下载失败，状态码: {chunk_response.status_code}", title="错误", icon="error")
                            os._exit(0)
                # print(bing_data_name)
                
                logging.info("下载完成！")
                os.system(f"explorer.exe /select,\"{filename.replace("/","\\")}\"")
                # tkt.dialogs.TkMessage(f"下载完成，文件位于：{cog['download_path']}\n文件名：{filename}", title="提示", icon="info")
                notification.notify(
                    title='下载完成',
                    message=f'文件位于：{os.path.dirname(os.path.abspath(filename))}\n文件名：{os.path.split(filename)[1]}',
                    app_icon="./assets/icon/icon.ico",
                    timeout=3,
                )
                more_bing()
            except Exception as e:
                tkt.dialogs.TkMessage(f"下载失败，详细错误信息请查看日志", title="错误", icon="error")
                logging.error(f"下载失败{e}")

                more_bing()

            # 任务完成后更新窗口
            # label.config(text="任务已完成!")

        def start_task1(*args):

            # label.config(text="任务正在进行中...")
            # 利用after方法调用长时间运行的任务
            root.after(100, long_running_task1)
        canvas_detail.place_forget()
        canvas_download.place(width=1280, height=720, x=640, y=360, anchor="center")    
        tkt.Text(canvas_download, (100, 100), text="正在下载...", fontsize=50, anchor="nw")
        pb1 = tkt.ProgressBar(canvas_download, (420, 260), (380, 8))
        tkt.animation.Animation(2000, tkt.animation.smooth, callback=pb1.set,
                            fps=60, repeat=math.inf).start(delay=1500)
        start_task1()
    def set_w_bing(*args):
        def long_running_task1():
            try:
                # global bing_data_name
                url=bing_data[0]['url']
                if(huazhiv):
                    url=bing_data[0]['url'].replace('1920x1080', 'UHD')
                # print(getBingImg())
                root.update() 
                # 自定义用户代理
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
                }

                # 发送HEAD请求以获取文件大小
                response = requests.head(url, headers=headers)
                root.update() 
                file_size = int(response.headers.get('Content-Length', 0))
                root.update() 
                # 自动识别文件名和扩展名
                # filename = url.split('/')[-1] or 'downloaded_file'
                # filename = f"{time.strftime('Bing_%Y-%m-%d.jpg', time.localtime())}"
                root.update() 
                # if not filename:
                    # filename = 'downloaded_file'
                root.update() 
                # 设定分段大小（例如：1MB）
                chunk_size = 1024 * 1024  # 1MB
                num_chunks = (file_size // chunk_size) + 1
                logging.info("开始下载")
                logging.info(f"开始下载 bk.jpg，总大小: {file_size} bytes，分为 {num_chunks} 段。")

                with open("C:/xiaoshu_wallpaper/bk.jpg", 'wb') as file:
                    for i in range(num_chunks):
                        root.update()
                        start = i * chunk_size
                        end = min(start + chunk_size - 1, file_size - 1)

                        # 设置Range请求头
                        range_header = {'Range': f'bytes={start}-{end}'}
                        chunk_response = requests.get(url, headers={**headers, **range_header}, stream=True)
                        root.update()
                        if chunk_response.status_code in (200, 206):  # 206表示部分内容
                            file.write(chunk_response.content)
                            root.update()
                            logging.info(f"下载段 {i + 1}/{num_chunks} 完成，大小: {len(chunk_response.content)} bytes")
                        else:
                            logging.info(f"下载失败，状态码: {chunk_response.status_code}")
                            root.update()
                            tkt.dialogs.TkMessage(f"下载失败，状态码: {chunk_response.status_code}", title="错误", icon="error")
                            os._exit(0)
                # print(bing_data_name)
                
                logging.info("下载完成！")
                # os.system(f"explorer.exe /select,\"{cog["download_path"]}\\{filename}\"")
                # tkt.dialogs.TkMessage(f"下载完成，文件位于：{cog['download_path']}\n文件名：{filename}", title="提示", icon="info")
                set_wallpaper("C:/xiaoshu_wallpaper/bk.jpg")
                notification.notify(
                    title='壁纸设置完成',
                    message=f'壁纸文件位于：C:/xiaoshu_wallpaper\n文件名：bk.jpg\n请勿删除！',
                    app_icon="./assets/icon/icon.ico",
                    timeout=3,
                )
                more_bing()
            except Exception as e:
                tkt.dialogs.TkMessage(f"下载失败，详细错误信息请查看日志", title="错误", icon="error")
                logging.error(f"下载失败{e}")

                more_bing()

            # 任务完成后更新窗口
            # label.config(text="任务已完成!")

        def start_task1(*args):

            # label.config(text="任务正在进行中...")
            # 利用after方法调用长时间运行的任务
            root.after(100, long_running_task1)
        canvas_detail.place_forget()
        canvas_download.place(width=1280, height=720, x=640, y=360, anchor="center")    
        tkt.Text(canvas_download, (100, 100), text="正在下载...", fontsize=50, anchor="nw")
        pb1 = tkt.ProgressBar(canvas_download, (420, 260), (380, 8))
        tkt.animation.Animation(2000, tkt.animation.smooth, callback=pb1.set,
                            fps=60, repeat=math.inf).start(delay=1500)
        start_task1()
    def copy_w_bing(*args):
        def long_running_task1():
            try:
                # global bing_data_name
                url=bing_data[0]['url']
                if(huazhiv):
                    url=bing_data[0]['url'].replace('1920x1080', 'UHD')
                # print(getBingImg())
                root.update() 
                # 自定义用户代理
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0'
                }

                # 发送HEAD请求以获取文件大小
                response = requests.head(url, headers=headers)
                root.update() 
                file_size = int(response.headers.get('Content-Length', 0))
                root.update() 
                # 自动识别文件名和扩展名
                # filename = url.split('/')[-1] or 'downloaded_file'
                root.update() 

                root.update() 
                # 设定分段大小（例如：1MB）
                chunk_size = 1024 * 1024  # 1MB
                num_chunks = (file_size // chunk_size) + 1
                logging.info("开始下载")
                logging.info(f"开始下载 {TEMP}\\copy.jpg，总大小: {file_size} bytes，分为 {num_chunks} 段。")

                with open(f"{TEMP}\\copy.jpg", 'wb') as file:
                    for i in range(num_chunks):
                        root.update()
                        start = i * chunk_size
                        end = min(start + chunk_size - 1, file_size - 1)

                        # 设置Range请求头
                        range_header = {'Range': f'bytes={start}-{end}'}
                        chunk_response = requests.get(url, headers={**headers, **range_header}, stream=True)
                        root.update()
                        if chunk_response.status_code in (200, 206):  # 206表示部分内容
                            file.write(chunk_response.content)
                            root.update()
                            logging.info(f"下载段 {i + 1}/{num_chunks} 完成，大小: {len(chunk_response.content)} bytes")
                        else:
                            logging.info(f"下载失败，状态码: {chunk_response.status_code}")
                            root.update()
                            tkt.dialogs.TkMessage(f"下载失败，状态码: {chunk_response.status_code}", title="错误", icon="error")
                            os._exit(0)
                # print(bing_data_name)
                
                logging.info("下载完成！")
                # os.system(f"explorer.exe /select,\"{cog["download_path"]}\\{filename}\"")
                # tkt.dialogs.TkMessage(f"下载完成，文件位于：{cog['download_path']}\n文件名：{filename}", title="提示", icon="info")
                copy_image_to_clipboard(f"{TEMP}\\copy.jpg")
                notification.notify(
                    title='已复制',
                    message='已经复制成功啦 ~ ',
                    app_icon="./assets/icon/icon.ico",
                    timeout=3,
                )
                more_bing()
            except Exception as e:
                tkt.dialogs.TkMessage(f"下载失败，详细错误信息请查看日志", title="错误", icon="error")
                logging.error(f"下载失败{e}")

                more_bing()

            # 任务完成后更新窗口
            # label.config(text="任务已完成!")

        def start_task1(*args):

            # label.config(text="任务正在进行中...")
            # 利用after方法调用长时间运行的任务
            root.after(100, long_running_task1)
        canvas_detail.place_forget()
        canvas_download.place(width=1280, height=720, x=640, y=360, anchor="center")   
        tkt.Text(canvas_download, (100, 100), text="正在获取图片数据...", fontsize=50, anchor="nw")
        pb1 = tkt.ProgressBar(canvas_download, (420, 260), (380, 8))
        tkt.animation.Animation(2000, tkt.animation.smooth, callback=pb1.set,
                            fps=60, repeat=math.inf).start(delay=1500)
        start_task1()
    tkt.Text(canvas_detail,(50, 70),text="详细信息",fontsize=40,anchor="w")
    tkt.Text(canvas_detail,(50, 110),text="今日Bing",fontsize=25,anchor="w")
    tkt.Text(canvas_detail,(50, 140),text=f"{bing_data[0]['date']}",fontsize=18,anchor="w")
    tkt.Text(canvas_detail,(50, 170),text=f"标题：{b_title}",fontsize=25,anchor="w")
    canvas_copyright=tkt.Canvas(canvas_detail,zoom_item=True,keep_ratio=False)
    canvas_copyright.place(x=40,y=190,width=1200,height=25,anchor="nw")
    tkt.Text(canvas_copyright,(10,10),text=f"版权：{b_copyright}",fontsize=25,anchor="w",underline=True)
    canvas_copyright.bind("<Button-1>", lambda event: webbrowser.open(bing_data[0]['copyrightlink']))
    # bq=canvas_detail.create_text(50,200,text=f"版权：{b_copyright}",font=25,anchor="w")
    # canvas_detail.tag_bind(bq, "<Button-1>", lambda event: webbrowser.open(bing_data[0]['copyrightlink']))
    tkt.Text(canvas_detail,(50, 230),text=f"预览：",fontsize=25,anchor="w")
    # canvas_detail.create_text(50,230,text=f"预览：",font=25,anchor="w")
    original_image = Image.open(fn)
    # 获取原始图片的宽度和高度
    original_width, original_height = original_image.size
    # 如果只指定了高度，按比例计算宽度
    aspect_ratio = original_width / original_height
    new_height = 200
    new_width = int(200 * aspect_ratio)
    # 等比缩放图片
    resized_image = original_image.resize((new_width, new_height), Image.LANCZOS)
    tkt.Image(canvas_detail, (300, 320), image=tkt.PhotoImage(resized_image),anchor="center")
    tkt.Text(canvas_detail,(50, 390),text=f"",fontsize=40,anchor="w")
    tkt.Text(canvas_detail,(80, 440),text=f"",fontsize=23,anchor="nw")._texts[0].styles["normal"] = {"fill": "red"}
    tkt.Text(canvas_detail,(110, 440),text=f"版权警告：图片仅供作为壁纸使用，禁止用于其他用途",fontsize=23,anchor="nw")
    # canvas_detail.create_text(90, 440, text="版权警告：图片仅供作为壁纸使用，禁止用于其他用途", font=23,anchor="nw")
    # canvas_detail.create_image(130, 220, anchor="nw", image=tkt.PhotoImage(resized_image)) 
    huazhiv=0
    tkt.Text(canvas_detail,(980, 615),text="画质：",fontsize=18,anchor="center")
    # canvas_detail.create_text(980, 615, text="画质：", font=18)
    def ch_return(ch1):
        (huazhi_re1, huazhi_re2)[ch1]()
    tkt.SegmentedButton(canvas_detail, (1000, 585), texts=(
        "1080P", "HUD(原图)"), default=0, command=ch_return)
    set_w_bing_icon = tkt.Canvas(canvas_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    set_w_bing_icon.place(x=1230, y=670,width=40,height=50,anchor="center")
    tkt.Text(set_w_bing_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    set_w_bing_icon.bind("<Button-1>", lambda event: set_w_bing())
    # b1=canvas_detail.create_image(1230, 670, image=tkt.PhotoImage(file=r"D:\Users\张秫\onedrive\OneDrive - 小树科技\图片\icon\set_w.png"))
    tkt.Text(canvas_detail,(1230, 705),text="设为壁纸",fontsize=15,anchor="center")
    # canvas_detail.create_text(1230, 705, text="设为壁纸", font=15)
    # canvas_detail.tag_bind(b1, "<Button-1>", lambda event: set_w_bing())
    ll_icon = tkt.Canvas(canvas_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    ll_icon.place(x=1150, y=670,width=40,height=50,anchor="center")
    tkt.Text(ll_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    ll_icon.bind("<Button-1>", lambda event: ll())
    # b2=canvas_detail.create_image(1150, 670, image=tkt.PhotoImage(file=r"D:\Users\张秫\onedrive\OneDrive - 小树科技\图片\icon\dto.png"))
    tkt.Text(canvas_detail,(1150, 705),text="另存为",fontsize=15,anchor="center")
    # canvas_detail.create_text(1150, 705, text="另存为", font=15)
    # canvas_detail.tag_bind(b2, "<Button-1>", lambda event: ll())
    dd_icon = tkt.Canvas(canvas_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    dd_icon.place(x=1070, y=670,width=40,height=50,anchor="center")
    tkt.Text(dd_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    dd_icon.bind("<Button-1>", lambda event: dd())
    # b3=canvas_detail.create_image(1070, 670, image=tkt.PhotoImage(file=r"D:\Users\张秫\onedrive\OneDrive - 小树科技\图片\icon\dp.png"))
    tkt.Text(canvas_detail,(1070, 705),text="下载",fontsize=15,anchor="center")
    # canvas_detail.create_text(1070, 705, text="下载", font=15)
    # canvas_detail.tag_bind(b3, "<Button-1>", lambda event: dd())
    copy_w_bing_icon = tkt.Canvas(canvas_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    copy_w_bing_icon.place(x=990, y=670,width=40,height=50,anchor="center")
    tkt.Text(copy_w_bing_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    copy_w_bing_icon.bind("<Button-1>", lambda event: copy_w_bing())
    # b4=canvas_detail.create_image(990, 670, image=tkt.PhotoImage(file=r"D:\Users\张秫\onedrive\OneDrive - 小树科技\图片\icon\copy.png"))
    tkt.Text(canvas_detail,(990, 705),text="复制",fontsize=15,anchor="center")
    # canvas_detail.create_text(990, 705, text="复制", font=15)
    # canvas_detail.tag_bind(b4, "<Button-1>", lambda event: copy_w_bing())
    test_icon = tkt.Canvas(canvas_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    test_icon.place(x=1280//2, y=670,width=40,height=50,anchor="center")
    tkt.Text(test_icon, (0, 10), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    test_icon.bind("<Button-1>", lambda event: webbrowser.open("https://www.bing.com/hp/api/v1/trivia"))
    # b5=canvas_detail.create_image(1280//2, 670, image=tkt.PhotoImage(file=r"D:\Users\张秫\onedrive\OneDrive - 小树科技\图片\icon\test.png"))
    tkt.Text(canvas_detail,(1280//2, 705),text="参与测验",fontsize=15,anchor="center")
    # canvas_detail.create_text(1280//2, 705, text="参与测验", font=15)
    # canvas_detail.tag_bind(b5, "<Button-1>", lambda event: webbrowser.open("https://www.bing.com/hp/api/v1/trivia"))
    back_detail = tkt.Canvas(canvas_detail, zoom_item=True, keep_ratio="min", free_anchor=True)
    back_detail.place(x=50, y=670,width=40,height=40,anchor="center")
    tkt.Text(back_detail, (0, 0), text="", fontsize=40, family="Segoe Fluent lcons",anchor="nw")
    back_detail.bind("<Button-1>", lambda event: main())

# 

### ✨ 页面切换

def egg():
    # tkt.dialogs.TkMessage(icon="info",title="彩蛋",message="你发现了一个彩蛋！",detail="你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！\n\n你发现了一个彩蛋！")
    canvas_index.delete("all")
    canvas.place_forget()
    canvas_index.pack_forget()
    canvas_egg.place(width=1280, height=720, x=640, y=360, anchor="center")

def wallpaper():
    wallpaper_wallhaven()
    canvas_index.delete("all")
    canvas.place_forget()
    canvas_index.place_forget()
    canvas_wallpaper_detail.place_forget()
    canvas_wallpaper.place(width=1280, height=720, x=640, y=360, anchor="center")
    

def setting():
    canvas_index.delete("all")
    canvas.place_forget()
    canvas_index.place_forget()
    canvas_setting.place(width=1280, height=720, x=640, y=360, anchor="center")

    canvas_setting.update_idletasks()
    canvas_setting._re_place()

def getBingImg():
    try:
        headers={
            'Content-Type':'application/json; charset=utf-8',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36', #不是必须
        }
        response = requests.get(
            "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=7&mkt=zh-CN",
            headers=headers, #请求头
            timeout=3, #设置请求超时时间
        )
        response = json.loads(response.text) #转化为json
        imgList = []
        for item in response['images']:
            imgList.append({
                'copyright':item['copyright'], #版权
                'date':item['enddate'][0:4]+'-'+item['enddate'][4:6]+'-'+item['enddate'][6:], #时间
                'urlbase':'https://cn.bing.com'+item['urlbase'], #原始图片链接
                'url':'https://cn.bing.com'+item['url'], #图片链接
                'title':item['title'], #标题
                'copyrightlink':item['copyrightlink'], #版权链接
            })
        return imgList #返回一个数据数组
    except:
        return False

def clean_filename(filename):
    # 替换无效字符
    return re.sub(r'[<>:"/\\|?*]', '_', filename).removesuffix("&pid=hp")


def about():
    canvas_index.delete("all")
    canvas.place_forget()
    canvas_about.place(width=1280, height=720, x=640, y=360, anchor="center")
    # TODO: 后面记得改
    canvas_about.update_idletasks()
    canvas_about._re_place()

    

def more_bing(*args):
    # tkt.dialogs.TkMessage("当前内容正在重构中，请谨慎进入", title="提示", icon="warning",detail="进入后，你可以点击左下角空白区域返回")
    canvas_index.delete("all")
    canvas.place_forget()
    canvas_index.place_forget()
    bing_detail()
    canvas_detail.place(width=1280, height=720, x=640, y=360, anchor="center")

    canvas_detail.update_idletasks()
    canvas_detail._re_place()
    
def main():
    # global last
    # if is_load_main is not True:
    #     index_window()
    index_window()
    canvas_setting.place_forget()
    canvas_about.place_forget()
    canvas_egg.place_forget()
    canvas.pack_forget()
    canvas_detail.delete("all")
    canvas_detail.place_forget()
    canvas_wallpaper.place_forget()
    canvas_index.place(x=0, y=0, width=1366, height=768)
    # TODO: tkt 3.0rc3时需修改
    canvas_index.update_idletasks()
    canvas_index._re_place()

root.mainloop()