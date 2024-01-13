import os
from colorama import init,Fore, Back, Style
init(autoreset=True)
try:
    print(f"{Style.RESET_ALL}{Fore.YELLOW}[!]更新模块启动")
    if os.path.exists("update_temp.exe") is not True:
        print(f"{Fore.RED}[×]更新失败，未检测到新版本文件")
    else:

        print(f"{Style.RESET_ALL}{Fore.YELLOW}[!]开始更新，请勿关闭更新模块！")
        os.remove("Bing壁纸.exe")
        print(f"{Style.RESET_ALL}{Fore.YELLOW}[!]更新中，请勿关闭更新模块！- 已删除旧版文件")
        os.rename("update_temp.exe","Bing壁纸.exe")
        print(f"{Style.RESET_ALL}{Fore.YELLOW}[!]更新中，请勿关闭更新模块！- 已配置新版文件")
        
        print(f"{Style.RESET_ALL}{Fore.GREEN}[✔]更新完成，即将启动新版本")
        os.system("Bing壁纸.exe")
except:
    print(f"{Style.RESET_ALL}{Fore.RED}[×]更新错误，请手动下载最新版！")
    