default persistent.pause_before_change_slide = False
default persistent.auto_clipboard = False

default map_enabled = True

define fadehold = Fade(0.5, 1.0, 0.5)
define fadelong = Fade(0.5, 0.5, 0.5)
default streetFunMusic = "road_trip"
default casualMusic = "Stealth_Groover"

default define_version = 1
default define_version_current = 0

default text_button_default_layout = "default"

default clickHoldMode = True #блокировка клика после диалога, если мышкой не двигали
default clickHoldFlag = False
default clickHoldLastTime = 0
default clickHoldLastMouseX = 0
default clickHoldLastMouseY = 0
default screenActionHappened = False

define imagesSizesCache = {}

label define_autorun:
    $ print "autorun!"

    $ define_version_current = define_version

    $ actions_objects = { #иконки действий
        "l" : {
            "description" : _("Смотреть"),
            "label_suffix" : "_use",
            "icon" : "/Icons/eye" + res.suffix + ".png",
        },
        "h" : {
            "description" : _("Взять"),
            "label_suffix" : "_hand",
            "icon" : "/Icons/hand" + res.suffix + ".png"
        },
        "t" : {
            "description" : _("Говорить"),
            "label_suffix" : "_talk",
            "icon" : "/Icons/talk3" + res.suffix +".png",
        },
        "w" : {
            "description" : _("Идти"),
            "label_suffix" : "_walk",
            "icon" : "/Icons/walk" + res.suffix + ".png",
        }
    }


    $ text_button_layouts = {
        "default": {
            "text_button.spacing1" : gui.resolution.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.text_button.spacing2,
            "text_button.style" : gui.resolution.text_button.style,
            "text_button.force_hovered.style" : gui.resolution.text_button.force_hovered.style,
            "text_button.padding" : gui.resolution.text_button.padding
        },

        "map" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        },
        "map_disabled" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button_disabled.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button_disabled.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        },
        "map_active" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button_active.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button_active.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        },
        "map_house" : {
            "text_button.spacing1" : gui.resolution.map.text_button.spacing1,
            "text_button.spacing2" : gui.resolution.map.text_button.spacing2,
            "text_button.style" : gui.resolution.map.text_button_active.style,
            "text_button.force_hovered.style" : gui.resolution.map.text_button_active.force_hovered.style,
            "text_button.padding" : gui.resolution.map.text_button.padding
        }
    }

    call define_hudpresets() from _call_define_hudpresets

    $ calendar_days = [_("Пн"), _("Вт"), _("Ср"), _("Чт"), _("Пт"), _("Сб"), _("Вс")]
    return

label define_hudpresets:
    $ hud_presets = {
        "default" : {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : True,
            "display_scene_map" : True,
            "display_bitchmeter" : True,
            "display_closemap" : True
        },
        "default_map_disabled" : {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : True,
            "display_scene_map" : False,
            "display_bitchmeter" : True,
            "display_closemap" : True
        },
        "map": {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : False,
            "display_scene_map" : False,
            "display_bitchmeter" : False,
            "display_closemap" : True
        },
        "map_locked" : {
            "display_daytime" : True,
            "display_money" : True,
            "display_objectives" : True,
            "display_calendar" : True,
            "display_scene_caption" : False,
            "display_scene_map" : False,
            "display_bitchmeter" : False,
            "display_closemap" : False
        },

    }
    return

label run_after_load:
    $ print "after load!"
    return

label game_init:
    $ image_screen_scene_flag = False
    $ show_scene_loop_flag = False
    $ interface_blocked_flag = False
    define dissolve1 = Dissolve(0.5)
    define dialogue_active_flag = False
    define last_dialogue_character = "m"

    $ width_half = config.screen_width / 2

    $ preferences.show_empty_window = False
#    $ config.keymap["game_menu"].remove("mouseup_3")
#    $ print(config.keymap["game_menu"])
#    $ print(config.keymap)
    $ config.log = True

    call define_autorun() from _call_define_autorun

    $ bitchmeter_places = {}

    $ objectives_list = []

#    $ map_enabled = False

    $ define_inventory_object("papers", {"description" : _("Papers"), "label_suffix" : "_use_papers", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/big_papers" + res.suffix + ".png"})
    $ define_inventory_object("phone", {"description" : _("Телефон"), "label_suffix" : "_use_phone", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/cell_phone" + res.suffix + ".png"})
    $ define_inventory_object("shovel", {"description" : "Shovel", "label_suffix" : "_use_shovel", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/shovel" + res.suffix + ".png"})
    $ define_inventory_object("journal", {"description" : _("Журнал Моды"), "label_suffix" : "_use_journal", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/journal" + res.suffix + ".png"})
    $ define_inventory_object("hairdye", {"description" : _("Краска для волос"), "label_suffix" : "_use_hairdye", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/hairdye" + res.suffix + ".png"})
    $ define_inventory_object("crumpled_dress", {"description" : _("Мятое платье"), "label_suffix" : "_use_crumpled_dress", "default_label" : False, "default_nolabel" : "cant_use", "icon" : "Inventory/crumpled_dress" + res.suffix + ".png"})

    $ scene_transition = False
    $ scene_sound = False
#    $ add_inventory("phone", 5, True)
#    $ add_inventory("shovel", 5, True)
#    $ remove_inventory("papers", 3, True)


#    call showLog("here!")
#    $ renpy.log("here!")
    return

label showLog(str):
    show screen notify(str)

    return
