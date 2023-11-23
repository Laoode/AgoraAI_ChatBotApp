# # import the library
import flet as ft

# IRFAN START
def get_green_check(self,e):
    if self.function_check:
        email = self.controls[0].content.controls[3].value
        password = self.controls[0].content.controls[3].password
        if (email):
            if "@gmail.com" in email or "@hotmail.com" in email or password:
                time.sleep(0.5)
                self.controls[0].content.controls[3].offset = ft.transform.Offset(-2,0)
                self.controls[0].content.controls[3].opacity = 1
                self.update()
                time.sleep(0.2)
                self.controls[0].content.controls[3].content.value = True
                time.sleep(0.1)
                self.update()
            else:
                self.controls[0].content.controls[3].offset = ft.transform.Offset(0, 0)
                self.controls[0].content.controls[3].opacity = 0
                self.update()
            
        else:
            pass
# IRFAN END

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