import yookassa as yk
from yookassa import Configuration, Payment
import os

Configuration.account_id = "123124"
Configuration.secret_key = os.getenv("SECRET_KEY")

try:
    payment = Payment.create({
        "amount": {
            "value": "100.00",
            "currency": "RUB"
        },
        "confirmation":{
            "type": "redirect",
            "return_url": "https://t.me/IsmailAiogramthebest_bot"
        },
        "description": "Оплата подписки"
    })
    payment_url = payment.confirmation.confirmation_url
    print(payment_url)
except Exception as ex:
    print("Ошибка",ex)







