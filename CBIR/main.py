import numpy as np
import cv2
import tkinter as tk
from PIL import Image, ImageTk


class Application(tk.Frame):

    def __init__(self, master, photo_frame_size, width, height, side_menu_width, bg_img_path, query_btn_width):

        super().__init__(master)

        self.master = master
        self.photo_frame_size = photo_frame_size
        self.width = width
        self.height = height
        self.side_menu_width = side_menu_width
        self.bg_img_path = bg_img_path
        self.query_btn_width = query_btn_width

        self.pack()
        self.create_ui_widgets()    
        


        
    def create_ui_widgets(self):

        canvas = tk.Canvas(width = self.width, height = self.height,  bg = "#EADEDA")      
        canvas.place(x = 0, y = 0)
        
        
                    
                           
        #--------------background image ---------------------
                           
        image = Image.open(self.bg_img_path)
        image = image.resize((self.width - self.side_menu_width, self.height), Image.ANTIALIAS)
        bg_image = ImageTk.PhotoImage(image)
        self.background_label = tk.Label(image = bg_image)
        self.background_label.place(x = 0, y = 0, width = self.width - self.side_menu_width, height = self.height)
        self.background_label.image = bg_image
        

        #-------------search and feedback buttons------------
        
        self.search_btn = tk.Button(text = "Search",command = self.search_command , state=tk.DISABLED)
        self.search_btn.place(x=1000, y=600, width = self.query_btn_width)
        
        self.feedback_btn = tk.Button(text = "Feedback",command = self.feedback_command , state=tk.DISABLED)
        self.feedback_btn.place(x=1200, y=600,width = self.query_btn_width)
        
        #------------query image and browse button-----------        
        self.label_Query_img = tk.Label(borderwidth=2, relief="groove", bg="white")
        self.label_Query_img.place(x = 1450 , y = 40 , width = self.photo_frame_size , height = self.photo_frame_size)
        self.choose_query_btn = tk.Button(text = "Choose Query Image",command = self.query_btn_command)
        self.choose_query_btn.place(x = 1495, y=350)
        
        
        
        #-----------------result images----------------------
        self.label_1 = tk.Label(borderwidth=2, relief="groove", bg="white")
        self.label_2 = tk.Label(borderwidth=2, relief="groove", bg="white")
        self.label_3 = tk.Label(borderwidth=2, relief="groove", bg="white")
        self.label_4 = tk.Label(borderwidth=2, relief="groove", bg="white")
        self.label_5 = tk.Label(borderwidth=2, relief="groove", bg="white")
        self.label_6 = tk.Label(borderwidth=2, relief="groove", bg="white")
        self.label_7 = tk.Label(borderwidth=2, relief="groove", bg="white")
        self.label_8 = tk.Label(borderwidth=2, relief="groove", bg="white")
        
        self.output_images = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6, self.label_7 ,self.label_8]

        
        self.output_images[0].place(x = 40 , y = 40 , width = self.photo_frame_size , height = self.photo_frame_size)
        self.output_images[1].place(x = self.photo_frame_size + 80 , y = 40 , width = self.photo_frame_size , height = self.photo_frame_size)       
        self.output_images[2].place(x = 2 * self.photo_frame_size + 120 , y = 40 , width = self.photo_frame_size , height = self.photo_frame_size)       
        self.output_images[3].place(x = 3 * self.photo_frame_size + 160 , y = 40 , width = self.photo_frame_size , height = self.photo_frame_size)
        self.output_images[4].place(x = 40 , y = self.photo_frame_size + 80 , width = self.photo_frame_size , height = self.photo_frame_size)
        self.output_images[5].place(x = self.photo_frame_size + 80 , y = self.photo_frame_size + 80 , width = self.photo_frame_size , height = self.photo_frame_size)  
        self.output_images[6].place(x = 2 * self.photo_frame_size + 120 , y = self.photo_frame_size + 80 , width = self.photo_frame_size , height = self.photo_frame_size)    
        self.output_images[7].place(x = 3 * self.photo_frame_size + 160 , y = self.photo_frame_size + 80 , width = self.photo_frame_size , height = self.photo_frame_size)
           
        
        #-------------checkbox for feedback-------------------
                           
        self.check_var1 = tk.IntVar()
        self.check_var2 = tk.IntVar()
        self.check_var3 = tk.IntVar()
        self.check_var4 = tk.IntVar()
        self.check_var5 = tk.IntVar()
        self.check_var6 = tk.IntVar()
        self.check_var7 = tk.IntVar()
        self.check_var8 = tk.IntVar()
        self.c1 = tk.Checkbutton(text="1", variable = self.check_var1,onvalue = 1, offvalue = 0, state=tk.DISABLED)
        self.c1.place(x = 42 ,y = 294)
        self.c2 = tk.Checkbutton(text="2", variable = self.check_var2,onvalue = 1, offvalue = 0, state=tk.DISABLED)
        self.c2.place(x = 382 ,y = 294)
        self.c3 = tk.Checkbutton(text="3", variable = self.check_var3,onvalue = 1, offvalue = 0, state=tk.DISABLED)
        self.c3.place(x = 722 ,y = 294)
        self.c4 = tk.Checkbutton(text="4", variable = self.check_var4,onvalue = 1, offvalue = 0, state=tk.DISABLED)
        self.c4.place(x = 1062 ,y = 294)
        self.c5 = tk.Checkbutton(text="5", variable = self.check_var5,onvalue = 1, offvalue = 0, state=tk.DISABLED)
        self.c5.place(x = 42 ,y = 633)
        self.c6 = tk.Checkbutton(text="6", variable = self.check_var6,onvalue = 1, offvalue = 0, state=tk.DISABLED)
        self.c6.place(x = 382 ,y = 633)
        self.c7 = tk.Checkbutton(text="7", variable = self.check_var7,onvalue = 1, offvalue = 0, state=tk.DISABLED)
        self.c7.place(x = 722 ,y = 633)
        self.c8 = tk.Checkbutton(text="8", variable = self.check_var8,onvalue = 1, offvalue = 0, state=tk.DISABLED)
        self.c8.place(x = 1062 ,y = 633)
        

        

       
        
        


    def search_command(self):
        self.start_app()

    def feedback_command(self):
        self.start_app()
    
    def query_btn_command(self):
        self.start_app()
            

    
    def start_app(self):
       
        pass
        

        
    
if __name__=="__main__":

    APP_WIDTH = 1400
    APP_HEIGHT = 700
    APP_WIN_X_LOC = 1
    APP_WIN_Y_LOC = 10
    APP_SIDE_MENU_WIDTH = 300
    APP_ICON = 'gui_images/icon.ico'
    BACKGROUND_IMG = 'gui_images/bg.jpg'
    APP_TITLE = 'CBIR'
    APP_WIN_GEOMETRY = str(APP_WIDTH) + "x" + str(APP_HEIGHT)  + "+" + str(APP_WIN_X_LOC) + "+" + str(APP_WIN_Y_LOC)
    PHOTO_FRAME_SIZE = 200
    QUERY_BTN_WIDTH = 110





    root = tk.Tk()
    root.geometry(APP_WIN_GEOMETRY)
    root.title(APP_TITLE)
    root.iconbitmap(APP_ICON)

    app = Application(master = root, photo_frame_size = PHOTO_FRAME_SIZE, width = APP_WIDTH, height = APP_HEIGHT, side_menu_width = APP_SIDE_MENU_WIDTH, bg_img_path = BACKGROUND_IMG,
    query_btn_width =  QUERY_BTN_WIDTH
    )
    app.mainloop()


