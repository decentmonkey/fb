################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

screen show_image_screen(image_name):
    layer "master"
    fixed:
        add image_name at convert_resolution_transform

screen credits_screen(creditsList):
    frame:
        background None
        at credits_transform

        $ ptr = 0
        for line1 in creditsList:
            $ lineType = line1[0]
            if lineType == 0:
                $ ptr += gui.credits.offset1
            if lineType == 1:
                text line1[1]:
                    xpos 0.5
                    ypos ptr
                    xanchor 0.5
                    style "credits_line1"
                $ ptr = ptr + gui.credits.offset2
            if lineType == 2:
                text line1[1]:
                    xpos 0.5
                    ypos ptr
                    xanchor 0.5
                    style "credits_line2"
                $ ptr = ptr + gui.credits.offset3
            if lineType == 3:
                text line1[1]:
                    xpos 0.5
                    ypos ptr
                    xanchor 0.5
                    style "credits_line3"
                $ ptr = ptr + gui.credits.offset4

            if lineType == 4:
                text line1[1] + "   ":
                    xpos 0.5
                    ypos ptr
                    xanchor 1.0
                    style "credits_line1"
                text "   " + line1[2]:
                    xpos 0.5
                    ypos ptr
                    xanchor 0.0
                    style "credits_line1"
                $ ptr = ptr + gui.credits.offset5

screen screen_sprites(scenes_data):
    zorder 10
    layer "master"
    default idle_num = 0.0

    fixed:
            button:
                xfill True
                yfill True
                action [
                    Hide("say"),
                    Hide("dialogue_image_left"),
                    Hide("dialogue_image_right"),
                    Hide("dialogue_image_center"),
                    Hide("dialogue_down_arrow"),
                    Hide("action_menu_screen"),
                    Hide("action_menu_tooltip_screen")
                ]
                alternate [
                    Hide("say"),
                    Hide("dialogue_image_left"),
                    Hide("dialogue_image_right"),
                    Hide("dialogue_image_center"),
                    Hide("dialogue_down_arrow"),
                    Hide("action_menu_screen"),
                    Hide("action_menu_tooltip_screen"),
                    Call("call_save")
                ]

            $ data = scenes_data["objects"][scene_name] if scene_name in scenes_data["objects"] else False
            if data != False and game_version1_screen_ready_to_render == True:
                $ zorder_list = []
                $ for i in data: zorder_list.append([i, data[i]["zorder"]])
                $ zorder_list.sort(key=lambda x:x[1])
#                $ print zorder_list
                for zorder_ptr in zorder_list:
                    $ i = zorder_ptr[0]
                    $ tooltip_data = data[i]["tooltip"] if "tooltip" in data[i] else False
                    $ day_time_suffix = "_" + day_time if day_time in ["evening"] else ""
                    $ brightness_adjustment = 0.1
                    $ saturation_adjustment = 1.0
                    $ contrast_adjustment = 1.2
                    if data[i]["type"] == 0 :
                        $ varName = data[i]["text"]
                        text "[varName]"

                    $ mask_canvas_offset = data[i]["canvas_img" + day_time_suffix + "_mask"] if data[i].has_key("canvas_img" + day_time_suffix + "_mask") != False else data[i]["canvas_img_mask"] if data[i].has_key("canvas_img_mask") != False else False
                    $ canvas_offset = data[i]["canvas_img" + day_time_suffix] if data[i].has_key("canvas_img" + day_time_suffix) != False else data[i]["canvas_img"] if data[i].has_key("canvas_img") else False
                    if canvas_offset == False:
                        $ canvas_offset = mask_canvas_offset
                    $ overlay_canvas_offset = data[i]["canvas_img" + day_time_suffix + "_overlay"] if data[i].has_key("canvas_img" + day_time_suffix + "_overlay") != False else data[i]["canvas_img_overlay"] if data[i].has_key("canvas_img_overlay") else False

                    if data[i]["type"] == 2: #overlay image, with mask (if exists)
#                        $ print data[i]
                        $ spriteImageStr = data[i]["img" + day_time_suffix] if data[i]["img" + day_time_suffix] != False else data[i]["img"] if data[i]["img"] != False else scene_image_file
                        $ maskName = data[i]["img" + day_time_suffix + "_mask"] if data[i]["img" + day_time_suffix + "_mask"] != False else data[i]["img" +"_mask"] if data[i]["img" +"_mask"] != False else False
#                        $ idleImg = im.FactorScale(im.AlphaMask(Image(spriteImageStr), Image(maskName)),zoom_factor) if maskName != False else im.FactorScale(Image(spriteImageStr),zoom_factor)
#                        if data[i].has_key("name") and data[i]["name"] == "Spot":
#                            $ print data[i]
                        if canvas_offset != False and spriteImageStr == scene_image_file:
#                            $ idleImg = Image(spriteImageStr)
                            $ maskImage = Image(maskName)
                            $ maskImageSize = getImageSize(maskImage, maskName)
                            $ canvas_offset[2] = canvas_offset[0] + maskImageSize[1] - 1
                            $ canvas_offset[3] = canvas_offset[1] + maskImageSize[0] - 1
                            $ croppedImg = im.Crop(spriteImageStr, (canvas_offset[1], canvas_offset[0], canvas_offset[3]-canvas_offset[1]+1, canvas_offset[2] - canvas_offset[0]+1))
                            $ idleImg = im.AlphaMask(croppedImg, maskImage) if maskName != False else Image(spriteImageStr)
                        else:
#                            $ idleImg = Image(spriteImageStr)
                            $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskName)) if maskName != False else Image(spriteImageStr)
                        $ overlayName = data[i]["img" + day_time_suffix + "_overlay"] if data[i]["img" + day_time_suffix + "_overlay"] != False else data[i]["img" + "_overlay"] if data[i]["img" + "_overlay"] != False else False
                        $ hoverImg = idleImg
                        if overlayName != False:
                            add overlayName at convert_resolution_transform:
                                if overlay_canvas_offset != False:
                                    xpos overlay_canvas_offset[1]
                                    ypos overlay_canvas_offset[0]
                                if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                    xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                    ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                            if data[i]["hover_overlay"] == True:
                                if overlay_canvas_offset != False and mask_canvas_offset != False:
                                    $ overlayImage = Image(overlayName)
                                    $ overlayImageSize = getImageSize(overlayImage, overlayName)
                                    $ overlay_canvas_offset[2] = overlay_canvas_offset[0] + overlayImageSize[1] - 1
                                    $ overlay_canvas_offset[3] = overlay_canvas_offset[1] + overlayImageSize[0] - 1
                                    $ maskCompositeImage = im.Composite((overlay_canvas_offset[3] - overlay_canvas_offset[1] + 1, overlay_canvas_offset[2] - overlay_canvas_offset[0]+1), (mask_canvas_offset[1] - overlay_canvas_offset[1], mask_canvas_offset[0] - overlay_canvas_offset[0]), maskName)
                                    $ hoverImg = im.AlphaMask(Image(overlayName), maskCompositeImage)
                                else:
                                    $ hoverImg = im.AlphaMask(Image(overlayName), Image(maskName)) if maskName != False else Image(overlayName)

#                                $ hoverImg = im.FactorScale(im.AlphaMask(Image(overlayName), Image(maskName)),zoom_factor) if maskName != False else im.FactorScale(Image(overlayName),zoom_factor)
                        if spriteImageStr != scene_image_file:
                            add idleImg:
                                if canvas_offset != False:
                                    xpos canvas_offset[1]
                                    ypos canvas_offset[0]
                                if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                    xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                    ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                        if spriteImageStr == scene_image_file: #добавляем яркость на фоновых предметах
                            $ brightness_adjustment = 0.1
                            $ saturation_adjustment = 1.07
                            $ contrast_adjustment = 1.3
                        $ if data[i].has_key("b") == True: brightness_adjustment = data[i]["b"]
                        $ if data[i].has_key("s") == True: saturation_adjustment = data[i]["s"]
                        $ if data[i].has_key("c") == True: contrast_adjustment = data[i]["c"]
                        $ tint_adjustment = False
                        $ if data[i].has_key("tint") == True: tint_adjustment = data[i]["tint"]
                        if data[i].has_key("hover_enabled") == False or data[i]["hover_enabled"] == True:
                            if tint_adjustment != False:
                                $ hoveredImage = im.MatrixColor(
                                    idleImg,
                                    im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment) * im.matrix.tint(tint_adjustment[0], tint_adjustment[1], tint_adjustment[2])
                                )
                            else:
                                $ hoveredImage = im.MatrixColor(
                                    hoverImg,
                                    im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment)
                                )
                            imagebutton:
                                if canvas_offset != False:
                                    xpos canvas_offset[1]
                                    ypos canvas_offset[0]
                                if data[i]["hover_overlay"] == True:
                                    xpos overlay_canvas_offset[1]
                                    ypos overlay_canvas_offset[0]

                                if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                    xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                    ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                                idle hoveredImage
                                hover hoveredImage
                                hovered SetScreenVariable("idle_num", 0.4)
                                at imagebutton_hover_type1(idle_num)
                                focus_mask True
                                if data[i]["actions"] == "l": #если объекту не заданы действия кроме просмотра, то не выводим доп. меню
                                    action [
                                        Call("process_object_click", data[i]["click"], i, data[i]),
                                    ]
                                else:
                                    action [
                                        Show("action_menu_screen", None, data[i]["click"], i, data[i]),
                                    ]

#                                alternate Show("action_menu_screen", None, data[i]["click"], i, data[i])
                                alternate Call("call_save")

                    if data[i]["type"] == 3: #text with image
                        $ button_layout = data[i]["layout"] if data[i].has_key("layout") else text_button_default_layout
                        $ tint_adjustment = [1.0, 1.0, 1.0]
                        $ if data[i].has_key("b") == True: brightness_adjustment = data[i]["b"]
                        $ if data[i].has_key("s") == True: saturation_adjustment = data[i]["s"]
                        $ if data[i].has_key("c") == True: contrast_adjustment = data[i]["c"]
                        $ if data[i].has_key("tint") == True: tint_adjustment = data[i]["tint"]
                        $ spriteStr = data[i]["img" + day_time_suffix] if data[i]["img" + day_time_suffix] != False else data[i]["img"] if data[i]["img"] != False else False
                        $ maskStr = data[i]["img" + day_time_suffix + "_mask"] if data[i]["img" + day_time_suffix + "_mask"] != False else data[i]["img" +"_mask"] if data[i]["img" +"_mask"] != False else False
                        $ if spriteStr != False: maskStr = False #убираем маску если есть спрайт
                        $ overlayName = data[i]["img" + day_time_suffix + "_overlay"] if data[i]["img" + day_time_suffix + "_overlay"] != False else data[i]["img" + "_overlay"] if data[i]["img" + "_overlay"] != False else False

                        $ left_arrow = data[i]["larrow"]
                        $ right_arrow = data[i]["rarrow"]
                        $ disableSprite = False
                        $ if spriteStr == False and maskStr == False and overlayName == False: disableSprite = True
                        if overlayName != False:
                            add overlayName at convert_resolution_transform:
                                if overlay_canvas_offset != False:
                                    xpos overlay_canvas_offset[1]
                                    ypos overlay_canvas_offset[0]
                                if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                    xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                    ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                                if data[i].has_key("sprite_align"):
                                    if data[i]["sprite_align"] == "dc":
                                        anchor (0.5, 1.0)

                        $ object_z_order = int(data[i]["zorder"])
                        $ highSpriteHover = False
                        $ if data[i].has_key("high_sprite_hover") and data[i]["high_sprite_hover"] == True: highSpriteHover = True #ебаный костыль из-за тупого ренпи!!!
                        button:
                            xpos int(float(data[i]["xpos"]) / 1920.0 * config.screen_width)
                            ypos int(float(data[i]["ypos"]) / 1080.0 * config.screen_height)
                            anchor (0.5,0.5)
                            frame:
                                background Solid("#18181a")
                                margin (0,0)
                                padding text_button_layouts[button_layout]["text_button.padding"]
                                style "sprite_textbutton_frm"
                                hbox:
                                    if left_arrow != False:
                                        null:
                                            width text_button_layouts[button_layout]["text_button.spacing1"]
                                        add left_arrow:
                                            yalign 0.5
                                    null:
                                        width text_button_layouts[button_layout]["text_button.spacing2"]
                                    text __(data[i]["text"]) style text_button_layouts[button_layout]["text_button.style"]
                                    null:
                                        width text_button_layouts[button_layout]["text_button.spacing2"]
                                    if right_arrow != False:
                                        add right_arrow:
                                            yalign 0.5
                                        null:
                                            width text_button_layouts[button_layout]["text_button.spacing1"]

                            if highSpriteHover == False:
                                hovered [
                                    Show("hover_text_sprite", None, spriteStr, maskStr, disableSprite, brightness_adjustment, saturation_adjustment, contrast_adjustment, tint_adjustment, data[i], canvas_offset)
#                                   With(dissolve)
                                ]
                            else:
                                hovered [
                                    Show("hover_text_sprite_high_hover_sprite", None, spriteStr, maskStr, disableSprite, brightness_adjustment, saturation_adjustment, contrast_adjustment, tint_adjustment, data[i], canvas_offset)
#                                   With(dissolve)
                                ]
                            if highSpriteHover == False:
                                unhovered [
                                    Hide("hover_text_sprite", Dissolve(0.4)),
                                ]
                            else:
                                unhovered [
                                    Hide("hover_text_sprite_high_hover_sprite", Dissolve(0.4)),
                                ]
                            action Call("process_object_click", data[i]["click"], i, data[i])

                        $ spriteImageStr = spriteStr if spriteStr != False else scene_image_file
#                        $ idleImg = im.FactorScale(im.AlphaMask(Image(spriteImageStr), Image(maskStr)),zoom_factor) if maskStr != False else im.FactorScale(Image(spriteImageStr),1.5)
#                        $ idleImg = Image(spriteImageStr)
                        if maskStr != False:
                            if mask_canvas_offset != False and spriteImageStr == scene_image_file:
#                                $ idleImg = Image(spriteImageStr)
                                $ maskImage = Image(maskStr)
                                $ maskImageSize = getImageSize(maskImage, maskStr)
                                $ mask_canvas_offset[2] = mask_canvas_offset[0] + maskImageSize[1] - 1
                                $ mask_canvas_offset[3] = mask_canvas_offset[1] + maskImageSize[0] - 1
                                $ croppedImg = im.Crop(spriteImageStr, (mask_canvas_offset[1], mask_canvas_offset[0], mask_canvas_offset[3]-mask_canvas_offset[1]+1, mask_canvas_offset[2] - mask_canvas_offset[0]+1))
                                $ idleImg = im.AlphaMask(croppedImg, maskImage)
#                            $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskStr)) if maskStr != False else Image(spriteImageStr)
                            else:
                                $ idleImg = Image(spriteImageStr)
                        else:
                            $ idleImg = Image(spriteImageStr)

                        $ spriteImage = im.MatrixColor(
                            idleImg,
                            im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment) * im.matrix.tint(tint_adjustment[0], tint_adjustment[1], tint_adjustment[2])
                        )

                        if spriteStr != False or maskStr != False or overlayName != False:
                            imagebutton:
                                if canvas_offset != False:
                                    xpos canvas_offset[1]
                                    ypos canvas_offset[0]
                                if data[i].has_key("xsprite") and data[i].has_key("ysprite"):
                                    xpos int(float(data[i]["xsprite"]) / 1920.0 * config.screen_width)
                                    ypos int(float(data[i]["ysprite"]) / 1080.0 * config.screen_height)
                                if data[i].has_key("sprite_align"):
                                    if data[i]["sprite_align"] == "dc":
                                        anchor (0.5, 1.0)
                                idle spriteImage
                                hover spriteImage
                                hovered [
                                    SetScreenVariable("idle_num", 0.4),
                                    Show("hover_sprite_text", None, i, data[i], left_arrow, right_arrow, button_layout)
#                                    Show("hover_sprite_text", Dissolve(0.2), i, data[i])
                                ]
#                                unhovered Hide("hover_sprite_text", Dissolve(0.4))
                                unhovered Hide("hover_sprite_text", None)
                                at imagebutton_hover_type1(idle_num)
                                focus_mask True
                                action Call("process_object_click", data[i]["click"], i, data[i])


screen hover_text_sprite(spriteImageStr, maskImageStr, disableSprite, brightness_adjustment, saturation_adjustment, contrast_adjustment, tint_adjustment, data, canvas_offset):
    layer "master"
#    zorder 11

    if disableSprite == False:
        $ spriteImageStr = spriteImageStr if spriteImageStr != False else scene_image_file
#        $ print maskImageStr
#        $ print spriteImageStr
#        $ idleImg = im.FactorScale(im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)),zoom_factor) if maskImageStr != False else im.FactorScale(Image(spriteImageStr),zoom_factor)

        if maskImageStr != False:
            if canvas_offset != False and spriteImageStr == scene_image_file:
                $ maskImage = Image(maskImageStr)
                $ maskImageSize = getImageSize(maskImage, maskImageStr)
                $ canvas_offset[2] = canvas_offset[0] + maskImageSize[1] - 1
                $ canvas_offset[3] = canvas_offset[1] + maskImageSize[0] - 1
                $ croppedImg = im.Crop(spriteImageStr, (canvas_offset[1], canvas_offset[0], canvas_offset[3]-canvas_offset[1]+1, canvas_offset[2] - canvas_offset[0]+1))
                $ idleImg = im.AlphaMask(croppedImg, maskImage)
            else:
                $ idleImg = Image(spriteImageStr)
        else:
            $ idleImg = Image(spriteImageStr)
#        $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)) if maskImageStr != False else Image(spriteImageStr)

        $ spriteImage = im.MatrixColor(
            idleImg,
            im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment) * im.matrix.tint(tint_adjustment[0], tint_adjustment[1], tint_adjustment[2])
        )
        fixed:
            add spriteImage at hover_text_sprite_transform:
                if canvas_offset != False:
                    xpos canvas_offset[1]
                    ypos canvas_offset[0]
                if data.has_key("xsprite") and data.has_key("ysprite"):
                    xpos int(float(data["xsprite"]) / 1920.0 * config.screen_width)
                    ypos int(float(data["ysprite"]) / 1080.0 * config.screen_height)
                if data.has_key("sprite_align"):
                    if data["sprite_align"] == "dc":
                        anchor (0.5, 1.0)
screen hover_text_sprite_high_hover_sprite(spriteImageStr, maskImageStr, disableSprite, brightness_adjustment, saturation_adjustment, contrast_adjustment, tint_adjustment, data, canvas_offset):
    layer "master"
    zorder 100

    if disableSprite == False:
        $ spriteImageStr = spriteImageStr if spriteImageStr != False else scene_image_file
#        $ idleImg = im.FactorScale(im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)),zoom_factor) if maskImageStr != False else im.FactorScale(Image(spriteImageStr),zoom_factor)

        if maskImageStr != False:
            if canvas_offset != False and spriteImageStr == scene_image_file:
                $ maskImage = Image(maskImageStr)
                $ maskImageSize = getImageSize(maskImage, maskImageStr)
                $ canvas_offset[2] = canvas_offset[0] + maskImageSize[1] - 1
                $ canvas_offset[3] = canvas_offset[1] + maskImageSize[0] - 1
                $ croppedImg = im.Crop(spriteImageStr, (canvas_offset[1], canvas_offset[0], canvas_offset[3]-canvas_offset[1]+1, canvas_offset[2] - canvas_offset[0]+1))
                $ idleImg = im.AlphaMask(croppedImg, maskImage)
            else:
                $ idleImg = Image(spriteImageStr)
        else:
            $ idleImg = Image(spriteImageStr)
#        $ idleImg = im.AlphaMask(Image(spriteImageStr), Image(maskImageStr)) if maskImageStr != False else Image(spriteImageStr)

        $ spriteImage = im.MatrixColor(
            idleImg,
            im.matrix.brightness(brightness_adjustment) * im.matrix.saturation(saturation_adjustment) * im.matrix.contrast(contrast_adjustment) * im.matrix.tint(tint_adjustment[0], tint_adjustment[1], tint_adjustment[2])
        )
        fixed:
            add spriteImage at hover_text_sprite_transform:
                if canvas_offset != False:
                    xpos canvas_offset[1]
                    ypos canvas_offset[0]
                if data.has_key("xsprite") and data.has_key("ysprite"):
                    xpos int(float(data["xsprite"]) / 1920.0 * config.screen_width)
                    ypos int(float(data["ysprite"]) / 1080.0 * config.screen_height)
                if data.has_key("sprite_align"):
                    if data["sprite_align"] == "dc":
                        anchor (0.5, 1.0)

screen hover_sprite_text(name, data, left_arrow, right_arrow, button_layout):
    layer "master"
    zorder 11
    button:
        xpos int(float(data["xpos"]) / 1920.0 * config.screen_width)
        ypos int(float(data["ypos"]) / 1080.0 * config.screen_height)
        anchor (0.5,0.5)
        frame:
            background Solid("#18181a")
            margin (0,0)
            padding text_button_layouts[button_layout]["text_button.padding"]
            style "sprite_textbutton_frm"
            hbox:
                if left_arrow != False:
                    null:
                        width text_button_layouts[button_layout]["text_button.spacing1"]
                    add left_arrow:
                        yalign 0.5
                null:
                    width text_button_layouts[button_layout]["text_button.spacing2"]
                text __(data["text"]) style text_button_layouts[button_layout]["text_button.force_hovered.style"]
                null:
                    width text_button_layouts[button_layout]["text_button.spacing2"]
                if right_arrow != False:
                    add right_arrow:
                        yalign 0.5
                    null:
                        width text_button_layouts[button_layout]["text_button.spacing1"]

# Меню по клику правой кнопки мыши
screen action_menu_screen(click_label, name, data):
    default tt = Tooltip("No button selected.")
    $ getMousePosition()
    default x = -1
    default y = -1
    if x == -1 and y == -1:
        $ x,y = renpy.get_mouse_pos()

    $ menu_len = (len(data["actions"]) + len(inventory)) * gui.resolution.action_menu.inventory_len1 + gui.resolution.action_menu.inventory_len2
    if x + menu_len > config.screen_width:
        $ x = config.screen_width - menu_len
    if y + gui.resolution.action_menu.menu_height > config.screen_height:
        $ y = config.screen_height - gui.resolution.action_menu.menu_height

    layer "master"
    zorder 20

    fixed:
        button:
            xfill True
            yfill True
            action [
                Hide("say"),
                Hide("dialogue_image_left"),
                Hide("dialogue_image_right"),
                Hide("dialogue_image_center"),
                Hide("dialogue_down_arrow"),
                Hide("action_menu_screen"),
                Hide("action_menu_tooltip_screen")
            ]
            alternate [
                Hide("say"),
                Hide("dialogue_image_left"),
                Hide("dialogue_image_right"),
                Hide("dialogue_image_center"),
                Hide("dialogue_down_arrow"),
                Hide("action_menu_screen"),
                Hide("action_menu_tooltip_screen")
            ]

        frame:
#            background Solid("#242426")
            background Frame("gui/frame2.png", left=2, top=2, right=2, bottom=2)
            pos(x, y)
            anchor(-10, -10)
            xpadding gui.resolution.action_menu.padding1
            ypadding gui.resolution.action_menu.padding1
            hbox:
                spacing gui.resolution.action_menu.spacing1
                #actions
                $ actions_list = get_object_actions(data["actions"])
                $ idx = 0
                $ item_offset = gui.resolution.action_menu.item_offset_init
                for action_data in actions_list:
#                    $ icon_image = Image(action_data["icon"])
                    $ iconImg = action_data["icon"]
                    if data.has_key("icon_" + action_data["action"]):
                        $ iconImg = data["icon_" + action_data["action"]]
                    $ icon_image_idle = LiveComposite((gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size), (0,0), "Icons/action_icon_background_idle" + res.suffix + ".jpg", (0,0), iconImg)
                    $ icon_image_hover = LiveComposite((gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size), (0,0), "Icons/action_icon_background_hover" + res.suffix + ".jpg", (0,0), iconImg)
                    imagebutton:
                        background Solid("#000000")
                        xysize(gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size)
                        idle icon_image_idle
                        hover icon_image_hover xalign 0.5 yalign 0.5
                        action [
                            Hide("action_menu_tooltip_screen"),
                            Call("process_object_click_alternate_action", idx, actions_list, click_label, name, data)
                        ]
                        hovered Show("action_menu_tooltip_screen", None, x, y, item_offset, action_data["description"], "#83bac4")
                        unhovered Hide("action_menu_tooltip_screen")
                    $ idx += 1
                    $ item_offset += gui.resolution.action_menu.item_offset

                if len(inventory) > 0:
                    null:
                        width 0
                    $ item_offset += gui.resolution.action_menu.item_offset_inv
                #inventory
                for idx in range(0, len(inventory)):
#                    $ print(inventory[idx])
                    $ inventory_data = inventory_objects[inventory[idx][0]]
                    $ icon_image_idle = LiveComposite((gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size), (0,0), "Icons/inventory_icon_background_idle" + res.suffix + ".jpg", (0,0), inventory_data["icon"])
                    $ icon_image_hover = LiveComposite((gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size), (0,0), "Icons/inventory_icon_background_hover" + res.suffix + ".jpg", (0,0), inventory_data["icon"])
                    imagebutton:
                        id inventory[idx][0] + "_displayable"
                        xysize(gui.resolution.action_menu.cell_size,gui.resolution.action_menu.cell_size)
                        idle icon_image_idle
                        hover icon_image_hover xalign 0.5 yalign 0.5
                        hovered Show("action_menu_tooltip_screen", None, x, y, item_offset, inventory_data["description"], "#ffa8a8")
                        unhovered Hide("action_menu_tooltip_screen")
                        action [
                            Hide("action_menu_tooltip_screen"),
                            Call("process_object_click_alternate_inventory", idx, inventory_data, click_label, name, data)
                        ]
                    $ item_offset += gui.resolution.action_menu.item_offset

screen dialogue_down_arrow(): #мигающая стрелка внизу
    fixed:
        add "down_arrow" at dialogue_down_arrow_transform

screen sprites_hover_dummy_screen():
    layer "master"
    zorder 25
    fixed:
        button:
            xfill True
            yfill True
            action Return(False)

screen dialogue_image_black_overlay():
    layer "master"
    zorder 28
    fixed:
        xpos 0.0
        ypos 0.0
        button:
            padding (0,0)
            xfill True
            yfill True
            add "Overlays/black.png"
            action Return(False)


screen dialogue_image_left(img, img_width, img_height): #изображение слева
    layer "master"
    zorder 30
    fixed:
        xpos 0.0
        ypos 0.0
        xmaximum 0.5
        ymaximum 1.0
        add img at dialogue_image_left:
            maxsize (img_width,img_height)

screen dialogue_image_right(img, img_width, img_height): #изображение справа
    layer "master"
    zorder 30
    fixed:
        xpos 0.5
        ypos 0.0
        xmaximum 0.5
        ymaximum 1.0
        add img at dialogue_image_right:
            maxsize (img_width,img_height)

screen dialogue_image_center(img, img_width, img_height): #изображение по центру
    layer "master"
    zorder 30
    fixed:
        xpos 0.0
        ypos 0.0
        add img at dialogue_image_center:
            maxsize (img_width,img_height)

screen action_menu_tooltip_screen(in_x, in_y, item_offset, tooltip_text, in_text_color):
    $ in_x = in_x + item_offset + gui.resolution.action_menu.tooltip.offset_x
    $ in_y = in_y + gui.resolution.action_menu.tooltip.offset_y

    frame:
        xpos in_x
        ypos in_y
        xanchor 0.5
        background Frame("gui/frame2.png", left=2, top=0, right=2, bottom=2)
        text __(tooltip_text):
            size gui.resolution.action_menu.tooltip.font_size
#            color "#ffc9c9"
            color in_text_color

screen hud_minimap(minimapData):
    layer "master"
    zorder 60
    fixed:
        if len(minimapData) > 0:
            pos (int(1711 * gui.resolution.koeff), int(85 * gui.resolution.koeff))
            if miniMapOpened == False:
                button:
                    yanchor 0.0
                    xanchor 0.5
                    xysize (int(196 * gui.resolution.koeff), int(110 * gui.resolution.koeff))
                    padding (0,0)
                    $ imgName = get_image_filename("Open_Button_Map1" + res.suffix)
                    add imgName
                    text "":
                        xanchor 0.5
                        xpos 0.465
                        ypos 0.5
                        style "minimap_open_button_text"
                    action [
                        Call("miniMapOpen")
                    ]
            else:
                vbox:
                    button:
                        yanchor 0.0
                        xanchor 0.5
                        xysize (int(196 * gui.resolution.koeff), int(110 * gui.resolution.koeff))
                        padding (0,0)
                        add get_image_filename("Open_Button_Map2" + res.suffix)
                        text "":
                            xanchor 0.5
                            xpos 0.465
                            ypos 0.5
                            style "minimap_open_button_text"
                        action [
                            Call("miniMapClose")
                        ]
                    null:
                        height 10
                    for minimapCell in minimapData:
#                       $ print minimapCell
                        $ locationDisabledFlag = False
                        if len(miniMapEnabledOnly) > 0:
                            if minimapCell["name"] in miniMapEnabledOnly:
                                $ locationDisabledFlag = False
                            else:
                                $ locationDisabledFlag = True
                        if minimapCell["name"] in miniMapDisabled:
                            $ locationDisabledFlag = True
                        $ print miniMapDisabled
                        button:
                            yanchor 0.0
                            xanchor 0.5
                            xysize (int(196 * gui.resolution.koeff), int(110 * gui.resolution.koeff))
                            padding (0,0)
                            if locationDisabledFlag == False:
                                add get_image_filename(minimapCell["img"] + res.suffix)
                            else:
                                add get_image_filename(minimapCell["img"] + "_Disabled" + res.suffix)
                            text minimapCell["caption"]:
                                ypos 0.5
                                xanchor 0.5
                                xpos 0.465
                                style "minimap_button_text"
                            if locationDisabledFlag == False:
                                action [
                                    Call("miniMapHouseGenerateTeleport", minimapCell["name"], minimapCell)
#                                   Return(False)
                                ]
                            else:
                                action [
                                    Call("miniMapDisabled", minimapCell["name"], minimapCell)
                                ]
#                    hovered tt.Action("This is City 1")
                        null:
                            height 10
#        pos renpy.get_mouse_pos()

screen hud_screen(hud_presets):
    layer "master"
    zorder 50
    fixed:
        pos (gui.resolution.hud_screen.value1_1,gui.resolution.hud_screen.value1_2)
        vbox:
            hbox:
                spacing gui.resolution.hud_screen.spacing2
                #время дня
                if hud_presets["display_daytime"] == True:
                    if day_time == "day":
                        add "icons/daytime_day" + res.suffix + ".png":
                            yoffset -2
                            xanchor 2
                    if day_time == "evening":
                        add "icons/daytime_evening" + res.suffix + ".png":
                            yoffset -2
                            xanchor 5
                if hud_presets["display_calendar"] == True:
                    null:
                        width 0
                    fixed:
                        xmaximum gui.resolution.hud_screen.value2
                        ymaximum gui.resolution.hud_screen.value2
                        add "icons/calendar" + res.suffix + ".png":
                            yoffset -3
                        $ current_calendar_day = calendar_days[(day-1)%7]
                        text __(current_calendar_day):
                            xalign 0.49
                            yalign 0.32
                            font "fonts/montserrat-bold.ttf"
                            color "#303030"
                            kerning -1
                            size gui.resolution.hud_screen.font1_size
                            outlines [(1, "#ffffff", -0.5,0.5), (1, "#e0e0e0", 0.5, -0.5)]

                if hud_presets["display_money"] == True:
                    if gui.flag720 != True:
                        null:
                            width 0
                    if money == 100000000.0:
                        add "icons/money_rich" + res.suffix + ".png":
                            yalign 0.5

                        $ money_text = "$ " + '{:10,.2f}'.format(money)
                        text money_text:
                            color "#00a000"
                            xalign 0.0
                            yalign 0.5
                            yoffset gui.resolution.hud_screen.yoffset3
                            outlines [(3, "#000000", 0, 0)]
                    else:
                        if money < 20:
                            $ money_text = "$ " + '{:2,.2f}'.format(money)
                            text money_text:
                                color "#e80000"
                                xalign 0.0
                                yalign 0.5
                                yoffset gui.resolution.hud_screen.yoffset3
                                outlines [(3, "#000000", 0, 0)]

            fixed:
                yoffset gui.resolution.hud_screen.yoffset1
                vbox:
                    spacing gui.resolution.hud_screen.spacing1
                    null:
                        height gui.resolution.hud_screen.height1
                    if hud_presets["display_objectives"] == True:
                        for objective in objectives_list:
                            text "- " + __(objective[1]):
                                color objective[2]
                                font objectivesFont
                                size gui.resolution.hud_screen.font2_size
                                outlines [(2, "#000000", 0, 0)]
                    if questionHelperEnabled == True:
                        null:
                            height gui.resolution.hud_screen.height1
                        imagebutton:
                            idle "icons/question_icon" + res.suffix + ".png"
                            hover "icons/question_icon_hover" + res.suffix + ".png"
                            action [
                                Call("question_helper_call")
                            ]
    frame:
        background None
        right_padding 8
        top_padding 8
        xpos 1.0
        xanchor 1.0
        vbox:
            hbox:
                if hud_presets["display_scene_caption"] == True:
                    text scene_caption:
#                        font "fonts/baskerville_bold_win95bt.ttf"
#                        font "fonts/bebasneue book.ttf"
                        font "fonts/bebasneue regular.ttf"
#                        font "fonts/linotte-semibold.otf"
#                        font "fonts/ubuntu-condensed.ttf"
#                        font "fonts/tahoma.ttf"
#                        font "fonts/montserrat-bold.ttf"
                        size gui.resolution.hud_screen.font3_size
                        outlines [(2, "#000000", 0, 0)]
                        yoffset gui.resolution.hud_screen.yoffset2
                        xoffset gui.resolution.hud_screen.xoffset2

                if hud_presets["display_scene_map"] == True:
                    if map_enabled == True and mapStreetCheckShowing == True:
                        imagebutton:
                            xoffset 7
                            yoffset -7
                            idle "icons/map_icon2_idle" + res.suffix + ".png"
                            hover "icons/map_icon2_hover" + res.suffix + ".png"
#                           at mega_test_image_anim
#                           hover "mega_test_image"
#                           at map_icon_button_transform
                            action [
                                Call("map_show")
#                                Notify("Map")
                            ]

                    else:
                        add "icons/map_icon2_disabled" + res.suffix + ".png":
                            xoffset 7
                            yoffset -7

    fixed:
#            size (200, 327)
        if hud_presets.has_key("display_bitchmeter") and hud_presets["display_bitchmeter"] == True:
            $ bitchmeter_description = get_bitchmeter_description()
            text bitchmeter_description:
                xpos config.screen_width - gui.resolution.hud_screen.bitchmeter_desc_x_pos
                ypos gui.resolution.hud_screen.bitchmeter_desc_y_pos
                xanchor 0.5
                yanchor 0.5
                xalign 0.5
                yalign 0.5
#                    color c_blue
#                    color "#d3ea5f" #white green
#                    color "#e0e85c"
                color "#c8da2b"
#                    color "#6383c2"
#                    font "fonts/arial.ttf"
                font "fonts/linotte-semibold.otf"
#                        font "fonts/ubuntu-condensed.ttf"
#                        font "fonts/tahoma.ttf"
                size gui.resolution.hud_screen.bitchmeter_desc_font_size
                outlines [(2, "#808080", -1, 1), (2, "#404040", 0, 0)]
                at bitchmeter_style_transform

            bar:
                xpos config.screen_width - gui.resolution.hud_screen.bitchmeter_x_pos
                ypos gui.resolution.hud_screen.bitchmeter_y_pos
                value (100.0 / maxBitchness * bitchmeterValue) / 100.0
                xoffset 5
                xysize(gui.resolution.hud_screen.bitchmeter_x_size,gui.resolution.hud_screen.bitchmeter_y_size)
                bar_vertical True
                top_bar "/icons/bar/bar_empty" + res.suffix + ".png"
                bottom_bar "/icons/bar/bar_full" + res.suffix + ".png"
                thumb "/icons/bar/bar_thumb" + res.suffix + ".png"
                bottom_gutter gui.resolution.hud_screen.bitchmeter_bottom_gutter
                top_gutter gui.resolution.hud_screen.bitchmeter_top_gutter
                thumb_offset gui.resolution.hud_screen.bitchmeter_thumb_offset

screen photoshot_screen():
    zorder 100
    fixed:
        add "Overlays/white_screen.jpg" at photoshoot_transform

screen textonblack_screen(in_text):
    zorder 100
    layer "master"
    frame:
        xfill True
        yfill True
        background Solid("#000000")
        text __(in_text) style "text_on_black_style":
            xanchor 0.5
            yanchor 0.5
            xalign 0.5
            yalign 0.5

screen intro_image(image_name):
    zorder 190
    fixed:
        add get_image_filename(image_name)


################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    zorder 200
    style_prefix "say"

    $ in_who = who
    $ in_what = what

    python:
#        global last_dialogue_character
#        global dialogue_active_flag, screenActionHappened
#        print who
#        if who == "Noone":
#            who = last_dialogue_character
#        else:
#            last_dialogue_character = who
#        dialogue_active_flag = True
#        screenActionHappened = True
        what = re.sub("\!\s{1,}", "!\n", what)
        what = re.sub("\?\s{1,}", "?\n", what)
        what = re.sub("\.\s{1,}", ".\n", what)
        what = re.sub("Mr\.\\n", "Mr. ", what)
        what = re.sub("Mrs\.\\n", "Mrs. ", what)
#        mycopytext(what)

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    fixed:
        button:
            xfill True
            yfill True
            action [
#                Notify("click!"),
                Return(True)
            ],
            alternate [
#                Notify("hide!"),
                Hide("say")
            ]
    key "h" action Hide("say")
    key "c" action [
        Call("mycopytext_label" ,what),
    ]
    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is dialogue_text
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"
    fixed:
        button:
            style "menu_choice_empty_background_button"
            xfill True
            yfill True
            action [
                NullAction()
            ]

    vbox:
        for i in items:
            if i.action:
                if " (disabled)" in i.caption:
#                    $ str1 = _(i.caption)
#                    $ print str1
                    textbutton i.caption text_style "choice_button_disabled_text"
#                    textbutton str1.replace(" (disabled)", "") text_style "choice_button_disabled_text"
                else:
                    textbutton i.caption:
                        action [
#                       Notify("click!"),
                            SetVariable("dialogue_active_flag", False),
                            i.action
                        ]


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos gui.resolution.choice_box.y_pos
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = False

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Start") action Start()

        else:

            textbutton _("History") action ShowMenu("history")

            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")

        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("End Replay") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Main Menu") action MainMenu()

        textbutton _("New Episodes") action OpenURL("http://decent-monkey.com/news/")
        textbutton _("My Thanks") action ShowMenu("about")

        if renpy.variant("pc"):

            ## Help isn't necessary or relevant to mobile devices.
#            textbutton _("Help") action ShowMenu("help")

            ## The quit button is banned on iOS and unnecessary on Android.
            textbutton _("Quit") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    ## This ensures that any other menu screen is replaced.
    tag menu

    style_prefix "main_menu"

    add gui.main_menu_background
    fixed:
        imagebutton:
            xpos get_resolution_x(1525)
            ypos get_resolution_y(35)
            idle "gui/patreon_button.png"
            hover "gui/patreon_button_hover.png"
            action OpenURL("https://www.patreon.com/decentmonkey")

        imagebutton:
            xpos get_resolution_x(1524)
            ypos get_resolution_y(162)
            idle "gui/web_button.png"
            hover "gui/web_button_hover.png"
            action OpenURL("http://decent-monkey.com/news/")

        add "gui/resolution_caption.png":
            xpos get_resolution_x(1345)
            ypos get_resolution_y(440)

    ## This empty frame darkens the main menu.
    frame:
        pass

    ## The use statement includes another screen inside this one. The actual
    ## contents of the main menu are in the navigation screen.
    use navigation

    if gui.show_name:

        vbox:
            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid". When
## this screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Reserve space for the navigation section.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_viewport:
    xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Version [config.version!t]\n")


            ## gui.about is usually set in options.rpy.
            if gui.about:
                text "[gui.about!t]\n"

#            text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


## This is redefined in options.rpy to add text to the about screen.
define gui.about = ""


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu
    if (gui.save_game.enabled == False or dialogue_active_flag == True) and 1==1:
        use game_menu("Save"):
            fixed:
                order_reverse True
            text "Save disabled during dialogues.\nIt causes major bugs with the game.\nI'm sorry :("
    else:
        use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):

        fixed:

            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action [
                            FileAction(slot),
                        ]

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
            hbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")

                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                ## range(1, 10) gives the numbers from 1 to 9.
                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    text_align 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")


## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Preferences"), scroll="viewport"):

        vbox:

            hbox:
                box_wrap True

                if renpy.variant("pc"):

                    vbox:
                        style_prefix "radio"
                        label _("Display")
                        textbutton _("Window") action Preference("display", "window")
                        textbutton _("Fullscreen") action Preference("display", "fullscreen")

                ## Additional vboxes of type "radio_pref" or "check_pref" can be
                ## added here, to add additional creator-defined preferences.

            null height (4 * gui.pref_spacing)

            hbox:
#                box_wrap True

                vbox:
                    xminimum gui.resolution.menu_pause_before_change_slide.value

                    style_prefix "radio"
                    label _("Pause before change slide")
                    textbutton _("Enable") action SetField(persistent, "pause_before_change_slide", True)
                    textbutton _("Disable") action SetField(persistent, "pause_before_change_slide", False)

                vbox:
                    xmaximum 400

                    if config.has_music:
                        label _("Music Volume")

                        hbox:
                            bar value Preference("music volume")

                    if config.has_sound:

                        label _("Sound Volume")

                        hbox:
                            bar value Preference("sound volume")

                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)


                    if config.has_music or config.has_sound or config.has_voice:
                        null height gui.pref_spacing

                        textbutton _("Mute All"):
                            action Preference("all mute", "toggle")
                            style "mute_all_button"

            null height 20
            hbox:
                vbox:
                    xminimum gui.resolution.menu_pause_before_change_slide.value
                    style_prefix "pref"

                    label _("Language")
                    textbutton "English" action Language("english")
                    textbutton "German" action Language("german")
                    textbutton "Russian" action Language(None)

                vbox:
                    style_prefix "radio"
                    label "Auto Clipboard"
                    textbutton _("Enable") action SetField(persistent, "auto_clipboard", True)
                    textbutton _("Disable") action SetField(persistent, "auto_clipboard", False)

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what

        if not _history_list:
            label _("The dialogue history is empty.")

screen Rain_overlay:
    layer "master"
    zorder 29
    if rainIntencity == 1:
        add "rain":
            alpha .05
    if rainIntencity == 2:
        add "rain":
            alpha .10
    if rainIntencity == 3:
        add "rain":
            alpha .15

screen Rain:
    # включаем и выключаем дождь вместе с экраном
    if rain == True:
        if rainIntencity == 1:
            on 'show' action SPlay("snd_light_rain", "rain", loop=True)
        if rainIntencity == 2:
            on 'show' action SPlay("snd_moderate_rain", "rain", loop=True)
        if rainIntencity == 3:
            on 'show' action SPlay("snd_heavy_rain", "rain", loop=True)
        # можно остановить только дождь SStop("rain"),
        # тогда начавшийся гром догремит и стихнет сам
        on 'hide' action SStop()
        # псевдо-рандомные раскаты
        if lightning == True:
            if rainIntencity >= 1:
                timer 10.5 repeat True action [SPlay("snd_lightning", "thunder1"), Hide("photoshot_screen"), Show("photoshot_screen")]
            if rainIntencity >= 2:
                timer 17.5 repeat True action [SPlay("snd_lightning_medium", "thunder2"), Hide("photoshot_screen"), Show("photoshot_screen")]
            if rainIntencity >= 3:
                timer 26.5 repeat True action [SPlay("snd_lightning_long", "thunder3"), Hide("photoshot_screen"), Show("photoshot_screen")]
    #    timer 6.5 repeat True action SPlay("snd_lightning_medium", "thunder2")
    #    timer 15.0 repeat True action SPlay("snd_lightning_long", "thunder3")
        # картинка с молниями
    #    timer .1 repeat True action NewXA()
    #    add "light":
    #        xalign xa
        # дождь
        if rainIntencity == 1:
            add "rain":
                alpha .05
        if rainIntencity == 2:
            add "rain":
                alpha .10
        if rainIntencity == 3:
            add "rain":
                alpha .15

## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = set()


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    text_align 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        ypos 0.2
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900
