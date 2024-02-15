from kivy.app import App
from kivy.uix.widget import Widget


class EdwardEditor(Widget):
    pass


class EdwardApp(App):
    def build(self):
        return EdwardEditor()


if __name__ == '__main__':
    EdwardApp().run()
