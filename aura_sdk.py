import win32com.client  # This only works on Windows
from pywintypes import com_error
import sys

try:
    aura = win32com.client.Dispatch("aura.sdk.1")  # Initialize Aura SDK
except com_error:
    print(
        "Aura SDK not found. Please make sure you have Aura installed and LightingService.exe is running."
    )
    sys.exit(1)

aura.SwitchMode()  # Acquire control of the Aura lighting service
devices = aura.Enumerate(0)  # Enumerate all devices


def set_all_to_color(color):
    for dev in devices:
        if dev.Type == 0x80000:  # If the device is an RGB Keyboard
            for key in dev.Keys:
                key.color = color
        else:
            for light in dev.Lights:
                light.color = color
        dev.Apply()  # Apply the changes to the device


def get_devices():
    return devices


def rgb_to_color(r, g, b):
    return (r << 16) | (g << 8) | b
