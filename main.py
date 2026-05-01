import gi
import sys

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


@Gtk.Template(filename='calculator.ui')
class CalculatorWindow(Gtk.Window):
    __gtype_name__ = "CalculatorWindow"

    def __init__(self) -> None:
        super().__init__()
        self.operand_a: float = 0.0
        self.operator: str = ""
        self.is_new_input: bool = False

    display: Gtk.Entry = Gtk.Template.Child()

    @Gtk.Template.Callback()
    def on_digit_pressed(self, button: Gtk.Button) -> None:
        label = button.get_label()

        if self.is_new_input:
            self.display.set_text("")
            self.is_new_input = False

        current_text = self.display.get_text()
        end_pos = self.display.get_text_length()

        if current_text == "0":
            self.display.delete_text(0, end_pos)

        self.display.insert_text(label, self.display.get_text_length())

    @Gtk.Template.Callback()
    def on_operator_pressed(self, operator: Gtk.Button) -> None:
        self.operand_a = float(self.display.get_text() or "0")
        self.operator = operator.get_label() or ""
        self.is_new_input = True

    @Gtk.Template.Callback()
    def on_clear_pressed(self, _) -> None:
        self.display.set_text("")

    @Gtk.Template.Callback()
    def on_equal_pressed(self, _) -> None:
        operand_b = float(self.display.get_text() or "0")
        result = 0.0

        match self.operator:
            case "+":
                result = self.operand_a + operand_b
            case "-":
                result = self.operand_a - operand_b
            case "*":
                result = self.operand_a * operand_b
            case "/":
                try:
                    result = self.operand_a / operand_b
                except ZeroDivisionError:
                    self.display.set_text("division by zero")
                    self.is_new_input = True
                    return
            case _:
                return

        self.display.set_text(f'{result:g}')
        self.is_new_input = True


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
