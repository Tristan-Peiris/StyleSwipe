from os import listdir
import tkinter as tk
import random
import csv

previous = None # The previous image
imageName = None # The name of the image

# Input: Window
#        The frame the stuff is in
#        Display object
#        The frame to display more information
#        The type of motion
# Process: Gets the next image to display
#          Places the image in the window
#          Destroys the previous image
# Output: None
# Displays the next image
def nextImage(window: tk.Tk, frame: tk.Frame, display, moreInfoFrame: tk.Frame, type: str = None):
    global previous # Getting what the user can see
    global imageName # Getting the name of the image

    if display.moving == True: # Preventing action is stuff is already moving
        return

    save_csv(imageName, type) # Saving the image to the csv file

    next = display.showFit(window, frame, moreInfoFrame, display, read_csv(imageName)) # Getting the next image

    if previous != None: # Playing in the next image
        next.lower(previous)
    next.place(x=162.5,y=240,anchor="center")
    if previous != None:
        if type == "like": # Moving the image
            display.slideRight(window, previous, 325, 162.5, "center", 1)
        elif type == "dislike":
            display.slideLeft(window, previous, 325, 162.5, "center", 1)
        else:
            raise ValueError("Invalid type") # Error handling
        previous.destroy() # Destroying the previous image
    previous = next # Setting the previous image to the current image



def darkMode(value: bool, window: tk.Tk, currentframe: tk.Frame, navFrame: tk.Frame):
    if value == True:
      window.configure(bg="#212120")
      currentframe.configure(bg="#212120")
      navFrame.configure(bg="#212120")
    else:
      window.configure(bg="white")
      currentframe.configure(bg="white")
      navFrame.configure(bg="white")

def save_csv(imageName: str, type: str):
    with open("closet.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([imageName, type])
        print(imageName)
    if type == "like":
        data = []
        with open("D:\\Year 10\\computing\\sac\\StyleSwipe\\fitpics.csv", "r") as file:
            reader = csv.reader(file, delimiter=",")
            for row in reader:
                if row[0] == imageName:
                    data.append([row[0], int(row[1]) + 1])
                    continue
                data.append(row)
            file.close()

        with open("D:\\Year 10\\computing\\sac\\StyleSwipe\\fitpics.csv", "w") as filedata:
            print(data)
            writer = csv.writer(filedata)
            writer.writerows(data)
            filedata.close()

def clear_csv():
    with open("closet.csv", "w", newline="") as file:
        pass

def read_csv(value: str):
    with open("fitpics.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == value:
                return row[1]
    return None

def selectPhoto(currentFrame: tk.Frame, display) -> tk.Frame:
    global imageName
    randomImage = random.randint(1, len(listdir('images/styles')))
    imageName = f"fitpic{randomImage}.png"
    return display.getDisplayImage(currentFrame, display.imageStorage, f"images/styles/fitpic{randomImage}.png", (278, 402))

clear_csv()

