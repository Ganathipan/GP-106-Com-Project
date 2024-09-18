from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super(WelcomeScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        welcome_label = Label(text="Welcome to Rock-Paper-Scissors!", font_size=32)
        self.add_widget(welcome_label)
        Clock.schedule_once(self.start_game, 2)  # Automatically move to game screen after 2 seconds

    def start_game(self, *args):
        self.manager.current = 'game'

class GameScreen(Screen):
    player_choice = StringProperty("None")
    computer_choice = StringProperty("None")
    player_score = NumericProperty(0)
    computer_score = NumericProperty(0)

    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        self.score_label = Label(text=self.get_score_text(), font_size=24)
        self.player_choice_image = Image(source='', size_hint=(1, 0.3))
        self.computer_choice_image = Image(source='', size_hint=(1, 0.3))
        
        self.layout.add_widget(self.score_label)
        self.layout.add_widget(Label(text="Player Choice:", font_size=18))
        self.layout.add_widget(self.player_choice_image)
        self.layout.add_widget(Label(text="Computer Choice:", font_size=18))
        self.layout.add_widget(self.computer_choice_image)
        self.add_widget(self.layout)

    def update_score(self, player_score, computer_score):
        self.player_score = player_score
        self.computer_score = computer_score
        self.score_label.text = self.get_score_text()

    def update_choice(self, player_choice, computer_choice):
        self.player_choice = player_choice
        self.computer_choice = computer_choice
        player_image_path = f"D:/E21_2nd_Sem/Computing/Python/Final_Project/Code Set V2.6/Image/{player_choice}.png" 
        computer_image_path = f"D:/E21_2nd_Sem/Computing/Python/Final_Project/Code Set V2.6/Image/{computer_choice}.png"
        self.player_choice_image.source = player_image_path
        self.computer_choice_image.source = computer_image_path

    def get_score_text(self):
        return f"Player: {self.player_score} - Computer: {self.computer_score}"

class ResultScreen(Screen):
    def __init__(self, **kwargs):
        super(ResultScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        self.result_label = Label(text="", font_size=32)
        self.layout.add_widget(self.result_label)
        self.add_widget(self.layout)

    def display_final_result(self, player_score, computer_score):
        if player_score > computer_score:
            result_text = "You Win!"
        elif player_score < computer_score:
            result_text = "You Lose!"
        else:
            result_text = "It's a Draw!"
        
        self.result_label.text = result_text

class RPSApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WelcomeScreen(name='welcome'))
        sm.add_widget(GameScreen(name='game'))
        sm.add_widget(ResultScreen(name='result'))
        return sm

    def update_score(self, player_score, computer_score):
        self.root.get_screen('game').update_score(player_score, computer_score)

    def update_choice(self, player_choice, computer_choice):
        self.root.get_screen('game').update_choice(player_choice, computer_choice)

    def display_final_result(self, player_score, computer_score):
        result_screen = self.root.get_screen('result')
        result_screen.display_final_result(player_score, computer_score)
        self.root.current = 'result'

if __name__ == '__main__':
    RPSApp().run()
