from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget


from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem, QPushButton, QHBoxLayout
)
import os


class DatasetManagerCentralWidget(QWidget):
    def __init__(self, dataset_directory="datasets"):
        super().__init__()
        self.dataset_directory = dataset_directory
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Table to list datasets
        self.dataset_table = QTableWidget()
        self.dataset_table.setColumnCount(3)
        self.dataset_table.setHorizontalHeaderLabels(["Dataset Name", "Size (KB)", "Source"])
        self.layout.addWidget(self.dataset_table)

        # Buttons for actions
        self.button_layout = QHBoxLayout()

        self.add_button = QPushButton("Add Dataset")
        self.add_button.clicked.connect(self.add_dataset)
        self.button_layout.addWidget(self.add_button)

        self.delete_button = QPushButton("Delete Dataset")
        self.delete_button.clicked.connect(self.delete_dataset)
        self.button_layout.addWidget(self.delete_button)

        self.view_button = QPushButton("View Dataset")
        self.view_button.clicked.connect(self.view_dataset)
        self.button_layout.addWidget(self.view_button)

        self.layout.addLayout(self.button_layout)

        # Load existing datasets
        self.load_datasets()

    def load_datasets(self):
        """Load datasets from the directory and populate the table."""
        if not os.path.exists(self.dataset_directory):
            os.makedirs(self.dataset_directory)

        self.dataset_table.setRowCount(0)  # Clear the table
        for dataset in os.listdir(self.dataset_directory):
            path = os.path.join(self.dataset_directory, dataset)
            if os.path.isfile(path):
                size_kb = os.path.getsize(path) // 1024
                row = self.dataset_table.rowCount()
                self.dataset_table.insertRow(row)
                self.dataset_table.setItem(row, 0, QTableWidgetItem(dataset))
                self.dataset_table.setItem(row, 1, QTableWidgetItem(f"{size_kb}"))
                self.dataset_table.setItem(row, 2, QTableWidgetItem("Local"))  # Default source

    def add_dataset(self):
        """Handle adding a new dataset."""
        print("Add Dataset clicked!")  # Placeholder for now

    def delete_dataset(self):
        """Handle deleting the selected dataset."""
        selected_row = self.dataset_table.currentRow()
        if selected_row == -1:
            print("No dataset selected!")
            return

        dataset_name = self.dataset_table.item(selected_row, 0).text()
        dataset_path = os.path.join(self.dataset_directory, dataset_name)

        try:
            os.remove(dataset_path)
            self.dataset_table.removeRow(selected_row)
            print(f"Deleted dataset: {dataset_name}")
        except Exception as e:
            print(f"Error deleting dataset: {e}")

    def view_dataset(self):
        """Handle viewing the selected dataset."""
        selected_row = self.dataset_table.currentRow()
        if selected_row == -1:
            print("No dataset selected!")
            return

        dataset_name = self.dataset_table.item(selected_row, 0).text()
        dataset_path = os.path.join(self.dataset_directory, dataset_name)

        try:
            with open(dataset_path, 'r', encoding='utf-8') as file:
                content = file.read(500)  # Show a preview of the dataset
            print(f"Preview of {dataset_name}:\n{content}")
        except Exception as e:
            print(f"Error viewing dataset: {e}")



class DatasetManagerLeftWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Dataset Manager Left Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class DatasetManagerRightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Dataset Manager Right Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class DataPreprocessingCentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Data Preprocessing Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class DataPreprocessingLeftWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Data Preprocessing Left Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class DataPreprocessingRightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Data Preprocessing Right Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class SearchEngineCentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Search Engine Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class SearchEngineLeftWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Search Engine Left Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class SearchEngineRightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Search Engine Right Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class WebCrawlerCentralWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Web Crawler Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class WebCrawlerLeftWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Web Crawler Left Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout


class WebCrawlerRightWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.placeholder_label = QLabel("Web Crawler Right Placeholder")
        self.layout.addWidget(self.placeholder_label)
        self.setLayout(self.layout)  # Set the layout
