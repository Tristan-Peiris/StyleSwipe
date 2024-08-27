from PIL import Image, ImageTk
from math import cos, pi
import tkinter as tk

imageStorage = {}  # Create a dictionary to store the images
moving = False


# Function to get an image
# Input: window - The window to place the image in
#        images - The dictionary to store the image in
#        path - The path to the image
#        size - The size of the image
# Process: Opens the image and resizes it
# Output: The frame with the image
def getDisplayImage(window, images: imageStorage, path: str, size: tuple[int, int], *bg: str) -> tk.Frame:
    if len(bg) > 0:
        bg = bg[0]
    else:
        bg = "white"

    image_frame = tk.Frame(window, width=size[0], height=size[1], bg=bg)  # Create a frame for the image

    img = Image.open(path).convert("RGBA")  # Open the image
    img = img.resize(size)  # Resize the image

    image = ImageTk.PhotoImage(img)  # Create a photo image from the image
    images[path] = image  # Saves image to prevent garbage collection

    # Create a label with the image

    image_label = tk.Label(image_frame, image=image, bg=bg)
    image_label.pack()

    return image_frame  # Return the frame


# Function to get an image and make it a button
# Input: window - The window to place the image in
#        images - The dictionary to store the image in
#        path - The path to the image
#        size - The size of the image
#        command - The command to run when the button is pressed
# Process: Opens the image and resizes it
# Output: The frame with the button
def getButtonImage(window, images: imageStorage, path: str, size: tuple[int, int], *bg: str, command) -> tk.Frame:
    if len(bg) > 0:
        bg = bg[0]
    else:
        bg = "white"

    image_frame = tk.Frame(window, width=size[0], height=size[1], bg="white")  # Create a frame for the image

    img = Image.open(path).convert("RGBA")  # Open the image
    img = img.resize(size)  # Resize the image

    image = ImageTk.PhotoImage(img)  # Create a photo image from the image
    images[path] = image  # Saves image to prevent garbage collection

    # Create a button with the image
    image_label = tk.Button(image_frame, image=image, bg="white", borderwidth=0, highlightthickness=0, relief='flat', command=command)
    image_label.pack()
    return image_frame  # Return the frame

# Stores the amount to move a frame by
movementMultipliers = [0.0, 0.0002467198171342, 0.0009866357858642205, 0.002219017698460002, 0.003942649342761062, 0.006155829702431115, 0.00885637463565564, 0.012041619030626283, 0.015708419435684462, 0.019853157161528467, 0.024471741852423234, 0.029559615522887273, 0.03511175705587427, 0.04112268715800943, 0.04758647376699027, 0.05449673790581605, 0.06184665997806821, 0.06962898649802818, 0.07783603724899246, 0.08645971286271908, 0.09549150281252627, 0.1049224938121548, 0.11474337861210537, 0.1249444651847702, 0.13551568628929422, 0.1464466094067262, 0.1577264470356557, 0.1693440673381741, 0.18128800512565518, 0.1935464731735117, 0.20610737385376343, 0.2189583110739347, 0.23208660251050173, 0.2454792921248144, 0.2591231629491424, 0.2730047501302266, 0.28711035421746367, 0.30142605468260975, 0.31593772365766093, 0.33063103987735426, 0.3454915028125263, 0.36050444698038536, 0.3756550564175725, 0.39092837930172863, 0.40630934270713764, 0.4217827674798845, 0.43733338321784787, 0.45294584334074284, 0.46860474023534326, 0.4842946204609358, 0.49999999999999994, 0.5157053795390641, 0.5313952597646567, 0.5470541566592572, 0.5626666167821521, 0.5782172325201155, 0.5936906572928624, 0.6090716206982713, 0.6243449435824273, 0.6394955530196146, 0.6545084971874737, 0.6693689601226457, 0.684062276342339, 0.6985739453173903, 0.7128896457825363, 0.7269952498697734, 0.7408768370508577, 0.7545207078751857, 0.7679133974894985, 0.7810416889260654, 0.7938926261462365, 0.8064535268264881, 0.8187119948743449, 0.8306559326618259, 0.8422735529643444, 0.8535533905932737, 0.8644843137107057, 0.8750555348152298, 0.8852566213878945, 0.8950775061878452, 0.9045084971874737, 0.913540287137281, 0.9221639627510075, 0.9303710135019718, 0.9381533400219317, 0.9455032620941839, 0.9524135262330097, 0.9588773128419905, 0.9648882429441257, 0.9704403844771128, 0.9755282581475768, 0.9801468428384715, 0.9842915805643155, 0.9879583809693737, 0.9911436253643444, 0.9938441702975689, 0.9960573506572389, 0.99778098230154, 0.9990133642141358, 0.9997532801828658, 1.0]

# The above numbers were calculated using the following function:
def getMultipliers() -> list[float]: # No longer required.
    timesegments = 100 # Defines and resolution of the movement
    multipliers = [] # Stores the numbers

    for i in range(timesegments+1): # Calculating the numbers
      x = i * (1/timesegments)
      multipliers.append((-cos(x*pi)+1)/2)
    print(multipliers) # Printing the for debug
    return multipliers # Returning the list of numbers

# Input: Window
#        The frame the stuff is in
#        Distance to move the elements
#        Start point of the frame
#        Anchor point of the frame
#        Speed to move the image at
# Process: Gets the list of multiplier to calculate where to place the frame
#          Places the frame the wait and repeat until at final ploint
# Output: None
# Moves the frame up
def moveUp(window: tk.Tk,frame: tk.Frame, distance: float, startPoint: float, anchor, speed: int):
    global moving
    if moving == True:
        return
    else:
        moving = True
    mutipliers = movementMultipliers
    for i in range(101):
        frame.place(y=startPoint - distance * mutipliers[i], anchor=anchor)
        window.update()
        window.after(speed)

    moving = False

# Input: Window
#        The frame the stuff is in
#        Distance to move the elements
#        Start point of the frame
#        Anchor point of the frame
#        Speed to move the image at
# Process: Gets the list of multiplier to calculate where to place the frame
#          Places the frame the wait and repeat until at final ploint
# Output: None
# Moves the frame down
def moveDown(window: tk.Tk ,frame: tk.Frame, distance: float, startPoint: float, anchor, speed: int):
    global moving
    if moving == True:
        return
    else:
        moving = True
    mutipliers = movementMultipliers
    for i in range(101):
        frame.place(y=startPoint + distance * mutipliers[i], anchor=anchor)
        window.update()
        window.after(speed)

    moving = False

# Input: Window
#        The frame the stuff is in
#        Distance to move the elements
#        Start point of the frame
#        Anchor point of the frame
#        Speed to move the image at
# Process: Gets the list of multiplier to calculate where to place the frame
#          Places the frame the wait and repeat until at final ploint
# Output: None
# Moves the frame right
def slideRight(window: tk.Tk ,frame: tk.Frame, distance: float, startPoint: float, anchor, speed: int):
    global moving
    if moving == True:
        return
    else:
        moving = True
    mutipliers = movementMultipliers
    for i in range(101):
        frame.place(x=startPoint + distance * mutipliers[i], anchor=anchor)
        window.update()
        window.after(speed)

    moving = False


# Input: Window
#        The frame the stuff is in
#        Distance to move the elements
#        Start point of the frame
#        Anchor point of the frame
#        Speed to move the image at
# Process: Gets the list of multiplier to calculate where to place the frame
#          Places the frame the wait and repeat until at final ploint
# Output: None
# Moves the frame left
def slideLeft(window: tk.Tk ,frame: tk.Frame, distance: float, startPoint: float, anchor, speed: int):
    global moving
    if moving == True:
        return
    else:
        moving = True
    mutipliers = movementMultipliers
    for i in range(101):
        frame.place(x=startPoint - distance * mutipliers[i], anchor=anchor)
        window.update()
        window.after(speed)

    moving = False