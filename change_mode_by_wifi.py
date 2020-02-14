# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:52:14 2020

"""

import os
import sys
import imp
import ctypes


imp.reload(sys)

cur_wifi_name=''
past_wifi_name=''

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

def change(new_mode):
    global curr_mode
    if new_mode != curr_mode:
#        print(new_mode)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, wall_p[new_mode] , 0) #change wall paper
        unpin(curr_mode)
        pin(new_mode)
        
    curr_mode = new_mode

def select_wifi():
    global wifi_list,mode1_wifi,mode2_wifi,mode3_wifi,mode1,mode2,mode3
    wifi_list=[]
    
    pre_wifi=os.popen('netsh wlan show profiles').readlines()
    
    for j in range(len(pre_wifi)):
        if j>=9:
            past_wifi=pre_wifi[j].strip()
            past_wifi_name=past_wifi[23:]
            if past_wifi_name!='':
                wifi_list.append(past_wifi_name)
                print(j-8,".",past_wifi_name)
                
    mode1=int(input('Input Scenario mode 1：'))-1
    print('Scenario 1:', wifi_list[mode1])
    mode1_wifi=wifi_list[mode1]
    
    mode2=int(input('Input Scenario mode 2：'))-1
    print('Scenario 2:', wifi_list[mode2])
    mode2_wifi=wifi_list[mode2]
    
    mode3=int(input('Input Scenario mode 3：'))-1
    print('Scenario 3:', wifi_list[mode3])
    mode3_wifi=wifi_list[mode3]

def checkWIFI():
    global cur_wifi_name
    post_wifi=os.popen('netsh wlan show interfaces').readlines()
    
    if len(post_wifi)>13:
        cur_wifi=post_wifi[19].strip()
        cur_wifi_name=cur_wifi[25:]
#        print(cur_wifi_name)
    
    
            
#    print(wifi_list)
    
    
select_wifi()

while 1:
    checkWIFI()
    if cur_wifi_name!=past_wifi_name:
#        print('change')
        
        if cur_wifi_name==mode1_wifi:
#            print('go mode1')
            change(0)
        elif cur_wifi_name==mode2_wifi:
#            print('go mode2')
            change(1)
        elif cur_wifi_name==mode3_wifi:
#            print('go mode3')
            change(2)
            
        past_wifi_name=cur_wifi_name
        
#    else:
#        print('same')
        
#    if cur_wifi_name==mode1_wifi:
#        print('mode1')
#    elif cur_wifi_name==mode2_wifi:
#        print('mode2')
#    elif cur_wifi_name==mode3_wifi:
#        print('mode3')
    
    
    
    
    
    
