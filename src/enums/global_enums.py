from enum import Enum

class GlobalErrorMessages(Enum):
    WRONG_STATUS_CODE = 'Получили неверный статус код'
    WRONG_ELEMENT_COUNT = 'Количество элементов не соответствует ожидаемому'
    WRONG_EMAIL = 'Wrong email'
    WRONG_TYPE_INT = 'Wrong type, expected int'
    EMPTY_USERS_ARRAY = 'Array of users is empty'