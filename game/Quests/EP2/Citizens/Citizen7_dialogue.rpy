label citizen7_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_7_1
            if citizen7_offered_last_day == day:
                img Dial_Citizen_7_4
                citizen "Я пытаюсь сосредоточиться на искусстве!"
                "Вы все-время отвлекаете меня!"
                return
            citizen "Да? Что Вы хотели?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen7_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_7_2
                        call reduce_flyers()
                        citizen "Взять флаер? Хорошо..."
                        img Dial_Citizen_7_3
                        citizen "А Вы хорошо выглядите!"
                        "Будете моей моделью?"
                        label citizen7_loop1:
                            menu:
                                "Я не собираюсь быть моделью для кого-то в этих трущобах!":
                                    #img Моника злится
                                    m "Я не собираюсь быть моделью для кого-то в этих трущобах!"
                                "Моделью? В каком жанре? (disabled)":
                                    jump citizen7_loop1
                    else:
                        img Dial_Citizen_7_3
                        citizen "Я пытаюсь сосредоточиться на искусстве!"
                        "Не отвлекайте меня!"
        "Уйти.":
            pass
    return
