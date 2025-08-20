#pyQt5 introduction

import sys
from PyQt5.QtWidgets import QApplication , QMainWindow ,QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello There !!")
        self.setGeometry(700,300,500,500)
        self.setWindowIcon(QIcon("img.jpeg"))

        lable = QLabel("Hello There !!",self)
        lable.setFont(QFont("Arial",20))
        lable.setGeometry(0,0, 500,100)
        lable.setStyleSheet("color:Blue"
                           "background-color:red"
                            "font_weight:bold"
                            "font_style:italic"
                            )
        #lable.setAlignment(Qt.AlignTop)
        #lable.setAlignment(Qt.AlignBottom)
        #lable.setAlignment(Qt.AlignRight)
        lable.setAlignment(Qt.AlignHCenter)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
      main()


