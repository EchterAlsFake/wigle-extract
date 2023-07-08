"""

Version: 1.0
Author: EchterAlsFake
License: LGPLv3
GUI: PySide6 (Qt for Python) See qt.io
Source: https://github.com/EchterAlsFake/wigle-extract

The extracted Wi-Fi Networks are based on my personal experience.

Explanation:

O2:

O2 Wi-Fi Networks are manufactured mostly by the Askey Compute Corporation.
They have managed to DON'T care about security and they are using

12345670 as the default WPS Pin. This can easily be exploited and give an attacker
the whole PSK in 5 seconds.

TP-Link:

Tp-Link routers have several security issues. One is the Pixie Dust attack, which can calculate the WPS PIN with
a few data; that the Router just throws away.

The other exploitation is the WPS PIN bruteforce. You can on some routers just try all the 11000 pins, and you can
get the WPS PIN within a few hours.

WPA:

WPA is an old encryption mechanism on Wi-Fi Routers. It was developed to fix the security issues of the WEP encryption,
but WPA is still not secure, and it can be exploited in a few hours. Although, there are very fewer routers that are
actually running with WPA. Please note that WPA is NOT WPA2

WEP:

WEP was the first encryption method on Wi-Fi Routers. It uses a very weak encryption, and you can calculate the Password
by getting something called IVs. You can get the password within seconds or minutes. There are very few routers that are
using this encryption, and if you see someone, then it's maybe from the Government / Police to catch hackers.
"""
import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidget, QTableWidgetItem
from ui_form import Ui_Form
import os


class Widget(QWidget):

    def __init__(self):
        super().__init__()
        self.wep_list = []
        self.o2_list = []
        self.wpa_list = []
        self.tp_link_list = []


        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.button_scan.clicked.connect(self.start)



    def qmsg(self, text):

        qmsg_box = QMessageBox()
        qmsg_box.setText(str(text))
        qmsg_box.exec()

    def check_csv(self, path):

        if os.path.isfile(path):
            return True

        else:

            self.qmsg(text="CSV file not found.  Please check the path and try again.")

    def start(self):

        path = self.ui.lineedit_csv.text()

        if self.check_csv(path):

            self.get_data(path)

    def get_data(self, path):

        with open(path, "rb") as csv:
            content = csv.read().splitlines()

            for line in content:
                line = line.decode("utf-8", errors="replace")  # decode the line from bytes to string

                if ",," in line:
                    pass

                elif "WEP" in line:
                    self.wep_list.append(line)

                if "o2-WLAN" in line:
                    self.o2_list.append(line)

                if "tp-link" in line or "TP-Link" in line:
                    self.tp_link_list.append(line)

                if "WPA2" in line:
                    pass

                elif "WPA-PSK-TKIP" in line:
                    self.wpa_list.append(line)

        self.get_results()
        self.show_results()

    def clear_lists(self):
        self.cleared_wep_list = {}
        self.cleared_o2_list = {}
        self.cleared_tp_link_list = {}
        self.cleared_wpa_list = {}

        for item in self.wep_list:
            values = item.split(",")
            mac = values[0]
            if mac not in self.cleared_wep_list:
                self.cleared_wep_list[mac] = values

        for item in self.o2_list:
            values = item.split(",")
            mac = values[0]
            if mac not in self.cleared_o2_list:
                self.cleared_o2_list[mac] = values

        for item in self.tp_link_list:
            values = item.split(",")
            mac = values[0]
            if mac not in self.cleared_tp_link_list:
                self.cleared_tp_link_list[mac] = values

        for item in self.wpa_list:
            values = item.split(",")
            mac = values[0]
            if mac not in self.cleared_wpa_list:
                self.cleared_wpa_list[mac] = values

    def show_results(self):
        self.show_wep()
        self.show_wpa()
        self.show_o2()
        self.show_tp_link()
        self.update_labels()

    def get_results(self):
        print("Executed")
        self.clear_lists()
        self.wep_length = len(self.cleared_wep_list)
        self.o2_length = len(self.cleared_o2_list)
        self.tp_link_length = len(self.cleared_tp_link_list)
        self.wpa_length = len(self.cleared_wpa_list)
        self.all_length = self.wep_length + self.o2_length + self.tp_link_length + self.wpa_length

    def show_wep(self):
        table = self.ui.table_widget_wep
        table.setRowCount(len(self.cleared_wep_list))
        for row, mac in enumerate(self.cleared_wep_list):
            values = self.cleared_wep_list[mac]
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]
            table.setItem(row, 0, QTableWidgetItem(mac))
            table.setItem(row, 1, QTableWidgetItem(name))
            table.setItem(row, 2, QTableWidgetItem(gps_latitude))
            table.setItem(row, 3, QTableWidgetItem(gps_longitude))

        table.resizeColumnsToContents()

    def show_wpa(self):
        table = self.ui.table_widget_wpa
        table.setRowCount(len(self.cleared_wpa_list))
        for row, mac in enumerate(self.cleared_wpa_list):
            values = self.cleared_wpa_list[mac]
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]
            table.setItem(row, 0, QTableWidgetItem(mac))
            table.setItem(row, 1, QTableWidgetItem(name))
            table.setItem(row, 2, QTableWidgetItem(gps_latitude))
            table.setItem(row, 3, QTableWidgetItem(gps_longitude))

        table.resizeColumnsToContents()


    def show_o2(self):

        table = self.ui.table_widget_o2
        table.setRowCount(len(self.cleared_o2_list))
        for row, mac in enumerate(self.cleared_o2_list):
            values = self.cleared_o2_list[mac]
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]
            table.setItem(row, 0, QTableWidgetItem(mac))
            table.setItem(row, 1, QTableWidgetItem(name))
            table.setItem(row, 2, QTableWidgetItem(gps_latitude))
            table.setItem(row, 3, QTableWidgetItem(gps_longitude))

        table.resizeColumnsToContents()

    def show_tp_link(self):

        table = self.ui.table_widget_tp_link
        table.setRowCount(len(self.cleared_tp_link_list))
        for row, mac in enumerate(self.cleared_tp_link_list):
            values = self.cleared_tp_link_list[mac]
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]
            table.setItem(row, 0, QTableWidgetItem(mac))
            table.setItem(row, 1, QTableWidgetItem(name))
            table.setItem(row, 2, QTableWidgetItem(gps_latitude))
            table.setItem(row, 3, QTableWidgetItem(gps_longitude))

        table.resizeColumnsToContents()

    def update_labels(self):


        wep = len(self.cleared_wep_list)
        wpa = len(self.cleared_wpa_list)
        o2 = len(self.cleared_o2_list)
        tp_link = len(self.cleared_tp_link_list)
        total = wep + wpa + o2 + tp_link

        self.ui.lineedit_total.setText(str(total))
        self.ui.lineedit_wep_total.setText(str(wep))
        self.ui.lineedit_wpa_total.setText(str(wpa))
        self.ui.lineedit_o2_total.setText(str(o2))
        self.ui.lineedit_tp_link_total.setText(str(tp_link))


if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    app.exec()