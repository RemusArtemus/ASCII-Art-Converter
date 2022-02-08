import tkinter as tk 
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import converter

color_set = True
root = tk.Tk()
root.title("ASCII Converter")
root.iconbitmap()
root.geometry('350x530')
root["bg"] = "#defffd"
root.resizable(width = False, height = False)

def resize_image(size):
    x, y = 280, 280
    if(size[0] > size [1]):
        y = int(280*size[1]/size[0])
    elif(size[0] < size[1]):
        x = int(280*size[0]/size[1])
    return [x, y]

def copy_to_clipboard(text):
    root.clipboard_clear()
    root.clipboard_append(text)

def upload_button_click():
    file_path = filedialog.askopenfilename(filetypes = [("Image", "*.jpg *.jpeg *.png")])
    if(file_path > ""):
        img_canvas.delete("all")
        pilImage = Image.open(file_path)
        converter.img = pilImage
        image = ImageTk.PhotoImage(pilImage.resize(resize_image(pilImage.size)))
        img_canvas.create_image(140, 140, image = image)
        img_canvas.image = image

def invert_button_click():
    global color_set
    if(color_set):
        example_label.config(bg = "white", fg = "black")
        color_set = False
    else:
        example_label.config(bg = "black", fg = "white")
        color_set = True
    converter.change_color_set(color_set)

def convert_button_click():
    if (converter.img != 0):
        file_path = filedialog.asksaveasfilename(filetypes = [("Text file", "*.txt")], defaultextension = "*.txt")
        if (file_path > ""):
            converter.symb_size(resolution_scale.get())
            text = converter.convert_image_to_text()
            new_file = open(file_path, 'w')
            new_file.write(text)
            new_file.close()
            copy_to_clipboard(text)
            messagebox.showinfo("Success", "Text has been copied to the clipboard!")

frame = tk.Frame(root, pady = 20, bg = root["bg"])
img_canvas = tk.Canvas(frame, width = 280, height = 280, bg = "#c9c9c9")
upload_button = tk.Button(frame, text = "upload image", height = 1, width = 10, command = upload_button_click)
invert_color_button = tk.Button(frame, text = "invert color", height = 1, width = 10, command = invert_button_click)
example_label = tk.Label(frame, text = "Ж#b:.", bg = "black", fg = "white")
convert_button = tk.Button(root, text = "Convert", bg = "#d2fcd3", width = 30, height = 4, command = convert_button_click)
resolution_scale = tk.Scale(frame, orient = tk.HORIZONTAL, from_= 1, to = 3, width = 10, bg = frame["bg"])

frame.pack()
img_canvas.pack()
upload_button.pack()
invert_color_button.pack()
example_label.pack()
resolution_scale.pack()
convert_button.pack()

root.mainloop()