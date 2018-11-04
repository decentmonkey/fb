default questionHelperEnabled = False
default questionHelperFuncName = False

label question_helper_enable(funcName):
    hide screen hud_screen
    $ questionHelperEnabled = True
    $ questionHelperFuncName = funcName
    show screen hud_screen(hud_presets[hud_preset_current])
    return

label question_helper_disable:
    $ questionHelperEnabled = False
    hide screen hud_screen
    show screen hud_screen(hud_presets[hud_preset_current])
    return

label question_helper_call:
    if interface_blocked_flag == True:
        return
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    hide screen action_menu_screen
    show screen sprites_hover_dummy_screen()
    call expression questionHelperFuncName
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ parse_transition_flag = False
    return
