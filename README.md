# DZ-K-LK4-1710-Kivy
<img width="1197" height="858" alt="image" src="https://github.com/user-attachments/assets/4ae09b56-acf9-4e68-a2bc-249d08507c2e" />
<img width="1200" height="862" alt="image" src="https://github.com/user-attachments/assets/df27e0e8-ddbf-4bc4-94ff-efac8383b39c" />

```markdown
## Cross-Platform Application - Kivy

## Описание проекта
Кроссплатформенное приложение с современным интерфейсом, включающее главный экран и экран профиля с анимацией и красивым дизайном.

## Стек технологий
- **Язык программирования**: Python 3.10+
- **GUI фреймворк**: Kivy 2.3.0+
- **Архитектура**: ScreenManager для навигации
- **Дополнительные модули**:
  - kivy.clock - для анимации и таймеров
  - kivy.graphics - для кастомной графики
  - kivy.core.window - для управления окном

## Особенности реализации
- Кроссплатформенность (Windows, Mac, Linux, Android, iOS)
- Анимация из последовательности изображений (имитация GIF)
- ScreenManager для переключения между экранами
- Адаптивная верстка с size_hint и pos_hint
- Кастомные цвета и графика через Canvas
- Закругленные углы элементов (RoundedRectangle)
- Полупрозрачные overlay для улучшения читаемости

## Структура проекта
project/
├── main.py # Главный файл приложения
├── images/ # Папка с ресурсами
│ ├── Hello.jpg # Фон главного экрана
│ ├── Scenary.jpg # Фон профиля
│ ├── Cat.jpg # Аватар пользователя
│ ├── PC1-5.jpg # Кадры для анимации
│ └── pc.gif # Исходная анимация
└── README.md # Документация

## Запуск приложения
```bash
python main.py

## Установка библиотек
pip install kivy[base] pillow

## Особенности Kivy:
-Единый код для всех платформ;
-Сенсорный интерфейс;
-Современный Material-дизайн;
-Высокая производительность.
