import settings

class player():
    #update Play Data 
    def inject():
        sysLog = open("gameConsoleLog.txt","w")
        sysLog.writelines(str(settings.Data))