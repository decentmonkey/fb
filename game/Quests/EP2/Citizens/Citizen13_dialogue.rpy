label citizen13_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_13_1
            if citizen13_offered_last_day == day:
                img Dial_Citizen_13_4
                citizen "Мне не до тебя сейчас!"
                return
            citizen "Да, Малышка? Что ты хочешь сказать мне?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen13_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_13_2
                        citizen "Просто флаер?..."
                        call reduce_flyers()
                        "Хорошо..."
                        img Dial_Citizen_13_3
                        citizen "У меня идея получше!"
                        "Малышка, пойдем развлечемся!"
                        label .loop1
                        menu:
                            "Я никого не собираюсь развлекать!":
                                #img Моника злится
                                m "Я никого не собираюсь развлекать!"
                            "Чем ты хочешь развлечься? (disabled)":
                                jump .loop1
                    else:
                        img Dial_Citizen_13_3
                        citizen "Не, Малышка! У меня нет места для твоего флаера!"
        "Уйти.":
            pass
    return
