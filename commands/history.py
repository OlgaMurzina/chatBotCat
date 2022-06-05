# история кошек

import command_system


def history():
    message = open('/home/school10/mysite/commands/his.txt').read()
    return message, ''


hello_command = command_system.Command()

hello_command.keys = ['история', 'history']
hello_command.description = 'Расскажу краткую историю кошек'
hello_command.process = history
