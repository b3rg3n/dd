init:
    image movie = Movie(size=(config.screen_width, config.screen_height))

    $ mods["splashscreenskita"]=u"Skitetsky Story"

label splashscreenskita:
    scene disk with flash
    play sound ins
    pause 5
    scene black with dissolve
    play sound bergintro
    pause 4
    $ renpy.movie_cutscene('screen/zastavochka1skit.ogv')
    jump skitovijmenu


define skt = Character('Дмитрий Скитецкий', color="#c8ffc8")
define cf = Character('ColdfSociety', color="#c8ffc8")
define berg = Character (u'thestrelok228', color = "#20B2AA")
define syava = Character (u'Сява', color = "#FF0000")
define ded = Character (u'deadlyxrd', color = "#c8ffc8")
define shepid = Character (u'Depesh1977', color = "#dd9933")
define tunechi = Character (u'k1ceargy', color = "#dd9933", what_outlines=[ (1, "#ffffff") ])
define ineony = Character (u'ineoony', color = "#dd9933", what_outlines=[ (1, "#b30000") ])
define th2 = Character (u' ', color = "#dd9933", what_outlines=[ (1, "#2488cf") ])
define lam = Character (u'Lameni', color="00ffff", what_color="ffffff")
define podsos = Character (u'Подсос', color="00ffff", what_color="ffffff")
define monolit = Character (u'Исполнитель желаний', color="00ffff", what_color="ffffff")
define island = "audio/sleeper.ogg"
define dzvuk = "audio/mndrainstr.ogg"
define suka1 = "audio/suka1.ogg"
define suka2 = "audio/suka2.ogg"
define suka3 = "audio/suka3.ogg"
define suka4 = "audio/suka4.ogg"
define smeh = "audio/ksm9.ogg"
define tg = "audio/tg.ogg"
define opend = "audio/door_squeak_light.ogg"
define kashel = "audio/kashel.ogg"
define stuk = "audio/stuk.ogg"
define islandcut = "audio/islandcut.ogg"
define introcut = "audio/introcut.ogg"
define ins = "audio/intro.ogg"
define sonmus = "audio/mir_stih.ogg"
define drink = "audio/drink.ogg"
define dedost = "audio/dedost.ogg"
define crysis3 = "audio/crysis3.ogg"
define mooze = "audio/wasteland2_r.ogg"
define zovut = "audio/syava.ogg"
define opanihuya = "audio/nihuya.ogg"
define skitbuhaet = "audio/retro_spec_chapter_one.ogg"
define freeman = "audio/freeman.ogg"
define noj1 = "audio/knife_hit1.ogg"
define noj2 = "audio/knife_hit2.ogg"
define noj3 = "audio/knife_hit3.ogg"
define maloletka = "audio/maloletka.ogg"
define ebanko = "audio/ebanko.ogg"
define posral = "audio/posral.ogg"
define ntema = "audio/sheped.ogg"
define intro1 = "audio/intro1.ogg"
define geniy = "audio/geniy.ogg"
define prosto = "audio/prosto.ogg"
define plan = "audio/plan.ogg"
define flatline = "audio/Scattle - Flatline.ogg"
define tolkan1 = "audio/tolkan1.ogg"
define tolkan2 = "audio/tolkan2.ogg"
define tolkan3 = "audio/tolkan3.ogg"
define tolkan4 = "audio/tolkan4.ogg"
define tolkan5 = "audio/tolkan5.ogg"
define tolkan6 = "audio/tolkan6.ogg"
define skit4mo = "audio/tempest.ogg"
define surge228 = "audio/surge.ogg"
define grena0 = "audio/grena0.ogg"
define nitro = "audio/nitro.ogg"
define chisti = "audio/chisti.ogg"
define grena1 = "audio/grena1.ogg"
define dostal = "audio/generic_holster.ogg"
define bergintro = "audio/bergintro.ogg"
define ustal = "audio/breath_1.ogg"
image shaht = Image("images/1.jpg")
image shaht2 = Image("images/2.jpg")
image avto = Image("images/avto.jpg")
image avto1 = Image("images/zastavka.jpg")
image dom = Image("images/dom1.jpg")
image hatabuh = Image("images/dom.jpg")
image zercalo = Image("images/dima_zver.jpg")
image legion4ik = Image("images/legion4ik.jpg")
image ostanovka = Image("images/ostanovka.jpg")
image kuhnya = Image("images/kuhnya.jpg")
image pomer = Image("images/pomer.jpg")
image 4atik = Image("images/4atik.jpg")
image son1 = Image("images/son1.png")
image son2 = Image("images/son2.png")
image son3 = Image("images/son3.png")
image son4 = Image("images/son4.png")
image son5 = Image("images/son5.png")
image disk = Image("images/disk.png")
image intro_legionorig = ("images/intro_legion.png")
image intro_kiberbullorig = ("images/intro_kiberbull.png")
image intro_vrtorig = ("images/intro_vrt.png")
image intro_transparent = ("images/intro_transparent.png")
image pomer = Image("images/pomer.jpg")
image kordon = Image("images/kordon.jpg")
image es = Image("images/es.jpg")
image tolkan = Image("images/tolkan.jpg")
image mall = Image("images/mall.jpg")
image sheped = Image("images/sheped.png")
image strelok = Image("images/strelok.png")
image tun = Image("images/tun.png")
image grena = Image("images/grena.png")
image babah = Image("images/babah.png")
image nitro = Image("images/nitro.png")
image nitro1 = Image("images/nitro1.jpg")
image nitro2 = Image("images/nitro2.jpg")
image nitro3 = Image("images/nitro3.jpg")
image nitro4 = Image("images/nitro4.jpg")
image rabota = Image("images/rabota.jpg")
image rabota1 = Image("images/rabota1.jpg")
image rabota2 = Image("images/rabota2.jpg")
image vilka = Image("images/vilka.png")
image krisa = Image("images/doberman.png")

image menushka1story = Movie(fps=60, size = (1920, 1080), play="screen/menushkaskit.ogv")

label skitvibororig:
    call screen skitvibor1orig

screen legionos_screenorig:
    add "intro_legionorig" xalign 0.0 yalign 0.0

screen kiberbull_screenorig:
    add "intro_kiberbullorig" xalign 0.0 yalign 0.0

screen vrt_screenorig:
    add "intro_vrtorig" xalign 0.0 yalign 0.0

screen skitvibor1orig:

    modal False tag menu
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 635, 1080)):
            hovered [Show("legionos_screenorig", transition=Dissolve(0.5))]
            unhovered [Hide("legionos_screenorig", transition=Dissolve(1.0))]
            action [Hide("legionos_screenorig", transition=Dissolve(0.5)), Jump("legionoss")]
        hotspot ((635, 0, 652, 1080)):
            hovered [Show("kiberbull_screenorig", transition=Dissolve(0.5))]
            unhovered [Hide("kiberbull_screenorig", transition=Dissolve(1.0))]
            action [Hide("kiberbull_screenorig", transition=Dissolve(0.5)), Jump("zakiberbulil")]
        hotspot ((1287, 0, 634, 1080)):
            hovered [Show("vrt_screenorig", transition=Dissolve(0.5))]
            unhovered [Hide("vrt_screenorig", transition=Dissolve(1.0))]
            action [Hide("vrt_screenorig", transition=Dissolve(0.5)), Jump("vrtvoskresil")]

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
