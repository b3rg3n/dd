label skitovijmenu:
    $ renpy.block_rollback()
    scene black with flash
    stop music fadeout 4
    pause 4
    scene menushka1story with dissolve
    play music intig33 fadein 1.5
    window hide
    call screen skit_main_menu

screen skit_main_menu():
    tag menu

    imagebutton auto "images/menu/skit_start_%s.png" xpos -190 ypos -50 focus_mask True action Jump("skitovij_start_mode")
    imagebutton auto "images/menu/so_exit_%s.png" xpos -180 ypos 150 focus_mask True action Jump("skitovijexit")

label skitovij_start_mode:
    $ renpy.block_rollback()
    play sound kashel
    scene black with dissolve
    stop music fadeout 2
    pause 3
    jump skitnachalo

label skitovijexit:
    $ renpy.block_rollback()
    play sound kashel
    scene black with dissolve
    stop music fadeout 2
    pause 3
    return

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
