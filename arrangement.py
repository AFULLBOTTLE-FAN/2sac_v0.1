#!/home/afullbottle/anaconda3/envs/obspy/bin/python
#!coding=utf-8

import obspy
import os
import shutil


root_dir = '/media/afullbottle/D9C3-CA83/obspy/test/' #改这里


for root, dirs, files in os.walk(root_dir):
    for file in files:


       
        if file.endswith('.gcf') and ('E' in file or 'N' in file or 'Z' in file )or file.endswith('.ref') or file.endswith('.miniseed'):

            
            file_path = os.path.join(root, file)

            
            rel_file_path = os.path.relpath(file_path,root_dir)
            
            dirs = rel_file_path.split('/')
            
            sub_folder_name = dirs[0]

            
            st = obspy.read(file_path)
            start_time = str(st[0].stats.starttime)
            end_time = str(st[0].stats.endtime)
            channel = str(st[0].stats.channel)

            starttime = start_time.replace(':', '-')
            endtime = end_time.replace(':', '-')

            
            folder_name = start_time[:10]
            folder_path = os.path.join(root_dir, 'Arrangement', sub_folder_name, folder_name)
            
            
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            
            
            shutil.copy(file_path, folder_path)
            
           
            new_file_path = os.path.join(folder_path, file)

            
            if file.endswith('.gcf'):
                new_file_name = "_".join([sub_folder_name, starttime, endtime, channel]) + '.gcf'
            elif file.endswith('.ref'):
                new_file_name = "_".join([sub_folder_name, starttime, endtime]) + '.ref'
            else:
                new_file_name = "_".join([sub_folder_name, starttime, endtime]) + '.miniseed'
            
            
            new_file_with_new_name_path = os.path.join(folder_path, new_file_name)
            
            
            os.rename(new_file_path, new_file_with_new_name_path)


