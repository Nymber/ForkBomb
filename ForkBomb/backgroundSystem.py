import settings

class player(self):
    def __init__(self):
        super().__init__()
        self.Data = ["Username = " + str(settings.username),"\n","password = " + str(settings.password),"\n","money = " + str(settings.money),"\n","power = " + str(settings.power),"\n","memory = " + str(settings.memory),"\n","connection = " + str(settings.connection),"\n","bitcoin = " + str(settings.bitcoin),"\n"]
        settings.msg = self.Data
        player.inject(self, self.Data)
    #update Play Data 
    
    def inject(self, data):
        sysLog = open("gameConsoleLog.txt","w")
        sysLog.writelines(str(data))
        sysLog.close()
        return str(data)#need to fix 
        
        