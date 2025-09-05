init:

    $ mods["tutorblya"]=u"Как высрать\nсвой шедевр"

image tutor1 = Image("images/tutor1.png")
image tutor2 = Image("images/tutor2.png")
image tutor3 = Image("images/tutor3.png")
image tutor4 = Image("images/1.jpg")
image tutor5 = Image("images/tutor5.png")
image tutor6 = Image("images/tutor6.png")
image bergenbook1 = Image("images/tutor7.jpg")

define minwal = "muzon/anotherlife.ogg"

define govnina = "\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй\nХуй"

define bergentutor = Character('BERGEN', color = "#b30000", what_outlines=[ (1, "#b30000") ])

label tutorblya:
    play music minwal fadein 3
    scene bergenokno228
    show doshd
    show bergenokno229
    window hide
    pause 1
    bergen "Здаров бандиты."
    bergen "С чего бы начать,{w=0.2} блять?"
    window hide
    pause 1
    bergen "Для начала в папке game/mods создаем rpy файл со своим неебенным названием."
    bergen "Открываем его нотепадом и сперва вписуем туда это:"
    show tutor1 with flash
    window hide
    pause 5
    bergen "tutorblya это название label,{w=0.2} при запуске мода которая воспроизводится.{w=0.2} Там мы ебашим код."
    bergen "Если хотите скопировать с туториала - {w=0.2}в mods будет лежать текстовый документ со всеми строчками блять."
    bergen "Продолжаем."
    hide tutor1 with dissolve2
    window hide
    pause 1
    bergen "Команда define добавляет ваш файл звука или музона."
    bergen "Для добавления фонов или спрайтов юзаем команду image."
    show tutor6 with flash
    bergen "Для добавления персонажей она тоже подходит."
    window hide
    pause 3
    hide tutor6 with dissolve2
    bergen "А говорить их заставляем так:{w=0.2} glc \"Здарова, заебала.\"."
    glc "Здарова,{w=0.2} заебала."
    bergen "Работает."
    bergen "Как делать текс {b}жирным{b},{w=0.2} {i}курсивом{i},{w=0.2} {nw}"
    bergentutor "Как делать текс {b}жирным{b},{w=0.2} {i}курсивом{i},{w=0.2}{fast} другого цвета {w=0.2}{nw}"
    bergen "Как делать текс {b}жирным{b},{w=0.2} {i}курсивом{i},{w=0.2} другого цвета {w=0.2}{fast}- мне влом объяснять."
    bergen "Чекайте txt файл с кодом говна."
    bergen "Команда scene ебашит ваш фон."
    bergen "К ней можно присрать with dissolve2/4/нихуя для плавного начала (2 - 2сек, 4 - 4сек, без - 1 сек)."
    bergen "Либо присрать with flash (соответственно, фон меняется со вспышкой)."
    bergen "Команда play music xxxxx/play sound xxxxxxx ебашит ваш музон/звук."
    bergen "К ней можно присрать fadein 2 или любое ваше число секунд плавного начала."
    bergen "Команда stop music/stop sound соответственно останавливает."
    bergen "К ней можно присрать fadeout 3 или другое ваше число. То же самое, что и fadein, только это плавное затухание."
    bergen "Выборы делаем так:"
    show tutor2 with flash
    window hide
    pause 15
    bergen "Просмотрели?"
    hide tutor2 with dissolve2
    bergen "Проверяем блять."
    menu:
        "Я еблан":
            jump eblantutor
        "Я норм паря":
            jump normpacantutor

label eblantutor:
    bergen "Я тебя поздравляю с этим."
    bergen "Оно кста сработало."
    jump tutor2

label normpacantutor:
    bergen "Красава нахуй."
    bergen "Оно кста сработало."
    jump tutor2

label tutor2:
    scene bergenokno228
    show doshd
    show bergenokno229
    bergen "Выборы работают,{w=0.2} заебись."
    bergen "Как делать 3D выбор -{w=0.2} я объяснять не хочу."
    bergen "Как делать так,{w=0.2} чтобы для получения концовки нужно было набрать определенное количество очков (как в бесконечном лете - бед и гуд) я не буду."
    bergen "Мне пизда влом."
    bergen "Если что -{w=0.2} чекайте видосы про создание модов на бл."
    bergen "Абсолютно то же самое."
    bergen "Только вместо значка доллара юзайте define и image на всякий случай бле."
    window hide
    pause 1
    bergen "Да кста -{w=0.2} нужно перед строками после label держать 4 пробела."
    bergen "Так что если вы кидаете мне в лс скрин трейсбека,{w=0.2} где вылетает ошибка tab characters not allowed in renpy - {w=0.2}вас в детстве уронили с балкона родители."
    bergen "Либо вы ни чёрта не поняли из того, {w=0.2}что я тут высирала."
    bergen "Напомню -{w=0.2} что пример кода мода будет в текстовом документе в папке game/mods."
    bergen "Как сделать ломание ебла скитецкого,{w=0.2} бег, {w=0.2}закрытие/открытие зенек,{w=0.2} я,{w=0.2} наверное,{w=0.2} не расскажу."
    bergen "Или расскажу."
    bergen "Скита отложим на неопределенный срок,{w=0.2} а вот код бега будет."
    window hide
    pause 1
    bergen "Для вас всё просто."
    bergen "Бег делаем так:"
    bergen "scene mall at beg"
    bergen "И проверяем."
    scene mall at beg
    bergen "Работает,{w=0.2} ахуеть!"
    bergen "Ещё можно сделать остановку бега."
    bergen "scene mall at beg_end"
    scene mall at beg_end
    bergen "Вот и всё блять."
    bergen "Закрытие глаз делаем так: show blink"
    show blink
    bergen "Воот."
    bergen "Открытие делаем командой show unblink."
    hide blink
    show unblink
    bergen "И да{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} Если вставляете открытие после загрытия не меняя фона,{w=0.2} перед show unblink пишем hide blink."
    bergen "Иначе черный экран вместо фона,{w=0.2} ок?"
    bergen "Дождь добавляем командой show doshd."
    show doshd
    bergen "Воот."
    window hide
    pause 1
    hide doshd
    bergen "Снег врубаем командой show snow"
    show snow
    window hide
    pause 1
    bergen "Или show heavy_snow"
    hide snow
    show heavy_snow
    window hide
    pause 1
    bergen "Эффект старого телека делаем так: show prologue_dream"
    hide heavy_snow
    show prologue_dream
    window hide
    pause 2
    bergen "Воот."
    hide prologue_dream
    bergen "Я кстати добавила эффект лсд трипа."
    bergen "Как его включить?"
    show tutor3 with flash
    bergen "Тут вам только код копировать."
    bergen "Как это работает?{w=0.2} Не спрашивайте.{w=0.2} Магия."
    hide tutor3 with dissolve2
    bergen "Смотрим."
    scene domint:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat

    show tripsMVWWW777:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat
    with dissolve
    bergen "Пизда всё плывет."
    window hide
    pause 1
    bergen "Ещё я добавила лепестки."
    bergen "Ща мы их добавим."
    bergen "Пишем show lepestki_krutyatsa"
    bergen "Проверяем."
    scene tutor4 with flash
    show lepestki_krutyatsa
    window hide
    pause 3
    bergen "Заебись."
    window hide
    pause 1
    bergen "Как сделать паузу?"
    bergen "Пишем window hide чтобы скрыть окно вывода текста."
    bergen "Следом пишем pause 2 или любое число в секундах."
    window hide
    pause 2
    bergen "Работает."
    window hide
    pause 1
    bergen "Как вставить титры?"
    bergen "Пишем define gavnina = в ковычках свой текст"
    bergen "\n слеш влево и n - перенос на другую строку."
    bergen "Потом в конце сюжета пишем это:"
    show tutor5 with flash
    window hide
    pause 10
    bergen "Просмотрели?"
    hide tutor5 with dissolve2
    bergen "Тестируем бля."
    window hide
    pause 3
    show credits Text (govnina, size=50, text_align=0.5):
        xalign 0.5
        ypos 1
        linear 40.0 ypos -2.84
    $ renpy.pause(5, hard = True)
    $ renpy.pause(15)
    bergen "Заебись,{w=0.2} работает."
    scene bergenbook1 with dissolve
    bergen "Дальше писать мне лень."
    bergen "Если есть вопросы -{w=0.2} стучим в {a=https://t.me/b3rg3n}telegram{/a} (ссылка кликабельна)."
    bergen "А теперь идите нахуй в меню."
    return

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
