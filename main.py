import sys
import time

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QCheckBox,
    QVBoxLayout,
    QWidget,
    QGridLayout,
    QLabel,
    QGroupBox
)

row_headers = [
    "Takeoff",
    "Yours",
    "Autoreffen",
    "AutoComplete",
    "YellowMagic",
    "GraphityArt",
    "RConcept",
    "SprintRacing",
    "Presutige",
    "Athlete",
    "SS",
    "AutoBahn",
    "FrameMaster",
    "Yamamato",
    "KakinokiRacing",
    "OMR",
    "Briton",
    "Strada",
    "Hi-Fi",
    "Artt",
    "AkibaPrecision",
    "TargaTop",
    "SpeedLicense",
    "ProSprint",
    "GTYouth",
    "WatanabeAutomobiles",
    "Wellweiner",
    "HighPerformer",
    "Independent",
    "SpeedGear",
    "TerrorTune",
    "Oneoff",
    "S-Style",
    "MagnesioZero",
    "GambinoRacing",
    "OmegaLine",
    "TechnoSpeed",
    "SilverCreek",
    "Evergreen",
    "Steiner",
]

column_headers = [
    "Slot 1",
    "Slot 2",
    "Slot 3",
    "Slot 4",
    "Slot 5",
    "Slot 6",
    "Slot 7",
    "Slot 8",
    "Slot 9",
    "Slot 10",
    "Slot 11",
    "Slot 12",
    "Slot 13",
    "Slot 14",
    "Slot 15",
    "Slot 16",
]

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Init class member variables
        self.count = 0
        self.sponsor_flags = [0 for _ in range(40)]

        # Init window
        self.setWindowTitle("TXRD2 Sponsor Optimizer")
        self.setFixedSize(QSize(500, 500))

        # init checkboxes
        self.checkbox_grid = QGridLayout()
        for row in range(10):
            for col in range(4):
                checkbox = SponsorCheckBox(self, row_headers[col + row*4], col+row*4)
                checkbox.stateChanged.connect(lambda state=checkbox, id=(col+row*4): self.set_sponsor_flag(state, id))
                self.checkbox_grid.addWidget(checkbox, row, col)

        # init button
        self.button = QPushButton("Kowalski, Analysis!")
        self.button.clicked.connect(self.find_optimal)

        # init edit texts
        self.textbox_grid = QGridLayout()
        for row in range(4):
            for col in range(4):
                group_box = SlotGroupBox(column_headers[col + row*4], sponsor_name=row_headers[col + row*4])
                self.textbox_grid.addWidget(group_box, row, col)

        # init layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.checkbox_grid)
        main_layout.addWidget(self.button)
        main_layout.addLayout(self.textbox_grid)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_layout)
        self.setCentralWidget(self.main_widget)
    
    def find_optimal(self):
        self.set_loading_ui()
        # TODO: put analysis code here, time sleep placeholder
        time.sleep(1)

        self.set_ready_ui()
    
    def set_loading_ui(self):
        """
        Set UI into loading state
        """
        self.button.setDisabled(True)
        self.setWindowTitle("[LOADING...] TXRD2 Sponsor Optimizer")
    
    def set_ready_ui(self):
        """
        Returns UI back to ready to be interacted state
        """
        self.button.setDisabled(False)
        self.setWindowTitle("TXRD2 Sponsor Optimizer")
    
    def set_sponsor_flag(self, state, id):
        self.sponsor_flags[id] = 1 if state == Qt.Checked else 0

class SlotGroupBox(QGroupBox):
    def __init__(self, title, sponsor_name="") -> None:
        super().__init__(title)
        self.sponsor_name = sponsor_name
        self.title = title
        self.layout = QVBoxLayout()
        self.text = QLabel(self.sponsor_name)
        self.text.setStyleSheet("font-weight: bold")
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)

class SponsorCheckBox(QCheckBox):
    def __init__(self, parent, name, id) -> None:
        super().__init__(parent)
        self.setText(name)
        self.name = name
        self.id = id
    
    def get_id(self):
        return self.id

# inits the UI
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()