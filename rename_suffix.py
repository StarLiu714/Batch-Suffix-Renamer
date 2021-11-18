#!/usr/bin/env python
# coding: utf-8


import os,sys


old_type = input('Please tap in the suffix you want to change (e.g: .webm, .mp4, .avi, .ts):')
new_type = input('The suffix you want to change:')
old_names = os.listdir('./')

for name in old_names:
    if len(old_type) == 5:
        if name[-5:] == str(old_type):
            os.rename(str(name), str(name[:-5]) + str(new_type))
            print(str(name) +' has been already renamed')
    elif len(old_type) == 4:
        if name[-4:] == str(old_type):
            os.rename(str(name), str(name[:-4]) + str(new_type))
            print(str(name) +' has been already renamed')
    elif len(old_type) == 3:
        if name[-3:] == str(old_type):
            os.rename(str(name), str(name[:-3]) + str(new_type))
            print(str(name) +' has been already renamed')
    elif len(old_type) == 2:
        if name[-2:] == str(old_type):
            os.rename(str(name), str(name[:-2]) + str(new_type))
            print(str(name) +' has been already renamed')

