from kivy.uix.screenmanager import Screen
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.graphics import Color, Rectangle


class PauseMenu(Popup):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "Paused"
        self.size_hint = (0.5, 0.6)
        self.auto_dismiss = False

    def build_widget(self):
        self.container: BoxLayout = BoxLayout(
            orientation="vertical",
            padding=(10, 10),
            spacing=10,
        )

        self.container.canvas.before.add(Color(0, 0, 0, 0.7))
        self.rect = Rectangle(size=self.container.size, pos=self.container.pos)
        self.container.canvas.before.add(self.rect)

        def update_rect(instance, value):
            self.rect.size = instance.size
            self.rect.pos = instance.pos

        self.container.bind(size=update_rect, pos=update_rect)

        self.title_label = Label(
            text="Paused",
            font_size=40,
            size_hint=(1, None),
            height=40,
        )
        self.container.add_widget(self.title_label)

        self.resume_btn = Button(text="Resume", size_hint=(1, None), height=50)
        self.resume_btn.bind(on_release=self.dismiss)
        self.container.add_widget(self.resume_btn)

        self.save_btn = Button(text="Save", size_hint=(1, None), height=50)
        self.save_btn.bind(on_release=self.save_game)
        self.container.add_widget(self.save_btn)

        self.load_btn = Button(text="Load", size_hint=(1, None), height=50)
        self.load_btn.bind(on_release=self.load_game)
        self.container.add_widget(self.load_btn)

        self.options_btn = Button(text="Options", size_hint=(1, None), height=50)
        self.options_btn.bind(on_release=self.open_options)
        self.container.add_widget(self.options_btn)

        self.main_menu_btn = Button(text="Main Menu", size_hint=(1, None), height=50)
        self.main_menu_btn.bind(on_release=self.return_to_main_menu)
        self.container.add_widget(self.main_menu_btn)

        self.quit_btn = Button(text="Quit", size_hint=(1, None), height=50)
        self.quit_btn.bind(on_release=self.quit_game)
        self.container.add_widget(self.quit_btn)

        self.add_widget(self.container)

    def save_game(self, instance):
        print("Saving game...")

    def load_game(self, instance):
        print("Loading game...")

    def open_options(self, instance):
        print("Opening options...")

    def return_to_main_menu(self, instance):
        print("Returning to main menu")
        self.dismiss()

    def quit_game(self, instance):
        from direct.showbase.MessengerGlobal import messenger

        messenger.send("game.input.user.quit_game")


class PauseScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pause_menu = PauseMenu()
        self.build: bool = False
        self.build_screen()

    def build_screen(self):
        if self.build is True:
            return
        self.build = True
        return self.pause_menu.build_widget()

    def on_enter(self, *args):
        self.pause_menu.open()

    def on_leave(self, *args):
        self.pause_menu.dismiss()
