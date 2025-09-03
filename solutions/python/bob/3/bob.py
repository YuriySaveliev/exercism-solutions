from enum import Enum

class Answer(Enum):
    FINE = 'Fine. Be that way!'
    SURE = 'Sure.'
    WHOA = 'Whoa, chill out!'
    CALM = 'Calm down, I know what I\'m doing!'
    WHATEVER = 'Whatever.'


def response(hey_bob: str) -> str:
    hey_bob_norm = hey_bob.strip()
    if len(hey_bob_norm) == 0:
        return Answer.FINE.value
    elif hey_bob_norm[-1] == '?':
        if hey_bob.isupper():
            return Answer.CALM.value
        else:
            return Answer.SURE.value
    elif hey_bob.isupper():
        return Answer.WHOA.value
    return Answer.WHATEVER.value
