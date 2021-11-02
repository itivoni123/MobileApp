# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):

        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text
        age = self.age.text

        print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color} and your age is {age}')
        # Print it to the screen
        # self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!'))

        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""
        self.age.text = ""


class Myapp(App):
    def build(self):
        return MyGridLayout()
# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.from kivy.app import App
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Myapp().run()
    # print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
