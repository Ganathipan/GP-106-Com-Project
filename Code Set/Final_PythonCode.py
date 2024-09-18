import threading
from kivy.clock import Clock
from GUI_PythonCode import RPSApp
import Game_PythonCode as g
import Hardware_PythonCode as h
import time

# Define the choices available in the game
choices = ["scissors", "paper", "rock", "lizard", "spock", "none"]

# Initialize the hardware
board = h.initialize_board("COM8")
button_pins = [4, 3, 2, 1, 0, 5]
led_pins = [3, 4, 5, 6, 7, 9, 10, 11, 12, 13]
buzzer_pin = 8
buttons, leds_choice, leds_player, leds_computer, led_indicator, buzzer = h.initialize_pins(board, button_pins, led_pins, buzzer_pin)
h.buzz(1, buzzer)

# Initialize the Kivy app
app = RPSApp()

def run_game():
    player1_points = 0
    computer_points = 0

    for k in range(7):  # Play 7 rounds
        if h.check_state(buttons[5]) is not True:  # Exit the game if the button is pressed
            print(f"\n \nRound {k+1}")
            g.choices_available()

            player1_choice = h.player1_choice(buttons, led_indicator, buzzer)
            g.show_player_choice(player1_choice, "Player")

            if player1_choice != 5:
                computer_choice = g.computer_choice_selection()
                g.show_player_choice(computer_choice, "Computer")
                h.show_player_choice(computer_choice, leds_choice)
            else:
                computer_choice = 5

            winner = g.round_result(player1_choice, computer_choice)
            player1_points, computer_points = g.update_points(winner, player1_points, computer_points)

            if player1_points > 3 or computer_points > 3:
                h.winner_led(winner, leds_player, leds_computer)
                break

            h.off_led((leds_player + leds_computer))
            h.winner_led(winner, leds_player, leds_computer)
            h.result_LED(player1_points, leds_player)
            h.result_LED(computer_points, leds_computer)

            def update_game_state(dt):
                app.update_choice(choices[computer_choice], choices[player1_choice])
                app.update_score(player1_points, computer_points)

            Clock.schedule_once(update_game_state, 1)  # Schedule update after 1 second

            # Use a different thread to run the Kivy app to avoid blocking
            threading.Thread(target=app.run).start()

            player1_choice, computer_choice = 0, 0
            winner = 0

        else:
            break
        time.sleep(0.75)

    leds = leds_player + leds_computer + leds_choice
    h.off_led(leds)

    h.buzz(1, buzzer)
    winner = g.display_final_results(player1_points, computer_points)
    h.winner_led(winner, leds_player, leds_computer)

    def update_final(dt):
        app.display_final_result(player1_points, computer_points)

    Clock.schedule_once(update_final, 1)  # Schedule final result update

    # Run the app in a separate thread
    threading.Thread(target=app.run).start()

    time.sleep(1)

    leds.append(led_indicator)
    h.off_led(leds)

def main():
    while True:
        if h.check_state(buttons[0]) is True:
            print(f"\n \n \tExited from Game!!!")
            time.sleep(0.5)
            h.buzz(1, buzzer)
            break
        else:
            run_game()

if __name__ == "__main__":
    main()
