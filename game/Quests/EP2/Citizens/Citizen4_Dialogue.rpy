label citizen4_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_4_1
            if citizen4_offered_last_day == day:
                img Dial_Citizen_4_4
                citizen "Нельзя!"
                return
            citizen "Да?"
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen4_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_4_2
                        call reduce_flyers()
                        citizen "Хорошо."
                        citizen "А что на нем?"
                        m "Это реклама вкусного кебаба... Там же написано!"
                        img Dial_Citizen_4_3
                        citizen "А я подумал Вы подошли познакомиться со мной!"
                        label citizen4_loop1
                        menu:
                            "У меня нет желания знакомиться с Вами!":
                                #img Моника злится
                                m "У меня нет желания знакомиться с Вами!"
                            "Что Вы подразумеваете под знакомством? (disabled)":
                                jump citizen4_loop1
                    else:
                        img Dial_Citizen_4_3
                        citizen "Давайте в другой раз!"
        "Уйти.":
            pass
    return
