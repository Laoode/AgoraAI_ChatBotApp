# # import the library
import flet as ft

#widya start
def main(page:ft.page):
    page.window_width = 420
    page.theme_mode = "light"

    t = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(
                text="Sign-In",
                icon=ft.icon.LOGIN,
                content=tab1_content(),
            ),
            ft.Tab(
                text="ChatBot",
                icon=ft.icon.CHAT,
                content=tab2_content(),
            ),
            ft.Tab(
                text="Settings",
                icon=ft.icon.SETTINGS,
                content=tab3_content(),
            ),
        ]
        expand=1,
    )
#widya end