import task
import dev

class Team:
    def __init__(self, devs:dict = None, manpower_pts:int = 0, max_mp_percentage:float=0, priority_queues_intervals:dict=None ):
        if devs is not None:
            self.devs = devs
        else:
            self.devs = dict()

        self.manpower_pts = manpower_pts
        self.max_mp_percentage = max_mp_percentage
        self.max_manpower = manpower_pts*max_mp_percentage

        if priority_queues_intervals is not None:
            self.priority_queues_intervals = priority_queues_intervals
        else:
            self.priority_queues_intervals = dict()

    def add_dev(self, dev:dev.Dev):
        self.devs[dev.dev_id] = dev
        # Update the manpower points and the max manpower every time you add a Dev
        self.update_manpower_pts(dev.experience_level)
        self.update_max_manpower()
        return dev

    def remove_dev(self, dev:dev.Dev=None, name:str=None, dev_id:int=None):
        removed_dev = None
        if dev is not None:
            if dev.dev_id in self.devs.keys():
                removed_dev = self.devs.pop(dev.dev_id)
        elif name is not None:
            for k,developer in self.devs.items():
                if developer.name == name:
                    removed_dev = self.devs.pop(k)
        elif dev_id is not None:
            if dev.dev_id in self.devs.keys():
                removed_dev = self.devs.pop(dev_id)
        else:
            print("No input given to remove dev")

        if removed_dev is None:
            print("The dev info given is invalid or the dev is not in this team")
        else:
            # The removed dev's manpower points get removed from the team total
            self.update_manpower_pts(-1*removed_dev.experience_level)
            self.update_max_manpower()
        return removed_dev

    def update_manpower_global(self):
        """
        Recalculates total manpower and max_manpower by going through all devs in the team.
        """

        total_manpower = 0
        for developer in self.devs.values():
            total_manpower += developer.experience_level
        self.manpower_pts = total_manpower
        self.update_max_manpower()
        return total_manpower

    def update_manpower_pts(self, points:int):
        self.manpower_pts += points
        return self.manpower_pts

    def update_max_manpower(self):
        """
        Only use AFTER updating manpower_pts. Quantum update to max_manpower
        :return: max_manpower
        """
        self.max_manpower = self.manpower_pts * self.max_mp_percentage
        return self.max_manpower
