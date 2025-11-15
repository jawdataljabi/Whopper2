from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QComboBox, QSpacerItem, QSizePolicy
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import Qt
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Sign Sync")
        self.setMinimumWidth(350)
        self.setWindowIcon(QIcon("Logo.png"))

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(20)

        layout.addLayout(self.create_dropdown("Voice:", ["Voice 1", "Voice 2", "Voice 3"], self.on_voice_changed))
        layout.addLayout(self.create_dropdown("Speed:", ["0.5x", "1x", "1.5x", "2x"], self.on_speed_changed))
                
       # Hear Voice Sample Button
        self.voice_sample_button = QPushButton("Hear Voice Sample")
        self.voice_sample_button.setFixedHeight(30)
        self.voice_sample_button.setFixedWidth(150)
        self.voice_sample_button.setObjectName("voice_sample_button")
        self.voice_sample_button.clicked.connect(self.play_voice_sample)
        self.voice_sample_button.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)


        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(self.voice_sample_button)

        layout.addLayout(button_layout)



        layout.addLayout(self.create_dropdown("NLP interpreter", ["None", "GPT-5"], self.on_nlp_changed))

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.start_button = QPushButton("START")
        self.start_button.setFixedHeight(50)
        self.start_button.setObjectName("start_button")
        self.start_button.isStart = True
        self.start_button.clicked.connect(self.toggle_start_button)

        layout.addWidget(self.start_button)

        self.setLayout(layout)

    def create_dropdown(self, label_text, items, callback):
        layout = QHBoxLayout()

        label = QLabel(label_text)
        dropdown = QComboBox()
        dropdown.addItems(items)
        dropdown.currentTextChanged.connect(callback)

        layout.addWidget(label)
        layout.addWidget(dropdown)

        return layout

    def on_voice_changed(self, value):
        print("Selected voice:", value)

    def on_speed_changed(self, value):
        print("Selected speed:", value)

    def on_nlp_changed(self, value):
        print("Selected NLP model:", value)

    def play_voice_sample(self):
        print("Playing voice sample...")


    def toggle_start_button(self):
        print("toggling start button")
        if self.start_button.isStart:
            self.start_button.setObjectName("start_button_live")
            self.start_button.setText("LIVE")
        else:
            self.start_button.setObjectName("start_button")
            self.start_button.setText("START")

        self.start_button.isStart = not self.start_button.isStart

        self.start_button.style().unpolish(self.start_button)
        self.start_button.style().polish(self.start_button)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
