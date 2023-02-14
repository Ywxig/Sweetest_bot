# Sweetest_bot

___Sweetest_bot___ - This is a bot for creating HTML pages in telegram. The bot was created on the Aiogram framework. It also uses my own python/c++ serialization library.

Below are all the features available for use:

___/reg___ - This command is designed to register a user. For successful registration, you need to enter this command in the chat. After that, your profile will be created in the Users/ directory.

___/td___ - This command will add a line to the HTML for the table. It has two arguments NUM - the line number. TEXT – row content of the table, the character “, ” is used to delimit

___/div___ - данная команда добавит в HTML блок div, имеет два аргумента NUM – номер дня, где 1-понидельник, 2-вторник, 3-среда, и т.д. TEXT – контент блока, для разграничения используется символ «,»

___/ping___ – проверит ваш id в системе

___/finish___  - данная команда соберёт вашу страничку и отправит в виде файла. Имеет один аргумент имя стиля для оформления.

___/add___ - this command will add to the HTML this command will add the tag you specify and the content of the tag you specify to 
the document.

___/start___ - starts the bot

## Command syntax:

` /td <line number> <content> `

` /div <Day number> <list of items on that day> `

` /add <tag> <style> <text enclosed in tag> `

## List of bot styles
