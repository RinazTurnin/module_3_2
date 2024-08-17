def send_email(message, recipient,* , sender = "university.help@gmail.com"):
  valid_domians = ['.com', '.net', '.ru']
  if not ('@' in sender and any(sender.endswith(domain) for domain in valid_domians)) or\
  not ('@' in recipient and any(recipient.endswith(domain) for domain in valid_domians)):
    print(f'Невозможно отправить письмо с {sender} на адрес {recipient}') 
  elif sender == recipient:
    print('Невозможно отправить письмо самому себе!')
  elif sender != 'university.help@gmail.com':
    print(f'НЕСТАНДАНЫЙ ОТПРАВИТЕЛЬ! Невозможно отправить письмо с {sender} на адрес {recipient}')
  else:
    print(f'Письмо успешно отправлено с адреса {sender} на адрес {recipient}!')








send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')