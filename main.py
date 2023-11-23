# # import the library
import flet as ft


    navbar = ft.Container(
        **navbar_style(),
        content=ft.Column([
            ft.Row([
                ft.IconButton(icon="menu", icon_size=25, icon_color="white"),
                ft.Text("Agora-AI", size=25, color="white", weight="bold"),
                ft.Row([
                    ft.IconButton(icon="notifications", icon_size=25, icon_color="white"),
                    ft.IconButton(icon="search", icon_size=25, icon_color="white"),
                ])
            ], alignment="spaceBetween"),
            t
        ])
    )

    page.add(navbar)
    page.update()

if __name__ == "__main__":
    ft.app(target=main)
    
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