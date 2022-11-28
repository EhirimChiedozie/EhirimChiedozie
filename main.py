import os
import csv
import pandas

for file in os.listdir():
    if file.endswith('.csv'):
        with open(file,'r') as f:
            df = pandas.read_csv(file)
            csv_file = open(f'summary_{file}','w')
            csv_writer = csv.writer(csv_file)
            csv_headers = f.readlines(1)
            joint_headers = ''.join(csv_headers)
            split_list = joint_headers.split(',')
            csv_writer.writerow(['Field','Minimum','Maximum','Average'])
            csv_writer.writerow([split_list[0].replace('\n',''),min(df[df.columns[0]]),max(df[df.columns[0]]),sum(df[df.columns[0]])/len(df)])
            csv_writer.writerow([split_list[1].replace('\n',''),min(df[df.columns[1]]),max(df[df.columns[1]]),sum(df[df.columns[1]])/len(df)])
            csv_writer.writerow([split_list[1].replace('\n',''),min(df[df.columns[2]]),max(df[df.columns[2]]),sum(df[df.columns[2]])/len(df)])
            csv_file.close()