# -*- coding: utf-8 -*-
"""
Created on Mon Feb 23 11:33:20 2015

@author: Benedeta
"""

import pandas as pd

def import_csv(f):
    d=pd.read_csv(f,encoding="utf-16")    
    return d
    
    
    
    
if __name__=='__main__':
    filename= 'files/csv/ETHOK_20141128.csv'
print import_csv(filename)
