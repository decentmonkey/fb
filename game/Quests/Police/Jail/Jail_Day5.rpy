label jail_day5:
    $ jailDay = 5
    $ day = day + 1
    $ jailDaySceneStage = 0
    $ jailScenePlace = 0
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_5_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_5_1"
    $ policeCellMonica1 = "Police_Cell_1_Day_5_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_5_1"
    $ policeCellMonicaLabel = "jail_day5_Monica"
    $ policeCellBedLabel = "jail_day5_Bed"
    $ policeCellCageLabel = "jail_day5_Cage"
    stop music fadeout 1.0
    call textonblack(_("ДЕНЬ 5"))
    img black_screen
    with Dissolve(1)
    music Jail_Clock

    img 2328
    with fadelong
    mt "Пятый день..."
    img 2329
    mt "Надо уломать этого жирного урода чтобы он принес мне одежду."
    "Мне надоело быть в таком виде!"

    if jailBoobsForFood == True:
        mt "И... еда..."
        "Мне что, теперь все время показывать ему свою грудь?"
        "Этому мерзкому насекомому?!"
        #
        "Я! МОНИКА БАКФЕТТ!!!"
    call refresh_scene_fade()
    return

label jail_day5_Monica(obj_name, obj_data):
    if jailDaySceneStage == 0:
        mt "Я.. хочу.. есть..."
    if jailDaySceneStage == 1:
        mt "Мне очень плохо здесь..."

    return

label jail_day5_Bed(obj_name, obj_data):
    if act == "l":
        call jail_day1_Bed(obj_name, obj_data)
        return
    if jailDaySceneStage == 0:
        mt "Я.. хочу.. есть..."
    if jailDaySceneStage == 1:
        menu:
            "Лечь спать":
                pass
            "Не ложиться":
                return
        call jail_day6()
        return
    return

label jail_day5_Cage(obj_name, obj_data):
    if act == "l":
        call jail_cage()
        call refresh_scene_fade()
        return
    if act == "w":
        $ cageInteractLabel = "jail_day5_Cage_Interact"
        call change_scene("police_jail_cage_scene")
        return

    return

label jail_day5_Cage_Interact:
    if jailDaySceneStage == 0:
        call jail_day5_1()

    if jailDaySceneStage == 1:
        img 2253
        with fadelong
        mt "Он не подходит."
        "Может быть он вообще ушел?"
        "Мне не видно отсюда!"
        if jailBoobsForFoodShowed == True:
            call jail_cage()
            return
        return
    return

label jail_day5_1:
    music Groove2_85
    # подходит
    img 5117
    with fadelong
    w
    img 2330
    overseer "Чего тебе снова?"
    m "Сэр."
    "Вы же знаете что надо бедной девушке?"
    if jailBoobsForFood == True:
        # ждет сисек :)
        img 5169
        overseer "..."
        img 5170
        m "..."
        img 5169
        overseer "..."
        m "Сэр? Чего Вы ждете?"
        overseer "..."
        img 5171
        m "Что? Снова сиськи?!?!"
        img 5172
        overseer "Я ухожу?"
        menu:
            "Сказать как его зовут." if monicaKnowOverseerName == True:
                call jail_boobs_for_food_end()
            "Показать грудь.":
                img 2373
                m "Стойте!"
                # показывает сиськи
                call jail_boobs_for_food()
            "Не показывать.":
                m "Я не хочу показывать свою грудь..."
                img 5173
                overseer "Нет вежливости, нет сисек, нет еды..."
                img 5116
                w
                # уходит
                call refresh_scene_fade()
                return
        img 5116
        with fadelong
        overseer "Сейчас принесу."

    else:
        img 5116
        with fadelong
        overseer "Сейчас принесу."

    img black_screen
    with Dissolve(1)
    img 5118
    with fadelong
    w
    # уходит и приходит
    if jailBoobsForFood == True:
        img 2324
    else:
        img 2330
    overseer "На, ешь!"
    m "Спасибо, Сэр!"
    mt "Спасибо, жирный урод!"
    $ jailFoodInteractLabel = "jail_day5_1a"
    call change_scene("police_jail_food_scene", "Fade", False)
    return

label jail_day5_1a:

    music Groove2_85
    img 2331
    with fadelong
    m "Сэр?"
    img 2330
    overseer "Ну что тебе снова?"
    img 2331
    music Hidden_Agenda
    m "Сэр."
    "А не могли бы Вы купить мне одежду?"
    "Такую которую здесь можно носить?"
    "Я была бы Вам очень благодарна!"
    "Вы стали бы в моих глазах настоящим Джентельменом!"
    img 2330
    music Groove2_85
    overseer "Кем бы я стал?"
    "Что это за слово?"
    "Какое-то ругательство что-ли?"
    img 2332
    music Hidden_Agenda
    m "Что Вы? Сэр!"
    "Это комплимент!"
    img 2333
    music Groove2_85
    overseer "Копли... Что?"
    "Что ты меня путаешь своими словечками?"
    "Нет у меня денег ничего никому покупать!"
    "Я здесь почти ничего не получаю!"
    "Разговор закончен на сегодня!"
    music Jail_Clock
    $ jailDaySceneStage = 1
    $ policeCellStageName1 = "scene_Police_Cell_1_Day_5_1"
    $ policeCellStageName2 = "scene_Police_Cell_2_Day_5_2"
    $ policeCellMonica1 = "Police_Cell_1_Day_5_1"
    $ policeCellMonica2 = "Police_Cell_2_Day_5_2"
    call refresh_scene_fade()
    return

    call jail_day6()

    return
