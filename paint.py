from tkinter import *
import tkinter.ttk as ttk #Lisä moduuli Tkinterii
from tkinter import colorchooser
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageGrab, ImageTk
import PIL
from tkinter import messagebox

root = Tk()
root.title('Ensinmmäinen piirrustus ohjelma')
root.geometry("800x800")

brush_color = "black"
def paint(e):
	
	#Brush Paramaters
	brush_width = '%0.0f' % float(my_slider.get())
	#brush_color = "green"

	# Brush Type: BUTT, ROUND, PROJECTING
	brush_type2 = brush_type.get()
	
	# Starting Position
	x1 = e.x - 1
	y1 = e.y - 1

	# Ending Position
	x2 = e.x + 1
	y2 = e.y + 1

	# Draw on the canvas
	my_canvas.create_line(x1, y1, x2, y2, fill=brush_color, width =brush_width, capstyle=brush_type2, smooth=True)

#Change size of the brush
def change_brush_size(thing):
	slider_label.config(text='%0.0f' % float(my_slider.get()))

#Change Brush Color
def change_brush_color():
	global brush_color
	brush_color = "black"
	brush_color = colorchooser.askcolor(color=brush_color)[1]
	

#Chnage Canvas Color
def change_canvas_color():
	global bg_color
	bg_color = "white"
	bg_color = colorchooser.askcolor(color=bg_color)[1]
	my_canvas.config(bg=bg_color)


#Clear Screen	
def clear_screen():
	my_canvas.delete(ALL)
	my_canvas.config(bg="white")


# Save Image
def save_as_png():
    result = filedialog.asksaveasfilename(initialdir='c:/paint/images/', filetypes=(("png files", "*.png"), ("all files", "*.*")))
    
    if result.endswith('.png'):
    	pass
    else:
    	result = result + '.png'

    if result:
    	x=root.winfo_rootx()+my_canvas.winfo_x()
    	y=root.winfo_rooty()+my_canvas.winfo_y()
    	x1=x+my_canvas.winfo_width()
    	y1=y+my_canvas.winfo_height()
    	ImageGrab.grab().crop((x,y,x1,y1)).save(result)

    	# Pop up succes message
    	messagebox.showinfo("Kuva on tallenettu", "Vau, mikä piirros! Olet niin taitava!")

#Create our canvas
w = 600
h = 400


my_canvas = Canvas(root, width=w, height=h, bg="white")
my_canvas.pack(pady=20)


#my_canvas.create_line(0, 100, 300, 100, fill="red")
#my_canvas.create_line(150, 0, 150, 200, fill="red")

my_canvas.bind('<B1-Motion>', paint)



# Create Brush Options Frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20)

# Brush Size
brush_size_frame = LabelFrame(brush_options_frame, text="Kynän Paksuus")
brush_size_frame.grid(row=0, column=0, padx=50)
#Brush Slider
my_slider = ttk.Scale(brush_size_frame, from_=1, to=100, command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)
#Brush Slider Label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

# Brush Type
brush_type_frame = LabelFrame(brush_options_frame, text="Kynän Muoto", height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set("round")

# Create Radio Buttons for Brush Type
brush_type_radio1 = Radiobutton(brush_type_frame, text="Pyöreä", variable=brush_type, value="round")
brush_type_radio2 = Radiobutton(brush_type_frame, text="Kenoviiva", variable=brush_type, value="butt")
brush_type_radio3 = Radiobutton(brush_type_frame, text="Timantti", variable=brush_type, value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)


# Change Colors
change_colors_frame = LabelFrame(brush_options_frame, text="Vaihda Väriä")
change_colors_frame.grid(row=0, column=2)

# Program Options Frame
options_frame = LabelFrame(brush_options_frame, text="Asetukset")
options_frame.grid(row=0, column=3, padx=50)

# CLear Screen Button
clear_button = Button(options_frame, text="Puhdista Ruutu",command=clear_screen)
clear_button.pack(padx=10, pady=10)

# Save Image
save_image_button = Button(options_frame, text="Tallenna PNG", command=save_as_png)
save_image_button.pack(pady=10, padx=10)


#Change Brush Color Button

brush_color_button = Button(change_colors_frame, text="Kynän Väri", command=change_brush_color)
brush_color_button.pack(pady=10, padx=10)

#Change Canvas Background Color

canvas_color_button = Button(change_colors_frame, text="Taustan Väri", command=change_canvas_color)
canvas_color_button.pack(pady=10, padx=10)


root.mainloop()