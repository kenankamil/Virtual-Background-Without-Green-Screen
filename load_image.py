import os
import tkinter
from PIL import Image
import tkinter.filedialog


def Root():          
    # filename = filedialog.askopenfilename(initialdir =  "/", title = "Select A File", filetype =
    # (("jpeg files","*.jpg"),("all files","*.*")) )
    
    Root = tkinter.Tk() # Create a Tkinter.Tk() instance
    Root.withdraw() # Hide the Tkinter.Tk() instance
    Default_dir = "C:\\" "file path"
    File_path = tkinter.filedialog.askopenfilename(title=u'select file', initialdir=(os.path.expanduser(Default_dir)))
    image = Image.open(File_path)
    return image




