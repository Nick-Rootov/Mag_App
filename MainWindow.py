# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\igore\PycharmProjects\mag_app\ui\QT_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setGeometry(QtCore.QRect(-1, 140, 771, 551))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 331, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.DtpLabel1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.DtpLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.DtpLabel1.setObjectName("DtpLabel1")
        self.verticalLayout.addWidget(self.DtpLabel1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DtpLabel2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.DtpLabel2.setIndent(0)
        self.DtpLabel2.setObjectName("DtpLabel2")
        self.horizontalLayout.addWidget(self.DtpLabel2)
        self.DtpYearComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.DtpYearComboBox.setObjectName("DtpYearComboBox")
        self.DtpYearComboBox.addItem("")
        self.horizontalLayout.addWidget(self.DtpYearComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.DtpLabel3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.DtpLabel3.setIndent(0)
        self.DtpLabel3.setObjectName("DtpLabel3")
        self.horizontalLayout_5.addWidget(self.DtpLabel3)
        self.DtpMonthComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.DtpMonthComboBox.setObjectName("DtpMonthComboBox")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.DtpMonthComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.DtpMonthComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.DtpSearchButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.DtpSearchButton.setObjectName("DtpSearchButton")
        self.verticalLayout.addWidget(self.DtpSearchButton)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(430, 0, 331, 129))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.WeatherLabel1 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.WeatherLabel1.setAlignment(QtCore.Qt.AlignCenter)
        self.WeatherLabel1.setObjectName("WeatherLabel1")
        self.verticalLayout_2.addWidget(self.WeatherLabel1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.WeatherLabel2 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.WeatherLabel2.setObjectName("WeatherLabel2")
        self.horizontalLayout_2.addWidget(self.WeatherLabel2)
        self.WatherYearComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.WatherYearComboBox.setObjectName("WatherYearComboBox")
        self.WatherYearComboBox.addItem("")
        self.WatherYearComboBox.addItem("")
        self.WatherYearComboBox.addItem("")
        self.WatherYearComboBox.addItem("")
        self.WatherYearComboBox.addItem("")
        self.WatherYearComboBox.addItem("")
        self.WatherYearComboBox.addItem("")
        self.WatherYearComboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.WatherYearComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.WeatherLabel3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.WeatherLabel3.setObjectName("WeatherLabel3")
        self.horizontalLayout_3.addWidget(self.WeatherLabel3)
        self.WeatherMonthComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.WeatherMonthComboBox.setObjectName("WeatherMonthComboBox")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.WeatherMonthComboBox.addItem("")
        self.horizontalLayout_3.addWidget(self.WeatherMonthComboBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.WeatherSearchButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.WeatherSearchButton.setObjectName("WeatherSearchButton")
        self.verticalLayout_2.addWidget(self.WeatherSearchButton)
        self.LoadDataButton = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.LoadDataButton.setObjectName("LoadDataButton")
        self.verticalLayout_2.addWidget(self.LoadDataButton)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.widget1 = QtWidgets.QWidget(self.tab_2)
        self.widget1.setGeometry(QtCore.QRect(10, 70, 771, 301))
        self.widget1.setObjectName("widget1")
        self.widget2 = QtWidgets.QWidget(self.tab_2)
        self.widget2.setGeometry(QtCore.QRect(10, 410, 771, 301))
        self.widget2.setObjectName("widget2")
        self.CrashButton = QtWidgets.QPushButton(self.tab_2)
        self.CrashButton.setGeometry(QtCore.QRect(680, 30, 75, 31))
        self.CrashButton.setObjectName("CrashButton")
        self.comboBox = QtWidgets.QComboBox(self.tab_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 341, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(20, 40, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(20, 380, 91, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox_2 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_2.setGeometry(QtCore.QRect(120, 40, 161, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_3 = QtWidgets.QComboBox(self.tab_2)
        self.comboBox_3.setGeometry(QtCore.QRect(120, 380, 161, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MagApp"))
        self.DtpLabel1.setText(_translate("MainWindow", "Поиск ДТП"))
        self.DtpLabel2.setText(_translate("MainWindow", " Выберите год:"))
        self.DtpYearComboBox.setItemText(0, _translate("MainWindow", "2021"))
        self.DtpLabel3.setText(_translate("MainWindow", " Выберите месяц:"))
        self.DtpMonthComboBox.setItemText(0, _translate("MainWindow", "январь"))
        self.DtpMonthComboBox.setItemText(1, _translate("MainWindow", "февраль"))
        self.DtpMonthComboBox.setItemText(2, _translate("MainWindow", "март"))
        self.DtpMonthComboBox.setItemText(3, _translate("MainWindow", "апрель"))
        self.DtpMonthComboBox.setItemText(4, _translate("MainWindow", "май"))
        self.DtpMonthComboBox.setItemText(5, _translate("MainWindow", "июнь"))
        self.DtpMonthComboBox.setItemText(6, _translate("MainWindow", "июль"))
        self.DtpMonthComboBox.setItemText(7, _translate("MainWindow", "август"))
        self.DtpMonthComboBox.setItemText(8, _translate("MainWindow", "сентябрь"))
        self.DtpMonthComboBox.setItemText(9, _translate("MainWindow", "октябрь"))
        self.DtpMonthComboBox.setItemText(10, _translate("MainWindow", "ноябрь"))
        self.DtpMonthComboBox.setItemText(11, _translate("MainWindow", "декабрь"))
        self.DtpSearchButton.setText(_translate("MainWindow", "Найти"))
        self.WeatherLabel1.setText(_translate("MainWindow", "Поиск информации о погоде"))
        self.WeatherLabel2.setText(_translate("MainWindow", "Выберите год:"))
        self.WatherYearComboBox.setItemText(0, _translate("MainWindow", "2015"))
        self.WatherYearComboBox.setItemText(1, _translate("MainWindow", "2016"))
        self.WatherYearComboBox.setItemText(2, _translate("MainWindow", "2017"))
        self.WatherYearComboBox.setItemText(3, _translate("MainWindow", "2018"))
        self.WatherYearComboBox.setItemText(4, _translate("MainWindow", "2019"))
        self.WatherYearComboBox.setItemText(5, _translate("MainWindow", "2020"))
        self.WatherYearComboBox.setItemText(6, _translate("MainWindow", "2021"))
        self.WatherYearComboBox.setItemText(7, _translate("MainWindow", "2022"))
        self.WeatherLabel3.setText(_translate("MainWindow", "Выберите месяц:"))
        self.WeatherMonthComboBox.setCurrentText(_translate("MainWindow", "январь"))
        self.WeatherMonthComboBox.setItemText(0, _translate("MainWindow", "январь"))
        self.WeatherMonthComboBox.setItemText(1, _translate("MainWindow", "февраль"))
        self.WeatherMonthComboBox.setItemText(2, _translate("MainWindow", "март"))
        self.WeatherMonthComboBox.setItemText(3, _translate("MainWindow", "апрель"))
        self.WeatherMonthComboBox.setItemText(4, _translate("MainWindow", "май"))
        self.WeatherMonthComboBox.setItemText(5, _translate("MainWindow", "июнь"))
        self.WeatherMonthComboBox.setItemText(6, _translate("MainWindow", "июль"))
        self.WeatherMonthComboBox.setItemText(7, _translate("MainWindow", "август"))
        self.WeatherMonthComboBox.setItemText(8, _translate("MainWindow", "сентябрь"))
        self.WeatherMonthComboBox.setItemText(9, _translate("MainWindow", "октябрь"))
        self.WeatherMonthComboBox.setItemText(10, _translate("MainWindow", "ноябрь"))
        self.WeatherMonthComboBox.setItemText(11, _translate("MainWindow", "декабрь"))
        self.WeatherSearchButton.setText(_translate("MainWindow", "Найти"))
        self.LoadDataButton.setText(_translate("MainWindow", "Загрузить последние данные в таблицу"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Дорожно-транспортная инфраструктура"))
        self.CrashButton.setText(_translate("MainWindow", "Crash"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Котельная 1"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Котельная 2"))
        self.label.setText(_translate("MainWindow", "Выбор измерения:"))
        self.label_2.setText(_translate("MainWindow", "Выбор измерения:"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "оксид углерода (CO)"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "метан (CH4)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Инженерные сети теплоснабжения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Сети газоснабжения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Сети электроснабжения"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Сети водоснабжения"))
