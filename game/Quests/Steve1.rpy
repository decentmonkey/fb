default monicaSteveDogOffended = False

label steve1_drive1_discard_others(obj_name, obj_data):
    m "Мне надо ехать в свой офис!"
    "Надо разобраться в бумагах Стива!"
    return
label steve1_drive1(target_scene):
    sound snd_car_engine
    imgl 1675
    with fadelong
    m "Фрэд!"

    "Быстро в офис!"

    imgr 1676
    fred "Принято, Мэм!"

    imgl 1677
    m "Позвоню этому уроду."

    sound snd_phone1
    $ renpy.pause(2.0)
    sound snd_phone_short_beeps
    $ renpy.pause(2.0)
    sound snd_phone1
    $ renpy.pause(2.0)
    sound snd_phone_short_beeps

    imgl 1678
    with fade
    sound snd_car_engine
    music Indo_Rock
    m "Фрэд!"

    "Поворачивай!"

    imgr 1676
    fred "Да, Мэм!"
    "Куда мы едем?"

    m "Мы едем к моему партнеру."
    "Стиву."
    fred "Принято, Мэм!"
    $ remove_objective("goto_office1")
    $ add_objective("catch_steve", _("Добраться до Стива"), c_red, 20)

    imgl 1679
    mt "Он сбрасывает мой звонок."
    "Что-ж."
    "Я сама сейчас к нему приеду."

    sound snd_car_engine
    imgl 1680
    with fadelong
    m "Фред!"
    "Твою мать!"
    "Едь быстрее уже!!!"
    "Тормоз!"

    imgr 1676
    fred "Простите, Мэм."
    m "Этот трусливый мешок с дерьмом может сбежать."

    sound snd_phone_ring
    imgl 1681
    with fade
    m "Ага!"
    "Вот ты и попался, мешок с дерьмом!"

    imgl 1682
    dick "Моника?"

    m "Дик?"

    imgl 1683
    "Черт!"

    "Дик, чего тебе??"

    if dickHelpsMoniceSue == True:
        dick "Моника, я хотел тебе сказать что иск на твоего соседа отправлен."
        "Не переживай."
        "Скоро проблема будет решена."
    else:
        dick "Моника, я хотел извиниться перед тобой за прошлый вечер."
        "Ты знаешь, у меня есть идея как все исправить."
        "Могу я рассчитывать снова увидеть тебя?"
    m "Да, Дик, хорошо."
    "Дик, сейчас не до тебя."
    "Я тебе позвоню потом на днях."

    dick "Хорошо, дорогая."

    "Буду ждать."

    imgl 1684
    m "Все, пока."
    $ map_objects["Teleport_Steve_Office"]["state"] = "visible"
    $ unfocus_map()


#    call change_scene("street_steve_office", "Fade_long", "snd_car_engine")
    return

label steve1_secretary_talk1:
    music Pyro_Flow
    img 1686
    with fadelong
    w
    img 1687
    w
    img 1688
    jane "Здравствуйте, Миссис Бакфетт!"

    img 1689
    "Чем могу Вам помочь?"

    img 1690
    m "Аааа..."
    "Джейн."
    "Мелкая подлиза."

    img 1691
    "Я смотрю ты уже пролезла в секретари Стива?"
    "Это тебя повысили или понизили, А?"
    "И как ты здесь оказалась?"

    img 1692
    "Через его член?"

    img 1693
    jane "Миссис Бакфетт!"

    img 1694
    m "Молчать!"
    "И встань когда с тобой разговаривает твой Босс!"

    img 1695
    jane "Но Мэм!"
    "Мой Босс Стив."

    img 1696
    m "Стив моя шестерка."
    "Через меня идут все деньги его компании!"

    img 1697
    "Так что я твой Босс, ку-кол-ка!!"

    img 1698
    "Встать!"

    img 1699
    "..."

    img 1700
    "Так-то лучше."

    img 1701
    "Это что у тебя за дресс код?"

    img 1702
    w
    img 1703
    w
    img 1704
    "Одета как проститутка!"

    img 1705
    "Что это вообще за место?"
    "Это фирма моего младшего партнера или публичный дом?"
    img 1706
    "..."
    "Что молчишь?"
    "Быстро отвечать!"

    img 1707
    jane "Это солидная фирма, Мэм...."
    img 1706
    m "А почему тогда здесь проститутки?"
    "Я всегда считала что проституткам место в борделе, а не в солидной фирме."

    img 1708
    "Как ты считаешь, Джейн?"

    img 1709
    jane "Да, Мэм."
    "Проституткам не место в солидной фирме."

    img 1710
    m "Да?"
    "И почему-же тогда ты здесь находишься?"

    img 1711
    jane "Мэм."
    "Я исправлюсь."
    "В следующий раз Вы меня увидите в строгом деловом костюме."

    img 1712
    m "В следующий раз??"
    "У тебя 30 секунд!"

    img 1713
    "Иначе в следующий раз я тебя здесь уже не увижу!"

    img 1714
    jane "Но Мэм."
    "У меня нет с собой другой одежды."

    img 1715
    m "Почему меня это должно волновать?"

    sound highheels_run2
    music Hidden_Agenda
    img 1716
    with fadelong
    tiffany "Джейн."

    img 1717
    "Какие планы после работы?"

    img 1718
    "Может сходим в клуб?..."

    img 1719
    w
    img 1720
    jane "Чшшш! Тихо!"

    img 1721
    w
    img 1722
    w
    music Pyro_Flow
    img 1723
    w
    img 1724
    w
    img 1725
    tiffany "..."

    img 1726
    "ОЙ!"

    img 1727
    "Миссис Бакфетт!"

    "Здравствуйте!"

    img 1728
    m "Оооо!"
    "А это кто у нас?"

    img 1729
    "Судя по внешнему виду, это напарница по ремеслу!"

    img 1730
    "Что девочки, вместе ходите сниматься в клуб?"

    img 1731
    tiffany "Мэм, я просто зашла..."

    img 1732
    "Передать документы..."

    sound highheels_run2
    img 1733
    "Я уже ухожу..."

    img 1734
    with fade
    w
    img 1735
    with fade
    w
    img 1736
    with fade
    w
    img 1737
    with fade
    w
    img 1738
    with fade
    w
    img 1739
    with fade
    w
    img 1740
    with fade
    w
    img 1741
    with fade
    w
    img 1742
    m "Стоять!!!"

    img 1743
    "Быстро назад!!!"

    sound highheels_short_walk
    img 1744
    "Как тебя зовут?"

    img 1745
    tiffany "Мое имя Тиффани, Мэм."

    img 1746
    m "Что-то я тебя не помню."

    "Давно ты здесь работаешь?"

    img 1747
    tiffany "Третий месяц, Мэм."

    img 1748
    m "И что ты здесь делаешь?"

    "Почему ты уже входишь практически в кабинет к Стиву?"

    img 1749
    "У тебя какие-то особые таланты, А?"

    "Почему ты так быстро поднялась по каръерной лестнице??"

    img 1750
    tiffany "Мэм."

    "У меня хорошее образование и отличное резюме."

    img 1751
    m "А мне сдается единственный быстрый социальный лифт в этой компании -"

    img 1752
    "- Это член Стива!"

    img 1753
    "..."

    img 1754
    "Развел проституток!"

    "Я наведу здесь порядок, не переживайте!"

    img 1755
    tiffany "Мэм..."

    img 1756
    m "Посмотри на себя!"

    "В чем ты одета!"

    img 1757
    m "Все."

    menu:
        "Вас обеих здесь больше не будет.":
            $ steveSecretaryFireOffended = True
            call bitch(1, "steve_secretaryjane_fireoffended") from _call_bitch_86
            img 1758
            "Вас обеих здесь больше не будет."
            img 1759
            m "А теперь быстро вышла отсюда!"

            img 1760
            "Я пойду надирать задницу вашему Боссу!"

        "Я пойду надирать задницу вашему Боссу!":
            img 1759
            m "А теперь быстро вышла отсюда!"
            img 1760
            "Я пойду надирать задницу вашему Боссу!"


    $ steveSecretaryOffended = True
    return

label steve1_secretary_talk2:
    img 1709
    with fade
    jane "Миссис Бакфетт!"
    img 1702
    "Обещаю, я буду соблюдать дресс-код!"
    "Это солидная фирма!"
    if steveSecretaryTalkAfterCatch == False:
        menu:
            "Это уже не имеет значения. Тебя здесь скоро не будет.":
                $ steveSecretaryFireOffended2 = True
                call bitch(2, "steve_secretaryjane_fireoffended2") from _call_bitch_87
                img 1709
                m "Это уже не имеет значения. Тебя здесь скоро не будет."
                steve "Миссис Бакфетт! Пожалуйста!"
                m "Я все сказала..."

            "Я посмотрю на твое поведение.":
                call bitch(-2, "steve_secretaryjane_fireoffended2") from _call_bitch_88
                m "Я посмотрю на твое поведение, девочка."
                "Возможно в этом виноват Стив, а не ты."
                img 1709
                jane "Да, Миссис Бакфетт! Спасибо Вам!!!"

        $ steveSecretaryTalkAfterCatch = True
    return

label steve1_secretary_talk3:
    img 1826
    with fade
    m "Пока-пока."

    jane "До свидания, Миссис Бакфетт."

    img 1827
    m "Прощай, голубок!"

    img 1828
    jane "..."
    return

label steve1_steve_talk1:
    $ remove_objective("catch_steve")
    img 1761
    with fadelong
    w
    img 1762
    with fade
    w
    img 1763
    with fade
    w
    img 1764
    with fade
    m "Ага!"
    "Попался."
    "Мешок с дерьмом!"

    img 1765
    steve "Моника, я..."

    img 1766
    "Я все объясню..."

    img 1767
    m "Брысь из моего кресла!"

    img 1768
    "Живо!"

    call change_scene("steve_office_office_table", "Fade_long") from _call_change_scene_100

    return

label steve1_steve_talk2:
    img 1769
    with fade
    steve "Моника..."
    "Я все объясню..."

    img 1770
    m "Я тебя слушаю, Стив!"

    img 1771
    steve "Моника, я..."
    "В общем..."
    "В общем у нас финансовые трудности."
    "И нам сложно выполнить то о чем мы договорились."
    "О взятии в аренду половины этажа в твоем тауере."

    $ steveOfficeSteveTableStateTalk = 1
    return

label steve1_steve_talk3:
    img 1772
    with fade
    m "Уже половины?"
    "Стив."
    "Речь шла о целом этаже."
    "Откуда половина?"

    img 1773
    steve "..."

    m "..."

    img 1774
    "Стив?"

    img 1775
    steve "Да."

    img 1776
    m "Стив."
    "Почему ты прятался от меня?"
    "Ты меня не уважаешь?"
    "А, Стив?"
    "Ответь-ка мне?"

    img 1777
    with dissolve
    "Ты ведь знаешь что я щелчком пальцев могу перекрыть тебе кислород."

    img 1778
    steve "Да, Моника."
    "Я знаю..."
    "..."
    "......"

    "Моника."

    "Я..."
    "Я......"

    "Я просто..."

    img 1779
    m "Что ты просто, Стив?"

    img 1780
    steve "Моника!"
    "Я боялся тебя!"
    "Я трус!"

    $ steveOfficeSteveTableStateTalk = 2
    return

label steve1_steve_talk4:
    img 1781
    m "Ахахаха!"
    "Хахахаха!"
    "Ну ты рассмешил меня."
    "Я знаю Стив."

    img 1782
    "Знаю что ты трусливый слизняк."

    img 1783
    "Но ты оказывается умеешь быть смелым."
    "У тебя хватило смелости сказать мне правду."

    img 1784
    steve "..."

    img 1785
    m "Хорошо."
    "Ты растопил мою решимость убрать тебя."
    "Поднял мне настроение."

    img 1786
    steve "..."

    img 1787
    m "Итак."
    "Что там у нас с арендой?"
    "Ты понимаешь что этот этаж сейчас пустует?"
    "Мне не нужны пустующие площади."
    "Меня не беспокоят деньги."

    img 1788
    "Пустующие площади вредно для репутации, Стив."
    "Ты понимаешь?"

    img 1789
    steve "Да, Моника."
    "Я понимаю."
    "Смотри."
    "Я предлагаю переделать наш годовой бюджет."
    "Для этого надо согласовать с твоей компанией."
    "У нас освободятся средства."
    "Мы закроем несколько сделок, которые висят."

    img 1790
    "У нас появится солидная прибыль."
    "И мы снимем половину этажа за 200.000 долларов."

    img 1791
    m "За 500.000 долларов, Стив."

    "Половина этажа."

    "Аренда."

    "600.000 за целый."

    img 1792
    steve "400.000 долларов за целый этаж аренды."

    img 1793
    m "500.000 за целый этаж."

    img 1794
    steve "250.000 за половину."

    img 1795
    m "За половину 350.000 долларов."

    img 1796
    steve "350.000 за целый."

    img 1797
    m "За целый 450.000."

    img 1798
    steve "Тогда за половину 300.000."

    img 1799
    m "370.000 за целый."

    img 1800
    steve "Хорошо."

    "Я согласен."

    img 1801
    menu:
        "И еще уволить этих двух сучек на входе к тебе.":
            m "И еще уволить этих двух сучек на входе к тебе."

    sound highheels_run2
    img 1802
    with fade
    m "Стив."
    "Что там за шум?"
    img 1803
    with fadelong
    steve "Тут никого нет."

    $ steveOfficeSteveTableStateTalk = 3
    $ steveOfficeSteveTableState = 1
    return
label steve1_steve_talk5:

    img 1804
    with fade
    steve "Моника, кого ты имеешь ввиду уволить?"
    "Каких двух сучек?"

    img 1805
    m "Одна твоя секретарь Джейн."

    steve "А вторая?"

    m "Вторая какая-то миловидная стерва."
    "Как ее зовут?.."

    "..."

    "....."
    img 1806
    "Тиффани!"

    "Кстати, чем она вообще занимается?"

    img 1807
    steve "Она обрабатывает отчеты."
    "Моника.
    Что она тебе сделала?"

    img 1808
    steve "Стив."

    "За 370.000 долларов ты не должен задавать вопросы."

    img 1809
    steve "Но Моника, в нашей компании трудятся только высокоморальные люди."

    "Тут никто не позволяет себе лишнего."

    img 1810
    m "Не ври мне, Стив."

    "Что одна что другая попали сюда через твой член."

    img 1811
    img 1812
    steve "Моника, я клянусь тебе!"

    "Могу поклясться своей мамой!"

    "Мамма-миа!"

    "У меня нет близости ни с одной из этих невинных девушек!"

    img 1813
    m "450.000 долларов."

    img 1814
    steve "Хорошо, Моника."

    "Я понял."

    "350.000 и я увольняю Тиффани и Джейн."

    img 1815
    m "Ладно, пусть будет по твоему."

    img 1816
    menu:
        "Если ты мне солгал, то ты отсосешь у собаки.":
            $ monicaSteveDogOffended = True
            m "Но я запомню твою клятву."


            call bitch(4, "steve_dog_offend") from _call_bitch_89
            "Если ты мне солгал, то ты отсосешь у собаки."

            img 1817
            steve "Моника!"

            "Ты что?"

            "Что ты такое говоришь?"

            img 1818
            m "Ничего."

            "Просто придумала самое омерзительное наказание за твою ложь."

            "Так ты согласен?"

            img 1819
            "Ведь если ты невиновен, тебе нечего бояться?"

            img 1820
            with fadelong
            steve "Хорошо, Моника."

            "Я согласен."

        "Но я запомню твою клятву.":
            m "Но я запомню твою клятву."
            img 1820
            with fadelong
            steve "Хорошо, Моника."


    img 1821
    m "Вот и все."

    "Ну..."

    "Я пошла."

    img 1822
    with fadelong
    m "Я разрешаю тебе пока посидеть в моем кресле, Стив."

    steve "Спасибо, Моника."

    $ add_objective("goto_office_for_tea", _("Ехать в свой офис"), c_green, 20)
    $ autorun_to_object("street_steve_office", "steve1_end_monica_thinking")
    $ autorun_to_object("monica_office_entrance", "steve1_scene1_1")
    $ steveOfficeSteveTableStateTalk = 4
    $ steveOfficeSteveState = 2
    return


label steve1_steve_talk6:
    img 1824
    with fadelong
    m "Ты помнишь наш уговор, Стив?"
    steve "Да, Моника!
    Я помню..."
    return

label steve1_end_monica_thinking:
    imgl Dial_Monica_BusinessCloth2_1
    mt "Теперь я довольна."

    "Как же мне такие вещи поднимают настроение!"

    "Ухх!!"

    "..."

    "Теперь пора в свой офис."

    "Где там Фред?"

    $ drivingPlacePlannedArray["Monica_Office"] = "monica_office_tea_drive1"
    $ autorun_to_object("monica_office_secretary", "monica_office_tea_enter_secretary")
    $ monicaOfficeDay2TeaPlanned = True
    return


label steve1_secretary_talk4:
    if janeTiffanyFirePlanned == True:
        img 1702
        with fadelong
        m "Ага!"
        "Вот значит как!"
        "Ну все, сучка Джейн, тебе конец!"
        "Где Стив?"
        img 1709
        with fade
        jane "Миссис Бакфетт!"
        "Стива сейчас нет."
        "Пожалуйста, это он сказал оставить эту одежду на мне!"
        m "Это еще и лучше."
        "Стив пойдет вслед за вами."
        "Мне понравился его стул. Пойду посижу."
        "А попозже сегодня еще заеду к вам."
        "Ты ведь не против, Джейн?"
        img 1702
        jane "Нет, Миссис Бакфетт! Я не против!"
        m "Замечательно, деточка."

    else:
        img 1709
        with fade
        jane "Миссис Бакфетт!"
        img 1702
        "Обещаю, я буду соблюдать дресс-код!"
        "Это солидная фирма!"
        m "Где Стив?"
        "У меня к нему есть вопросы."
        jane "Миссис Бакфетт!"
        "Стива нет на месте. Он скоро приедет!"
        "Мне понравился его стул. Пойду посижу."
        "А попозже сегодня еще заеду к вам."
        "Ты ведь не против, Джейн?"
        img 1702
        jane "Нет, Миссис Бакфетт! Я не против!"
        m "Замечательно, деточка."
    $ add_objective("go_to_steve_after", _("Заехать к Стиву немного позже."), c_blue, 25)

    return

label steve1_scene1_1: #разговор с Джейн и Тиффани

    music Hidden_Agenda
    call textonblack(_("ТЕМ ВРЕМЕНЕМ...")) from _call_textonblack_2
    img black_screen
    with Dissolve(1)
#    img
#    with fadelong
    # Джейн заходит ко Стиву
    img 4854
    w
    img 4855
    w
    img 4856
    jane "Стив!"
    img 4857
    steve "О, моя милая Джейн!"
    "Хорошо что ты зашла."
    img 4858
    jane "Стив, скажи, что это значит?"
    img 4859
    steve "Джейн, что ты имеешь ввиду?"
    img 4860
    jane "Эта Бакфетт, она унизила меня только что."
    img 4861
    steve "..."
    img 4862
    jane "Более того, я думаю она собирается уволить меня."
    img 4863
    "Она ведь говорила об этом с тобой, Стив?"
    img 4864
    steve "Нет, Джейн, она не говорила об этом. Наоборот, она хорошо отзывалась о тебе!"
    img 4865
    jane "Стив, ты мне врешь! Я все слышала!"
    img 4866
    steve "Ты подслушивала?"
    img 4867
    jane "Стив, мы находимся в таких отношениях, когда я имею право следить за тем что происходит!"
    img 4868
    steve "Ты про что, Джейн?"
    img 4869
    with fadelong
    jane "Про наши планы! Надеюсь ты не забыл?!"
    img 4870
    steve "Планы?"
    img 4871
    jane "Да, Стив! Наши планы!"
    img 4872
    "Не забудь, какие документы проходят через меня."
    img 4873
    "Я же вижу все твои темные делишки! И на многих документах стоят мои подписи, как секретаря!"
    img 4874
    "И если тебя возьмут за мягкое место, Стив, то могут взять и меня."
    img 4875
    "А, зная тебя, я не удивлюсь, если стану козлом отпущения!"
    img 4876
    "Потому если ты хочешь чтобы все дальше шло как идет."
    img 4877
    "Чтобы я закрывала глаза на твои делишки. Чтобы я ходила при тебе как проститутка. И все остальное."
    img 4878
    "И никакая Бакфетт или другая сучка не смогла бы уволить меня!"
    img 4879
    "То давай поженимся, как и собирались. Наши отношения станут законными и отвечать, если что, будешь за все ты."
    img 4880
    steve "Прибыль тоже будет общая. Да, Джейн?"
    "Как и доля в компании..."
    img 4881
    jane "Конечно, Стив!" #ехидно улыбается
    img 4880
    steve "..."
    img 4882
    jane "..."
    img 4883
    with fadelong
    jane "Ты передумал, милый? Ты меня больше не любишь?"
    img 4884
    jane "Ты уже не хочешь жениться на мне?"
    img 4885
    with fadelong
    steve "Что ты, Джейн! Я тебя очень люблю! Иди ко мне моя малышка."
    img 4886
    "Дай я поцелую тебя..."
    img 4887
    w
    img 4888
    w
    img 4889
    w
    sound snd_fabric1
    img 4890
    with fadelong
    w
    img 4891
    steve "Малышка, поцелуй меня скорее, закрепим наш союз..."
    img 4892
    w
    img 4893
    w
    img 4894
    w
    img 4896
    with fadelong
    w
    img 4895
    music Loved_up
    jane "Хорошо, милый..."

    img 4896
    w
    img 4897
    w
    img 4898
    w
    img 4899
    w
    img 4900
    w
    img 4901
    w
    #video


    # делает минет
    img 4903
    steve "Мммм.. даа.."
    scene black
    image videoSteve_Jane_Blowjob_1_1 = Movie(play="video/Steve_Jane_Blowjob_1_1.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_1
    wclean
    img 4904
    w
    scene black
    image videoSteve_Jane_Blowjob_1_2 = Movie(play="video/Steve_Jane_Blowjob_1_2.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_2
    wclean
    img 4905
    w
    scene black
    image videoSteve_Jane_Blowjob_1_3 = Movie(play="video/Steve_Jane_Blowjob_1_3.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_3
    wclean
    img 4906
    "Вот так, давай... соси..."
    scene black
    image videoSteve_Jane_Blowjob_1_4 = Movie(play="video/Steve_Jane_Blowjob_1_4.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_4
    wclean
    img 4907
    w
    scene black
    image videoSteve_Jane_Blowjob_1_5 = Movie(play="video/Steve_Jane_Blowjob_1_5.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_5
    wclean
    img 4908
    "Соси... свою долю в компании... давай..."
    scene black
    image videoSteve_Jane_Blowjob_1_6 = Movie(play="video/Steve_Jane_Blowjob_1_6.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_6
    wclean
    img 4909
    w
    scene black
    image videoSteve_Jane_Blowjob_1_7 = Movie(play="video/Steve_Jane_Blowjob_1_7.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_7
    wclean
    scene black
    image videoSteve_Jane_Blowjob_1_8 = Movie(play="video/Steve_Jane_Blowjob_1_8.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_8
    wclean
    scene black
    image videoSteve_Jane_Blowjob_1_9 = Movie(play="video/Steve_Jane_Blowjob_1_9.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_9
    wclean
    img 4910
    "Вот так... дааа..."
    scene black
    image videoSteve_Jane_Blowjob_1_10 = Movie(play="video/Steve_Jane_Blowjob_1_10.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_10
    wclean
    scene black
    image videoSteve_Jane_Blowjob_1_11 = Movie(play="video/Steve_Jane_Blowjob_1_11.mp4", fps=30)
    show videoSteve_Jane_Blowjob_1_11
    wclean

    img 4911
    w

    # заходит Тиффани
    music Groove2_85
    img 4912
    with fadelong
    w
    img 4913
    tiffany "Ой!"
    img 4914
    w
    img 4915
    "Мистер Стив! Простите!"
    "Я зашла передать документы..."
    img 4916
    w
    img 4917
    jane "Упс!"
    img 4918
    steve "Тиффани, обожди минуту."
    img 4919
    "Я сейчас освобожусь."
    img 4920
    tiffany "Хорошо, Мистер Стив!"
    "Я подожду у рабочего стола Джейн."
    sound snd_fabric1
    img 4922
    with fadelong
    jane "..." #встает и вытирает лицо
    img 4921
    jane "Стив. Я давно хотела спросить тебя."
    img 4923
    steve "Да, милая, можешь спрашивать все что хочешь. Мы уже почти семья."
    img 4924
    jane "Почему Тиффани так одета. Это мне что-то напоминает про твои ко мне просьбы."
    img 4925
    steve "Я не знаю, Джейн!" #мутный и хитрый
    img 4926
    jane "Ты не знаешь?"
    img 4927
    steve "Нет, она же твоя подружка. Я думал ты знаешь..."
    img 4928
    w
    img 4929
    jane "Ты не просил ее этого делать, правда ведь Стив?" #пристально смотрит
    img 4930
    steve "Конечно нет, Джейн! Ты же знаешь что для меня есть только ты!"
    img 4931
    "Может быть Тиффани сама флиртует со мной... Но я даже не смотрю на нее, Джейн!"
    img 4932
    "Может быть она завидует тебе, пытается равняться на тебя."
    "Начинает подражать..."
    img 4933
    music Loved_up
    "Но это бесполезно, ты ведь знаешь меня!"
    img 4934
    w
    img 4935
    w
    img 4936
    w
    img 4937
    w
    img 4938
    w
    img 4939
    jane "Чмок!"
    img 4940
    jane "Хорошо, милый. Я пошла."
    img 4941
    "Сегодня я поеду подбирать свадебное платье. А от тебя я жду даты свадьбы, решай это скорее!"
    steve "Да, милая, конечно!"
    img 4942
    w

    #jane уходит

    #fade
    #разговор у стола джейн и тиффани
    music Indo_Rock
    img 4943
    with fadelong
    w
    img 4944
    with fade
    w
    img 4945
    w
    img 4946
    w
    img 4947
    tiffany "О, Джейн! Вы закончили со Стивом! Я могу войти?"
    img 4948
    jane "Да, Тиффани, можешь заходить."
    img 4949
    "Я сегодня не поеду с тобой в клуб. Мне надо выбирать свадебное платье."
    img 4950
    "Присоединишься ко мне?"
    img 4951
    tiffany "Джейн, конечно! Я очень рада за вас!"
    img 4952
    "Я с удовольствием присоединюсь к тебе! Ты моя лучшая подруга!"
    img 4953
    "Как я могу пропустить такое мероприятие, как выбор подвенечного платья!"
    img 4954
    jane "Хорошо, Тиффани, уже почти конец рабочего дня."
    "Как освободишься, скажи мне. Я уже свободна."
    img 4955
    tiffany "Хорошо, Джейн! Чмоки!"

    #заходит ко стиву, стив сидит за столом на что-то отвлечен

    music Hidden_Agenda
    img 4956
    with fadelong
    w
    img 4957
    with fade
    w
    img 4958
    with fade
    tiffany "Мистер Стив!"
    img 4959
    steve "Да, Джейн? Ты хотела передать документы?"
    img 4960
    tiffany "Мистер Свит! На самом деле я пришла поговорить с вами о Миссис Бакфетт!"
    img 4961
    steve "Я тебя слушаю, говори."
    img 4962
    tiffany "Она собирается уволить меня!"
    "Она мне практически так и сказала!"
    img 4963
    steve "Она сказала именно так? Но за что?"
    ##
    if steveSecretaryFireOffended == True:
        img 4962
        tiffany "Да, сказала именно так!"
    else:
        img 4962
        tiffany "Не совсем так, но она намекала на это!"
    img 4964
    steve "За что она хочет уволить тебя?"
    img 4965
    tiffany "За мой внешний вид!"
    img 4966
    steve "?" #глупое лицо, косит под дурачка, улыбается и разводит руками
    img 4967
    tiffany "Мистер Стив! Это вы заставляете меня носить это!"
    img 4968
    #стив встает и подходит сбоку к Тиффани
    steve "Тиффани, моя хорошая. Я ведь не приказывал тебе этого делать, я поднял тебе зарплату и ты решила меня отблагодарить..."
    "Разве нет?"
    img 4969
    tiffany "Мистер Стив! Вы недвусмысленно намекнули мне о том, благодаря чему запрплата будет повышена." #лисичка
    img 4970
    "И вы повысили ее после того как я выполнила ваши намеки."
    img 4971
    "А теперь из-за этого я могу лишиться работы!"
    img 4972
    steve "..."
    img 4973
    "Мистер Стив! Вы знаете, что с таким резюме как у меня, я смогу устроиться в любую компанию, где будет дальнейший карьерный рост!"
    img 4974
    steve "..."
    img 4975
    steve "О да! Тиффани!" #лапает за попу
    sound Jump2
    img 4976
    with fadelong
    w
    img 4977
    with fade
    w
    img 4978
    "С таким резюме у тебя открыты все дороги... И в этой компании тоже..."
    img 4979
    tiffany "И в этой компании тоже?"
    img 4980
    steve "Да, Тиффани... Я давно напоминал тебе о повышении.." #продолжает лапать
    img 4981
    w
    img 4982
    steve "Не знаю почему ты говоришь мне каждый раз слово НЕТ..."
    img 4983
    music Groove2_85
    tiffany "Потому что вы женитесь на Джейн."
    "А у меня есть моральные принципы, которые запрещают мне делать то что вы просите в данных обстоятельствах."
    img 4984
    with fadelong
    steve "Женюсь?? Кто тебе сказал это?"
    tiffany "Мне сказала это Джейн."
    #стив ошарашен
    img 4985
    steve "..."
    img 4986
    tiffany "Ведь это правда?"
    img 4987
    steve "Тиффани.. я... у нас правда есть кое-какие планы с Джейн... но..."
    img 4988
    tiffany "???"
    img 4989
    music Hidden_Agenda
    steve "Тиффани, ты такая красивая!"
    sound Jump2
    img 4990
    "Знала бы ты как я хочу тебя!" #снова лапает ее
    img 4991
    tiffany "Больше чем Джейн?"
    img 4992
    steve "Конечно больше! Раздевайся скорее!" #лапает
    img 4993
    tiffany "Хорошо, но при одном условии!"
    sound snd_fabric1
    img 4994
    with fadelong
    w
    img 4995
    steve "Проси все что хочешь, я не могу удержаться. Я тебя возьму прямо здесь! Любимая Тиффани!" #стив стоит с опущенными штанами с членом
    img 4996
    tiffany "Вы поднимаете мне зарплату в два раза..." #тиффани поворачивается к нему
    steve "Хорошо, Тиффани! Скорее, возьми его!"
    img 4997
    w
    img 4998
    w
    img 4999
    tiffany "Вы защищаете меня от этой сучки, Бакфетт!"
    img 5000
    steve "Хорошо, Тиффани, я договорюсь с ней. Она не тронет тебя."
    img 5001
    "Скорее возьми его в ротик!"
    img 5002
    music Groove2_85
    tiffany "И последнее..." #берет его за член
    img 5003
    w
    img 5004
    w
    img 5005
    w
    img 5006
    tiffany "И последнее..." #берет его за член
    img 5007
    w
    img 5008
    "Я занимаю место Джейн..."
    img 5009
    steve "..." #ошарашен
    img 5010
    tiffany "Подумайте, Мистер Стив..."
    img 5013
    w
    img 5011
    tiffany "Можете не торопиться!" #щелкает его по члену
    img 5012
    with dissolve
    w
    img 5014
    with fade
    w
    img 5015
    with fade
    w
    img 5016
    with fade
    w
    img 5017
    with fade
    w
    img 5018
    with fade
    w
    img 5019
    with fade
    w
    img 5020
    with fade
    w
    img 5021
    with fade
    w
    img 5022
    steve "..."
    #тиффани сексуально уходит
    #стив смотрит ей вслед со смущением и злостью

    #fade
    #тиффани и джейн у стола джейн
    img 5023
    music Indo_Rock
    with fadelong
    jane "Ты передала документы? Все хорошо?"
    img 5024
    w
    img 5025
    tiffany "Да, Джейн!" #улыбается веселая
    "Я свободна на сегодня!"
    img 5026
    "Поехали скорее выбирать тебе платье!"
    img 5027
    jane "Хорошо, Тиффани. Я сейчас сообщу Боссу и особожусь. Жди меня внизу!"
    img 5028
    tiffany "Хорошо, Джейн! Поторопись! Мне показалось что Босс сегодня немного злой."
    img 5029
    jane "Я не боюсь его злости, Тиффани. Я знаю подход к нему!"
    img 5030
    tiffany "О, Джейн! Конечно! Ты моя лучшая подруга."
    img 5031
    jane "Ты тоже моя лучшая подруга, Тиффани! Увидимся через 10 минут!"
    img 5032
    tiffany "Пока! Чмоки!"

    #fade
    #выходит Стив
    img 5033
    with fadelong
    jane "Стив, я уже все закончила, так что я пойду. Мы с Тиффани поедем выбирать мне свадебное платье."
    img 5034
    steve "Конечно, Джейн! Ты сейчас пойдешь."
    img 5035
    jane "Стив! Что ты делаешь???"
    img 5036
    w
    img 5037
    with dissolve
    w
    img 5038
    w
    img 5039
    with fade
    jane "Стив! Что ты делаешь???"
    img 5040
    steve "Проверка соблюдения дресс-кода!"
    img 5041
    w
    img 5042
    w
    img 5043
    w
    img 5044
    jane "Я все соблюдаю, Стив!"
    img 5045
    jane "Стив! Мне надо идти! Я тороплюсь!"
    steve "Конечно, Джейн! Ты сейчас пойдешь."
    #хватает ее, поднимает и поворачивает руками на стол
    img 5046
    "Но прежде ты исполнишь супружеский долг!"
    menu:
        "Ахххх..":
            img 5049
            jane "Ахххх.."
            # секс стива и джейн
            img 5048
            w
            img 5050
            jane "Нет, Стив! Он слишком большой!"
            img 5051
            jane "Только после свадьбы!"

            #video
            scene black
            image videoSteve_Jane_Sex_1_1 = Movie(play="video/Steve_Jane_Sex_1_1.mp4", fps=30)
            show videoSteve_Jane_Sex_1_1
            wclean
            scene black
            image videoSteve_Jane_Sex_1_2 = Movie(play="video/Steve_Jane_Sex_1_2.mp4", fps=30)
            show videoSteve_Jane_Sex_1_2
            wclean
            scene black
            image videoSteve_Jane_Sex_1_3 = Movie(play="video/Steve_Jane_Sex_1_3.mp4", fps=30)
            show videoSteve_Jane_Sex_1_3
            wclean
            scene black
            image videoSteve_Jane_Sex_1_4 = Movie(play="video/Steve_Jane_Sex_1_4.mp4", fps=30)
            show videoSteve_Jane_Sex_1_4
            wclean
            scene black
            image videoSteve_Jane_Sex_1_5 = Movie(play="video/Steve_Jane_Sex_1_5.mp4", fps=30)
            show videoSteve_Jane_Sex_1_5
            wclean
            scene black
            image videoSteve_Jane_Sex_1_6 = Movie(play="video/Steve_Jane_Sex_1_6.mp4", fps=30)
            show videoSteve_Jane_Sex_1_6
            wclean
            scene black
            image videoSteve_Jane_Sex_1_7 = Movie(play="video/Steve_Jane_Sex_1_7.mp4", fps=30)
            show videoSteve_Jane_Sex_1_7
            wclean
            scene black
            image videoSteve_Jane_Sex_1_8 = Movie(play="video/Steve_Jane_Sex_1_8.mp4", fps=30)
            show videoSteve_Jane_Sex_1_8
            wclean
            scene black
            image videoSteve_Jane_Sex_1_9 = Movie(play="video/Steve_Jane_Sex_1_9.mp4", fps=30)
            show videoSteve_Jane_Sex_1_9
            wclean
            scene black
            image videoSteve_Jane_Sex_1_10 = Movie(play="video/Steve_Jane_Sex_1_10.mp4", fps=30)
            show videoSteve_Jane_Sex_1_10
            wclean
            scene black
            image videoSteve_Jane_Sex_1_11 = Movie(play="video/Steve_Jane_Sex_1_11.mp4", fps=30)
            show videoSteve_Jane_Sex_1_11
            wclean


            img 5052
            steve "АААааррргххх!!!"
            img 5053
            steve "Аааааа!!!"
            img 5054
            jane "Нет, Стив! Не в меня!!!"
            steve "АААааррргххх!!!"
            img 5055
            with fadelong
            steve "Все, детка!"
            img 5056
            steve "Можешь идти!"
            img 5057
            w
            img 5058
            steve "Рабочий день закончен..."

        "Только после свадьбы, Стив!":
            img 5047
            jane "Только после свадьбы, Стив!"

    call refresh_scene_fade() from _call_refresh_scene_fade_9
    music Mandeville
    return
