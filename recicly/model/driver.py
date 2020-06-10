from model.person import Person


class Driver(Person):

    def __init__(self, id, name, cpf, drivers_license, profile_picture, email, password, points=0):
        super().__init__(id, name, cpf, profile_picture, email, password, points)
        self.drivers_license = drivers_license
