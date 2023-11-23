# import the library
import flet as ft
from flet import *
from math import pi
import time
import threading
import openai

openai.api_key="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"
def main_style():
   #the styling properties for the main content area class
   return {
       "width": 420,
       "height": 450,
       "bgcolor": "ebeefa",
       "border_radius": 10,
       "padding": 15,
   } 

# defining the main function
def main(page:ft.Page):
    # setting the page title
    page.title = "Kelompok1.chatbot.ai"
    


    # text control
    text= ft.Text(value='Testing Home', color="blue")
    page.controls.append(text)
    page.update()
# starting the app
ft.app(target=main, view = ft.WEB_BROWSER)