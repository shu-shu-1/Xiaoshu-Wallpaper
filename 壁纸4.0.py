# Copyright (c) 2024 by shu-shu-1 3458222@qq.com, All Rights Reserved. 
VER = 4.0
import time,os,requests,json,win32api,win32con,ctypes,shutil,sys
from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttk
import ctypes, sys
sys.stdout = sys.__stdout__
folder_name = r"C:\bing_wallpaper"
if os.path.exists(folder_name):
    pass
else: 
    os.mkdir(folder_name)
# _*_ coding:utf-8 _*_

def is_admin():
    try:
        # return 1
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        messagebox.showerror("错误", "获取管理员身份出错")
i=0
if is_admin():
    while 1:    
        i+=1
        with open('settings.json') as f:
            settings = json.loads(f.read())
        Downloads = os.path.join(os.path.expanduser("~"), 'Downloads')
        if settings["check_update"] and i==1:
            try:
                try:
                    h_update_js=json.loads(requests.get("https://mirror.ghproxy.com/https://raw.githubusercontent.com/shu-shu-1/BingWallpaper/main/version.json").text)
                except:
                    h_update_js=json.loads(requests.get("https://fastly.jsdelivr.net/gh/shu-shu-1/BingWallpaper@main/version.json").text)
                h_update_v=h_update_js["version"]
                h_update_url=h_update_js["dl_url"]
                if h_update_v > VER:
                    mmm=f"""选择功能
当前版本：{VER} 最新正式版本：{h_update_v}
有新版本！
Made By 小树
"""
                    mmf="非最新版"
                    have_update=1
                elif h_update_v == VER:
                    mmm=f"""选择功能
当前版本：{VER} 最新正式版本：{h_update_v}
当前为最新版
Made By 小树
"""                
                    have_update=0
                    mmf="正式版本"
                else:
                    mmm=f"""选择功能
当前版本：{VER} 最新正式版本：{h_update_v}
当前为测试版，请勿外泄
Made By 小树
"""
                    have_update=0
                    mmf="测试版本"
            except:
                messagebox.showerror("更新错误","检查更新失败")
                mmm=f"""选择功能
当前版本：{VER} [检查更新失败]
Made By 小树
"""
                have_update=0
                mmf="[检查更新失败]"
        elif i==1:
            mmm=f"""选择功能
当前版本：{VER} [检查更新已关闭]
Made By 小树
"""
            have_update=0
            mmf="[检查更新已关闭]"
            # os.chdir(sys.path[0])
        def download(url: str, fname: str):
            s = requests.Session()
            s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0'})
            resp = s.get(url, stream=True)
            with open(fname, "wb") as f:
                for chunk in resp.iter_content(chunk_size=512):
                    f.write(chunk)




        timestamp = time.time()
        url_1080p="https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
        url_2880_1620=f"https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc={int(timestamp * 1000)}&pid=hp&uhd=1&uhdwidth=2880&uhdheight=1620"




        def set_wallpaper(filelink):
            ctypes.windll.user32.SystemParametersInfoW(20, 0, filelink, 0)
            time.sleep(1)
            Hkey = win32api.RegCreateKey(win32con.HKEY_CURRENT_USER, r'Control Panel\Desktop')
            win32api.RegSetValueEx(Hkey, 'WallPaper', 0, win32con.REG_SZ, filelink)
            win32api.RegCloseKey(Hkey)

        import tkinter as tk
        from PIL import Image, ImageTk

        def bbuttonbox(title, msg, choices, image_path=None ,icon=None):
            root = ttk.Window(themename="minty")

            root.title(title)
            # root.iconbitmap("setting-config.ico")  # 请确保此图标文件实际存在或注释掉这行代码
            message_label = ttk.Label(root, text=msg)
            message_label.pack(pady=10)
            if icon:

                root.iconbitmap(icon)
            # Check if an image_path was provided and if so, display the image
            if image_path:
                # Open the image file
                img = Image.open(image_path)
                # Resize the image to a better-fitting size if necessary
                img.thumbnail((200, 200))  # Adjust the size as per your requirement
                photo = ImageTk.PhotoImage(img)
                image_label = ttk.Label(root, image=photo)
                image_label.photo = photo  # Keep a reference!
                image_label.pack(pady=10)  # Display image above the buttons

            buttons_frame = ttk.Frame(root)
            buttons_frame.pack(pady=10)

            def on_button_click(choice):
                root.result = choice
                root.destroy()
                root.exit()

            for index, choice in enumerate(choices):
                button = tk.Button(buttons_frame, text=choice,
                                    command=lambda choice=choice: on_button_click(choice))
                button.grid(row=0, column=index, padx=5, pady=5)
            
            root.mainloop()
            try:
                return root.result
            except:
                return None

        # Example usage:
        # result = bbuttonbox("Test Window", "Choose your option:", ["Button1", "Button2", "Button3"], image_path="setting-config.png")
        # print("You chose:", result)
            
            # if custom_buttons:
            #     for index, button_text in enumerate(custom_buttons):
            #         button = tk.Button(buttons_frame, text=button_text,
            #                            command=lambda button_text=button_text: on_button_click(button_text))
            #         button.grid(row=1, column=index, padx=5, pady=5)
            


        if have_update:
            chchch=["Bing壁纸源","unsplash随机壁纸","wallhaven壁纸源（镜像）","关于","设置","更新","退出"]
        else:
            chchch=["Bing壁纸源","unsplash随机壁纸","wallhaven壁纸源（镜像）","关于","设置","退出"]
        a=bbuttonbox(msg=mmm,title=f"壁纸 V{VER} {mmf}" ,choices=chchch,icon="icon.ico")
        if a=="Bing壁纸源":
            response = requests.get(url_1080p) 
            data = response.json()
            image = data["images"][0]
            image_url = "https://cn.bing.com" + image["url"]
            title = image["title"]
            copyright = image["copyright"]
            quiz = "https://cn.bing.com" + image["quiz"]
            UHD_image_url='https://cn.bing.com' + image["url"].replace('1920x1080', 'UHD')
            download(image_url,f"temp.png")
            b=bbuttonbox(msg=f"Bing每日壁纸\n今日标题: {title}\n版权: {copyright}",title=f"壁纸 V{VER} {mmf}",choices=["下载","设置壁纸"],image_path="temp.png",icon="q.ico")
            if b=="下载":
                c=bbuttonbox(msg=f"Bing每日壁纸\n今日标题: {title}\n版权: {copyright}\n\n\n下载-请选择清晰度",title=f"壁纸 V{VER} {mmf}",choices=["UHD(最高清)","1080P"],image_path="temp.png",icon="q.ico")
                if c=="1080P":
                    download(image_url,f"{Downloads}\\{title}_{time.strftime('%Y-%m-%d', time.localtime())}.png")
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"下载完成\n文件保存至{Downloads}\\{title}_{time.strftime('%Y-%m-%d', time.localtime())}.png")
                if c=="UHD(最高清)":
                    download(UHD_image_url,f"{Downloads}\\{title}_{time.strftime('%Y-%m-%d', time.localtime())}.png")
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"下载完成\n文件保存至{Downloads}\\{title}_{time.strftime('%Y-%m-%d', time.localtime())}.png")
            elif b=="设置壁纸":
                
                c=bbuttonbox(msg=f"Bing每日壁纸\n今日标题: {title}\n版权: {copyright}\n\n\n设置壁纸-请选择清晰度",title=f"壁纸 V{VER} {mmf}",choices=["UHD(最高清)","1080P"],image_path="temp.png",icon="q.ico")
                if c=="1080P":
                    download(image_url,r"C:\bing_wallpaper\wallpaper.png")
                    set_wallpaper(r"C:\bing_wallpaper\wallpaper.png")
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"设置完成\n壁纸文件保存至C:\\bing_wallpaper\\wallpaper.png\n请勿删除")
                if c=="UHD(最高清)":
                    download(UHD_image_url,r"C:\bing_wallpaper\wallpaper.png")
                    set_wallpaper(r"C:\bing_wallpaper\wallpaper.png")
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"设置完成\n壁纸文件保存至C:\\bing_wallpaper\\wallpaper.png\n请勿删除")
        elif a=="unsplash随机壁纸":
            
            # b=bbuttonbox(msg="unsplash壁纸源 接口选择",title=f"壁纸 V{VER} {mmf}",choices=["随机","搜索"],icon="unsplash.ico")

            # if b=="随机":
            c=bbuttonbox(msg="unsplash随机壁纸\n选择分辨率",title=f"壁纸 V{VER} {mmf}",choices=["1080P","完全随机"],icon="unsplash.ico")
            if c=="1080P":
                url=f"https://source.unsplash.com/random/1920x1080"
            elif c=="完全随机":
                url=f"https://source.unsplash.com/random/"
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
                source_url = url
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
            download(url,f"temp.{fm_value}")       
            bb=bbuttonbox(msg=f"unsplash壁纸源 随机",title=f"壁纸 V{VER} {mmf}",choices=["下载","设置壁纸"],image_path=f"temp.{fm_value}",icon="unsplash.ico")
            if bb == "下载":
                shutil.copy(f"temp.{fm_value}",f"{Downloads}\\unsplash随机_{time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime())}.{fm_value}")
                messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"下载完成\n壁纸文件保存至{Downloads}\\unsplash随机_{time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime())}.{fm_value}")
            elif bb == "设置壁纸":
                shutil.copy(f"temp.{fm_value}",f"C:\\bing_wallpaper\\wallpaper.{fm_value}")
                set_wallpaper(f"C:\\bing_wallpaper\\wallpaper.{fm_value}")
                messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"设置完成\n壁纸文件保存至C:\\bing_wallpaper\\wallpaper.{fm_value}\n请勿删除")
            # messagebox.showwarning(f"壁纸 V{VER} {mmf}",f"{mmf}-该功能暂未开放")
        elif a=="wallhaven壁纸源（镜像）":
            b=bbuttonbox(msg="wallhaven壁纸源（镜像）",title=f"壁纸 V{VER} {mmf}",choices=["随机","每日"],icon="wallhaven.ico")
            if b=="随机":
                url="https://api.nguaduot.cn/wallhaven/random"
            elif b=="每日":
                url="https://api.nguaduot.cn/wallhaven/today"
            import mechanize
            br = mechanize.Browser()
            br.set_handle_equiv(True)  # 设置是否处理HTML http-equiv标头
            br.set_handle_redirect(True)  # 设置是否处理重定向
            br.set_handle_referer(True)  # 设置是否向每个请求添加referer头
            br.set_handle_robots(False)  # 设置是不遵守robots中的规则
            br.set_handle_gzip(False)  # 处理giz传输编码
            br.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
            source_url = url
            response=br.open(source_url)
            target_url=response.geturl()
            fm_value=target_url[-3:]
            try:
                download(url,f"temp.{fm_value}")
                bb=bbuttonbox(msg=f"wallhaven壁纸源",title=f"壁纸 V{VER} {mmf}",choices=["下载","设置壁纸"],image_path=f"temp.{fm_value}",icon="wallhaven.ico")
                if bb == "下载":
                    shutil.copy(f"temp.{fm_value}",f"{Downloads}\\wallhaven壁纸源_{time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime())}.{fm_value}")
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"下载完成\n壁纸文件保存至{Downloads}\\wallhaven壁纸源_{time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime())}.{fm_value}")
                elif bb == "设置壁纸":
                    shutil.copy(f"temp.{fm_value}",f"C:\\bing_wallpaper\\wallpaper.{fm_value}")
                    set_wallpaper(f"C:\\bing_wallpaper\\wallpaper.{fm_value}")
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"设置完成\n壁纸文件保存至C:\\bing_wallpaper\\wallpaper.{fm_value}\n请勿删除")
            except:
                messagebox.showwarning(f"壁纸 V{VER} {mmf}",f"下载失败")
            # messagebox.showwarning(f"壁纸 V{VER} {mmf}",f"{mmf}-该功能暂未开放")
        elif a=="设置":
            b=bbuttonbox(msg="设置",title=f"壁纸 V{VER} {mmf}",choices=["检查更新设置","设置Bing壁纸自启动"],icon="setting-config.ico")
            if b=="检查更新设置":
                if settings['check_update']:
                    cu="是"
                    
                    
                else:
                    cu="否"
                c=bbuttonbox(msg=f"是否启用更新检查\n当前选项:{cu}",title=f"壁纸 V{VER} {mmf}",choices=["是","否"],icon="setting-config.ico")
                if c=="是":

                    settings['check_update']=1
                    with open('settings.json', 'w') as f:
                        f.write(str(settings).replace("'", "\""))
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"已启用更新检查")
                if c=="否":
                    settings['check_update']=0
                    with open('settings.json', 'w') as f:
                        f.write(str(settings).replace("'", "\""))
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"已禁用更新检查")
            elif b=="设置Bing壁纸自启动":
                

                if settings['bing_auto_start']:
                    a_s="是"
                else:
                    a_s="否"
                c=bbuttonbox(msg=f"是否启用Bing壁纸自启动\n当前选项:{a_s}",title=f"壁纸 V{VER} {mmf}",choices=["是","否"],icon="setting-config.ico")
                if c=="是":
                    settings['bing_auto_start']=1
                    if os.path.exists(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bing_auto_run.exe") is not True:
                        shutil.copy("bing_auto_run.exe",r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")

                    with open('settings.json', 'w') as f:
                        f.write(str(settings).replace("'", "\""))
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"已启用Bing壁纸自启动")
                if c=="否":
                    settings['bing_auto_start']=0
                    if os.path.exists(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bing_auto_run.exe"):
                        os.remove(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bing_auto_run.exe")
                    with open('settings.json', 'w') as f:
                        f.write(str(settings).replace("'", "\""))
                    messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"已禁用Bing壁纸自启动")
        elif a=="更新":
            download(h_update_url,fname="新版本文件(请手动解压替换).zip")
            messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"已下载最新版本压缩包至\n{os.getcwd()}\\新版本文件(请手动解压替换).zip\n请手动解压替换旧版本！")
            exit()
        elif a=="退出":
            exit()
        elif a=="关于":
            messagebox.showinfo(f"壁纸 V{VER} {mmf}",f"壁纸\n版本：{VER} {mmf}\n作者：小树\n更新时间：2024.1.13\n联系作者：zs3458222@outlook.com")
        # elif a=="帮助":

            # messagebox.showwarning(f"壁纸 V{VER} {mmf}",f"{mmf}-该功能暂未开放")
        # elif a=="bing 设置壁纸":
            # folder_name = r"C:\bing_wallpaper"
            # if os.path.exists(folder_name):
                # pass

            # else:
                    
                # os.mkdir(folder_name)
            # download(UHD_image_url,r"C:\bing_wallpaper\wallpaper.png")
            # set_wallpaper(r'C:\bing_wallpaper\wallpaper.png')
        # elif a=="unsplash随机（可能有水印） 下载":
            # download("https://source.unsplash.com/random",f"unsplash随机_{time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime())}.png")
            
        # elif a=="wallhaven随机 下载（可能随机出不好的东西）":

            # fff=f"wallhaven随机_{time.strftime("%Y-%m-%d_%H.%M.%S", time.localtime())}.png"
            # res1 = requests.get("https://v.api.aa1.cn/api/api-fj-1/index.php?aa1=json") 
            # url11=f"https://v.api.aa1.cn/api/api-fj-1{json.loads(res1.text)['img']}"
            # print(url11)
            # download("https://api.nguaduot.cn/wallhaven/random",fff)

            # mode=input(f"""{Style.RESET_ALL}{Back.GREEN}选择模式:
            # -d1080\t下载1080p图片至当前文件夹
            # -duhd\t下载UHD最高请图片至当前文件夹
            # -w1080\t设置1080p图片为壁纸
            # -wuhd\t设置UHD最高请图片为壁纸
            # {ifupdate}
            # {Style.RESET_ALL}{Back.GREEN}输入命令选择：-""")
            # if mode == "d1080" or mode == "-d1080":
            #     # download_img(image_url,f"{title}_{time.strftime("%Y-%m-%d", time.localtime())}.png")
            #     download(image_url,f"{title}_{time.strftime("%Y-%m-%d", time.localtime())}.png")
            # elif mode == "w1080" or mode == "-w1080":
            #     import ctypes
            #     folder_name = r"C:\bing_wallpaper"
            #     if os.path.exists(folder_name):

            #         print(f"{Style.RESET_ALL}{Fore.YELLOW}[!]文件夹“{folder_name}”已创建过，跳过")
            #     else:
                    
            #         os.mkdir(folder_name)
            #         print(f"{Style.RESET_ALL}{Fore.GREEN}[✔]新建文件夹“{folder_name}”成功")
            #     download(image_url,r"C:\bing_wallpaper\wallpaper.png")
            #     set_wallpaper()
            # elif mode == "duhd" or mode == "-duhd":
            #     # download_img(image_url,f"{title}_{time.strftime("%Y-%m-%d", time.localtime())}.png")
            #     download(UHD_image_url,f"{title}_{time.strftime("%Y-%m-%d", time.localtime())}.png")
            # elif mode == "wuhd" or mode == "-wuhd":
            #     import ctypes
            #     folder_name = r"C:\bing_wallpaper"
            #     if os.path.exists(folder_name):

            #         print(f"{Style.RESET_ALL}{Fore.YELLOW}[!]文件夹“{folder_name}”已创建过，跳过")
            #     else:
                    
            #         os.mkdir(folder_name)
            #         print(f"{Style.RESET_ALL}{Fore.GREEN}[✔]新建文件夹“{folder_name}”成功")
            #     download(UHD_image_url,r"C:\bing_wallpaper\wallpaper.png")
            #     set_wallpaper()
            # elif mode == "up" or mode == "-up":
                
            #     download(h_update_url,"update_temp.exe")
            #     # print(f"{Style.RESET_ALL}{Fore.BLUE}[]重要！")
            #     subprocess.call(['python', 'update.exe'])
            #     exit()
            # else:
            #     print(f"{Style.RESET_ALL}{Fore.RED}[×]命令：“{mode}” 不存在")
            # input('按下回车退出……')




else:
    # 以管理员权限重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)
    
