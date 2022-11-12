# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang import Builder

# Set the App size
Window.size = (500, 700)
Builder.load_file('calc.kv')


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):

        prior = self.ids.calc_input.text
        # Test for error first
        if "Error" in prior:
            prior = ''
        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    # create a addition function
    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        # slap a plus sign to the textbox
        self.ids.calc_input.text = f'{prior}{sign}'

    def equals(self):

        prior = self.ids.calc_input.text
        # Error handling
        try:

            # Evaluate the math from the text box
            answer = eval(prior)
            self.ids.calc_input.text = str(answer)
        except:
            self.ids.calc_input.text = "Error"

        '''
        # Addition
        if "+" in prior:
            num_list = prior.split("+")
            answer = 0.0
            for number in num_list:
                answer = answer + float(number)
            # print the answer in the textbox
            self.ids.calc_input.text = str(answer)
        '''

    # Create decimal function
    def dot(self):
        prior = self.ids.calc_input.text
        num_list = prior.split("+")
        if "+" in prior and "." not in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior
        elif "." in prior:
            pass
        else:
            # Add a decimal to the end of the text
            prior = f'{prior}.'
            # Output back to the textbox
            self.ids.calc_input.text = prior

    # Create function to make positive or negative
    def pos_neg(self):
        prior = self.ids.calc_input.text

        # Test to see if there's a - sign already
        if "-" in prior:
            self.ids.calc_input.text = f'{prior.replace("-", " ")}'
        else:
            self.ids.calc_input.text = f'-{prior}'

    # Create function to remove last character in textbox
    def remove(self):
        prior = self.ids.calc_input.text
        # Remove the last item in the text box
        self.ids.calc_input.text = prior[:-1]


class CalculatorApp(App):
    def build(self):
        # Window.clearcolor = (1, 1, 1, 1)
        return MyLayout()


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.from kivy.app import App
    # print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    CalculatorApp().run()
    # print_hi('PyCharm')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
