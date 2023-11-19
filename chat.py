# # import the library
import flet as ft

# defining the main function
def main(page:ft.Page):
    # setting the page title
    page.title = "Hello World!"

    print("ini revan tes")
    
    # text control
    text= ft.Text(value='My first app with flutter', color="blue")
    page.controls.append(text)
    page.update()
# starting the app
ft.app(target=main, view = ft.WEB_BROWSER)