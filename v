# Import the required libraries and modules
import flet as ft
from flet import *
from math import pi
import time
import openai

# Set API key for OpenAI
openai.api_key = "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" #API IRFAN
# openai.api_key = "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" #API RIO

# The styling properties for the main content area class/ for chat AI
def main_style():
    return {
        "width": 420,
        "height": 450,
        "bgcolor": "#ebeefa",  
        "border_radius": 10,
        "padding": 15,
    }

def navbar_style():
    # styling for the navigation bar
    return {
        "border_radius": ft.border_radius.vertical(bottom=30),
        "shadow": ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color="#fc4795",
        ),
        "gradient": ft.LinearGradient(
            begin=ft.alignment.top_left,
            end=ft.alignment.bottom_right,
            colors=["#fc4795", "#7c59f0"]
        ),
        "width": 420,
        "height": 800,
        "padding": 10,
    }

# Function to set the display style of the prompt
def prompt_style():
    return {
        "width": 420,
        "height": 40,
        "border_color": "white",
        "content_padding": 10,
        "cursor_color": "white",
    }

#main content area class
class MainContentArea(ft.Container):
    def __init__(self):
        super().__init__(**main_style())
        self.chat = ft.ListView(
            expand=True,
            height=200,
            spacing=15,
            auto_scroll=True,
        )
        self.content = self.chat

#Before pushing text to UI - create a class that generates the UI for the actual text prompts
class CreateMessage(ft.Column):
    def __init__(self, name: str, message: str):
        self.name = name #show's which prompt is whos
        self.message = message
        self.text = ft.Text(self.message)
        super().__init__(spacing=4)
        self.controls = [ft.Text(self.name, opacity=0.6), self.text]

# OOP Polimorphism
class MessageOutput(ft.UserControl):
    def __init__(self, name: str, chat: ft.ListView):
        self.name = name
        self.chat: ft.ListView = chat
        super().__init__()
        
    # output display is working - but let's add animation to text output...
    def animate_text_output(self, prompt: str):
        word_list = []
        msg = CreateMessage(self.name, "")
        self.chat.controls.append(msg)

        #list(prompt) => we deconstruct the prompt text into sepreate characters, and loop over them
        for word in list(prompt):
            word_list.append(word)
            msg.text.value = "".join(word_list)
            self.chat.update()
            time.sleep(0.008)
class UserOutput(MessageOutput):
    def __init__(self, chat: ft.ListView):
        super().__init__("Me", chat)

    def display_output(self, prompt):
        self.animate_text_output(prompt)
class GptOutput(MessageOutput):
    # the following is the basic response to get chat GPT answer
    def __init__(self, chat: ft.ListView):
        super().__init__("Agora", chat)

    def display_output(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        response = response['choices'][0]['message']['content'].strip()
        self.animate_text_output(response)

# class running
class Prompt(ft.TextField):
    def __init__(self, chat: ft.ListView, user_output: UserOutput, gpt_output: GptOutput, **kwargs):
        super().__init__(**prompt_style(), on_submit=self.run_prompt, **kwargs)
        self.chat: ft.ListView = chat
        self.user_output: UserOutput = user_output  # Tambahkan parameter user_output
        self.gpt_output: GptOutput = gpt_output  # Tambahkan parameter gpt_output


    #method : runn all methods when started
    def run_prompt(self, event):
        # set the value of the user prompt
        text = event.control.value
        # disabling input field can also be added ...
        self.value = ""
        self.update()
        # first, we output the user prompt
        self.user_output.display_output(prompt=text)
         # second, we display GPT output
        self.gpt_output.display_output(prompt=text)

    
# Class definition for a custom sign-in button in the GUI.

class SignInButton(ft.UserControl):
    def __init__(self, btn_name): 
        self.btn_name = btn_name
        super().__init__()
  
    def build(self):
        return ft.Container(
            content=ft.ElevatedButton(
                content=ft.Text(
                    self.btn_name,
                    size=13,
                    weight='bold',
                ),
                style=ft.ButtonStyle(
                    shape={
                        "": ft.RoundedRectangleBorder(radius=8),
                    },
                    color={
                        "": "black",
                    },
                    bgcolor={
                        "": "#7df6dd",
                    }
                ),
                height=42,
                width=320,
            )
        )


#Class for the animation box
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

# Classes for user input
class UserInputField(ft.UserControl):
    def __init__(self, icon_name, text_hint, hide, function_emails: bool, function_check: bool):
        self.icon_name = icon_name
        self.text_hint = text_hint
        self.hide = hide
        self.function_emails = function_emails
        self.function_check = function_check
        super().__init__()
    
    # Function to add email prefix
    def return_email_prefix(self, e):
        email = self.controls[0].content.controls[1].value
        if e.control.data in email:
            pass
        else:
            self.controls[0].content.controls[1].value += e.control.data
            self.controls[0].content.controls[2].offset = ft.transform.Offset(0.5, 0)
            self.controls[0].content.controls[2].opacity = 0
            self.update()
    
    # Function for composing email prefix labels
    def prefix_email_containers(self):
        email_labels = ["@gmail.com", "@hotmail.com"]
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
                        weight="bold",
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
    
    # Function to display the off-focus checkbox
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
    
    # Function to get email prefix
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
        
    # Function to get a green check
    def get_green_check(self, e):
        if self.function_check:
            email = self.controls[0].content.controls[1].value
            password = self.controls[0].content.controls[1].password
            if (email):
                if "@gmail.com" in email or "@hotmail.com" in email or password:
                    time.sleep(0.5)
                    self.controls[0].content.controls[3].offset = ft.transform.Offset(-2, 0)
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

    def build(self):
        return ft.Container(
            width=320,
            height=40,
            border=ft.border.only(bottom=ft.border.BorderSide(0.5, "white54")),
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
        
# kelas barunya
# Kelas Ui adalah kelas turunan dari ft.Container yang digunakan untuk membuat wadah UI kustom. Tujuan kelas ini adalah membuat tampilan atau elemen UI yang khusus dengan properti tertentu, seperti judul (title) dan konten (content)
class Ui(ft.Container):
    def __init__(self, title: str, content: str):
        super().__init__(width=300, height=200, bgcolor="#ffffff", border_radius=10, padding=15)
        self.title = title
        self.content = content
        self.title_text = ft.Text(title, size=16, weight='bold', color='#333333')
        self.content_text = ft.Text(content, size=12, color='#666666')

        self.add_controls([
            self.title_text,
            self.content_text
        ])
        
# Function to display tab1 content
def tab1_content():
    return Card(
        elevation=15,
        content=ft.Container(
            width=300,  
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
                            Text("selamat ujian", size=22, weight='bold'),
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

# Function to display tab2 content
def tab2_content():
    main_area = MainContentArea()
    user_output = UserOutput(chat=main_area.chat)
    gpt_output = GptOutput(chat=main_area.chat)
    prompt = Prompt(chat=main_area.chat, user_output=user_output, gpt_output=gpt_output)
    
    # Instancekan objek kelas ui
    object1 = Ui(title="Object 1", content="This is the content of object 1")
    object2 = Ui(title="Object 2", content="This is the content of object 2")
    
    return ft.Column([
        main_area,
        ft.Divider(height=3, color="transparent"),
        prompt,
        object1, # ditambahkan
        object2
    ])

# Function to display tab3 content
def tab3_content():
    return ft.Text("This is Tab 3 Content", size=18, weight="w800")

# The main function to run the application
def main(page: ft.Page):
    page.horizontal_alignment="center"
    page.vertical_alignment="center"
    page.window_width = 420
    page.theme_mode = "light"

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Sign-In",
                icon=ft.icons.LOGIN,
                content=tab1_content(),
            ),
            ft.Tab(
                text="ChatBot",
                icon=ft.icons.CHAT,
                content=tab2_content(),
            ),
            ft.Tab(
                text="Settings",
                icon=ft.icons.SETTINGS,
                content=tab3_content(),
            ),
        ],
        expand=1,
    )

    navbar = ft.Container(
        **navbar_style(),
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon="menu", icon_size=25, icon_color="white"),
                ft.Text("Agora-AI", size=25, color="white", weight="bold"),
                ft.Row([
                    ft.IconButton(icon="notifications", icon_size=25, icon_color="white"),
                    ft.IconButton(icon="search", icon_size=25, icon_color="white"),
                ])
            ], alignment="spaceBetween"),
            t
        ])
    )

    page.add(navbar)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
