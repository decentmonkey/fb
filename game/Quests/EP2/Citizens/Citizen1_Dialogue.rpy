label citizen1_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_1_1
            if citizen1_offered_last_day == day:
                img Dial_Citizen_1_4
                citizen "Эй! Тетя!"
                "Ты уже подходила ко мне!"
                "Хватит с меня твоих флаеров!"
                return
            citizen "Да, тетя? Что тебе надо?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen1_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_1_2
                        citizen "Хорошо, давай сюда свой флаер!"
                        img Dial_Citizen_1_3
                        citizen "Тетя! А больше ты ничего мне не можешь дать?"
                        label citizen1_loop1
                        menu:
                            "Больше ничего!":
                                #img Моника злится
                                call reduce_flyers()
                                m "Больше ничего!"
                            "А что бы ты хотел? (disabled)":
                                jump citizen1_loop1
                    else:
                        img Dial_Citizen_1_3
                        citizen "Мне не нужен твой флаер, тетя!"

        "Уйти.":
            pass
    return
