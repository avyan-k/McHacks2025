import task

class Devs:
    def __init__(self, id:int, name:str,  experience_level:int):
        self.experience_level = experience_level
        self.current_task = None
        self.attributed_task = set()

