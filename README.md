EN:

VK Bot with Webhook

The main task of this bot, to respond to user requests, which can be easily added.
See repository - https://github.com/koliadrot/Telegram_Bot_Webhook

This bot works as follows: A bot accepts a request from a VK server and the bot processes the data.
sent to the server.

This method is effective compared to the reverse method of Webhook (the bot itself requests (spam) vk server,
and vk the server is responsible for it), since the delay between the bot and the server almost disappears and disappears
satisfactory results that could pass between requests.

Useful notes to get started:
1. Do not forget to insert your VK token in the data_api_bot file - the variable "token"

2. The bot itself was placed on the site of the service - https://www.pythonanywhere.com
   The cost of the service is free, you only need to renew it every 3 months, it is also free!

Details about the methods of VK bot look at - https://vk.com/dev/methods

Bot Setup Guide - https://vk.com/dev/bots_docs

Attention!!!

There are two types of VK bots:
1. Bot with user access key
2. Bot with community access key
   To work with the Messages method, you need a bot with a community key !!!
   The bot with the community key cannot work with the Messages method !!!

RU: 

VK Бот с Webhook 

Главная задача этого бота, отвечать на запросы пользователей,которые могут быть легко добавлены.
Смотри хранилище(репозиторий) - https://github.com/koliadrot/Telegram_Bot_Webhook 

Данный бот работает по следующему принципу: Бот принимает запрос от VK сервера и бот обрабатывая дан- 
ные, отправляет данные серверу. 

Данный метод эффективен по сравнению с методом обратному Webhook(Бот сам запрашивает(спамит) vk сервер, 
а vk сервер ему отвечает), так как задержка между ботом и сервером практически исчезает и пропадают не- 
удовлетворительные результаты, которые могли проходить между запросами. 

Полезные заметки для начала работы: 
1. Не забудьте вставить ваш токен VK в файле data_api_bot - переменная "token"

2. Сам бот размещался на сайте сервиса - https://www.pythonanywhere.com
   Стоимость услуги бесплатная, нужно только каждые 3 месяца продливать, это тоже бесплатно!

Подробно о методах VK бота смотреть на - https://vk.com/dev/methods

Гайд по настройке бота - https://vk.com/dev/bots_docs

Важно!!!
Есть два типа ботов VK:
1. Бот с ключом доступа пользователя
2. Бот с ключом доступа сообщества
   Чтобы работать с методом Messages, нужен бот с ключом сообщества!!!
   Бот с ключом сообщества, работать с методом Messages не может!!!

