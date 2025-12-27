label huinya:
    $ renpy.block_rollback()
    scene black with flash
    stop music fadeout 4
    pause 4
    scene menushka1 with dissolve
    window hide
    call screen sosok1_main_menu

screen sosok1_main_menu():
    tag menu

    imagebutton auto "images/menu/so_start_%s.png" xpos -190 ypos -50 focus_mask True action Jump("sosok1_start_mode")
    imagebutton auto "images/menu/so_exit_%s.png" xpos -180 ypos 250 focus_mask True action Jump("skitovijexit")#Quit(confirm=not main_menu)

label sosok1_start_mode:
    $ renpy.block_rollback()
    play sound kashel
    scene black with dissolve
    stop music fadeout 2
    pause 3
    jump vibornachala

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
