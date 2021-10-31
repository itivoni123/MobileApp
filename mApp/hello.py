# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        # Set columns
        self.cols = 1

        # Create a second gridlayout
        self.top_grid = GridLayout()
        self.top_grid.cols = 2

        # Add widgets
        self.top_grid.add_widget(Label(text="Name: "))

        # Add Input Box
        self.name = TextInput(multiline=True)
        self.top_grid.add_widget(self.name)

        # Add widgets
        self.top_grid.add_widget(Label(text="Favorite Pizza: "))

        # Add Input Box
        self.pizza = TextInput(multiline=True)
        self.top_grid.add_widget(self.pizza)

        # Add widgets
        self.top_grid.add_widget(Label(text="Favorite Color: "))

        # Add Input Box
        self.color = TextInput(multiline=True)
        self.top_grid.add_widget(self.color)

        # Add the new top_grid to our app
        self.add_widget(self.top_grid)

        # Create a Submit Button
        self.submit = Button(text="Submit", font_size=72)
        # Bind the Button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)

    def press(self, instance):

        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        #print(f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}')
        # Print it to the screen
        self.add_widget(Label(text=f'Hello {name}, you like {pizza} pizza, and your favorite color is {color}!'))

        # Clear the input boxes
        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()
# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    MyApp().run()
    # print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
