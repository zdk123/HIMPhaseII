#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 20:38:21 2015

@author: Wenliang Zhao, wz927@nyu.edu

input: folder contains all keywords files
output: folder contains all filtered keywords files
"""

import re,sys,glob,os

index_folder = sys.argv[1].strip()
index_filter_folder = index_folder + "_filter"
if not os.path.exists(index_filter_folder):
    os.makedirs(index_filter_folder)
index_file_list = glob.glob(index_folder+"/*.txt")

for f in index_file_list:
    f1 = os.path.basename(f)
    L = []
    dict_file = "LEXICON"
    with open(dict_file) as IN:
        for line in IN:
            if re.search("{base=",line):
                L.append(line.split("{base=")[1].strip().lower())
            if re.search("acronym_of=",line):
                L.append(line.split("acronym_of=")[1].split("|",1)[0].strip().lower())
    IN.close()

    match_file = index_filter_folder+"/"+f1[:-4]+"_match.txt" 
    unmatch_file = index_filter_folder+"/"+f1[:-4] + "_unmatch.txt"
    MT = open(match_file, 'w')
    UNMT = open(unmatch_file, 'w')
    with open(f) as IND:
        for line in IND:
            line = line.strip().lower()
            if line in L:
                MT.write(line+"\n")
            else:
                UNMT.write(line+"\n")

    IND.close()
    MT.close()
    UNMT.close()
