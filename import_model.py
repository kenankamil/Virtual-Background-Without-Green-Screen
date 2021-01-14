import cv2
import numpy as np
import class_model
from load_image import Root

LABEL_NAMES = np.asarray([
  'person'
])

FULL_LABEL_MAP = np.arange(len(LABEL_NAMES)).reshape(len(LABEL_NAMES), 1)
FULL_COLOR_MAP = class_model.label_to_color_image(FULL_LABEL_MAP)

MODEL = class_model.DeepLabModel('deeplab_model.tar.gz')
print('model loaded successfully!')
def background():
    background=Root()
    background = cv2.cvtColor(np.uint8(background), cv2.COLOR_BGR2RGB)
    # Resizing image based on deeplab model 
    background = cv2.resize(background, (513,384))
    return background