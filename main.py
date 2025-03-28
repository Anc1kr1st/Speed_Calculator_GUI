from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox

import sys

class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance:")
        self.distance_label_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Metric (km)', 'Imperial (miles)'])

        time_label = QLabel("Time (hours):")
        self.time_label_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 0)

        self.setLayout(grid)

    def calculate_speed(self):
        current_distance = float(self.distance_label_edit.text())
        current_time = float(self.time_label_edit.text())
        speed = current_distance / current_time

        if self.combo.currentText() == 'Metric (km)':
            speed = round(speed, 2)
            unit = "km/h"
        if self.combo.currentText() == 'Imperial (miles)':
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        self.output_label.setText(f"Average speed: {speed} {unit}.")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())