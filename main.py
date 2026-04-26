import gi
import sys

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


@Gtk.Template(filename='calculator.ui')
class CalculatorWindow(Gtk.Window):
    __gtype_name__ = "CalculatorWindow"

    def __init__(self) -> None:
        super().__init__()
        self.first_number: float
        self.operator: str
        self.waiting_for_second_number: bool = False

    display: Gtk.Entry = Gtk.Template.Child()

    @Gtk.Template.Callback()
    def on_digit_pressed(self, button: Gtk.Button) -> None:
        label = button.get_label()

        if self.waiting_for_second_number:
            self.display.set_text("")
            self.waiting_for_second_number = False

        current_text = self.display.get_text()
        end_pos = self.display.get_text_length()

        if current_text == "0":
            self.display.delete_text(0, end_pos)

        self.display.insert_text(label, self.display.get_text_length())

    @Gtk.Template.Callback()
    def on_operator_pressed(self, operator: Gtk.Button) -> None:
        self.first_number = float(self.display.get_text() or "0")
        self.operator = operator.get_label() or ""
        self.waiting_for_second_number = True

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
