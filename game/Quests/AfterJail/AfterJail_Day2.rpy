label afterJailDay2_clothShopStreet1:
    mt "ЧЕРТ! ОПЯТЬ ЭТОТ ДОЖДЬ!!!"
    "Надо быстрее идти к Дику!"
    "Это все невыносимо затянулось!"
    "Улица, дождь!"
    "Это платье!"
    "Мне уже надоело носить одно и то же платье!"
    "ЧЕРТ! И у меня нет трусиков!"
    "Проклятье!"
    "Многие поплатятся за все это! Очень скоро!"
    "Клянусь!"
    $ dickReceptionStage = 2
    $ autorun_to_object("street_dick_office", "afterJailDay2_dickofficestreet1")
    return

label cashier_afterjail_day2_talk1:
    if clothShopCashierFirstNightOffended == False:
        img 1913
        with fade
        cashier "Мэм."
        "Прошу прощения еще раз..."
        "Впредь я всегда буду внимательнее к покупателям..."
    else:
        img 1916
        with fade
        cashier "Мэм."
        "Впредь обещаю что мы будем более внимательными к посетителям."
        "И такой ситуации больше не повторится."
        "Прошу прощения еще раз..."
    return

label afterJailDay2_dickofficestreet1:
    mt "Черт! Я стоптала все ноги в каблуках пока шла через весь город!"
    "Где там этот Дик?!"
    "Тюфяк! Мог бы сам меня найти скорее!"
    return

label afterJail_Day2_DickOffice_entrance_dialogue1:
    img 2822
    with fadelong
    reception_secretary "Мэм?"
    "Вы куда?"
    img 2823
    m "Я направляюсь в офис Дика Адвоката!"
    img 2824
    reception_secretary "Мэм?"
    "Вы записаны на прием?"
    img 2825
    m "Мне не нужна запись!"
    "Мы друзья!"
    "Даже больше!"
    img 2826
    "Мне позвонить ему чтобы он с вами связался?"
    "По другому вы меня не хотите пускать?"
    img 2827
    reception_secretary "Хорошо, Мэм."
    "Проходите."
    "Нет нужны беспокоить Мистера Дика."
    img 2828
    m "То-то же."

    $ dickReceptionStage = 3
    return
label afterJail_Day2_DickOffice_entrance_dialogue2:
    reception_secretary "Мэм."
    "Проходите."
    "Нет нужны беспокоить Мистера Дика."
    return
label afterJail_Day2_DickOffice_entrance_dialogue3:
    music Groove2_85
    img 2902
    with fade
    reception_secretary "Мэм."
    "Офисы уже закрыты."
    "Приходите завтра."
    img 2903
    m "Да, конечно."
    call refresh_scene_fade()
    return

label afterJail_Day2_DickOffice_entrance_dialogue3_a:
    reception_secretary "Да, Мэм?"
    "Вы что-то хотели?"
    mt "Она говорила что у нее нет телефона Дика, черт!!!"
    m "Нет, я ничего не хотела!"

    return

label afterJail_Day2_DickOffice_entrance_dialogue4:
    music Groove2_85
    img 2904
    with fadelong
    mt "Итак."
    "Я снова не встретилась с Диком."
    "Он что, не хочет меня видеть?"
    "Нет, такого не может быть."
    "Этот слизняк так ползал вокруг меня."
    "Он полностью в меня влюблен."
    img 2905
    "Я думаю это все происки той сучки, что сидит у входа в его кабинет."
    "Завтра я не дам ей меня надуть!"
    "Я обязательно увижу Дика!"
    "И он сразу решит все мои проблемы!"
    "..."
    "..."
    img 2906
    "Но что теперь?"
    "На улице снова стемнело."
    "Мне надо где-то ночевать."
    "В отель идти не стоит."
    "Там эта жирная корова на рецепшене."
    "Которая завидует мне."
    "..."
    "В тот магазин, где я спала сегодня ночью, идти не получится."
    if clothShopCashierOffended2 == True or clothShopCashierOffended3ReturnDress == True:
        "Эта проститутка продавщица наверняка будет проверять кабинки каждый вечер."
    else:
        "Продавщица наверняка будет проверять примерочные каждый вечер."

    mt "Куда же мне идти?"
    mt "Может еще поспрашивать на улице людей?"

    $ rainIntencity = 3
    $ lightning = True

    $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_street_dialogue1")
    call refresh_scene_fade()
    return

label afterJail_Day2_DickOffice_Secretary_dialogue1:
    music Groove2_85
    img 2829
    with fadelong
    dick_secretary "Здравстуйте, Мэм!"
    "Куда это Вы собрались?"

    $ dickOfficeSecretaryTalkedFlag1 = True
    call refresh_scene_fade()

    return

label afterJail_Day2_DickOffice_Secretary_dialogue2:
    music Groove2_85
    if dickOfficeSecretaryTalkedFlag1 == False:
        $ dickOfficeSecretaryTalkedFlag1 = True
        img 2829
        with fadelong
        dick_secretary "Здравстуйте, Мэм!"
        "Куда это Вы собрались?"
    img 2830
    m "В смысле куда я собралась?"
    "Я иду к Дику!"
    img 2831
    dick_secretary "Мэм."
    "Как Ваше имя?"
    img 2832
    with fade
    w
    img 2833
    with fade
    w
    img 2834
    with fade
    w
    img 2835
    with fade
    w
    img 2836
    with fade
    w
    img 2837
    with fade
    w
    img 2838
    with fade
    w
    img 2839
    with fade
    w
    img 2840
    with fade
    w
    img 2841
    with fade
    m "Меня зовут Моника Бакфетт!"
    "И ты, дорогуша, должна бы знать это!"
    "Твоя предшественница знала это прекрасно!"
    img 2842
    "И, не знаю куда она делась, но если ты не хочешь последовать за ней, то лучше запомни меня!"
    img 2843
    dick_secretary "Мэм."
    "Я сейчас проверю в списке встреч и сообщу Вам о результате."
    img 2844
    m "Что за бюрократия?"
    "Ну проверяй!"
    img 2845
    m "..."
    dick_secretary "..."
    img 2846
    m "..."
    dick_secretary "..."
    img 2847
    music Power_Bots_Loop
    dick_secretary "Мэм."
    "Вас нет в списке людей, с которыми у Мистера Дика назначена встреча."
    m "И что это значит?"
    dick_secretary "Вы не можете пройти, Мэм."
    img 2848
    m "Ты соображаешь что говоришь?"
    "Что это за список?"
    "Я не его деловой партнер, а его друг!"
    "Очень даже близкий!"
    "Даже более чем!"
    img 2849
    music Groove2_85
    dick_secretary "Хм.."
    "Мэм."
    "Насколько знаю, у Мистера Дика уже есть близкий друг."
    img 2850
    mt "Это она имеет ввиду себя что-ли?"
    "Очередная дешевая давалка!"
    img 2852
    dick_secretary "Мэм."
    "Хорошо."
    "Я сейчас проверю список друзей Мистера Дика."
    img 2851
    m "Давай! Смотри быстрее!"
    img 2853
    dick_secretary "..."
    m "..."
    img 2854
    dick_secretary "..."
    m "..."
    img 2855
    music Power_Bots_Loop
    dick_secretary "Мэм."
    "Вы не числитесь среди друзей Мистера Дика."
    "Мне очень жаль."
    img 2856
    m "ЧТО???"
    "Да как ты смеешь!"
    "Малявка!"
    "Быстро пусти меня к Дику!"
    "Или я сама туда зайду, БЕЗ ТВОЕГО РАЗРЕШЕНИЯ!"
    img 2857
    music Groove2_85
    dick_secretary "Мэм."
    "В любом случае Мистера Дика сейчас нет."
    "Он уехал по каким-то важным делам."
    img 2858
    m "По каким это?"
    img 2859
    dick_secretary "Я не знаю, Мэм."
    "Дела Мистера Дика очень серьезные и приватные и никого не касаются."
    img 2860
    mt "Знаю я какие у него обычно серьезные дела..."
    img 2861
    "Свяжитесь с Мистером Диком и передайте что его ждет Моника Бакфетт."
    img 2862
    dick_secretary "Мэм."
    "Мистер Дик просил его не беспокоить."
    "Я не буду нарушать его приказ."
    img 2863
    m "Что значит нарушать?"
    "Мы с ним друзья, он будет рад тому что я здесь."
    img 2864
    dick_secretary "Мэм."
    "Если вы друзья, то может быть вы сами позвоните ему?"
    img 2865
    music Power_Bots_Loop
    mt "ЧЕРТ!"
    mt "Я НЕ ПОМНЮ ЕГО НОМЕР! ОН БЫЛ В ТЕЛЕФОНЕ!"
    "А если я начну его спрашивать у этой дуры, то она точно его не даст."
    img 2866
    music Groove2_85
    m "Скажите, Мистер Дик когда вернется?"
    img 2867
    dick_secretary "Я точно не знаю, Мэм."
    "Вы можете подождать."
    img 2868
    m "Хорошо, я подожду в его кабинете."
    img 2869
    dick_secretary "Это исключено, Мэм."
    "Туда имеет доступ только Мистер Дик."
    img 2870
    m "А где мне тогда ждать?"
    img 2871
    dick_secretary "Вы можете присесть где Вам будет удобно, Мэм."
    img 2872
    m "Хорошо, я подожду его."

    $ dickOfficeSecretaryMonicaStage = 1
    $ remove_objective("dick_search")
    $ add_objective("wait_dick", _("Дождаться Дика"), c_orange, 5)
    $ add_objective("wait_dick_chair", _("Подождать Дика в удобном кресле"), c_green, 6)
    $ autorun_to_object("dick_office_hall1", "afterJail_Day2_DickOffice_Secretary_dialogue3")
    call refresh_scene_fade()

    return

label afterJail_Day2_DickOffice_Secretary_dialogue3:
    music Pyro_Flow
    img 2873
    with fadelong
    mt "Я не понимаю!"
    "Эта сучка что, издевается?"
    "Здесь нигде нет ни одного кресла!"
    "Вообще нет ничего куда сесть!"
    "Пойду ей это предъявлю!"
    $ dickOfficeSecretaryMonicaStage = 2
    $ remove_objective("wait_dick_chair")
    $ add_objective("wait_dick_chair", _("Тут негде ждать! Она издевается???"), c_red, 6)
    call refresh_scene_fade()

    return

label afterJail_Day2_DickOffice_Secretary_dialogue4:
    music Pyro_Flow
    img 2874
    with fadelong
    m "Слушайте!"
    "Я обошла весь этаж и не нашла ни одного кресла!"
    "Как вы прикажете мне его ждать?"
    img 2875
    music Groove2_85
    dick_secretary "Мэм."
    "Я сказала чтобы Вы удобно устроились."
    "Я не сказала что это ЗДЕСЬ."
    "Вы сами можете найти себе место где угодно."
    "И там подождать."
    img 2876
    music Pyro_Flow
    mt "ОНА ИЗДЕВАЕТСЯ!!!"
    "Я ВСЕ ВЫСКАЖУ ДИКУ ПО ПОВОДУ ЭТОЙ СУЧКИ!!!"
    "Я ДОБЬЮСЬ ЧТОБЫ ОН ЕЕ УВОЛИЛ!!!"
    "....."
    img 2877
    music Groove2_85
    m "Хорошо."
    "ЕСЛИ ВЫ ТАК НАСТАИВАЕТЕ..."
    img 2878
    "Я ПОДОЖДУ СНАРУЖИ..."
    "...."
    img 2879
    mt "АГРРРРРРРР!!!!"
    img 2880
    dick_secretary "Спасибо, Мэм."
    "Вы можете подойти через час или два."
    "Возможно Мистер Дик уже появится."

    $ dickOfficeSecretaryMonicaStage = 3

    $ remove_objective("wait_dick_chair")
    $ add_objective("wait_dick2", _("Зайти попозже узнать появился-ли Дик"), c_blue, 6)
    $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_Secretary_dialogue5")
    call refresh_scene_fade()
    return

label afterJail_Day2_DickOffice_Secretary_dialogue5:
    mt "ЧЕРТ!!!"
    "ЭТА СУЧКА ИЗДЕВАЕТСЯ!!!"
    "Мне теперь что, ждать этого гребаного Дика под дождем???"
    "..."
    "!!!!!!!!"
    "Ладно... Моника, выдохни..."
    "Надо зайти попозже, просто зайти попозже..."
    "Скоро все закончится..."

    $ mapChangedFlag = False
    $ streetDickOfficeAutorunIdx = 1
    $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_Secretary_dialogue6")
    return

label afterJail_Day2_DickOffice_Secretary_dialogue6:
    if mapChangedFlag == False:
#        $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_Secretary_dialogue6")
        return
    mt "Кажется уже прошло какое-то время..."
    "Может стоит проверить Дика?"

    $ dickOfficeSecretaryMonicaStage = 4
    $ streetDickOfficeAutorunIdx = 0
    return

label afterJail_Day2_DickOffice_Secretary_dialogue7:
    music Groove2_85
    img 2882
    with fadelong
    m "Скажите, Мистер Дик еще не подошел?"
    img 2883
    dick_secretary "Нет, Мэм."
    "Мистера Дика еще нет."
    m "Скоро он вообще появится?"
    dick_secretary "Мэм."
    "Я пока не знаю"
    "Зайдите попозже."
    img 2884
    m "Хорошо, зайду..."
    img 2885
    mt "АГРРРРРРРХХХ...."

    $ dickOfficeSecretaryMonicaStage = 5
    $ mapChangedFlag = False
    $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_Secretary_dialogue8")

    call refresh_scene_fade()
    return

label afterJail_Day2_DickOffice_Secretary_dialogue8:
    mt "ЧЕРТ!!!"
    mt "ЧЕРТ!!! ЧЕРТ!!! ЧЕРТ!!!"
    "Этого Дика так и нет!"
    "Ладно, Моника!"
    "Спокойствие!"
    "Подождем еще немного..."
    "..."
    "Да, и его секретарь будет уволена."
    "Это определенно!"

    $ streetDickOfficeAutorunIdx = 2
    $ mapChangedFlag = False
    $ teleportDickOfficeEveningFlag = True
    $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_Secretary_dialogue9")

    return

label afterJail_Day2_DickOffice_Secretary_dialogue9:
    if mapChangedFlag == False:
#        $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_Secretary_dialogue9")
        return
    $ streetDickOfficeAutorunIdx = 0
    $ autorun_to_object("street_dick_office", "afterJail_Day2_DickOffice_Secretary_dialogue10")
    call refresh_scene_fade()
return

label afterJail_Day2_DickOffice_Secretary_dialogue10:
    $ dickOfficeSecretaryMonicaStage = 6
    mt "Уже наступил вечер!!!"
    "Где там этот чертов Дик?!?!?"
    return

label afterJail_Day2_DickOffice_Secretary_dialogue11:
    music Pyro_Flow
    img 2887
    with fadelong
    m "Послушайте!"
    "Уже почти поздний вечер!"
    "Мистер Дик собирается вообще приезжать?"
    music Groove2_85
    img 2888
    dick_secretary "Сожалею, Мэм."
    "Мистер Дик позвонил и сказал что будет только завтра."
    img 2889
    music Power_Bots_Loop
    m "КАК ТОЛЬКО ЗАВТРА!??"
    "ОН НУЖЕН МНЕ СЕГОДНЯ!!!"
    img 2890
    dick_secretary "Сожалею, Мэм."
    img 2891
    m "ДАЙ СЮДА ТЕЛЕФОН!"
    "Я ЕМУ САМА ПОЗВОНЮ!"
    img 2892
    music Groove2_85
    dick_secretary "Мэм."
    "Если Вы будете слишком настойчивы, я вызову охрану."
    "Для этого мне надо нажать кнопку."
    "И через 15 секунд Вас отсюда выведут."
    img 2893
    music Pyro_Flow
    m "....."
    mt "?!?!?!?!!?!??!"
    "!!!!!!!!!"
    img 2894
    with fade
    w
    img 2895
    with fade
    m "ХОРОШО!"
    "ВО СКОЛЬКО"
    "ЗАВТРА"
    "БУДЕТ"
    "МИСТЕР ДИК??"
    img 2896
    music Groove2_85
    dick_secretary "Я не знаю, Мэм."
    "Но завтра он должен быть здесь."
    "Приходите завтра."
    img 2897
    m "Вы можете предупредить его что я приду?"
    img 2898
    dick_secretary "Конечно, Мэм."
    "Я предупрежу."
    img 2899
    m "Спасибо, ДО-РО-ГУ-ША...."
    img 2900
    dick_secretary "Всего хорошего, Мэм."

    $ remove_objective("wait_dick")
    $ remove_objective("wait_dick2")
    $ add_objective("dick_tomorrow1", _("Придти к Дику завтра"), c_white, 6)
    $ dickOfficeSecretaryMonicaStage = 7
    $ dickReceptionStage = 4

    $ autorun_to_object("dick_office_entrance", "afterJail_Day2_DickOffice_entrance_dialogue4")
    call refresh_scene_fade()

    return

label afterJail_Day2_DickOffice_street_dialogue1:
    $ gameSubStage = 2
    mt "Черт!"
    "Снова ледяной ливень!!!"
    "Нет никаких вариантов общаться с прохожими!"
    "Я ходила по городу целый день, но не увидела никаких приличных мест, чтобы переночевать..."
    "Думай скорее, Моника! Иначе ты замерзнешь!"
    "..."
    "Мне так сильно задувает... туда..."
    "..."
    "Так, мне надо идти в какой-то небогатый район."
    "Мне не по карману сейчас ночевать в приличном месте..."
    "И все из-за этой СУЧКИ!!!"
    "Я НЕ ПРОСТО УВОЛЮ ЕЕ!!!"
    "Я СДЕЛАЮ ЭТО ОСОБЕННО ЖЕСТКО!!!"
    "..."
    "Может спросить у того продавца кебаба?"
    if shawarmaTraderOffended1 == True:
        "Он животное, но может он сможет пролаять по человечески где находится какой-нибудь недорогой отель?"
        "Фу, Моника! Опять это слово!"
    else:
        "Он не слишком приятен, но может быть он знает где находится какой-нибудь недорогой отель?"
    $ whore1Enabled = False
    $ whoresMonicaDisturb = True
    $ add_objective("ask_shawarma", _("Спросить у продавца кебаба, может быть он знает где переночевать?"), c_blue, 6)

    return

label afterJail_Day2_Shawarma_dialogue1:
#    hide screen Rain
    $ renpy.music.set_pause(True, "rain")
    $ lightning = False
    music DarxieLand
    img 2907
    with fadelong
    shawarma "Мадаме!!!"
    "Вы неотразимы в этом платье!"
    "Никогда с ним не расставайтесь!"
    img 2908
    m "Я и не собираюсь!"
    "..."
    img 2909
    "Слушай."
    "Я не знаю как тебя зовут..."
    img 2910
    shawarma "Меня зовут, Джек, Мадаме!"
    "Лучшая шаверма!"
    "Во всей округе!"
    img 2909
    m "Она у тебя правда... вкусная?"
    img 2911
    shawarma "Конечно, Мадаме!"
    "Желаете попробовать?"
    img 2912
    m "Нет, нет, не хочу."
    "Я просто спросила..."
    img 2913
    shawarma "Чем могу быть Вам полезен, Мадаме?"
    menu:
        "У меня к тебе вопрос.":
            pass
        "Ничем. До свидания.":
            img 2912
            m "Ничем. До свидания."
            $ lightning = True
            $ renpy.music.set_pause(False, "rain")
            call refresh_scene_fade()
            return
    img 2914
    m "У меня к тебе вопрос."
    "Мне надо для одного знакомого человека найти место для ночлега."
    "Такое чтобы стоило дешево."
    "Ну.. совсем дешево."
    "Понимаешь меня?"
    img 2913
    shawarma "Конечно понимаю, Мадаме!"
    "Но зачем Вам ночевать в таком плохом месте!"
    "Есть много хороших гостиниц, Мадаме!"
    img 2915
    music Pyro_Flow
    m "Это не для меня, идиот!"
    "Я же сказала что это для другого человека!"

    img 2916
    music DarxieLand
    shawarma "Я здесь вижу только Вас, Мадаме!"
    "Вас и Ваше платье!"
    img 2917
    m "Слушай."
    "Ты можешь просто сказать мне место?"
    img 2918
    shawarma "Конечно могу, Мадаме!"
    "Вам надо идти назад, пройти метров 500, затем повернуть налево. Вы увидите дорогу."
    "Она ведет к старому многоквартирному дому."
    "В его подвале есть дешевый хостел."
    "Вы ведь про такое место спрашивали, Мадаме?"

    img 2919
    m "Это та дорога на которой стоят шлюхи?"

    img 2920
    shawarma "О! Мадаме!"
    "Эти ночные бабочки порока!"
    "Разве не из порока-ли появляется жизнь и цветут цветы!!!"
    "Стоит им только прикоснуться к Вам своим крылом и Вы обретете их легкость и изящество!"
    img 2921
    music Pyro_Flow
    m "Что за бред ты несешь?"
    "Какое изящество?"
    "У этих шлюх?"
    "А другой дороги туда нет?"

    img 2922
    music DarxieLand
    shawarma "Да, мадаме!"
    "Вы можете пройти по переулку, который находится прямо за мной!"

    menu:
        "Этот грязный переулок из которого воняет?":
            call bitch(2, "shawarma_hostel_offence")
            m "Этот грязный переулок из которого воняет?"
            "А еще какой-нибудь дороги туда нет?"
            shawarma "Нет, Мадаме!"
        "Хорошо. Спасибо.":
            pass
    img 2923
    m "Ладно."
    "Спасибо и на этом."
    img 2924
    shawarma "Спасибо мало, Мадаме!"
    img 2923
    m "В смысле???"
    img 2924
    shawarma "Я бы хотел попросить воздушный поцелуй у такой прекрасной женщин!"
    img 2925
    m "Никаких тебе поцелуев, ни воздушных, ни... ни каких еще, понял!"
    img 2926
    shawarma "Я буду ждать, Мадаме!"
    "Мое сердце принадлежит Вам!"
    img 2927
#    music Pyro_Flow
    m "Иди к черту!"

    $ renpy.music.set_pause(False, "rain")
    $ lightning = True
    $ remove_objective("ask_shawarma")
    $ add_objective("go_hostel", _("Найти дешевый хостел"), c_green, 6)
    $ streetHostelPathEnabled = True
    call refresh_scene_fade()
    return

label afterJail_Day2_Shawarma_dialogue2:
    $ renpy.music.set_pause(True, "rain")
    $ lightning = False
#    hide screen Rain
    music DarxieLand
    img 2907
    with fadelong
    shawarma "Мадаме!!!"
    "Вы неотразимы в этом платье!"
    img 2917
    m "Ты это уже говорил!"
    img 2918
    shawarma "Мадаме!!!"
    "Вы нашли то что искали? Вы нашли обитель на ночь?"
    "Вам понравилось там?"
    img 2919
    m "Да, нашла!"
    "И хватит уже об этой дыре!"
    $ lightning = True
    $ renpy.music.set_pause(False, "rain")
    call refresh_scene_fade()
    return

label hostel_street_dialogue1:
    mt "Похоже это тот хостел, про который говорил продавец шавермы."
    return

label hostel_edge_1_a_dialogue1:
    mt "Это какая-то мусорка. Что я забыла здесь?"
    return

label afterjail_whores_disturb_dialogue1:
    mt "Мне не по себе идти мимо этих... девушек..."
    "Я, пожалуй, быстро пробегу..."
    return
