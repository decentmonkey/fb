label citizen6_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_6_1
            if citizen6_offered_last_day == day:
                img Dial_Citizen_6_4
                citizen "Нельзя! Я тороплюсь!"
                return
            citizen "Да, Леди? Что Вы хотели?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen6_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_6_2
                        call reduce_flyers()
                        citizen "Взять флаер? Хорошо..."
                        img Dial_Citizen_6_3
                        citizen "Какой красивый флаер! Прямо такой-же как Ваше личико!"
                        label citizen6_loop1:
                            menu:
                                "Не надо сравнивать меня с флаером!":
                                    #img Моника злится
                                    m "Не надо сравнивать меня с флаером!"
                                "Я Вам нравлюсь? (disabled)":
                                    jump citizen6_loop1
                    else:
                        img Dial_Citizen_6_3
                        citizen "Я тороплюсь! Давайте в другой раз!"
        "Уйти.":
            pass
    return
