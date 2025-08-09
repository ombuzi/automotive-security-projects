# Project 2: Advanced CAN Message Injection & Filtering

**Author:** Frank Otieno  
**Contact:** frankotieno254@gmail.com  

## Overview
This project simulates attack and defense techniques on vehicle CAN networks.  
It demonstrates how to craft and inject malicious CAN frames, and how to filter/block suspicious traffic with logging.

## Setup
- Kali Linux with can-utils and python-can installed  
- Virtual CAN (`vcan0`) interface active

## Usage
- Run `injector.py` to send crafted attack frames  
- Run `filter.py` to block/filter malicious frames and log events

