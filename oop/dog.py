class Dog:
    def __init__(self,name,dog_id):
        self.name=name
        self.dogId=dog_id
    def get_dog_details(self):
        print(f'the dog name is {self.name} and the dog id is {self.dogId}')
