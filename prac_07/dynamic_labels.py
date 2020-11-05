from kivy.app import App
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.core.window import Window

names = ['Luke', 'John', 'Bob', 'Gary', 'Fred']


class DynamicLabelsApp(App):
    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (1000, 600)
        self.title = "Dynamic Labels App"
        self.root = Builder.load_file('dynamic_labels.kv')

        for name in names:
            temp_label = Label(text=name, id=name)
            self.root.ids.labels_box.add_widget(temp_label)


        return self.root


DynamicLabelsApp().run()
