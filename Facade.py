import random, sys
from collections import deque
import datetime
import pandas as pd
import matplotlib.pyplot as plt  # $ pip install matplotlib
import matplotlib.animation as animation
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy, QVBoxLayout, QMessageBox, QTableWidget, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from MainWindow import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib import dates
from SearchData import SearchDTP, SearchWeatherInfo

utech = 0
error_check_20_CO = True
error_check_100_CO = True
error_check_metan = True
excel_file_path = 'data/weather_january_2015.xlsx'

def plot_single_empty_graph_CO():
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10,7), dpi=85, facecolor='white',frameon=True, edgecolor='black',linewidth=1)
    fig.subplots_adjust(wspace=0.4,hspace=0.6,left=0.15,right=0.85,top=0.9,bottom=0.1)
    axes.grid(True, c='lightgrey', alpha=0.5)
    axes.set_title('Измерение уровня CO', fontsize=10)
    axes.set_xlabel('время', fontsize=8)
    axes.set_ylabel('мг/м^3', fontsize=8)

    return fig, axes

def plot_single_empty_graph_Metan():
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(10,7), dpi=85, facecolor='white',frameon=True, edgecolor='black',linewidth=1)
    fig.subplots_adjust(wspace=0.4,hspace=0.6,left=0.15,right=0.85,top=0.9,bottom=0.1)
    axes.grid(True, c='lightgrey', alpha=0.5)
    axes.set_title('Измерение уровня метана', fontsize=10)
    axes.set_xlabel('время', fontsize=8)
    axes.set_ylabel('% об.д.', fontsize=8)

    return fig, axes

def prepare_canvas_and_toolbar_CO(parent = None):
    parent.fig1, parent.axes1 = plot_single_empty_graph_CO()
    error_20_CO = QMessageBox()
    error_20_CO.setWindowTitle('Критические показатели')
    error_20_CO.setText('Превышение предельно допустимой концентрации оксида углерода в воздухе рабочей зоны!')
    error_20_CO.setStandardButtons(QMessageBox.Ok)
    #error.button(QMessageBox.Ok).animateClick(10)  # Автоматическое закрытие через 3 секунды
    error_100_CO = QMessageBox()
    error_100_CO.setWindowTitle('Критические показатели')
    error_100_CO.setText('Критический уровень концентрации оксида углерода в воздухе рабочей зоны!!!')
    error_100_CO.setStandardButtons(QMessageBox.Ok)
    #print(parent.comboBox.currentText())
    npoints = 500
    x = deque([0], maxlen=npoints)
    x[0] = datetime.datetime.now()
    y = deque([0], maxlen=npoints)
    y[0] = 8
    line, = parent.axes1.plot(x, y)
    #[line] = parent.axes1.step(x, y)
    parent.fig1.autofmt_xdate()
    parent.axes1.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
    print('Test')
    parent.axes1.set_ybound(0,25)
    #print(parent.axes1.ylim)

    def update(dy):
        z = random.randint(-100, 100)/500
        x.append(datetime.datetime.now())  # update data
        y.append(y[-1] + z + utech)
        #print(y[-1] + z)
        if (y[-1] + z)>=20:
            line.set_color("orange")
        if (y[-1] + z)>=100:
            line.set_color("red")
        #y.append(y[-1] + 1)
        line.set_xdata(x)  # update plot data
        line.set_ydata(y)
        #print(x[0])
        parent.axes1.relim()  # update axes limits
        if error_check_20_CO and (y[-1] + z)>=20:
            error_20_CO.exec_()
            with open('incident.txt', 'a') as file:
                file.write(f'{parent.comboBox.currentText()}: Превышение предельно допустимой концентрации оксида углерода в воздухе рабочей зоны!; {x[-1]}; \n')
            file.close()
            shift_1_check_CO()

        if error_check_100_CO and (y[-1] + z)>=100:
            error_100_CO.exec_()
            print('Test33')
            with open('incident.txt', 'a') as file:
                file.write(f'{parent.comboBox.currentText()}: Критический уровень концентрации оксида углерода в воздухе рабочей зоны!!!; {x[-1]}; \n')
            file.close()
            shift_2_check_CO()

        if (y[-1] + z)>=20:
            parent.axes1.autoscale_view(True, True, True)
        else:
            parent.axes1.autoscale_view(True, True, False)



        return line, parent.axes1

    def data_gen():
        while True:
            yield 1 if random.random() <= 0.5 else -1

    def shift_1_check_CO():
        global error_check_20_CO
        error_check_20_CO = False

    def shift_2_check_CO():
        global error_check_100_CO
        error_check_100_CO = False

    parent.ani = animation.FuncAnimation(parent.fig1, update, data_gen, interval=1000)
    parent.ani.event_source.start()

    parent.companovka_for_mpl = QVBoxLayout(parent.widget1)
    parent.canvas = MyMplCanvas(parent.fig1)
    parent.companovka_for_mpl.addWidget(parent.canvas)
    parent.toolbar = NavigationToolbar2QT(parent.canvas, parent)
    parent.companovka_for_mpl.addWidget(parent.toolbar)


def prepare_canvas_and_toolbar2(parent=None):
    parent.fig2, parent.axes2 = plot_single_empty_graph_Metan()

    npoints = 500
    x = deque([0], maxlen=npoints)
    x[0] = datetime.datetime.now()
    y = deque([0], maxlen=npoints)
    y[0] = 0.05
    line, = parent.axes2.plot(x, y)
    parent.fig2.autofmt_xdate()
    parent.axes2.xaxis.set_major_formatter(dates.DateFormatter('%H:%M:%S'))
    parent.axes2.set_ybound(0,0.88)

    def update(dy):
        z = random.randint(-100, 100)/100000
        x.append(datetime.datetime.now())  # update data
        #y.append(y[-1] + 1)
        y.append(y[-1] + z)
        #line.set_xdata(x)  # update plot data
        #line.set_ydata(y)
        line.set_xdata(x)  # update plot data
        line.set_ydata(y)
        parent.axes2.relim()  # update axes limits
        parent.axes2.autoscale_view(True, True, False)

        return line, parent.axes2

    def data_gen():
        while True:
            yield 1 if random.random() <= 0.9 else -1

    parent.ani2 = animation.FuncAnimation(parent.fig2, update, data_gen, interval=1000)
    parent.ani2.event_source.start()

    parent.companovka_for_mpl = QVBoxLayout(parent.widget2)
    parent.canvas = MyMplCanvas(parent.fig2)
    parent.companovka_for_mpl.addWidget(parent.canvas)
    parent.toolbar = NavigationToolbar2QT(parent.canvas, parent)
    parent.companovka_for_mpl.addWidget(parent.toolbar)


class MyMplCanvas(FigureCanvasQTAgg):
    def __init__(self, fig, parent = None):
        self.fig = fig
        FigureCanvasQTAgg.__init__(self, self.fig)
        FigureCanvasQTAgg.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvasQTAgg.updateGeometry(self)


class MainWindow (QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.widgets_adjust()

    def widgets_adjust(self):
        self.CrashButton.clicked.connect(self.activation_utech)
        self.DtpSearchButton.clicked.connect(lambda: self.call_SearchDTP(self.DtpYearComboBox.currentText(),self.DtpMonthComboBox.currentText()))
        self.WeatherSearchButton.clicked.connect(lambda: self.call_SearchWetherInfo(self.WatherYearComboBox.currentText(),self.WeatherMonthComboBox.currentText()))
        prepare_canvas_and_toolbar_CO(parent=self)
        prepare_canvas_and_toolbar2(parent=self)

        self.LoadDataButton.clicked.connect(lambda: self.loadExcelData())
        #print(self.WeatherMonthComboBox.__dir__)

    def loadExcelData(self):
        df = pd.read_excel(excel_file_path)
        self.tableWidget.setRowCount(df.shape[0])
        self.tableWidget.setColumnCount(df.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(df.columns)

        for row in df.iterrows():
            #print(df.iterrows())
            values = row[1]
            #print(values)
            for col_index, value in enumerate(values):
                if isinstance(value, (float, int)):
                    value = '{0:0,.0f}'.format(value)
                tableItem = QTableWidgetItem(str(value))
                tableItem.setTextAlignment(Qt.AlignHCenter)
                self.tableWidget.setItem(row[0], col_index, tableItem)
        self.tableWidget.setColumnWidth(0, 190)
        self.tableWidget.setColumnWidth(1, 190)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 120)
        self.tableWidget.setColumnWidth(4, 150)
        self.tableWidget.setColumnWidth(5, 190)

    def activation_utech(self):
        print('Test_click')
        global utech
        print(utech)
        utech = utech + 0.4
        print(utech)

    def call_SearchDTP(self,year,month):
        SearchDTP(year,month)
        print('Test1')

    def call_SearchWetherInfo(self,year,month):
        global excel_file_path
        excel_file_path=SearchWeatherInfo(year,month)
        #print(excel_file_path)

def main_application ():
    app =  QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main_application()