default houseOutMode = "usual"
default lastDayFunMusic = 0

label house_out:
    if gameStage > 2:
        call change_scene("street_house_main_yard", "Fade_long")
        return

    if houseOutMode == "evening":
        m "Я устала за сегодня.
        Не хочу на улицу."
        return
    if houseOutMode == "evening2":
        m "Я не пойду туда. На улице одни идиоты!"
        return
    if houseOutMode == "usual":
        if bathTaken == False:
            m "Не пойду же я на улицу грязной!"

            "Мне надо принять душ!"
            return
        if monicaEated == False:
            m "Я не могу идти заниматься делами на голодный желудок"

            "Мне стоит сначала поесть."
            return

        if cloth_type != "BusinessCloth":
            m "Как я пойду на улицу в таком виде?"

            "Мне надо выглядеть подобающе."

            "Я ведь королева!"
            return
    $ remove_objective("go_outside")

    if lastDayFunMusic != day:
        $ lastDayFunMusic = day
        music streetFunMusic
    call change_scene("street_house_main_yard", "Fade_long") from _call_change_scene_51
    return
