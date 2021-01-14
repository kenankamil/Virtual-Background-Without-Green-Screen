from load_image import Root
import matplotlib.pyplot as plt
import cv2
import numpy as np
from PIL import Image
from import_model import MODEL
from class_model import label_to_color_image

    
def photobackground():
    background=Root();
    plt.imshow(background)
    plt.show()
    background = cv2.cvtColor(np.uint8(background), cv2.COLOR_BGR2RGB)
    background = cv2.resize(background, (428,513))

    
    back = np.copy(background)
    return back

def photo():
    image=Root();
    plt.imshow(image)
    plt.show()
    cv2_im = cv2.cvtColor(np.uint8(image), cv2.COLOR_BGR2RGB)

    pil_im = Image.fromarray(cv2_im)
    resized_im, seg_map = MODEL.run(pil_im)
    arr = np.asarray(seg_map)
    
    seg_image = label_to_color_image(seg_map).astype(np.uint8)
    seg_image = seg_image[:,:,0] > 100 
    seg_image = np.uint8(seg_image)*255
    seg_image = cv2.cvtColor(seg_image, cv2.COLOR_GRAY2BGR)
    seg_image = 255 - seg_image
    seg_image=cv2.resize(seg_image,(428,513))
    masked_image = cv2.resize(cv2_im, (428,513))
    masked_image[seg_image != 0] = 0
    return masked_image,seg_image


