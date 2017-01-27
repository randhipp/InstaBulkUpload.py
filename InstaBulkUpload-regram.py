#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

import os
import time
import random
import re
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

PhotoPath = "changePath" # Change Directory to Folder with Pics that you want to upload
IGUSER    = "changeUser" # Change to your Instagram USERNAME
PASSWD    = "changePass" # Change to your Instagram Password
IGCaption = "captionHere" 
# Change to your Photo Hashtag
hashtag   = "#hashtagHere"

os.chdir(PhotoPath)
ListFiles = [f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))]
print ("Start listing photo...\nTotal Photo in this folder:" + str (len(ListFiles)))

#Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER,PASSWD)
igapi.login() # login

for i in range(len(ListFiles)):
    photo = ListFiles[i]
	
    ext   = os.path.splitext(photo)[-1].lower()
    
    #Regex Filename to Create Username for Regram
    orig       = photo
    matchpat   = "---.*"
    replacepat = ""
    Regram     = re.sub(matchpat, replacepat, orig)
    #End Regex
        
    print ("Progress :" + str([i+1]) + " of " + str(len(ListFiles)))
    print ("Regram from : " + str(Regram))
    
    #check Extension for jpg
    if ext == ".jpg":
        print ("Now Uploading this photo to instagram: " + photo )
        igapi.uploadPhoto(photo, caption = "Regram from " + str(Regram) + "\n\n" + IGCaption + "\n\n" + hashtag ,upload_id=None)
    elif ext == ".mp4":
        print ("It's a VIDEO File!!\nSkipping for now" )
        #igapi.make_thumb(photo)
        #thumb = str(photo+"thumb.jpg")
        #igapi.uploadVideo(photo, thumb, caption = "Video Regram from " + str(Regram) + "\n\n" + IGCaption + "\n\n" + hashtag ,upload_id=None)
    
    # sleep for random between 60 - 120s
    n = randint(60,120)
    print ("Sleep upload for :" + str(n) + "seconds")
    time.sleep(n)
