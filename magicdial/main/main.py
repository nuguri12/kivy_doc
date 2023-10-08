from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.metrics import dp, sp
from kivy.uix.anchorlayout import AnchorLayout

class MagicDialApp(App):
    def build(self):
        layout = AnchorLayout()  # Use AnchorLayout to center the button
        btn = MyButton(text='Click Me!')
        layout.add_widget(btn)
        return layout

class MyButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (None, None)
        self.width = dp(200)
        self.height = dp(50)  # Set a height for the button
        self.font_size = sp(20)
        self.background_color = (1, 0, 0, 1)  # Red color

if __name__ == '__main__':
    MagicDialApp().run()
