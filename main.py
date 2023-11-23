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
        
    # Mas Dimas your code put here
    
    # method : run all methods when started
    def run_prompt(self, event):
        #set the value of the user prompt
        text = event.control.value

        # disabling input field can also be added ...
        self.value = ""
        self.update()

        # first, we output the user prompt
        self.user_output(prompt=text)

        # second, we display GPT output
        self.gpt_output(prompt=text)
        
# Mas Fauzan your code put here


class AnimatedBox(ft.UserControl):
    def __init__(self, border_color, bg_color, rotate_angle):
        self.border_color = border_color
        self.bg_color = bg_color
        self.rotate_angle = rotate_angle
        super().__init__()

    def build(self):
        return ft.Container(
            width=48,
            height=48,
            border=ft.border.all(2.5, self.border_color),
            bgcolor=self.bg_color,
            border_radius=2,
            rotate=ft.transform.Rotate(self.rotate_angle, alignment.center),
            animate_rotation=ft.animation.Animation(700, "easeInOut"),
        )

class userInputField(ft.UserControl):
    def__init__(self,icon_name,text_hint,hide,function,emails:bool, function_check:bool):
        self.icon_name = icon_name
        self.text_hint = text_hint
        self.hide = hide
        self.function_emails = function_emails
        seld.function_check = function_check
        super().__init()
    
    def return_email_prefix(self, e):
        email = self.controls[0].content.controls[1].value
        if e.control.data in email:
            pass
        else:
            self.controls[0].content.controls[1].value+= e.control.data
            self.controls[0].content.controls[2].offset = ft.transform.Offset(0.5, 0)
            self.controls[0].content.controls[2].opacity = 0
            self.update()
                    








def prefix_email_containers(self):
    email_labels =["@gmail.com", "@hotmail.com"]
    label_title = ["GMAIL", "MAIL"]
    __ = ft.Row(spacing=1, alignment=ft.MainAxisAlignment.END)
    for index, label in enumerate(email_labels):
        __.controls.append(
            ft.Container(
            width=45,
            height=30,
            alignment=ft.alignment.center,
            data=label,
            on_click=lambda e: self.return_email_prefix(e),
            content=ft.Text(
                label_title[index],
                size=9,
                weight="bold"
                ),
            )
        )
    return ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.END,
        spacing=2,
        opacity=0,
        animate_opacity=200,
        offset=ft.transform.Offset(0.35, 0),
        animate_offset=ft.animation.Animation(400, "decelerate"),
        controls=[__]
    )



    def off_focus_input_check(self):
        return ft.Container(
            opacity=0,
            offset=ft.transform.Offset(0, 0),
            animate=200,
            border_radius=6,
            width=18,
            height=18,
            alignment=ft.alignment.center,
            content=ft.Checkbox(
                fill_color="#7df6dd",
                check_color="black",
                disabled=True,
            )
        )
    
    def get_prefix_emails(self, e):
        if self.function_emails:
            email = self.controls[0].content.controls[1].value
            if e.data:
                if "@gmail.com" in email or "@hotmail.com" in email:
                    self.controls[0].content.controls[2].offset = ft.transform.Offset(0, 0)
                    self.controls[0].content.controls[2].opacity = 0
                    self.update()
                else:
                    self.controls[0].content.controls[2].offset = ft.transform.Offset(-0.15, 0)
                    self.controls[0].content.controls[2].opacity = 1
                    self.update()
            else:
                self.controls[0].content.controls[2].offset = ft.transform.Offset(0.5, 0)
                self.controls[0].content.controls[2].opacity = 0
                self.update()
        else:
            pass

# IRFAN START
def get_green_check(self,e):
    if self.function_check:
        email = self.controls[0].content.controls[3].value
        password = self.controls[0].content.controls[3].password
        if (email):
            if "@gmail.com" in email or "@hotmail.com" in email or password:
                time.sleep(0.5)
                self.controls[0].content.controls[3].offset = ft.transform.Offset(-2,0)
                self.controls[0].content.controls[3].opacity = 1
                self.update()
                time.sleep(0.2)
                self.controls[0].content.controls[3].content.value = True
                time.sleep(0.1)
                self.update()
            else:
                self.controls[0].content.controls[3].offset = ft.transform.Offset(0, 0)
                self.controls[0].content.controls[3].opacity = 0
                self.update()
            
        else:
            pass
# IRFAN END

# Madin
    def build(self):
        return ft.Container(
            width=320,
            height=40,
            border=ft.border.only(bottom=ft.border.BorderSide(0.5, "white45")),
            content=ft.Row(
                spacing=20,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Icon(
                        name=self.icon_name,
                        size=14,
                        opacity=0.85,
                    ),
                    ft.TextField(
                        border_color="transparent",
                        bgcolor="transparent",
                        height=20,
                        width=180,
                        text_size=12,
                        content_padding=3,
                        cursor_color="white",
                        hint_text=self.text_hint,
                        hint_style=ft.TextStyle(size=11),
                        password=self.hide,
                        on_change=lambda e: self.get_prefix_emails(e),
                        on_blur=lambda e: self.get_green_check(e),
                    ),
                    self.prefix_email_containers(),
                    self.off_focus_input_check(),
                ],
            )
        )

def tab1_content():
    return Card(
        elevation=15,
        content=ft.Container(
            width=300,  # Tambahkan properti width di sini
            height=612,
            bgcolor="#ebeefa",
            border_radius=6,
            content=Column(
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[ 
                    Divider(height=20, color='transparent'),
                    Stack(
                        controls=[
                            AnimatedBox("#e9665a", None, 0),
                            AnimatedBox("#7df6dd", "#ebeefa", pi / 4),
                        ]
                    ),
                    Divider(height=20, color='transparent'),
                    Column(
                        alignment=MainAxisAlignment.CENTER,
                        spacing=5,
                        controls=[
                            Text("Sign In Below", size=22, weight='bold'),
                            Text("          Agora-AI", size=13, weight='bold'),
                        ],
                    ),
                    Divider(height=20, color='transparent'),
                    UserInputField(icons.PERSON_ROUNDED, "Email", False, True, True),
                    Divider(height=2, color='transparent'),
                    UserInputField(icons.LOCK_OPEN_ROUNDED, "Password", True, False, True),

                    Divider(height=20, color='transparent'),
                    Row(
                        width=320,
                        alignment=MainAxisAlignment.END,
                        controls=[Text("Forgot Password?", size=9)],
                    ),
                    Divider(height=20, color='transparent'),
                    SignInButton("Sign In"),
                    Divider(height=20, color='transparent'),
                    Text("Footer text goes in here.", size=10, color='black'),
                ],
            ),
        ),
    )
# defining the main function
def main(page:ft.Page):
    # setting the page title
    page.title = "Kelompok1.chatbot.ai"

    
