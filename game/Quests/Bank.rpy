label bank_office_talk1:
#    img 1649
#    w
#    $ add_objective("goto_bank1", _("Ехать в Банк по вопросу денег от Стива"), c_red, 20)
    $ remove_objective("goto_bank1")
    music Stealth_Groover
    img 1650
    with fadelong
    bank_clerk "Добрый день, Мэм!"
    "Чем могу Вам помочь?"

    img 1651
    m "Здравствуйте."
    "Я пришла уточнить ньюансы по движению на моих счетах."

    img 1652
    bank_clerk "Да, пожалуйста."
    "Ваши документы."

    img 1653
    m "Пожалуйста, возьмите."
    bank_clerk "Спасибо."

    img 1654
    m "Вот здесь бумага на которой написаны интересующие меня реквизиты."

    img 1655
    bank_clerk "Спасибо."
    "Уточняю."
    "..."

    img 1656
    with fadelong
    bank_clerk "Извините, Мэм."
    "По данным реквизитам движения средств отсутствуют."

    img 1657
    m "То есть вы хотите сказать что никаких денег не поступало?"

    bank_clerk "Нет, Мэм."

    m "То есть это не ваша задержка, а мне не перечислили деньги?"

    bank_clerk "Движения средств не зарегистрированы, Мэм."

    img 1658
    with fade
    m "Значит этот мешок с дерьмом все-таки мне соврал..."

    img 1659
    bank_clerk "Простите, Мэм?"

    img 1660
    m "Я говорю почему эти данные не были предоставлены моему секретарю?"

    "Почему я должна ездить."

    "Тратить свое время?"

    img 1661
    m "СКАЖИТЕ МНЕ??"

    img 1662
    bank_clerk "Простите, Мэм."
    "На ваших сотрудников закончилась доверенность."
    "Вам необходимо оформить новую и..."
    menu:
        "ВЫ ОБНАГЛЕЛИ В КОНЕЦ!":
            $ clerksOffended = True
            img 1663
            m "ЭТО НЕ ДОВЕРЕННОСТЬ ЗАКОНЧИЛАСЬ!"
            call bitch(2, "bank_office1")

            "ЭТО ВЫ ОБНАГЛЕЛИ В КОНЕЦ!"
            "Я держу свои деньги в вашем банке!"
            "А вы меня дурите какими-то доверенностями!"
            img 1664
            bank_clerk "Мэм, простите, но..."
            img 1665
            m "Никаких простите!"
            "Твое имя?"
            "БЫСТРО!"
            img 1666
            bank_clerk "Мэм, но..."
            img 1665
            m "БЫСТРО Я СКАЗАЛА!!"
            img 1667
            bank_clerk "Patricia Dolares, Мэм."
            img 1668
            m "Отлично, я запомню."
            "Я подам на тебя жалобу, Patricia."
            img 1669
            bank_clerk "Мэм, пожалуйста, не надо!"
            "Я работаю здесь недавно."
            "У меня будут проблемы из-за этого."
            img 1670
            m "Это даже лучше!"
            "Спасибо за информацию!"
            img 1671
            bank_clerk "Мне очень жаль, Мэм."
            img 1672
            m "Мне не жаль!"
            "До свидания!"
            img 1673
            bank_clerk "До свидания, Мэм..."
            img 1674
            w
            $ autorun_to_object("bank_office", "bank_office_thinking1")

        "Я понимаю...":
            img 1669
            m "Ладно, я понимаю."
            "Это недосмотр кого-то из моего персонала."
            "Вы ни при чем."
            img 1652
            bank_clerk "Спасибо, Мэм!"
            "Я рада что Вы понимаете..."
            img 1669
            m "До свидания!"
            img 1652
            bank_clerk "До свидания, Мэм..."

    music casualMusic
    $ bankOfficeState = 2

    $ add_objective("goto_office1", _("Ехать в Офис"), c_pink, 20)
    $ drivingPlacePlannedArray["Steve_Office"] = "steve1_drive1"
    $ focus_map("Teleport_Monica_Office", "steve1_drive1_discard_others")
    $ mapSubstMonicaOfficeToSteve = True

#    $ unfocus_map()
    call refresh_scene_fade()
    return

label bank_office_thinking1:
    mt "Я задала отличную трепку."
    "У меня бы даже поднялось настроение, если бы ни..."
    "Так! Стив!!!"

    return

label bank_office_talk2:
    img 1671
    with fade
    bank_clerk "Добрый день, Мэм!"
    "Чем могу Вам помочь?"
    m "Ты мне уже ничем не поможешь!"
    "Скоро тебя здесь не будет!"
    call refresh_scene_fade()
    return

label bank_office_talk2_not_offended:
    img 1652
    with fade
    bank_clerk "Добрый день, Мэм!"
    "Чем могу Вам помочь?"
    m "Спасибо, пока ничего не надо..."
    call refresh_scene_fade()
    return
