# main.py
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.core.window import Window
from kivy.uix.button import Button

# Set window size for landscape orientation
Window.size = (1280, 720)

class MainMenu(FloatLayout):
    def __init__(self, app, **kwargs):
        super(MainMenu, self).__init__(**kwargs)
        self.app = app

        self.bg_image = Image(source='bgAwal.png')
        self.add_widget(self.bg_image)

        self.click_sound = SoundLoader.load('buttonClick.mp3')  # Load sound here

        # Create a horizontal BoxLayout for the buttons
        button_layout = BoxLayout(
            orientation='horizontal',
            spacing=20,  # Jarak antar tombol
            size_hint=(None, None),  # Atur ukuran manual
            size=(400, 400),  # Ukuran layout tombol
            pos_hint={"center_x": 0.4, "center_y": 0.3}  # Posisikan di tengah
        )

        # Start Game Button
        self.start_button = Button(
            background_normal='mulai.png',
            background_down='mulai.png',
            size_hint=(None, None),  # Atur ukuran manual
            size=(400, 400),  # Ukuran tombol (lebar, tinggi)
            on_press=self.start_game
        )
        button_layout.add_widget(self.start_button)

        # Exit Game Button
        self.exit_button = Button(
            background_normal='keluar.png',
            background_down='keluar.png',
            size_hint=(None, None),  # Atur ukuran manual
            size=(400, 400),  # Ukuran tombol (lebar, tinggi)
            on_press=self.exit_game
        )
        button_layout.add_widget(self.exit_button)

        # Add the button layout to the main layout
        self.add_widget(button_layout)

        self.mute_image = Image(source='musikOn.png', size_hint=(0.1, 0.1), pos_hint={"x": 0.05, "top": 0.95})
        self.mute_image.bind(on_touch_down=self.toggle_sound)
        self.add_widget(self.mute_image)

        if self.app.background_sound and self.app.background_sound.state != 'play':
            self.app.background_sound.play()

    def toggle_sound(self, instance, touch):
        if self.app.background_sound.state == 'play':
            self.app.background_sound.stop()
            self.mute_image.source = 'mute.png'
        else:
            self.app.background_sound.play()
            self.mute_image.source = 'musikOn.png'
        self.mute_image.reload()

    def start_game(self, instance):
        if self.click_sound:
            self.click_sound.play()  # Play sound on button click
        from pilihLevel import LevelSelection  # Pindahkan import ke sini
        print("Navigating to Level Selection")  # Debug log
        self.app.change_screen(LevelSelection(self.app))

    def exit_game(self, instance):
        if self.click_sound:
            self.click_sound.play()  # Play sound on button click
        App.get_running_app().stop()  # Exit the game

class MyGameApp(App):
    def __init__(self, **kwargs):
        super(MyGameApp, self).__init__(**kwargs)
        self.background_sound = SoundLoader.load('musik.mp3')
        if self.background_sound:
            self.background_sound.loop = True
            self.background_sound.play()

    def build(self):
        return MainMenu(self)

    def change_screen(self, new_screen):
        self.root.clear_widgets()
        self.root.add_widget(new_screen)

if __name__ == '__main__':
    MyGameApp().run()
