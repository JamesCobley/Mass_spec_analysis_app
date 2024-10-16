import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QFileDialog, QTextEdit

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Label to display instructions or file path
        self.label = QLabel("Upload an Excel file", self)
        layout.addWidget(self.label)

        # Upload button to select the file
        upload_button = QPushButton("Choose File", self)
        upload_button.clicked.connect(self.show_file_dialog)
        layout.addWidget(upload_button)

        # Confirm button to proceed after file selection
        self.confirm_button = QPushButton("Confirm File Selection", self)
        self.confirm_button.setVisible(False)  # Hidden by default
        self.confirm_button.clicked.connect(self.confirm_file_selection)
        layout.addWidget(self.confirm_button)

        # Text area to display file contents or other messages
        self.text_area = QTextEdit(self)
        self.text_area.setReadOnly(True)  # Make the text area read-only
        layout.addWidget(self.text_area)

        self.setLayout(layout)
        self.setWindowTitle("Simple PyQt Mass Spec App")
        self.setGeometry(300, 300, 600, 400)

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
        # Handle the confirmed file (load and process Excel data)
        try:
            # Load the Excel file using Pandas
            df = pd.read_excel(self.selected_file)

            # Display some file information in the text area
            file_info = f"File confirmed: {self.selected_file}\n\n"
            file_info += f"Sheet Name: {df.columns}\n\n"
            file_info += f"Preview of the data:\n{df.head()}"
            
            # Display the file information and preview in the text area
            self.text_area.setText(file_info)

        except Exception as e:
            # In case of an error, display the error message
            self.text_area.setText(f"Error loading file: {e}")

# Main loop
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    ex.show()
    sys.exit(app.exec_())
