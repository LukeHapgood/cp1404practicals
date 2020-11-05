from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class Convert_Miles_To_km_App(App):
    miles = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (500, 200)
        self.title = "Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_to_km.kv')
        return self.root

    def handle_change(self, change):
        """Adjust the input miles by a specified value"""
        value = self.test_input()
        result = value + change
        self.root.ids.input_miles.text = str(result)
        self.handle_conversion()

    def handle_conversion(self):
        """Convert input miles to kilometers"""
        value = self.test_input()
        self.miles = str(value * MILES_TO_KM)

    def test_input(self):
        try:
            input = float(self.root.ids.input_miles.text)
            return input
        except ValueError:
            return 0

Convert_Miles_To_km_App().run()
