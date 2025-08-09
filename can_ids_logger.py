#!/usr/bin/env python3
import can
from datetime import datetime
from collections import defaultdict

bus = can.interface.Bus(channel='vcan0', bustype='socketcan')

print("Starting CAN IDS logger...")
id_counter = defaultdict(int)
start_time = datetime.now()

with open("ids_log.txt", "a") as log_file:
    while True:
        msg = bus.recv()
        if msg is None:
            continue

        # Log every message
        log_line = f"{datetime.now()} - ID: {msg.arbitration_id:X} Data: {msg.data.hex()}\n"
        log_file.write(log_line)
        log_file.flush()

        # Count frequency
        id_counter[msg.arbitration_id] += 1
        if id_counter[msg.arbitration_id] > 5:
            alert = f"ALERT: High frequency detected for ID {msg.arbitration_id:X}"
            print(alert)
            log_file.write(alert + "\n")
