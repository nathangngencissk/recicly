from model.person import Person


class User(Person):

    def __init__(self, id, name, cpf, profile_picture, email, password, points=0, admin=False):
        super().__init__(id, name, cpf, profile_picture, email, password, points)
        self.admin = admin
