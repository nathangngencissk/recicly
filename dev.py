from datetime import date


from model.user import User
from model.driver import Driver
from handlers.user.process_request import History, Request, State

pedro = User('Pedro', '1232144')
print(pedro.name)

matheus = User('Matheus', '123214334')
print(matheus.name)

jonas = Driver('Jonas', '12333', '1233312')
print(jonas.drivers_license)

history = History()

request = Request(date=date.today(), user=pedro, request_type="NEW")

request.advance()

history.add_state(request.save_state())

request.advance()

request.user = matheus

history.add_state(request.save_state())

request.advance()

history.add_state(request.save_state())

print(request.request_type)
print(request.user)

request.restore_state(history.get_state(0))

print(request.request_type)
print(request.user)
