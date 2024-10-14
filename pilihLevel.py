# pilihLevel.py
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.audio import SoundLoader
from kivy.graphics import Ellipse, Color
from kivy.uix.button import Button

class OvalButton(Button):
    def __init__(self, click_sound, **kwargs):
        super(OvalButton, self).__init__(**kwargs)
        self.click_sound = click_sound  

        # Atur latar belakang tombol menjadi transparan
        self.background_color = (0, 0, 0, 0)  

        with self.canvas.before:
            Color(*self.background_color)  
            self.oval = Ellipse(size=self.size, pos=self.pos)  

        self.bind(size=self._update_oval, pos=self._update_oval)

    def _update_oval(self, *args):
        self.oval.pos = self.pos
        self.oval.size = self.size

    def on_press(self):
        if self.click_sound:
            self.click_sound.play()  

class LevelSelection(FloatLayout):
    def __init__(self, app, **kwargs):
        super(LevelSelection, self).__init__(**kwargs)
        self.app = app

        if self.app.background_sound and self.app.background_sound.state != 'play':
            self.app.background_sound.play()

        # Menambahkan gambar latar belakang
        self.bg_image = Image(source='bgLevel.png')
        self.add_widget(self.bg_image)

        click_sound = SoundLoader.load('buttonClick.mp3')

        # Menambahkan gambar Level 1
        level1_image = Image(
            source='level1.png',
            size_hint=(None, None),
            size=(400, 400),
            pos_hint={"center_x": 0.35, "center_y": 0.5}
        )
        self.add_widget(level1_image)

        # Menambahkan gambar Level 2
        level2_image = Image(
            source='level2.png',
            size_hint=(None, None),
            size=(400, 400),
            pos_hint={"center_x": 0.65, "center_y": 0.5}
        )
        self.add_widget(level2_image)

        # Menambahkan gambar Level 3
        level3_image = Image(
            source='level3.png',
            size_hint=(None, None),
            size=(400, 400),
            pos_hint={"center_x": 0.5, "center_y": 0.2}
        )
        self.add_widget(level3_image)

        # Tombol Kembali
        back_button_image = Image(
            source='back.png',
            size_hint=(0.1, 0.1),
            pos_hint={"right": 0.9, "top": 0.95}
        )
        back_button_image.bind(on_touch_down=self.go_back)
        self.add_widget(back_button_image)

        # Tombol Mute
        self.mute_image = Image(source='musikOn.png', size_hint=(0.1, 0.1), pos_hint={"x": 0.05, "top": 0.95})
        self.mute_image.bind(on_touch_down=self.toggle_sound)
        self.add_widget(self.mute_image)

    def toggle_sound(self, instance, touch):
        if self.app.background_sound.state == 'play':
            self.app.background_sound.stop()
            self.mute_image.source = 'mute.png'
        else:
            self.app.background_sound.play()
            self.mute_image.source = 'musikOn.png'
        self.mute_image.reload()

    def go_back(self, instance, touch):
        if touch.button == 'left':
            if self.app.background_sound: 
                click_sound = SoundLoader.load('buttonClick.mp3')
                click_sound.play()
            from main import MainMenu
            self.app.change_screen(MainMenu(self.app))

    def go_to_level1(self, instance):
        from level1 import Level1
        self.app.change_screen(Level1(self.app))

    def go_to_level2(self, instance):
        from level2 import Level2
        self.app.change_screen(Level2(self.app))

    def go_to_level3(self, instance):
        from level3 import Level3
        self.app.change_screen(Level3(self.app))
