#!/usr/bin/python
#!coding=utf-8

#给ref的数据文件加上.ref的后缀方便读取
import os



root_folder_path = '/media/afullbottle/D9C3-CA83/obspy/test/' #改这里
print(root_folder_path)
folders = ['FJ12', 'FJ16'] #ref格式的数据台站文件夹名称

for folder in folders:
    folder_path = os.path.join(root_folder_path, folder)   
    print(folder_path)
    if not os.path.isdir(folder_path):
        continue 
    
    for root, dirs, files in os.walk(folder_path): 
        parent_dir = os.path.basename(root)
        
        if parent_dir == "1":   
            for file in files:
                if file.endswith(".ref"):  
                    continue
                file_path = os.path.join(root, file)  
                new_file_path = os.path.join(root, file + ".ref")   
                os.rename(file_path, new_file_path)

