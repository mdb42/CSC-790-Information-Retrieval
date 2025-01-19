from PyQt6.QtWidgets import QMainWindow
from app.gui.ui_mainwindow import Ui_MainWindow
from app.core.constants import ACTIONS, STATES
import qtawesome as qta

class InfoQuest(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()
        self.current_state_index = 0
        
    def init_ui(self):
        self.setWindowTitle("InfoQuest Data Studio")
        self.setWindowIcon(qta.icon("mdi.database"))
        self.connect_splash_buttons()
        self.connect_project_creation_buttons()
        self.splash_screen()


    def splash_screen(self):
        self.set_current_state(STATES["Splash"])
        self.crawler_widget.setEnabled(False)
        self.indexer_widget.setEnabled(False)
        pass

    def home_screen(self):
        self.set_current_state(STATES["Home"])
        self.crawler_widget.setEnabled(True)
        self.indexer_widget.setEnabled(True)
    
    def create_project(self):
        self.set_current_state(STATES["Create Project"])
        self.crawler_widget.setEnabled(False)
        self.indexer_widget.setEnabled(False)

    def set_current_state(self, state_index):
        self.current_state_index = state_index
        self.stacked_widget.setCurrentIndex(state_index)

    def connect_splash_buttons(self):
        self.create_project_button.clicked.connect(self.create_project)
        self.open_project_button.clicked.connect(self.home_screen)

    def connect_project_creation_buttons(self):
        self.cancel_project_creation_button.clicked.connect(self.splash_screen)
        self.begin_project_button.clicked.connect(self.home_screen)
