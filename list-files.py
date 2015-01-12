#!/usr/bin/env python

import piggyphoto
from pprint import pprint
C = piggyphoto.camera()

def folder_recurse(folder_path, depth=0):
    folders = C.list_folders(folder_path)
    if folders:
        for folder in folders:
            if folder:
                print ' ' * depth, folder[0]
                folder_recurse(folder_path + folder[0] +'/', depth+1)
    else:
        files = C.list_files(folder_path)
        for f in files:
            print ' ' * depth, '|->', "%s%s" % (folder_path, f[0])

folder_recurse("/")
