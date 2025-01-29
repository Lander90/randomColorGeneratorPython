import tkinter as tk
import random, time

randY = 0
randX = 0
greenValue = 0
redValue = 0
blueValue = 0

def buttonClick():
    global greenValue
    global redValue
    global blueValue
    
    redValue = random.randint(0,255)
    greenValue = random.randint(0,255)
    blueValue = random.randint(0,255)
    
    root.config(bg=rgbToHex(redValue,greenValue,blueValue))
    header.config(bg=rgbToHex(redValue,greenValue,blueValue), fg = rgbToHex(255-redValue,255-greenValue,255-blueValue))
    colorLabel.config(text = rgbToHex(redValue,greenValue,blueValue), fg = rgbToHex(255-redValue,255-greenValue,255-blueValue),bg = rgbToHex(redValue,greenValue,blueValue))
    
def rgbToHex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'

root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)

header = tk.Label(root, text='Random Color Generator', font = 'Callibri 16 bold')
header.pack(pady=10)
    
button = tk.Button(root, bg='white', text='Press Me!', command = buttonClick, font = 'Callibri 10')
button.pack(pady=5)

colorLabel= tk.Label(root, font = 'Callibri 16 bold')
colorLabel.pack(pady= 16)

root.mainloop()
