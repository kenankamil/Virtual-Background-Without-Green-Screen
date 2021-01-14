import cv2
import numpy as np
from PIL import Image
from import_model import MODEL
from class_model import label_to_color_image
from import_model import background

def opencam():
    
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    background_=background()
    
    while True:
        ret, frame = cap.read()
        
        if ret:
            cv2_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_im = Image.fromarray(cv2_im)
            
            resized_im, seg_map = MODEL.run(pil_im)
            arr = np.asarray(seg_map)
            
            seg_image = label_to_color_image(seg_map).astype(np.uint8)
            seg_image = seg_image[:,:,0] > 100 
            seg_image = np.uint8(seg_image)*255
            seg_image = cv2.cvtColor(seg_image, cv2.COLOR_GRAY2BGR)
            seg_image = 255 - seg_image
            back = np.copy(background_)
    
            masked_image = cv2.resize(frame, (513,384))
            masked_image[seg_image != 0] = 0
      
            back[seg_image == 0] = 0
            cv2.imshow("Virtual Background Project",masked_image+back)
    
            if(cv2.waitKey(1)==27):
                break
    
        else:
            break
    
    cv2.destroyAllWindows()
    cap.release()













