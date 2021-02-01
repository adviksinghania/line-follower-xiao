# Line-Follower-Xiao

## About
A Line Follower Robot made using Seeeduino Xiao, running CircuitPython (Arduino sketch also included)

*   Components required:
    -   Seeeduino Xiao
    -   _2x_ IR Sensor breakouts
    -   L293D Motor driver IC
    -   _2x_ 9V General Purpose DC Motors
    -   Breadboard & Jumper wires
    -   9V Battery
    -   7805 5V Voltage Regulator IC
    -   _2x_ 10 uF, 25V Electrolytic Capacitors

## Seeeduino XIAO
The SEEED Studio's [Seeeduino XIAO](https://wiki.seeedstudio.com/Seeeduino-XIAO/) is a minimal, low-cost board that uses the Atmel ATSAMD21G18, a powerful 32-bit ARM Cortex®-M0+ processor running at 48MHz with 256KB Flash and 32KB SRAM. The board is 20 x 17.5mm in size which is perfect for wearable devices and small projects. It has multiple development interfaces including DAC output, SWD Bonding pad interface, I2C, UART and SPI interfaces. It's Compatible with both [Arduino IDE](https://www.arduino.cc) and [CircuitPython](https://circuitpython.org/board/seeeduino_xiao/) and uses a USB-C connector.

## Setup
*   Get started with [CircuitPython](https://learn.adafruit.com/welcome-to-circuitpython/what-is-circuitpython) if you haven't already. Install [Mu](https://codewith.mu/) on your PC.
*   Make sure that you're running the latest version of CircuitPython on the board you're using. More info can be found [here](https://wiki.seeedstudio.com/Seeeduino-XIAO-CircuitPython/), [there](https://learn.adafruit.com/welcome-to-circuitpython/installing-circuitpython) and [everywhere](https://learn.adafruit.com/welcome-to-circuitpython/troubleshooting).
*   **Optional:** Download and install [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) or use it as a binary file. (This is needed since Seeeduino Xiao doesn't support the Mu Editor's serial console at the moment.)
*   Clone the repository ```git clone https://github.com/adviksinghania/line-follower-xiao.git``` into your working directory and copy the ```code.py``` to your CIRCUITPY Drive
*   Disconnect the board and wire the components according to the diagram below:
![Schematic](https://github.com/adviksinghania/line-follower-xiao/blob/main/circuit.png?raw=true)
