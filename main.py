import gi
import sys

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


class Calculator(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id='com.calculator.gminos', flags=Gio.ApplicationFlags.FLAGS_NONE)
        self.window: Gtk.Window | None = None
        self.entry: Gtk.Entry | None = None
        self.btns_ids = (
            "btn_1", 
            "btn_2", 
            "btn_3",
            "btn_4", 
            "btn_5", 
            "btn_6", 
            "btn_7", 
            "btn_8", 
            "btn_9", 
            "btn_0"
        )

    def do_activate(self) -> None:
        builder = Gtk.Builder()
        try:
            builder.add_from_file('calculator.ui')
        except Exception as e:
            print(f"Error: lading interface: {e}")
            return

        window_obj = builder.get_object('main_window')
        if not isinstance(window_obj, Gtk.Window):
            print("Error: not found'main_window'")
            return

        self.window = window_obj
        self.window.set_application(self)

        entry_obj = builder.get_object('display')
        if not isinstance(entry_obj, Gtk.Entry):
            print("Error: Not found display")
            return

        self.entry = entry_obj

        for btn_id in self.btns_ids:
            btn_id_obj = builder.get_object(btn_id)
            if isinstance(btn_id_obj, Gtk.Button):
                btn_id_obj.connect('clicked', self.on_digit_pressed)

        self.window.present()

    def on_digit_pressed(self, button: Gtk.Button) -> None:
        number = button.get_label()
        if self.entry is not None and number is not None:
            self.entry.set_text(number)


if __name__ == '__main__':
    app = Calculator()
    sys.exit(app.run(sys.argv))
