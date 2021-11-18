#!/usr/bin/env python
# coding: utf-8


import os,sys


old_type = input('Please tap in the suffix you want to change (e.g: .webm, .mp4, .avi, .ts):')
new_type = input('The suffix you want to change:')
old_names = os.listdir('./')

for name in old_names:
    l = len(old_type)
    if l <= 7:
        if name[-l:] == str(old_type):
            os.rename(str(name), str(name[:-l]) + str(new_type))
            print(str(name) +' has been already renamed')
