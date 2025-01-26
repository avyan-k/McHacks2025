import task
import devs

class Team:
    def __init__(self, devs:dict = None, manpower_pts:int = 0, max_manpower:int = 0 ):
        self.devs = devs
        self.manpower_pts = manpower_pts
        self.max_manpower = max_manpower

    def add_dev(self, dev:devs.Devs):
        self.devs[dev.dev_id] = dev

    def remove_dev(self, dev:devs.Devs=None, name:str=None, dev_id:int=None):
        removed_dev = None
        if dev is not None:
            removed_dev = self.devs.pop(dev.dev_id)
        elif name is not None:
            for k,developer in self.devs.items():
                if developer.name == name:
                    removed_dev = self.devs.pop(k)
        elif dev_id is not None:
            removed_dev = self.devs.pop(dev_id)
        return removed_dev