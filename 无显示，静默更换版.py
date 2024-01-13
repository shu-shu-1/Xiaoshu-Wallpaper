
import os,requests,win32api,win32con,ctypes
s = requests.Session()
s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1788.0'})

def download(url: str, fname: str):
    resp = s.get(url, stream=True)

    
    with open(fname, "wb") as f:
        for chunk in resp.iter_content(chunk_size=512):
            f.write(chunk)
    # total = int(resp.headers.get('content-length', 0))
    # with open(fname, 'wb') as file, tqdm(
    #     desc=fname,
    #     total=total,
    #     unit='iB',
    #     unit_scale=True,
    #     unit_divisor=1024,
    # ) as bar:
    #     for data in resp.iter_content(chunk_size=1024):
    #         size = file.write(data)
    #         bar.update(size)


response = s.get("https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=zh-CN") 



def set_wallpaper(filelink):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, filelink, 0)
    Hkey = win32api.RegCreateKey(win32con.HKEY_CURRENT_USER, r'Control Panel\Desktop')
    win32api.RegSetValueEx(Hkey, 'WallPaper', 0, win32con.REG_SZ, filelink)
    win32api.RegCloseKey(Hkey)


data = response.json()
image = data["images"][0]
title = image["title"]
UHD_image_url='https://cn.bing.com' + image["url"].replace('1920x1080', 'UHD')


folder_name = r"C:\bing_wallpaper"
if os.path.exists(folder_name):
    pass

else:       
    os.mkdir(folder_name)
download(UHD_image_url,r"C:\bing_wallpaper\wallpaper.png")
set_wallpaper(r'C:\bing_wallpaper\wallpaper.png')

