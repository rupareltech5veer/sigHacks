import tf_example as md

# import the opencv library 
import cv2

#import numpy as np
from PIL import Image
import time

#webhook materials
import requests 
  
# defining the api-endpoint  
API_ENDPOINT = ""

#vol up + down on computer imports for pycow
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math


# define a video capture object 
vid = cv2.VideoCapture(0)
counter = 0
while(True): 
      
    # Capture the video frame 
    # by frame 
    t_end = time.time() + 7
    #while time.time() < t_end:
    ret, image = vid.read()
    cv2.imshow('frame', image)
    #if(time.time()>= t_end):
    outputs = md.predictImage(Image.fromarray(image, 'RGB'))

    if outputs['Prediction']=='Light On':
        #send webhook to ifttt for light on
        #setting the api-detail
        API_ENDPOINT = "https://maker.ifttt.com/trigger/Light_On/with/key/cSS9mVWwj0JTDMNFp4MmSb"
        # sending post request and saving response as response object 
        requests.post(url = API_ENDPOINT)

    if outputs['Prediction']=='Light Off':
        #send webhook to ifttt for light off
        #setting the api-detail
        API_ENDPOINT = "https://maker.ifttt.com/trigger/Light_Off/with/key/cSS9mVWwj0JTDMNFp4MmSb"
        # sending post request and saving response as response object 
        requests.post(url = API_ENDPOINT)
        
    if outputs['Prediction']=='TV On':
        #send webhook to ifttt for light on
        #setting the api-detail
        API_ENDPOINT = "https://maker.ifttt.com/trigger/Tv_On/with/key/bKSRo51H7vnD0zjYNyMEuAKwnPH1fuwD5hJE08Y-VSf"
        # sending post request and saving response as response object 
        requests.post(url = API_ENDPOINT)

    if outputs['Prediction']=='TV Off':
        #send webhook to ifttt for light off
        #setting the api-detail
        API_ENDPOINT = "https://maker.ifttt.com/trigger/Tv_Off/with/key/bKSRo51H7vnD0zjYNyMEuAKwnPH1fuwD5hJE08Y-VSf"
        # sending post request and saving response as response object 
        requests.post(url = API_ENDPOINT)

    if outputs['Prediction']=='Emergency':
        #send webhook to ifttt for light off
        #setting the api-detail
        API_ENDPOINT = "https://maker.ifttt.com/trigger/Emergency/with/key/bKSRo51H7vnD0zjYNyMEuAKwnPH1fuwD5hJE08Y-VSf"
        # sending post request and saving response as response object 
        requests.post(url = API_ENDPOINT)

    # Get default audio device using PyCAW
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))


    if outputs['Prediction']=='Volume Up':
        # Get current volume 
        currentVolumeDb = volume.GetMasterVolumeLevel() 
        volume.SetMasterVolumeLevel(currentVolumeDb + 15.00, None)
        # NOTE: -10.25 dB = half volume !

    if outputs['Prediction']=='Volume Down':
        print("Volummmme DownDownDown")
        # Get current volume 
        currentVolumeDb = volume.GetMasterVolumeLevel()
        volume.SetMasterVolumeLevel(currentVolumeDb - 15.00, None)
        # NOTE: -10.25 dB = half volume !
        
    t_end = time.time() + 7
    #time.sleep(2)
    #print('Next')
    #image = np.fromstring(frame.getvalue(), dtype='uint8')
    # Display the resulting frame 
    #cv2.imshow('frame', image)

    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('s'):
        #cv2.imwrite(frame,frame)
        #md.predictImage(Image.fromarray(image, 'RGB'))
        print(image)

# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 
