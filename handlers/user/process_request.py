class Request:
    def __init__(self, date, user, request_type):
        self.__date = date
        self.__user = user
        self.__request_type = request_type

    @property
    def date(self):
        return self.__date

    @date.setter
    def date(self, date):
        self.__date = date

    @property
    def user(self):
        return self.__user

    @user.setter
    def user(self, user):
        self.__user = user

    @property
    def request_type(self):
        return self.__request_type

    @request_type.setter
    def request_type(self, request_type):
        self.__request_type = request_type

    def advance(self):
        if self.__request_type == "NEW":
            self.__request_type = "ONGOING"
        elif self.__request_type == "ONGOING":
            self.__request_type = "ACCEPTED"
        elif self.__request_type == "ACCEPTED":
            self.__request_type = "CONCLUDED"

    def save_state(self):
        return State(
            Request(
                date=self.__date, user=self.__user, request_type=self.__request_type
            )
        )

    def restore_state(self, state):
        self.__user = state.request.user
        self.__date = state.request.date
        self.__request_type = state.request.request_type


class State:
    def __init__(self, request):
        self.__request = request

    @property
    def request(self):
        return self.__request


class History:
    def __init__(self):
        self.__saved_states = list()

    def get_state(self, index):
        return self.__saved_states[index]

    def add_state(self, state):
        self.__saved_states.append(state)
