VER=3.2  #Python Beta 构建版
try:
    
    import time,os,requests,json,win32api,win32con
    from tqdm import tqdm
    from colorama import init,Fore, Back, Style
    import subprocess
    init(autoreset=True)
    # os.chdir(sys.path[0])
    def download(url: str, fname: str):
        resp = requests.get(url, stream=True)

        total = int(resp.headers.get('content-length', 0))
        with open(fname, 'wb') as file, tqdm(
            desc=fname,
            total=total,
            unit='iB',
            unit_scale=True,
            unit_divisor=1024,
        ) as bar:
            for data in resp.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
        print(f"{Fore.GREEN}[✔]下载完成")
    print(f"{Fore.YELLOW}[!]正在检查更新")
    try:
        try:
            h_update_js=json.loads(requests.get("https://mirror.ghproxy.com/https://raw.githubusercontent.com/shu-shu-1/BingWallpaper/main/version.json").text)
        except:
            h_update_js=json.loads(requests.get("https://fastly.jsdelivr.net/gh/shu-shu-1/BingWallpaper@main/version.json").text)
        h_update_v=h_update_js["version"]
        h_update_url=h_update_js["dl_url"]
        h_update_t=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        h_update=f"最后检查更新：{h_update_t} 最新版本：{h_update_v}"
        print(f"""Made By 小树
        当前版本：{VER} {h_update}""")
    except:
        print(f"{Style.RESET_ALL}{Fore.RED}[×]检查更新失败")

    print(f"{Fore.YELLOW}[!]正在连接Bing壁纸远程服务器获取信息")
    timestamp = time.time()
    url_1080p="https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN"
    url_2880_1620=f"https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc={int(timestamp * 1000)}&pid=hp&uhd=1&uhdwidth=2880&uhdheight=1620"
    try:
        response = requests.get(url_1080p) 
    except:
        print(f"{Style.RESET_ALL}{Fore.RED}[×]连接Bing壁纸远程服务器失败")
        

    def set_wallpaper():
        ctypes.windll.user32.SystemParametersInfoW(20, 0, r'C:\bing_wallpaper\wallpaper.png', 0)
        time.sleep(1)
        Hkey = win32api.RegCreateKey(win32con.HKEY_CURRENT_USER, r'Control Panel\Desktop')
        win32api.RegSetValueEx(Hkey, 'WallPaper', 0, win32con.REG_SZ, r'C:\bing_wallpaper\wallpaper.png')
        win32api.RegCloseKey(Hkey)
        print(f"{Fore.GREEN}[✔]壁纸设置完成")


    data = response.json()


    image = data["images"][0]
    image_url = "https://cn.bing.com" + image["url"]
    title = image["title"]
    copyright = image["copyright"]
    quiz = "https://cn.bing.com" + image["quiz"]

    UHD_image_url='https://cn.bing.com' + image["url"].replace('1920x1080', 'UHD')
    ifupdate=""
    if h_update_v != VER:
        ifupdate=f"""-up\t下载新版本
    {Fore.YELLOW}有新版本，请更新！
    """
    print(f"""{Fore.GREEN}[✔]今日壁纸信息获取成功
    {Back.WHITE}{Fore.BLACK}图片URL(1080p): {image_url}
    图片URL(UHD最高请): {UHD_image_url}
    标题: {title}
    版权: {copyright}
    {Fore.RED}
    -----图片仅限用作桌面壁纸，禁止商用-----""")


    mode=input(f"""{Style.RESET_ALL}{Back.GREEN}选择模式:
    -d1080\t下载1080p图片至当前文件夹
    -duhd\t下载UHD最高请图片至当前文件夹
    -w1080\t设置1080p图片为壁纸
    -wuhd\t设置UHD最高请图片为壁纸
    {ifupdate}
    {Style.RESET_ALL}{Back.GREEN}输入命令选择：-""")
    if mode == "d1080" or mode == "-d1080":
        # download_img(image_url,f"{title}_{time.strftime("%Y-%m-%d", time.localtime())}.png")
        download(image_url,f"{title}_{time.strftime("%Y-%m-%d", time.localtime())}.png")
    elif mode == "w1080" or mode == "-w1080":
        import ctypes
        folder_name = r"C:\bing_wallpaper"
        if os.path.exists(folder_name):

            print(f"{Style.RESET_ALL}{Fore.YELLOW}[!]文件夹“{folder_name}”已创建过，跳过")
        else:
            
            os.mkdir(folder_name)
            print(f"{Style.RESET_ALL}{Fore.GREEN}[✔]新建文件夹“{folder_name}”成功")
        download(image_url,r"C:\bing_wallpaper\wallpaper.png")
        set_wallpaper()
    elif mode == "duhd" or mode == "-duhd":
        # download_img(image_url,f"{title}_{time.strftime("%Y-%m-%d", time.localtime())}.png")
        download(UHD_image_url,f"{title}_{time.strftime("%Y-%m-%d", time.localtime())}.png")
    elif mode == "wuhd" or mode == "-wuhd":
        import ctypes
        folder_name = r"C:\bing_wallpaper"
        if os.path.exists(folder_name):

            print(f"{Style.RESET_ALL}{Fore.YELLOW}[!]文件夹“{folder_name}”已创建过，跳过")
        else:
            
            os.mkdir(folder_name)
            print(f"{Style.RESET_ALL}{Fore.GREEN}[✔]新建文件夹“{folder_name}”成功")
        download(UHD_image_url,r"C:\bing_wallpaper\wallpaper.png")
        set_wallpaper()
    elif mode == "up" or mode == "-up":
        
        download(h_update_url,f"Bing壁纸 V{h_update_v}.exe")
        # print(f"{Style.RESET_ALL}{Fore.BLUE}[]重要！")
        
    else:
        print(f"{Style.RESET_ALL}{Fore.RED}[×]命令：“{mode}” 不存在")
    input('按下回车退出……')
except KeyboardInterrupt:
    print(f"\n{Style.RESET_ALL}{Fore.RED}[×]使用Ctrl+C强制退出")
    input('按下回车退出……')
except Exception as e:
    if e == "":
        print(f"\n{Style.RESET_ALL}{Fore.RED}[×]发生未知错误")
    print(f"\n{Style.RESET_ALL}{Fore.RED}[×]发生错误：{e}")
    input('按下回车退出……')


