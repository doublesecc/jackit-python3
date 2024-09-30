# Workaround to fix problem where device time outs

import usb.core
import usb.util
import os

try:
    from fcntl import ioctl
except ImportError:
    # Make sure this code does not break platforms without ioctl - if any...
    ioctl = lambda *args: None

# Thanks to https://github.com/Paufurtado/usbreset.py
USBDEVFS_RESET = ord('U') << (4 * 2) | 20

def reset_radio(index, idVendor=0x1915, idProduct=0x0102):
    device = list(usb.core.find(idVendor=idVendor, idProduct=idProduct, find_all=True))[index]
    bus = str(device.bus).zfill(3)
    addr = str(device.address).zfill(3)
    filename = f"/dev/bus/usb/{bus}/{addr}"
    
    try:
        with open(filename, "wb") as f:
            ioctl(f, USBDEVFS_RESET, 0)
    except IOError:
        print(f"Unable to reset device {filename}")


