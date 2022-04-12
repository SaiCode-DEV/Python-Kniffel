from os import system, name
from time import sleep

loading01 = [" _ ",
             "| |",
             "| '",
             "| .",
             "|_|"]

loading02 = [" _  _",
             "| |/ ",
             "| ' /",
             "| . \\",
             "|_|\_"]

loading03 = [" _  __ ",
             "| |/ /_ ",
             "| ' /| '",
             "| . \| |",
             "|_|\_\_|"]

loading04 = [" _  __    ",
             "| |/ /_ __",
             "| ' /| '_ ",
             "| . \| | |",
             "|_|\_\_| |"]

loading05 = [" _  __     ",
             "| |/ /_ __  ",
             "| ' /| '_ \\",
             "| . \| | | |",
             "|_|\_\_| |_|"]

loading06 = [" _  __      _ ",
             "| |/ /_ __ (_)",
             "| ' /| '_ \| |",
             "| . \| | | | |",
             "|_|\_\_| |_|_|"]

loading07 = [" _  __      _  _",
             "| |/ /_ __ (_)/ ",
             "| ' /| '_ \| | |",
             "| . \| | | | |  ",
             "|_|\_\_| |_|_|_|"]

loading08 = [" _  __      _  __",
             "| |/ /_ __ (_)/ _",
             "| ' /| '_ \| | |_",
             "| . \| | | | |  _",
             "|_|\_\_| |_|_|_| "]

loading09 = [" _  __      _  __  _",
             "| |/ /_ __ (_)/ _|/ ",
             "| ' /| '_ \| | |_| |",
             "| . \| | | | |  _|  ",
             "|_|\_\_| |_|_|_| |_|"]

loading10 = [" _  __      _  __  __ ",
             "| |/ /_ __ (_)/ _|/ _|",
             "| ' /| '_ \| | |_| |_ ",
             "| . \| | | | |  _|  _|",
             "|_|\_\_| |_|_|_| |_|  "]

loading11 = [" _  __      _  __  __   ",
             "| |/ /_ __ (_)/ _|/ _| _",
             "| ' /| '_ \| | |_| |_ / ",
             "| . \| | | | |  _|  _|  ",
             "|_|\_\_| |_|_|_| |_|  \_"]

loading12 = [" _  __      _  __  __    ",
             "| |/ /_ __ (_)/ _|/ _| __",
             "| ' /| '_ \| | |_| |_ / _",
             "| . \| | | | |  _|  _|  _",
             "|_|\_\_| |_|_|_| |_|  \__"]

loading13 = [" _  __      _  __  __     ",
             "| |/ /_ __ (_)/ _|/ _| ___",
             "| ' /| '_ \| | |_| |_ / _ \\",
             "| . \| | | | |  _|  _|  __/",
             "|_|\_\_| |_|_|_| |_|  \___|"]

loading14 = [" _  __      _  __  __      _  ",
             "| |/ /_ __ (_)/ _|/ _| ___| | ",
             "| ' /| '_ \| | |_| |_ / _ \ | ",
             "| . \| | | | |  _|  _|  __/ | ",
             "|_|\_\_| |_|_|_| |_|  \___|_| "]

loadingAnyKey = [" _  __      _  __  __      _  ",
                 "| |/ /_ __ (_)/ _|/ _| ___| | ",
                 "| ' /| '_ \| | |_| |_ / _ \ | ",
                 "| . \| | | | |  _|  _|  __/ | ",
                 "|_|\_\_| |_|_|_| |_|  \___|_| ",
                 "",
                 "",
                 "PRESS ANY KEY TO CONTINUE"]

loading = [loading01, loading02, loading03, loading04, loading05, loading06, loading07, loading08, loading09, loading10, loading11, loading12, loading13,
           loading14, loading14, loading14, loading14, loading14, loading14, loading14, loading14, loading14, loading14,
           loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey,
           loading14, loading14, loading14, loading14, loading14, loading14, loading14,
           loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey,
           loading14, loading14, loading14, loading14, loading14, loading14, loading14,
           loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey,
           loading14, loading14, loading14, loading14, loading14, loading14, loading14,
           loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey, loadingAnyKey]


def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")


while True:
    for teil_loaded in loading:
        clear()
        for zeile in teil_loaded:
            print(zeile)
        sleep(0.15)
