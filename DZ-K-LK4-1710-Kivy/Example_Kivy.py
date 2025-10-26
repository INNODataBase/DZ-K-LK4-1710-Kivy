from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle
import os

class GifAnimation(Image):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frames = []
        self.current_frame = 0
        self.load_gif_frames()
        if self.frames:
            self.source = self.frames[0]
            Clock.schedule_interval(self.update, 0.2)
    
    def load_gif_frames(self):
        gif_frames = [
            "images/PC1.jpg",
            "images/PC2.jpg", 
            "images/PC3.jpg",
            "images/PC4.jpg",
            "images/PC5.jpg"
        ]
        
        for frame_path in gif_frames:
            if os.path.exists(frame_path):
                self.frames.append(frame_path)
        
        if not self.frames:
            fallback_frames = ["images/Cat.jpg", "images/Scenary.jpg"]
            for frame_path in fallback_frames:
                if os.path.exists(frame_path):
                    self.frames.append(frame_path)
    
    def update(self, dt):
        if len(self.frames) > 1:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.source = self.frames[self.current_frame]

class ProfileScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
    
    def setup_ui(self):
        Window.size = (800, 600)
        
        # Фоновое изображение Scenary.jpg
        if os.path.exists("images/Scenary.jpg"):
            bg_image = Image(
                source="images/Scenary.jpg",
                size_hint=(1, 1),
                pos=(0, 0),
                allow_stretch=True,
                keep_ratio=False
            )
            self.add_widget(bg_image)
        else:
            with self.canvas.before:
                Color(0.1, 0.2, 0.4, 1)
                Rectangle(pos=self.pos, size=Window.size)
        
        # Cat.jpg побольше
        if os.path.exists("images/Cat.jpg"):
            cat_image = Image(
                source="images/Cat.jpg",
                size_hint=(None, None),
                size=(200, 200),
                pos=(300, 350),
                allow_stretch=True,
                keep_ratio=True
            )
            self.add_widget(cat_image)
        
        # Имя пользователя
        user_label = Label(
            text="Ковалев Егор",
            size_hint=(None, None),
            size=(400, 40),
            pos=(200, 300),
            font_size='24sp',
            color=(1, 1, 0, 1)  # Ярко-жёлтый цвет
        )
        self.add_widget(user_label)
        
        # Биография
        bio_label = Label(
            text="Биография",
            size_hint=(None, None),
            size=(400, 30),
            pos=(50, 250),
            font_size='18sp',
            color=(1, 1, 0, 1)  # Ярко-жёлтый цвет
        )
        self.add_widget(bio_label)
        
        about_label = Label(
            text="Я - начинающий инженер инноватик",
            size_hint=(None, None),
            size=(400, 40),
            pos=(50, 220),
            text_size=(400, None),
            color=(1, 1, 0, 1)  # Ярко-жёлтый цвет
        )
        self.add_widget(about_label)
        
        # Умения
        skills_label = Label(
            text="Умения",
            size_hint=(None, None),
            size=(400, 30),
            pos=(50, 180),
            font_size='18sp',
            color=(1, 1, 0, 1)  # Ярко-жёлтый цвет
        )
        self.add_widget(skills_label)
        
        languages_label = Label(
            text="Математика, музыка, искусство\nи программирование",
            size_hint=(None, None),
            size=(400, 50),
            pos=(50, 140),
            text_size=(400, None),
            color=(1, 1, 0, 1)  # Ярко-жёлтый цвет
        )
        self.add_widget(languages_label)
        
        # Опыт
        experience_label = Label(
            text="Опыт",
            size_hint=(None, None),
            size=(400, 30),
            pos=(50, 100),
            font_size='18sp',
            color=(1, 1, 0, 1)  # Ярко-жёлтый цвет
        )
        self.add_widget(experience_label)
        
        developer_label = Label(
            text="Python, 11 классов,\nмузыкальная школа",
            size_hint=(None, None),
            size=(400, 40),
            pos=(50, 60),
            text_size=(400, None),
            color=(1, 1, 0, 1)  # Ярко-жёлтый цвет
        )
        self.add_widget(developer_label)
        
        driver_dates_label = Label(
            text="oct 25 2025 - oct 26 2025",
            size_hint=(None, None),
            size=(400, 20),
            pos=(50, 30),
            font_size='12sp',
            color=(1, 1, 0, 1)  # Ярко-жёлтый цвет
        )
        self.add_widget(driver_dates_label)
        
        # Кнопка для возврата
        from kivy.uix.button import Button
        back_btn = Button(
            text="Назад",
            size_hint=(None, None),
            size=(100, 40),
            pos=(20, 20),
            background_color=(0.3, 0.5, 0.8, 1),
            color=(1, 1, 1, 1)
        )
        back_btn.bind(on_press=self.go_back)
        self.add_widget(back_btn)
    
    def go_back(self, instance):
        Window.size = (960, 660)
        self.manager.current = 'welcome'

class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.setup_ui()
    
    def setup_ui(self):
        # Текст приветствия
        hello_label = Label(
            text="Добро пожаловать в тестовое окно!",
            size_hint=(None, None),
            size=(400, 30),
            pos=(280, 630),
            color=(0, 0, 0, 1)
        )
        self.add_widget(hello_label)
        
        # Фоновое изображение
        image_path = "images/Hello.jpg"
        if os.path.exists(image_path):
            bg_image = Image(
                source=image_path,
                size_hint=(1, 1),
                pos=(0, 0)
            )
            self.add_widget(bg_image)
        else:
            with self.canvas.before:
                Color(0.8, 0.8, 1, 1)
                Rectangle(pos=self.pos, size=(960, 660))
        
        # Анимированное GIF изображение
        gif_image = GifAnimation(
            size_hint=(None, None),
            size=(100, 100),
            pos=(0, 570)
        )
        self.add_widget(gif_image)
        
        # Кнопка для перехода к профилю
        from kivy.uix.button import Button
        profile_btn = Button(
            text="Посмотреть профиль",
            size_hint=(None, None),
            size=(180, 50),
            pos=(390, 50),
            background_color=(0.2, 0.6, 1, 1),
            color=(1, 1, 1, 1),
            font_size='16sp'
        )
        profile_btn.bind(on_press=self.go_to_profile)
        self.add_widget(profile_btn)
    
    def go_to_profile(self, instance):
        self.manager.current = 'profile'

class MultiWindowApp(App):
    def build(self):
        sm = ScreenManager()
        welcome_screen = WelcomeScreen(name='welcome')
        profile_screen = ProfileScreen(name='profile')
        sm.add_widget(welcome_screen)
        sm.add_widget(profile_screen)
        sm.current = 'welcome'
        Window.size = (960, 660)
        return sm

if __name__ == '__main__':
    MultiWindowApp().run()