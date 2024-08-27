from client import ImageHandeler, ClientLogic
import tkinter as tk


display = ImageHandeler

# Configures the window
window = tk.Tk()
window.geometry("325x650")
window.title("Style Swipe")
window.iconphoto(False,tk.PhotoImage(file="images/icon.png"))
window.resizable(False, False)
window.configure(bg="white")

# Stores the frame elements so that it can be cleared, and also be seperate from these 
currentframe = tk.Frame(width=325, height=650, bg="white")

# Icon in top left
logo = display.getDisplayImage(window, display.imageStorage, "images/styleswipe.png", (70,25))
logo.place(x=10,y=5,anchor="nw")

# NavBar
# Nav bar elements
navFrame = tk.Frame(window, width=329, height=45) # Frame to store the nav bar
navFrame.configure(bg="white", highlightcolor="#d3d3d3", highlightthickness=2, relief="solid")

home = display.getButtonImage(navFrame, display.imageStorage, "images/home.png", (35, 35), command=lambda: [
  clearScreen(currentframe),
  drawHome()
])
home.place(x=40.2,y=20,anchor="center")
hanger = display.getButtonImage(navFrame, display.imageStorage, "images/hanger.png", (35, 35), command=lambda: [
  clearScreen(currentframe),
  drawCloset()
])
hanger.place(x=222.5,y=20,anchor="center")
settings = display.getButtonImage(navFrame, display.imageStorage, "images/settings.png", (35, 35), command=lambda: [
  clearScreen(currentframe),
  drawSettings()
])
settings.place(x=280.5,y=20,anchor="center")
search = display.getButtonImage(navFrame, display.imageStorage, "images/search.png", (37, 37),command=lambda: [
  clearScreen(currentframe),
  drawSearch()
])
search.place(x=102.5,y=20,anchor="center")
addcircle = display.getButtonImage(navFrame, display.imageStorage, "images/addcircle.png", (35, 35),command=lambda: [
  clearScreen(currentframe),
  drawAdd()
])
addcircle.place(x=162.5,y=20,anchor="center")

navFrame.place(x=-2, y=650, anchor="sw")

def clearScreen(frame: tk.Frame):
  for child in frame.winfo_children():
    child.destroy()

def drawHome():
  global window
  global currentframe
  global display

  fitpic1 = display.getDisplayImage(currentframe, display.imageStorage, "images/styles/fitpic1.png", (278, 402))
  infoBar = display.getButtonImage(fitpic1, display.imageStorage, "images/bottombar3.png", (290, 35), command=lambda: display.moveUp(window, moreInfoFrame, 325, 650, "n", 2))
  likes = tk.Label(fitpic1, text="10K", fg="white", font=("Helvetica bold", 7), bg="#ff6c5c")
  likes.place(x=261, y=395.5, anchor="center")
  infoBar.place(x=135.5, y=405, anchor="s")
  fitpic1.place(x=162.5,y=240,anchor="center")
  crossgcircle = display.getDisplayImage(currentframe, display.imageStorage, "images/greycircle.png", (95, 95))
  crossgcircle.place(x=82.5,y=500,anchor="center")
  crosswcircle = display.getDisplayImage(currentframe, display.imageStorage, "images/whitecircle.png", (65, 65),'#d3d3d3')
  crosswcircle.place(x=82.5,y=500,anchor="center")
  cross = display.getButtonImage(currentframe, display.imageStorage, "images/cross.png", (45, 45), command=lambda: [
    display.slideLeft(window, fitpic1, 325, 162.5, "center", 1)
  ])
  cross.place(x=82.5,y=500,anchor="center")
  heartgcircle = display.getDisplayImage(currentframe, display.imageStorage, "images/greycircle (copy).png", (95, 95))
  heartgcircle.place(x=242.5,y=500,anchor="center")
  heartwcircle = display.getDisplayImage(currentframe, display.imageStorage, "images/whitecircle (copy).png", (65, 65),'#d3d3d3')
  heartwcircle.place(x=242.5,y=500,anchor="center")
  heart = display.getButtonImage(currentframe, display.imageStorage, "images/heart.png", (45, 45), command=lambda: [
    print("test"),
    ClientLogic.displayImage(window, currentframe, moreInfoFrame, display).place(x=162.5,y=240,anchor="center"),
    display.slideRight(window, fitpic1, 325, 162.5, "center", 1),
    ClientLogic.likeImage()
  ])
  heart.place(x=242.5,y=500,anchor="center")

  # More info data
  moreInfoFrame = tk.Frame(width=325, height=400, bg="white")
  moreInfoFrame.place(x=162.5, y=650, anchor="n")

  topbar = display.getButtonImage(moreInfoFrame, display.imageStorage, "images/moreinfotop.png", (325,40), command=lambda: [
    display.moveDown(window, moreInfoFrame, 500, 325, "n", 2)
  ])
  topbar.place(x=0, y=0, anchor="nw")

def drawCloset():
  global window
  global currentframe
  global display

def drawSearch():
  global window
  global currentframe
  global display

def drawAdd():
  global window
  global currentframe
  global display

def drawSettings():
  global window
  global currentframe
  global display

  darkmode = tk.Checkbutton(currentframe, bg= "white", borderwidth=0, highlightthickness=0, relief='flat')
  darkmode.place(x=300, y=100, anchor="center")
  darkmodetext = tk.Label(currentframe, text="Dark Mode",height=1, width=10, bg="white", borderwidth=0, highlightthickness=0,)
  darkmodetext.place(x=80, y=100, anchor="center")
  lightbulb = display.getDisplayImage(currentframe, display.imageStorage, "images/lightbulb.png", (30, 30))
  lightbulb.place(x=30,y=100,anchor="center")

drawHome()

currentframe.place(x=0, y=0, anchor="nw")
window.mainloop()