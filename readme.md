Документация
------------
chatBotCat - приложение для развлечения и отдыха, которое помогает отвлечься от дурных мыслей на просмотр фото котиков.

Настройка программы
-------------------

Необходимые для работы приложения модули перечислены в файле requirements.txt Установка модулей из файла requirements.txt по команде в терминале: \$ pip install -r requirements.txt

Установка программы
-------------------

Бот развернут в облаке и уже запущен. Работает по адресу сообщества: https://vk.com/club205645471
Здесь приведены исходные коды рабочих модулей. Сами по себе они не запустятся, т.к. работа основана на CallBack-сервере сообщества.

Запуск программы
----------------

Зайти в сообщество https://vk.com/club205645471 и тестировать чат-бота. 

Инструкция
----------

Управление - после первого запроса появляется подсказка от чат-бота.

Правила простые - ввод команд (ключевых слов) с клавиатуры.

Слово "помощь" (предусмотрен дубль на английском языке) - вызывает сообщение от бота с правилами сообщества.

Далее - по инструкции от бота.

Цель общения - получить немного информации о котиках. 


Дополнения
----------
Исходный код хранится на PythonAnyWhere.com.


Использованные технологии
-------------------------
Работа с чтением текстовых файлов

Работа с JSON-файлами с использованием библиотеке JSON

Работа с VK_API

Работа с .env файлом через библиотеку OS и через получение постоянных запросов от ВК.

Работа с модулями - отдельными файлами для хранения разных видов функционала для чат-бота.

Работа с запросами к стенам сообществ с целью добывания фото котиков.