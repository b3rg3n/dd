label start:
    play music mndmusmenu fadein 10
    scene black with dissolve2
    $ renpy.pause(4, hard=True)
    $ renpy.block_rollback()
    show mnd_a3_menu_1
    show mnd_a3_menu_2

    show doshd
    with dissolve4
    "Дмитрий шёл по Новошохтинску,{w=0.2} закурил джоинт,{w=0.2} подумал."
    "Стоит ли ему рассказывать вам эту историю?"
    window hide
    pause 1
    "Согласен,{w=0.2} вопрос уебанский."
    "Но ведь реально -{w=0.2} захочет ли Димка?"
    window hide
    pause 1
    skt "Я не хочу вспоминать с чего всё начиналось,{w=0.2} ведь{nw}"
    skt1 "меня обоссали школьники(9(9(9(99999((((((( {nw}"
    skt "Я не хочу вспоминать с чего всё начиналось,{w=0.2} ведь{fast} это было очень давно{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    skt "Мне очень тяжело это вспоминать{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    skt "Всё начиналось{w=0.2}.{w=0.2}.{w=0.2}."
    "Чтобы 3D выбор работал,{w=0.2} нужно зажать палец на экране и выбрать нужный сюжет -{w=0.2} при отпускании отправитесь проходить."
    "Если вы ничё не поняли,{w=0.2} то я дам вам обычный ренпаевский выбор."
    "Ну так?"
    menu:
        "3D выбор как на компе":
            jump vibornachala
        "Выбор как в бесконечном лете":
            jump vibornachalastandart

label vibornachalastandart:
    menu:
        "Skittels15 Classic":
            jump novoshahtinsk
        "Skeetovij Bank":
            jump skeetovijbank
        "BERGEN сошла с ума":
            jump bergeneblan

label skeetovijbank:
    scene black with dissolve2
    play music bankintro fadein 5
    scene domext with flash
    show doshd
    "Эта история берёт свое начало здесь."
    "Дядя Дима был крупным акционером Новошахтинских компаний."
    window hide
    pause 1
    "Нстолько богатым,{w=0.2} что создал свой банк."
    "Назывался он Skeetovij BANK."
    window hide
    pause 1
    "Но были у него и конкуренты..."
    skt "iGandone LLC...{w=0.2} СУКИ,{w=0.2} Я ВАС НЕНАВИЖУ!"
    "Компания iGandone LLC занималась всякой хернёй."
    "Тем не менее,{w=0.2} она могла конкурировать со скитом."
    "В какой отрасли?"
    "Да они жили тем,{w=0.2} что подсерали скиту."
    window hide
    pause 1
    "Иногда даже в прямом смысле."
    scene sret with flash
    play sound tolkan4
    window hide
    pause 3
    scene domext with flash
    show doshd
    "Но не будем о грустном."
    window hide
    pause 1
    "Так вот,{w=0.2} Димку Скитови заказали одной очень малоизвестной киллерше."
    scene bergenllc with flash
    window hide
    pause 1
    ineony "Говорите,{w=0.2} у вас есть опыт в обращенни с дцпешниками?"
    window hide
    pause 1
    bergen "Конечно."
    window hide
    pause 1
    ineony "Вас ждёт очень щедрое вознаграждение.{w=0.2} Поверьте, ящик лимонно аскании того стоит!"
    window hide
    pause 1
    bergen "Я знаю."
    window hide
    pause 1
    ineony "Ну что ж."
    ineony "Добро пожаловать в iGandone LLC!"
    window hide
    stop music fadeout 4
    pause 4
    $ renpy.movie_cutscene('screen/skeet.ogv')
    scene bergdomint1 with flash
    play music dumaet
    window hide
    pause 1
    "BERGEN сидела дома и думала..."
    bergen "Каким образом грохнуть скитяру?"
    window hide
    pause 1
    bergen "Накуканить его и снять на видео?{w=0.2} А потом сжечь нахуй?"
    bergen "Хуета."
    window hide
    pause 1
    bergen "Утопить его в его же толчке?"
    bergen "Хуета."
    window hide
    pause 1
    bergen "Заминировать его хату?"
    bergen "Хуета."
    window hide
    pause 1
    "Пока думала,{w=0.2} нихуя не придумала...{w=0.2} И решила пойти на кухню."
    scene bergkuhint1 with dissolve2
    window hide
    pause 1
    bergen "Ну и нахуй я сюда пришла?"
    "Она решила подойти к окну."
    scene bergkuhint2 with dissolve2
    window hide
    pause 1
    bergen "Погодка ниче так сегодня."
    window hide
    pause 1
    "BERGEN решила попарить свою любимую жижку."
    window hide
    pause 1
    "Она достала подик и хорошенько затянулась."
    play sound podik
    window hide
    pause 5
    "Никотин приятно ударил в голову."
    window hide
    pause 1
    "По всему телу пошло приятное расслабление."
    window hide
    pause 1
    "А ведь это всего лишь 20мг на дрипке..."
    window hide
    pause 1
    "И тут BERGEN поняла,{w=0.2} что она хочет сделать со скитом."
    window hide
    pause 1
    bergen "Оригинально выходит.{w=0.2} Никто ещё так не делал."
    window hide
    pause 1
    bergen "iNeoony будет доволен,{w=0.2} ахах..."
    window hide
    pause 1
    scene bergkoridor with flash
    "Она не хотела терять ни минуты."
    "План уже был проработан в её голове."
    window hide
    pause 1
    "Скитецкого ждала страшная учесть."
    window hide
    pause 1
    bergen "Пизда ему."
    window hide
    pause 1
    "Но это потом."
    "А сейчас BERGEN заказывает яндекс такси и едет в Новошахтинск."
    scene bergfire with flash
    window hide
    pause 1
    bergen "Я иду за тобой,{w=0.2} Скит."
    window hide
    pause 1
    bergen "Жди и бойся."
    window hide
    pause 1
    bergen "Хуесос."
    scene black with dissolve2
    stop music fadeout 4
    window hide
    pause 4
    play music xarakter fadein 2
    scene domext with dissolve2
    show doshd with dissolve
    "В Новошахтинске сегодня был дождливый день."
    window hide
    pause 1
    "Димончик вышел из дома и спешил на встречу с главой очень известной компании..."
    window hide
    pause 1
    skt "Наконец-то от меня отстанут эти ебучие iGandone LLC!"
    skt "Я смогу жить полноценной жизнью!"
    skt "Запущу свой бренд говнозвонов Skeetovij phone!"
    skt "А в свободное время буду собирать легиончик с фм радио под редми 8 оливе!"
    window hide
    pause 1
    "Но этим мечтам не суждено было сбыться."
    play sound minusebalo
    pause 3
    show blink
    "Удар по лысой головешке перекрыл все эти маняфантазии."
    "И Димон отключился."
    scene black
    hide blink
    window hide
    pause 1
    "Занавес."
    window hide
    stop music fadeout 4
    pause 4
    play music hellozepp fadein 4
    scene skitpila
    show unblink
    window hide
    pause 2
    skt "Сука, где я?"
    window hide
    pause 1
    "Димка осмотрелся."
    window hide
    pause 1
    "Он всё понял."
    window hide
    pause 1
    play sound prosnulsa2
    pause 1.2
    stop sound
    hide unblink
    window hide
    pause 1
    play sound telek fadein 5
    "Димка что-то услышал."
    window hide
    pause 2
    scene skitsaw with flash
    play sound bergbazar
    window hide
    pause 32
    scene skitpila with flash
    "Димка понял,{w=0.2} в какую жопу он влез."
    play sound suka1
    scene skitpila with vpunch
    pause 0.7
    play sound suka2
    scene skitpila with vpunch
    pause 1.5
    play sound suka3
    scene skitpila with vpunch
    pause 2
    skt "МАМА,{w=0.2} Я НЕ ХОЧУ УМИРАТЬ!"
    window hide
    pause 0.5
    skt "ЛЕГИОНЧИК,{w=0.2} РОДНОЙ,{w=0.2} СОБИРАЙСЯ!"
    window hide
    pause 1
    play sound oshibka1
    "Но комп выдал ошибку."
    play sound oshibka2
    scene skitpila with vpunch
    pause 3.5
    play sound suka4
    scene skitpila with vpunch
    pause 0.1
    scene skitpila with vpunch
    pause 0.1
    scene skitpila with vpunch
    pause 2.8
    scene skitsaw with flash
    play sound vremyaskit
    window hide
    pause 4
    play sound porvalo
    scene skitpila with vpunch
    pause 0.6
    scene skitpila with vpunch
    pause 0.3
    scene skitpila with vpunch
    pause 0.6
    stop music
    scene black with flash
    pause 3
    scene prosnulsa
    play sound huevo
    show unblink
    window hide
    pause 3
    hide unblink
    skt "Твою ж мать..."
    skt "Это был сон..."
    stop sound fadeout 3
    window hide
    pause 1
    skt "Хорошо вчера побухал..."
    skt "Ща на важную встречу пойду."
    "Скит посмотрел на часы."
    window hide
    pause 0.5
    play sound prosnulsa1
    pause 1.5
    play sound prosnulsa2
    pause 1
    skt "Сука,{w=0.2} я опаздываю к iGandone..."
    skt "Где-то у меня был ручной телепорт..."
    window hide
    pause 1
    skt "Вот он ебать."
    play sound teleport
    scene ineonyllc with flash
    play music xarakter fadein 3
    skt "Здарова."
    skt "Я не сильно опоздал?"
    ineony "Часа на пол."
    ineony "...хаха лысый)"
    skt "А?"
    ineony "Да ничего страшного, говорю."
    window hide
    pause 1
    ineony "Может чаю?"
    skt "Почему нет?"
    ineony "Сейчас его принесёт моя ассистентка."
    "Скит невольно начал пускать слюнки."
    "Он давно не трахался даже с рукой."
    "Лишь одна мысль затуманила его разум."
    "Ведьмак 3:{w=0.2} Дико бабу охота."
    window hide
    pause 2
    scene ineonyllc1 with flash
    bergen "Вот ваш чай,{w=0.2} мой господин."
    window hide
    pause 1
    "Скит ахуел."
    "Бля,{w=0.2} это же та баба из сна..."
    "Та самая рыжольда,{w=0.2} что устроила пилу в Новошахтинске..."
    "Пизда."
    ineony "Что-то не так?"
    skt "Да не,{w=0.2} я просто вспоминал..."
    ineony "Что вспоминал?"
    "Айнеони не смог скрыть ухмылку,{w=0.2} но Скит этого не заметил."
    skt "Да вот выключил ли я чайник дома..."
    ineony "Да ладно."
    ineony "Если электрический,{w=0.2} то ничего страшного."
    skt "Ладно..."
    play sound drink
    "Скит сделал три глотка чефира."
    window hide
    pause 1
    "Они долго базарили о всякой хуйне,{w=0.2} пока Димку не выбил из колеи нехороший звук."
    play sound srat_ohota
    "Скит захотел срать."
    "Пиздец как."
    skt "Где у вас тут туалет?"
    bergen "Двумя этажами выше,{w=0.2} справа."
    bergen "Провести?"
    skt "Да не..."
    "Пристальный взгляд рыжей бабы напрягал скита так,{w=0.2} что одно неверное движение или шорох,{w=0.2} и скит обдрищет свои штаники от гуччи."
    "Но скит думал сейчас только об одном."
    "Как бы не обосраться."
    window hide
    pause 1
    "Скит побежал в толчок."
    ineony "Парашу заминировала?"
    bergen "Ясен хуй."
    bergen "Там вон камера стоит."
    bergen "Ща он досрёт,{w=0.2} и я активирую детонатор."
    ineony "Моя ты умница!"
    window hide
    pause 1
    scene tolkan with flash
    skt "Как же ахуенно..."
    "Скин начал надристывать полный унитаз говна."
    "Он хотел насрать такую кучу,{w=0.2} чтоб не смылась потом."
    "И он начал издавать анальные симфонии."
    play sound rid1
    pause 1
    play sound rid2
    pause 1
    play sound rid3
    pause 1
    play sound rid4
    pause 1
    play sound rid5
    pause 1
    play sound rid6
    pause 1
    play sound rid7
    pause 1
    play sound rid8
    pause 1
    skt "Фух,{w=0.2} вроде досрал."
    window hide
    pause 1
    "Скит было уже собирался пробывать смыть своё говно,{w=0.2} но {nw}"
    play sound timer
    "Скит было уже собирался пробывать смыть своё говно,{w=0.2} но {fast}{w}его смутил звук."
    skt "Вот это вы классно придумали."
    skt "Я даже сначала не понял."
    skt "А потом как понял."
    skt "Так ахуел."
    window hide
    pause 1
    "А последними словами Димона были:"
    stop music
    play sound maloletka
    pause 2
    play sound csgo
    pause 2
    scene black with flash
    pause 2
    stop sound fadeout 2
    pause 2
    play music leto1 fadein 3
    scene mogila with dissolve
    window hide
    pause 1
    ineony "Вот и помер дядя дима..."
    ineony "Грустно это всё конечно."
    window hide
    pause 1
    ineony "Мне трудно даются эти слова..."
    window hide
    pause 1
    ineony "Скит был хорошим конкурентом."
    ineony "Честным."
    window hide
    pause 1
    ineony "Никогда не желал нам зла..."
    scene mall with flash
    play sound ebanko
    pause 2
    scene mogila with flash
    window hide
    pause 1
    ineony "Никогда не обзывал..."
    scene tolkan with flash
    play sound maloletka
    pause 2
    scene mogila with flash
    window hide
    pause 1
    "Он повернулся к BERGEN."
    scene mogila1 with dissolve
    ineony "Чё я несу,{w=0.2} ёпта?"
    ineony "Туда ему и дорога!"
    ineony "Вапдомик на том свете пусть сидит делает."
    window hide
    pause 1
    ineony "А ты что думаешь?"
    window hide
    pause 1
    bergen "Хочу питсы."
    window hide
    pause 1
    bergen "Ну,{w=0.2} если бы у меня была возможность,{w=0.2} перед его смертью я бы ему сказала..."
    bergen "Земля тебе стекловатой,{w=0.2} лысый урод."
    bergen "Стулья тебе хуями дрочёнными,{w=0.2} понял,{w=0.2} пёс?{w=0.2} Добирманчик бля."
    play sound smeh
    window hide
    pause 3
    "Айнеони от души проорал."
    window hide
    pause 1
    ineony "Ну что{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} Пойдём?"
    bergen "Трахаться с тобой я не буду."
    ineony "Больно надо{w=0.2}.{w=0.2}.{w=0.2}."
    ineony "Я вообще хотел предложить тебе пропустить пару стаканчиков на упокой вапгомика,{w=0.2} так-то{w=0.2}.{w=0.2}.{w=0.2}."
    bergen "А{w=0.2}а{w=0.2}а{w=0.2}.{w=0.2} Ну за это я всегда за!"
    scene mogila with dissolve2
    stop music fadeout 5
    "И они ушли."
    "А Дядя Дима остался тут."
    "Червей кормит."
    "Своим говном."
    window hide
    pause 1
    "Ай,{w=0.2} в пизду."
    "Пускай титры нахуй."
    play music leto2 fadein 3
    window hide
    pause 3
    show credits Text (about_text, size=50, text_align=0.5):
        xalign 0.5
        ypos 1
        linear 40.0 ypos -2.84
    $ renpy.pause(5, hard = True)
    $ renpy.pause(37)
    stop music fadeout 6
    window hide
    jump huinya

label bergeneblan:
    stop music fadeout 5
    scene black with dissolve2
    $ renpy.pause(4, hard=True)
    $ renpy.block_rollback()
    play music intig1 fadein 4
    scene bergenshiza with dissolve4
    window hide
    pause 1
    skt "У нас с тобой ещё могло получиться договориться,{w=0.2} но{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    skt "Какое же жалкое зрелище."
    window hide
    pause 1
    skt "Это ж надо было умудриться{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Ахах{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    skt "Я ведь говорил..."
    window hide
    pause 1
    skt "{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}что написал заяву{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    skt "Ответь мне только на один вопрос."
    window hide
    pause 1
    skt "К чему тебя привело твоё упрямство?"
    window hide
    pause 1
    skt "И сама не спаслась,{w=0.2} и дружков погубила{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Не будет никакой спасательной операции."
    bergen "Заткнись."
    window hide
    pause 0.5
    skt "Ты нахуй никому не нужна."
    play music intig11
    scene bergenshiza with vpunch
    bergen "ЗАТКНИСЬ!"
    scene bergenshiza with vpunch
    skt "АХАХА НАХУЙ)"
    scene bergenshiza with vpunch
    skt "АЙНЕОНИ ТВОЙ СЛИЛСЯ,{w=0.2} КАК ЖАРЕННЫМ ЗАПАХЛО,{w=0.2} ДА?"
    scene bergenshiza with vpunch
    skt "КТО Ж ТЕБЕ ТЕПЕРЬ ПОМОЖЕТ?))"
    scene bergenshiza with vpunch
    skt "А?!"
    window hide
    pause 2
    "BERGEN ему ничего не ответила."
    window hide
    pause 0.5
    skt "И как тебе со срока только удалось соскочить{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}{nw}"
    scene bergenshiza with vpunch
    bergen "СОСКОЧИТЬ?"
    scene bergenshiza with vpunch
    bergen "ТЫ ЕБЛАН ИЛИ ПРИТВОРЯЕШЬСЯ?"
    scene bergenshiza with vpunch
    bergen "Тебе повезло сука,{w=0.2} что у меня руки связаны."
    bergen "Второго шанса я не упущу."
    stop music fadeout 5
    skt "Поживём,{w=0.2} увидим."
    window hide
    pause 2
    skt "Я ещё вернусь."
    bergen "Иди на хуй."
    bergen "Лысая кочерыжка,{w=0.2} блин."
    window hide
    pause 1
    $ renpy.movie_cutscene('screen/bergen4mo.ogv')
    scene black
    play music discoblackmetal fadein 2
    scene bergenokno228 with dissolve2
    show doshd
    show bergenokno229
    window hide
    pause 2
    "Эта история бёрет начало здесь."
    "Скиту бизнесмену слили все данные про BERGEN."
    "Слил их iNeoony."
    "Или это был pechorsky?"
    play sound herznaet
    window hide
    pause 2
    "Это сейчас не важно."
    "У BERGEN большие проблемы."
    window hide
    pause 1
    bergen "Скит таки написал заяву{w=0.2}.{w=0.2}.{w=0.2}."
    "Эта мысль не выходила из головы."
    "Было тошно."
    "Ненависть затуманила разум."
    bergen "Я это так не оставлю."
    window hide
    pause 1
    "Ей нужно было найти iNeoony."
    bergen "Только вот как{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    "BERGEN решила сесть за комп."
    stop music fadeout 5
    scene black with dissolve2
    scene bergenbook with dissolve2
    play music flatline fadein 2
    window hide
    pause 1
    bergen "Ни глотка аскании не осталось{w=0.2}.{w=0.2}.{w=0.2}."
    bergen "Пиздец{w=0.2}.{w=0.2}.{w=0.2}."
    play sound tg
    "Ей пришло в тг сообщение от глицинчика."
    glc "Нам пизда."
    play sound tg
    glc "Скитови написал заяву."
    play sound tg
    glc "Лови гс,{w=0.2} которую он приводит как пруф."
    play sound govnoloh
    window hide
    pause 8
    play sound tg
    bergen "Я знаю."
    window hide
    pause 1
    play sound tg
    glc "Видишь ли в чём дело{w=0.2}.{w=0.2}.{w=0.2}."
    play sound tg
    glc "iNeoony всё скинул на тебя."
    play sound tg
    glc "И едут они только за тобой."
    play sound tg
    bergen "Ты никак не мог этому помешать?"
    play sound tg
    glc "Вообще нихуя."
    play sound tg
    glc "Я бля парил сидел свой мегаподик,{w=0.2} и тут ебать переслали скита смс."
    play sound tg
    bergen "Пизда."
    "BERGEN решила подойти к окну."
    scene bergenokno228 with dissolve2
    show doshd
    show bergenokno229
    window hide
    pause 2
    "Возле падика стоял наряд мусаров."
    window hide
    pause 2
    bergen "Извиняюсь,{w=0.2} конечно,{w=0.2} за мат{w=0.2}.{w=0.2}.{w=0.2}."
    bergen "Пизда."
    window hide
    pause 2
    "BERGEN поняла,{w=0.2} что бежать некуда."
    "Осталась только крыша."
    scene bergendie1 with dissolve2
    show doshd
    bergen "Неужели это конец?"
    bergen "Ебучий айнеони{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    bergen "Это ж надо было{w=0.2}.{w=0.2}.{w=0.2}."
    show blink
    window hide
    pause 1
    "BERGEN закрыла глаза."
    "Сами по себе начали течь слёзы."
    "От ощущения безысходности на душе в один миг стало настолько горько,{w=0.2} что{w=0.2}.{w=0.2}.{w=0.2}."
    scene black
    hide blink
    window hide
    pause 1
    play music intig22
    scene bergendie with vpunch
    show doshd
    "BERGEN с разбегу полетела вниз."
    window hide
    pause 0.5
    "Холодный ветер обдувает тело."
    "Которое с бешенной скоростью летит вниз."
    window hide
    pause 0.5
    "17 этажей{w=0.2}.{w=0.2}.{w=0.2}."
    "Разве можно выжить после такого падения?"
    stop music
    play sound padenie
    scene black with flash
    window hide
    pause 1
    "Но{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 2
    scene palata
    show unblink
    bergen "Бляяя{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    hide unblink
    scene skitpalata with flash
    skt "Думала самовыпилом от меня скрыться? {w}Ахаха{w=0.2}.{w=0.2}.{w=0.2}.{nw}"
    play music intig22
    play sound padenie
    scene palata with vpunch
    bergen "ХУЙ ТЕБЕ!"
    "BERGEN поползла к выходу из палаты."
    scene palata1
    play sound razebal
    pause 1.5
    scene palata2 with flash
    pause 0.4
    scene palata3 with flash
    bergen "СУКИИИ!!!!"
    scene bergensanitari with flash
    "BERGEN схватили санитары."
    scene bergensanitari with vpunch
    bergen "ПУСТИТЕ МЕНЯ СУКИ!!!"
    sanitar "Сестра,{w=0.2} коли быстрее,{w=0.2} блин!"
    stop music fadeout 3
    show blink
    "И BERGEN отключилась."
    scene black
    hide blink
    window hide
    pause 2
    play music ddlc fadein 4
    scene bergenshiza with dissolve4
    bergen "Это уже какой-то пиздец идёт,{w=0.2} БУДИТЕ МЕНЯ НАХУЙ!"
    window hide
    pause 1
    bergen "Это не сон{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    "В палату вошел санитар."
    sanitar "К вам гости."
    bergen "Кто блять?"
    window hide
    pause 1
    skt "Здарова бандитка."
    window hide
    pause 1
    "Ни сил,{w=0.2} ни желания истерить не было."
    "Её накачали мощными транквилизаторами."
    "То,{w=0.2} что она,{w=0.2} пусть и туговато соображет -{w=0.2} уже чудо нахуй."
    window hide
    pause 1
    "Да и куда делись все многочисленные переломы?"
    "Я бы мог ответить в стиле:"
    play sound herznaet
    window hide
    pause 1.5
    "Но просто прошло уже пол года."
    "Из за ахуенных веществ BERGEN ничего не помнит об этом времени."
    "Всё зажило."
    "Кроме одной большой душевной раны."
    bergen "Ты нашёл айнеони?"
    skt "Да.{w=0.2} Он дал мне твои контакты."
    skt "В обмен на сохранность своей жопы."
    stop music fadeout 2
    window hide
    pause 2
    play music walesmus fadein 2
    bergen "Что теперь со мной будет?"
    skt "Ну как сказать{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 0.5
    play sound prosnulsa1
    pause 1.5
    play sound prosnulsa2
    pause 1
    bergen "Ахах{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    skt "А какие ощущения были в начале?"
    skt "Не подумай ничего,{w=0.2} мне просто интересно{w=0.2}.{w=0.2}.{w=0.2}."
    bergen "Ну{w=0.2}.{w=0.2}.{w=0.2}."
    play sound zlosti
    window hide
    pause 5
    skt "Даа{w=0.2}.{w=0.2}.{w=0.2}."
    bergen "Теперь ты будешь посещать меня до конца моих дней и издеваться?"
    skt "Именно."
    skt "Такие хуемрази как ты должны страдать."
    bergen "А ты не думал,{w=0.2} что под транквилизаторами мне-то в принципе и похуй так-то,{w=0.2} а?"
    skt "Хорошо."
    skt "Больше тебе их выдавать не будут."
    "И зачем только спизданула?{w=0.2} Тупая дура."
    window hide
    pause 1
    skt "Ну,{w=0.2} мне пора идти."
    skt "Скоро увидимся."
    play sound opend
    "Скитецкий ушёл."
    "Он оставил BERGEN в полном одиночестве.{w=0.2} Санитар вышел после того,{w=0.2} как зашел скит."
    bergen "Это конец."
    bergen "Всё началось с любопытства."
    window hide
    pause 3
    show credits Text (about_text1, size=50, text_align=0.5):
        xalign 0.5
        ypos 1
        linear 40.0 ypos -2.84
    $ renpy.pause(5, hard = True)
    $ renpy.pause(37)
    stop music fadeout 6
    window hide
    jump huinya

label novoshahtinsk:
    scene black with dissolve2
    play music nightmaremus fadein 5
    scene nmall with flash
    show doshd with dissolve
    "Дмитрий ехал по Новошохтинску на своём некро-ведре."
    "Из хрипящих динамиков доносился до ушей старый добрый русский транс."
    "Движок десятки пердел,{w=0.2} хрипел,{w=0.2} умирал,{w=0.2} но,{w=0.2} сука,{w=0.2} работал."
    "Самое главное -{w=0.2} что ехал."
    "Иначе Димка бы ехал на маршрутке."
    "С бабками.{w} Которые не моются."
    "И тогда бы ему было пиздец как грустно."
    window hide
    pause 1
    "Куда он едет?"
    play sound herznaet
    window hide
    pause 1.6
    "Димка повернул в сторону своей trap хаты."
    scene traphata with dissolve2
    show doshd
    window hide
    pause 1
    "Выглядит как бомжатник?"
    "У{w=0.2}у{w=0.2}у{w=0.2},{w=0.2} это вы ещё внутри не были!"
    "Там вообще пиздец свалка нахуй."
    "Как говорит Димасек:"
    skt "Главное -{w=0.2} кто пахан.{w=0.2} Остальное не ебёт.{w=0.2} Если,{w=0.2} конечно,{w=0.2} ты не под шконкой))){w=0.2} гы"
    window hide
    pause 1
    scene domext
    play sound tazik1
    show doshd
    "Доместос Скитов припарковал свой тазик,{w=0.2} обклеенный аниме наклейками с зеро ту."
    play sound tazik2
    "Оставив тазик гнить под открытым небом,{w=0.2} Скит отправился домой."
    scene domint with dissolve2
    window hide
    pause 1
    "Зайдя, как полагается,{w=0.2} на хату,{w=0.2} Дерьмон начал думать{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Чем бы заняться сука?"
    window hide
    pause 1
    "Димка решил поклацать свой пк."
    scene pc with dissolve2
    "Его комп на AMD Athlon 64 4000+ с 256 мб ддр1 еле тянул браузер."
    "А IDE хард на 40 гигов был забит файлами для прошивки на LegionOS."
    skt "ДА ЗАГРУЖАЙСЯ БЫСТРЕЕ,{w=0.2} СУКА!"
    play sound udarklava
    "Скитолс въебал двоечку по клавиатуре ps/2."
    window hide
    pause 2
    skt "Чи ссд поставить?"
    stop music fadeout 5
    window hide
    pause 1
    "Не долго думая,{w=0.2} Димка решил отправится в DNS в своём любимом тц Новошахтинск MALL."
    scene traphata with dissolve2
    show doshd
    window hide
    pause 1
    skt "Ща по фасту все сделаем."
    skt "Хули время терять."
    "И Димка поехал в тц."
    play music sleeper fadein 2
    scene nmall with dissolve2
    show doshd with dissolve
    "Димас припарковал свой тазик и вышел на улицу."
    scene novomall
    show doshd
    window hide
    pause 1
    skt "Бля там охранник сука."
    scene propusk with dissolve2
    "Предъявив охране свой паспорт,{w=0.2} Дима отправился гулять по тц."
    scene nmallint with dissolve2
    window hide
    pause 3
    "Димка таки купил ссд."
    "Это был Goldenfir на 120 гб."
    "Доместос отдал за него three hundred bucks."
    "Зато теперь его windows 98 будет загружаться очень быстро."
    window hide
    pause 1
    "Дима решил по пути к своему тазику заскачить в толчок."
    "И обоссать там весь ободок."
    "Так,{w=0.2} напоследок."
    skt "Почему нет?"
    "Думал Дима."
    "И отправился в толчок."
    play music doom1 fadein 3
    scene parashanmall with dissolve2
    "Скит залетел в парашу."
    window hide
    pause 1
    scene tolkanb with dissolve
    "Его взягляд остановился на одной особе{w=0.2}.{w=0.2}.{w=0.2}."
    "Которая мыла свои прекрасные руки."
    window hide
    pause 1
    "Скит набирается смелости и решается подкатить к ней."
    scene parashanmall with flash
    "Далее от лица BERGEN."
    window hide
    pause 0.5
    show skit3 with dissolve
    "Это ещё что за дцпешник?"
    "BERGEN тратила все сила организма на то,{w=0.2} чтобы сдержать истерический хохот."
    "Это было {w=0.2}РЕАЛЬНО{w=0.2} сложно."
    "Такого дцпешника не каждый день увидишь."
    window hide
    pause 1
    play sound z1
    pause 1
    skt "Не желаешь познакомится?"
    "BERGEN прихуела от такого кривого базара со стороны патау додика."
    play sound gofuck
    window hide
    pause 4
    skt "Ты ранила меня в самое сердце("
    skt "Хотя я всё ещё очень хочу тебя выебать."
    skt "Пиздец как."
    show blink
    "BERGEN переполняла ненависть."
    "Она пыталась её контролировать,{w=0.2} но{w=0.2}.{w=0.2}.{w=0.2}."
    hide skit3
    hide blink
    show hernya_kakaya_toMVWWW777 with flash
    play music doom2
    show skit2:
        zoom 2.0
        ypos 0.0
        pause (0.38)
        linear 0.09 ypos -0.07
        linear 0.09 ypos 0.0
        pause (0.19)
        repeat

    show dlya_ebalaMVWWW777:
        xpos 1.0
        ypos 1.0
        linear 0.20 xpos -0.0 ypos -0.0
        pause (0.40)
        linear 0.15 xpos 1.0 ypos 1.0
        pause (1.0)
        repeat





    show dlya_ebalaleftMVWWW777:
        xpos -1.0
        ypos 0.5
        pause (1.0)
        linear 0.20 xpos -0.0 ypos -0.0
        pause (0.40)
        linear 0.15 xpos -1.0 ypos 0.5

        repeat



    $ renpy.pause (0.39)


    window show
    skt "Та за шо?"
    bergen "За всё хорошее."
    window hide
    pause 1
    bergen "Тебе пизда,{w=0.2} щенок."
    skt "Бляяя,{w=0.2} я всего-то хотел,{w=0.2} чтобы ты села мне на лицо("
    "Пизда копчёному."
    "Ну,{w=0.2} в переносном смысле."
    "BERGEN девушка приличная и дцпешникам не даёт."
    "Точнее,{w=0.2} никому не даёт."
    window hide
    pause 1
    bergen "Извиняйся,{w=0.2} пока не поздно{w=0.2}.{w=0.2}.{w=0.2}."
    bergen "Лысая ты хуйня!"
    skt "Даже если ты не бреешь,{w=0.2} я тогов вылизать там всё,{w=0.2} моя богиня!"
    "Какая-то ебатория уже пошла."
    "Пора прекращать пизделку."
    window hide
    pause 1
    hide hernya_kakaya_toMVWWW777 with dissolve
    hide dlya_ebalaMVWWW777
    hide dlya_ebalaleftMVWWW777
    hide skit2
    with dissolve
    stop sound
    "BERGEN делает финальный хук в ебло лысой гниды."
    window hide
    show skit1 with dissolve:
        xpos -0.05 ypos -0.37 zoom 3.0
        pause (0.38)
        linear 0.19 ypos -0.42
        linear 0.19 ypos -0.33
        linear 0.19 ypos -0.30
        linear 0.19 ypos -0.37
        pause (0.19)

    show dlya_ebalaMVWWW777:
        xpos 1.0
        ypos 1.0
        linear 0.20 xpos -0.0 ypos -0.0
        pause (0.50)
        linear 0.15 xpos 1.0 ypos 1.0

    play sound udarMVWWW777
    $ renpy.pause (0.5)
    hide hernya_kakaya_toMVWWW777 with dissolve
    show skit1 with dissolve:
        xpos -0.05 ypos -0.37 zoom 3.0
        pause (0.2)
        linear 1.0 ypos 1.5
    play sound padenie
    pause 1
    play sound fatalitysound
    pause 2
    window show
    bergen "Ибо нехуй.{w} Лезьть.{w} КО МНЕ БЛЯТЬ!"
    stop music fadeout 3
    window hide
    pause 3
    "BERGEN ушла по своим делам."
    window hide
    pause 1
    show skit3
    "Димасек поднялся и отряхнулся."
    window hide
    pause 1
    $ renpy.movie_cutscene('screen/classicmovie.ogv')
    play music xarakter
    scene ineonyllc1 with dissolve
    ineony "Вы утверждаете,{w=0.2} что вам насолил Дима Скит?"
    bergen "Да."
    bergen "Я очень хочу,{w=0.2} чтобы вы его не кисло наказали!"
    window hide
    pause 1
    ineony "Вы же понимаете,{w=0.2} что эта услуга будет стоить дорого{w=0.2}.{w=0.2}.{w=0.2}."
    bergen "{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    ineony "Ладно,{w=0.2} об этом потом."
    window hide
    pause 1
    ineony "Почему вы выбрали именно нас?"
    bergen "М."
    bergen "Хорошие отзывы в интернете{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    ineony "И что же вам такого Скитови сделал только?"
    window hide
    pause 1
    bergen "Я{w=0.2}.{w=0.2}.{w=0.2}.{w} Не хочу об этом{w=0.2}.{w=0.2}.{w=0.2}. {w}Говорить{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    ineony "Ладно."
    bergen "Так вы согласны?"
    ineony "Конечно."
    scene ineonyllc with flash
    "Проводив BERGEN до лифта,{w=0.2} Айнеони начал думать."
    "План сразу же выстроился в его голове."
    ineony "Сначала уроним забор{w=0.2}.{w=0.2}.{w=0.2}."
    ineony "Затем уроним парашу{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    "Но и тут Айнеони решил блеснуть генаильностью{w=0.2}.{w=0.2}.{w=0.2}."
    "Используя для крушения забора килограм тротилла."
    scene zaborskit with dissolve
    "Нахуя-то он начал снимать это на видео."
    window hide
    stop music
    play sound zabor1
    pause 21
    scene zaborskit1
    window hide
    play sound csgo1
    window hide
    pause 1.2
    scene zaborskit2
    pause 0.8
    play sound csgo
    pause 2
    scene zaborskit3
    pause 0.4
    scene zaborskit4
    play sound zabor
    window hide
    pause 5
    scene zaborskit4 at beg
    window hide
    pause 5
    scene domext at beg
    window hide
    pause 4
    scene domext at beg_end
    window hide
    pause 3
    "Но Айнеони на этом не остановился."
    window hide
    pause 1
    scene skittolkan1 with dissolve
    "На втором рейде он решил уронить скитовый туалет."
    "Естественно своим фирминным способом с оперативной съёмкой."
    window hide
    play sound tualetskit
    pause 22
    $ renpy.movie_cutscene('screen/skitsret1.ogv')
    play sound tolkan4
    window hide
    pause 3
    scene skittolkan2
    play sound csgo1
    window hide
    pause 1.2
    scene skittolkan3
    pause 0.8
    $ renpy.movie_cutscene('screen/skitsret2.ogv')
    scene skitupalvtolkan
    play sound tolkan6
    window hide
    pause 12
    play music dvakbaksov fadein 1
    scene skitserun with dissolve4
    window hide
    pause 1
    "На следующий день Айнеони сидел на крыше высотки офиса своей компании и курил электронную сигарету."
    "Вдалеке он разглядел какую-то хуйню."
    scene skitserun1
    "Он достал камеру чтобы приблизить."
    window hide
    pause 1
    play sound smeh4
    window hide
    pause 7
    play sound ksm7
    pause 5
    window hide
    pause 2
    ineony "Бля,{w=0.2} я же ему туалет взорвал,{w=0.2} где ему срать теперь,{w=0.2} если не на крыше?"
    "Вспомнив в деталях весь процесс,{w=0.2} Айнеони чуть не упал нахуй с крыши от смеха."
    play sound smeh2
    window hide
    pause 6
    scene ineonyllc with dissolve2
    "Когда Айнеони зашел в офис,{w=0.2} он набрал BERGEN и назначил встречу прямо сейчас."
    scene ineonyllc1 with flash
    "Когда BERGEN явиалсь,{w=0.2} Айнеони показал ей все видеозаписи и фото срущего на крыше скита."
    window hide
    pause 1
    bergen "Не кисло."
    bergen "Так что там насчёт оплаты?"
    ineony "Вашей невинности будет достаточно{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}{nw}"
    bergen "Каво?"
    ineony "Я говорю,{w=0.2} что с вас лишь экранизация этого чуда."
    ineony "Я хочу сделать из студии кибербуллинга студию разработки игр."
    bergen "Предлагаете мне на вас работать?"
    ineony "Именно."
    bergen "Ну хорошо."
    ineony "Вот и отлично!"
    "После этого они заключили контракт."
    stop music fadeout 3
    scene black with flash
    window hide
    pause 3
    "На следующий день BERGEN позвонил Скит и назначил встречу в баре,{w=0.2} где он работает сантехником."
    play music gramatik fadein 3
    scene nitro4 with dissolve4
    window hide
    pause 1
    bergen "Ну и где этот мудак?"
    "Нахлынувшие воспоминания дали понять BERGEN,{w=0.2} где искать Скита."
    "Он отправилась в толкан."
    "Далее от лица Скитови."
    scene rabota:
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
    skt "Фух мля{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Последний{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    "Дмитрий был под таблеткой триганчика."
    "Это,{w=0.2} типа,{w=0.2} чтоб веселее работать было."
    bergen "Здарова,{w=0.2} уебан."
    hide tripsMVWWW777
    scene rabota with flash
    "Весь трип как рукой сняло."
    skt "Привки."
    bergen "Зачем звал?"
    "Скит понял,{w=0.2} что чистка последнего толчка откладывается."
    skt "Пойдем."
    "И они пошли в бар."
    scene rabota3 with dissolve2
    window hide
    pause 1
    bergen "Зачем звал-то?"
    skt "Слушай{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Прости меня пожалуйста,{w=0.2} я не хотел тебя обидеть!"
    "BERGEN вспомнила про фокусы Айнеони."
    "Нереальный ор сдерживать было так же нереально."
    "Но у неё всегда получалось."
    skt "Я правда не хотел!"
    bergen "{w=0.2}.{w=0.2}.{w=0.2}.кхых.{w=0.2}.{w=0.2}.{w=0.2} Ладно."
    bergen "Я тебя прощаю{w=0.2}.{w=0.2}.{w=0.2}. ихихи{w=0.2} бля{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Правда?"
    bergen "Конечно{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} ахаха.{w=0.2}.{w=0.2}."
    window hide
    pause 1
    bergen "Я могу идти?"
    skt "Да."
    scene nitro4 with dissolve
    stop music fadeout 5
    "И BERGEN ушла."
    "Скит приступил к очистке последнего толчка."
    play music lostalphaending fadein 3
    scene bergenbook with flash
    "BERGEN приступила к написанию сценария для экранизации истории Дмитрия Скитецского."
    "Она потела и старалась{w=0.2}.{w=0.2}.{w=0.2}."
    "И Айнеони оценил."
    "Как и все сотрудники iGandone LLC."
    window hide
    pause 2
    ineony "Счастливый конец,{w=0.2} типа?"
    bergen "Да."
    bergen "Ща пойдут титры."
    window hide
    pause 3
    show credits Text (about_text, size=50, text_align=0.5):
        xalign 0.5
        ypos 1
        linear 40.0 ypos -2.84
    $ renpy.pause(5, hard = True)
    $ renpy.pause(37)
    stop music fadeout 6
    window hide
    jump huinya

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
