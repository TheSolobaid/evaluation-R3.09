import sys
from PyQt6.QtWidgets import *
import threading

stop_chrono = False



class FirstWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chronomètre")
        self.setGeometry(200, 100, 240, 100)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.layout = QGridLayout(central_widget)

        self.text_compteur = QLabel("Compteur :", self)
        self.chiffre_input = QLineEdit(self)
        self.chiffre_input.setPlaceholderText("0")
        self.chiffre_input.textChanged.connect(self.correction)
        self.error_message = QLabel("", self)
        self.error_message.setStyleSheet("color: red;")

        start_button = QPushButton("Start", self)
        start_button.clicked.connect(self.start)
        reset_button = QPushButton("Reset", self)
        reset_button.clicked.connect(self.reset)
        stop_button = QPushButton("Stop", self)
        connect_button = QPushButton("Connect", self)
        quit_button = QPushButton("Quitter", self)
        quit_button.clicked.connect(self.quitter)

        self.layout.addWidget(self.text_compteur,0,0)
        self.layout.addWidget(self.chiffre_input,1,0,1,2)
        self.layout.addWidget(start_button,2,0,1,2)
        self.layout.addWidget(reset_button,3,0)
        self.layout.addWidget(stop_button, 3,1)
        self.layout.addWidget(connect_button,4,0)
        self.layout.addWidget(quit_button,4,1)
        


    def start(self):
        try :
            tmp = self.chiffre_input.text()
            if not tmp:
                val = 0
            else:
                val= int(self.chiffre_input.text())
        except:
            self.show_error_message(message="Un nombre entier est attendu")
        else:
            
            val = str(val+1)
            self.chiffre_input.setText(val)

    def reset(self):
        self.chiffre_input.setText("0")

    def quitter(self):
        self.close()
    
    def show_error_message(self, message):
        self.error_message = QLabel(message, self)
        self.error_message.setStyleSheet("color: red;")
        self.layout.addWidget(self.error_message, 0,1)

        self.error_message.show()

    def correction(self):
        self.error_message.clear()
def main():
    app = QApplication(sys.argv)
    fenetre = FirstWindow()
    fenetre.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
