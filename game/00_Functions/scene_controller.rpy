default pause_enter = 0
default pause_exit = 0
default sceneStages = []
default lastSceneName = False
default game_version1_screen_ready_to_render = False

label show_scene:
    $ show_scene_loop_flag = False
    if scene_refresh_flag == False:
        jump show_scene_loop
    $ hide_screens_for_scene()
#    if dialogue_active_flag == True:
#        $ renpy.show_screen("dialogue_down_arrow")
#        $ renpy.pause()
#        $ renpy.hide_screen("dialogue_down_arrow")

label show_scene_now:
    if define_version_current != define_version:
        call define_autorun() from _call_define_autorun_2
    $ print "pause_enter"
    $ print pause_enter
    $ print "pause_exit"
    $ print pause_exit

    if rain != True or sceneIsStreet != True:
        hide screen Rain

    $ interface_blocked_flag = True
    $ list_files_scene_drop_flag = False
    if scene_sound != False:
        $ sound_to_play = get_filename(scene_sound)
        play sound sound_to_play
        $ scene_sound = False
    $ print "Bitchiness"
    $ print bitchmeterValue
    hide screen sprites_hover_dummy_screen

#    window hide
#    window show
    $ config.keymap["hide_windows"] = []
#    config.keymap["hide_windows"] = ["mouseup_3", "mouseup_2", "h"]

    if scene_transition != False and gui.scenes_transitions == True:
        if scene_transition == "Fade":
            scene black_screen at convert_resolution_transform
            with Dissolve(0.2)
            $ renpy.pause(0.2, hard=True)
        if scene_transition == "Fade_long":
            scene black_screen at convert_resolution_transform
            with Dissolve(0.7)
            $ renpy.pause(0.7, hard=True)

    $ renpy.scene()
    $ scene_image_file = get_image_filename(scene_image, True)
    $ scene_refresh_flag == False
    show screen show_image_screen(scene_image_file)
    $ image_screen_scene_flag = True
    call map_street_scene_visibility_check()
    show screen hud_screen(hud_presets[hud_preset_current])
    show screen hud_minimap(miniMapData)
    if rain == True and sceneIsStreet == True:
        show screen Rain
        stop music fadeout 1.0

    define idle_len = 0.0
    $ parse_transition_flag = True
    $ interface_blocked_flag = False
    show screen screen_sprites(scenes_data)
    if parse_transition_flag == True:
        if scene_transition != False and gui.scenes_transitions == True:
            if scene_transition == "Fade":
                with Dissolve(0.2)
            if scene_transition == "Fade_long":
                with Dissolve(0.7)
    $ scene_transition = False

    if scenes_data["autorun"].has_key(scene_name):
        $ autorunFunc = scenes_data["autorun"][scene_name]
        $ del scenes_data["autorun"][scene_name]
        show screen sprites_hover_dummy_screen()
        call expression autorunFunc from _call_expression_7
        jump show_scene

label show_scene_loop:
    $ pause_enter += 1
    pause
    $ pause_exit += 1
    if show_scene_loop_flag == False:
        jump show_scene_loop
    else:
        jump show_scene


label change_scene(scene_label, in_transition_name="Fade", in_sound_name="highheels_short_walk"):
    $ sceneIsStreet = False
    $ scene_transition = in_transition_name
    $ scene_sound = in_sound_name
    $ scene_refresh_flag = True
    $ scene_label = get_scene_label(scene_label)
    $ lastSceneName = scene_name
    call expression scene_label from _call_expression_4
    return

label refresh_scene():
    $ scene_refresh_flag = True
    $ show_scene_loop_flag = True
    $ lastSceneName = scene_name
    call expression scene_name from _call_expression_5
    return

label refresh_scene_fade():
    $ scene_transition = "Fade"
    $ lastSceneName = scene_name
    call refresh_scene()
    return
label refresh_scene_fade_long():
    $ scene_transition = "Fade_long"
    $ lastSceneName = scene_name
    call refresh_scene()
    return

label remove_dialogue():
    python:
        renpy.hide_screen("say")
        renpy.hide_screen("choice")
        renpy.hide("window")
        dialogue_active_flag = False


label after_load():
    if game_version1_screen_ready_to_render == False:
        $ game_version1_screen_ready_to_render = True
        call refresh_scene()
    $ imagesSizesCache = {}
    $ show_scene_loop_flag = True
    jump show_scene
#    return

label call_save():
    if interface_blocked_flag == True:
        return
    if renpy.get_screen("say") != None or renpy.get_screen("choice") != None:
        return
    call screen save()
    return
    return
