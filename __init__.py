from mycroft import MycroftSkill, intent_file_handler


class Skilltest(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skilltest.intent')
    def handle_skilltest(self, message):
        self.speak_dialog('skilltest')


def create_skill():
    return Skilltest()

