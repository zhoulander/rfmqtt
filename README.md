# rfmqtt
RF MQTT Remote

Listens to MQTT topic to control Westinghouse ceiling fan controlled by RF Remote.
Uses RPITx to play the signal recordings.
Recordings were captured using an RTLSDR.

Perhaps you can make use of this. Good luck.

| File | Usage |
|-----:|-----------|
|fan.py | run this on your pi|
|fan.yaml | put this in your Home Assistant config|
| ha_fan_change.yaml | Home assistant automation|
| ha_light_toggle.yaml | Home assistant automation|
