import tkinter
import time

class WorldTimePage(tkinter.Tk):
    def __init__(self, parent):
        tkinter.Tk.__init__(self, parent)

        self.clockListName = []
        self.clockListTime = []

        self.parent = parent
        self.initialize()

    def clock(self,live_T = time.strftime("%H:%M:%S")):
        live_T = time.strftime("%H:%M:%S")
        self.clockListTime[0].config(text=live_T)
        self.clockListTime[0].after(1,self.clock)
        

    def initialize(self):
        # set window env
        self.grid()
        self.grid_columnconfigure((0, 1), weight=1)
        self.resizable(False, False)
        self.geometry("300x320+800+140")
        self.title("세계시간")

        

        time_list = [
            {
                "name": "서울",
                #"time": "2019-01-01 00:00:00"
                "time" :time.strftime("%H:%M:%S")
            },
            {
                "name": "서울2",
                #"time": "2019-01-01 00:00:00"
                "time" :time.strftime("%H:%M:%S")
            },
        ]
        
        self.build(time_list)

    # TODO: 동적으로 시간 표시

    def build(self, timelist):
        for i, data in enumerate(timelist):
            a=tkinter.Label(self, text=data["name"])
            a.grid(column=0, row=i, sticky="ew")
            b=tkinter.Label(self, text=data["time"])
            b.grid(column=1, row=i, sticky="ew")
            self.clockListName.append(a)
            self.clockListTime.append(b)
        self.clock()
