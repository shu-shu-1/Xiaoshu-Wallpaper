from tkinter import messagebox
import tkinter as tk
import ttkbootstrap as ttk
import json5, os, shutil, ctypes, sys, re
from tkinter import filedialog

def convert_path(path):
    new_path = re.sub(r'[\\/]', r'\\', path)
    return new_path

def is_admin():
    try:
        # return 1
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        messagebox.showerror("错误", "获取管理员身份出错")

if is_admin():
    with open('./data/style.json5', encoding="utf-8") as f:
        style_settings = json5.loads(f.read())

    root = tk.Tk()
    style = ttk.Style(style_settings["theme"])
    root.iconbitmap("./icon/setting.ico")
    root.title("小树壁纸 | 修改配置")
    root.geometry("1050x650")  # 设置窗口大小

    with open('./data/settings.json5', encoding="utf-8") as f:
        settings = json5.loads(f.read())
    # -----高dpi适配
    if (settings["dpi_fix"]):
    #告诉操作系统使用程序自身的dpi适配
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
        #获取屏幕的缩放因子
        ScaleFactor=ctypes.windll.shcore.GetScaleFactorForDevice(0)
        #设置程序缩放
        root.tk.call('tk', 'scaling', ScaleFactor/settings["dpi_fix_size"])
    def save_json(file, data):
        with open(file, 'w', encoding="utf-8") as f:
            json5.dump(data, f, ensure_ascii=False, indent=4)

    notebook = ttk.Notebook(root, width=1000, height=600)
    notebook.pack(pady=10, expand=True)

    frame_general = ttk.Frame(notebook, width=1000, height=600)
    frame_update = ttk.Frame(notebook, width=1000, height=600)
    frame_theme = ttk.Frame(notebook, width=1000, height=600)
    frame_display = ttk.Frame(notebook, width=1000, height=600)
    frame_test = ttk.Frame(notebook, width=1000, height=600)


    frame_general.pack(fill='both', expand=True)
    frame_update.pack(fill='both', expand=True)
    frame_theme.pack(fill='both', expand=True)
    frame_display.pack(fill='both', expand=True)
    frame_test.pack(fill='both', expand=True)


    notebook.add(frame_general, text="常规设置")
    notebook.add(frame_update, text="更新设置")
    notebook.add(frame_theme, text="主题设置")
    notebook.add(frame_display, text="显示设置")
    notebook.add(frame_test, text="预览设置项")


    # 常规设置
    msg = ttk.Label(frame_general, text="常规设置", font=("微软雅黑", 15))
    msg.grid(columnspan=3, pady=10)
    msg1 = ttk.Label(frame_update, text="更新设置", font=("微软雅黑", 15))
    msg1.grid(columnspan=3, pady=10)
    msg3 = ttk.Label(frame_theme, text="主题设置", font=("微软雅黑", 15))
    msg3.grid(columnspan=3, pady=10)
    msg4 = ttk.Label(frame_display, text="显示设置", font=("微软雅黑", 15))
    msg4.grid(columnspan=3, pady=10)
    msg5 = ttk.Label(frame_test, text="预览设置项", font=("微软雅黑", 15))
    msg5.grid(columnspan=3, pady=10)



    def bing_check():
        if bing_var.get():
            if not os.path.exists(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bing_auto_run.exe"):
                shutil.copy("./app/bing_auto_run.exe", r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup")
        else:
            if os.path.exists(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bing_auto_run.exe"):
                os.remove(r"C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\bing_auto_run.exe")
        settings["bing_auto_start"] = bing_var.get()
        save_json('./data/settings.json5', settings)

    bing_var = ttk.IntVar(value=settings["bing_auto_start"])
    bing_l = ttk.Label(frame_general, text="Bing每日开机自动更换：")
    bing_l.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    bing_c = ttk.Checkbutton(frame_general, bootstyle="round-toggle", variable=bing_var, command=bing_check)
    bing_c.grid(row=1, column=1, sticky="w", padx=10, pady=5)

    def pic_time():
        settings["pic_time"] = int(pic_time_e.get())
        save_json('./data/settings.json5', settings)

    pic_time_l = ttk.Label(frame_general, text="壁纸切换间隔(秒)：")
    pic_time_l.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    pic_time_e = ttk.Entry(frame_general, width=10)
    pic_time_e.grid(row=2, column=1, sticky="w", padx=10, pady=5)
    pic_time_e.insert(0, settings["pic_time"])
    pic_time_b = ttk.Button(frame_general, text="确定", command=pic_time)
    pic_time_b.grid(row=2, column=2, sticky="w", padx=10, pady=5)

    def save_time():
        settings["Pictures_save_path"] = convert_path(pic_save_e.get())
        save_json('./data/settings.json5', settings)

    pic_save_l = ttk.Label(frame_general, text="壁纸文件保存路径(如果为空将使用系统图片目录)：")
    pic_save_l.grid(row=3, column=0, sticky="w", padx=10, pady=5)
    pic_save_e = ttk.Entry(frame_general, width=50)
    pic_save_e.grid(row=3, column=1, sticky="w", padx=10, pady=5)
    pic_save_e.insert(0, settings["Pictures_save_path"])
    pic_save_b = ttk.Button(frame_general, text="确定", command=save_time)
    pic_save_b.grid(row=3, column=2, sticky="w", padx=10, pady=5)

    def browse_folder():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            pic_save_e.delete(0, tk.END)
            pic_save_e.insert(0, folder_selected)
            settings["Pictures_save_path"] = folder_selected
            save_json('./data/settings.json5', settings)

    browse_button = ttk.Button(frame_general, text="浏览", command=browse_folder)
    browse_button.grid(row=3, column=3, sticky="w", padx=10, pady=5)


    # 更新设置

    def update_check():
        settings["check_update"] = check_var.get()
        save_json('./data/settings.json5', settings)

    check_var = ttk.IntVar(value=settings["check_update"])
    update_l = ttk.Label(frame_update, text="更新检查：")
    update_l.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    update_c = ttk.Checkbutton(frame_update, bootstyle="round-toggle", variable=check_var, command=update_check)
    update_c.grid(row=1, column=1, sticky="w")



    def update_channel_save():
        settings["update_channel"] = update_channel.get()
        save_json('./data/settings.json5', settings)

    update_channel = ttk.StringVar(value=settings["update_channel"])
    update_channel_l = ttk.Label(frame_update, text="更新渠道：")
    update_channel_l.grid(row=2, column=0, sticky="w", padx=10, pady=5)
    update_channel_c1 = ttk.Radiobutton(frame_update, text="正式版", variable=update_channel, value="release", command=update_channel_save)
    update_channel_c1.grid(row=2, column=1, sticky="w", padx=10, pady=5)
    update_channel_c2 = ttk.Radiobutton(frame_update, text="测试版", variable=update_channel, value="beta", command=update_channel_save)
    update_channel_c2.grid(row=2, column=2, sticky="w", padx=10, pady=5)



    # 主题设置
    def select_source():
        style_settings["theme"] = var1.get()
        save_json('./data/style.json5', style_settings)
        style.theme_use(style_settings["theme"])

    var1 = ttk.StringVar(value=style_settings["theme"])
    ll = ttk.Label(frame_theme, text="主题：")
    ll.grid(row=1, column=0, sticky="w", padx=10, pady=5)
    theme = ttk.Combobox(frame_theme, values=['cosmo', 'flatly', 'litera', 'minty', 'lumen', 'sandstone', 'yeti', 'pulse', 'united', 'morph', 'journal', 'darkly', 'superhero', 'solar', 'cyborg', 'vapor', 'simplex', 'cerculean'], textvariable=var1)
    theme.grid(row=1, column=1, sticky="w", padx=10, pady=5)
    theme.bind("<<ComboboxSelected>>", lambda event: select_source())

    def save_time1():
        style_settings["pic"] = convert_path(pic_save_e1.get())
        save_json('./data/style.json5', style_settings)
        messagebox.showinfo("成功","设置成功，重启生效")
    if (settings["in_test"]):
        pic_save_l1 = ttk.Label(frame_theme, text="主界面背景图片(如果为空将禁用)：")
        pic_save_l1.grid(row=2, column=0, sticky="w", padx=10, pady=5)
        pic_save_e1 = ttk.Entry(frame_theme, width=50)
        pic_save_e1.grid(row=2, column=1, sticky="w", padx=10, pady=5)
        pic_save_e1.insert(0, style_settings["pic"])
        pic_save_b1 = ttk.Button(frame_theme, text="确定", command=save_time1)
        pic_save_b1.grid(row=2, column=2, sticky="w", padx=10, pady=5)

        def browse_file():
            folder_selected = filedialog.askopenfilename(filetypes=[('图片文件', ('.jpg', '.png', '.jpeg'))])
            if folder_selected:
                pic_save_e1.delete(0, tk.END)
                pic_save_e1.insert(0, folder_selected)
                style_settings["pic"] = folder_selected
                save_json('./data/style.json5', style_settings)

        browse_button1 = ttk.Button(frame_theme, text="浏览", command=browse_file)
        browse_button1.grid(row=2, column=3, sticky="w", padx=10, pady=5)

    # 显示设置
    def dpi_fix():
        settings["dpi_fix"] = dpi_var.get()
        save_json('./data/settings.json5', settings)
        messagebox.showinfo("成功","设置成功，重启生效")
    dpi_var = ttk.IntVar(value=settings["dpi_fix"])
    dpi_m=ttk.Label(frame_display,text="高DPI适配:")
    dpi_m.grid(column=0,row=1)
    dpi1=ttk.Checkbutton(frame_display, bootstyle="round-toggle", variable=dpi_var, command=dpi_fix)
    dpi1.grid(column=1,row=1)
    def dpi_fix2():
        try:
            if 150 > dpi2_var.get() > 20:
                settings["dpi_fix_size"] = dpi2_var.get()
                save_json('./data/settings.json5', settings)
                if settings["dpi_fix"]:
                    messagebox.showinfo("成功","设置成功，重启生效")
            else:
                messagebox.showerror("错误","你仅能输入范围20~150的整数")
        except:
            messagebox.showerror("错误","你仅能输入整数")
    dpi2_m=ttk.Label(frame_display,text="DPI缩放因子处理值，值越大界面越小(范围20~150的整数):")
    dpi2_m.grid(column=0,row=2,columnspan=3)
    dpi2_var = ttk.IntVar(value=settings["dpi_fix_size"])
    dpi2=ttk.Entry(frame_display,textvariable=dpi2_var)
    dpi2.grid(column=4,row=2)
    dpi2_b=ttk.Button(frame_display,text="确定",command=dpi_fix2)
    dpi2_b.grid(column=5,row=2)
    # 预览设置项
    def vie_fix():
        settings["in_test"] = vie_var.get()
        save_json('./data/settings.json5', settings)
        messagebox.showinfo("成功","设置成功，重启生效")
    vie_var = ttk.IntVar(value=settings["in_test"])
    vie_m=ttk.Label(frame_test,text="是否启用未经验证的预览设置项:")
    vie_m.grid(column=0,row=1,columnspan=2)
    vie1=ttk.Checkbutton(frame_test, bootstyle="round-toggle", variable=vie_var, command=vie_fix)
    vie1.grid(column=2,row=1)


    root.mainloop()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
