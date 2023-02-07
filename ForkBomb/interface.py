import level
import threading
class startInterface:
    game = threading.Thread(target = level.run(), name='game', args=(lock),kwargs={})