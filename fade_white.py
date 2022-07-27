import time
import aura_sdk as aura

print("Devices found:")
for dev in aura.get_devices():
    print("  " + dev.Name)

for j in range(5):
    for i in range(255):
        aura.set_all_to_color(aura.rgb_to_color(i, i, i))
        time.sleep(0.005)
    for i in range(255):
        aura.set_all_to_color(aura.rgb_to_color(255 - i, 255 - i, 255 - i))
        time.sleep(0.005)