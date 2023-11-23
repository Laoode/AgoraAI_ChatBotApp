# # import the library
import flet as ft




    def gpt_output(self, prompt):
        response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user","content": prompt }]
        )
        response = response['choice'][0]['message']['content'].strip()
        self.animate_text_output(name="Agora",prompt=response)

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