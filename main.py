# # import the library
import flet as ft

def tab2_content():
    main_area = MainContentArea()
    prompt = Prompt(chat=main_area.chat)
    return ft.Column([
        main_area,
        ft.Divider(height=3, color="transparent"),
        prompt,
    ])
def tab3_content():
    return ft.Text("This is Tab 3 Content", size=18, weight="w800")

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