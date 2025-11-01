# Boot Config for USB HID Mouse Artist


import usb_hid

usb_hid.enable(
    (usb_hid.Device.KEYBOARD, usb_hid.Device.MOUSE)
)

print("USB HID Devices enabled : Keyboard + Mouse ")