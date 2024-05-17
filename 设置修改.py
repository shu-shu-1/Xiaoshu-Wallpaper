from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttk
import json,os,shutil,ctypes,sys,re
from tkinter import filedialog
# cosmo - flatly - journal - literal - lumen - minty - pulse - sandstone - united - yeti（浅色主题）
# cyborg - darkly - solar - superhero（深色主题）
def convert_path(path):
    # 使用正则表达式匹配路径格式
    new_path = re.sub(r'[\\/]', r'\\', path)
    return new_path
def is_admin():
    try:
        # return 1
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        messagebox.showerror("错误", "获取管理员身份出错")
if is_admin():
    with open('./data/style.json',encoding="utf-8") as f:
        style_settings = json.loads(f.read())
    root = tk.Tk()
    style = ttk.Style(style_settings["theme"])
    root.iconbitmap("./icon/icon.ico")
    root.title("小树壁纸 | 修改配置")
    # root.geometry("500x500")
    with open('./data/settings.json',encoding="utf-8") as f:
        settings = json.loads(f.read())
    msg=ttk.Label(root,text="修改配置",font=("微软雅黑",15))
    msg.grid()
    # 创建一个IntVar对象
    check_var = ttk.IntVar()
    update_l=ttk.Label(text="更新检查：")
    update_l.grid(row=1, column=0, sticky="w")
    def update_check():
        settings["check_update"] = check_var.get()
        with open('./data/settings.json', 'w',encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
    update_c=ttk.Checkbutton(bootstyle="round-toggle", variable=check_var,command=update_check)
    if settings["check_update"]:
        check_var.set(1)
    update_c.grid(row=1, column=1, sticky="w")
    bing_var = ttk.IntVar()
    bing_l=ttk.Label(text="Bing每日开机自动更换：")
    bing_l.grid(row=2, column=0, sticky="w")
    def bing_check():

        if bing_var.get():
            if os.path.exists(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bing_auto_run.exe") is not True:
                shutil.copy("./app/bing_auto_run.exe",r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        else:
            if os.path.exists(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bing_auto_run.exe"):
                os.remove(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bing_auto_run.exe")
        settings["bing_auto_start"] = bing_var.get()    
        with open('./data/settings.json', 'w',encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
    bing_c=ttk.Checkbutton(bootstyle="round-toggle", variable=bing_var,command=bing_check)
    if settings["bing_auto_start"]:
        bing_var.set(1)
    bing_c.grid(row=2, column=1, sticky="w")
    pic_time_l=ttk.Label(text="壁纸切换间隔(秒)：")
    pic_time_l.grid(row=3, column=0, sticky="w")
    pic_time_e=ttk.Entry(width=50)
    pic_time_e.grid(row=3, column=1, sticky="w")
    pic_time_e.insert(0,settings["pic_time"])
    def pic_time():
        settings["pic_time"] = int(pic_time_e.get())
        with open('./data/settings.json', 'w',encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
    pic_time_b=ttk.Button(text="确定",command=pic_time)
    pic_time_b.grid(row=3, column=2, sticky="w")

    pic_save_l=ttk.Label(text="壁纸文件保存路径(如果为空将使用系统图片目录)：")
    pic_save_l.grid(row=4, column=0, sticky="w")
    pic_save_e=ttk.Entry(width=50)
    pic_save_e.grid(row=4, column=1, sticky="w")
    pic_save_e.insert(0,settings["Pictures_save_path"])
    def save_time():
        settings["Pictures_save_path"] = convert_path(pic_save_e.get())
        with open('./data/settings.json', 'w',encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
    pic_time_b=ttk.Button(text="确定",command=save_time)
    pic_time_b.grid(row=4, column=2, sticky="w")
    def browse_folder():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            # 更新输入框和设置
            pic_save_e.delete(0, tk.END)
            pic_save_e.insert(0, folder_selected)
            settings["Pictures_save_path"] = folder_selected
    browse_button = ttk.Button(text="浏览", command=browse_folder)
    browse_button.grid(row=4, column=3, sticky="w")

    # 创建一个IntVar对象
    def update_channel_save():
        settings["update_channel"] = update_channel.get()
        with open('./data/settings.json', 'w',encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=4)
    update_channel = ttk.StringVar()
    update_channel.set(settings["update_channel"])
    update_channel_l=ttk.Label(text="更新渠道：")
    update_channel_l.grid(row=5, column=0, sticky="w")
    update_channel_c=ttk.Radiobutton(text="正式版", variable=update_channel, value="release", command=update_channel_save)
    update_channel_c.grid(row=5, column=1, sticky="w")
    update_channel_c=ttk.Radiobutton(text="测试版", variable=update_channel, value="beta", command=update_channel_save)
    update_channel_c.grid(row=5, column=2, sticky="w")
    # update_channel_c=ttk.Radiobutton(text="内部测试版", variable=update_channel, value="internal")
    # update_channel_c.grid(row=4, column=3, sticky="w")

    # update_channel_b=ttk.Button(text="确定",command=update_channel_save)
    # update_channel_b.grid(row=4, column=4, sticky="w")
    # print(new_settings)

    root.mainloop()
else:
    # 以管理员权限重新运行程序
    ctypes.windll.shell32.ShellExecuteW(None,"runas", sys.executable, __file__, None, 1)
