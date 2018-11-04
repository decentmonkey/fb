label street_house_fence:
    $ print "enter_street_house_fence"
    $ miniMapData = []
    call miniMapHouseGenerate()

    $ scene_name = "street_house_fence"
    $ sceneIsStreet = True
    $ scene_caption = _("House Fence")
    $ clear_scene_from_objects(scene_name)
    $ scene_image = "scene_Street_House_Fence_Monica_" + cloth + day_suffix

    $ add_object_to_scene("Monica", {"type" : 2, "base" : "Street_House_Fence_Monica_" + cloth + day_suffix, "click" : "street_house_fence_environment", "actions" : "l", "zorder":10, "tint": monica_tint})

    $ add_object_to_scene("Scratch", {"type":2, "base":"Street_House_Fence_Scratch", "click" : "street_house_fence_environment", "actions" : "l", "zorder" : 0})

#    $ add_object_to_scene("Teleport_House_Fence_Scratch", {"type":3, "text" : _("ЦАРАПИНА"), "rarrow" : "arrow_up_2", "base":"Street_House_Gate_Teleport_Outside", "click" : "street_house_fence_teleport", "xpos" : 638, "ypos" : 564, "zorder":11})
    $ add_object_to_scene("Teleport_House_Yard", {"type":3, "text" : _("НАЗАД ВО ДВОР"), "larrow" : "arrow_down_2", "base":"Screen_Down_Arrow", "click" : "street_house_fence_teleport", "xpos" : 960, "ypos" : 956, "zorder":11})
    return
#                            $ brightness_adjustment = 0.1
#                            $ saturation_adjustment = 1.07
#                            $ contrast_adjustment = 1.3

label street_house_fence_teleport(obj_name, obj_data):
    if obj_name == "Teleport_House_Yard":
        call change_scene("street_house_main_yard") from _call_change_scene_31
        return
    if obj_name == "Teleport_House_Outside":
        call change_scene("street_house_outside") from _call_change_scene_32
        return
    return
label street_house_fence_environment(obj_name, obj_data):
# neighborOffended1 = False #не здороваться
# neighborOffended2 = False #без разницы что он чуть не погиб
# neighborOffended3 = False #решил потоптать во дворе?
# neighborOffended4 = False #это не просто царапина, наехать
# neighborOffended5 = False #прогнать идиота, грубо
# neighborOffendedSue = False #закатить иск
# neighborOffendedSueBig = False #иск огромный
# neighborOffendedFarm = False #наехать на ферму
    if obj_name == "Monica":
        if gameStage > 2:
            mt "Я помню эту царапину."
            "Кажется будто это было еще вчера..."
            "Она так и не починена."
            "Эти хозяева недостойны моего дома!"
            "Я верну его назад, клянусь!"
            return
        m "Мой замечательный забор...
        Теперь с царапиной..."
    if obj_name == "Scratch":
        if gameStage > 2:
            mt "Я помню эту царапину."
            "Кажется будто это было еще вчера..."
            "Она так и не починена."
            "Эти хозяева недостойны моего дома!"
            "Я верну его назад, клянусь!"
            return
        if day_time == "day":
            img scene_Street_House_Scratch
        if day_time == "evening":
            img scene_Street_House_Scratch_Evening

        m "Мой сосед."
        if neighborOffended1 == True:
            m "С которым даже здороваться не по статусу такой девушке как Я!"
        if neighborOffended2 == True:
            m "Чуть не лишил себя своей никчемной жизни, когда стриг газон."
        else:
            m "Чуть не погиб из-за какой-то мелочи."
        if neighborOffended3 == True:
            m "Потом заявился ко мне, чтобы потоптать мой газон своими грязными ботинками!"
            "На газоне до-сих пор остались его грязные следы!"
        else:
            m "Затем пришел ко мне и показал эту царапину."
        if neighborOffended4 == True:
            m "И он посмел назвать это царапиной!
            Да он мне чуть не свернул весь забор!"
            "Он полностью сломал его!"
        else:
            m "Я считаю что ему не стоило беспокоится из-за такой мелочи."
            return

        if neighborOffended5 == True:
            m "Но я прогнала этого кретина и больше не хочу его видеть!"
            return
        if neighborOffendedSue == True:
            if neighborOffendedSueBig == True:
                m "Я закатила ему иск!"
                "Теперь Дик разотрет его в порошок!"
                "И оставит без штанов и без дома!"
                "Так ему и надо!"
                if neighborOffendedFarm == True:
                    m "Да, и еще эта дурацкая ферма через дорогу!"
                    "Ко всему прочему, я снесу эту чертову ферму, которая портит мне вид из окна!"
                    "Клянусь!"
            else:
                m "Я справедливо оценила ущерб в $500."
                "Но если он не вернет эти деньги в ближайшее время, то ему придется общаться с моим адвокатом!"
                if neighborOffendedFarm == True:
                    m "Да, и еще эта дурацкая ферма через дорогу!"
                    "Может соседу стоит ее куда-нибудь перенести?"

    return
