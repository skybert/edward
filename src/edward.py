#! /usr/bin/env python3
#
# by torstein@skybert.net
#
"""
Lean and fast Markdown editor for Android and Linux
"""
import sys
import os

from pathlib import Path

from kivy.app import App, Widget
from kivy.base import Clock
from kivy.uix.popup import Popup

from pygments.lexers.markup import MarkdownLexer


class EdwardEditor(Widget):
    """
    The root widget of Edward the editor
    """

    def on_cursor_pos(self, pos):
        """
        Triggered when the cursor, the caret, position
        changes. Note, This is different from the mouse cursor
        position.
        """
        self.ids.lbl_linecol.text = (
            f"{self.ids.code_input.cursor[1] + 1}:{self.ids.code_input.cursor[0] + 1}"
        )


class FileDialogPopup(Popup):
    """
    What it says on the tin.
    """
    def file_selected(self, selection):
        """
        Triggered when one or more _files_ have been selected in
        the file dialogue. Closes the popup.
        """
        self.dismiss()


class EdwardApp(App):
    """
    The Edward Kivi app class.
    """

    file_chooser_dir = str(Path.home())
    fn = "/tmp/foo.md"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def show_file_dialog(self):
        """
        Show a file dialogue that also works on Android (modal).
        """
        file_dialog = FileDialogPopup()
        file_dialog.ids.file_chooser.path = self.file_chooser_dir
        file_dialog.open()

    def on_file_changed(self, new_text):
        """
        Triggered whenever the text inside the CodeInput widget
        has changed.
        """
        self.root.ids.lbl_fn_state.text = "*"

    def file_selected(self, selected_file):
        """
        Triggered when a file has been selected in the file
        dialogue.
        """
        if selected_file:
            p = Path(selected_file[0])
            self.file_chooser_dir = str(p.parent)
            self.fn = selected_file[0]
            self.open_file()
        else:
            self.root.ids.lbl_fn.text = "No file selected"

    def open_file(self):
        """
        Opens the file passed.
        """
        self.root.ids.lbl_fn.text = f"File: {self.fn}"
        with open(self.fn, "r", encoding="UTF-8") as f:
            self.root.ids.code_input.text = f.read()

    def save_file(self, call_interval=1.0):
        """
        Saves/flushed the file to disk.
        """
        if not self.fn:
            return

        with open(self.fn, "w", encoding="UTF-8") as f:
            f.write(self.root.ids.code_input.text)
        self.root.ids.lbl_fn_state.text = " "

    def build(self):
        editor = EdwardEditor()
        editor.ids.code_input.lexer = MarkdownLexer()
        # Auto save every 10 seconds
        Clock.schedule_interval(self.save_file, 5.0)
        return editor


if __name__ == "__main__":
    file_name = None

    # Not using argparse here as it interferes with Kivy's
    # argparsing. (yes, I know about KIVY_NO_ARGS=1)
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
        if not os.path.exists(file_name):
            with open(file_name, "w", encoding="UTF-8"):
                print("Created new file", file_name)

    app = EdwardApp()
    app.fn = file_name
    app.run()
