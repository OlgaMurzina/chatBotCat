# уход за котиками

import command_system


def animal_care():
    message = open('/home/school10/mysite/commands/care.txt').read()
    return message, ''


hello_command = command_system.Command()

hello_command.keys = ['уход', 'содержание']
hello_command.description = 'Расскажу об уходе за кошками'
hello_command.process = animal_care
