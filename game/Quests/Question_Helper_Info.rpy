label question_helper_hairdye:
    menu:
        "Посмотреть подсказку":
            img help1_1
            with fadelong
            help "Подойти к зеркалам и взять краску для волос."
            img help1_2
            with fade
            help "Разлить краску на ковер."
        "Продолжить игру.":
            pass

    call refresh_scene_fade()
#    help "Help!"
    return

label question_helper_hairdye_find_julia:
    menu:
        "Посмотреть подсказку":
            help "Юлия в подвале. Вход в подвал у лестницы на нижнем этаже."
        "Продолжить игру.":
            pass

    return


label question_helper_laundry:
    menu:
        "Посмотреть подсказку":
            img help1_3
            with fadelong
            w
            help "Взять платье в нижнем ящике."
            w
            img help1_4
            with fade
            w
            help "Взять утюг из нижней коробки."
            w
            img help1_5
            with fade
            help "Убрать мусор. Затем применить поочереди платье и утюг, чтобы погладить."
        "Продолжить игру.":
            pass
    call refresh_scene_fade()
    return

label question_gas_trader1:
    menu:
        "Посмотреть подсказку":
            img help1_6
            with fadelong
            help "Кассир за дверью."
        "Продолжить игру.":
            pass
    call refresh_scene_fade()
    return

label question_gas_trader2:
    menu:
        "Посмотреть подсказку":
            img help1_7
            with fadelong
            help "Идти сюда."
            img help1_8
            with fade
            help "Затем идти сюда."
            img help1_9
            with fade
            help "Разбить дорогую бутылку вина."
        "Продолжить игру.":
            pass
    call refresh_scene_fade()
    return

label question_cloth_shop_dick_buy_dress:
    menu:
        "Посмотреть подсказку":
            img help1_10
            with fadelong
            help "Проверить места."
            w
            img help1_11
            with fade
            w
            img help1_12
            with fade
            help "После каждого места идти примерять платье в примерочную."
            img help1_13
            with fade
            help "Повесить свое платье на вешалку."
            img help1_14
            help "Нажать сюда чтобы примерить новое платье."
        "Продолжить игру.":
            pass
    call refresh_scene_fade()
    return

label question_hostel_perry_dress:
    img help1_15
    with fadelong
    w
    return

label question_office_tea_lost_phone:
    img help1_16
    with fadelong
    help "Телефон на полу при входе в офис..."
    w
    return
