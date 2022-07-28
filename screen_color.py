import time
import aura_sdk as aura
from PIL import Image
from PIL import ImageGrab
import numpy as np

print("Devices found:")
for dev in aura.get_devices():
    print("  " + dev.Name)

FPS = 30

last_color = np.zeros(3)

while True:
    screen = ImageGrab.grab()  # Grab the screen
    screen = screen.resize(
        (8, 8)
    )  # Resize to a manageable size (not 1 as it is unstable)
    screen.convert("RGB")  # Convert from HSV to RGB
    frame = np.array(screen)  # Convert to a numpy array
    arr = frame.transpose(2, 0, 1).reshape(
        3, -1
    )  # Convert frame into arrays of r, g, b
    color = arr.mean(
        axis=1
    )  # Get the average color of the screen (axis 1 meaning get the average of each row)
    color = color.astype(int)  # Convert to int
    color = np.flip(color)  # Flip the color to match the Aura SDK
    if not np.array_equal(color, last_color):
        aura.set_all_to_color(aura.rgb_to_color(*color))  # Set the color of all devices
        last_color = color
    time.sleep(1 / FPS)  # Wait for the next frame to conserve resources
