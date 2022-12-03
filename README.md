# ledi-api

```
python3 -m venv ./env
source env/bin/activate

uvicorn main:app --reload --host 0.0.0.0
```

Build raspi led matrix for RGB Hat and run rpi-rgb-led-matrix/bindings/python build with venv activated to install correctly

 `sudo setcap 'cap_sys_nice=eip' /usr/bin/python3.9` so you don't have to run uvicorn as sudo

`sudo ./demo -D4 --led-rows=64 --led-cols=64` in rpi-rgb-led-matrix/examples-api-use to test matrix
`sudo ./runtext.py -r=64 --led-cols=64 --led-gpio-mapping=adafruit-hat` in rpi-rgb-led-matrix/bindings/python/samples to test python build