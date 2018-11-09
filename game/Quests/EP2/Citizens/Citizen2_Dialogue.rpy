label citizen2_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_2_1
            if citizen2_offered_last_day == day:
                img Dial_Citizen_2_4
                citizen "Иди отсюда со своими флерами!"
                "Ты уже подходила ко мне!"
                return
            citizen "Хоу! Девочка! Что тебе надо?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen2_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_2_2
                        call reduce_flyers()
                        citizen "Хорошо, давай сюда свой флаер!"
                        img Dial_Citizen_2_3
                        citizen "Выпьешь со мной пива?"
                        label citizen2_loop1
                        menu:
                            "Еще чего!":
                                #img Моника злится
                                m "Еще чего!"
                            "У меня есть идея получше (disabled)":
                                jump citizen2_loop1
                    else:
                        img Dial_Citizen_2_3
                        citizen "Мне не нужны никакие флаеры!"
        "Уйти.":
            pass
    return
