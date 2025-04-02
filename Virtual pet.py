import sys;
import pygame as py;

py.init()

screen = py.display.set_mode((800, 600))
py.display.set_caption("Virtual Pet")

while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    py.display.update()
    

    