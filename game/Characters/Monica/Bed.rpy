
label check_sleep:
    if gameStage > 2:
        mt "Как же я хочу прилечь на нее! На мою любимую кроватку!"
        "Но если эта сучка Бетти заметит это, то сразу выгонит меня на улицу!"
        "Мне надо быть осторожной..."
        "Пока я не решила свои небольшие проблемы..."
        return

    if day_time == "day":
        m "Я люблю подольше поспать, но я уже совсем выспалась.
        Надо заняться чем-то другим.
        Мне скучно."
        return

    if day == 1 and day_time == "evening":
        if cloth == "EveningDress":
#            imgc Dial_MonicaEveningDress_5
#            mt "Мне надо переодеться сначала."
            imgc inv_eveningdress
            mt "Надо переодеться в спальную одежду"
            return
        if cloth_type == "HomeCloth":
            img 1456
            mt "Надо переодеться в спальную одежду"
            return
        if bathTakenJust == False or monicaEated == False or (juliaPunished == True and juliaPunishedChecked == False):
#            img 1457
            img 3384
            mt "Я еще не приготовилась ко сну."
            "Надо доделать домашние дела."
            return
        menu:
            "Лечь спать?":
                m "Я уже устала.
                Пора ложиться спать..."
                $ remove_objective("sleep")
                stop music fadeout 1.0
                img 1010
                with fadelong
                $ renpy.pause(2)
                call gas_saleswoman_dialogue2()
                #call quest_house_monica_day2_day_init()
                return


            "Не ложиться...":
                return
    if day == 2 and day_time == "evening":
        if cloth == "BusinessCloth2":
            imgc Dial_Monica_BusinessCloth2_Thinking
            mt "Я только с улицы."
            "Сначала надо переодеться."
            return
        if cloth_type == "HomeCloth":
            imgc inv_homecloth2
            mt "Надо переодеться в спальную одежду"
            return
        if bathTaken == False or monicaEated == False:
            imgc inv_lingerie3
            mt "Я еще не приготовилась ко сну."
            "Надо доделать домашние дела."
            return
        menu:
            "Лечь спать?":
                m "Я уже устала.
                Пора ложиться спать..."
                $ remove_objective("sleep")
                stop music fadeout 1.0
                img 1010
                with fadelong
                $ renpy.pause(2)
                call quest_house_monica_day3_day_init()
                return
            "Не ложиться...":
                return
    return
