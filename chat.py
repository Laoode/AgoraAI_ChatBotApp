# # import the library
import flet as ft

# defining the main function
def main(page:ft.Page):
    # setting the page title
    page.title = "Project Chat Bot"
    
    # text control
    text= ft.Text(value='Ade', color="white")
    page.controls.append(text)
    page.update()
# starting the app
ft.app(target=main, view = ft.WEB_BROWSER)