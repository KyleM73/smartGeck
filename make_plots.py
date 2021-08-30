# Write your code here :-)
import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from datetime import datetime, timedelta
from collections import deque
import send

def make_and_send_plots(requested=False):
    
    current_path = os.path.dirname(os.path.realpath(__file__))
    data_dir = 'data_logs'
    img_dir = 'daily_plots'
    file_path = os.path.join(current_path,data_dir)
    img_name = 'daily_log_'+datetime.strftime(datetime.now()-timedelta(1),'%m-%d-%Y')+'.png'
    req_img_name = img_name = 'daily_log_'+datetime.strftime(datetime.now(),'%m-%d-%Y')+'.png'
    
    if requested:
        new_dir = os.path.join(current_path,img_dir,datetime.strftime(datetime.now(),'%m-%d-%Y'))
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
    else:
        new_dir = os.path.join(current_path,img_dir,datetime.strftime(datetime.now()-timedelta(1),'%m-%d-%Y'))
        if not os.path.exists(new_dir):
            os.mkdir(new_dir)
    
    fname_img = os.path.join(new_dir,img_name)
    req_fname = os.path.join(new_dir,'requested_'+req_img_name)

    
    
    all_files = glob.glob(file_path+'/*')
    fname = max(all_files,key=os.path.getctime)
    
    with open(fname,'rb') as f:
        lines = deque(f,240)
    num_lines = sum(1 for row in lines)
    data = np.genfromtxt(lines,delimiter=',',names=['Time','Temperature','Humidity'])
    y_temp = data['Temperature']
    y_humid = data['Humidity']
    if num_lines < 240:
        y_temp = np.concatenate((np.zeros((240-num_lines,)),y_temp))
        y_humid = np.concatenate((np.zeros((240-num_lines,)),y_humid))
           
    fig,ax = plt.subplots()
    #data['Time'] -> see datetime.datetime.strptime(time,format)
    x = np.linspace(0,24,num=240)
    temp = ax.plot(x,y_temp,linewidth=2,label='Temperature ($^\circ$F)')
    humid = ax.plot(x,y_humid,linewidth=2,label='% Humidity')
    ax.legend(loc='lower right')
    ax.set_xlabel('Time')
    ax.set_xlim(0,24)
    ax.set_ylim(0,100)
    ax.xaxis.set_ticks(np.arange(0,24,4))
    if requested:
        ax.set_title('Daily Logs Requested on '+datetime.strftime(datetime.now(),'%m-%d-%Y %H:%M'))
        fig.savefig(req_fname)
        send.send_img(req_fname)
    else:
        ax.set_title('Daily Logs on '+datetime.strftime(datetime.now()-timedelta(1),'%m-%d-%Y'))
        fig.savefig(fname_img)
        send.send_img(fname_img)
    
