import gi
import sys

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


@Gtk.Template(filename='calculator.ui')
class CalculatorWindow(Gtk.Window):
    __gtype_name__ = "CalculatorWindow"

    display: Gtk.Entry = Gtk.Template.Child()

    @Gtk.Template.Callback()
    def on_digit_pressed(self, button: Gtk.Button) -> None:
        label = button.get_label()

        current_text = self.display.get_text()
        end_pos = self.display.get_text_length()

        if current_text == "0":
            self.display.delete_text(0, end_pos)

        self.display.insert_text(label, self.display.get_text_length())

    @Gtk.Template.Callback()
    def on_clear_pressed(self, _) -> None:
        self.display.set_text("")


class Calculator(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id='com.calculator.gminos', flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self) -> None:
        self.window = CalculatorWindow()
        self.window.set_application(self)
        self.window.present()


if __name__ == '__main__':
    app = Calculator()
    sys.exit(app.run(sys.argv))
