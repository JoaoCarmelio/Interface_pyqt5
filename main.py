import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget, QMessageBox, QTextEdit
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt


class InstagramApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyPerfil")
        self.setGeometry(100, 100, 360, 640)  # Tamanho ajustado para celular
        self.initUI()

    def initUI(self):
        # Criando o layout principal
        layout = QVBoxLayout()

        # Título no topo
        title_label = QLabel("PyPerfil", self)
        title_label.setFont(QFont("Arial", 20, QFont.Bold))
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        # Campo para exibir a imagem do Instagram
        logo = QLabel(self)
        pixmap = QPixmap("insta_logo.jpg")  # Coloque a imagem 'instagram_logo.png' na mesma pasta do script
        pixmap = pixmap.scaled(80, 80, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo.setPixmap(pixmap)
        logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(logo)

        # Texto "Qual a tag que deseja?"
        text_label = QLabel("DIGITE A TAG DESEJADA:", self)
        text_label.setFont(QFont("Arial", 12))
        text_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(text_label)

        # Campo de entrada de texto
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Digite a tag desejada aqui")
        self.input_field.setFont(QFont("Arial", 10))
        self.input_field.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.input_field)

        # Botão "OK"
        ok_button = QPushButton("OK", self)
        ok_button.setFont(QFont("Arial", 12))
        ok_button.clicked.connect(self.showTagInfo)
        layout.addWidget(ok_button)

        # Campo de resultados
        self.result_field = QTextEdit(self)
        self.result_field.setReadOnly(True)  # Campo de texto apenas para exibição
        self.result_field.setFont(QFont("Arial", 10))
        self.result_field.setPlaceholderText("O resultado será exibido aqui...")
        layout.addWidget(self.result_field)

        # Configurando o layout principal
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def showTagInfo(self):
        tag = self.input_field.text()
        if tag:
            # Exibindo o resultado no campo de texto
            self.result_field.setText(f"Você escolheu a tag: {tag}")
        else:
            QMessageBox.warning(self, "Erro", "Por favor, insira uma tag antes de continuar.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InstagramApp()
    window.show()
    sys.exit(app.exec_())
