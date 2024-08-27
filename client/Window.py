
import tkinter as tk
import ImageHandeler

window = tk.Tk()
window.geometry("325x650")
window.title("Style Swipe")
window.iconphoto(False,tk.PhotoImage(file="images/icon.png"))
window.resizable(False, False)
window.configure(bg="white")

display = ImageHandeler

def clearScreen():
    global window
    for child in window.winfo_children():
        child.destroy()
        
def drawHome():
    global window
    global display

    navFrame = tk.Frame(window)
    
    home = display.getDisplayImage(navFrame, display.imageStorage, "images/home.png", (35, 35))
    home.place(x=40.2,y=565,anchor="center")
    fitpic1 = display.getDisplayImage(window, display.imageStorage, "images/output-onlinepngtools (1).png", (280, 400))
    fitpic1.place(x=162.5,y=250,anchor="center")
    crosswcircle = display.getDisplayImage(window, display.imageStorage, "images/whitecircle.png", (80, 80))
    crosswcircle.place(x=102.5,y=100,anchor="center")
    crossgcircle = display.getDisplayImage(window, display.imageStorage, "images/greycircle.png", (80, 80))
    crossgcircle.place(x=102.5,y=500,anchor="center")
    cross = display.getDisplayImage(window, display.imageStorage, "images/cross.png", (60, 60),'#d3d3d3')
    cross.place(x=102.5,y=500,anchor="center")
    heart = display.getDisplayImage(window, display.imageStorage, "images/heart.png", (50, 50),)
    heart.place(x=222.5,y=500,anchor="center")
    logo = display.getDisplayImage(window, display.imageStorage, "images/styleswipe.png", (70,25))
    logo.place(x=10,y=10,anchor="nw")
    
    hanger = display.getDisplayImage(navFrame, display.imageStorage, "images/hanger.png", (35, 35))
    hanger.place(x=222.5,y=565,anchor="center")
    settings = display.getDisplayImage(navFrame, display.imageStorage, "images/settings.png", (35, 35))
    settings.place(x=280.5,y=565,anchor="center")
    search = display.getDisplayImage(navFrame, display.imageStorage, "images/search.png", (37, 37))
    search.place(x=102.5,y=566,anchor="center")
    addcircle = display.getDisplayImage(navFrame, display.imageStorage, "images/addcircle.png", (35, 35))
    addcircle.place(x=162.5,y=565,anchor="center")
    navFrame.place(x=162.5,y=565,anchor="center")
    
window.mainloop()