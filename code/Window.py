from tkinter import *
from tkinter.font import Font
import pyglet

# Start of Setup 
pyglet.font.add_file('LM Mono 10.otf')

root = Tk()
root.title("Admissions Calculator")
root.geometry("750x500")
root.state("zoomed")
root.config(bg = "#5414b5")
icon = PhotoImage(file = "icon.png")
root.iconphoto(False, icon)
# End of Setup

# Start of Center
Label(root, text = "										", bg = "#5414b5").grid(row = 0, column = 0)
Label(root, text = "Admissions Calculator", font = ('LM Mono 10', 40), bg = "#5414b5").grid(row = 0, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 0, column = 2)

Label(root, text = "										", bg = "#5414b5").grid(row = 1, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 2, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 3, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 4, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 5, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 6, column = 1)
Label(root, text = "University Name", font = ('LM Mono 10', 20)).grid(row = 7, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 8, column = 1)
University = Entry(root, width = 40, borderwidth = 5, font = "20", justify = "center").grid(row = 9, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 10, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 11, column = 1)
Label(root, text = "										", bg = "#5414b5").grid(row = 12, column = 1)

def submit():
	print("hello")

Submit = Button(root, text = "Submit", command = submit, font = ('LM Mono 10', 20)).grid(row = 13, column = 1)
# End of Center 

# Start of Left
Label(root, text = "hello", font = ('LM Mono 10', 20)).grid(row = 0, column = 0)
# End of Left

root.mainloop()
