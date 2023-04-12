from parsing import *
registred_states = {}

develop_url="https://habr.com/ru/flows/develop/"#разработка
admin_url="https://habr.com/ru/flows/admin/"#администрирование
design_url="https://habr.com/ru/flows/design/"#дизайн
management_url="https://habr.com/ru/flows/management/"#менеджмент
marketing_url="https://habr.com/ru/flows/marketing/"#маркетинг
popsci_url="https://habr.com/ru/flows/popsci/"#научпоп

def get_state(state_id):
    return registred_states[state_id]

def get_root_state():
    global root_state_id
    return registred_states[root_state_id]


class Transition:

    def __init__(self, to_id, synonims):
        self.to_id = to_id
        self.synonims = synonims

    def must_go(self, user_text):
        return user_text in self.synonims

    def get_dest_id(self):
        return self.to_id

class State:

    def __init__(self, id, text, transitions, default_transition, is_end=False):
        self.id = id
        self.text = text
        self.transitions = transitions
        self.default_transition = default_transition
        self.is_end=is_end

    def get_next_state(self, user_input):
        for transition in self.transitions:
            if transition.must_go(user_input):
                return get_state(transition.to_id)

        return get_state(self.default_transition)

    def register(self):
        global registred_states
        registred_states[self.id] = self

    def get_text(self):
        return self.text

    def get_id(self):
        return self.id

    def is_end_state(self):
        return self.is_end

def init():
    global root_state_id
    global admin_url
    State("100", "Привет! Хотите услышать самые интересные и свежие новости из мира технологий?", [Transition("900",["нет","Нет"])], "101").register()

    State("101", "Что вам по душе ? Разработка, администрирование, дизайн, менеджмент, маркетинг, а может научпоп ? ", [
        Transition("900",["нет","Нет", "Не хочу", "не хочу", "Неа","неа"]),
        Transition("200", ["1","Разработка","разработка","первое","Первое"]),
        Transition("300", ["2","Администрирование","администрирование","Второе","второе"]),
        Transition("400", ["3","Дизайн","дизайн","Третье","третье"]),
        Transition("500", ["4","Менеджмент","менеджмент","Четвертое","Четвёртое","четвертое","четвёртое"]),
        Transition("600", ["5","Маркетинг","маркетинг","Пятое","пятое", "Предпоследнее", "предпоследнее"]),
        Transition("700", ["6","последнее","Научпоп","научпоп","Последнее"])
    ], None).register()

    State("200", f"Вот что я могу предложить 👾 : {spisok(develop_url)} Назовите номер выбранной вами новости",
          [
              Transition("210", ["1", "первое", "Первое"]),
              Transition("211", ["2", "Второе", "второе"]),
              Transition("212", ["3", "Третье", "третье"]),
              Transition("213", ["4", "Четвертое", "Четвёртое", "четвертое", "четвёртое"]),
              Transition("214", ["5", "Пятое", "пятое", "Последнее", "последнее"])
          ], None).register()

    State("210", f"Вот что я могу предложить 👨‍🚀 : {tekst(spisok(admin_url))} Назовите номер выбранной вами новости",
          [Transition("900", [])], "900").register()

    State("300", f"Вот что я могу предложить 👨‍🚀 : {spisok(admin_url)} Назовите номер выбранной вами новости",
          [Transition("900", [])], "900").register()

    State("400", f"Вот что я могу предложить 🎨 : {spisok(design_url)} Назовите номер выбранной вами новости",
          [Transition("900", [])], "900").register()

    State("500", f"Вот что я могу предложить 👔 : {spisok(management_url)} Назовите номер выбранной вами новости",
          [Transition("900", [])], "900").register()

    State("600", f"Вот что я могу предложить 🛒 : {spisok(marketing_url)} Назовите номер выбранной вами новости",
          [Transition("900", [])], "900").register()

    State("700", f"Вот что я могу предложить 👓 : {spisok(popsci_url)} Назовите номер выбранной вами новости",
          [Transition("900", [])], "900").register()


    State("900", "Пока, удачи!", [], None, True).register()

    root_state_id="100"

init()


    #Храм технологий