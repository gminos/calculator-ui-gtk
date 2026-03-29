import gi
import sys

gi.require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


class Calculator(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id='com.calculator.gminos', flags=Gio.ApplicationFlags.FLAGS_NONE)

    def do_activate(self):
        builder = Gtk.Builder()
        try:
            builder.add_from_file('calculator.ui')
        except Exception as e:
            print(f"Error cargando la interfaz: {e}")
            sys.exit(1)

        self.window = builder.get_object('main_window')
        self.window.set_application(self)
        self.window.present()


if __name__ == '__main__':
    app = Calculator()
    sys.exit(app.run(sys.argv))
