import sys
import random
import os

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (QApplication, QMainWindow,
                           QPushButton, QLabel, QMessageBox)
from PyQt6.QtGui import QPixmap, QEnterEvent


class MainWindow(QMainWindow):
    """Главное окно приложения с убегающей кнопкой"""
    
    # Константы интерфейса
    WINDOW_SIZE = QSize(780, 450)
    BUTTON_SIZE = QSize(100, 30)
    IMAGE_FILE = "monkey780x450.jpg"
    
    def __init__(self):
        """Инициализация UI компонентов и обработчиков событий"""
        super().__init__()
        self._init_ui()
        self._setup_event_handlers()
        
    def _init_ui(self):
        """Настройка пользовательского интерфейса"""
        self.setWindowTitle("Убегающая кнопка")
        self.setFixedSize(self.WINDOW_SIZE)
        
        # Настройка фонового изображения
        self._setup_background()
        
        # Создание и позиционирование кнопки
        self.button = self._create_button()
        self._center_button()
        
        self.setCentralWidget(self.image)
    
    def _setup_background(self):
        """Загрузка и настройка фонового изображения"""
        if getattr(sys, 'frozen', False):
            # Режим упакованного EXE
            base_path = sys._MEIPASS
        else:
            # Режим разработки
            base_path = os.path.dirname(os.path.abspath(__file__))
            
        image_path = os.path.join(base_path, self.IMAGE_FILE)
        self.pixmap = QPixmap(image_path).scaled(
            self.WINDOW_SIZE.width(),
            self.WINDOW_SIZE.height()
        )
        self.image = QLabel(self)
        self.image.setPixmap(self.pixmap)
        self.image.resize(self.WINDOW_SIZE)
    
    def _create_button(self):
        """Создание кнопки с базовыми настройками"""
        button = QPushButton("Нажми меня!", self)
        button.setFixedSize(self.BUTTON_SIZE)
        return button
        
    def _center_button(self):
        """Позиционирование кнопки по центру окна"""
        x = (self.WINDOW_SIZE.width() - self.BUTTON_SIZE.width()) // 2
        y = (self.WINDOW_SIZE.height() - self.BUTTON_SIZE.height()) // 2
        self.button.move(x, y)
    
    def _setup_event_handlers(self):
        """Настройка обработчиков событий"""
        self.button.setMouseTracking(True)
        self.button.installEventFilter(self)
        self.button.clicked.connect(self._on_button_click)
    
    def _on_button_click(self):
        """Обработчик клика по кнопке"""
        msg = QMessageBox(self)
        msg.setWindowTitle("Победа!")
        msg.setText("Вы победили!")
        
        close_btn = msg.addButton("Закрыть", QMessageBox.ButtonRole.AcceptRole)
        msg.exec()
        
        if msg.clickedButton() == close_btn:
            self.close()
    
    def eventFilter(self, obj, event):
        """Обработчик события наведения на кнопку"""
        if obj == self.button and isinstance(event, QEnterEvent):
            self._move_button_randomly()
            return True
        return super().eventFilter(obj, event)
    
    def _move_button_randomly(self):
        """Перемещение кнопки в случайную позицию"""
        max_x = self.WINDOW_SIZE.width() - self.BUTTON_SIZE.width()
        max_y = self.WINDOW_SIZE.height() - self.BUTTON_SIZE.height()
        self.button.move(
            random.randint(0, max_x),
            random.randint(0, max_y)
        )


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()