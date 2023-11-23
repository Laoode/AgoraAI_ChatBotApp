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



def navbar_style():
    # styling for the navbar
    return {
        "border_radius": ft.border_radius.vertical(bottom=30),
        "shadow": ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color="#fc4795",
        ),
        "gradient": ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.aligment.bottom_right,
            colors=["#fc4795", "#7c59f0"]
        ),
        "width": 420,
        "height": 800,
        "padding": 10,
    }
# Style 
def prompt_style():
  return {
    "width": 420,
    "height": 40,
    "border_color": "white",
    "content_padding": 10,
    "cursor_color": "white",
  }
#main content area atau bagian home dari chatbot
class MainContentArea(ft.Container):
  def __init__(self):
    #super() merupakan inheritance atau pewarisan metode untuk mengambil atribut dari class parent
    super().__init__(**main_style())
    self.chat = ft.ListView(
      expand=True,
      height=200,
      spacing=15,
      auto_scroll=True,
    )
    self.content = self.chat
#before pushing text to UI - create a class that generates the UI for the actual text prompts
class CreateMessage(ft.Column):
    def __init__(self, name: str, message: str):
        self.name = name #show's which prompt is whos
        self.message = message
        self.text= ft.Text(self.message)
        super().__init__(spacing=4)
        self.controls=[ft.Text(self.name, opacity=0.6), self.text]

#user input class
class Prompt(ft.TextField):
    def __init__(self, chat:ft.ListView):
        super().__init__(**prompt_style(), on_submit=self.run_prompt)
        #need access to main chat area -from MainContentArea class
        self.chat: ft.ListView =chat
    # output display is working - but let's add animation to text output...

# Mashaf start
def animate_text_output(self, name:str, prompt:str):
    word_list: list =[]
    msg= CreateMessage(name,"")
    self.chat.controls.append(msg)
        
    for word in list(prompt):
        word_list.append(word)
        msg.text.value="".join(word_list)
        self.chat.update()
        time.sleep(0.008)
    
def user_output(self,prompt):
        self.animate_text_output(name="Me", prompt=prompt)
# Mashaf end       
# defining the main function
def main(page:ft.Page):
    # setting the page title
    page.title = "Kelompok1.chatbot.ai"




