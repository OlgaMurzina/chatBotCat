# Породы кошек

import command_system


def morf():
    # Получаем список пород
    message = open('/home/school10/mysite/commands/morff.txt').read()
    return message, ''


cat_command = command_system.Command()

cat_command.keys = ['порода', 'масть', 'вид']
cat_command.description = 'Пришлю список пород по запросу'
cat_command.process = morf
