import os
import telebot
import datetime
from datetime import datetime, date, time


TOKEN = '1646816781:AAG2vaigabICfQKUMm76MPfXubd1oY9zkUc'
AdminId = 507799769
bot = telebot.TeleBot(TOKEN)
bot.send_message(AdminId, 'start')
print('start')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    current_date = datetime.now()
    # _______________________________________________________________________________________
    if datetime.now().isocalendar()[1] % 2 == 0:
        weekend = False  # чисельник - тру, знаменик - фалсе
    else:
        weekend = True
    # _______________________________________________________________________________________
    if message.text == '!?!':
        print(message)
        bot.send_message(message.chat.id, "все ок")
        print(current_date.time())
    # _______________________________________________________________________________________
    if message.text == 'stop':
        if message.from_user.id == AdminId:
            bot.send_message(message.chat.id, '(')
            os.abort()
        else:
            bot.send_message(message.chat.id, 'неа')
    # _______________________________________________________________________________________
    if message.text == '/help':
        bot.send_message(message.chat.id,
                         '_Пара_ або _пара_ - дізнатися яка зараз пара (силку на пару бот починає видавати за 5хв до початку пари)\n'
                         '_Розклад_ або _розклад_ - має багато варіацій:\n'
                         '\t\t\tпросто _розклад_ - дізнатися сьогоднішній розклад\n'
                         '\t\t\t_розклад понеділок_ - дізнатися розклад в понеділок цього тижня *(пятницю писати без апострофа!)*\n'
                         '\t\t\t_розклад понеділок наступний_ - дізнатися розклад в понеділок наступного тижня *(пятницю писати без апострофа!)*',
                         parse_mode='Markdown')
    # _______________________________________________________________________________________
    def schedle(weekend, day):
        if weekend:
            if day == 0:
                bot.send_message(message.chat.id,
                                 '1 пара:\n_8:30 − 10:05_\n*Комп`ютерні технології та програмування*\nДілай І.В.\n_Лекція_\n\n'
                                 '2 пара:\n_10:20 − 11:55_\n*Вища математика*\nСлюсарчук О.З.\n_Лекція_\n\n'
                                 '3 пара:\n_12:10 − 13:45_\n*Основи автоматики та автоматизації*\nСтасюк І.Д.\n_Лекція_',
                                 parse_mode='Markdown')
            elif day == 1:
                bot.send_message(message.chat.id,
                                 '1 пара:\n_8:30 − 10:05_\n*Фізичне виховання*\nКубрак Я.Д., хлопці/Незгода С.П., дівчата\n_Практична_\n\n'
                                 '2 пара:\n_10:20 − 11:55_\n*ВІКНО*\n\n'
                                 '3 пара:\n_12:10 − 13:45_\n*Вища математика*\nОлексів І.Я.\n_Практична_\n\n'
                                 '4 пара:\n_14:15 − 15:50_\n*Історія державності та культури України*\nСтасюк І.М.\nПрактична\n\n'
                                 '5 пара:\n_16:00 − 17:35_\n*Комп`ютерні технології та програмування*\n2 підгрупа\nДілай І.В.\n_Лабораторна_',
                                 parse_mode='Markdown')
            elif day == 2:
                bot.send_message(message.chat.id,
                                 '1 пара:\n_8:30 − 10:05_\n*Комп`ютерні технології та програмування*\n2 підгрупа\nДілай І.В.\n_Лабораторна_\n\n'
                                 '2 пара:\n_10:20 − 11:55_\n*Комп`ютерні технології та програмування*\n1 підгрупа\nДілай І.В.\n_Лабораторна_\n\n'
                                 '3 пара:\n_12:10 − 13:45_\n*Іноземна мова за професійним спрямуванням*\nКушка Б.Г./Гасько О.Л.\n_Практична_\n\n'
                                 '4 пара:\n_14:15 − 15:50_\n*Комп`ютерні технології та програмування*\nДілай І.В.\nПрактична',
                                 parse_mode='Markdown')
            elif day == 3:
                bot.send_message(message.chat.id, '3 пара:\n_12:10 − 13:45_\n*Фізика*\nРоманюк М.М.\n_Практична_\n\n'
                                                  '4 пара:\n_14:15 − 15:50_\n*Комп`ютерні технології та програмування*\n1 підгрупа\nДілай І.В.\n_Лабораторна_\n\n'
                                                  '5 пара:\n_16:00 − 17:35_\n*Комп`ютерні технології та програмування*\n2 підгрупа\nДілай І.В.\n_Лабораторна_',
                                 parse_mode='Markdown')
            elif day == 4:
                bot.send_message(message.chat.id,
                                 '1 пара:\n_8:30 − 10:05_\n*Вища математика*\nСлюсарчук О.З.\n_Лекція_\n\n'
                                 '2 пара:\n_10:20 − 11:55_\n*Комп`ютерні технології та програмування*\nДілай І.В.\n_Лекція_\n\n'
                                 '3 пара:\n_12:10 − 13:45_\n*Фізика*\nРоманюк М.М.\n_Лекція_\n\n'
                                 '4 пара:\n_14:15 − 15:50_\n*Основи автоматики та автоматизації*\nСтасюк І.Д.\nЛекція',
                                 parse_mode='Markdown')
        else:
            if day == 0:
                bot.send_message(message.chat.id,
                                 '1 пара:\n_8:30 − 10:05_\n*Комп`ютерні технології та програмування*\nДілай І.В.\n_Лекція_\n\n'
                                 '2 пара:\n_10:20 − 11:55_\n*Вища математика*\nСлюсарчук О.З.\n_Лекція_\n\n'
                                 '3 пара:\n_12:10 − 13:45_\n*Основи автоматики та автоматизації*\nСтасюк І.Д.\n_Лекція_',
                                 parse_mode='Markdown')
            elif day == 1:
                bot.send_message(message.chat.id,
                                 '1 пара:\n_8:30 − 10:05_\n*Фізичне виховання*\nКубрак Я.Д., хлопці/Незгода С.П., дівчата\n_Практична_\n\n'
                                 '2 пара:\n_10:20 − 11:55_\n*ВІКНО*\n\n'
                                 '3 пара:\n_12:10 − 13:45_\n*Вища математика*\nОлексів І.Я.\n_Практична_\n\n'
                                 '4 пара:\n_14:15 − 15:50_\n*Основи автоматики та автоматизації*\n2 підгрупа\nНиколин Г.А.\nЛабораторна',
                                 parse_mode='Markdown')
            elif day == 2:
                bot.send_message(message.chat.id,
                                 '1 пара:\n_8:30 − 10:05_\n*Основи автоматики та автоматизації*\n1 підгрупа\nНиколин Г.А.\n_Лабораторна_\n\n'
                                 '2 пара:\n_10:20 − 11:55_\n*Комп`ютерні технології та програмування*\n1 підгрупа\nДілай І.В.\n_Лабораторна_\n\n'
                                 '3 пара:\n_12:10 − 13:45_\n*Іноземна мова за професійним спрямуванням*\nКушка Б.Г./Гасько О.Л.\n_Практична_\n\n'
                                 '4 пара:\n_14:15 − 15:50_\n*Історія державності та культури України*\nСтасюк І.М.\nПрактична',
                                 parse_mode='Markdown')
            elif day == 3:
                bot.send_message(message.chat.id,
                                 '3 пара:\n_12:10 − 13:45_\n*Фізика*\nРоманюк М.М./Семків І.В.\n_Лабораторна_\n\n'
                                 '4 пара:\n_14:15 − 15:50_\n*Комп`ютерні технології та програмування*\n1 підгрупа\nДілай І.В.\n_Лабораторна_\n\n'
                                 '5 пара:\n_16:00 − 17:35_\n*Комп`ютерні технології та програмування*\n2 підгрупа\nДілай І.В.\n_Лабораторна_',
                                 parse_mode='Markdown')
            elif day == 4:
                bot.send_message(message.chat.id,
                                 '1 пара:\n_8:30 − 10:05_\n*Історія державності та культури України*\nБарановська Н.М.\n_Лекція_\n\n'
                                 '2 пара:\n_10:20 − 11:55_\n*Комп`ютерні технології та програмування*\nДілай І.В.\n_Лекція_\n\n'
                                 '3 пара:\n_12:10 − 13:45_\n*Фізика*\nРоманюк М.М.\n_Лекція_', parse_mode='Markdown')
    # _______________________________________________________________________________________
    def timeNow():
        q = str(current_date.month) if current_date.month >= 10 else '0' + str(current_date.month)
        w = str(current_date.day) if current_date.day >= 10 else '0' + str(current_date.day)
        e = str(current_date.year % 100) if current_date.year % 100 >= 10 else '0' + str(current_date.year % 100)
        r = str(current_date.hour) if current_date.hour >= 10 else '0' + str(current_date.hour)
        t = str(current_date.minute) if current_date.minute >= 10 else '0' + str(current_date.minute)
        y = str(current_date.second) if current_date.second >= 10 else '0' + str(current_date.second)
        datetime_string = q + '/' + w + '/' + e + ' ' + r + ':' + t + ':' + y
        return (datetime.strptime(datetime_string, '%m/%d/%y %H:%M:%S'))
    # _______________________________________________________________________________________
    def timeZadane(q, w):
        return (datetime.combine(date(current_date.year, current_date.month, current_date.day), time(q, w, 0)))
    # _______________________________________________________________________________________
    if message.text.find('Розклад') != -1 or message.text.find('розклад') != -1:
        # _______________________________________________________________________________________
        if message.text.find('понеділок') != -1 or message.text.find('Понеділок') != -1:
            if message.text.find('наступний') != -1 or message.text.find('Наступний') != -1:
                weekend0 = False if weekend else True
                schedle(weekend0, 0)
            else:
                schedle(weekend, 0)
        # _______________________________________________________________________________________
        elif message.text.find('вівторок') != -1 or message.text.find('Вівторок') != -1:
            if message.text.find('наступний') != -1 or message.text.find('Наступний') != -1:
                weekend0 = False if weekend else True
                schedle(weekend0, 1)
            else:
                schedle(weekend, 1)
        # _______________________________________________________________________________________
        elif message.text.find('середа') != -1 or message.text.find('Середа') != -1:
            if message.text.find('наступний') != -1 or message.text.find('Наступний') != -1:
                weekend0 = False if weekend else True
                schedle(weekend0, 2)
            else:
                schedle(weekend, 2)
        # _______________________________________________________________________________________
        elif message.text.find('четвер') != -1 or message.text.find('Четвер') != -1:
            if message.text.find('наступний') != -1 or message.text.find('Наступний') != -1:
                weekend0 = False if weekend else True
                schedle(weekend0, 3)
            else:
                schedle(weekend, 3)
        # _______________________________________________________________________________________
        elif message.text.find('пятниця') != -1 or message.text.find('Пятниця') != -1:
            if message.text.find('наступний') != -1 or message.text.find('Наступний') != -1:
                weekend0 = False if weekend else True
                schedle(weekend0, 4)
            else:
                schedle(weekend, 4)
        #_______________________________________________________________________________________
        elif len(message.text) == 7:
            if datetime.now().weekday() == 0:
                schedle(weekend, 0)
            elif datetime.now().weekday() == 1:
                schedle(weekend, 1)
            elif datetime.now().weekday() == 2:
                schedle(weekend, 2)
            elif datetime.now().weekday() == 3:
                schedle(weekend, 3)
            elif datetime.now().weekday() == 4:
                schedle(weekend, 4)
            else:
                bot.send_message(message.chat.id, "Сьогодні вихідний, можеш йти висипатися")
    # _______________________________________________________________________________________
    if message.text == 'Пара' or message.text == 'пара':
        #==========================понеділок==================================
        if datetime.now().weekday() == 0:
            # перед 1 парою
            if timeNow() < timeZadane(7, 0):
                bot.send_message(message.chat.id, 'Ще рано, іди досипай', parse_mode='Markdown')
            if timeZadane(7, 0) <= timeNow() < timeZadane(8, 30):
                delta = timeZadane(8, 30) - timeNow()
                h0 = delta.total_seconds() // 3600
                m0 = (delta.total_seconds() % 3600) // 60
                h = str(h0).replace('.0', '')
                m = str(m0).replace('.0', '')
                if h0 != 0:
                    bot.send_message(message.chat.id,
                                     'Пара *Комп`ютерні технології та програмування*, _Лекція_ почнеться за ' + str(
                                         h) + ' годин ' + str(m) + ' хвилин', parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id,
                                     'Пара *Комп`ютерні технології та програмування*, _Лекція_ почнеться за ' + str(
                                         m) + ' хвилин', parse_mode='Markdown')
            # 1 пара
            if timeZadane(8, 20) <= timeNow() <= timeZadane(10, 5):
                bot.send_message(message.chat.id,
                                 'Зараз *Комп`ютерні технології та програмування*, _Лекція_:\n https://zoom.us/j/97806771611?pwd=U2FIUmp3bUpHMVFNNHd6MmcwakNodz09',
                                 parse_mode='Markdown')
            # перед 2 парою
            if timeZadane(10, 5) < timeNow() < timeZadane(10, 20):
                delta = timeZadane(10, 20) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                bot.send_message(message.chat.id, 'Пара *Вища математика*, _Лекція_ почнеться за ' + str(m) + ' хвилин',
                                 parse_mode='Markdown')
            # 2 пара
            if timeZadane(10, 10) <= timeNow() <= timeZadane(11, 55):
                bot.send_message(message.chat.id,
                                 'Зараз *Вища математика*, _Лекція_:\n https://teams.microsoft.com/l/meetup-join/19%3acfa8e61978ce46789b29b322bbf30002%40thread.tacv2/1612796220568?context=%7b%22Tid%22%3a%227631cd62-5187-4e15-8b8e-ef653e366e7a%22%2c%22Oid%22%3a%222fb81daf-256a-4237-b4fc-27ed4fa68c67%22%7d',
                                 parse_mode='Markdown')
            # перед 3 парою
            if timeZadane(11, 55) < timeNow() < timeZadane(12, 10):
                delta = timeZadane(12, 10) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                bot.send_message(message.chat.id,
                                 'Пара *Основи автоматики та автоматизації*, _Лекція_ почнеться за ' + str(
                                     m) + ' хвилин', parse_mode='Markdown')
            # 3 пара
            if timeZadane(12, 0) <= timeNow() <= timeZadane(13, 45):
                bot.send_message(message.chat.id,
                                 'Зараз *Основи автоматики та автоматизації*, _Лекція_:\n https://zoom.us/j/94070701572?pwd=dnQwNWhadGg5aVh4OGgyUUdwR2xIdz09',
                                 parse_mode='Markdown')
            if timeNow() > timeZadane(13, 45):
                bot.send_message(message.chat.id, 'Пари вже закінчилися')
       #===================================вівторок=====================================
        elif current_date.weekday() == 1:
            # перед 1 парою
            if timeNow() < timeZadane(7, 30):
                bot.send_message(message.chat.id, 'Ще рано, іди досипай', parse_mode='Markdown')
            if timeZadane(7, 30) <= timeNow() < timeZadane(8, 30):
                delta = timeZadane(8, 30) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                bot.send_message(message.chat.id,
                                 'Пара *Фізичне виховання*, _Практична_ почнеться за ' + str(m) + ' хвилин',
                                 parse_mode='Markdown')
            # 1 пара
            if timeZadane(8, 20) <= timeNow() <= timeZadane(10, 5):
                bot.send_message(message.chat.id,
                                 'Зараз *Фізичне виховання*, _Практична_:\nХлопці: https://us05web.zoom.us/j/81070738412?pwd=QnVIejUvT3p0L1UwY3BuV1lLS21Fdz09\nДівчата:',
                                 parse_mode='Markdown')
            # перед 3 парою
            if timeZadane(10, 5) < timeNow() < timeZadane(12, 10):
                delta = timeZadane(12, 10) - timeNow()
                h0 = delta.total_seconds() // 3600
                m0 = (delta.total_seconds() % 3600) // 60
                h = str(h0).replace('.0', '')
                m = str(m0).replace('.0', '')
                if h0 != 0:
                    bot.send_message(message.chat.id,
                                     'Пара *Вища математика*, _Практична_ почнеться за ' + str(h) + ' годин ' + str(
                                         m) + ' хвилин', parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id,
                                     'Пара *Вища математика*, _Практична_ почнеться за ' + str(m) + ' хвилин',
                                     parse_mode='Markdown')
            # 3 пара
            if timeZadane(12, 0) <= timeNow() <= timeZadane(13, 45):
                bot.send_message(message.chat.id,
                                 'Зараз *Вища математика*, _Практична_:\nhttps://us04web.zoom.us/j/76001059944?pwd=ZFVuWWNLTkVIdjJ4ZDNZU09XakpxZz09',
                                 parse_mode='Markdown')
            # перед 4 парою
            if timeZadane(13, 45) < timeNow() < timeZadane(14, 15):
                delta = timeZadane(14, 15) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Пара *Історія державності та культури України*, _Практична_ почнеться за ' + str(
                                         m) + ' хвилин', parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id,
                                     'Пара *Основи автоматики та автоматизації*, _Лабораторна_, *2 підгрупа* почнеться за ' + str(
                                         m) + ' хвилин', parse_mode='Markdown')
            # 4 пара
            if timeZadane(14, 5) <= timeNow() <= timeZadane(15, 50):
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Зараз *Історія державності та культури України*, _Практична_:\nhttps://zoom.us/j/3449405168\n*ПАРОЛЬ:*362018',
                                     parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id,
                                     'Зараз *Основи автоматики та автоматизації*, _Лабораторна_, *2 підгрупа*:\nhttps://zoom.us/j/3700022521?pwd=aWh5T2UzaVF4Nm14S1FEdFNJejJSUT09',
                                     parse_mode='Markdown')
            # перед 5 парою
            if timeZadane(15, 50) < timeNow() < timeZadane(16, 0):
                delta = timeZadane(16, 0) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Пара *Комп`ютерні технології та програмування*, _Лабораторна_, *2 підгрупа* почнеться за ' + str(
                                         m) + ' хвилин', parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, 'Пари вже закінчилися')
            # 5 пара
            if timeZadane(15, 50) <= timeNow() <= timeZadane(17, 35):
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Зараз *Комп`ютерні технології та програмування*, _Лабораторна_, *2 підгрупа*:\nhttps://zoom.us/j/92723428274?pwd=eFdld3hnMS9VbVVCSjJZbEtEUTFDUT09',
                                     parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, 'Пари вже закінчилися')
            if timeNow() > timeZadane(17, 35):
                bot.send_message(message.chat.id, 'Пари вже закінчилися')
        #==============================================середа==================================
        elif current_date.weekday() == 2:
            # перед 1 парою
            if timeNow() < timeZadane(7, 0):
                bot.send_message(message.chat.id, 'Ще рано, іди досипай', parse_mode='Markdown')
            if timeZadane(7, 0) <= timeNow() < timeZadane(8, 30):
                delta = timeZadane(8, 30) - timeNow()
                h0 = delta.total_seconds() // 3600
                m0 = (delta.total_seconds() % 3600) // 60
                h = str(h0).replace('.0', '')
                m = str(m0).replace('.0', '')
                if h0 != 0:
                    if weekend:
                        bot.send_message(message.chat.id,
                                         'Пара *Комп`ютерні технології та програмування*, _Лабораторна_, *2 підгрупа* почнеться за ' + str(
                                             h) + ' годин ' + str(m) + ' хвилин', parse_mode='Markdown')
                    else:
                        bot.send_message(message.chat.id,
                                         'Пара *Основи автоматики та автоматизації*, _Лабораторна_, *1 підгрупа* почнеться за ' + str(
                                             h) + ' годин ' + str(m) + ' хвилин', parse_mode='Markdown')
                else:
                    if weekend:
                        bot.send_message(message.chat.id,
                                         'Пара *Комп`ютерні технології та програмування*, _Лабораторна_, *2 підгрупа* почнеться за ' + str(
                                             m) + ' хвилин', parse_mode='Markdown')
                    else:
                        bot.send_message(message.chat.id,
                                         'Пара *Основи автоматики та автоматизації*, _Лабораторна_, *1 підгрупа* почнеться за ' + str(
                                             m) + ' хвилин', parse_mode='Markdown')
            # 1 пара
            if timeZadane(8, 20) <= timeNow() <= timeZadane(10, 5):
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Зараз *Комп`ютерні технології та програмування*, _Лабораторна_, *2 підгрупа*:\nhttps://zoom.us/j/97619492211?pwd=T25vODhtMmNKOE5VVUtJUVJjcXNEZz09',
                                     parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id,
                                     'Зараз *Основи автоматики та автоматизації*, _Лабораторна_, *1 підгрупа*:\nhttps://zoom.us/j/3700022521?pwd=aWh5T2UzaVF4Nm14S1FEdFNJejJSUT09',
                                     parse_mode='Markdown')
            # перед 2 парою
            if timeZadane(10, 5) < timeNow() < timeZadane(10, 20):
                delta = timeZadane(10, 20) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                bot.send_message(message.chat.id,
                                 'Пара *Комп`ютерні технології та програмування*, _Лабораторна_, *1 підгрупа* почнеться за ' + str(
                                     m) + ' хвилин', parse_mode='Markdown')
            # 2 пара
            if timeZadane(10, 10) <= timeNow() <= timeZadane(11, 55):
                bot.send_message(message.chat.id,
                                 'Зараз *Комп`ютерні технології та програмування*, _Лабораторна_, *1 підгрупа*:\nhttps://zoom.us/j/93673281697?pwd=NVljOS9HSUJUNEEwdkNWc3BER2dNUT09',
                                 parse_mode='Markdown')
            # перед 3 парою
            if timeZadane(11, 55) < timeNow() < timeZadane(12, 10):
                delta = timeZadane(12, 10) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                bot.send_message(message.chat.id,
                                 'Пара *Іноземна мова за професійним спрямуванням*, _Практична_ почнеться за ' + str(
                                     m) + ' хвилин', parse_mode='Markdown')
            # 3 пара
            if timeZadane(12, 0) <= timeNow() <= timeZadane(13, 45):
                bot.send_message(message.chat.id,
                                 'Зараз *Іноземна мова за професійним спрямуванням*, _Практична_:\nКушка: https://bit.ly/3bUjTVg\nГасько: https://zoom.us/j/9064294090?pwd=ZzViVjBwc052WURCYlozeXRnOWk0UT09',
                                 parse_mode='Markdown')
            # перед 4 парою
            if timeZadane(13, 45) < timeNow() < timeZadane(14, 15):
                delta = timeZadane(14, 15) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Пара *Комп`ютерні технології та програмування*, _Практична_ почнеться за ' + str(
                                         m) + ' хвилин', parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id,
                                     'Пара *Історія державності та культури України*, _Практична_ почнеться за ' + str(
                                         m) + ' хвилин', parse_mode='Markdown')
            # 4 пара
            if timeZadane(14, 5) <= timeNow() <= timeZadane(15, 50):
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Зараз *Комп`ютерні технології та програмування*, _Практична_:\nhttps://zoom.us/j/97417892205?pwd=U0ptTkNLVmRUMjMrOXVScXpMOFkvQT09',
                                     parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id,
                                     'Зараз *Історія державності та культури України*, _Практична_:\nhttps://zoom.us/j/3449405168\n*ПАРОЛЬ:*362018',
                                     parse_mode='Markdown')
            if timeNow() > timeZadane(15, 50):
                bot.send_message(message.chat.id, 'Пари вже закінчилися')
        #=====================================четвер=================================
        elif current_date.weekday() == 3:
            # перед 3 парою
            if timeNow() < timeZadane(9, 0):
                bot.send_message(message.chat.id, 'Ще рано, іди досипай', parse_mode='Markdown')
            if timeZadane(9, 0) <= timeNow() < timeZadane(12, 10):
                delta = timeZadane(12, 10) - timeNow()
                h0 = delta.total_seconds() // 3600
                m0 = (delta.total_seconds() % 3600) // 60
                h = str(h0).replace('.0', '')
                m = str(m0).replace('.0', '')
                if h0 != 0:
                    if weekend:
                        bot.send_message(message.chat.id,
                                         'Пара *Фізика*, _Практична_ почнеться за ' + str(h) + ' годин ' + str(
                                             m) + ' хвилин(и)', parse_mode='Markdown')
                    else:
                        bot.send_message(message.chat.id,
                                         'Пара *Фізика*, _Лабораторна_, *1 підгрупа* почнеться за ' + str(
                                             h) + ' годин ' + str(m) + ' хвилин(и)', parse_mode='Markdown')
                else:
                    if weekend:
                        bot.send_message(message.chat.id,
                                         'Пара *Фізика*, _Практична_ почнеться за ' + str(m) + ' хвилин(и)',
                                         parse_mode='Markdown')
                    else:
                        bot.send_message(message.chat.id,
                                         'Пара *Фізика*, _Лабораторна_, *1 підгрупа* почнеться за ' + str(
                                             m) + ' хвилин(и)', parse_mode='Markdown')
            # 3 пара
            if timeZadane(12, 0) <= timeNow() <= timeZadane(13, 45):
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Зараз *Фізика*, _Практична_:\nhttps://us02web.zoom.us/j/81284721222?pwd=MjNJK1IzQlgxY2NiaS9GMWJ5dGh3QT09',
                                     parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id,
                                     'Зараз *Фізика*, _Лабораторна_,:\nРоманюк: https://us02web.zoom.us/j/87035903619?pwd=eGFWQ2JIeWRpMTVvTVg4TkJYSE1tdz09\nСемків: https://zoom.us/j/98065457693?pwd=bkhtRlNxL3E3SnZCTU1oSFNHcHJNQT09',
                                     parse_mode='Markdown')
            # перед 4 парою
            if timeZadane(13, 45) < timeNow() < timeZadane(14, 15):
                delta = timeZadane(14, 15) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                bot.send_message(message.chat.id,
                                 'Пара *Комп`ютерні технології та програмування*, _Лабораторна_, *1 підгрупа* почнеться за ' + str(
                                     m) + ' хвилин(и)', parse_mode='Markdown')
            # 4 пара
            if timeZadane(14, 5) <= timeNow() <= timeZadane(15, 50):
                bot.send_message(message.chat.id,
                                 'Зараз *Комп`ютерні технології та програмування*, _Лабораторна_, *1 підгрупа*:\nhttps://zoom.us/j/92237604092?pwd=RFhlOCtWRHUrelRTbEQ2Mk9MUGpsUT09',
                                 parse_mode='Markdown')
            # перед 5 парою
            if timeZadane(15, 50) < timeNow() < timeZadane(16, 0):
                delta = timeZadane(16, 0) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                bot.send_message(message.chat.id,
                                 'Пара *Комп`ютерні технології та програмування*, _Лабораторна_, *2 підгрупа* почнеться за ' + str(
                                     m) + ' хвилин(и)', parse_mode='Markdown')
            # 5 пара
            if timeZadane(15, 50) <= timeNow() <= timeZadane(17, 35):
                bot.send_message(message.chat.id,
                                 'Зараз *Комп`ютерні технології та програмування*, _Лабораторна_, *2 підгрупа*:\nhttps://zoom.us/j/97097891532?pwd=R1grS2VUNTNqOEs4Vk55UGJhZms0Zz09',
                                 parse_mode='Markdown')
            if timeNow() > timeZadane(17, 35):
                bot.send_message(message.chat.id, 'Пари вже закінчилися')
        #===================================п'ятниця================================
        elif current_date.weekday() == 4:
            # перед 1 парою
            if timeNow() < timeZadane(7, 0):
                bot.send_message(message.chat.id, 'Ще рано, іди досипай', parse_mode='Markdown')
            if timeZadane(7, 0) <= timeNow() < timeZadane(8, 30):
                delta = timeZadane(8, 30) - timeNow()
                h0 = delta.total_seconds() // 3600
                m0 = (delta.total_seconds() % 3600) // 60
                h = str(h0).replace('.0', '')
                m = str(m0).replace('.0', '')
                if h0 != 0:
                    if weekend:
                        bot.send_message(message.chat.id,
                                         'Пара *Вища математика*, _Лекція_ почнеться за ' + str(h) + ' годин ' + str(
                                             m) + ' хвилин', parse_mode='Markdown')
                    else:
                        bot.send_message(message.chat.id,
                                         'Пара *Історія державності та культури України*, _Лекція_ почнеться за ' + str(
                                             h) + ' годин ' + str(m) + ' хвилин', parse_mode='Markdown')
                else:
                    if weekend:
                        bot.send_message(message.chat.id,
                                         'Пара *Вища математика*, _Лекція_ почнеться за ' + str(m) + ' хвилин',
                                         parse_mode='Markdown')
                    else:
                        bot.send_message(message.chat.id,
                                         'Пара *Історія державності та культури України*, _Лекція_ почнеться за ' + str(
                                             m) + ' хвилин', parse_mode='Markdown')
            # 1 пара
            if timeZadane(8, 20) <= timeNow() <= timeZadane(10, 5):
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Зараз *Вища математика*, _Лекція_:\nhttps://teams.microsoft.com/l/meetup-join/19%3acfa8e61978ce46789b29b322bbf30002%40thread.tacv2/1612797709286?context=%7b%22Tid%22%3a%227631cd62-5187-4e15-8b8e-ef653e366e7a%22%2c%22Oid%22%3a%222fb81daf-256a-4237-b4fc-27ed4fa68c67%22%7d',
                                     parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id,
                                     'Зараз *Історія державності та культури України*, _Лекція_:\nhttps://zoom.us/j/96736044871?pwd=S0N0OFhva2h1OURQdmpMZWNmR0Rkdz09',
                                     parse_mode='Markdown')
            # перед 2 парою
            if timeZadane(10, 5) < timeNow() < timeZadane(10, 20):
                delta = timeZadane(10, 20) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                bot.send_message(message.chat.id,
                                 'Пара *Комп`ютерні технології та програмування*, _Лекція_ почнеться за ' + str(
                                     m) + ' хвилин', parse_mode='Markdown')
            # 2 пара
            if timeZadane(10, 10) <= timeNow() <= timeZadane(11, 55):
                bot.send_message(message.chat.id,
                                 'Зараз *Комп`ютерні технології та програмування*, _Лекція_:\nhttps://zoom.us/j/92809723013?pwd=VkNqNS84MlhjNUhidWJRNTZodDNnZz09',
                                 parse_mode='Markdown')
            # перед 3 парою
            if timeZadane(11, 55) < timeNow() < timeZadane(12, 10):
                delta = timeZadane(12, 10) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                bot.send_message(message.chat.id, 'Пара *Фізика*, _Лекція_ почнеться за ' + str(m) + ' хвилин',
                                 parse_mode='Markdown')
            # 3 пара
            if timeZadane(12, 0) <= timeNow() <= timeZadane(13, 45):
                bot.send_message(message.chat.id,
                                 'Зараз *Фізика*, _Лекція_:\nhttps://us02web.zoom.us/j/88623572013?pwd=UzVIb1lGUW8xM0VZRGwrdTcwcFZKdz09',
                                 parse_mode='Markdown')
            # перед 4 парою
            if timeZadane(13, 45) < timeNow() < timeZadane(14, 15):
                delta = timeZadane(14, 15) - timeNow()
                m0 = (delta.total_seconds() % 3600) // 60
                m = str(m0).replace('.0', '')
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Пара *Основи автоматики та автоматизації*, _Лекція_ почнеться за ' + str(
                                         m) + ' хвилин', parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, 'Пари вже закінчилися')
            # 4 пара
            if timeZadane(14, 5) <= timeNow() <= timeZadane(15, 50):
                if weekend:
                    bot.send_message(message.chat.id,
                                     'Зараз *Основи автоматики та автоматизації*, _Лекція_:\nhttps://zoom.us/j/94070701572?pwd=dnQwNWhadGg5aVh4OGgyUUdwR2xIdz09',
                                     parse_mode='Markdown')
                else:
                    bot.send_message(message.chat.id, 'Пари вже закінчилися')
            if timeNow() > timeZadane(15, 50):
                bot.send_message(message.chat.id, 'Пари вже закінчилися')
        # вихідні
        else:
            bot.send_message(message.chat.id, 'Сьогодні немає пар')


bot.polling(none_stop=True, interval=0)
