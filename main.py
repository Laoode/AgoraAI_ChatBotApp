# # import the library
import flet as ft

#Rahmiii start
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
#Rahmi end

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