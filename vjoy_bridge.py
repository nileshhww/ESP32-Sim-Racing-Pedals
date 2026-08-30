import serial
import pyvjoy

# ==========================
# SETTINGS
# ==========================

COM_PORT = "COM7"
BAUD_RATE = 115200

# Adjust if needed
BRAKE_MIN = 500
BRAKE_MAX = 43333

THROTTLE_MIN = 500
THROTTLE_MAX = 43556

DEADZONE = 285

# Higher = less sensitive
CURVE = 1.0

# ==========================
# CONNECT
# ==========================

ser = serial.Serial(COM_PORT, BAUD_RATE, timeout=1)
j = pyvjoy.VJoyDevice(1)

print("Connected to ESP32 and vJoy")

brake_filtered = BRAKE_MIN
throttle_filtered = THROTTLE_MIN

# ==========================
# MAIN LOOP
# ==========================

while True:
    try:
        line = ser.readline().decode('utf-8', errors='ignore').strip()

        if not line:
            continue

        parts = line.split(',')

        if len(parts) != 4:
            continue

        brake = int(parts[0])
        throttle = int(parts[1])
        gear_up = int(parts[2])
        gear_down = int(parts[3])

        # Strong smoothing
        brake_filtered = (brake_filtered * 0.95) + (brake * 0.05)
        throttle_filtered = (throttle_filtered * 0.95) + (throttle * 0.05)

        # Normalize
        brake_norm = (brake_filtered - BRAKE_MIN) / (BRAKE_MAX - BRAKE_MIN)
        throttle_norm = (throttle_filtered - THROTTLE_MIN) / (THROTTLE_MAX - THROTTLE_MIN)

        brake_norm = max(0.0, min(1.0, brake_norm))
        throttle_norm = max(0.0, min(1.0, throttle_norm))

        # Less sensitive pedal curve
        brake_axis = int((brake_norm ** CURVE) * 32767)
        throttle_axis = int((throttle_norm ** CURVE) * 32767)

        # Deadzone
        if brake_axis < DEADZONE:
            brake_axis = 0

        if throttle_axis < DEADZONE:
            throttle_axis = 0

        # Send to vJoy
        j.set_axis(pyvjoy.HID_USAGE_X, brake_axis)
        j.set_axis(pyvjoy.HID_USAGE_Y, throttle_axis)

        # Gear buttons
        j.set_button(1, gear_up)
        j.set_button(2, gear_down)

        print(
            f"Brake:{brake} X:{brake_axis} | "
            f"Throttle:{throttle} Y:{throttle_axis} | "
            f"UP:{gear_up} DOWN:{gear_down}",
            end="\r"
        )

    except Exception as e:
        print("\nERROR:", e)
