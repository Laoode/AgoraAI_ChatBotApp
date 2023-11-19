# # import the library
import flet as ft

# defining the main function
def main(page:ft.Page):
    # setting the page title
    page.title = "Kelompok1.chatbot.ai"
    
    print("Halo Dunia")

    # text control
    text= ft.Text(value='Testing Home', color="blue")
    page.controls.append(text)
    page.update()
# starting the app
ft.app(target=main, view = ft.WEB_BROWSER)