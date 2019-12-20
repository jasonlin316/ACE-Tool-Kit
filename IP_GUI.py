import os
import ctypes
import tkinter as tk
from PIL import ImageTk, Image

taskbar=['calc','mspaint']

wall_p = []
wall_p.append("C:\\Users\\hsuang\\Documents\\GitHub\\Smart-Scenario-Detector\\wallpaper\\0.jpg")
wall_p.append("C:\\Users\\hsuang\\Documents\\GitHub\\Smart-Scenario-Detector\\wallpaper\\1.jpg")
wall_p.append("C:\\Users\\hsuang\\Documents\\GitHub\\Smart-Scenario-Detector\\wallpaper\\2.jpg")

apps = []

school = []
office = []
home   = []

office.append("mspaint.exe")
office.append("calc.exe") #skype
apps.append(office)

school.append("calc.exe")
school.append("EXCEL.EXE")
school.append("WINWORD.EXE")
apps.append(school)

home.append("WINWORD.EXE")
apps.append(home)

new_mode = 0
curr_mode = 0
           
cmd='cmd /c "'
def pin(new_mode): #pin
    global cmd
    for i in range(len(apps[new_mode])):
        cmd=cmd+'syspin "C:\Windows\\System32\\'+apps[new_mode][i]+'" 5386 '
        if i!=len(apps[new_mode])-1:
            cmd=cmd+'&& '
        else:
            cmd=cmd+'"'
    os.system(cmd)
    cmd = '' 

def unpin(curr_mode): #unpin
    global cmd
    for i in range(len(apps[curr_mode])):
        cmd=cmd+'syspin "C:\Windows\\System32\\'+apps[curr_mode][i]+'" 5387 '
        if i!=len(apps[curr_mode])-1:
            cmd=cmd+'&& '
        else:
            cmd=cmd+'"'
    os.system(cmd)
    cmd = '' 

#while True:
#    new_mode = input('enter mode:')
#
#    try:
#        new_mode = int(new_mode)
#    except ValueError:
#        break
#
#    if new_mode != curr_mode:
#        ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_p[new_mode] , 0) #change wall paper
#        unpin(curr_mode)
#        pin(new_mode)
#        
#    curr_mode = new_mode
    
def change(new_mode):
    global curr_mode
    if new_mode != curr_mode:
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_p[new_mode] , 0) #change wall paper
        unpin(curr_mode)
        pin(new_mode)
        
    curr_mode = new_mode

def mode0():
    change(0)
    
def mode1():
    change(1)
    
def mode2():
    change(2)

root = tk.Tk()
root.geometry('600x600')
#背景
canvas = tk.Canvas(root, width=600,height=600,bd=0, highlightthickness=0)
imgpath = 'tenor.gif'
img = Image.open(imgpath)
photo = ImageTk.PhotoImage(img)
 
canvas.create_image(300, 300, image=photo)
canvas.grid(column=0,row=0,columnspan=3)

img_png = tk.PhotoImage(file = '3.gif')
entry0=tk.Button(root,image=img_png,height=100,width=100,command=mode0)
entry0.grid(column=0,row=0)

entry1=tk.Button(root,image=img_png,height=100,width=100,command=mode1)
entry1.grid(column=1,row=0)

entry2=tk.Button(root,image=img_png,height=100,width=100,command=mode2)
entry2.grid(column=2,row=0)

#canvas.create_window(100, 50, width=100, height=20,window=entry)

root.mainloop()
