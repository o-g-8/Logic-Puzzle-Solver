class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self,text):
        for observer in self._observers:
            observer.update(text)

class Observer:
    def update(self, text):
        pass 
