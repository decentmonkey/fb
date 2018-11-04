label monica_office_tea_drive1(target_scene):
    sound snd_car_turn_on
    m "Поехали в офис."
    fred "Хорошо, Мэм."

    sound snd_car_engine
    music Walking_Sax2
    imgl 1675
    with fadelong
    menu:
        "Надоели эти пешеходы!":
            call bitch(1, "monica_office_tea_drive1")
            m "Надоели эти пешеходы!"

            "Как было бы здорово если бы их не было!"

            "Да, Фрэд?"

            imgr 1676
            fred "Но Мэм."

            "Когда мы выходим из машины, мы тоже становимся пешеходами."

            imgl 1518
            m "Не говори ерунды, Фрэд!"

            "Я хожу только от машины до офиса."

            "Это бедняки бродят по улицам."

            "Переходят дороги."

            "Я считаю надо вообще запретить переходить улицу!"

            fred "Мэм, но как же тогда людям пересекать улицу?"

            m "Это не мое дело."

            call bitch(1, "monica_office_tea_drive2")
            "Пусть рождаются и умирают на своей стороне дороги."

            "И не мешают мне ездить!"

            imgr 1517
            fred "..."

        "Молча ехать и смотреть инстаграм.":
            pass
    $ changeDayTime("evening")
    music casualMusic
    return

label monica_office_tea_enter_secretary:
    $ remove_inventory("phone", 1)
#    $ add_inventory("phone", 1, True)
    return

label monica_office_tea_talk1:
#    $ add_objective("goto_office_for_tea", _("Ехать в свой офис"), c_green, 20)
    $ remove_objective("goto_office_for_tea")
    $ add_objective("tea_with_secretary", _("Попить чай с секретаршей"), c_pink, 20)

    music RnB4_100
    img 1829
    secretary "Добрый вечер, Миссис Бакфетт!"

    img 1830
    mt "Вечер?"

    "Ах, ну да."

    "Уже вечер!"

    "Я столько времени потеряла из-за этого Стива!"

    img 1831
    "Добрый вечер, моя дорогая."

    "Что нового?"

    img 1832
    secretary "Мэм, у Вас несколько новых факсов."

    "Я обработала большинство из них."

    "Но есть пара, на которые Вам надо взглянуть."

    img 1833
    m "Ох."

    "Дорогая моя."

    "Я так устала от работы сегодня."

    "Пойду к себе."

    "Приходи ко мне в кабинет."

    "Попьем чай."

    img 1834
    secretary "Одну минуту, Миссис Бакфетт!"

    "Сейчас заварю чай и принесу его к Вам!"

    music casualMusic

    $ autorun_to_object("monica_office_cabinet_table", "monica_office_tea_talk2")
    return

label monica_office_tea_talk2:
    music RnB4_100
    img 1835
    with fadelong
    secretary "Миссис Бакфетт."

    "Пожалуйста, Ваш чай."

    img 1836
    m "Спасибо, моя дорогая."

    img 1837
    secretary "У Вас сегодня было много дел?"

    img 1838
    m "Да."

    "Ты не представляешь какие люди меня окружают."

    "Вокруг все лжецы и обманщики."

    img 1839
    secretary "..."

    img 1840
    m "Я была сегодня у Стива."
    "Представляешь, у него там работают девушки, которые явно не соответствуют занимаемым должностям."
    "Я определенно уверена в том каким способом они получили эти должности."

    img 1841
    secretary "Ох, Миссис Бакфетт."

    "Я ничуть не удивлена."

    "В наше время старые моральные ценности почти ничего не значат."

    "Я всю жизнь прожила следуя строгим моральным принципам."

    "И проживу оставшуюся так же."

    "Я добилась своей должности работая день и ночь."

    "Без устали."

    img 1842
    "Я бы никогда не позволила себе переступить моральную черту."

    "И получить должность за счет близости с чужим мужчиной."

    img 1843
    "..."

    "....."

    img 1844
    "Я бы никогда и ни за что не разделась ни перед кем."

    img 1845
    with dissolve
    "Если честно, Миссис Бакфетт."
    "Я даже осуждаю то что происходит у нас в студии."

    img 1846
    "Этот Алекс."

    "Ваш фотограф."

    "У меня такое чувство, что его интересует не тонкая женская красота."

    "А интересуют интимные места и позы."

    "Дай ему волю, он бы превратил наш журнал в порнографический."

    img 1847
    m "Да, моя дорогая."

    "Я знаю."

    if alexPhotographOffended1 == True:

        "Я вчера сделала ему замечание."

        "Если еще раз заметишь что-то подобное, то скажи мне."

        img 1848
        "Я сразу уволю его."
    else:
        m "Дорогая, это лучший фотограф, которого можно найти за деньги."
        "Однако он пообещал мне что будет внимательнее следить за своим поведением."
        "Так что приглядывай за ним."

    img 1849
    secretary "Хорошо, Миссис Бакфетт."

    "Я прослежу за ним."

    img 1850
    m "Спасибо, моя дорогая."

    "Без тебя я бы не справилась с нашей компанией."

    img 1851
    secretary "Миссис Бакфетт."

    img 1852
    "Я всегда буду Вам верна."

    img 1853
    m "Спасибо, моя дорогая."

    "А я обещаю тебе что мы никогда не скатимся во что-то неприличное."

    "Хотя, ты знаешь."

    "Сейчас весь мир скатывается в непотребство."

    img 1854
    "Но мы будем держать свой курс!"

    img 1855
    secretary "Спасибо, Миссис Бакфетт!"

    "Я бы не смогла работать в компании, где не ценят высокую мораль!"

    img 1856
    m "Вкусный чай."

    "Спасибо!"

    secretary "Всегда пожалуйста, Миссис Бакфетт!"

    m "Хорошо, можешь идти."

    "Мне надо позвонить Дику."

    secretary "..."

    img 1858
    with fadelong
    m "..."

    music Stealth_Groover
    "Так, а где мой телефон?"

    img 1859
    "Здесь его нет."

    img 1860
    "И здесь тоже."

    "..."

    "Хм..."

    img 1861
    "Куда я его дела?"

    "..."

    "Моя дорогая, я куда-то дела свой телефон."

    "Может я выронила его где-то здесь."

    "Поищи, пожалуйста!"

    music Jazz_club1_130
    img 1862
    secretary "Да, Миссис Бакфетт!"

    "Я его найду!!"

    menu:
        "Искать телефон.":
            pass
        "Показать подсказку.":
            img help1_16
            with fadelong
            help "Телефон на полу при входе в офис..."

    call question_helper_enable("question_office_tea_lost_phone")
    $ monicaOfficeDay2TeaPlanned = False
    $ remove_objective("tea_with_secretary")
    $ add_objective("find_phone", _("Найти телефон!"), c_orange, 20)

    sound highheels_run1
    show screen notify(_("Секретарша убежала искать телефон..."))

    $ monicaOfficeDay2PhoneLost = True
    $ autorun_to_object("monica_office_secretary", "monica_office_tea_secretary_searching_phone")
    call refresh_scene_fade()
    return

label monica_office_tea_secretary_searching_phone:
    if day != 2:
        return
    img 1867
    with fade
    secretary "Миссис Бакфетт!"
    "Я не могу найти Ваш телефон!"
    "Простите!"
    if monicaOfficeDay2PhoneLost == True:
        m "Продолжай искать!"
#        $ autorun_to_object("monica_office_secretary", "monica_office_tea_secretary_searching_phone")
    else:
        m "Не волнуйся, моя дорогая."
        "Я нашла его."
    return

label monica_office_tea_phone(obj_name, obj_data):
    call question_helper_disable()
    if obj_data["action"] == "l":
        mt "Ага!"
        "Вот ты где!"
        return
    if obj_data["action"] == "h":
        img 1863
        with fade
        mt "Ага!"
        img 1864
        "Вот ты где!"
        $ add_inventory("phone", 1, True)
        $ monicaOfficeDay2PhoneLost = False
        $ autorun_to_object("monica_office_entrance", "monica_office_tea_phone_talk_after_found")
        $ autorun_to_object("monica_office_secretary", "monica_office_tea_secretary_searching_phone")
        $ monicaOfficeSecretaryAtDesk = True
        music casualMusic
        call refresh_scene_fade()
    return

label monica_office_tea_phone_talk_after_found:
    img 1865
    with fadelong
    mt "Что-то у меня уже нет никакого настроения звонить Дику."
    "Устроил мне вчера дурацкое свидание..."
    "..."

    img 1866
    "Кстати!"

    "Я же собиралась вернуть платье!"

    "Надо вернуть его скорее пока не закрылся тот дурацкий магазин."

    $ remove_objective("find_phone")
    $ add_objective("return_dress", _("Вернуть платье в магазин!"), c_pink, 20)
#    $ drivingPlacePlannedArray["Cloth_Shop"] = "dress_return_drive1"
    $ drivingPlacePlannedArray["Street_Corner"] = "dress_return_drive1"

    $ mapSubstClothingShopToStreetCorner = True
    call refresh_scene_fade()

    return
