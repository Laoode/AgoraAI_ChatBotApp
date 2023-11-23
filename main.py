# # import the library
import flet as ft

class userInputField(ft.UserControl):
    def__init__(self,icon_name,text_hint,hide,function,emails:bool, function_check:bool):
        self.icon_name = icon_name
        self.text_hint = text_hint
        self.hide = hide
        self.function_emails = function_emails
        seld.function_check = function_check
        super().__init()
    
    def return_email_prefix(self, e):
        email = self.controls[0].content.controls[1].value
        if e.control.data in email:
            pass
        else:
            self.controls[0].content.controls[1].value+= e.control.data
            self.controls[0].content.controls[2].offset = ft.transform.Offset(0.5, 0)
            self.controls[0].content.controls[2].opacity = 0
            self.update()
                    







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