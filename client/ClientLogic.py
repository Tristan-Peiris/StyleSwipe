import tkinter as tk
import csv
import random
from os import listdir
previousimage = None
randomimage = 1
# Input: None
# Proccess: Get a random image
# Returns the image
def displayImage(window: tk.Tk, frame: tk.Frame, moreInfoFrame: tk.Frame, display) -> tk.Frame:
    global randomimage, previousimage
    totalimages = len(listdir("images/styles"))
    randomimage = random.randint(1,totalimages)
    while randomimage == previousimage:
        randomimage = random.randint(1, totalimages)

    previousimage = randomimage


    
    currentimage = display.getDisplayImage(frame, display.imageStorage, f"images/styles/fitpic{randomimage}.png", (278, 402))
    
    infoBar = display.getButtonImage(currentimage, display.imageStorage, "images/bottombar3.png", (290, 35), command=lambda: display.moveUp(window, moreInfoFrame, 325, 650, "n", 2))
    
    likes = tk.Label(currentimage, text="10K", fg="white", font=("Helvetica bold", 7), bg="#ff6c5c")
    
    likes.place(x=261, y=395.5, anchor="center")
    infoBar.place(x=135.5, y=405, anchor="s")

    currentimage.lower()
    currentimage.place(x=162.5,y=240,anchor="center")
    print("done")
    
    return currentimage
    
def likeImage():
    global currentimage
    global randomimage
    with open("closet.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([f"images/styles/fitpic{randomimage}.png"])


def dislikeImage():
    displayImage()

def clear_csv():
    with open("closet.csv", "w", newline="") as file:
        pass


clear_csv()

