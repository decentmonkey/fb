default monicaOfficeSecretaryAtDesk = True
default monicaOfficeSecretaryLooked = False
default monicaOfficeSecretaryQuest1Planned = True
default monicaOfficeSecretaryCasualMode = False
default monicaOfficeSteveCall1Planned = False

default monicaOfficeDickIncomingCallPlanned = False

default monicaOfficeSecretaryDialogueOffended1 = False
default monicaOfficeSecretaryDialogueOffended2 = False

default photoStudioOpened = False

default monicaOfficeDay2TeaPlanned = False
default monicaOfficeDay2TeaTalkStage = 0
default monicaOfficeDay2PhoneLost = False

label monica_office_secretary:
    $ print "enter_monica_office_secretary"
    $ miniMapData = []

    $ scene_name = "monica_office_secretary"
    $ scene_caption = _("Monica's Secretary")
    $ clear_scene_from_objects(scene_name)

    if monicaOfficeSecretaryAtDesk == True:
        $ scene_image = "scene_Office_Monica_Secretary_Monica_Secretary_" + cloth + day_suffix
        $ print "Office_Monica_Secretary_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Secretary_Monica_Secretary_" + cloth + day_suffix, "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":10})
        $ add_object_to_scene("Secretary", {"type" : 2, "base" : "Office_Monica_Secretary_Secretary", "click" : "monica_office_secretary_environment", "actions" : "lt", "zorder":10})
    else:
        $ scene_image = "scene_Office_Monica_Secretary_Monica_" + cloth + day_suffix
        $ add_object_to_scene("Monica", {"type" : 2, "base" : "Office_Monica_Secretary_Monica_" + cloth + day_suffix, "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":10})


    $ add_object_to_scene("Books1", {"type" : 2, "base" : "Office_Monica_Secretary_Books1", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Books2", {"type" : 2, "base" : "Office_Monica_Secretary_Books2", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Globe", {"type" : 2, "base" : "Office_Monica_Secretary_Globe", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Music_Instrument", {"type" : 2, "base" : "Office_Monica_Secretary_Music_Instrument", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Table", {"type" : 2, "base" : "Office_Monica_Secretary_Table", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0})
    $ add_object_to_scene("Teatable", {"type" : 2, "base" : "Office_Monica_Secretary_Teatable_Object", "click" : "monica_office_secretary_environment", "actions" : "lw", "zorder":0})
    $ add_object_to_scene("Windows", {"type" : 2, "base" : "Office_Monica_Secretary_Windows", "click" : "monica_office_secretary_environment", "actions" : "l", "zorder":0})

    $ add_object_to_scene("Teleport_Monica_Office_Photostudio", {"type":3, "text" : _("ФОТОСТУДИЯ"), "larrow" : "arrow_left_2", "base":"empty", "click" : "monica_office_secretary_teleport", "xpos" : 178, "ypos" : 1014, "zorder":11})

    $ add_object_to_scene("Teleport_Monica_Office_Cabinet", {"type":3, "text" : _("КАБИНЕТ МОНИКИ"), "rarrow" : "arrow_down_2", "base":"Office_Monica_Secretary_Teleport_Cabinet", "click" : "monica_office_secretary_teleport", "xpos" : 1692, "ypos" : 756, "zorder":11})

    $ add_object_to_scene("Teleport_Monica_Office_Entrance", {"type":3, "text" : _("ЛИФТ"), "rarrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "monica_office_secretary_teleport", "xpos" : 780, "ypos" : 956, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label monica_office_secretary_teleport(obj_name, obj_data):
    if obj_name == "Teleport_Monica_Office_Entrance":
        call change_scene("monica_office_entrance", "Fade_long", "snd_lift") from _call_change_scene_71
        return
    if obj_name == "Teleport_Monica_Office_Cabinet":
        call change_scene("monica_office_cabinet") from _call_change_scene_72
        return
    if obj_name == "Teleport_Monica_Office_Photostudio":
        if photoStudioOpened == False:
            m "В студии идет съемка.
            Не буду пока их отвлекать."
            return
        call change_scene("monica_office_photostudio") from _call_change_scene_73
        return

    return
label monica_office_secretary_environment(obj_name, obj_data):
    if obj_name == "Globe":
        m "Глобус?
        Фи!"
        "Зачем он ей?"
        "Она может разве только помечтать о разных странах."
        "Это я бывала везде, по всему миру.
        Ей нет необходимости в этом."
        "Она работает у меня, а значит должна работать, а не путешествовать!"
        "Все что может отвлекать от работы - неприемлемо!"
        call bitch(3, "secretary_globe") from _call_bitch_61
    if obj_name == "Monica":
        m "Это этаж моего главного офиса."
        "У меня здесь все под рукой."
        "Моя секретарь, фото-студия и мой кабинет."

    if obj_name == "Books1" or obj_name == "Books2":
        m "Моя секретарь слишком много увлекается чтением."
        "Она очень образована, но к чему ей развиваться дальше?"
        "Она что, хочет стать умнее меня?!"

    if obj_name == "Music_Instrument":
        m "Моя секретарь играет на музыкальных инструментах."
        "Это единственное чего я не умею из того что умеет она."
        "Но я не считаю это каким-то преимуществом."
        "Подумаешь играет, ну и что?"
        "В любом случае, если бы я считала что она лучше меня хоть в чем-то, то она бы здесь не работала..."

    if obj_name == "Table":
        m "За этим столом моя секретарь проводит почти все рабочее время."

    if obj_name == "Windows":
        m "Из этих окон ужасный вид на город!
        Фи!"
        "Не то что из окон моего дома!"
        "Поэтому я даже закрыла окна у себя в офисе, чтобы не портить себе настроение!"
        "Если бы я могла, я бы переместила это здание куда-нибудь в другое, более живописное место!"
    if obj_name == "Teatable":
        if obj_data["action"] == "l":
            m "Это чайный столик."
            "Моя секретарь обычно угощает чаем, либо кофе тех, кто ожидает моего приема."
            "Разумеется, я распорядилась, чтобы выпечка была невкусная."
            "Эти люди собираются отнять мое время, в конце концов!"
            "И я не собираюсь облегчать им жизнь!"

        if obj_data["action"] == "w":
            call change_scene("monica_office_secretary_teatable") from _call_change_scene_74
            return

    if obj_name == "Secretary":
        if obj_data["action"] == "l":
            img Monica_Secretary_Alone
            mt "Это моя секретарша."

            mt "Одна из немногих нормальных женщин, которые знают как держать себя с окружающими."

            "Она очень воспитанна и интеллигентна."

            "Четно говоря, я подозреваю что ей не очень-то нравится модельный бизнес."

            "Он для нее несколько выходит за строгие моральные принципы, по которым она воспитана."

            "Но так как ей очень хорошо платят (я плачу), она держится этой работы."

            "Более того она на самом деле хороший сотрудник."

            "Она очень тонко чувствует что надо ее начальнице."

            "Улавливает мое настроение и мысли."

            "Работает быстро."

            "Делает все сразу."

            "И знает свое место ниже меня."

            "Она понимает, что должна подчиняться таким как Я."

            "Потому что у нее нет такой красоты и интеллекта как у меня."
            $ monicaOfficeSecretaryLooked = True
            return
        if obj_data["action"] == "t":
            if monicaOfficeDay2TeaPlanned == True:
                if monicaOfficeDay2TeaTalkStage == 0:
                    call monica_office_tea_talk1()
                    $ monicaOfficeSecretaryAtDesk = False
                    call refresh_scene_fade()
                    return
            if monicaOfficeSecretaryCasualMode == True:
                music RnB4_100
                img 1154

                if day_time == "evening" and day == 1:
                    secretary "Миссис Бакфетт!"
                    m "Дорогая, что ты делаешь на работе так поздно?"
                    secretary "Миссис Бакфетт, я делаю документы по платежу от Вашего младшего партнера Стива!"
                    "Вы сказали что разберетесь с этим и я заранее начала их готовить!"
                    m "Да, дорогая.
                    Я совсем забыла."
                    "Завтра я обязательно разберусь с этим, так что продолжай работу."
                    secretary "Рада служить Вам!"

                else:
                    secretary "Миссис Бакфетт!"

                    "Я выполню любое Ваше поручение!"

                    "Только скажите что необходимо!"

                    "Рада служить Вам!"

                    m "Хорошо, дорогая."

                    "Пока ничего не надо."
                    w
                music casualMusic

            if monicaOfficeSecretaryQuest1Planned == True:
                $ monicaOfficeSecretaryQuest1Planned = False
                music RnB4_100
                img 1140
                img 1141
                secretary "Добрый день, Миссис Бакфетт!"

                img 1142
                "Вы выглядите потрясающе в этом платье!"

                m "Добрый день, моя дорогая."

                if monicaOfficeSecretaryLooked == False:
                    img 1143
                    mt "Это моя секретарша."

                    "Одна из немногих нормальных женщин, которые знают как держать себя с окружающими."

                    "Она очень воспитанна и интеллигентна."

                    "Четно говоря, я подозреваю что ей не очень-то нравится модельный бизнес."

                    "Он для нее несколько выходит за строгие моральные принципы, по которым она воспитана."

                    "Но так как ей очень хорошо платят (я плачу), она держится этой работы."

                    "Более того она на самом деле хороший сотрудник."

                    "Она очень тонко чувствует что надо ее начальнице."

                    "Улавливает мое настроение и мысли."

                    "Работает быстро."

                    "Делает все сразу."

                    "И знает свое место ниже меня."

                    img 1144
                    "Она понимает, что должна подчиняться таким как Я."

                    "Потому что у нее нет такой красоты и интеллекта как у меня."

                    img 1145
                    "Итак..."

                    "...."

                img 1146
                m "Что у нас на сегодня?"

                img 1147
                secretary "Миссис Бакфетт."

                "Я проследила и не обнаружила платежа за аренду."

                "От нашего младшего партнера Стива."

                "Согласно договоренности, о которой Вы мне упоминали, платеж должен был поступить сегодня до обеда, но его все так и нет."

                menu:
                    "Почему ты не связалась с ним?":
                        call bitch(2, "monica_secretary1") from _call_bitch_62
                        $ monicaOfficeSecretaryDialogueOffended1 = True
                        img 1146
                        m "Почему ты не связалась с ним?"

                        img 1150
                        secretary "Миссис Бакфетт!
                        Простите меня!"
                        "Просто я всего-лишь секретарь, а он большой начальник."
                        img 1151
                        "К тому же, вы знаете какие у него моральные нравы!"
                        "Я боюсь приближаться к нему даже на расстояние телефонной трубки!"

                        m "Хорошо, дорогая."

                        "Я с этим разберусь.
                        Стив всего-лишь мелкий слизняк, тебе не стоит бояться его."

                        "Что еще?"

                    "Хорошо, дорогая. Я разберусь.":

                        m "Хорошо, дорогая."

                        "Я с этим разберусь."

                        "Что еще?"

                img 1148
                secretary "Еще на сегодня у Вас кастинг двух моделей."

                m "От какого агентства?"

                secretary "Эти модели не представляют никакого агентства.
                Они пришли просто с улицы."

                "Если честно, я не уверена стоило-ли мне включать их в Ваш график."

                "Они проявили завидное упорство.
                На мой взгляд им очень нужны деньги."

                "Они меня так умоляли...
                В общем, я решила дать им шанс."

                menu:
                    "Снова какие-то попрошайки?":
                        call bitch(5, "monica_secretary2") from _call_bitch_63
                        $ monicaOfficeSecretaryDialogueOffended2 = True
                        img 1149
                        m "Снова какие-то попрошайки?"

                        "Дорогая, я просила тебя не отнимать у меня время разными уборщицами и посудомойками."

                        img 1150
                        secretary "Мэм, мне вычеркнуть их из расписания?"

                        img 1149
                        m "Не надо, я посмотрю их."

                        "Но в следующий раз не отнимай мое время подобными вещами."

                        img 1151
                        secretary "Конечно, Мэм.
                        Такого больше не повторится."

                        "Я больше никому не позволю отнимать Ваше драгоценное время по пустякам."

                        img 1152
                        m "Вот и славно, дорогая."

                        img 1153
                        m "Рада служить Вам, Миссис Бакфетт!"

                        img 1149
                        m "Я пойду в свой кабинет."

                        m "Можешь вызывать своих уборщиц."

                    "Хорошо, я посмотрю их.":
                        call bitch(-5, "monica_secretary2") from _call_bitch_64
                        m "Я пойду в свой кабинет."
                        "Можешь вызывать их."

                img 1154
                secretary "Выполняю, Мэм!"
                w

                music casualMusic
                $ monicaOfficeSecretaryCasualMode = True
                $ monicaOfficeWorkMonkeysPlanned = True
                $ monicaOfficeSteveCall1Planned = True
                $ add_objective("go_work", _("Идти в свой кабинет и позвонить Стиву"), c_green, 1)
                return
    return




















    #
