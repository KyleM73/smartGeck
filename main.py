# Write your code here :-)
import send
import read
import make_plots
import listen
import relay
import datetime
import time
import pandas as pd
import csv
import os
import glob

flag = True
new_file = False
danger_temp_high = 79
danger_temp_low = 65
data = {'Time':[],'Temperature':[],'Humidity':[]}
states = [0,0,0,0]

start_t = datetime.datetime.now()
current_path = os.path.dirname(os.path.realpath(__file__))
data_dir = 'data_logs'
print('Searching For Logs...')
data_path = os.path.join(current_path,data_dir)
all_data_files = glob.glob(data_path+'/*.csv')
if all_data_files and not new_file:
    print('Log Found!')
    file_name = max(all_data_files,key=os.path.getctime)
else:
    print('No Logs Found')
    fname = 'data_log_'+start_t.strftime('%m-%d-%Y_%H:%M')+'.csv'
    file_name = os.path.join(current_path,data_dir,fname)
    print('Creating File... ',file_name)
    with open(file_name, 'w') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(['Time','Temperature','Humidity'])

print('Running...')
running_avg_t = []
running_avg_h = []
while True:
    curr_t = datetime.datetime.now()
    states = relay.toggle(1)
    [te,hu] = read.read(False)
    running_avg_t.append(te)
    running_avg_h.append(hu)
    if curr_t.minute % 6 == 0:
        t = (sum(running_avg_t)-max(running_avg_t)-min(running_avg_t))/(len(running_avg_t)-2)
        h = (sum(running_avg_h)-max(running_avg_h)-min(running_avg_h))/(len(running_avg_h)-2)
        if not danger_temp_low < t < danger_temp_high or h < 45:
            msg_txt = 'WARNING: Temp: {:.02f}*F Humidity: {:.01f}%'.format(t,h)
            send.send_msg(msg_txt)
            make_plots.make_and_send_plots(True)
            
        data['Time'] = curr_t.strftime('%Y/%m/%d %H:%M')
        data['Temperature'] = [t]
        data['Humidity'] = [h]
        df = pd.DataFrame(data, columns=['Time','Temperature','Humidity'])
        df.set_index('Time',inplace=True)
        with open(file_name, 'a') as f:
            df.to_csv(f,mode='a',header=None)
    if curr_t.hour==0 and flag:
        make_plots.make_and_send_plots()
        flag = False
    if curr_t.hour==1:
        flag = True
    
    time.sleep(45)
    
