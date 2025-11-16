"""
Converts miles to kilometres using Kivy
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILE_TO_KM_CONVERSION = 1.609344

class ConvertMilesKmApp(App):
    message = StringProperty()

    """ConvertMilesKmApp is a Kivy App for converting miles to kilometres"""
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km_layout.kv')
        self.message = "Type in miles then press convert"
        return self.root

    def change_value(self, value):
        """Increases or decreases value of input by value"""
        try:
            mile = float(self.root.ids.input_text.text)
            mile += value
            self.root.ids.input_text.text = str(mile)
        except ValueError:
            self.message = "Value must be a number"

    def event_handler(self):
        """Converts miles to km"""
        try:
            mile = float(self.root.ids.input_text.text)
            km = mile * MILE_TO_KM_CONVERSION
            self.message = str(km)
        except ValueError:
            self.message = "Value must be a number"

ConvertMilesKmApp().run()