# jackit-python3
This repository is a minor update to the original [jackit repository](https://github.com/insecurityofthings/jackit) with the intention to make it work consistently with python3 in a python virtual environment (venv).

You can use this [repository](https://github.com/kuzmin-no/nrf-research-firmware-python3) to flash your crazyradio PA with the mousejack firmware using python3.

> [!IMPORTANT]  
> This script has been created for debian based systems and tested successfully against Ubuntu and Kali distributions.

# Quick Setup
## Clone this repository
```bash
git clone https://github.com/doublesecc/jackit-python3.git && \
cd jackit-python3/
```
## Run the setup.sh script
```bash
source ./setup.sh
```

If there are no errors, you should be able to run jackit
```bash
sudo ~/venv/jackit/bin/jackit
```

If there are any errors, check that all system packages are up to date and then re-run the script
```bash
sudo apt update -y
```

# Manual Setup
## Setup Python Virtual Environment
### Install venv
``` bash
sudo apt install python3-venv
```
### Create dirctory to store venvs
```bash
mkdir ~/venv
```

### Create venv
```bash
python3 -m venv ~/venv/jackit
```

### Activate venv
```bash
source ~/venv/jackit/bin/activate
```

## Clone this repository
```bash
git clone https://github.com/doublesecc/jackit-python3.git && \
cd jackit-python3/
```

## Install Required packages
### Install system packages
Install pyusb
```bash
sudo apt install python3-usb
```
### Install pip3 packages

```bash
pip3 install -r requirements.txt
```

## Install jackit python package in jackit venv
```bash
pip3 install -e .
```

# Usage
## Run jackit
```bash
sudo ~/venv/jackit/bin/jackit
```

# Troubleshooting
## Timeout Error
Sometimes the jackit will generate a timeout related error.

You can just run jackit with the reset option to fix this and do it each time as needed.
```bash
sudo ~/venv/jackit/bin/jackit --reset
```

## Help
```bash
sudo ~/venv/jackit/bin/jackit --help
Usage: jackit [OPTIONS]

Options:
  --debug             Enable debug
  --script PATH       Ducky file to use for injection
  --lowpower          Disable LNA on CrazyPA
  --interval INTEGER  Interval of scan in seconds, default to 5s
  --layout TEXT       Keyboard layout: us, gb, de...
  --address TEXT      Address of device to target attack
  --vendor TEXT       Vendor of device to target (required when specifying
                      address)
  --reset             Reset CrazyPA dongle prior to initialization
  --autopwn           Automatically find and attack all targets
  --all-channels      Send attack to all detected channels
  --keylogging        Log keystrokes for XOR encrypted MS keyboards
  --help              Show this message and exit.
```
