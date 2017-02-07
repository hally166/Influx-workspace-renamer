#Copyright (c) 2017 Genome Research Ltd.

#Workspace renamer for BD Influx running Sortware v1.2.0.142
#v2.1 Jan 2017
#Python 3.5 (2016)
#Author : Christopher Hall, Wellcome Trust Sanger Institute, christopher.hall@sanger.ac.uk

#This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3 of the License, or (at your option) any later version.
#This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.


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
				except OSError as os.errno.ERROR_INVALID_NAME:
					newname = re.sub(r'[\\/*?:"<>|]',"-",workspace)
					os.rename(os.path.join(r), os.path.join(root,newname+"_"+str(random.randrange(0,1000,1))+".xml"))
					print("Some files have been renamed to remove illegal characters")
				except OSError as os.errno.ERROR_ALREADY_EXISTS:	
					os.rename(os.path.join(r), os.path.join(root,workspace+"_"+str(random.randrange(0,1000,1))+".xml"))
					print("Some files have been renamed to add a random number to prevent overwriting")
print("Finished and closing")
time.sleep(2)
