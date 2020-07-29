#!/usr/bin/python3
import sys
import os
import pandas as pd

def get_size(path):
    total = 0
    for entry in os.scandir(path):
        try:
            if entry.is_dir(follow_symlinks=False):
                total += get_size(entry.path)
            else:
                total += entry.stat(follow_symlinks=False).st_size
        except Exception as e:
            print ("Exception: ", e)
            total += 0
        return total

#only use this if the script is to be run as a stand-alone script
if __name__ =='__main__':
    path = r"C:\Users\Kanupriya\Desktop"
    #Change path according to your requirement
    print("total arguments passed: ", len(sys.argv))

    directory = sys.argv[1] if len(sys.argv) >=2 else path
    
    usage = []
    paths = []
    for entry in os.scandir(directory):
        print (entry.path)
        if entry.is_dir(follow_symlinks=False):
            #print(entry.path + " is a directory")
            #print(get_size(entry.path))
            total = get_size(entry.path)
            print(total)
            paths.append(entry.path)
            usage.append(total)
        usage_dict = {'directory' : paths, 'usage' : usage}
        df = pd.DataFrame(usage_dict)
        print(df)
        df.to_csv("disk_home_usage.csv")
    
