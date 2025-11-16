"""
Simplified understanding of dynamic widgets using labels.
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelApp(App):
    """Main Program - Kivy App to display all names in a list"""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the Kivy GUI"""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_label_layout.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create a label widget for every name in names"""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

DynamicLabelApp().run()