from src.enums.global_enums import GlobalErrorMessages
class Person:
    name = []

    def set_name(self, user_name):
        self.name.append(user_name)
        return len(self.name) - 1

    def get_name(self, user_id):
        if not isinstance(user_id, int):
            return GlobalErrorMessages.WRONG_TYPE_INT.value
        if not self.name:
            return GlobalErrorMessages.EMPTY_USERS_ARRAY.value
        else:
            if user_id >= len(self.name):
                return 'There is no such user'
            else:
                return self.name[user_id]




