Send data via MQTT from Raspberry Pi to AWS IOT platform
AWS IOT PLATFORM SETUP
1. Register device in AWS IOT platform via this link http://docs.aws.amazon.com/iot/latest/developerguide/iot-sdk-setup.html
2. Download all AWS IOT platform certificates -Private key -Public key -Rootca certificate -TODO add last cert.
PI SETUP
1. Download and install Raspbian OS
2. In Aws_IOT_Subscriber.py change: line 32-34 to use the certificates that you downloaded in step 2 of AWS IOT PLATFORM SETUP. line 24 change the client ID to use your register client ID line 39 change the endpoint to use the endpoint of your device
3. Run Aws_IOT_Subscriber.py and test with AWS IOT MQTT client
SENSOR SETUP
1. Connect the touch sensor to the GPIO pins of the PI
2. run TouchSensor.py. You should see messages "sensor active" on your screen when the sensor is touched
TODO ...
