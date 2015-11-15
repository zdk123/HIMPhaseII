#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:38:21 2015

@author: Wenliang Zhao, wz927@nyu.edu

input: 1)text file contains all patient keywords
       2)text file contains paper information (c1:paper name; c2:journal name; c3: citation; c4:year; c5:evidence)
       3)folder contains all filtered keywords text (with "match")

output: input data without labels (input_data.txt) 
"""

import sys, glob, os, re

feature_file = sys.argv[1].strip()
paper_file = sys.argv[2].strip()
index_folder = sys.argv[3].strip()
input_file = "input_data.txt"

feature_list = []
with open(feature_file) as IN:
    for line in IN:
        if len(line):
            feature_list.append(line.strip().lower())
IN.close()

paper_list = []
with open(paper_file) as IN:
    for line in IN:
        if len(line):
            temp_list = line.strip().split("\t")
            temp_list = [x.strip().lower() for x in temp_list]
            paper_list.append(temp_list)
IN.close()

index_file_list = glob.glob(index_folder+"/*_match.txt")
OUT = open(input_file,'w')
k = 0
print "freature lisr: ", feature_list
for L in paper_list:
    if k == 0:
        k += 1
        continue
    paper_name = L[0]
    journal_name = L[1]
    year = 2015 - int(L[2])
    cite = int(L[3])
    preference = int(L[4])
    temp = [x for x in index_file_list if re.search(paper_name[:-4],x.lower())]
    print "current file is: ", paper_name
    temp_index_file = temp[0]
 
    if os.stat(temp_index_file).st_size == 0:
        for l in feature_list:
            OUT.write('0 ')
    else:
        temp_list = ['0'] * len(feature_list)
        with open(temp_index_file) as IND:
            for line in IND:
                line = line.strip()
                if line in feature_list:
                    temp_list[feature_list.index(line)] = '1'                
        for l in temp_list:
            OUT.write(l+" ")
    OUT.write(str(year)+" ")
    OUT.write(str(cite)+" ")
    OUT.write(str(preference))
    if k != len(paper_list):
        OUT.write("\n")
    k += 1 

OUT.close()

    
    


    
