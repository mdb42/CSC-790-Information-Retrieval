import sys
from PyQt6.QtWidgets import QApplication
from app.gui.info_quest import InfoQuest

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InfoQuest()
    window.show()
    sys.exit(app.exec())
