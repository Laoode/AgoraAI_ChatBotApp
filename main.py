# # import the library
import flet as ft


def prefix_email_containers(self):
    email_labels =["@gmail.com", "@hotmail.com"]
    label_title = ["GMAIL", "MAIL"]
    __ = ft.Row(spacing=1, alignment=ft.MainAxisAlignment.END)
    for index, label in enumerate(email_labels):
        __.controls.append(
            ft.Container(
            width=45,
            height=30,
            alignment=ft.alignment.center,
            data=label,
            on_click=lambda e: self.return_email_prefix(e),
            content=ft.Text(
                label_title[index],
                size=9,
                weight="bold"
                ),
            )
        )
    return ft.Row(
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        alignment=ft.MainAxisAlignment.END,
        spacing=2,
        opacity=0,
        animate_opacity=200,
        offset=ft.transform.Offset(0.35, 0),
        animate_offset=ft.animation.Animation(400, "decelerate"),
        controls=[__]
    )



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