label citizen3_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_3_1
            if citizen3_offered_last_day == day:
                img Dial_Citizen_3_4
                citizen "Вы меня уже отвлекали сегодня!"
                return
            citizen "Да, Мадам? Что Вы хотели?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen3_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_3_2
                        call reduce_flyers()
                        citizen "Хорошо."
                        img Dial_Citizen_3_3
                        citizen "А что на нем? Ваш номер телефона?"
                        "Вы девочка по вызову?"
                        label citizen3_loop1:
                            menu:
                                "НЕТ!":
                                    #img Моника злится
                                    m "НЕТ!"
                                "В общем нет, но... (disabled)":
                                    jump citizen3_loop1
                    else:
                        img Dial_Citizen_3_3
                        citizen "Я занят! Пожалуйста, не отвлекайте меня!"
        "Уйти.":
            pass
    return
