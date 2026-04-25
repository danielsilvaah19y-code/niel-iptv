from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.videoplayer import VideoPlayer

class MenuPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Título Centralizado
        layout.add_widget(Label(
            text="NIEL IPTV PREMIUM", 
            font_size='26sp', 
            size_hint_y=None,
            height=100,
            bold=True, 
            color=(0, 1, 0.5, 1)
        ))
        
        scroll = ScrollView()
        # Grade com espaçamento maior para não embolar
        grid = GridLayout(cols=2, spacing=20, size_hint_y=None, padding=10)
        grid.bind(minimum_height=grid.setter('height'))
        
        # Canais com Cores Fortes (RGB)
        canais = [
            ("TV GLOBO", "https://akamaized.net", (0.1, 0.4, 0.8, 1)), # Azul
            ("SBT", "https://jmvstream.com", (0.5, 0.1, 0.5, 1)), # Roxo
            ("RECORD", "https://akamaized.net", (0.7, 0.1, 0.1, 1)), # Vermelho
            ("BAND", "https://akamaized.net", (0.1, 0.5, 0.1, 1)), # Verde
            ("FILMES", "http://pluto.tv", (0.8, 0.5, 0, 1)), # Laranja
            ("SÉRIES", "http://pluto.tv", (0.2, 0.2, 0.2, 1)) # Grafite
        ]
        
        for nome, link_video, cor in canais:
            # Botão com texto centralizado e fonte grande
            btn = Button(
                text=nome,
                font_size='18sp',
                bold=True,
                size_hint_y=None,
                height=180,
                background_normal='',
                background_color=cor,
                halign='center',
                valign='middle'
            )
            # Isso garante que o texto fique no meio do botão
            btn.bind(size=btn.setter('text_size'))
            
            btn.bind(on_release=lambda x, l=link_video: self.play_video(l))
            grid.add_widget(btn)
            
        scroll.add_widget(grid)
        layout.add_widget(scroll)
        self.add_widget(layout)

    def play_video(self, link):
        app = App.get_running_app()
        app.root.get_screen('player').video_link = link
        app.root.current = 'player'

class PlayerScreen(Screen):
    def on_enter(self):
        Window.rotation = 90 
        layout = BoxLayout(orientation='vertical')
        self.player = VideoPlayer(source=self.video_link, state='play', options={'allow_stretch': True})
        btn_voltar = Button(text="VOLTAR", size_hint=(1, 0.15), background_color=(0.8, 0, 0, 1), bold=True)
        btn_voltar.bind(on_release=self.voltar)
        layout.add_widget(self.player)
        layout.add_widget(btn_voltar)
        self.add_widget(layout)

    def voltar(self, instance):
        self.player.state = 'stop'
        Window.rotation = 0 
        self.clear_widgets()
        self.manager.current = 'menu'

class NielIPTV(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MenuPrincipal(name='menu'))
        sm.add_widget(PlayerScreen(name='player'))
        return sm

if __name__ == "__main__":
    NielIPTV().run()
