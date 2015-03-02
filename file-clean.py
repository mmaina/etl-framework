# -*- coding: utf-8 -*-
"""
Created on Wed Feb 25 10:19:32 2015

@author: Benedeta
"""

import pandas as pd
import os


def check_csv(f):
    
    filename,file_ext = os.path.splitext(f)
    if not file_ext =='.csv':
        print 'the file is not a csv'
    else:
       d = pd.read_csv(f,encoding="utf-16")
       return d
       
       
def data_correct(data):
    if data == None:
        return 'Data is empty'
        
    
    

    
    
    
if __name__=='__main__':
    
    filename='c:/project/ETHEB_20141128.csv'
    data = check_csv(filename)
    print data_correct(data)