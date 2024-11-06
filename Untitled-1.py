import os
from dotenv import dotenv_values
import smtplib
from dotenv import load_dotenv

load_dotenv('pass.env')
login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)

name = '%friend_name%'
my_name = '%my_name%'
website = 'https: // dvmn.org/referrals/U95Ga4KyIUWGC6AGQhDi6rA3a6Eof9yQrVDymOQL/'

sender = 'devmanorg@yandex.ru'
recipient = 'lion21.85@yandex.ru'

message = f'''\
From: {sender}
To: {recipient}
Subject: Важно!
Content-Type: text/plain; charset="UTF-8";\n\n


Привет, %friend_name% ! %my_name% приглашает тебя на сайт %website% !

%website% — это новая версия онлайн-курса по программированию.\n Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на %website%?\n → Попрактикуешься на реальных кейсах.\n Задачи от тимлидов со стажем от 10 лет в программировании.\n→ Будешь учиться без стресса и бессонных ночей.\n Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.\n→ Подготовишь крепкое резюме.\n Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.

Регистрируйся → %website% \n На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

message = message.replace(
    "%website%", "https: // dvmn.org/referrals/U95Ga4KyIUWGC6AGQhDi6rA3a6Eof9yQrVDymOQL/")
message = message.replace(name, "Алексей")
message = message.replace(my_name, "Татьяна")

message = message.encode("UTF-8")

server.sendmail(sender, recipient, message)
server.quit()
