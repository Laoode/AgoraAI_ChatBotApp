# # import the library
import flet as ft

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
    


    # text control
    text= ft.Text(value='Testing Home', color="blue")
    page.controls.append(text)
    page.update()
# starting the app
ft.app(target=main, view = ft.WEB_BROWSER)