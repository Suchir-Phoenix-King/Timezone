from tkinter import *
from PIL import ImageTk, Image
import pytz
import time

root = Tk()
root.title("Timezones")
root.geometry("600x600")
clock_image = ImageTk.PhotoImage(Image.open("clock.jpg"))
#-------------------------INDIA--------------------------
india_label = Label(root, text = "India")
india_label.place(relx = 0.2, rely = 0.05, anchor = CENTER)

india_clock = Label(root)
india_clock["image"] = clock_image
india_clock.place(relx = 0.2, rely = 0.35, anchor = CENTER)

india_time = Label(root)
india_time.place(relx = 0.2, rely = 0.65, anchor = CENTER)

#--------------------------USA---------------------------
us_label = Label(root, text = "USA")
us_label.place(relx = 0.7, rely = 0.05, anchor = CENTER)

us_clock = Label(root)
us_clock["image"] = clock_image
us_clock.place(relx = 0.7, rely = 0.35, anchor = CENTER)

us_time = Label(root)
us_time.place(relx = 0.7, rely = 0.65, anchor = CENTER)

#--------------------FUNCTIONS & CLASSES------------------
class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time["text"] = "Time: "+ current_time
        india_time.after(200, self.times)
        
class USA():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        us_time["text"] = "Time: "+ current_time
        us_time.after(200, self.times)
        
        
obj_india = India()
obj_usa = USA()
india_btn = Button(root, text = "SHOW TIME", command = obj_india.times)
india_btn.place(relx=0.2, rely = 0.8, anchor = CENTER)
usa_btn = Button(root, text = "SHOW TIME", command = obj_usa.times)
usa_btn.place(relx=0.7, rely = 0.8, anchor = CENTER)
root.mainloop()
