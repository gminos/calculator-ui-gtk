import gi
import sys

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


class Calculator(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id='com.calculator.gminos', flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.window: Gtk.Window | None = None
        self.entry: Gtk.Entry | None = None
        self.buttons_grid: Gtk.Widget | None = None

    def do_activate(self) -> None:
        builder = Gtk.Builder()
        try:
            builder.add_from_file('calculator.ui')
        except Exception as e:
            print(f"Error loading UI file 'calculator.ui': {e}")
            return

        window_obj = builder.get_object('main_window')
        if not isinstance(window_obj, Gtk.Window):
            print("Error: UI object 'main_window' not found or is not a Gtk.Window")
            return

        self.window = window_obj
        self.window.set_application(self)

        entry_obj = builder.get_object('display')

        if not isinstance(entry_obj, Gtk.Entry):
            print("Error: UI object 'display' not found or is not a Gtk.Entry")
            return

        self.entry = entry_obj

        grid_container = builder.get_object('gtk_grid')

        if not isinstance(grid_container, Gtk.Widget):
            print("Error: UI object 'gtk_grid' not found or is not a Gtk.Widget")
            return

        self.buttons_grid = grid_container

        current_button = self.buttons_grid.get_first_child()

        while current_button is not None:
            if current_button.has_css_class("number-button"):
                current_button.connect('clicked', self.on_digit_pressed)

            current_button = current_button.get_next_sibling()

        self.window.present()

    def on_digit_pressed(self, button: Gtk.Button) -> None:
        label = button.get_label()

        if self.entry is not None and label is not None:
            current_text = self.entry.get_text()
            end_pos = self.entry.get_text_length()

            if current_text == "0":
                self.entry.delete_text(0, end_pos)

            self.entry.insert_text(label, self.entry.get_text_length())


if __name__ == '__main__':
    app = Calculator()
    sys.exit(app.run(sys.argv))
