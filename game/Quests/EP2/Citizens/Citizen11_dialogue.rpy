label citizen11_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_11_1
            if citizen11_offered_last_day == day:
                img Dial_Citizen_11_4
                citizen "Я занят!"
                return
            citizen "Да? Что Вам угодно?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen11_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        call reduce_flyers()
                        citizen "Флаер? Хорошо..."
                        img Dial_Citizen_11_2
                        citizen "Ты мне кажешься знакомой... Эта одежда..."
                        img Dial_Citizen_11_3
                        citizen "Точно! Ты ведь предлагаешь услуги? Я бы не против!"
                        label .loop1
                        menu:
                            "Я ничего не предлагаю!":
                                #img Моника злится
                                m "Я ничего не предлагаю!"
                            "А какие услуги Вас интересуют? (disabled)":
                                jump .loop1
                    else:
                        img Dial_Citizen_11_3
                        citizen "Я занят!"
        "Уйти.":
            pass
    return
