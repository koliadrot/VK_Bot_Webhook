from flask import Flask
from flask import request
from flask import jsonify
from flask_sslify import SSLify

from data_api_bot import *

import requests
import json
import datetime

app=Flask(__name__)
sslify=SSLify(app)

#Class with the main functions of the bot
#Класс с основными функциями бота
class BotHandler:
        def __init__(self, token):
                self.token = token
                self.api_url = "https://api.vk.com/method/"
        def send_message(self,user_id,message):
            params={"access_token":token,"v":"5.50","user_id":user_id,"message":message}
            res=requests.post(self.api_url + "messages.send", params)
        def delete_message(self,message_ids,group_id):
            params={"access_token":token,"v":"5.50","message_ids":message_ids,"group_id":group_id}
            res=requests.post(self.api_url + "messages.delete", params)
        def get_update(self,user_id,group_id):
            params={"access_token":token,"v":"5.50","user_id":user_id,"group_id":group_id,"count":20,"start_message_id":-1}
            res=requests.get(self.api_url + "messages.getHistory",params).json()
            with open('history.json','w') as file:
                json.dump(res,file,indent=2,ensure_ascii=False)
        def get_user(self,user_id):
            params={"access_token":token,"v":"5.50","user_id":user_id}
            res=requests.get(self.api_url + "users.get",params).json()
            return res["response"][0]["first_name"]

#Writes the received data in json format
#Записывает полученные данные в json формат
def write_json(data):
    with open('posts.json','w') as file:
        json.dump(data,file,indent=2,ensure_ascii=False)

bot = BotHandler(token)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method=='POST':
        now = datetime.datetime.now()
        r = request.get_json()
        if r["type"]=="message_new":
            try:
                #Loads data from a file for reading in json format
                #Загружает данные из файла для чтения в формате json
                with open('posts.json') as file:
                    data=json.load(file)
                last_user_id=r["object"]["user_id"]
                last_message_id=r["object"]["id"]
                last_group_id=r["group_id"]
                last_message=r["object"]["body"]
                penultimate_message_id=data["object"]["id"]
            except BaseException:
                write_json(r)
                with open('posts.json') as file:
                    data=json.load(file)
                last_user_id=r["object"]["user_id"]
                last_message_id=r["object"]["id"]
                last_group_id=r["group_id"]
                last_message=r["object"]["body"]
                penultimate_message_id=data["object"]["id"]
            if last_message_id>=penultimate_message_id:
                #Welcome bot depending on the time of day with a time shift
                #Приветствие бота в зависимости от времени суток со сдвигом по времени
                if last_message.lower() in greetings and 6 <= now.hour+2 < 12:
                    bot.send_message(last_user_id,f'Доброе утро, {bot.get_user(last_user_id)}!')
                elif last_message.lower() in greetings and 12 <= now.hour+2 < 17:
                    bot.send_message(last_user_id,f'Доброе день, {bot.get_user(last_user_id)}!')
                elif last_message.lower() in greetings and 17 <= now.hour+2 < 23:
                    bot.send_message(last_user_id,f'Доброе вечер, {bot.get_user(last_user_id)}!')
                elif last_message.lower() in greetings and ((now.hour+2)>=23 or (now.hour+2)<6):
                    bot.send_message(last_user_id,f'Доброго времени суток, {bot.get_user(last_user_id)}!')
                #Updates the history of the latest bot messages with the user
                #Обновляет историю последних сообщений бота с пользователем
                bot.get_update(last_user_id,last_group_id)
                write_json(r)
    #When setting up the CallBack API, the server should return a unique string. For example: "4acc2a03" Otherwise, the bot will not work properly!
    #При настройке CallBack API, сервер должен вернуть уникальную строку.Например:"4acc2a03" Иначе бот не будет работать исправно!
    return "ok"

if __name__ == '__main__':
    app.run()
