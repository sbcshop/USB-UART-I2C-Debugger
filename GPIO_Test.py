from PyMCP2221A import PyMCP2221A

import time
gpio = PyMCP2221A.PyMCP2221A()
gpio.Reset()
time.sleep(1)

print('-'*20)
print('MCP2221(A) GPIO Test')
print('-'*20)
gpio = PyMCP2221A.PyMCP2221A()
gpio.GPIO_Init()
gpio.GPIO_0_OutputMode()
gpio.GPIO_3_InputMode()
print(" CTRL+C keys to exit.")
while 1:
    if gpio.GPIO_3_Input()[0]:
        # Note that GPIO_3_Input() returns a tuple
        # GPIO_GetValue() is available if you don't need to know
        # what the Direction is
        print("GPIO 3 is HIGH!")
    gpio.GPIO_2_Output(1)
    time.sleep(0.1)
    gpio.GPIO_2_Output(0)
    time.sleep(0.1)
    gpio.GPIO_1_Output(1)
    time.sleep(0.1)
    gpio.GPIO_1_Output(0)
    time.sleep(0.1)
    gpio.GPIO_0_Output(1)
    time.sleep(0.1)
    gpio.GPIO_0_Output(0)
    time.sleep(0.1)
