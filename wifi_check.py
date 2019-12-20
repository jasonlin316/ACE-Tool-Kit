# coding=utf-8
#Environment: python3.7
import os
import sys
import imp
imp.reload(sys)

list=[]
sel1=0
sel2=0
sel3=0

def checkWIFI():

	#loop const
	pre_count=0
	post_count=0
	num=1
	temp_list=[]

	# wifi_list:SSID名稱 , sel_mode: Scenario選擇
	wifi_list=[]
	sel_mode1=0
	sel_mode2=0
	sel_mode3=0


	#當前wifi資訊
	pre_wifi = os.popen('netsh wlan show profiles').readlines()
	#print(pre_wifi)
	#曾使用過的wifi資訊
	post_wifi = os.popen('netsh wlan show interfaces').readlines()

	print('=============================')	
	for i in post_wifi:
		if post_count==19:
			post_result = i.strip()
			print('當前連接的wifi為:\n1. ', post_result[22:])
			wifi_list.append(post_result[22:])

		post_count=post_count+1		
	
	print('曾連接之wifi:')	
	for j in pre_wifi:
		pre_result = j.strip()
		if pre_result.find(u"所有使用者配置檔案 : ") :
			if pre_count>9:
				print(num+1,".",pre_result[11:])
				num=num+1
				temp_list=pre_result[11:]
				temp_list.strip().lstrip().rstrip(',')
				wifi_list.append(temp_list) 

		pre_count=pre_count+1

	#select Secnario
	s1 = input('Input Secnario mode 1：')
	sel_mode1=int(s1)
	sel_mode1=sel_mode1-1
	print('Secnario 1:', wifi_list[sel_mode1])

	s2 = input('Input Secnario mode 2：')
	sel_mode2=int(s2)
	sel_mode2=sel_mode2-1
	print('Secnario 2:', wifi_list[sel_mode2])

	s3 = input('Input Secnario mode 3：')
	sel_mode3=int(s3)
	sel_mode3=sel_mode3-1
	print('Secnario 3:', wifi_list[sel_mode3])

	
	return wifi_list,sel_mode1,sel_mode2,sel_mode3



list,sel1,sel2,sel3 = checkWIFI()

print(list,"\n")
print(sel1,sel2,sel3)