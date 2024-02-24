from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.codeinput import CodeInput
from pygments.lexers.markup import MarkdownLexer

class EdwardEditor(GridLayout):
    fn = "/tmp/foo.md"

    def save_file(self):
        with open(self.fn, "w") as f:
            f.write(self.textinput.text)
    def read_file(self):
        with open(self.fn, "r") as f:
            return f.read()
    
    def on_text(self, instance, value):
        pass

    def on_focus(self, instance, value):
        print("on focus")
        if not value:
            print(instance, "lost focus")
            self.save_file()

    def __init__(self, **kwargs):
        super(EdwardEditor, self).__init__(**kwargs)
        self.cols = 1
        # self.textinput = TextInput(
        #     text=self.read_file()
        # )
        self.textinput = CodeInput(
            text=self.read_file(),
            lexer=MarkdownLexer(),
        )
        self.textinput.bind(text=self.on_text)
        self.textinput.bind(focus=self.on_focus)

        self.add_widget(self.textinput)





class EdwardApp(App):
    def build(self):
        return EdwardEditor()


if __name__ == '__main__':
    EdwardApp().run()
