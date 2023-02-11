import settings

class player():
    def __init__(self, Data, *args):
        self.Data = [settings.username, settings.password, settings.money, settings.power, settings.power, settings.memory, settings.connection, settings.power, settings.bitcoin]
        super().__init__()
        player.inject(self, self.Data)
    #update Play Data 
    
    def inject(self, Data):
        self.Data = Data
        sysLog = open("gameConsoleLog.txt","w")
        sysLog.writelines(str(self.Data))
        sysLog.close()
        return self.Data
        
        