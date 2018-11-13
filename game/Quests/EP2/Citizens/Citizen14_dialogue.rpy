label citizen14_dialogue:
    menu:
        "Мистер... Можно к Вам обратиться?":
            m "Мистер... Можно к Вам обратиться?"
            #img Моника спрашивает
            img Dial_Citizen_14_1
            if citizen14_offered_last_day == day:
                img Dial_Citizen_14_4
                citizen "Я тороплюсь! У меня много важных дел!"
                return
            citizen "Какая красавица! Что тебе надо от такого как Я? Ик!..."
            menu:
                "Возьмите, пожалуйста, этот флаер...":
                    $ citizen14_offered_last_day = day
                    m "Возьмите, пожалуйста, этот флаер..."
                    if renpy.random.randint(0, 1) == 0:
                        img Dial_Citizen_14_2
                        citizen "Флаер?..."
                        call reduce_flyers()
                        "Хорошо... Ик!"
                        img Dial_Citizen_14_3
                        citizen "Но ты же не просто так подошла ко мне!"
                        "Я ведь понравился тебе? Хрюк..."
                        label .loop1:
                            menu:
                                "Мне никто не может понравиться в этой дыре!":
                                    #img Моника злится
                                    m "Мне никто не может понравиться в этой дыре!"
                                "Может и так... (disabled)":
                                    jump .loop1
                    else:
                        img Dial_Citizen_14_3
                        citizen "Не возьму... Я все-равно его потеряю... Хрюк..."
        "Уйти.":
            pass
    return
