#!/usr/bin/env python3

from kivy.app import App

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView

from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.textinput import TextInput
from kivy.uix.codeinput import CodeInput

from kivy.config import Config

from back import *

Config.set('input', 'mouse', 'mouse,multitouch_on_demand') 
Config.set("graphics","resizable","0")
Config.set("graphics","width","700")
Config.set("graphics","height","500")


ciphers = (
  "Caesar Cipher", "Bacon"
)

comments = (
    "### Caesar ###",

)

class CryptographyApp(App):

    def getCipher(self, mode):
        if mode.id in ['E','D']:
            self.result.font_size = 14
            if not self.message.text: 
                self.result.text = ":: Message is not found ::"; return
            if self.toggle[0].state == 'down':
                self.result.text = caesar(mode.id, self.message.text, self.key.text)
        else:
            switch, code = False, ""
            self.result.font_size = 12
            self.result.text = ""
            for index in range(len(ciphers)):
                if self.toggle[index].state == 'down':
                    with open("back.py") as file:
                        for string in file:
                            if switch:
                                if comments[index] not in string:
                                    code += string
                                else: break
                            if comments[index] in string:
                                switch = True
                    self.result.text += code
        self.result.cursor = (0,0)

    def clear(self, mode):
        self.result.font_size = 14
        self.key.text = ""
        self.message.text = ""
        self.result.text = ""

    def build(self):
        root = BoxLayout(orientation = "horizontal", padding = 3)

        left = ScrollView(size_hint = [.4,1])
        right = BoxLayout(orientation = "vertical")

        leftGrid = GridLayout(cols = 1, size_hint_y = None)
        leftGrid.bind(minimum_height = leftGrid.setter('height'))

        self.toggle = [0 for _ in range(35)]

        for index in range(len(ciphers)):
            
            self.toggle[index] = ToggleButton(
                id = str(index), text = ciphers[index], 
                group = 'cipher', height = 30, 
                state = "normal", size_hint_y = None)
            leftGrid.add_widget(self.toggle[index])

        left.add_widget(leftGrid)

        topBox = BoxLayout(orientation = "horizontal", size_hint = [1,.33])

        self.key = TextInput(hint_text = "Key", multiline = False, font_size = 16)
        topBox.add_widget(self.key)

        rightTopBox = BoxLayout(orientation = "vertical", size_hint = [.5,1])
        rightTopBox.add_widget(Button(id = 'E', text = "Encrypt", on_press = self.getCipher))
        rightTopBox.add_widget(Button(id = 'D', text = "Decrypt", on_press = self.getCipher))

        topBox.add_widget(rightTopBox)
        right.add_widget(topBox)

        self.message = TextInput(hint_text = "Message", font_size = 16)
        right.add_widget(self.message)

        self.result = CodeInput(readonly = True, hint_text = "Result", font_size = 14, background_color = [1,1,1,.8])
        right.add_widget(self.result)

        downBox = BoxLayout(orientation = "horizontal", size_hint = [1,.15])

        downBox.add_widget(Button(id = 'C', text = "Code", on_press = self.getCipher))
        downBox.add_widget(Button(text = "Clear", on_press = self.clear))

        right.add_widget(downBox)

        root.add_widget(left)
        root.add_widget(right)

        return root

if __name__ == "__main__":
    CryptographyApp().run()