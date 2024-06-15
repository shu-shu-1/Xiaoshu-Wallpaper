# Copyright (c) 2024 by shu-shu-1 3458222@qq.com, All Rights Reserved. 
VER = 5.1
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
import time,os,requests,json5,win32api,win32con,ctypes,shutil,sys,threading,pystray,random,schedule,mechanize
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttk
from PIL import Image, ImageTk
from tkinter import PhotoImage
print("测试版专用控制台窗口，如有任何报错请联系作者\n请等待窗口显示")

with open('./data/settings.json5',encoding="utf-8") as f:
    settings = json5.loads(f.read())
with open('./data/style.json5',encoding="utf-8") as f:
    style_settings = json5.loads(f.read())
def new_folder(ffffffff):
    folder_name = ffffffff

    if os.path.exists(folder_name):
        pass
    else: 
        os.makedirs(folder_name)
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


images11=[i for i in os.listdir(path)]
# 壁纸更换任务
def change_wallpaper():


    img = random.choice(images11)
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
        
# 托盘----------------------------------------------

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
                update_web_json5=json5.loads(requests.get("https://mirror.ghproxy.com/https://raw.githubusercontent.com/shu-shu-1/BingWallpaper/main/version.json").text)
            except:
                update_web_json5=json5.loads(requests.get("https://fastly.jsdelivr.net/gh/shu-shu-1/BingWallpaper@main/version.json").text)
            web_ver=update_web_json5[settings["update_channel"]]["ver"]
            update_f_url=update_web_json5[settings["update_channel"]]["url"]
            update_note=update_web_json5[settings["update_channel"]]["note"]
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
        except:
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
    style = ttk.Style(style_settings["theme"])
    windows.geometry("1000x800+374+182")
    windows.title(f"小树壁纸 V{VER} {update_type}")
    windows.iconbitmap("./icon/icon.ico")
    # windows.resizable(0, False)
    # windows.attributes('-topmost', 'true')  # 置顶
    # hwnd = windows.winfo_id()  # 获取Tkinter窗口的句柄
    # 使用Windows API禁用最大化按钮
    # win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE) & ~win32con.WS_MAXIMIZEBOX)
    # windows.attributes('-transparentcolor','white')
    # windows.overrideredirect(True)  # 关闭标题栏

    # 定义拖动函数
    def start_dragging(event):
        windows.x = event.x_root
        windows.y = event.y_root

    def stop_dragging(event):
        windows.x = None
        windows.y = None

    def do_dragging(event):
        if windows.x is not None:
            # 引入步长来降低拖动灵敏度
            step_x = (event.x_root - windows.x) / 50  # 调整除数来控制步长大小
            step_y = (event.y_root - windows.y) / 50  # 调整除数来控制步长大小
            new_x = windows.winfo_x() + round(step_x)
            new_y = windows.winfo_y() + round(step_y)

            # 检查新的位置是否在屏幕内
            screen_width = windows.winfo_screenwidth()
            screen_height = windows.winfo_screenheight()
            window_width = windows.winfo_width()
            window_height = windows.winfo_height()

            # 确保窗口不会完全移出屏幕
            if new_x < 0:
                new_x = 0
            if new_y < 0:
                new_y = 0
            if new_x + window_width > screen_width:
                new_x = screen_width - window_width
            if new_y + window_height > screen_height:
                new_y = screen_height - window_height

            windows.geometry(f"+{new_x}+{new_y}")


# -----高dpi适配
    if (settings["dpi_fix"]):
    #告诉操作系统使用程序自身的dpi适配
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        #获取屏幕的缩放因子
        ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
        #设置程序缩放
        windows.tk.call('tk', 'scaling', ScaleFactor/settings["dpi_fix_size"])

# -----背景




    if style_settings["pic"] != "" and settings["in_test"]:
        # 加载背景图片
        bg_image = Image.open(style_settings["pic"])
        bg_photo = ImageTk.PhotoImage(bg_image)

        # 创建一个Label用于显示背景图片
        bg_label = tk.Label(windows, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        windows.bind("<Configure>", lambda event: refa())
    # # 加载背景图片
    #     background_image_path = style_settings["pic"]
    #     original_image = Image.open(background_image_path)
    #     new_folder("temp")
    #     temp_image_path = "./temp/temp_background.png"

    #     # 更新背景图片的函数
    #     def update_background():
    #         # 根据当前窗口大小截取背景图片
    #         width, height = windows.winfo_width(), windows.winfo_height()
    #         cropped_image = original_image.resize((width, height))
    #         cropped_image.save(temp_image_path)

    #         # 加载截取后的图片
    #         temp_image = ImageTk.PhotoImage(cropped_image)

    #         # 设置窗口背景
    #         background_label.config(image=temp_image)
    #         background_label.image = temp_image  # 保持对图片的引用，防止被垃圾回收

    #     # 创建一个标签用于显示背景图片
    #     background_label = tk.Label(windows)
    #     background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #     # 初始化背景
    #     update_background()

    #     # 绑定窗口大小改变事件
    #     windows.bind("<Configure>", lambda event: update_background())




# -----
# -----菜单栏
    # menubar = ttk.Menu(windows) 
    # menubar.add_command(label = "收藏夹自动轮换开关",command=start_stop_wallpaper)
    # menubar.add_command(label = "设置",command=lambda: os.system("config.exe"))
    # if have_update:
    #     menubar.add_command(label = "更新",command=lambda: update()) 
    # menubar.add_command(label = "关于",command=lambda: about()) 
    # menubar.add_command(label='退出',command=lambda: os._exit(1)) 

    # windows.config(menu = menubar)
    buttonbar =ttk.Frame(windows,style='primary.TFrame')
    buttonbar.pack(fill=ttk.X,pady=1,side=ttk.TOP)

    buttonbar.bind("<ButtonPress-1>", start_dragging)
    buttonbar.bind("<ButtonRelease-1>", stop_dragging)
    buttonbar.bind("<B1-Motion>", do_dragging)
    images = [
            PhotoImage(
                name='se', 
                file='./assets/setting 20x.png'),
            PhotoImage(
                name='rs', 
                file='./assets/收藏文件夹_folder-focus.png'),
            PhotoImage(
                name='ex', 
                file='./assets/退出_logout.png'),   
            PhotoImage(
                name='ab', 
                file='./assets/信息_info.png'),     
            PhotoImage(
                name='up', 
                file='./assets/更新_update-rotation.png'),    
            PhotoImage(
                name='st', 
                file='./assets/星星_star.png'),  
            PhotoImage(
                name='dl', 
                file='./assets/下载_download.png'), 
            PhotoImage(
                name='sw', 
                file='./assets/计算机设置_setting-computer.png'),   
            PhotoImage(
                name='rd', 
                file='./assets/redo.png'),     
            PhotoImage(
                name='nothing',
                file="./assets/透明.png"
            )
            ]

    if have_update:
        btn2 = ttk.Button(master=buttonbar,text='更新',image='up',compound=ttk.LEFT,command=lambda: update())
        btn2.pack(side=ttk.LEFT,ipadx=5,ipady=5,padx=0,pady=1)
    btn1 = ttk.Button(master=buttonbar,text='收藏夹自动轮换开关',image='rs',compound=ttk.LEFT,command=start_stop_wallpaper)
    btn1.pack(side=ttk.LEFT,ipadx=5,ipady=5,padx=0,pady=1)

    

    btn = ttk.Button(master=buttonbar,text='退出',image='ex',compound=ttk.LEFT,command=lambda: os._exit(1))
    btn.pack(side=ttk.RIGHT,ipadx=5,ipady=5,padx=0,pady=1)
    btne = ttk.Button(master=buttonbar,text='设置',image='se',compound=ttk.LEFT,command=lambda: os.system("config.exe"))
    btne.pack(side=ttk.RIGHT,ipadx=5,ipady=5,padx=0,pady=1)
    btne = ttk.Button(master=buttonbar,text='关于',image='ab',compound=ttk.LEFT,command=lambda: about())
    btne.pack(side=ttk.RIGHT,ipadx=5,ipady=5,padx=0,pady=1)
    


# -----
    icon_title=ttk.Label(windows, text="小树壁纸", font=("微软雅黑", 30))       
    icon_title.pack(side="top", padx=0, pady=0)
    ti=tk.Label(windows, text="请选择壁纸源:")
    ti.pack(side="top")
        # 假设你有一个函数 refresh_image 用于刷新图片
    def refresh_image():
        # 刷新图片的逻辑
        with open('./data/style.json5',encoding="utf-8") as f:
            style_settings = json5.loads(f.read())
        style.theme_use(style_settings["theme"])



    refresh_button = ttk.Button(windows, text="刷新主题", image='rd',compound=ttk.RIGHT, command=refresh_image)
    # refresh_button.image = refresh_button_photo  # Keep a reference!
    refresh_button.pack(side="bottom", anchor=ttk.SE,ipadx=5,ipady=5,padx=0,pady=1)
    var = ttk.StringVar()
    var.set("请选择……")
    choices=ttk.Combobox(windows, textvariable=var, value=('Bing壁纸源', 'Unsplash随机壁纸', 'wallhaven壁纸源(镜像)', '二次元壁纸源(测试)','风景(测试)'))
    choices.pack(side="top", padx=10, pady=10)
    

    choices.bind("<<ComboboxSelected>>", lambda event: select_source())
    option_frame = tk.Frame(windows)
    option_frame.pack(fill='both', expand=True)
    def refa(): 
        # option_frame.config(bg="white")
        # option_frame.config(bg="white")
        # option_frame.config(bg="")
        # option_frame.config(bg="")
        # option_frame.config(bg="white")
        # option_frame.config(bg="")
        pass
    refa()
    note_msg=ttk.Label(windows, text=note,background="")
    note_msg.pack(side='top', expand='yes', anchor='sw')

    def clear_frame():
        # 移除当前frame中的所有组件
        refa()
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
        
        refa()
        global pa1,resolution_combobox
        clear_frame()
        pa1=0
        if var.get() == "Bing壁纸源":
            refa()
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
            refa()
            
            def bing_w():
                refa()
                global pa,dlb,pa1,image_url,UHD_image_url,title,dlb1,dlb2,bing_msg
                if pa:
                    dlb.destroy()
                    dlb1.destroy()
                    dlb2.destroy()
                    pa=0
                
                dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd(iiurl), image="dl",compound=ttk.LEFT)
                dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1(iiurl), image="sw",compound=ttk.LEFT)
                dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2(iiurl), image="st",compound=ttk.LEFT)
                image_label.config(text="正在获取数据……")
                try:
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
                    refa()
                    def dd(url1):
                        thread_it(img_download, url1, f"{Pictures}\\{title}_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.png")
                    def dd1(url1):
                        thread_it(wal_download, url1, f"{Pictures}\\壁纸\\{title}_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.png")
                    def dd2(url1):
                        thread_it(star_download, url1, f"{Pictures}\\收藏\\{title}_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.png")
                    if var_resolution.get() == "UHD(原图)":
                        iiurl=UHD_image_url
                    else:
                        iiurl=image_url
                    pa=1
                    refa()
                    dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                    dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                    dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                    refa()
                except:
                    messagebox.showerror("错误","连接错误，请检测网络或重试")
                    resolution_combobox.config(state="normal")
                    choices.config(state="normal")
                    image_label.config(text="出现错误")
        elif var.get() == "Unsplash随机壁纸":
            refa()
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
                refa()
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
                dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd(), image="dl",compound=ttk.LEFT)
                dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1(), image="sw",compound=ttk.LEFT)
                dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2(), image="st",compound=ttk.LEFT)
                image_label.config(text="正在获取数据……")
                try:
                    if pau1 != 1:
                        pau1=1
                        if var_resolution.get() == "无限制":
                            iiurl="https://source.unsplash.com/random/"
                        else:
                            iiurl="https://source.unsplash.com/random/1920x1080"
                        prefix = 'plus'
                        while prefix!='images':
                            
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
                        refa()
                    def dd():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"下载完成\n壁纸文件保存至{Pictures}\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                    def dd1():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\壁纸\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        set_wallpaper(f"{Pictures}\\壁纸\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"设置完成\n壁纸文件保存至{Pictures}\\壁纸\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}\n请勿删除!")
                    def dd2():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\收藏\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d_%H.%M.%S_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"收藏完成\n壁纸文件保存至{Pictures}\\收藏\\Unsplash随机壁纸_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                    pau=1
                    refa()
                    dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                    dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                    dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                    refa()
                except:
                    messagebox.showerror("错误","连接错误，请检测网络或重试")
                    resolution_combobox.config(state="normal")
                    choices.config(state="normal")
                    image_label.config(text="出现错误")

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
            refa()
            
            def wn_w():
                refa()
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
                try:
                    dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd(), image="dl",compound=ttk.LEFT)
                    dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1(), image="sw",compound=ttk.LEFT)
                    dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2(), image="st",compound=ttk.LEFT)
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
                        img.thumbnail((250, 250))  # Adjust size as needed
                        photo = ImageTk.PhotoImage(img)
                        image_label.config(image=photo)
                        image_label.image = photo  # Keep a reference!
                        resolution_combobox.config(state="normal")
                        choices.config(state="normal")
                        refa()
                    


                    def dd():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\wallhaven壁纸源_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"下载完成\n壁纸文件保存至{Pictures}\\wallhaven壁纸源_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                    def dd1():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\壁纸\\wallhaven壁纸源_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        set_wallpaper(f"{Pictures}\\壁纸\\wallhaven壁纸源_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"设置完成\n壁纸文件保存至{Pictures}\\壁纸\\wallhaven壁纸源_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}\n请勿删除!")
                    def dd2():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\收藏\\wallhaven壁纸源_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"收藏完成\n壁纸文件保存至{Pictures}\\收藏\\wallhaven壁纸源_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                    wau=1
                    refa()
                    dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                    dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                    dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                    refa() 
                except:
                    messagebox.showerror("错误","连接错误，请检测网络或重试")
                    resolution_combobox.config(state="normal")
                    choices.config(state="normal")
                    image_label.config(text="出现错误")
        elif var.get() == "二次元壁纸源(测试)":
            ttk.Separator(option_frame).pack(fill=ttk.X)
            wn_info=ttk.Label(option_frame, text="请注意!\n该功能使用了不稳定的第三方API,我们不保证该功能的质量和可用性\n如果API失效或返回任何违法内容,请立即提交反馈!",anchor=ttk.CENTER, justify=ttk.CENTER)
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
            refa()

            
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
                dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd(), image="dl",compound=ttk.LEFT)
                dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1(), image="sw",compound=ttk.LEFT)
                dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2(), image="st",compound=ttk.LEFT)
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
                try:
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
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\二次元_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"下载完成\n壁纸文件保存至{Pictures}\\二次元_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                    def dd1():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\壁纸\\二次元_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        set_wallpaper(f"{Pictures}\\壁纸\\二次元_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"设置完成\n壁纸文件保存至{Pictures}\\壁纸\\二次元_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}\n请勿删除!")
                    def dd2():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\收藏\\二次元_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"收藏完成\n壁纸文件保存至{Pictures}\\收藏\\二次元_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                    tau=1
                    refa()
                    dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                    dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                    dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                    refa()
                except:
                    messagebox.showerror("错误","连接错误，请检测网络或重试")
                    resolution_combobox.config(state="normal")
                    choices.config(state="normal")
                    image_label.config(text="出现错误")
        elif var.get() == "风景(测试)":
            ttk.Separator(option_frame).pack(fill=ttk.X)
            
            wn_info=ttk.Label(option_frame, text="请注意!\n该功能使用了不稳定的第三方API,我们不保证该功能的质量和可用性\n如果API失效或返回任何违法内容,请立即提交反馈!",anchor=ttk.CENTER, justify=ttk.CENTER)
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
            refa()

            
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
                dlb=ttk.Button(option_frame, text="下载壁纸", command=lambda: dd(), image="dl",compound=ttk.LEFT)
                dlb1=ttk.Button(option_frame, text="设置壁纸", command=lambda: dd1(), image="sw",compound=ttk.LEFT)
                dlb2=ttk.Button(option_frame, text="收藏壁纸", command=lambda: dd2(), image="st",compound=ttk.LEFT)
                image_label.config(text="正在获取数据……")
                resolution_combobox.config(state="disabled")
                choices.config(state="disabled")
                if var_resolution.get() == "远方接口":
                    iiurl="https://tu.ltyuanfang.cn/api/fengjing.php"
                elif var_resolution.get() == "缙哥哥接口":
                    iiurl="https://api.dujin.org/pic/fengjing"
                try:
                    fm_value=get_file_format(iiurl)
                    download(iiurl,f"temp.{fm_value}") 
                        

                    img = Image.open(f"temp.{fm_value}")
                    img.thumbnail((300, 300))  # Adjust size as needed
                    photo = ImageTk.PhotoImage(img)
                    image_label.config(image=photo)
                    image_label.image = photo  # Keep a reference!
                    resolution_combobox.config(state="normal")
                    choices.config(state="normal")
                        

                    # # 假设你有一个函数 refresh_image 用于刷新图片
                    # # def refresh_image():
                    # #     # 刷新图片的逻辑
                    # #     pass

                    # # 创建刷新按钮
                    # refresh_button_image = Image.open("./icon/redo.png")
                    # refresh_button_image.thumbnail((25, 25))
                    # refresh_button_photo = ImageTk.PhotoImage(refresh_button_image)
                    
                    # refresh_button = ttk.Button(option_frame, image=refresh_button_photo, command=refresh_image)
                    # refresh_button.image = refresh_button_photo  # Keep a reference!
                    # refresh_button.pack(side="bottom", anchor=ttk.SE)

                    def dd():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\风景_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"下载完成\n壁纸文件保存至{Pictures}\\风景_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                    def dd1():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\壁纸\\风景_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        set_wallpaper(f"{Pictures}\\壁纸\\风景_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"设置完成\n壁纸文件保存至{Pictures}\\壁纸\\风景_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}\n请勿删除!")
                    def dd2():
                        shutil.copy(f"temp.{fm_value}",f"{Pictures}\\收藏\\风景_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                        messagebox.showinfo(f"小树壁纸 V{VER} {update_type}",f"收藏完成\n壁纸文件保存至{Pictures}\\收藏\\风景_{time.strftime('%Y-%m-%d_%H.%M.%S', time.localtime())}.{fm_value}")
                    fju=1
                    refa()
                    dlb.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)
                    dlb1.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER) 
                    dlb2.pack(side=ttk.LEFT, expand=True, fill=ttk.X, anchor=ttk.CENTER)  
                    refa() 
                    refa()             
                except:
                    messagebox.showerror("错误","连接错误，请检测网络或重试")
                    resolution_combobox.config(state="normal")
                    choices.config(state="normal")
                    image_label.config(text="出现错误")
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
