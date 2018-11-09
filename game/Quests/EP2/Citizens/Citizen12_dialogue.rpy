label citizen12_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_12_1
            if citizen12_offered_last_day == day:
                img Dial_Citizen_12_4
                citizen "Я тороплюсь! Мне некогда!"
                return
            citizen "Да, Крошка? Что ты хочешь от меня?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen12_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_12_2
                        citizen "Ээээ... взять что?"
                        m "Возьмите, пожалуйста, этот флаер..."
                        call reduce_flyers()
                        citizen "Ок..."
                        img Dial_Citizen_12_3
                        citizen "И все? А как же развлечься?"
                        label .loop1
                        menu:
                            "Я никого не собираюсь развлекать!":
                                #img Моника злится
                                m "Я никого не собираюсь развлекать!"
                            "Чем тебя развлечь? (disabled)":
                                jump .loop1
                    else:
                        img Dial_Citizen_12_3
                        citizen "Мне неинтересны никакие флаеры!"
        "Уйти.":
            pass
    return
