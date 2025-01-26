import task

class Devs:
    def __init__(self, dev_id:int, name:str,  experience_level:int):
        self.dev_id = dev_id
        self.experience_level = experience_level
        self.current_task = None
        self.attributed_task = set()

