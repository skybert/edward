from kivy import app
from kivy.app import App
from kivy.base import Clock
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.codeinput import CodeInput
from kivy.uix.actionbar import ActionBar, ActionButton, ActionLabel, ActionPrevious
from kivy.uix.actionbar import ActionView
from pygments.lexers.markup import MarkdownLexer
from kivy.core.window import Window
from kivy.uix.filechooser import FileChooserIconView

class EdwardEditor(GridLayout):
    fn = "/tmp/foo.md"

    def save_file(self, **kwargs):
        print("saving file", self.fn)
        with open(self.fn, "w") as f:
            f.write(self.textinput.text)

    def read_file(self):
        self.label_fn.text = self.fn
        with open(self.fn, "r") as f:
            return f.read()

    def on_text(self, instance, value):
        pass

    def on_focus(self, instance, value):
        print("on focus")
        if not value:
            print(instance, "lost focus")
            self.save_file()

    def open_file(self, instance):
        print("open file")
        self.file_chooser = FileChooserIconView (

        )
        self.add_widget(self.file_chooser)
        pass

    def on_key_down(self, *args):
        # UI works best with scales starting one, hence +1 here
        self.label_licol.text = str(self.textinput.cursor_row + 1) + ":" + str(self.textinput.cursor_col + 1)


    def __init__(self, **kwargs):
        super(EdwardEditor, self).__init__(**kwargs)
        self.cols = 1
        self.action_view = ActionView()
        self.action_previous = ActionPrevious(
                title="Edward",
                with_previous=False)
        self.action_view.add_widget(self.action_previous)
        self.cmd_open_file = ActionButton(
            text="Open",
            on_press=self.open_file)
        self.action_view.add_widget(self.cmd_open_file)


        self.label_licol = ActionLabel(text="1:2")
        self.label_fn = ActionLabel(text="/foo/bar")
        self.action_view.add_widget(self.label_fn)
        self.action_view.add_widget(self.label_licol)

        self.action_bar = ActionBar()
        self.action_bar.add_widget(self.action_view)
        self.add_widget(self.action_bar)
        self.textinput = CodeInput(
            text=self.read_file(),
            lexer=MarkdownLexer()
        )
        self.textinput.cursor = (0, 0)

        self.textinput.bind(text=self.on_text)
        self.textinput.bind(focus=self.on_focus)
        Window.bind(on_key_down=self.on_key_down)

        self.add_widget(self.textinput)

class EdwardApp(App):
    def build(self):
        editor = EdwardEditor()

        # Fails with: TypeError: EdwardEditor.save_file() takes 1 positional argument but 2 were given
        # Clock.schedule_interval(editor.save_file, 10.0/60.0)

        return editor


if __name__ == '__main__':
    EdwardApp().run()
