import time
import aura_sdk as aura
import atexit

atexit.register(aura.close)

print("Devices found:")
for dev in aura.get_devices():
    print("  " + dev.Name)

for i in range(10):
    aura.set_all_to_color(0x0000FF)
    time.sleep(0.1)
    aura.set_all_to_color(0x000000)
    time.sleep(0.1)
