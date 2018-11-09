label citizen9_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_9_1
            if citizen9_offered_last_day == day:
                img Dial_Citizen_9_4
                citizen "Простите! Вы уже подходили ко мне!"
                return
            citizen "А? Да?"
            "Что?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen9_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_9_2
                        call reduce_flyers()
                        citizen "А? Что?"
                        "Флаер?"
                        "Хорошо..."
                        img Dial_Citizen_9_3
                        citizen "А я тебя знаю!"
                        "Мы с тобой как-то развлекались!"
                        "Повернись задом, я вспомню точно!"
                        label .loop1
                        menu:
                            "Я не собираюсь никак поворачиваться!":
                                #img Моника злится
                                m "Я не собираюсь никак поворачиваться!"
                            "Хорошо... (disabled)":
                                jump .loop1
                    else:
                        img Dial_Citizen_9_3
                        citizen "Простите! Я пытаюсь кое-что вспомнить..."
                        "Вы меня отвлекаете!"
        "Уйти.":
            pass
    return
