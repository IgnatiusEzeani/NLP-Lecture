# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 18:21:27 2021

@author: ezeani
"""


import os, random

def sample_data_points(n):
    _sample_pt = list(zip(random.sample(range(0, 999), n), n*['pos']))
    _sample_pt.extend(list(zip(random.sample(range(0, 999), n),n*['neg'])))
    random.shuffle(_sample_pt)
    return _sample_pt

# define folder structures
base_folder = os.path.join(".","movie_reviews")
pos_dir = os.path.join(base_folder,"pos")
neg_dir = os.path.join(base_folder,"neg")

# get review file names
pos_reviews, neg_reviews = os.listdir(pos_dir), os.listdir(neg_dir)

sample_points = sample_data_points(10)

with open("reformated_sample.tsv", "w", encoding="utf8") as datafile:
    for position, sentiment in sample_points:
        if sentiment == "pos":
            with open(os.path.join(pos_dir,pos_reviews[position]), "r",
                      encoding="utf8") as pos_file:
                text = " ".join(pos_file.read().split("\n")[:10])
                datafile.write(f"{text} \t positive\n")
        else:
            with open(os.path.join(neg_dir,neg_reviews[position]), "r", 
                      encoding="utf8") as neg_file:
                text = " ".join(neg_file.read().split("\n")[:10])
                datafile.write(f"{text} \t negative\n")