import pytest, string, random

from OZON.persons import Person
from src.enums.global_enums import GlobalErrorMessages

#Заполняем массив рандомных "имён"
def get_rnd_names(count):
    letters = string.ascii_lowercase
    names = []
    for _ in range(count):
        names.append(''.join(random.choice(letters) for _ in range(5)))
    return names
testnames =get_rnd_names(10)

#Проверяем без тестовых данных
def test_empty_check():
    assert Person.get_name(Person, 0) == GlobalErrorMessages.EMPTY_USERS_ARRAY.value



#Name наполняется с различными входными, индекс корректно увеличивается
@pytest.mark.parametrize('val, expected',[
    (testnames[0], 0),
    (None, 1),
    (None, 2),
    (1, 3),
    (-1, 4),
    (0, 5),
    (testnames[6], 6)

])
def test_set_name(val, expected):
    assert Person.set_name(Person,val) == expected



@pytest.mark.parametrize('val, expected',[
    (0, testnames[0]), #вернулось корректное по индексу
    (1, None), #вернулся None
    (50, 'There is no such user'), #при превышение длины возвращается ожидаемый exception
    ('asd', GlobalErrorMessages.WRONG_TYPE_INT.value), #Строка
    ('5', GlobalErrorMessages.WRONG_TYPE_INT.value), #Число как строка
    (2.5, GlobalErrorMessages.WRONG_TYPE_INT.value), #Число с плавающей точкой
    (-1, testnames[6]) #отрицательный индекс
])
def test_get_name(val, expected):
    assert Person.get_name(Person, val) == expected

#Проверка очистки массива
def test_get_name_clear(clear_names):
    assert Person.get_name(Person,0)==GlobalErrorMessages.EMPTY_USERS_ARRAY.value
#print(Person.get_name(Person,-5))