import customtkinter as ctk
import os
import subprocess
import tkinter as tk
import sys
from PIL import Image, ImageTk 
import tkinter.messagebox as msgbox


ctk.set_appearance_mode("Dark")


def terminate_process(process_name):
    subprocess.call([sys.executable, "combine_results.pyw"])
    answer = msgbox.askquestion("Stop", "Are you sure you want to Stop?\n IF you Stop and restart the program all data will be REMOVED...!")
    if answer == "yes":

        os.system(f"taskkill /f /im {process_name}.exe")
        window.destroy()

def launch_scripts():

    subprocess.call([sys.executable, "start.pyw"])
    subprocess.call([sys.executable, "Face_Recognition.pyw"])
#window
window = ctk.CTk()
# window.title("Attendance Application")
# Load the image using Pillow

window.geometry('600x600')


#frame
frame = ctk.CTkFrame(window,width=600,height= 600)
frame.pack(padx=100, pady=30)  # Adjust padx to make the frame wider

#frame.pack(padx = 50 , pady = 30)

# Customize the background color of the window
frame.tk_setPalette(background="#010E1E")  # Set your desired background color


#logo
image = Image.open("g302.png")
# Resize the image to your desired dimensions
new_width = 430
new_height = 430
image = image.resize((new_width, new_height), Image.LANCZOS)
photo = ImageTk.PhotoImage(image)

# Create a label widget to display the image
image_label = tk.Label(frame, image=photo,borderwidth=0)
image_label.pack()

# #label
# label = ctk.CTkLabel(frame , text = 'Attendance' , text_color = 'white' , fg_color = 'transparent',font = ('Harlow Solid Italic' , 50))
# label.pack()

w = 340
h = 40
font_settings = ('Arial Black', 16)  # Font settings for buttons

#Button Browse
button_browse = ctk.CTkButton(frame , width=w,height=h,font = font_settings,text = 'Select DataBase' , text_color = 'white' , hover_color = '#00F8F8', command =  lambda:subprocess.call([sys.executable, "Browse.pyw"]))
button_browse.pack(pady=15)


#Button1
button_1 = ctk.CTkButton(frame , width=w,height=h,font = font_settings,text = 'Start The Program' ,text_color = 'white' ,  fg_color='green',hover_color = '#00F8F8', command = lambda:subprocess.call([sys.executable, "Start.pyw"]))
button_1.pack(pady=15)



# #Button Face recognition
# button_FR = ctk.CTkButton(frame , width=w,height=h,font=font_settings,text = 'Face Recog' , text_color = 'white' ,  hover_color = '#00F8F8', command = lambda:subprocess.call([sys.executable, "Face_Recognition.pyw"]))
# button_FR.pack(pady=15)

#Button exit
button_exit = ctk.CTkButton(frame , width=w,height=h,font = font_settings,text = 'Stop' , text_color = 'white' ,fg_color='red',  hover_color = '#00F8F8', command = lambda:terminate_process("WNetWatcher"))
button_exit.pack(pady=15)

window.mainloop()


#button_2 = ctk.CTkButton(frame , text = 'Browse' , text_color = 'white' ,  hover_color = 'dodger blue', command =  lambda:subprocess.call("C:\Attendance\Code\Browse.pyw"))
