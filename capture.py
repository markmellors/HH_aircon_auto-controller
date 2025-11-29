from machine import Pin
from ir_rx.acquire import IR_RX

# Configure your input pin here
IR_PIN = 16  # change if you wired to a different GPIO

ir = IR_RX(Pin(IR_PIN, Pin.IN))

print("Ready to capture. Point the remote and press the button...")

# This call blocks until it sees a complete burst or times out
durations = ir.acquire()   # Returns a list of mark/space durations in µs

print("Captured {} entries:".format(len(durations)))
print(durations)
