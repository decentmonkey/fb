define gui.flag720 = False
define gui.scenes_transitions = True
define gui.resolution.menu_pause_before_change_slide.value = 600 #600, 380
define gui.resolution.hud_screen.value1_1 = 16 # 16, 10
define gui.resolution.hud_screen.value1_2 = 16 # 16, 10
define gui.resolution.hud_screen.spacing2 = 8 #8, 5
define gui.resolution.hud_screen.value2 = 64 # 64, 48
define gui.resolution.hud_screen.font1_size = 23 #23, 20
define gui.resolution.hud_screen.height1 = 12 #12, 4
define gui.resolution.hud_screen.font2_size = 20 #20, 14
define gui.resolution.hud_screen.yoffset1 = 0 #0, -5
define gui.resolution.hud_screen.font3_size = 56 #56, 44
define gui.resolution.hud_screen.yoffset2 = 10 #10, 1
define gui.resolution.hud_screen.xoffset2 = 0 #0, 3
define gui.resolution.hud_screen.yoffset3 = 0 #0, -2
define gui.resolution.hud_screen.spacing1 = 0 #0, -2
define gui.resolution.hud_screen.bitchmeter_y_pos = 87 #87, 58
define gui.resolution.hud_screen.bitchmeter_x_pos = (1920 - 1844) # (1920 - 1844), 52
define gui.resolution.hud_screen.bitchmeter_x_size = 69 #69, 46
define gui.resolution.hud_screen.bitchmeter_y_size = 327 #327, 218
define gui.resolution.hud_screen.bitchmeter_top_gutter = 18 #18, 12
define gui.resolution.hud_screen.bitchmeter_bottom_gutter = 15 #15, 10
define gui.resolution.hud_screen.bitchmeter_thumb_offset = 22 #22, 14

define gui.resolution.hud_screen.bitchmeter_desc_y_pos = 250 #250, 166
define gui.resolution.hud_screen.bitchmeter_desc_x_pos = (1920-1866) #(1920-1866), 39
define gui.resolution.hud_screen.bitchmeter_desc_font_size = 26 #26, 18

define gui.resolution.text_button.spacing1 = 12 #12, 8
define gui.resolution.text_button.spacing2 = 15 #15, 10
define gui.resolution.text_button.padding = (0,15) #
define gui.resolution.text_button.style = "sprite_textbutton_text"
define gui.resolution.text_button.force_hovered.style = "sprite_textbutton_force_hovered_text"

define gui.resolution.action_menu.inventory_len1 = (64 + 8) # (64 + 8), (43 + 6)
define gui.resolution.action_menu.inventory_len2 = 16 + 16 # 16 + 16, 10 + 10
define gui.resolution.action_menu.padding1 = 8 #8, 6
define gui.resolution.action_menu.spacing1 = 8 #8, 6
define gui.resolution.action_menu.item_offset_init = 10 #10, 7
define gui.resolution.action_menu.item_offset =  64 + 8 #64 + 8, 43 + 6
define gui.resolution.action_menu.item_offset_inv = 8 #8, 6
define gui.resolution.action_menu.cell_size = 64 #64, 43
define gui.resolution.action_menu.tooltip.offset_x = 32 + 8 #32 + 8, 20 + 11
define gui.resolution.action_menu.tooltip.offset_y = 8 + 64 + 8 + 10 - 3 #8 + 64 + 8 + 10 - 3, 6 + 43 + 6 + 8
define gui.resolution.action_menu.tooltip.font_size = 24 #24, 16
define gui.resolution.action_menu.menu_height = 124 #83

#map
define gui.resolution.map.text_button.spacing1 = 12 #, 12
define gui.resolution.map.text_button.spacing2 = 10 #, 10
define gui.resolution.map.text_button.padding = (0,10)
define gui.resolution.map.text_button.style = "sprite_textbutton_map_text"
define gui.resolution.map.text_button.force_hovered.style = "sprite_textbutton_map_force_hovered_text"
define gui.resolution.map.text_button_disabled.style = "sprite_textbutton_disabled_map_text"
define gui.resolution.map.text_button_disabled.force_hovered.style = "sprite_textbutton_disabled_map_force_hovered_text"
define gui.resolution.map.text_button_active.style = "sprite_textbutton_active_map_text"
define gui.resolution.map.text_button_active.force_hovered.style = "sprite_textbutton_active_map_force_hovered_text"
#

define gui.resolution.choice_box.y_pos = 405 #405, 270

define gui.choice_button_text_size = 34 #25

define gui.resolution.koeff = 1


define res.suffix = "" #"", "_720p"
style dialogue_text:
    line_spacing 5 #5, 3

style sprite_textbutton_frm:
    ypadding 15 #15, 10

style sprite_textbutton_text is text:
    xpadding 15 #15, 10
    ypadding 15 #15, 10
    color "#b4b45b"
    hover_color "#f0f07a"
    size 36 #36, 26

#style sprite_textbutton_force_hovered is button:
#    xpadding 15 #15, 10
#    ypadding 15 #15, 10
#    margin (0,0)

style sprite_textbutton_force_hovered_text is text:
    color "#f0f07a"
    hover_color "#f0f07a"
#        outlines [(0, "#b4b45b", 1, 1)]
    size 36 #36, 26


style sprite_textbutton_map_text is text:
    xpadding 0 #15, 10
    ypadding 0 #15, 10
    color "#b4b45b"
    hover_color "#f0f07a"
    size 24 #, 24

style sprite_textbutton_map_force_hovered_text is text:
    color "#f0f07a"
    hover_color "#f0f07a"
    size 24 #, 24

style sprite_textbutton_disabled_map_text is text:
    xpadding 0 #15, 10
    ypadding 0 #15, 10
    color "#696969"
    hover_color "#808080"
    size 24 #, 24

style sprite_textbutton_disabled_map_force_hovered_text is text:
    color "#808080"
    hover_color "#808080"
    size 24 #, 24

style sprite_textbutton_active_map_text is text:
    xpadding 0 #15, 10
    ypadding 0 #15, 10
    color "#e3252e"
    hover_color "#fe5569"
    size 24 #, 24

style sprite_textbutton_active_map_force_hovered_text is text:
    color "#fe5569"
    hover_color "#fe5569"
    size 24 #, 24

style text_on_black_style:
    color "#ffffff"
    size 62


style minimap_open_button_text:
    font "fonts/bebasneue regular.ttf"
    outlines [(2, "#000000", 0, 0)]
    size 40
    color "#e0e0e0"
    hover_color "#ffffff"
    text_align 0.5

style minimap_button_text:
    font "fonts/bebasneue regular.ttf"
    outlines [(2, "#000000", 0, 0)]
    size 0
    hover_color "#e0e0e0"
    hover_size 40
    text_align 0.5


style credits_line1:
    font "fonts/OpenSans-Regular.ttf"
    color "#ffffff"
#    kerning -1
#    size 24
    size 24

style credits_line2:
    font "fonts/Ubuntu-Condensed.ttf"
    color "#ffffff"
#    kerning -1
#    size 28
    size 32

style credits_line3:
    font "fonts/Ubuntu-Condensed.ttf"
    color "#ffffff"
#    kerning -1
#    size 40
    size 48

transform credits_transform:
    ypos 1080
    linear 520.0 ypos -27240

define gui.credits.offset1 = 30
define gui.credits.offset2 = 42
define gui.credits.offset3 = 40
define gui.credits.offset4 = 50
define gui.credits.offset5 = 45
define gui.credits.timeout = 170.0
