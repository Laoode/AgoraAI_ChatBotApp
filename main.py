# # import the library
import flet as ft

# ADE start
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
# ADE end