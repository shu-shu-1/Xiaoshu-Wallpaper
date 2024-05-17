# Copyright (c) 2024 by shu-shu-1 3458222@qq.com, All Rights Reserved. 
VER = 5.0
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0"
pa=0
pa1=0
bing_run_past=0
pau=0
pau1=0
wau=0
wau1=0
tau=0
tau1=0
tau2=0
fju=0
fju1=0
import time,os,requests,json,win32api,win32con,ctypes,shutil,sys,threading,pystray,random,schedule
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
print("测试版专用控制台窗口，如有任何报错请联系作者\n请等待窗口显示")

with open('./data/settings.json',encoding="utf-8") as f:
    settings = json.loads(f.read())

def new_folder(ffffffff):
    folder_name = ffffffff

    if os.path.exists(folder_name):
        pass
    else: 
        os.mkdir(folder_name)
if settings["Pictures_save_path"]=="":
    settings["Pictures_save_path"]=os.path.join(os.environ['USERPROFILE'],'Pictures')
Pictures=settings["Pictures_save_path"]
new_folder(r"C:\bing_wallpaper")
new_folder(f"{Pictures}\\收藏")
new_folder(f"{Pictures}\\壁纸")
def get_file_format(url):
    try:
        response = requests.head(url, allow_redirects=True)
        content_type = response.headers.get('Content-Type')
        if content_type:
            return content_type.split('/')[-1]
        else:
            return "Unknown"
    except Exception as e:
        messagebox.showerror("错误", f"无法获取目标格式\n详细错误信息：{e}")
        return None
def set_wallpaper(filelink):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filelink, 0)
    time.sleep(1)
    Hkey = win32api.RegCreateKey(win32con.HKEY_CURRENT_USER, r'Control Panel\Desktop')
    win32api.RegSetValueEx(Hkey, 'WallPaper', 0, win32con.REG_SZ, filelink)
    win32api.RegCloseKey(Hkey)

def clean_mode_data(mode):
    global pau1,pa1,wau1,wau,pa,pau,tau,tau1,tau2,fju,fju1
    if mode=="Bing壁纸源":
        pau1,wau1,wau,pau,tau,tau1,tau2,fju,fju1=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif mode=="Unsplash随机壁纸":
        pa1,wau1,wau,pa,tau,tau1,tau2,fju,fju1=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif mode=="wallhaven壁纸源":
        pa1,pau1,pau,pa,tau,tau1,tau2,fju,fju1=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    elif mode=="风景":
        pa1,pau1,pau,pa,tau,tau1,tau2,wau,wau1=[0, 0, 0, 0, 0, 0, 0, 0, 0]
    else:
        pa1,pa,pau1,pau,wau,wau1,fju,fju1=[0, 0, 0, 0, 0, 0, 0, 0]

def update():
    
    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"即将下载最新版本\n当前版本：{VER} | 最新版本：{web_ver}")
    clear_frame()
    import mechanize
    br = mechanize.Browser()
    br.set_handle_equiv(True)  # 设置是否处理HTML http-equiv标头
    br.set_handle_redirect(True)  # 设置是否处理重定向
    br.set_handle_referer(True)  # 设置是否向每个请求添加referer头
    br.set_handle_robots(False)  # 设置是不遵守robots中的规则
    br.set_handle_gzip(False)  # 处理giz传输编码
    br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
    source_url = update_f_url
    response=br.open(source_url)
    target_url=response.geturl()
    # print(target_url)
    choices.config(state="disabled")
    
    thread_it(up_download,update_f_url,"新版本安装包.exe")
    
    

# -----------------------------------------------------收藏夹轮动
# 设置壁纸的函数

path=f"{Pictures}\\收藏\\"
new_folder(path)


images=[i for i in os.listdir(path)]
# 壁纸更换任务
def change_wallpaper():


    img = random.choice(images)
    set_wallpaper(path+img)
# runnn=0
# 创建和管理壁纸更换线程的类
class WallpaperChanger:
    def __init__(self, interval):
        global runnn,th
        runnn = 0
        self.interval = interval
        th = None


    def job(self):
        if runnn:
            change_wallpaper()

    def scheduler_job(self):
        schedule.every(self.interval).seconds.do(self.job)
        while runnn:
            schedule.run_pending()
            time.sleep(1)

    def start(self):
        global runnn,th
        if not runnn:
            # global runnn
            runnn = 1
            th = threading.Thread(target=self.scheduler_job)
            th.start()
            print("Wallpaper changer started.")

    def stop(self):
        global runnn,th
        if runnn:
            # global runnn
            runnn = 0
            th.join()  # 等待线程结束
            schedule.clear()  # 清除所有计划任务
            print("Wallpaper changer stopped.")
wallpaper_changer = WallpaperChanger(settings['pic_time'])
def start_stop_wallpaper():
    if len(os.listdir(path)) == 0:
        messagebox.showinfo('提示', '收藏夹为空')
        return
    # 这里直接使用wallpaper_changer引用，不依赖self
    if not runnn:
        wallpaper_changer.start()
    else:
        wallpaper_changer.stop()
# -----------------------------------------------------
def is_admin():
    try:
        return 1
        # return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        messagebox.showerror("错误", "获取管理员身份出错")

runn=0

def about():
    try:
        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"壁纸\n版本：{VER} | {update_type}\n作者：小树\n更新时间：2024.5.12\n联系作者：zs3458222@outlook.com")
    except: pass

if is_admin():
    def download(url: str, fname: str):
        # 确保fname中的目录存在，若不存在则创建
        try:
            if not os.path.exists(os.path.dirname(fname)):
                os.makedirs(os.path.dirname(fname), exist_ok=True)
        except: pass
        # 创建会话并设置User-Agent
        s = requests.Session()
        s.headers.update({'User-Agent': UA})
        
        # 开始下载文件
        resp = s.get(url, stream=True)
        with open(fname, "wb") as f:
            for chunk in resp.iter_content(chunk_size=512):
                if chunk:  # 过滤掉保持连接的新块(chunk)
                    f.write(chunk)
    def img_download(url: str, fname: str):

        try:
            if not os.path.exists(os.path.dirname(fname)):
                os.makedirs(os.path.dirname(fname), exist_ok=True)
        except: pass
        s = requests.Session()
        s.headers.update({'User-Agent': UA})
        resp = s.get(url, stream=True)
        with open(fname, "wb") as f:
            for chunk in resp.iter_content(chunk_size=512):
                f.write(chunk)
        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"下载完成\n图片保存至{fname}")
    def wal_download(url: str, fname: str):
        # 确保fname中的目录存在，若不存在则创建
        try:
            if not os.path.exists(os.path.dirname(fname)):
                os.makedirs(os.path.dirname(fname), exist_ok=True)
        except: pass
        s = requests.Session()
        s.headers.update({'User-Agent': UA})
        resp = s.get(url, stream=True)
        with open(fname, "wb") as f:
            for chunk in resp.iter_content(chunk_size=512):
                f.write(chunk)
        set_wallpaper(fname)
        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"设置完成\n壁纸文件保存至{fname}\n请勿删除!")
    def star_download(url: str, fname: str):
        # 确保fname中的目录存在，若不存在则创建
        try:
            if not os.path.exists(os.path.dirname(fname)):
                os.makedirs(os.path.dirname(fname), exist_ok=True)
        except: pass
        s = requests.Session()
        s.headers.update({'User-Agent': UA})
        resp = s.get(url, stream=True)
        with open(fname, "wb") as f:
            for chunk in resp.iter_content(chunk_size=512):
                f.write(chunk)
        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"收藏完成\n壁纸文件保存至{fname}")
    def up_download(url: str, fname: str):
        # 确保fname中的目录存在，若不存在则创建
        try:
            if not os.path.exists(os.path.dirname(fname)):
                os.makedirs(os.path.dirname(fname), exist_ok=True)
        except: pass
        # 创建会话并设置User-Agent
        s = requests.Session()
        s.headers.update({'User-Agent': UA})
        
        # 开始下载文件
        resp = s.get(url, stream=True)
        with open(fname, "wb") as f:
            for chunk in resp.iter_content(chunk_size=512):
                if chunk:  # 过滤掉保持连接的新块(chunk)
                    f.write(chunk)
        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"即将打开更新程序\n当前程序即将退出\n按下确定开始")
        os.startfile(fname)
        os._exit(1)

    def on_quit_clicked(icon):             # 自定义回调函数
        icon.stop()
        os._exit(1)

        # sys.exit()
        


    image = Image.open("./icon/icon.ico")   # 打开 ICO 图像文件并创建一个 Image 对象
    menu = (pystray.MenuItem(text='收藏夹自动轮换开关', action= start_stop_wallpaper), pystray.Menu.SEPARATOR ,pystray.MenuItem(text='关于', action=about), pystray.MenuItem(text='退出', action=on_quit_clicked)) # 创建菜单项元组
    icon = pystray.Icon("name", image, "小树壁纸", menu)            # 创建 PyStray Icon 对象，并传入关键参数

    # 显示图标
    # icon.run_detached()
    threading.Thread(target=icon.run, daemon=True).start()                              # 启动托盘图标目录
# 更新检测-------------------------------------------
    if settings["check_update"]:
        try:
            try:
                update_web_json=json.loads(requests.get("https://mirror.ghproxy.com/https://raw.githubusercontent.com/shu-shu-1/BingWallpaper/main/version.json").text)
            except:
                update_web_json=json.loads(requests.get("https://fastly.jsdelivr.net/gh/shu-shu-1/BingWallpaper@main/version.json").text)
            web_ver=update_web_json[settings["update_channel"]]["ver"]
            update_f_url=update_web_json[settings["update_channel"]]["url"]
            update_note=update_web_json[settings["update_channel"]]["note"]
            if web_ver > VER:
                note=f"""
当前版本：{VER} 最新{settings["update_channel"]}版本：{web_ver}
有新版本！
新版本公告：
{update_note}

Made By 小树
"""
                update_type="非最新版"
                have_update=1
            elif web_ver == VER:
                note=f"""
当前版本：{VER} 渠道：{settings["update_channel"]} 
当前为最新版
Made By 小树
"""                
                have_update=0
                update_type="最新版本"
            else:
                note=f"""
当前版本：{VER} 最新公开{settings["update_channel"]}版本：{web_ver}
当前仍处于测试版，请等待新的正式版
Made By 小树
"""
                have_update=0
                update_type="测试版本"
        except EncodingWarning:
            messagebox.showerror("更新错误","检查更新失败")
            note=f"""
当前版本：{VER} [检查更新失败]
Made By 小树
"""
            have_update=0
            update_type="[检查更新失败]"
    else:
        note=f"""
当前版本：{VER} [检查更新已关闭]
Made By 小树
"""
        have_update=0
        update_type="[检查更新已关闭]"
# -----------------------------------------------------窗口定义
    windows = tk.Tk()
    style = ttk.Style("cosmo")
    windows.geometry("1000x800+374+182")
    windows.title(f"小树壁纸 V{VER} {update_type}")
    windows.iconbitmap("./icon/icon.ico")
    icon_title=ttk.Label(windows, text="小树壁纸 公开测试版", font=("微软雅黑", 30))       
    icon_title.pack(side="top", padx=0, pady=0)
# -----菜单栏
    menubar = ttk.Menu(windows) 
    menubar.add_command(label = "收藏夹自动轮换开关",command=start_stop_wallpaper)
    menubar.add_command(label = "设置",command=lambda: os.system("config.exe"))
    if have_update:
        menubar.add_command(label = "更新",command=lambda: update()) 
    menubar.add_command(label = "关于",command=lambda: about()) 
    menubar.add_command(label='退出',command=lambda: os._exit(1)) 

    windows.config(menu = menubar)
# -----
    ti=ttk.Label(windows, text="请选择壁纸源:")
    ti.pack(side="top")
    var = ttk.StringVar()
    var.set("请选择……")
    choices=ttk.Combobox(windows, textvariable=var, value=('Bing壁纸源', 'Unsplash随机壁纸', 'wallhaven壁纸源(镜像)', '二次元壁纸源(测试)','风景(测试)'))
    choices.pack(side="top", padx=10, pady=10)
    
    choices.bind("<<ComboboxSelected>>", lambda event: select_source())
    option_frame = ttk.Frame(windows)
    option_frame.pack(fill='both', expand=True)
    note_msg=ttk.Label(windows, text=note)
    note_msg.pack(side='top', expand='yes', anchor='sw')
    def clear_frame():
        # 移除当前frame中的所有组件
        for widget in option_frame.winfo_children():
            widget.destroy()

    def thread_it(func, *args):
        '''将函数打包进线程'''
        # 创建
        t = threading.Thread(target=func, args=args)
        # 守护 !!!
        # t.setDaemon(True)
        # 启动
        t.start()
        # 阻塞--卡死界面！
        # t.join()
    def select_source():
        global pa1,resolution_combobox
        clear_frame()
        pa1=0
        if var.get() == "Bing壁纸源":
            clean_mode_data("Bing壁纸源")
            ttk.Separator(option_frame).pack(fill=ttk.X)
            bing_note = ttk.Label(option_frame, text="选择清晰度:")
            bing_note.pack(side="top", padx=10, pady=10)
            var_resolution = tk.StringVar()
            var_resolution.set("请选择……")  # 默认选择1080P
            resolution_choices = ["1080P", "UHD(原图)"]
            resolution_combobox = ttk.Combobox(option_frame, textvariable=var_resolution, values=resolution_choices)
            resolution_combobox.pack()
            resolution_combobox.bind("<<ComboboxSelected>>", lambda e: thread_it(bing_w))
            image_label = ttk.Label(option_frame)
            image_label.pack()

            
            def bing_w():
            
                global pa,dlb,pa1,image_url,UHD_image_url,title,dlb1,dlb2,bing_msg
                if pa:
                    dlb.destroy()
                    dlb1.destroy()
                    dlb2.destroy()
                    pa=0
                
                dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd(iiurl))
                dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1(iiurl))
                dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2(iiurl))
                image_label.config(text="正在获取数据……")
                if pa1 != 1:
                    pa1=1
                    resolution_combobox.config(state="disabled")
                    choices.config(state="disabled")
                    # 切换清晰度
                    choice = var_resolution.get()
                    # 下载图片并显示
                    url_1080p="https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
                    response = requests.get(url_1080p) 
                    data = response.json()
                    image = data["images"][0]
                    image_url = "https://cn.bing.com" + image["url"]
                    title = image["title"]
                    copyright = image["copyright"]
                    quiz = "https://cn.bing.com" + image["quiz"]
                    UHD_image_url='https://cn.bing.com' + image["url"].replace('1920x1080', 'UHD')
                    download(image_url,"temp.png")
                    img = Image.open("temp.png")
                    bing_msg=ttk.Label(option_frame,text=f"今日标题: {title}\n版权: {copyright}")
                    bing_msg.pack()
                    bing_run_past=1
                    img.thumbnail((500, 500))  # Adjust size as needed
                    photo = ImageTk.PhotoImage(img)
                    image_label.config(image=photo)
                    image_label.image = photo  # Keep a reference!
                    resolution_combobox.config(state="normal")
                    choices.config(state="normal")

                def dd(url1):
                    thread_it(img_download, url1, f"{Pictures}\\{title}_{time.strftime('%Y-%m-%d', time.localtime())}.png")
                def dd1(url1):
                    thread_it(wal_download, url1, f"{Pictures}\\壁纸\\{title}_{time.strftime('%Y-%m-%d', time.localtime())}.png")
                def dd2(url1):
                    thread_it(star_download, url1, f"{Pictures}\\收藏\\{title}_{time.strftime('%Y-%m-%d', time.localtime())}.png")
                if var_resolution.get() == "UHD(原图)":
                    iiurl=UHD_image_url
                else:
                    iiurl=image_url
                pa=1
                dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
        elif var.get() == "Unsplash随机壁纸":
            ttk.Separator(option_frame).pack(fill=ttk.X)
            un_note = ttk.Label(option_frame, text="选择清晰度:")
            un_note.pack(side="top", padx=10, pady=10)
            var_resolution = tk.StringVar()
            var_resolution.set("请选择……")  # 默认选择1080P
            resolution_choices = ["1080P", "无限制"]
            resolution_combobox = ttk.Combobox(option_frame, textvariable=var_resolution, values=resolution_choices)
            resolution_combobox.pack()
            resolution_combobox.bind("<<ComboboxSelected>>", lambda e: thread_it(un_w))
            image_label = ttk.Label(option_frame)
            image_label.pack()

            
            def un_w():
                
                global pau,dlb,pau1,image_url,UHD_image_url,title,dlb1,dlb2,bing_run_past
                resolution_combobox.config(state="disabled")
                choices.config(state="disabled")
                clean_mode_data("Unsplash随机壁纸")
                if bing_run_past:
                    bing_msg.destroy()
                    bing_run_past=0
                if pau:
                    dlb.destroy()
                    dlb1.destroy()
                    dlb2.destroy()
                    pau=0
                dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd())
                dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1())
                dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2())
                image_label.config(text="正在获取数据……")
                if pau1 != 1:
                    pau1=1
                    if var_resolution.get() == "无限制":
                        iiurl="https://source.unsplash.com/random/"
                    else:
                        iiurl="https://source.unsplash.com/random/1920x1080"
                    prefix = 'plus'
                    while prefix!='images':
                        import mechanize
                        br = mechanize.Browser()
                        br.set_handle_equiv(True)  # 设置是否处理HTML http-equiv标头
                        br.set_handle_redirect(True)  # 设置是否处理重定向
                        br.set_handle_referer(True)  # 设置是否向每个请求添加referer头
                        br.set_handle_robots(False)  # 设置是不遵守robots中的规则
                        br.set_handle_gzip(False)  # 处理giz传输编码
                        br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
                        source_url = iiurl
                        response=br.open(source_url)
                        target_url=response.geturl()
                        from urllib.parse import urlparse, parse_qs
                        parsed_url = urlparse(target_url)
                        # 提取查询参数
                        query_params = parse_qs(parsed_url.query)
                        # 获取fm参数的值
                        fm_value = query_params.get('fm', [None])[0]

                        if parsed_url.scheme == 'https' and parsed_url.netloc == 'images.unsplash.com':
                            prefix = 'images'
                        elif parsed_url.scheme == 'https' and parsed_url.netloc == 'unsplash.com':
                            prefix = 'plus'
                        else:
                            prefix = None   

                    download(iiurl,f"temp.{fm_value}") 
                    

                    img = Image.open(f"temp.{fm_value}")
                    img.thumbnail((300, 300))  # Adjust size as needed
                    photo = ImageTk.PhotoImage(img)
                    image_label.config(image=photo)
                    image_label.image = photo  # Keep a reference!
                    
                    resolution_combobox.config(state="normal")
                    choices.config(state="normal")

                def dd():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"下载完成\n壁纸文件保存至{Pictures}\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                def dd1():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\壁纸\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    set_wallpaper(f"{Pictures}\\壁纸\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"设置完成\n壁纸文件保存至{Pictures}\\壁纸\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}\n请勿删除!")
                def dd2():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\收藏\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"收藏完成\n壁纸文件保存至{Pictures}\\收藏\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                pau=1
                dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
        elif var.get() == "wallhaven壁纸源(镜像)":
            ttk.Separator(option_frame).pack(fill=ttk.X)
            wn_note = ttk.Label(option_frame, text="选择模式:")
            wn_note.pack(side="top", padx=10, pady=10)
            var_resolution = tk.StringVar()
            var_resolution.set("请选择……")  # 默认选择1080P
            resolution_choices = ["随机", "每日"]
            resolution_combobox = ttk.Combobox(option_frame, textvariable=var_resolution, values=resolution_choices)
            resolution_combobox.pack()
            resolution_combobox.bind("<<ComboboxSelected>>", lambda e: thread_it(wn_w))
            image_label = ttk.Label(option_frame)
            image_label.pack()

            
            def wn_w():
                
                global wau,dlb,wau,image_url,UHD_image_url,title,dlb1,dlb2,bing_run_past,wau1,pa1
                clean_mode_data("wallhaven壁纸源(镜像)")
                if bing_run_past:
                    bing_msg.destroy()
                    bing_run_past=0
                if wau:
                    dlb.destroy()
                    dlb1.destroy()
                    dlb2.destroy()
                    wau=0
                dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd())
                dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1())
                dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2())
                image_label.config(text="正在获取数据……")
                if wau1 != 1:
                    wau1=1
                    resolution_combobox.config(state="disabled")
                    choices.config(state="disabled")
                    if var_resolution.get() == "随机":
                        iiurl="https://api.nguaduot.cn/wallhaven/random"
                    else:
                        iiurl="https://api.nguaduot.cn/wallhaven/today"
                    fm_value=get_file_format(iiurl)
                    download(iiurl,f"temp.{fm_value}") 
                    

                    img = Image.open(f"temp.{fm_value}")
                    img.thumbnail((300, 300))  # Adjust size as needed
                    photo = ImageTk.PhotoImage(img)
                    image_label.config(image=photo)
                    image_label.image = photo  # Keep a reference!
                    resolution_combobox.config(state="normal")
                    choices.config(state="normal")
                    


                def dd():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\wallhaven壁纸源_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"下载完成\n壁纸文件保存至{Pictures}\\wallhaven壁纸源_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                def dd1():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\壁纸\\wallhaven壁纸源_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    set_wallpaper(f"{Pictures}\\壁纸\\wallhaven壁纸源_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"设置完成\n壁纸文件保存至{Pictures}\\壁纸\\wallhaven壁纸源_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}\n请勿删除!")
                def dd2():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\收藏\\wallhaven壁纸源_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"收藏完成\n壁纸文件保存至{Pictures}\\收藏\\wallhaven壁纸源_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                wau=1
                dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
        elif var.get() == "二次元壁纸源(测试)":
            ttk.Separator(option_frame).pack(fill=ttk.X)
            wn_info=ttk.Label(option_frame, text="请注意，\n该功能使用了不稳定的第三方API\n我们不保证该功能的质量和可用性\n如果API失效或返回任何违法内容，请立即提交反馈！")
            wn_info.pack(side="top", padx=10, pady=10)
            wn_note = ttk.Label(option_frame, text="选择接口:")
            wn_note.pack(side="top", padx=10, pady=10)
            var_resolution = tk.StringVar()
            var_resolution.set("请选择……")  # 默认选择1080P
            resolution_choices = ["[保罗]sm.ms-动漫", "[保罗]gitHub.io-动漫", "[次元]原神","[次元]随机","[次元]AI生成","[次元]风景","[次元]小狐狸","[次元]萌图","[樱花]随机","[PAULZZH]东方"]
            resolution_combobox = ttk.Combobox(option_frame, textvariable=var_resolution, values=resolution_choices)
            resolution_combobox.pack()
            resolution_combobox.bind("<<ComboboxSelected>>", lambda e: thread_it(en_w))
            image_label = ttk.Label(option_frame)
            image_label.pack()

            
            def en_w():
                
                global tau,dlb,tau1,image_url,UHD_image_url,title,dlb1,dlb2,bing_run_past,wau1,pa1,tau2
                clean_mode_data("1")
                if bing_run_past:
                    bing_msg.destroy()
                    bing_run_past=0
                if tau:
                    dlb.destroy()
                    dlb1.destroy()
                    dlb2.destroy()
                    tau=0
                dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd())
                dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1())
                dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2())
                image_label.config(text="正在获取数据……")

                resolution_combobox.config(state="disabled")
                choices.config(state="disabled")
                if var_resolution.get() == "[保罗]sm.ms-动漫":
                    iiurl="https://api.paugram.com/wallpaper/?source=sm"
                elif var_resolution.get() == "[保罗]gitHub.io-动漫":
                    iiurl="https://api.paugram.com/wallpaper/?source=github"
                elif var_resolution.get() == "[次元]原神":
                    iiurl="https://t.mwm.moe/ysz"
                elif var_resolution.get() == "[次元]随机":
                    iiurl="https://t.mwm.moe/pc"
                elif var_resolution.get() == "[次元]AI生成":
                    iiurl="https://t.mwm.moe/ai"
                elif var_resolution.get() == "[次元]风景":
                    iiurl="https://t.mwm.moe/fj"
                elif var_resolution.get() == "[次元]小狐狸":
                    iiurl="https://t.mwm.moe/xhl"    
                elif var_resolution.get() == "[次元]萌图":
                    iiurl="https://t.mwm.moe/moe"      
                elif var_resolution.get() == "[樱花]随机":
                    iiurl="https://www.dmoe.cc/random.php"  
                elif var_resolution.get() == "[PAULZZH]东方":
                    iiurl="https://img.paulzzh.com/touhou/random"     
                        
                fm_value=get_file_format(iiurl)
                download(iiurl,f"temp.{fm_value}") 
                

                img = Image.open(f"temp.{fm_value}")
                img.thumbnail((500, 500))  # Adjust size as needed
                photo = ImageTk.PhotoImage(img)
                image_label.config(image=photo)
                image_label.image = photo  # Keep a reference!
                resolution_combobox.config(state="normal")
                choices.config(state="normal")
                    


                def dd():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\二次元_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"下载完成\n壁纸文件保存至{Pictures}\\二次元_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                def dd1():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\壁纸\\二次元_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    set_wallpaper(f"{Pictures}\\壁纸\\二次元_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"设置完成\n壁纸文件保存至{Pictures}\\壁纸\\二次元_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}\n请勿删除!")
                def dd2():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\收藏\\二次元_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"收藏完成\n壁纸文件保存至{Pictures}\\收藏\\二次元_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                tau=1
                dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
        elif var.get() == "风景(测试)":
            ttk.Separator(option_frame).pack(fill=ttk.X)
            
            wn_info=ttk.Label(option_frame, text="请注意，\n该功能使用了不稳定的第三方API\n我们不保证该功能的质量和可用性\n如果API失效或返回任何违法内容，请立即提交反馈！")
            wn_info.pack(side="top", padx=10, pady=10)
            wn_note = ttk.Label(option_frame, text="选择接口:")
            wn_note.pack(side="top", padx=10, pady=10)
            var_resolution = tk.StringVar()
            var_resolution.set("请选择……")  # 默认选择1080P
            resolution_choices = ["远方接口","缙哥哥接口"]
            resolution_combobox = ttk.Combobox(option_frame, textvariable=var_resolution, values=resolution_choices)
            resolution_combobox.pack()
            resolution_combobox.bind("<<ComboboxSelected>>", lambda e: thread_it(en_w))
            image_label = ttk.Label(option_frame)
            image_label.pack()

            
            def en_w():
                
                global fju,dlb,tau1,image_url,UHD_image_url,title,dlb1,dlb2,bing_run_past,fju1,pa1,tau2
                clean_mode_data("风景")
                if bing_run_past:
                    bing_msg.destroy()
                    bing_run_past=0
                if fju:
                    dlb.destroy()
                    dlb1.destroy()
                    dlb2.destroy()
                    fju=0
                dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd())
                dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1())
                dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2())
                image_label.config(text="正在获取数据……")
                resolution_combobox.config(state="disabled")
                choices.config(state="disabled")
                if var_resolution.get() == "远方接口":
                    iiurl="https://tu.ltyuanfang.cn/api/fengjing.php"
                elif var_resolution.get() == "缙哥哥接口":
                    iiurl="https://api.dujin.org/pic/fengjing"
                fm_value=get_file_format(iiurl)
                download(iiurl,f"temp.{fm_value}") 
                    

                img = Image.open(f"temp.{fm_value}")
                img.thumbnail((500, 500))  # Adjust size as needed
                photo = ImageTk.PhotoImage(img)
                image_label.config(image=photo)
                image_label.image = photo  # Keep a reference!
                resolution_combobox.config(state="normal")
                choices.config(state="normal")
                    


                def dd():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\风景_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"下载完成\n壁纸文件保存至{Pictures}\\风景_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                def dd1():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\壁纸\\风景_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    set_wallpaper(f"{Pictures}\\壁纸\\风景_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"设置完成\n壁纸文件保存至{Pictures}\\壁纸\\风景_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}\n请勿删除!")
                def dd2():
                    shutil.copy(f"temp.{fm_value}",f"{Pictures}\\收藏\\风景_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"收藏完成\n壁纸文件保存至{Pictures}\\收藏\\风景_{time.strftime('%Y-%m-%d', time.localtime())}.{fm_value}")
                fju=1
                dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)                
            # messagebox.showwarning(f"小树壁纸 V{VER} {update_type}","当前功能暂未移植至5.0内部测试版\n如想参与测试该功能\n请联系获取4.6内部测试版")
    # def on_closing():
    #     # 处理关闭窗口事件的代码
    #     windows.deiconify()

    # windows.protocol("WM_DELETE_WINDOW", on_closing)
    windows.mainloop()
# -----------------------------------------------------

    

else:
    # 以管理员权限重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)
