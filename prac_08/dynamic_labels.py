from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        # basic data (model) example - dictionary of names: phone numbers
        self.names = ["Jeremiah", "Aberforth", "Ansel", "Birlb", "Cruuth", "Fiore", "Norm"]

    def create_labels(self):
        """Create labels from data and add them to the GUI."""
        for name in self.names:
            # create a label for each data entry, specifying the text
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root


DynamicLabelsApp().run()
