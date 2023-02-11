import settings

class player():
    def __init__(self, Data, *args):
        self.Data = Data
        super().__init__()
        settings.msg = self.Data
        player.inject(self, self.Data)
    #update Play Data 
    
    def inject(self, Data):
        self.Data = Data
        sysLog = open("gameConsoleLog.txt","w")
        sysLog.writelines(str(self.Data))
        sysLog.close()
        return self.Data
        
        