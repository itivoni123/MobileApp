# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file('update_label.kv')


class MyLayout(Widget):
    def press(self):
        # Create variables for our widget
        name = self.ids.name_input.text
        print(name)

        # Update the label
        self.ids.name_label.text = f'Hello {name}!'

        # Clear input box
        self.ids.name_input.text = ''


class DJApp(App):
    def build(self):
        # Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()
# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.from kivy.app import App
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    DJApp().run()
    # print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
