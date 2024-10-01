# jackit-python3
This repository is an minor update to the original [jackit repo](https://github.com/insecurityofthings/jackit) with the intention to make it work consistenetly with python3.

You can use this [repository](https://github.com/kuzmin-no/nrf-research-firmware-python3) to flash your crazyradio PA with the mousejack firmware using python3.

# Quick Setup
Clone this repository:
```bash
git clone https://github.com/doublesecc/jackit-python3.git && \
cd jackit-python3/
```

Run the setup.sh script:
```bash
source ./setup.sh
```

If there are no errors, you should be able to run jackit:
```bash
sudo ~/venv/jackit/bin/jackit
```

# Manual Setup
## Setup Python Virtual Environment
### Install venv
``` bash
sudo apt install python3-venv
```
### Setup venv filesystem
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

## Clone
```bash
git clone https://github.com/doublesecc/jackit-python3.git && \
cd jackit-python3/
```

## Install Required packages
### System Packages
Install pyusb
```bash
sudo apt install python3-usb
```
### Pip3 packages

```bash
pip3 install -r requirements.txt
```

## Install jackit python package into 
```bash
pip3 install -e .
```

# Usage
## Run Jackit
```bash
sudo ~/venv/jackit/bin/jackit
```

## Resetting jackit
Sometimes the following error will appear:

You can reset it and then just run jackit as normal
```bash
sudo ~/venv/jackit/bin/jackit --reset
```
