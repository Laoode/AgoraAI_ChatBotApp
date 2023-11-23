# # import the library
import flet as ft

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
    


    # text control
    text= ft.Text(value='Testing Home', color="blue")
    page.controls.append(text)
    page.update()
# starting the app
ft.app(target=main, view = ft.WEB_BROWSER)