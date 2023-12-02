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
        layout = QGridLayout(central_widget)

        self.text_compteur = QLabel("Compteur :", self)
        self.chiffre_input = QLineEdit(self)
        self.chiffre_input.setPlaceholderText("0")

        start_button = QPushButton("Start", self)
        reset_button = QPushButton("Reset", self)
        stop_button = QPushButton("Stop", self)
        connect_button = QPushButton("Connect", self)
        quit_button = QPushButton("Quitter", self)
        quit_button.clicked.connect(self.close)

        layout.addWidget(self.text_compteur,0,0,1,2)
        layout.addWidget(self.chiffre_input,1,0,1,2)

        layout.addWidget(start_button,2,0,1,2)
        layout.addWidget(reset_button,3,0)
        layout.addWidget(stop_button, 3,1)
        layout.addWidget(connect_button,4,0)
        layout.addWidget(quit_button,4,1)
        
 


        
def main():
    app = QApplication(sys.argv)
    fenetre = FirstWindow()
    fenetre.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
