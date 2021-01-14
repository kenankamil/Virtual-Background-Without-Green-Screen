from kivy.app import App
from kivy.uix.button import Button
from Photo import photo,photobackground
from kivy.uix.gridlayout import GridLayout
import matplotlib.pyplot as plt
import cv2
from kivy.core.window import Window
from video import opencam
from kivy.graphics import Color

class ButtonApp(App):  
    global masked_image
    global seg_image
    global back
    def build(self):
       layout = GridLayout(cols = 3,padding = 250) #define number of columns  

       btnbackground = Button(text ="Load Background Image",
          font_size ="10sp")
       btnfront = Button(text ="Load Image",
          font_size ="10sp")
       btnprocess = Button(text ="Process Image",
          font_size ="10sp")
       btnexit = Button(text ="Exit App",
          font_size ="10sp")
       btnvideo = Button(text ="Open Cam",
          font_size ="10sp")
       
       # bind() use to bind the button to function callback
       btnbackground.bind(on_press = self.callbackback)
       btnfront.bind(on_press = self.callbackimage)
       btnprocess.bind(on_press = self.callbackprocess)
       btnexit.bind(on_press = self.exit)
       btnvideo.bind(on_press = self.videocam)
       
       #add button to layout
       layout.add_widget(btnbackground)
       layout.add_widget(btnfront)
       layout.add_widget(btnprocess)
       layout.add_widget(btnexit)
       layout.add_widget(btnvideo)

       return layout
   
    # functions called by button pressed
    def videocam(self,event):
        opencam()
        
    def exit(self, event):
        App.get_running_app().stop()
        Window.close()
   
    def callbackback(self, event):
       print("button pressed")
       global back
       back=photobackground()
    
    def callbackimage(self, event):
       print("button pressed")
       global masked_image
       global seg_image
       masked_image,seg_image=photo()
      
    def callbackprocess(self, event):
       print("button pressed")
       global masked_image
       global seg_image
       global back
       back[seg_image == 0] = 0
       #cv2.imshow("Image",masked_image+back)
       plt.imshow(cv2.cvtColor(masked_image+back, cv2.COLOR_BGR2RGB))
       plt.show()
    
      
# creating the object root for ButtonApp() class
root = ButtonApp()  
#run function runs the whole program.
root.run()

