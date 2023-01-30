from datetime import datetime
from database import *

def readfile():
    with open('CNAB.txt', encoding="UTF-8") as file:
        for line in file:
            x = line[1:9]
            y = line[42:48]
            
            date = datetime.strptime(x, '%Y%m%d');
            time = datetime.strptime(y, '%H%M%S');

            typeline = line[0]
            dateline = date.strftime('%Y-%m-%d')
            valueline = int(line[10:19]) / 100
            cpfline = line[19:30]
            cardline = line[30:42]
            timeline = time.strftime('%H:%M:%S')
            ownerline = line[48:62]
            storeline = line[62:81]

            dataconnect(typeline, dateline, valueline, cpfline, cardline, timeline, ownerline, storeline)