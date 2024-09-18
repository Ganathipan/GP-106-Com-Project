
"""
Hardware_PythonCode.py

Author: S. Ganathipan
Location: D:\E21_2nd_Sem\Computing\Python\Final_Project\Code Set V2.5/Hardware_PythonCode.py
Version: 2.5
Date: 2024-07-24 10:42 PM

Description:
This module initializes and controls an Arduino board for a game that involves
buttons, LEDs, and a buzzer. It includes functions to set up the board, handle
inputs and outputs, and manage game logic using the Arduino.

"""

# Import modules from Pyfirmata and the inbuilt time module
from pyfirmata import Arduino, INPUT, OUTPUT, util
import time

# Define the choices available in the game
choices = ["Scissors", "Paper", "Rock", "Lizard", "Spock"]

'''
Defining the needed functions for the game to use Arduino modules
'''

def initialize_board(port):
    """
    Initialize the Arduino board.
    
    Args:
    - port (str): The port to which the Arduino board is connected.
    
    Returns:
    - board: The initialized Arduino board or None if initialization failed.
    """
    board = Arduino(port)
    print(f"Successfully connected to the board on {port}")

    iterator = util.Iterator(board)
    iterator.start()
        
    return board

def initialize_pins(board, button_pins, led_pins, buzzer_pin):
    """
    Initialize button and LED pins on the Arduino board.

    Args:
    - board (Arduino): The Arduino board instance.
    - button_pins (list): List of button pin numbers.
    - led_pins (list): List of LED pin numbers.
    - buzzer_pin (int): The buzzer pin number.

    Returns:
    - tuple: A tuple containing lists of Button objects, LED objects, and the Buzzer object.
    """
    # Initialize button pins
    buttons = [board.get_pin(f'a:{pin}:i') for pin in button_pins]
    
    # Initialize LED pins
    leds_choice = [board.get_pin(f'd:{pin}:o') for pin in led_pins[0:5]]
    leds_player1 = [board.get_pin(f'd:{pin}:o') for pin in led_pins[5:7]]
    leds_computer = [board.get_pin(f'd:{pin}:o') for pin in led_pins[7:9]]
    led_indicator = board.get_pin(f'd:{led_pins[9]}:o')

    # Initialize buzzer pin
    buzzer = board.get_pin(f'd:{buzzer_pin}:o')

    for pin in (leds_choice + leds_player1 + leds_computer):
        pin.write(0)

    return buttons, leds_choice, leds_player1, leds_computer, led_indicator, buzzer

def buzz(times, buzzer):
    """
    Activate the buzzer for a specified number of times.

    Args:
    - times (int): Number of times to activate the buzzer.
    - buzzer: The buzzer pin object.
    """
    for _ in range(times):
        buzzer.write(1)
        time.sleep(0.3)
        buzzer.write(0)
        time.sleep(0.3)

def check_state(button):
    """
    Check the state of a button.

    Args:
    - button (char): The button pin object.

    Returns:
    - bool: True if the button is pressed, False otherwise.
    """

    time.sleep(0.3)
    return bool(round(button.read()))

def off_led(leds):
    """
    Turn off all the LEDs.

    Args:
    - leds (list): List of LED pin objects.
    """
    for led in leds:
        led.write(0)

def player1_choice(buttons, led_indicator, buzzer):
    """
    Determine Player 1's choice based on button presses.

    Args:
    - buttons (list): List of button pin objects.
    - led_indicator(list): The LED indicator pin object.
    - buzzer(int): The buzzer pin object.

    Returns:
    - int: The index of Player 1's choice.
    """
    led_indicator.write(1)
    print("Make your choice")
    # Measure time elapsed to allow button press
    start_time = time.time()

    # Loop until time limit is reached
    while time.time() - start_time <= 3:

        # Check each button for press
        for index, button in enumerate(buttons):
            if round(button.read()):
                return index
            time.sleep(0.4)
        
    led_indicator.write(0)
    buzz(2, buzzer)
    return 5  # If no button pressed within time limit, return 5 (no choice)

def show_player_choice(choice, leds):
    """
    Simulate Player 2's choice by lighting up corresponding LED.

    Args:
    - choice (int): Player 1's choice.
    - leds (list): List of LED objects.
    """
    if 0 <= choice < len(choices): # To check the validity of choice
        leds[choice].write(1)
        time.sleep(1) # Wait for a short duration
        leds[choice].write(0) # Turn off the LED
    
def result_LED(result, leds):
    """
    Display the result on LEDs in binary format.

    Args:
    - result (int): The player's points.
    - leds (list): List of LED pin objects for the player.
    """

    # Convert the result to binary and display on LEDs
    bit = format(result, '02b')
    for pin, i in zip(leds, range(2)):
        pin.write(int(bit[i]))

def winner_led(winner, leds_player1, leds_computer):
    """
    Display the winner on the corresponding player's LEDs.

    Args:
    - winner (int): 1 if Player 1 wins, -1 if Player 2 wins, 0 if draw.
    - leds_player1 (list): List of LED pin objects for Player 1.
    - leds_computer (list): List of LED pin objects for Player 2.
    """
    if winner == 1:
        blink_led(2, leds_player1, 2)  # Player 1 wins
        
    elif winner == -1:
        blink_led(2, leds_computer, 2)  # Player 2 wins
        
    else:
        leds = leds_player1 + leds_computer
        blink_led(2, leds, 2)  # Draw

def blink_led(times, leds, Type):
    """
    Blinks or makes an animated look for LEDs for a specified number of times.

    Args:
    - times (int): Number of times to blink.
    - leds (list): List of LED objects.
    - type (int): Mentions which way the LEDs need to work. 
                    (1: LED(s) brightness increases 
                     2: LED(s) blinks
                     3: LED(s) lights Up)
    """

    if Type == 1: # LED light up shades 
        for i in range(0, times):
            for pin in range(len(leds)): 
                leds[pin].write(i / (times-1))
            time.sleep(0.3) # Wait for a short duration
        
    elif Type == 2: # LED blinks for certain time
        for i in range(0, times):
            for pin in range(len(leds)): 
                leds[pin].write(1)
            time.sleep(0.5) # Wait for a short duration
            for pin in range(len(leds)): 
                leds[pin].write(0)
            time.sleep(0.5) # Wait for a short duration
    
    else: # LED set to ON
        for pin in range(len(leds)): 
            leds[pin].write(1)