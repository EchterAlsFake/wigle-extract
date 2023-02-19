from colorama import *
import configparser, sys, datetime


class Configure():
    def __init__(self):

        self.conf = configparser.ConfigParser()
        self.conf.read("config.ini")
        try:
            self.variables()
            print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTMAGENTA_EX + "Variables loaded...")
        except Exception as e:
            print(Fore.LIGHTRED_EX + "[!] " + Fore.LIGHTMAGENTA_EX + "Error: " + str(e))
            sys.exit()
        self.get_language()

        if self.language == "Deutsch":
            print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Konfiguration abgeschlossen!")
        elif self.language == "English":
            print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTYELLOW_EX + "Configuration successful!")

    def get_language(self):

        if self.conf['Language']['not_set'] == 'true':
            self.set_language()

        elif self.conf['Language']['german'] == 'true':
            self.language = "Deutsch"
            print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTBLUE_EX + "Sprache: Deutsch")
            self.configure_german()

        elif self.conf['Language']['english'] == 'true':
            self.language = "English"
            self.configure_english()

    def set_language(self):

        language = input(f"""
Please select your language:

{Fore.LIGHTMAGENTA_EX}1) German / Deutsch
{Fore.LIGHTYELLOW_EX}2) English / Englisch
--------------------->:""")
        try:
            with open("config.ini", 'w') as ConfigFile:

                if language == "1":
                    self.conf.set("Language", 'german', 'true')
                    self.conf.set("Language", 'not_set', 'false')
                    self.conf.write(ConfigFile)
                    self.configure_german()

                elif language == "2":
                    self.conf.set("Language", 'english', 'true')
                    self.conf.set("Language", "not_set", 'false')
                    self.conf.write(ConfigFile)
                    self.configure_english()

                else:
                    print("ERR:  Wrong number.  Please choose between 1 and 2")
        except KeyError as e:
            print(f"KeyError:  {e}.  This mostly happens because of a misconfiguration in the config.ini file")

    def configure_german(self):

        if self.conf['AGB']['accept'] == 'false':
            self.agb_german()

        self.file = input(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTCYAN_EX + "Bitte gib den Pfad zur CSV Datei ein: ")
        self.date = datetime.datetime.now()

    def configure_english(self):

        self.file = input(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTYELLOW_EX + "Please enter the path to your CSV file: ")
        self.date = datetime.datetime.now()

        if self.conf['AGB']['accept'] == 'false':
            self.agb_english()

    def agb_german(self):

        agb = input("""
Bevor du mit der Benutzung des Programmes anfängst möchte ich, dass du folgendes liest.

Dieses Programm wurde von EchterAlsFake (Johannes Habel) entwickelt. Ich hatte hilfe von ChatGPT (chat.openai.com) 

Dir ist es als Nutzer erlaubt, dinge zu verändern und zu veröffentlichen, allerdings nur, WENN du daraufhinweist, dass
du etwas verändert hast und du must die Quelle für das Original (https://github.com/EchterAlsFake/wigle-extract) angeben.

Das Programm wurde erstellt um zu zeigen, wie viele W-LAN Netzwerke bis heute noch unter schlechter Sicherheit leiden.
Ich möchte nicht, dass du gezielt nach W-LAN Netzwerken suchst, welche eine Schwachstelle haben. Im Endeffekt liegt es an dir
wie du dieses Programm nutzt. Ich bin nur der Programmierer, du bist der Benutzer und ich bin in keiner Weise haftbar für
Schäden die durch die Benutzung des Programmes entstehen!

Das Programm funktioniert ohne Internet und sammelt keine Daten. Ich bin für Privatsphäre und möchte niemanden
zwingen irgendwelche 'Diagnosedaten' hochzuladen.  Solltest du Fehler usw. bekommen, dann kannst du auf die obrige Seite gehen
und dort in der Sektion 'Issues' einen Fehler melden. Andernfalls kannst du den Fehler auch an meine E-Mail senden:

EchterAlsFake@proton.me

1) Ich habe alles gelesen und akzeptiere die Bedingungen.
2) Ich habe alles gelesen und stimme den Bedingungen NICHT zu.
----------------------------------------------------------------=>""")
        if agb == "1":
            with open("config.ini", 'w') as ConfigFile:
                self.conf.set("AGB", 'accept', 'true')
                self.conf.write(ConfigFile)

        elif agb == "2":
            with open("config.ini", 'w') as ConfigFile:
                self.conf.set("AGB", 'accept', 'false')
                self.conf.write(ConfigFile)

        else:
            print("Wrong number.  Please choose between 1 and 2")

    def agb_english(self):
        agb = input("""

Hello! Before you start using the program, I would like you to read the following:
This program was developed by EchterAlsFake (Johannes Habel), with the help of ChatGPT (chat.openai.com).
As a user, you are allowed to modify and publish things, but only IF you indicate that you have made changes and you MUST provide the source for the original (https://github.com/EchterAlsFake/wigle-extract).
The program was created to demonstrate how many Wi-Fi networks still suffer from poor security today. I do not want you to intentionally search for Wi-Fi networks with vulnerabilities. 
Ultimately, it is up to you how you use this program. I am only the programmer, you are the user, and I am not liable for any damages caused by the use of the program.
The program works without internet and does not collect any data. I am committed to privacy and do not want to force anyone to upload any 'diagnostic data'. If you encounter any errors, 
you can go to the above-mentioned page and report the issue in the 'Issues' section. Alternatively, you can also send the error to my email:

EchterAlsFake@proton.me

I have read and agree to the terms.
I have read and do not agree to the terms.
----------------------------------------------------=>

""")

    def variables(self):

        if self.conf['WPS']['tp_link'] == 'true':
            self.wps_tp_link = True
            self.wps_tp_link_ext = Fore.LIGHTGREEN_EX + "Enabled"

        elif self.conf['WPS']['tp_link'] == 'false':
            self.wps_tp_link = False
            self.wps_tp_link_ext = Fore.LIGHTRED_EX + "Disabled"

        if self.conf['WPS']['o2'] == 'true':
            self.wps_o2 = True
            self.wps_o2_ext = Fore.LIGHTGREEN_EX + "Enabled"

        elif self.conf['WPS']['o2'] == 'false':
            self.wps_o2 = False
            self.wps_o2_ext = Fore.LIGHTRED_EX + "Disabled"

        if self.conf['WPA']['tkip'] == 'true':
            self.wpa = True
            self.wpa_ext = Fore.LIGHTGREEN_EX + "Enabled"

        elif self.conf['WPA']['tkip'] == 'false':
            self.wpa = False
            self.wpa_ext = Fore.LIGHTRED_EX + "Disabled"

        if self.conf['WEP']['wep'] == 'true':
            self.wep = True
            self.wep_ext = Fore.LIGHTGREEN_EX + "Enabled"

        elif self.conf['WEP']['wep'] == 'false':
            self.wep = False
            self.wep_ext = Fore.LIGHTRED_EX + "Disabled"

        else:
            print("Variables not loaded.")



class Wigle_German(Configure):

    def __init__(self):
        super().__init__()
        self.wep_list = []
        self.wpa_list = []
        self.tp_link_list = []
        self.o2_list = []
        self.menu()

    def menu(self):

        menu_input = input(f"""
{Fore.LIGHTCYAN_EX}1) Schwachstellen Analyse
{Fore.LIGHTGREEN_EX}2) Einstellungen
{Fore.LIGHTYELLOW_EX}3) Info
{Fore.LIGHTRED_EX}4) CSV Datei ändern
{Fore.LIGHTMAGENTA_EX}5) Exit        
{Fore.LIGHTRED_EX}------------------------------=>""")

        if menu_input == "1":
            self.vulnerability_search()
            self.get_results()
            self.show_results()

        elif menu_input == "2":
            self.settings()

        elif menu_input == "3":
            self.info()

        elif menu_input == "4":
            self.file = input(Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTMAGENTA_EX + "Bitte gib den Pfad zur CSV Datei ein: ")
            self.menu()

        elif menu_input == "5":
            exit()

    def settings(self):

        setting = input(f"""
        
        {Fore.LIGHTRED_EX}1) Aktivieren / Deaktivieren - Anzeigen von WEP Netzwerken.             Aktuell: {self.wep_ext}
        {Fore.LIGHTCYAN_EX}2) Aktivieren / Deaktivieren - Anzeigen von WPA Netzwerken.             Aktuell: {self.wps_tp_link_ext}
        {Fore.LIGHTMAGENTA_EX}3  Aktivieren / Deaktivieren - Anzeigen von o2  Netzwerken.             Aktuell: {self.wps_o2_ext}
        {Fore.LIGHTGREEN_EX}4) Aktivieren / Deaktivieren - Anzeigen von TP-Link Netzwerken.         Aktuell: {self.wps_tp_link_ext}
        {Fore.LIGHTYELLOW_EX}5) Sprache ändern - Englisch oder Deutsch.                              Aktuell: {self.language}
        {Fore.LIGHTRED_EX}----------------------------------------------------------------=>""")

        with open("config.ini", 'w') as ConfigFile:
            if setting == "1":

                if self.wep:
                    self.conf.set("WEP", 'wep', 'false')
                    self.conf.write(ConfigFile)

                elif not self.wep:
                    self.conf.set("WEP", 'wep', 'true')
                    self.conf.write(ConfigFile)

            elif setting == "2":

                if self.wpa:
                    self.conf.set("WPA", 'tkip', 'false')
                    self.conf.write(ConfigFile)

                elif not self.wpa:
                    self.conf.set("WPA", 'tkip', 'true')
                    self.conf.write(ConfigFile)

            elif setting == "3":

                if self.wps_o2:
                    self.conf.set("WPS", 'o2', 'false')
                    self.conf.write(ConfigFile)

                elif not self.wps_o2:
                    self.conf.set("WPS", 'o2', 'true')
                    self.conf.write(ConfigFile)

            elif setting == "4":

                if self.wps_tp_link:
                    self.conf.set("WPS", 'tp_link', 'false')
                    self.conf.write(ConfigFile)

                elif not self.wps_tp_link:
                    self.conf.set("WPS", 'tp_link', 'true')
                    self.conf.write(ConfigFile)

            elif setting == "5":

                if self.language == "Deutsch":

                    self.conf.set("Language", 'german', 'false')
                    self.conf.set("Language", 'english', 'true')
                    self.conf.write(ConfigFile)
                    self.configure_german()

                elif self.language == "English":

                    self.conf.set("Language", 'german', 'true')
                    self.conf.set("Language", 'english', 'false')
                    self.conf.write(ConfigFile)
                    self.configure_english()

                else:
                    print("Wrong number.  Please choose between 1 and 5")

    def vulnerability_search(self):
        with open(self.file, 'r') as csv_file:
            print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTCYAN_EX + "Daten werden ausgewertet....")
            text = csv_file.read().encode("utf-8").splitlines()
            for line in text:
                if ",," in str(line):
                    pass

                if self.wep:

                    if "WEP" and ",," in str(line):
                        pass

                    elif "WEP" in str(line):
                        self.wep_list.append(line)

                if self.wps_o2:

                    if "o2-WLAN" in str(line):
                        self.o2_list.append(line)

                if self.wps_tp_link:
                    if "tp-link" in str(line):
                        self.tp_link_list.append(line)

                    elif "TP-Link" in str(line):
                        self.tp_link_list.append(line)

                if self.wpa:
                    if "WPA-PSK-TKIP" and "WPA2" in str(line):
                        pass

                    elif "WPA-PSK-TKIP" in str(line):
                        self.wpa_list.append(line)

    def get_results(self):

        self.wep_length = len(self.wep_list)
        self.o2_length = len(self.o2_list)
        self.tp_link_length = len(self.tp_link_list)
        self.wpa_length = len(self.wpa_list)
        self.all_length = self.wep_length + self.o2_length + self.tp_link_length + self.wpa_length

    def show_results(self):

        if self.wep_length == 0:
            print(Fore.LIGHTRED_EX + "Es wurden keine WEP Netzwerke gefunden oder das Anzeigen dieser ist in den Einstellungen deaktiviert worden.")

        elif self.wep:
            print(f"{Fore.LIGHTRED_EX}Es wurden: {Fore.LIGHTWHITE_EX}{self.wep_length}{Fore.LIGHTRED_EX} WEP Netzwerke gefunden.")

        if self.o2_length == 0:
            print(Fore.LIGHTRED_EX + "Es wurden keine o2-WLAN Netzwerke gefunden oder das Anzeigen dieser ist in den Einstellungen deaktiviert worden.")

        elif self.o2_length:
            print(f"{Fore.LIGHTMAGENTA_EX}Es wurden: {Fore.LIGHTWHITE_EX}{self.o2_length}{Fore.LIGHTMAGENTA_EX} o2-WLAN Netzwerke gefunden.")

        if self.tp_link_length == 0:
            print(Fore.LIGHTRED_EX + "Es wurden keine TP-Link Netzwerke gefunden oder das Anzeigen dieser ist in den Einstellungen deaktiviert worden.")

        elif self.tp_link_length:
            print(f"{Fore.LIGHTGREEN_EX}Es wurden: {Fore.LIGHTWHITE_EX}{self.tp_link_length}{Fore.LIGHTGREEN_EX} TP-Link Netzwerke gefunden.")

        if self.wpa_length == 0:
            print(Fore.LIGHTRED_EX + "Es wurden keine WPA-PSK-TKIP Netzwerke gefunden oder das Anzeigen dieser ist in den Einstellungen deaktiviert worden.")

        elif self.wpa_length:
            print(f"{Fore.LIGHTBLUE_EX}Es wurden: {Fore.LIGHTWHITE_EX}{self.wpa_length} {Fore.LIGHTBLUE_EX}WPA-PSK-TKIP Netzwerke gefunden.")

        print(f"{Fore.LIGHTYELLOW_EX}Insgesamt haben: {Fore.LIGHTWHITE_EX}{self.all_length}{Fore.LIGHTYELLOW_EX} W-LAN Netzwerke eine potentielle Schwachstelle.")

        self.showing_input()

    def showing_input(self):
        self.showing = input(f"""
{Fore.LIGHTWHITE_EX}Falls du die Netzwerke mit Name und GPS Koordinaten anzeigen möchtest, dann kannst du unten die Zahl dafür eingeben:

{Fore.LIGHTRED_EX}1) WEP
{Fore.LIGHTBLUE_EX}2) WPA
{Fore.LIGHTMAGENTA_EX}3) o2-WLAN
{Fore.LIGHTGREEN_EX}4) TP-Link
{Fore.LIGHTYELLOW_EX}5) Die Analyse beenden. 
{Fore.LIGHTWHITE_EX}----------------=>:""")

        if self.showing == "1":
            self.show_wep()

        elif self.showing == "2":
            self.show_wpa()

        elif self.showing == "3":
            self.show_o2()

        elif self.showing == "4":
            self.show_tp_link()

        elif self.showing == "5":
            self.menu()

    def show_wep(self):

        for line in self.wep_list:

            values = line.decode().strip().split(",")
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]

            print("{:<30} {:<30} {:<30} {:<30}".format(f"{Fore.LIGHTYELLOW_EX}[Name]", f"{Fore.LIGHTCYAN_EX}[Latitude]", f"{Fore.LIGHTGREEN_EX}[Longitude]", f"{Fore.LIGHTWHITE_EX}[Mac] "))
            print("{:<30} {:<30} {:<30} {:<30}".format(Fore.LIGHTYELLOW_EX + name, Fore.LIGHTCYAN_EX + gps_latitude, Fore.LIGHTGREEN_EX + gps_longitude, Fore.LIGHTWHITE_EX + mac))

        self.showing_input()

    def show_wpa(self):

        for line in self.wpa_list:
            # Help from ChatGPT in this part of code.

            values = line.decode().strip().split(",")
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]

            print("{:<30} {:<30} {:<30} {:<30}".format(f"{Fore.LIGHTYELLOW_EX}[Name]", f"{Fore.LIGHTCYAN_EX}[Latitude]",
                                                       f"{Fore.LIGHTGREEN_EX}[Longitude]",
                                                       f"{Fore.LIGHTWHITE_EX}[Mac] "))
            print("{:<30} {:<30} {:<30} {:<30}".format(Fore.LIGHTYELLOW_EX + name, Fore.LIGHTCYAN_EX + gps_latitude,
                                                       Fore.LIGHTGREEN_EX + gps_longitude, Fore.LIGHTWHITE_EX + mac))
        self.showing_input()

    def show_o2(self):

        for line in self.o2_list:
            values = line.decode().strip().split(",")
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]

            print("{:<30} {:<30} {:<30} {:<30}".format(f"{Fore.LIGHTYELLOW_EX}[Name]", f"{Fore.LIGHTCYAN_EX}[Latitude]",
                                                       f"{Fore.LIGHTGREEN_EX}[Longitude]",
                                                       f"{Fore.LIGHTWHITE_EX}[Mac] "))
            print("{:<30} {:<30} {:<30} {:<30}".format(Fore.LIGHTYELLOW_EX + name, Fore.LIGHTCYAN_EX + gps_latitude,
                                                       Fore.LIGHTGREEN_EX + gps_longitude, Fore.LIGHTWHITE_EX + mac))
        self.showing_input()

    def show_tp_link(self):
        for line in self.tp_link_list:
            values = line.decode().strip().split(",")
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]

            print("{:<30} {:<30} {:<30} {:<30}".format(f"{Fore.LIGHTYELLOW_EX}[Name]", f"{Fore.LIGHTCYAN_EX}[Latitude]",
                                                       f"{Fore.LIGHTGREEN_EX}[Longitude]",
                                                       f"{Fore.LIGHTWHITE_EX}[Mac] "))
            print("{:<30} {:<30} {:<30} {:<30}".format(Fore.LIGHTYELLOW_EX + name, Fore.LIGHTCYAN_EX + gps_latitude,
                                                       Fore.LIGHTGREEN_EX + gps_longitude, Fore.LIGHTWHITE_EX + mac))

        self.showing_input()

    def program_info(self):
        print(f"""
{Fore.LIGHTWHITE_EX}
Wigle-Extract wurde von Johannes Habel (EchterAlsFake) entwickelt, um
zu zeigen, wie viele W-LAN Netzwerke bis heute eine Schwachstelle haben.

Das Programm wird mithilfe der CSV Dateien von Wigle benutzt.  Diese 
werden nach den Parametern meiner persönlichen Erfahrung ausgewertet.

Die Lizenz des Programmes, erlaubt es jedem es zu verändern und zu nutzen.
Bei Veränderung MUSS die Original Quelle angegeben werden (Creative Commons).""")

    def wpa_info(self):
        print(f"""{Fore.LIGHTRED_EX}W{Fore.LIGHTCYAN_EX}P{Fore.LIGHTYELLOW_EX}A
                                {Fore.LIGHTWHITE_EX}
WPA ist ein WLAN-Protokoll, das nach dem WEP-Standard entwickelt wurde. Es sollte die ursprünglichen Probleme von WEP lösen und eine bessere 
Sicherheit gewährleisten. Jedoch hat dies nicht ausgereicht und so kannWPA sehr schnell geknackt werden. Der Algorithmus basiert immer noch auf
dem von WEP, nur dass jetzt statt 24 Bit 48 Bit verwendet werden. Aber auch das ist nicht sicher. Siehe Michael Shutdown Exploit. Es gibt hier 
auch nur wenige WPA-Netzwerke und der Standard ist heute WPA2/WPA3.""")

    def wep_info(self):
        print(f"""
        {Fore.LIGHTWHITE_EX}{Fore.LIGHTYELLOW_EX}W{Fore.LIGHTCYAN_EX}E{Fore.LIGHTMAGENTA_EX}P  {Fore.LIGHTWHITE_EX}
WEP ist ein WLAN-Protokoll, das vor etwa 20 Jahren entwickelt wurde, um eine Möglichkeit zu bieten, ein WLAN-Netzwerk zu sichern. Allerdings ist dieses Netzwerkprotokoll anfällig für 
einige Angriffe. Ein Angreifer kann die Daten, die vom Gerät zum Router gesendet werden, manipulieren und durch eine schlechte Verschlüsselung das Passwort in weniger als 3 Stunden 
herausfinden. WEP sollte nicht mehr verwendet werden und stellt ein hohes Sicherheitsrisiko dar!""")

    def o2_info(self):
        print(f"""

    {Fore.LIGHTGREEN_EX}W{Fore.LIGHTYELLOW_EX}P{Fore.LIGHTCYAN_EX}S{Fore.LIGHTMAGENTA_EX}-{Fore.LIGHTGREEN_EX}o{Fore.LIGHTMAGENTA_EX}2{Fore.LIGHTWHITE_EX}
Die meisten WLAN-Netzwerke haben ein Feature namens WPS, welches eine schnelle Möglichkeit bietet, das WLAN-Passwort 
auszutauschen. Allerdings ist die Implementierung bei einigen  WLAN-Routern ziemlich schwach. WPS hat aufgrund einiger Fehler 
eine maximale Anzahl von 11000 möglichen Kombinationen. Man kann ein WLAN-Netzwerk in weniger als 4 Stunden hacken und mit 
dem 8-stelligen WPS-PIN das Passwort herausfinden. Es gibt keinen Grund, WPS zu verwenden, und man sollte es in den 
WLAN-Router-Einstellungen deaktivieren. Der Hersteller AVM hat als Standard-WPS-Methode die Push-Button-Connect-Methode, die 
als sicher gilt, da hier wirklich der Knopf gedrückt werden muss. Allerdings hat der Hersteller einiger o2-WLAN-Router das nicht 
so gut gemacht. Bei WLAN-Routern, die von der Askey Compute Corporation hergestellt wurden, ist der Standard-WPS-PIN 12345670, 
was ein hohes Sicherheitsrisiko darstellt. Somit kann das 20-stellige Passwort in 3-20 Sekunden ermittelt werden!""")

    def tp_link_info(self):
        print(f"""
        {Fore.LIGHTGREEN_EX}W{Fore.LIGHTYELLOW_EX}P{Fore.LIGHTCYAN_EX}S{Fore.LIGHTMAGENTA_EX}-{Fore.LIGHTGREEN_EX}T{Fore.LIGHTMAGENTA_EX}P{Fore.LIGHTWHITE_EX}-{Fore.LIGHTGREEN_EX}L{Fore.LIGHTMAGENTA_EX}I{Fore.LIGHTWHITE_EX}N{Fore.LIGHTMAGENTA_EX}K{Fore.LIGHTWHITE_EX}

Es gibt bei WPS einen weiteren Angriff, bei welchem einige Daten gesammelt werden und der PIN mit diesen berechnet
wird. Dieser Angriff nennt sich Pixie Dust und kann in wenigen Sekunden das Passwort herausfinden. Es sind häufig 
TP-Link Netzwerke von diesem Angriff betroffen und dazu, haben alle TP-Link Netzwerke keinen nennenswerten Schutz 
gegen Brute Force Attacken und wenn man ein bisschen Zeit hat, kann man auch hier das Passwort in ein paar Tagen
knacken.""")

    def info(self):

        options = input(f"""
{Fore.LIGHTGREEN_EX}1) Programm Info
{Fore.LIGHTRED_EX}2) WEP Info
{Fore.LIGHTCYAN_EX}3) WPA Info
{Fore.LIGHTMAGENTA_EX}4) o2 Info
{Fore.GREEN}5) TP-Link Info
{Fore.LIGHTYELLOW_EX}6) Exit
----------------=>:""")

        if options == "1":
            self.program_info()
            self.menu()

        elif options == "2":
            self.wep_info()
            self.menu()

        elif options == "3":
            self.wpa_info()
            self.menu()

        elif options == "4":
            self.o2_info()
            self.menu()

        elif options == "5":
            self.tp_link_info()
            self.menu()

        elif options == "6":
            self.menu()



class Wigle_English(Configure):

    def __init__(self):
        super().__init__()
        self.wep_list = []
        self.wpa_list = []
        self.tp_link_list = []
        self.o2_list = []
        self.menu()

    def menu(self):

        menu_input = input(f"""
    {Fore.LIGHTCYAN_EX}1) Security Analysis
    {Fore.LIGHTGREEN_EX}2) Settings
    {Fore.LIGHTYELLOW_EX}3) Info
    {Fore.LIGHTRED_EX}4) Change CSV file
    {Fore.LIGHTMAGENTA_EX}5) Exit        
    {Fore.LIGHTRED_EX}------------------------------=>""")

        if menu_input == "1":
            self.vulnerability_search()
            self.get_results()
            self.show_results()

        elif menu_input == "2":
            self.settings()

        elif menu_input == "3":
            self.info()

        elif menu_input == "4":
            self.file = input(
                Fore.LIGHTGREEN_EX + "[+]" + Fore.LIGHTMAGENTA_EX + "Please enter the path to the CSV file: ")

        elif menu_input == "5":
            exit()

    def settings(self):

        setting = input(f"""

            {Fore.LIGHTRED_EX}1) Enable / Disable - Showing WEP networks.             Currently: {self.wep_ext}
            {Fore.LIGHTCYAN_EX}2) Enable / Disable - Showing WPA nwtworks.             Currently: {self.wps_tp_link_ext}
            {Fore.LIGHTMAGENTA_EX}3  Enable / Disable - Showing o2 networks.              Currently: {self.wps_o2_ext}
            {Fore.LIGHTGREEN_EX}4) Enable / Disable - Showing TP-Link networks.         Currently: {self.wps_tp_link_ext}
            {Fore.LIGHTYELLOW_EX}5) Change Language - German or English.                 Currently: {self.language}
            {Fore.LIGHTRED_EX}----------------------------------------------------------------=>""")

        with open("config.ini", 'w') as ConfigFile:
            if setting == "1":

                if self.wep:
                    self.conf.set("WEP", 'wep', 'false')
                    self.conf.write(ConfigFile)

                elif not self.wep:
                    self.conf.set("WEP", 'wep', 'true')
                    self.conf.write(ConfigFile)

            elif setting == "2":

                if self.wpa:
                    self.conf.set("WPA", 'tkip', 'false')
                    self.conf.write(ConfigFile)

                elif not self.wpa:
                    self.conf.set("WPA", 'tkip', 'true')
                    self.conf.write(ConfigFile)

            elif setting == "3":

                if self.wps_o2:
                    self.conf.set("WPS", 'o2', 'false')
                    self.conf.write(ConfigFile)

                elif not self.wps_o2:
                    self.conf.set("WPS", 'o2', 'true')
                    self.conf.write(ConfigFile)

            elif setting == "4":

                if self.wps_tp_link:
                    self.conf.set("WPS", 'tp_link', 'false')
                    self.conf.write(ConfigFile)

                elif not self.wps_tp_link:
                    self.conf.set("WPS", 'tp_link', 'true')
                    self.conf.write(ConfigFile)

            elif setting == "5":

                if self.language == "Deutsch":

                    self.conf.set("Language", 'german', 'false')
                    self.conf.set("Language", 'english', 'true')
                    self.conf.write(ConfigFile)

                elif self.language == "English":

                    self.conf.set("Language", 'german', 'true')
                    self.conf.set("Language", 'english', 'false')
                    self.conf.write(ConfigFile)

                else:
                    print("Wrong number.  Please choose between 1 and 5")

    def vulnerability_search(self):
        with open(self.file, 'r') as csv_file:
            print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTCYAN_EX + "Analyzing data....")
            text = csv_file.read().encode("utf-8").splitlines()
            for line in text:
                if ",," in str(line):
                    pass

                if self.wep:

                    if "WEP" and ",," in str(line):
                        pass

                    elif "WEP" in str(line):
                        self.wep_list.append(line)

                if self.wps_o2:

                    if "o2-WLAN" in str(line):
                        self.o2_list.append(line)

                if self.wps_tp_link:
                    if "tp-link" in str(line):
                        self.tp_link_list.append(line)

                    elif "TP-Link" in str(line):
                        self.tp_link_list.append(line)

                if self.wpa:
                    if "WPA-PSK-TKIP" and "WPA2" in str(line):
                        pass

                    elif "WPA-PSK-TKIP" in str(line):
                        self.wpa_list.append(line)

    def get_results(self):

        self.wep_length = len(self.wep_list)
        self.o2_length = len(self.o2_list)
        self.tp_link_length = len(self.tp_link_list)
        self.wpa_length = len(self.wpa_list)
        self.all_length = self.wep_length + self.o2_length + self.tp_link_length + self.wpa_length

    def show_results(self):

        if self.wep_length == 0:
            print(
                Fore.LIGHTRED_EX + "No WEP networks were found or the display of these has been deactivated in the settings.")

        elif self.wep:
            print(
                f"{Fore.LIGHTRED_EX}Found: {Fore.LIGHTWHITE_EX}{self.wep_length}{Fore.LIGHTRED_EX} WEP networks.")

        if self.o2_length == 0:
            print(
                Fore.LIGHTRED_EX + "No o2 networks were found or the display of these has been deactivated in the settings.")

        elif self.o2_length:
            print(
                f"{Fore.LIGHTMAGENTA_EX}Found: {Fore.LIGHTWHITE_EX}{self.o2_length}{Fore.LIGHTMAGENTA_EX} o2-WLAN Netzwerke gefunden.")

        if self.tp_link_length == 0:
            print(
                Fore.LIGHTRED_EX + "No TP-Link networks were found or the display of these has been deactivated in the settings.")

        elif self.tp_link_length:
            print(
                f"{Fore.LIGHTGREEN_EX}Found: {Fore.LIGHTWHITE_EX}{self.tp_link_length}{Fore.LIGHTGREEN_EX} TP-Link networks.")

        if self.wpa_length == 0:
            print(
                Fore.LIGHTRED_EX + "No WPA-PSK-TKIP networks were found or the display of these has been deactivated in the settings.")

        elif self.wpa_length:
            print(
                f"{Fore.LIGHTBLUE_EX}Found: {Fore.LIGHTWHITE_EX}{self.wpa_length} {Fore.LIGHTBLUE_EX}WPA-PSK-TKIP networks.")

        print(
            f"{Fore.LIGHTYELLOW_EX}Found in total: {Fore.LIGHTWHITE_EX}{self.all_length}{Fore.LIGHTYELLOW_EX} WiFi networks with a potential security risk.")

        self.showing_input()

    def showing_input(self):
        self.showing = input(f"""
    {Fore.LIGHTWHITE_EX}If you want to display the networks with name and GPS coordinates, then you can enter the number for it below:

    {Fore.LIGHTRED_EX}1) WEP
    {Fore.LIGHTBLUE_EX}2) WPA
    {Fore.LIGHTMAGENTA_EX}3) o2-WLAN
    {Fore.LIGHTGREEN_EX}4) TP-Link
    {Fore.LIGHTYELLOW_EX}5) Quit 
    {Fore.LIGHTWHITE_EX}----------------=>:""")

        if self.showing == "1":
            self.show_wep()

        elif self.showing == "2":
            self.show_wpa()

        elif self.showing == "3":
            self.show_o2()

        elif self.showing == "4":
            self.show_tp_link()

        elif self.showing == "5":
            self.menu()

    def show_wep(self):

        for line in self.wep_list:
            values = line.decode().strip().split(",")
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]

            print("{:<30} {:<30} {:<30} {:<30}".format(f"{Fore.LIGHTYELLOW_EX}[Name]", f"{Fore.LIGHTCYAN_EX}[Latitude]",
                                                       f"{Fore.LIGHTGREEN_EX}[Longitude]",
                                                       f"{Fore.LIGHTWHITE_EX}[Mac] "))
            print("{:<30} {:<30} {:<30} {:<30}".format(Fore.LIGHTYELLOW_EX + name, Fore.LIGHTCYAN_EX + gps_latitude,
                                                       Fore.LIGHTGREEN_EX + gps_longitude, Fore.LIGHTWHITE_EX + mac))

        self.showing_input()

    def show_wpa(self):

        for line in self.wpa_list:
            # Help from ChatGPT in this part of code.

            values = line.decode().strip().split(",")
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]

            print("{:<30} {:<30} {:<30} {:<30}".format(f"{Fore.LIGHTYELLOW_EX}[Name]", f"{Fore.LIGHTCYAN_EX}[Latitude]",
                                                       f"{Fore.LIGHTGREEN_EX}[Longitude]",
                                                       f"{Fore.LIGHTWHITE_EX}[Mac] "))
            print("{:<30} {:<30} {:<30} {:<30}".format(Fore.LIGHTYELLOW_EX + name, Fore.LIGHTCYAN_EX + gps_latitude,
                                                       Fore.LIGHTGREEN_EX + gps_longitude, Fore.LIGHTWHITE_EX + mac))
        self.showing_input()

    def show_o2(self):

        for line in self.o2_list:
            values = line.decode().strip().split(",")
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]

            print("{:<30} {:<30} {:<30} {:<30}".format(f"{Fore.LIGHTYELLOW_EX}[Name]", f"{Fore.LIGHTCYAN_EX}[Latitude]",
                                                       f"{Fore.LIGHTGREEN_EX}[Longitude]",
                                                       f"{Fore.LIGHTWHITE_EX}[Mac] "))
            print("{:<30} {:<30} {:<30} {:<30}".format(Fore.LIGHTYELLOW_EX + name, Fore.LIGHTCYAN_EX + gps_latitude,
                                                       Fore.LIGHTGREEN_EX + gps_longitude, Fore.LIGHTWHITE_EX + mac))
        self.showing_input()

    def show_tp_link(self):
        for line in self.tp_link_list:
            values = line.decode().strip().split(",")
            mac = values[0]
            name = values[1]
            gps_latitude = values[6]
            gps_longitude = values[7]

            print("{:<30} {:<30} {:<30} {:<30}".format(f"{Fore.LIGHTYELLOW_EX}[Name]", f"{Fore.LIGHTCYAN_EX}[Latitude]",
                                                       f"{Fore.LIGHTGREEN_EX}[Longitude]",
                                                       f"{Fore.LIGHTWHITE_EX}[Mac] "))
            print("{:<30} {:<30} {:<30} {:<30}".format(Fore.LIGHTYELLOW_EX + name, Fore.LIGHTCYAN_EX + gps_latitude,
                                                       Fore.LIGHTGREEN_EX + gps_longitude, Fore.LIGHTWHITE_EX + mac))

        self.showing_input()

    def program_info(self):
        print(f"""
    {Fore.LIGHTWHITE_EX}
Wigle Extract was developed by Johannes Habel (EchterAlsFake) to
show how many W-LAN networks have a weak point to date.

The program is using the CSV files from Wigle. This
are evaluated according to the parameters of my personal experience.

The license of the program allows anyone to modify and use it.
In the case of changes, the original source MUST be specified (Creative Commons)""")

    def wpa_info(self):
        print(f"""{Fore.LIGHTRED_EX}W{Fore.LIGHTCYAN_EX}P{Fore.LIGHTYELLOW_EX}A
                                    {Fore.LIGHTWHITE_EX}
WPA is a WLAN protocol that was developed after the WEP standard. It should solve the WEP
original problems and ensure better security. However, this was not enough and WPA can 
be cracked very quickly. The algorithm is still based on that of WEP, only now 48 bits 
are used instead of 24 bits. But even that is not certain. See Michael Shutdown Exploit. 
There are only a few WPA networks and the standard today is WPA2/WPA3.""")

    def wep_info(self):
        print(f"""
            {Fore.LIGHTWHITE_EX}{Fore.LIGHTYELLOW_EX}W{Fore.LIGHTCYAN_EX}E{Fore.LIGHTMAGENTA_EX}P  {Fore.LIGHTWHITE_EX}
WEP is a WiFi protocol that was developed about 20 years ago to provide a way to secure 
a WiFi network. However, this network protocol is vulnerable to some attacks. An attacker 
can manipulate the data sent from the device to the router and, through poor encryption, 
figure out the password in less than 3 hours. WEP should no longer be used and represents 
a high security risk!""")

    def o2_info(self):
        print(f"""

        {Fore.LIGHTGREEN_EX}W{Fore.LIGHTYELLOW_EX}P{Fore.LIGHTCYAN_EX}S{Fore.LIGHTMAGENTA_EX}-{Fore.LIGHTGREEN_EX}o{Fore.LIGHTMAGENTA_EX}2{Fore.LIGHTWHITE_EX}
Most WLAN networks have a feature called WPS, which provides a quick way to exchange the 
WLAN password. However, the implementation on some WLAN routers is quite weak. Due to 
some flaws, WPS has a maximum number of 11000 possible combinations. One can hack a WLAN 
network in less than 4 hours and find out the password with the 8-digit WPS PIN. There 
is no reason to use WPS, and it should be disabled in the WLAN router settings. 
The manufacturer AVM has the Push-Button-Connect method as the standard WPS method, 
which is considered secure since the button must be pressed. However, some o2 WLAN 
routers' manufacturers did not do it as well. For WLAN routers manufactured by the 
Askey Compute Corporation, the standard WPS PIN is 12345670, which is a high-security 
risk. Therefore, the 20-digit password can be determined in 3-20 seconds!""")

    def tp_link_info(self):
        print(f"""
            {Fore.LIGHTGREEN_EX}W{Fore.LIGHTYELLOW_EX}P{Fore.LIGHTCYAN_EX}S{Fore.LIGHTMAGENTA_EX}-{Fore.LIGHTGREEN_EX}T{Fore.LIGHTMAGENTA_EX}P{Fore.LIGHTWHITE_EX}-{Fore.LIGHTGREEN_EX}L{Fore.LIGHTMAGENTA_EX}I{Fore.LIGHTWHITE_EX}N{Fore.LIGHTMAGENTA_EX}K{Fore.LIGHTWHITE_EX}

There is another attack on WPS, in which some data is collected, and the PIN is 
calculated using this data. This attack is called Pixie Dust and can find out the 
password in a few seconds. TP-Link networks are often affected by this attack, and 
all TP-Link networks have no significant protection against brute-force attacks. 
If one has some time, they can also crack the password here in a few days..""")

    def info(self):

        options = input(f"""
    {Fore.LIGHTGREEN_EX}1) Program Info
    {Fore.LIGHTRED_EX}2) WEP Info
    {Fore.LIGHTCYAN_EX}3) WPA Info
    {Fore.LIGHTMAGENTA_EX}4) o2 Info
    {Fore.GREEN}5) TP-Link Info
    {Fore.LIGHTYELLOW_EX}6) Exit
    ----------------=>:""")

        if options == "1":
            self.program_info()
            self.menu()

        elif options == "2":
            self.wep_info()
            self.menu()

        elif options == "3":
            self.wpa_info()
            self.menu()

        elif options == "4":
            self.o2_info()
            self.menu()

        elif options == "5":
            self.tp_link_info()
            self.menu()

        elif options == "6":
            self.menu()




if __name__ == "__main__":

    conf = configparser.ConfigParser()
    conf.read('config.ini')

    if conf['Language']['german'] == "true":
        while True:
            Wigle_German()

    elif conf['Language']['english'] == "true":
        while True:
            Wigle_English()
