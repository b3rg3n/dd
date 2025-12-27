define config.name = _("Dmitry Diary")
define gui.show_name = False

define config.version = "1.2"

define gui.about = _p("""
Кликабельные ссылки:

Автор - {a=https://t.me/viva_la_razumizm}BERGEN{/a}.

Канал - {a=https://t.me/SkeetDynasty}Skeet Dynasty{/a}.

Это моя последняя рефлексия - аж 3 истории про BeerdMANNа, Skittels15, Morerator-bot, доберманчике да и просто о Дмитрии Скитецком.

Эту игру ждали многие.

Правда?
""")

define build.name = "DmitryDiary"

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.sample_sound = "audio/kashel.ogg"

define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.intra_transition = dissolve

define config.after_load_transition = dissolve

define config.end_game_transition = dissolve







define config.window = "auto"




define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)








default preferences.text_cps = 100





default preferences.afm_time = 15
















define config.save_directory = "DmitryDiary-1644223432"






define config.window_icon = "gui/window_icon.png"
define config.windows_icon = "gui/window_icon.png"






init python:




















    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)



    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.ogv', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.rpy', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')

    build.documentation('*.html')
    build.documentation('*.txt')
