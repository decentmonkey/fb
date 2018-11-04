label intro_scene:
    $ print "enter_intro_scene"

    $ scene_name = "intro_scene"
    $ scene_caption = _("Bedroom")
    $ clear_scene_from_objects(scene_name)

    $ scene_image = "scene_Intro"
    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Intro_Monica", "click" : "intro_environment", "actions" : "lh", "zorder":10})

    return

label intro_environment(obj_name, obj_data):
    if obj_name == "Monica":
        if obj_data["action"] == "l":
            mt "Zzzzzzzz...."
        if obj_data["action"] == "h":
            $ remove_objective("monica_wakeup")
            call start_new_game() from _call_start_new_game
            return
    return

label intro_scene_start:
#    music BossaBossa
    music Cheery_Monday_silent
#    music Poppers_and_Prosecco
    help "Привет!
    Добро пожаловать в обновленную игру про Монику!"

    "Что стоит сразу запомнить."

    show screen intro_image("Intro_Help1")
    with Dissolve(0.5)
    "В левом верхнем углу вы можете всегда видеть много полезной информации.
    Например, текущие задания!"

    show screen intro_image("Intro_Help2")
    with Dissolve(0.5)
    "Справа располагается название текущей локации и кнопка вызова карты."
    "Сейчас она недоступна, потому что Моника спит :)"

    show screen intro_image("Intro_Help3")
    with Dissolve(0.5)
    "Также справа находится Bitchmeter :).
    Он показывает кем сейчас является Моника."

    "Вы можете влиять на ее поведение в течении игры."
    "И сделать из нее либо скромную девушку, либо законченную сучку."
    "Все это будет сказываться на игре и на развитии сюжета!"

    show screen intro_image("Intro_Help4")
    with Dissolve(0.5)
    "На экране много интерактивных объектов.
    С ними можно взаимодействовать по разному."

    "Например, можно посмотреть на них, можно использовать, разговаривать и тд."
    "Либо использовать на них какие-то предметы инвентаря."

    "Меню действий вызывается левым кликом мышки опционально, либо правым кликом мышки принудительно."

    show screen intro_image("Intro_Help5")
    with Dissolve(0.5)

    "Во время диалогов правая кнопка мыши, либо клавиша <H>, скрывают диалог, чтобы вы могли видеть картинку целиком!"

    "Также вы можете включить принудительную паузу после диалога перед сменой картинки в настройках игры!"

    show screen intro_image("Intro_Help6")
    with Dissolve(0.5)
    "Если появилась кнопка с вопросом, значит для этого квеста есть подсказки!"

    "Нажмите на кнопку, если Вы запутались!"

    hide screen intro_image
    with Dissolve(0.5)

    "А теперь пришла мора разбудить Монику и начать игру!
    Удачи!"


#intro_image
    return
