from model.person import Person


class Driver(Person):

    def __init__(self, name, cpf, drivers_license):
        super().__init__(name, cpf)
        self.drivers_license = drivers_license
