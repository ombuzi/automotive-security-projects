# Project 1: Vehicle CAN Bus Pentest Lab

**Author:** Frank Otieno  
**Email:** frankotieno254@gmail.com

## Overview
This project sets up a secure and isolated CAN bus pentesting lab on Kali Linux.  
It simulates a modern vehicle's Controller Area Network (CAN) using virtual interfaces, enabling both offensive and defensive testing without needing physical hardware.

## Setup Commands
```bash
mkdir -p ~/vehicle-security/project1-canbus
cd ~/vehicle-security/project1-canbus
git init
sudo apt update
sudo apt install can-utils
sudo modprobe vcan
sudo ip link add dev vcan0 type vcan
sudo ip link set up vcan0
