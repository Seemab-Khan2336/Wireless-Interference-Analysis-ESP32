import subprocess
import re
import matplotlib.pyplot as plt
import time

def get_wifi_signal_strength():
    try:
        result = subprocess.check_output(
            ["netsh", "wlan", "show", "interfaces"],
            shell=True,
            text=True
        )
        signal = re.search(r"Signal\s*:\s*(\d+)%", result)
        if signal:
            return int(signal.group(1))
    except:
        return None

plt.ion()  # interactive mode
fig, ax = plt.subplots()

while True:
    strength = get_wifi_signal_strength()
    ax.clear()

    if strength is not None:
        ax.bar(["WiFi Signal"], [strength])
        ax.set_ylim(0, 100)
        ax.set_ylabel("Signal Strength (%)")
        ax.set_title("Live WiFi Signal Strength")
        ax.text(0, strength + 2, f"{strength}%", ha='center')
    else:
        ax.text(0.5, 0.5, "No WiFi Connected", ha='center')

    plt.pause(2)  # update every 2 seconds
