import vk_api
from vk_bot import VkBot
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})


# API-ключ созданный ранее
token = "6a9c267cd469388709a9e9acaddbe0aa81a0abbf12239b3e597a31729ffbddb9c88e80a443554c918b8f7"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:

        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:

            # Сообщение от пользователя
            request = event.text

            # Каменная логика ответа
            if request == "привет":
                write_msg(event.user_id, "Хай")
            elif request == "пока":
                write_msg(event.user_id, "Пока((")
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

# API-ключ созданный ранее
token = "6a9c267cd469388709a9e9acaddbe0aa81a0abbf12239b3e597a31729ffbddb9c88e80a443554c918b8f7"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk)
#Войдем в основной цикл:

# Основной цикл
for event in longpoll.listen():
    class VkBot:

        def __init__(self, user_id):
            print("Создан объект бота!")
            self._USER_ID = user_id
            self._USERNAME = self._get_user_name_from_vk_id(user_id)

            self._COMMANDS = ["ПРИВЕТ", "ПОГОДА", "ВРЕМЯ", "ПОКА"]

        def _get_user_name_from_vk_id(self, user_id):
            request = requests.get("https://vk.com/id" + str(user_id))
            bs = bs4.BeautifulSoup(request.text, "html.parser")

            user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])

            return user_name.split()[0]


# Получение времени:
def _get_time(self):
    request = requests.get("https://my-calend.ru/date-and-time-today")
    b = bs4.BeautifulSoup(request.text, "html.parser")
    return self._clean_all_tag_from_str(str(b.select(".page")[0].findAll("h2")[1])).split()[1]


# Получение погоды
def _get_weather(city: str = "санкт-петербург") -> list:
    request = requests.get("https://sinoptik.com.ru/погода-" + city)
    b = bs4.BeautifulSoup(request.text, "html.parser")

    p3 = b.select('.temperature .p3')
    weather1 = p3[0].getText()
    p4 = b.select('.temperature .p4')
    weather2 = p4[0].getText()
    p5 = b.select('.temperature .p5')
    weather3 = p5[0].getText()
    p6 = b.select('.temperature .p6')
    weather4 = p6[0].getText()
    result = ''
    result = result + ('Утром :' + weather1 + ' ' + weather2) + '\n'
    result = result + ('Днём :' + weather3 + ' ' + weather4) + '\n'
    temp = b.select('.rSide .description')
    weather = temp[0].getText()
    result = result + weather.strip()

    return result


# Метод для очистки от ненужных тэгов

@staticmethod
def _clean_all_tag_from_str(string_line):
    """
    Очистка строки stringLine от тэгов и их содержимых
    :param string_line: Очищаемая строка
    :return: очищенная строка
    """
    result = ""
    not_skip = True
    for i in list(string_line):
        if not_skip:
            if i == "<":
                not_skip = False
            else:
                result += i
        else:
            if i == ">":
                not_skip = True

    return result


def new_message(self, message):
    # Привет
    if message.upper() == self._COMMANDS[0]:
        return f"Привет-привет, {self._USERNAME}!"

    # Погода
    elif message.upper() == self._COMMANDS[1]:
        return self._get_weather()

    # Время
    elif message.upper() == self._COMMANDS[2]:
        return self._get_time()

    # Пока
    elif message.upper() == self._COMMANDS[3]:
        return f"Пока-пока, {self._USERNAME}!"

    else:
        return "Не понимаю о чем вы..."


print("Server started")
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            print('New message:')
            print(f'For me by: {event.user_id}', end='')

            bot = VkBot(event.user_id)
            write_msg(event.user_id, bot.new_message(event.text))

            print('Text: ', event.text)