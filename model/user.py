from model.person import Person


class User(Person):

    def __init__(self, name, cpf):
        super().__init__(name, cpf)
