import time
import webbrowser

i= 0

print("This program started on "+time.ctime())
while i <2:
    time.sleep(4)
    webbrowser.open("https://www.youtube.com/watch?v=5CxdZpGaVco")
    i += 1
