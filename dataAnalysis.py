import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QDateEdit
from PyQt5.QtCore import QDate
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import yfinance as yf

class FinApp(QWidget):
    def __init__(self):
        super().__init__()
        self.figure, self.ax = plt.subplots(figsize=(12, 6))
        self.canvas = FigureCanvas(self.figure)
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        
        self.input_ticker = QLineEdit(self)
        self.input_ticker.setPlaceholderText("Search for stocks")
        self.layout.addWidget(self.input_ticker)

        self.date_start = QDateEdit(self)
        self.date_start.setCalendarPopup(True)
        self.date_start.setDate(QDate.currentDate().addYears(-1))
        self.layout.addWidget(self.date_start)

        self.date_end = QDateEdit(self)
        self.date_end.setCalendarPopup(True)
        self.date_end.setDate(QDate.currentDate())
        self.layout.addWidget(self.date_end)
        
        self.btn = QPushButton("Analiziraj", self)
        self.btn.clicked.connect(self.plot_data)
        self.layout.addWidget(self.btn)
        
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        self.show()

    def plot_data(self):
        stock = self.input_ticker.text()
        start_date = self.date_start.date().toString("yyyy-MM-dd")
        end_date = self.date_end.date().toString("yyyy-MM-dd")

        try:
            data = yf.download(stock, start=start_date, end=end_date)
            if data.empty:
                raise ValueError("No data for that stock.")

            data["SMA_50"] = data["Close"].rolling(window=50).mean()
            data["SMA_200"] = data["Close"].rolling(window=200).mean()

            self.ax.clear()
            self.ax.plot(data.index, data["Close"], label="Real price", color="blue", alpha=0.4)
            self.ax.plot(data.index, data["SMA_50"], label="50 day average", color="orange")
            self.ax.plot(data.index, data["SMA_200"], label="200 day average", color="red")

            self.ax.set_title(f"Analysis: {stock}")
            self.ax.set_xlabel("Date")
            self.ax.set_ylabel("USD price")
            self.ax.legend(loc="upper left")
            self.ax.grid(True, linestyle='--')

            self.canvas.draw()
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = FinApp()
    sys.exit(app.exec_())