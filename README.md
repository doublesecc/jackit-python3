# jackit-python3

You can use https://github.com/kuzmin-no/nrf-research-firmware-python3 to flash your crazyradio PA with the mousejack firmware via python3.

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

## Run Setup
```bash
python setup.py install
```

## Run Jackit
```bash
sudo ~/venv/jackit/bin/jackit
```


