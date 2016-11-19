from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
	def build():
		return Button(text='Hola mundo')

TestApp().run()