from colorama import *

def vulnerability_search():
    with open("demo.csv", 'r') as csv_file:
        print(Fore.LIGHTGREEN_EX + "[+] " + Fore.LIGHTCYAN_EX + "Daten werden ausgewertet....")
        for line in csv_file:
            values = line.strip().split(",")
            mac = values[0]
            name = values[1]
            gps = values[6]

            print(f"""
MAC: {mac}
NAME: {name}
GPS: {gps}

""")

vulnerability_search()