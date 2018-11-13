label citizen8_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_8_1
            if citizen8_offered_last_day == day:
                img Dial_Citizen_8_4
                citizen "Детка! Не приставай ко мне!"
                return
            citizen "Да, детка? Что ты хочешь мне предложить?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen8_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_8_2
                        call reduce_flyers()
                        citizen "Взять флаер? Хорошо..."
                        img Dial_Citizen_8_3
                        citizen "Детка! Ты подошла только за этим?"
                        "Хочешь предложить что-то еще?"
                        label .loop1:
                            menu:
                                "Я ничего не собираюсь предлагать!":
                                    #img Моника злится
                                    m "Я ничего не собираюсь предлагать!"
                                "А что бы Вы хотели? (disabled)":
                                    jump .loop1
                    else:
                        img Dial_Citizen_8_3
                        citizen "Детка! Не приставай ко мне с этим!"
        "Уйти.":
            pass
    return
