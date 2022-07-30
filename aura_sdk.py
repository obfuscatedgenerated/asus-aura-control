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
    """Sets all Aura devices to the given (hexadecimal) color.

    Args:
        color (int): The color to set all devices to.
    """    
    for dev in devices:
        if dev.Type == 0x80000:  # If the device is an RGB Keyboard
            for key in dev.Keys:
                key.color = color
        else:
            for light in dev.Lights:
                light.color = color
        dev.Apply()  # Apply the changes to the device


def get_devices():
    """Lists all Aura devices.

    Returns:
        COMObject: A list of Aura devices (enumerable).
    """    
    return devices


def rgb_to_color(r, g, b):
    """Converts an RGB color to a hexadecimal color.

    Args:
        r (int): Red channel value.
        g (int): Green channel value.
        b (int): Blue channel value.

    Returns:
        int: A hexadecimal color.
    """    
    return (b << 16) | (g << 8) | r

def close():
    aura.ReleaseControl(0)