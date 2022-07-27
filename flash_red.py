import time
import aura_sdk as rgb

print("Devices found:")
for dev in rgb.get_devices():
    print("  " + dev.Name)

for i in range(10):
    rgb.set_all_to_color(0x0000FF)
    time.sleep(0.1)
    rgb.set_all_to_color(0x000000)
    time.sleep(0.1)
