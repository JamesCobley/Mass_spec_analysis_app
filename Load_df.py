import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout, QPushButton, QFileDialog

class SimpleApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Upload an Excel file", self)
        layout.addWidget(self.label)

        upload_button = QPushButton("Choose File", self)
        upload_button.clicked.connect(self.show_file_dialog)
        layout.addWidget(upload_button)

        self.setLayout(layout)
        self.setWindowTitle("Simple PyQt Mass Spec App")
        self.setGeometry(300, 300, 300, 200)

    def show_file_dialog(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Excel File", "", "Excel Files (*.xlsx)")
        
        if file_path:
            self.label.setText(f"Selected file: {file_path}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleApp()
    ex.show()
    sys.exit(app.exec_())
