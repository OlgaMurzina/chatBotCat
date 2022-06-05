# фото или картинка с котиком случайная из интернета


import command_system
import settings
import vkapi


def cat():
    # Получаем случайную картинку из паблика
    attachment = vkapi.get_random_wall_picture(-32015300, settings.access_token)
    message = 'Вот чудо-котик :)\nВ следующий раз покажу нового котика.'
    return message, attachment


cat_command = command_system.Command()

cat_command.keys = ['кот', 'котик', 'cat']
cat_command.description = 'Пришлю фотографию котика'
cat_command.process = cat
