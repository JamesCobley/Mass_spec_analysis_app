import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QFileDialog

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label to display messages
        self.label = QLabel("Upload an Excel file", self)
        layout.addWidget(self.label)

        # Upload button to select the file
        upload_button = QPushButton("Choose File", self)
        upload_button.clicked.connect(self.show_file_dialog)
        layout.addWidget(upload_button)

        # Confirm button (initially hidden) to proceed after file selection
        self.confirm_button = QPushButton("Confirm File Selection", self)
        self.confirm_button.setVisible(False)  # Hidden by default
        self.confirm_button.clicked.connect(self.confirm_file_selection)
        layout.addWidget(self.confirm_button)

        self.setLayout(layout)
        self.setWindowTitle("Simple PyQt Mass Spec App")
        self.setGeometry(300, 300, 400, 200)

    def show_file_dialog(self):
        # Open file dialog to choose Excel file
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx)")
        
        if file_path:
            # Update the label with selected file path
            self.label.setText(f"Selected file: {file_path}")
            self.selected_file = file_path
            # Show the confirm button
            self.confirm_button.setVisible(True)

    def confirm_file_selection(self):
        # Handle the confirmed file (you can add more processing logic here)
        self.label.setText(f"File confirmed: {self.selected_file}")

# Main loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    ex.show()
    sys.exit(app.exec_())
