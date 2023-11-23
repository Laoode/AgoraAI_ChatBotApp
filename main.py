# # import the library
import flet as ft
import openai 


# start wayan 
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
# end wayan 

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