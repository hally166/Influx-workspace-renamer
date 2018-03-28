#Workspace renamer for BD Influx running Sortware v1.2.0.142
#v1.0 Jun 2017
#Python 3.6 (2017)
#Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk
#License : GPLv3 https://www.gnu.org/licenses/gpl-3.0.html

#This script renames all XML files in its folder and subfolders to the 'name' tag of the file.  
#DO NOT do this on your working workspace directory.  Make a copy of it and do it there

#import dependencies
import xml.etree.ElementTree as ET
import os
import random
import re
import time


for root, dirs, files in os.walk('.'):
 for name in files:
  if name.endswith(".xml"):
   r=(os.path.join(root, name))
   content = ET.parse (r)
   for locate in content.findall('Name'):
    workspace = locate.text
    try:
     os.rename(os.path.join(r), os.path.join(root,workspace+".xml"))
    except OSError:
      newname = re.sub(r'[\\/*?:"<>|]',"-",workspace)
      os.rename(os.path.join(r), os.path.join(root,newname+"_"+str(random.randrange(0,1000,1))+".xml"))
      print("Some files have been renamed to remove illegal characters and/or to prevent overwriting")
                        
print("Finished and closing")
time.sleep(2)
