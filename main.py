import sys

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
    QGroupBox,
    QLineEdit
)
import numpy as np
from scipy.optimize import linear_sum_assignment

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

matrix = [
[1000,1000,10000,3000,3000,2000,2000,2000,1000,1000,7000,3000,3000,2000,2000,2000],
[1000,1000,9000,2000,2000,2000,2000,2000,1000,1000,11000,2000,2000,2000,2000,2000],
[1000,1000,30000,2000,2000,10000,10000,10000,2000,2000,10000,2000,2000,10000,10000,10000],
[2000,2000,50000,5000,5000,10000,10000,10000,2000,2000,30000,5000,5000,10000,10000,10000],
[1000,1000,30000,4000,4000,10000,10000,10000,1000,1000,9000,4000,4000,10000,10000,10000],
[1000,1000,50000,7000,7000,15000,15000,15000,2000,2000,25000,7000,7000,15000,15000,15000],
[2000,2000,70000,3000,3000,50000,50000,50000,1000,1000,37000,3000,3000,50000,50000,50000],
[3000,3000,65000,4000,4000,45000,45000,45000,2000,2000,40000,4000,4000,45000,45000,45000],
[5000,5000,188000,50000,50000,80000,80000,80000,5000,5000,75000,50000,50000,80000,80000,80000],
[3000,3000,140000,70000,70000,110000,110000,110000,3000,3000,75000,70000,70000,110000,110000,110000],
[4000,4000,70000,5000,5000,45000,45000,45000,4000,4000,45000,5000,5000,45000,45000,45000],
[3000,3000,150000,90000,90000,45000,45000,45000,2000,2000,110000,90000,90000,45000,45000,45000],
[3000,3000,138000,80000,80000,85000,85000,85000,3000,3000,85000,80000,80000,85000,85000,85000],
[3000,3000,60000,4000,4000,50000,50000,50000,3000,3000,50000,4000,4000,50000,50000,50000],
[5000,5000,155000,85000,85000,120000,120000,120000,5000,5000,100000,85000,85000,120000,120000,120000],
[5000,5000,150000,90000,90000,100000,100000,100000,4000,4000,75000,90000,90000,100000,100000,100000],
[5000,5000,100000,6000,6000,75000,75000,75000,5000,5000,80000,6000,6000,75000,75000,75000],
[7000,7000,250000,110000,110000,125000,125000,125000,5000,5000,200000,110000,110000,125000,125000,125000],
[3000,3000,100000,65000,65000,70000,70000,70000,3000,3000,90000,65000,65000,70000,70000,70000],
[7000,7000,200000,125000,125000,140000,140000,140000,7000,7000,190000,125000,125000,140000,140000,140000],
[2000,2000,30000,3000,3000,6000,6000,6000,2000,2000,8000,3000,3000,6000,6000,6000],
[1000,1000,25000,3000,3000,7000,7000,7000,1000,1000,8000,3000,3000,7000,7000,7000],
[1000,1000,80000,8000,8000,10000,10000,10000,2000,2000,15000,8000,8000,10000,10000,10000],
[3000,3000,100000,10000,10000,15000,15000,15000,3000,3000,25000,10000,10000,15000,15000,15000],
[1000,1000,50000,9000,9000,18000,18000,18000,1000,1000,30000,9000,9000,18000,18000,18000],
[9000,9000,190000,80000,80000,100000,100000,100000,7000,7000,110000,80000,80000,100000,100000,100000],
[10000,10000,200000,90000,90000,100000,100000,100000,10000,10000,125000,90000,90000,100000,100000,100000],
[8000,8000,180000,70000,70000,90000,90000,90000,8000,8000,100000,70000,70000,90000,90000,90000],
[5000,5000,280000,5000,5000,100000,100000,100000,5000,5000,188000,50000,50000,100000,100000,100000],
[8000,8000,300000,70000,70000,130000,130000,130000,7000,7000,150000,70000,70000,130000,130000,130000],
[35000,35000,350000,100000,100000,180000,180000,180000,35000,35000,200000,100000,100000,180000,180000,180000],
[5000,5000,14000,50000,50000,65000,65000,65000,5000,5000,75000,50000,50000,65000,65000,65000],
[6000,6000,98000,45000,45000,50000,50000,50000,5000,5000,75000,45000,45000,50000,50000,50000],
[6000,6000,100000,50000,50000,70000,70000,70000,6000,6000,75000,50000,50000,70000,70000,70000],
[7000,7000,165000,65000,65000,80000,80000,80000,7000,7000,80000,65000,65000,80000,80000,80000],
[9000,9000,100000,70000,70000,75000,75000,75000,8000,8000,90000,70000,70000,75000,75000,75000],
[10000,10000,330000,72000,72000,165000,165000,165000,10000,10000,180000,72000,72000,165000,165000,165000],
[20000,20000,500000,98000,98000,135000,135000,135000,20000,20000,250000,98000,98000,135000,135000,135000],
[50000,50000,620000,100000,100000,150000,150000,150000,30000,30000,350000,100000,100000,150000,150000,150000],
[100000,100000,700000,220000,220000,250000,250000,250000,100000,100000,500000,220000,220000,250000,250000,250000],
]

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        # Init class member variables
        self.count = 0
        self.sponsor_flags = [0 for _ in range(40)]
        self.sponsor_slots: list[SlotGroupBox] = []

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
                group_box = SlotGroupBox(self, column_headers[col + row*4])
                self.textbox_grid.addWidget(group_box, row, col)
                self.sponsor_slots.append(group_box)
        
        # init area showing total
        self.valueText = QLineEdit()
        self.valueText.setReadOnly(True)

        # init layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(self.checkbox_grid)
        main_layout.addWidget(self.button)
        main_layout.addLayout(self.textbox_grid)
        main_layout.addWidget(self.valueText)

        self.main_widget = QWidget()
        self.main_widget.setLayout(main_layout)
        self.setCentralWidget(self.main_widget)
    
    def find_optimal(self):
        self.set_loading_ui()

        # 1. Create matrix from selected sponsor_flags
        calculate_matrix: list[list[int]] = []
        m_row_headers: list[str] = []
        for idx, flag in enumerate(self.sponsor_flags):
            if flag == 1:
                calculate_matrix.append(matrix[idx])
                m_row_headers.append(row_headers[idx])

        # 2. Pass matrix to solver
        row_ind, col_ind = solve_hungarian(calculate_matrix, maximize=True)
        optimal_list = []
        optimal_value = 0
        for row, col in zip(row_ind, col_ind):
            if row >= len(m_row_headers) or col >= len(column_headers):
                continue
            optimal_list.append([row, col])
            optimal_list.sort(key=lambda x: x[1])
            if row < len(row_headers):
                optimal_value = optimal_value + int(calculate_matrix[row][col])

        # 3. Pass result to UI
        for li in optimal_list:
            self.sponsor_slots[li[1]].setSponsorName(m_row_headers[li[0]])
        self.valueText.setText(str(optimal_value))

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
    def __init__(self, parent, title, sponsor_name="") -> None:
        super().__init__(parent)
        self.sponsor_name = sponsor_name
        self.setTitle(title)
        self.layout = QVBoxLayout()
        self.text = QLabel(self.sponsor_name)
        self.text.setStyleSheet("font-weight: bold")
        self.layout.addWidget(self.text)
        self.setLayout(self.layout)
    
    def setSponsorName(self, sponsor_name: str) -> None:
        self.text.setText(sponsor_name)

class SponsorCheckBox(QCheckBox):
    def __init__(self, parent, name, id) -> None:
        super().__init__(parent)
        self.setText(name)
        self.name = name
        self.id = id
    
    def get_id(self):
        return self.id

def solve_hungarian(matrix, maximize=False):
    """
    Solves the assignment problem using the Hungarian algorithm.
    
    Parameters:
    - matrix (2D list or numpy array): The cost matrix to minimize/maximize.
    - maximize (bool): If True, solve the maximization problem.
    
    Returns:
    - row_ind (list): The row indices of the optimal assignment.
    - col_ind (list): The column indices of the optimal assignment.
    - total_cost (float): The total cost of the optimal assignment.
    """
    # Convert to numpy array if necessary
    matrix = np.array(matrix)
    
    # Handle maximization by converting to minimization problem
    if maximize:
        matrix = matrix.max() - matrix
    
    # If the matrix is not square, pad it to make it square
    n_rows, n_cols = matrix.shape
    if n_rows != n_cols:
        max_dim = max(n_rows, n_cols)
        padded_matrix = np.zeros((max_dim, max_dim))
        padded_matrix[:n_rows, :n_cols] = matrix
        
        if maximize:
            padded_matrix[n_rows:, :] = 0
            padded_matrix[:, n_cols:] = 0
        else:
            padded_matrix[n_rows:, :] = matrix.max() + 1
            padded_matrix[:, n_cols:] = matrix.max() + 1
        
        matrix = padded_matrix
    
    # Solve the assignment problem
    row_ind, col_ind = linear_sum_assignment(matrix)
    
    return row_ind, col_ind

# inits file

# inits the UI
app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()