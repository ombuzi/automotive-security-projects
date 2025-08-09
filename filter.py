#!/usr/bin/env python3
"""
CAN Bus Filter and Logger  
Author: Frank Otieno  
Contact: frankotieno254@gmail.com

Blocks messages with suspicious IDs and logs them.
"""

import can
from datetime import datetime

SUSPICIOUS_IDS = {0x500, 0x600, 0x700}

def main():
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')
    log_file = open("filter_log.txt", "a")

    print("[+] Starting CAN filter... Press Ctrl+C to stop.")

    try:
        while True:
            msg = bus.recv()
            if msg is None:
                continue

            if msg.arbitration_id in SUSPICIOUS_IDS:
                alert = f"{datetime.now()} ALERT: Blocked suspicious CAN ID {hex(msg.arbitration_id)} Data: {msg.data.hex()}\n"
                print(alert.strip())
                log_file.write(alert)
                log_file.flush()
                # Do NOT forward/send the message to simulate blocking
            else:
                # Normally forward or process the message here if needed
                pass

    except KeyboardInterrupt:
        print("\n[+] Filter stopped by user.")
    finally:
        log_file.close()

if __name__ == "__main__":
    main()
