"""
CP1404/CP5632 Practical
Kivy GUI program to convert miles to kilometres
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty

MILES_TO_KMS = 1.60934


class ConvertMilesKmApp(App):
    """ ConvertMilesKmApp is a kivy app for converting miles to km """
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (1000, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        self.message = "Convert miles to km"
        return self.root

    def handle_increment(self, value, increment):
        result = self.get_valid_input(value) + increment
        self.root.ids.km_input.text = str(result)

    def handle_calculate(self, value):
        """ handle calculation (could be button press or other call), output result to label widget """
        result = self.get_valid_input(value) * MILES_TO_KMS
        self.root.ids.output_label.text = str(result)

    def get_valid_input(self, value):
        try:
            value = float(self.root.ids.km_input.text)
        except ValueError:
            value = 0.0
        return value


ConvertMilesKmApp().run()
