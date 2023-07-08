# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1094, 822)
        Form.setStyleSheet(u"background-color: rgb(0, 0, 0)")
        self.gridLayout_3 = QGridLayout(Form)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_csv = QLabel(Form)
        self.label_csv.setObjectName(u"label_csv")
        self.label_csv.setStyleSheet(u"color: white")

        self.horizontalLayout.addWidget(self.label_csv)

        self.lineedit_csv = QLineEdit(Form)
        self.lineedit_csv.setObjectName(u"lineedit_csv")
        self.lineedit_csv.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.horizontalLayout.addWidget(self.lineedit_csv)

        self.button_scan = QPushButton(Form)
        self.button_scan.setObjectName(u"button_scan")
        self.button_scan.setStyleSheet(u"QPushButton {\n"
"    background-color: #5468ff;\n"
"	border-width: 2px;\n"
"	border-color: rgb(98, 255, 182);\n"
"	border-style: double;\n"
"    border-radius: 6px;\n"
"    color: #fff;\n"
"    font-family: \"JetBrains Mono\", monospace;\n"
"    font-size: 15px;\n"
"    padding: 0px 16px 0px 16px;\n"
"    height: 24px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #3c4fe0;\n"
"	border-color: rgb(179, 0, 255)\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #3c4fe0;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.button_scan)


        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.table_widget_wpa = QTableWidget(self.groupBox)
        if (self.table_widget_wpa.columnCount() < 4):
            self.table_widget_wpa.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget_wpa.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget_wpa.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget_wpa.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget_wpa.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_widget_wpa.setObjectName(u"table_widget_wpa")
        self.table_widget_wpa.setStyleSheet(u"background-color: gray;\n"
"color: white;")

        self.gridLayout.addWidget(self.table_widget_wpa, 3, 0, 1, 1)

        self.label_tp_link = QLabel(self.groupBox)
        self.label_tp_link.setObjectName(u"label_tp_link")
        self.label_tp_link.setStyleSheet(u"color: white")

        self.gridLayout.addWidget(self.label_tp_link, 0, 1, 1, 1)

        self.table_widget_wep = QTableWidget(self.groupBox)
        if (self.table_widget_wep.columnCount() < 4):
            self.table_widget_wep.setColumnCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_widget_wep.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_widget_wep.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_widget_wep.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_widget_wep.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        self.table_widget_wep.setObjectName(u"table_widget_wep")
        self.table_widget_wep.setStyleSheet(u"background-color: gray;\n"
"color: white;")

        self.gridLayout.addWidget(self.table_widget_wep, 3, 1, 1, 1)

        self.label_o2 = QLabel(self.groupBox)
        self.label_o2.setObjectName(u"label_o2")
        self.label_o2.setStyleSheet(u"color: white;")

        self.gridLayout.addWidget(self.label_o2, 0, 0, 1, 1)

        self.table_widget_tp_link = QTableWidget(self.groupBox)
        if (self.table_widget_tp_link.columnCount() < 4):
            self.table_widget_tp_link.setColumnCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_widget_tp_link.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_widget_tp_link.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_widget_tp_link.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_widget_tp_link.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        self.table_widget_tp_link.setObjectName(u"table_widget_tp_link")
        self.table_widget_tp_link.setStyleSheet(u"background-color: gray;\n"
"color: white;")

        self.gridLayout.addWidget(self.table_widget_tp_link, 1, 1, 1, 1)

        self.table_widget_o2 = QTableWidget(self.groupBox)
        if (self.table_widget_o2.columnCount() < 4):
            self.table_widget_o2.setColumnCount(4)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_widget_o2.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_widget_o2.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_widget_o2.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_widget_o2.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        self.table_widget_o2.setObjectName(u"table_widget_o2")
        self.table_widget_o2.setStyleSheet(u"background-color: gray;\n"
"color: white;\n"
"")

        self.gridLayout.addWidget(self.table_widget_o2, 1, 0, 1, 1)

        self.label_wpa = QLabel(self.groupBox)
        self.label_wpa.setObjectName(u"label_wpa")
        self.label_wpa.setStyleSheet(u"color: white")

        self.gridLayout.addWidget(self.label_wpa, 2, 0, 1, 1)

        self.label_wep = QLabel(self.groupBox)
        self.label_wep.setObjectName(u"label_wep")
        self.label_wep.setStyleSheet(u"color: white")

        self.gridLayout.addWidget(self.label_wep, 2, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_wep_total = QLabel(self.groupBox_2)
        self.label_wep_total.setObjectName(u"label_wep_total")
        self.label_wep_total.setStyleSheet(u"color: white")

        self.gridLayout_2.addWidget(self.label_wep_total, 0, 0, 1, 1)

        self.lineedit_wep_total = QLineEdit(self.groupBox_2)
        self.lineedit_wep_total.setObjectName(u"lineedit_wep_total")
        self.lineedit_wep_total.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.gridLayout_2.addWidget(self.lineedit_wep_total, 0, 1, 1, 1)

        self.label_wpa_total = QLabel(self.groupBox_2)
        self.label_wpa_total.setObjectName(u"label_wpa_total")
        self.label_wpa_total.setStyleSheet(u"color: white")

        self.gridLayout_2.addWidget(self.label_wpa_total, 1, 0, 1, 1)

        self.lineedit_wpa_total = QLineEdit(self.groupBox_2)
        self.lineedit_wpa_total.setObjectName(u"lineedit_wpa_total")
        self.lineedit_wpa_total.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.gridLayout_2.addWidget(self.lineedit_wpa_total, 1, 1, 1, 1)

        self.label_o2_total = QLabel(self.groupBox_2)
        self.label_o2_total.setObjectName(u"label_o2_total")
        self.label_o2_total.setStyleSheet(u"color: white")

        self.gridLayout_2.addWidget(self.label_o2_total, 2, 0, 1, 1)

        self.lineedit_o2_total = QLineEdit(self.groupBox_2)
        self.lineedit_o2_total.setObjectName(u"lineedit_o2_total")
        self.lineedit_o2_total.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.gridLayout_2.addWidget(self.lineedit_o2_total, 2, 1, 1, 1)

        self.label_tp_link_total = QLabel(self.groupBox_2)
        self.label_tp_link_total.setObjectName(u"label_tp_link_total")
        self.label_tp_link_total.setStyleSheet(u"color: white")

        self.gridLayout_2.addWidget(self.label_tp_link_total, 3, 0, 1, 1)

        self.lineedit_tp_link_total = QLineEdit(self.groupBox_2)
        self.lineedit_tp_link_total.setObjectName(u"lineedit_tp_link_total")
        self.lineedit_tp_link_total.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.gridLayout_2.addWidget(self.lineedit_tp_link_total, 3, 1, 1, 1)

        self.label_total = QLabel(self.groupBox_2)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setStyleSheet(u"color: white")

        self.gridLayout_2.addWidget(self.label_total, 4, 0, 1, 1)

        self.lineedit_total = QLineEdit(self.groupBox_2)
        self.lineedit_total.setObjectName(u"lineedit_total")
        self.lineedit_total.setStyleSheet(u"QLineEdit {\n"
"    border: 2px solid #757575;\n"
"    border-radius: 5px;\n"
"    padding: 0 8px;\n"
"    background: rgb(94, 92, 100);  /* setzt den Hintergrund auf Schwarz */\n"
"    color: #FFFFFF;  /* setzt die Textfarbe auf Wei\u00df */\n"
"    font-size: 16px;\n"
"    height: 20px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border-color: rgb(107, 0, 255)\n"
"}\n"
"\n"
"QLineEdit:disabled {\n"
"    background: #444444;  /* setzt den Hintergrund auf ein dunkles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    color: #aaaaaa;  /* setzt die Textfarbe auf ein helles Grau, wenn das QLineEdit deaktiviert ist */\n"
"    border-color: #aaaaaa;\n"
"}")

        self.gridLayout_2.addWidget(self.lineedit_total, 4, 1, 1, 1)


        self.gridLayout_3.addWidget(self.groupBox_2, 2, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Wigle-Extract : 1.0 : LGPLv3 : https://github.com/EchterAlsFake/wigle-extract", None))
        self.label_csv.setText(QCoreApplication.translate("Form", u"CSV File:", None))
        self.button_scan.setText(QCoreApplication.translate("Form", u"Scan", None))
        self.groupBox.setTitle("")
        ___qtablewidgetitem = self.table_widget_wpa.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem1 = self.table_widget_wpa.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Mac", None));
        ___qtablewidgetitem2 = self.table_widget_wpa.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Lat", None));
        ___qtablewidgetitem3 = self.table_widget_wpa.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Lon", None));
        self.label_tp_link.setText(QCoreApplication.translate("Form", u"TP-Link", None))
        ___qtablewidgetitem4 = self.table_widget_wep.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem5 = self.table_widget_wep.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"MAC", None));
        ___qtablewidgetitem6 = self.table_widget_wep.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Lat", None));
        ___qtablewidgetitem7 = self.table_widget_wep.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Lon", None));
        self.label_o2.setText(QCoreApplication.translate("Form", u"O2", None))
        ___qtablewidgetitem8 = self.table_widget_tp_link.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem9 = self.table_widget_tp_link.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"MAC", None));
        ___qtablewidgetitem10 = self.table_widget_tp_link.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Lat", None));
        ___qtablewidgetitem11 = self.table_widget_tp_link.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Lon", None));
        ___qtablewidgetitem12 = self.table_widget_o2.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem13 = self.table_widget_o2.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"MAC", None));
        ___qtablewidgetitem14 = self.table_widget_o2.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Lat", None));
        ___qtablewidgetitem15 = self.table_widget_o2.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"Lon", None));
        self.label_wpa.setText(QCoreApplication.translate("Form", u"WPA", None))
        self.label_wep.setText(QCoreApplication.translate("Form", u"WEP", None))
        self.groupBox_2.setTitle("")
        self.label_wep_total.setText(QCoreApplication.translate("Form", u"WEP:", None))
        self.label_wpa_total.setText(QCoreApplication.translate("Form", u"WPA:", None))
        self.label_o2_total.setText(QCoreApplication.translate("Form", u"O2:", None))
        self.label_tp_link_total.setText(QCoreApplication.translate("Form", u"TP-Link:", None))
        self.label_total.setText(QCoreApplication.translate("Form", u"Total:", None))
    # retranslateUi

