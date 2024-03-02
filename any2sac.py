#!/usr/bin/python
#!coding=utf-8

import os
from obspy import read
from obspy import Stream

st = Stream()

root_dir0 = '/media/afullbottle/D9C3-CA83/obspy/test/' #改这里
root_dir = os.path.join(root_dir0, 'Arrangement')


for root, dirs, files in os.walk(root_dir):
    if len(files) > 1:  
        print('Found directory:', root)  
        
        for filename in os.listdir(root):
            print(filename)

          
            sub_folder_name = os.path.relpath(root, root_dir)
            statsname = sub_folder_name.split('/')[0]
            
            st += read(os.path.join(root, filename))
            print('name', filename)
            

        st.merge(fill_value='interpolate')

        sac_file_path = os.path.join(root_dir0, 'SAC', statsname, '')
        print(sac_file_path)

        if not os.path.exists(sac_file_path):
            os.makedirs(sac_file_path)

    
        if len(st)>1:
            tr0 = st[0]
            tr1 = st[1]
            tr2 = st[2]

            tr0starttime = (str(tr0.stats.starttime)).replace(':', '-')
            tr0endtime = (str(tr0.stats.endtime)).replace(':', '-')
            fname0 = "%s_%s_%s_%s.SAC" % (statsname, tr0starttime, tr0endtime, tr0.stats.channel)
            tr0.write(sac_file_path + fname0, format="SAC")

            tr1starttime = (str(tr1.stats.starttime)).replace(':', '-')
            tr1endtime = (str(tr1.stats.endtime)).replace(':', '-')
            fname1 = "%s_%s_%s_%s.SAC" % (statsname, tr1starttime, tr1endtime, tr1.stats.channel)
            tr1.write(sac_file_path + fname1, format="SAC")

            tr2starttime = (str(tr2.stats.starttime)).replace(':', '-')
            tr2endtime = (str(tr2.stats.endtime)).replace(':', '-')
            fname2 = "%s_%s_%s_%s.SAC" % (statsname, tr2starttime, tr2endtime, tr2.stats.channel)
            tr2.write(sac_file_path + fname2, format="SAC")
        else:
            tr = st[0]

            trstarttime = (str(tr.stats.starttime)).replace(':', '-')
            trendtime = (str(tr.stats.endtime)).replace(':', '-')
            fname = "%s_%s_%s_%s.SAC" % (statsname, trstarttime, trendtime, tr.stats.channel)
            tr.write(sac_file_path + fname, format="SAC")  

        st = Stream()  
        

