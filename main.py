import sys
import pyqtgraph as pg
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from PyQt6.QtCore import Qt
from services.stock_api import get_stock_data
from datetime import datetime

class DateAxisItem(pg.AxisItem):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def tickStrings(self, values, scale, spacing):
        return [datetime.utcfromtimestamp(value).strftime('%Y-%m-%d') for value in values]

class StockApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Stock Market Tracker')
        self.setGeometry(100, 100, 1000, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        self.symbol_input = QLineEdit(self)
        self.symbol_input.setPlaceholderText('Enter stock symbol (e.g., AAPL)')
        self.symbol_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.symbol_input)

        self.load_button = QPushButton('Load Stock Data', self)
        layout.addWidget(self.load_button)

        date_axis = DateAxisItem(orientation='bottom')

        self.graph_widget = pg.PlotWidget(axisItems={'bottom': date_axis})
        layout.addWidget(self.graph_widget)

        self.info_label = QLabel('Enter a stock symbol and click "Load Stock Data" to see the chart.', self)
        self.info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.info_label)

        self.graph_widget.setTitle('Stock Price Over Time', color='b', size='15pt')
        self.graph_widget.setLabel('left', 'Price', color='white', size='10pt')
        self.graph_widget.setLabel('bottom', 'Time', color='white', size='10pt')
        self.graph_widget.showGrid(x=True, y=True)

        self.load_button.clicked.connect(self.load_data)

    def load_data(self):
        symbol = self.symbol_input.text()

        if not symbol:
            self.info_label.setText("Please enter a valid stock symbol.")
            return

        dates, prices = get_stock_data(symbol)

        if not dates:
            self.info_label.setText(f"No data found for symbol: {symbol}")
            return

        self.graph_widget.clear()

        x = [datetime.strptime(date, '%Y-%m-%d').timestamp() for date in dates]

        self.graph_widget.plot(x, prices, pen=pg.mkPen(color='g', width=2))

        self.info_label.setText(f"Showing data for: {symbol}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = StockApp()
    main.show()
    sys.exit(app.exec())
