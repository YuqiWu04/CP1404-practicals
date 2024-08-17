from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    def build(self):
        """build the Kivy app from the kv file """
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root
    def handle_greet(self):
        """Use the greet button to display the greet name"""
        print("test")
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"

    def handle_clear(self):
        """Use the clear button to clear all content into empty"""
        self.root.ids.output_label.text = ' '
        self.root.ids.input_name.text = ' '

BoxLayoutDemo().run()