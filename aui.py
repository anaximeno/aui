"""Action UI - Basic GTK Based UI Toolkit for Nemo Actions.
@Author: Anaxímeno Brito <anaximenobrito@gmail.com>
@Url: https://github.com/anaximeno/aui
@Version: 0.1
@License: TODO
"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class DialogWindow(Gtk.Window):
    def __init__(
        self,
        message_type,
        content_message: str,
        title: str = None,
        content_title: str = None,
        buttons=None,
    ) -> None:
        super().__init__(title=title)
        self.dialog = Gtk.MessageDialog(
            flags=0,
            transient_for=self,
            title=title,
            message_type=message_type,
            text=content_title,
            buttons=buttons,
        )
        self.dialog.format_secondary_text(content_message)

    def run(self):
        return self.dialog.run()

    def destroy(self):
        self.dialog.destroy()
        super().destroy()


class InfoDialogWindow(DialogWindow):
    def __init__(self, message: str, title: str = None) -> None:
        super().__init__(
            message_type=Gtk.MessageType.INFO,
            title=title,
            content_message=message,
            buttons=Gtk.ButtonsType.OK,
        )


class QuestionDialogWindow(DialogWindow):
    RESPONSE_YES = "y"
    RESPONSE_NO = "n"

    def __init__(
        self,
        message: str,
        title: str = None,
    ) -> None:
        super().__init__(
            message_type=Gtk.MessageType.QUESTION,
            content_message=message,
            title=title,
            buttons=Gtk.ButtonsType.YES_NO,
        )

    def run(self):
        """Returns `y` if the user clicked yes, or `n` if the user clicked no.
        If no response was given (by closing the window or clicking escape) it
        returns python `None`.
        """
        result = super().run()
        if result == Gtk.ResponseType.YES:
            return self.RESPONSE_YES
        elif result == Gtk.ResponseType.NO:
            return self.RESPONSE_NO
        return None
