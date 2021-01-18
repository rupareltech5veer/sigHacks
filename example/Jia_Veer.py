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
        API_ENDPOINT = "https://maker.ifttt.com/trigger/Tv_Off/with/key/bKSRo51H7vnD0zjYNyMEuAKwnPH1fuwD5hJE08Y-VSf"
        # sending post request and saving response as response object 
        requests.post(url = API_ENDPOINT)
        
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
