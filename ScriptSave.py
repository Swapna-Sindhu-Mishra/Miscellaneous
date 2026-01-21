# -*- coding: utf-8 -*-
"""
Created on Thu May 23 15:06:36 2024

@author: SS Mishra
"""
import os
import shutil
import time
#copied_script_name = time.strftime("%Y%m%d-%H%M") + '_' + os.path.basename(__file__)
copied_script_name = time.strftime("%Y%m%d-%H%M") + '_' + 'Script_Original_Name.py'
shutil.copy(__file__, f'{folderpath}/{subfolder}' + os.path.sep + copied_script_name) 
