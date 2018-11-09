label citizen10_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_10_1
            if citizen10_offered_last_day == day:
                img Dial_Citizen_10_4
                citizen "Я Вас не знаю! Не отвлекайте меня!"
                return
            citizen "Да? Я Вас откуда-то знаю?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen10_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_10_2
                        call reduce_flyers()
                        citizen "Флаер? Хорошо..."
                        img Dial_Citizen_10_3
                        citizen "Я уверен, что такая красотка может предложить что-то еще!"
                        label .loop1
                        menu:
                            "Мне больше нечего предлагать!":
                                #img Моника злится
                                m "Мне больше нечего предлагать!"
                            "А что Вас интересует... (disabled)":
                                jump .loop1
                    else:
                        img Dial_Citizen_10_3
                        citizen "У меня полные карманы всяких бумажек!"
        "Уйти.":
            pass
    return
