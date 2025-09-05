python early:
    mods = {}

init python:
    style.mm_root.background = None 

    import random


    random.seed()




    def Snow(image, max_particles=50, speed=150, wind=100, xborder=(0,100), yborder=(50,400), **kwargs):
        """
        This creates the snow effect. You should use this function instead of instancing
        the SnowFactory directly (we'll, doesn't matter actually, but it saves typing if you're
        using the default values =D)

        @parm {image} image:
            The image used as the snowflakes. This should always be a image file or an im object,
            since we'll apply im transformations in it.

        @parm {int} max_particles:
            The maximum number of particles at once in the screen.

        @parm {float} speed:
            The base vertical speed of the particles. The higher the value, the faster particles will fall.
            Values below 1 will be changed to 1

        @parm {float} wind:
            The max wind force that'll be applyed to the particles.

        @parm {Tuple ({int} min, {int} max)} xborder:
            The horizontal border range. A random value between those two will be applyed when creating particles.

        @parm {Tuple ({int} min, {int} max)} yborder:
            The vertical border range. A random value between those two will be applyed when creating particles.
            The higher the values, the fartest from the screen they will be created.
        """
        return Particles(SnowFactory(image, max_particles, speed, wind, xborder, yborder, **kwargs))


    class SnowFactory(object):
        """
        The factory that creates the particles we use in the snow effect.
        """
        def __init__(self, image, max_particles, speed, wind, xborder, yborder, **kwargs):
            """
            Initialize the factory. Parameters are the same as the Snow function.
            """
            
            self.max_particles = max_particles
            
            
            self.speed = speed
            
            
            self.wind = wind
            
            
            self.xborder = xborder
            self.yborder = yborder
            
            
            
            
            self.depth = kwargs.get("depth", 10)
            
            
            self.image = self.image_init(image)
        
        
        def create(self, particles, st):
            """
            This is internally called every frame by the Particles object to create new particles.
            We'll just create new particles if the number of particles on the screen is
            lower than the max number of particles we can have.
            """
            
            if particles is None or len(particles) < self.max_particles:
                
                
                depth = random.randint(1, self.depth)
                
                
                
                
                depth_speed = 1.5-depth/(self.depth+0.0)
                
                return [ SnowParticle(self.image[depth-1],      
                                      random.uniform(-self.wind, self.wind)*depth_speed,  
                                      self.speed*depth_speed,  
                                      random.randint(self.xborder[0], self.xborder[1]), 
                                      random.randint(self.yborder[0], self.yborder[1]), 
                                      ) ]
        
        
        def image_init(self, image):
            """
            This is called internally to initialize the images.
            will create a list of images with different sizes, so we
            can predict them all and use the cached versions to make it more memory efficient.
            """
            rv = [ ]
            
            
            for depth in range(self.depth):
                
                p = 1.1 - depth/(self.depth+0.0)
                if p > 1:
                    p = 1.0
                
                rv.append( im.FactorScale( im.Alpha(image, p), p ) )
            
            return rv
        
        
        def predict(self):
            """
            This is called internally by the Particles object to predict the images the particles
            are using. It's expected to return a list of images to predict.
            """
            return self.image


    class SnowParticle(object):
        """
        Represents every particle in the screen.
        """
        def __init__(self, image, wind, speed, xborder, yborder):
            """
            Initializes the snow particle. This is called automatically when the object is created.
            """
            
            
            self.image = image
            
            
            
            
            if speed <= 0:
                speed = 1
            
            
            self.wind = wind
            
            
            self.speed = speed
            
            
            
            self.oldst = None
            
            
            self.xpos = random.uniform(0-xborder, renpy.config.screen_width+xborder)
            self.ypos = -yborder
        
        
        def update(self, st):
            """
            Called internally in every frame to update the particle.
            """
            
            
            if self.oldst is None:
                self.oldst = st
            
            lag = st - self.oldst
            self.oldst = st
            
            
            self.xpos += lag * self.wind
            self.ypos += lag * self.speed
            
            
            if self.ypos > renpy.config.screen_height or\
            (self.wind< 0 and self.xpos < 0) or (self.wind > 0 and self.xpos > renpy.config.screen_width):
                    
                    return None
            
            
            
            
            return int(self.xpos), int(self.ypos), st, self.image
init:
    image snow = Snow("images/anim/snow.png")
    image heavy_snow = Snow("images/anim/snow.png", max_particles=500)
    image movie = Movie(size=(config.screen_width, config.screen_height))

    transform beg:
        parallel:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.2 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.48 ypos 0.51
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.52 ypos 0.51
            repeat

    transform beg_end:
        ease 0.2 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5

image prologue_dream:
    "images/anim/prologue_1.png"
    pause 0.1
    "images/anim/prologue_2.png"
    pause 0.1
    "images/anim/prologue_3.png"
    pause 0.1
    "images/anim/prologue_2.png"
    repeat

image unblink:
    contains:
        "images/anim/blink_up.png"
        xalign 0 yalign 0
        ease 1.5 pos (0,-1080)
    contains:
        "images/anim/blink_down.png"
        xalign 0 yalign 0
        ease 1.5 pos (0,1080)

image blink:
    contains:
        "images/anim/blink_up.png"
        pos (0,-1080)
        ease 1.5 xalign 0 yalign 0
    contains:
        "images/anim/blink_down.png"
        pos (0,1080)
        ease 1.5 xalign 0 yalign 0

image doshd:
    contains:
        "images/anim/rain.png"
        xpos 0.5 ypos -1.0
    contains:
        "images/anim/rain.png"
        xpos -0.5 ypos -1.0
    contains:
        "images/anim/rain.png"
        xpos 0.5 ypos 0.0
    contains:
        "images/anim/rain.png"
        xpos -0.5 ypos 0.0
    contains:
        "images/anim/rain.png"
        xpos 0.5 ypos 1.0
    contains:
        "images/anim/rain.png"
        xpos -0.5 ypos 1.0
    contains:
        "images/anim/rain.png"
        xpos 0.5 ypos 2.0
    contains:
        "images/anim/rain.png"
        xpos -0.5 ypos 2.0
    block:
        yanchor 1.0
        linear 0.3 yanchor 0.0
        repeat

image mnd_a3_menu_3:
    contains:
        "screen/mnd_a3_menu_3_1.png"
    contains:
        "screen/mnd_a3_menu_3_2.png"
        alpha 0.0
        ease 2.6 alpha 1.0
        ease 2.6 alpha 0.0
        repeat

define flash = Fade(.25, 0, .75, color="#fff")
define dissolve2 = Dissolve(2.0)
define dissolve4 = Dissolve(4.0)

image lepestki:
    choice:
        "images/anim/lep_1.png"
    choice:
        "images/anim/lep_2.png"
    choice:
        "images/anim/lep_3.png"
    choice:
        "images/anim/lep_4.png"
    choice:
        "images/anim/lep_5.png"
    xanchor 0.5 yanchor 0.5 rotate 0
    parallel:
        choice:
            rotate 0
            linear 5 rotate 360
            repeat
        choice:
            rotate 0
            linear 7 rotate -360
            repeat
        choice:
            rotate 0
            linear 9 rotate 360
            repeat
        choice:
            rotate 0
            linear 11 rotate -360
            repeat
        choice:
            rotate 0
            linear 13 rotate 360
            repeat
        choice:
            rotate 0
            linear 15 rotate -360
            repeat

image ftf_moving_lepestki:
    "lepestki"
    parallel:
        choice:
            xpos -0.1 ypos 0.2
        choice:
            xpos -0.1 ypos 0.1
        choice:
            xpos -0.1 ypos 0.0
        choice:
            xpos 0.0 ypos -0.1
        choice:
            xpos 0.0 ypos -0.2
        choice:
            xpos 0.1 ypos -0.1
        choice:
            xpos 0.1 ypos -0.2
        choice:
            xpos 0.2 ypos -0.1
        choice:
            xpos 0.2 ypos -0.2
        choice:
            xpos 0.3 ypos -0.1
        choice:
            xpos 0.3 ypos -0.2
    parallel:
        choice:
            easeout 10 xpos 0.5
        choice:
            easeout 10 xpos 0.6
        choice:
            easeout 10 xpos 0.7
        choice:
            easeout 10 xpos 0.8
        choice:
            easeout 10 xpos 0.9
        choice:
            easeout 10 xpos 1.0
        choice:
            easeout 10 xpos 1.1
    parallel:
        choice:
            linear 7 ypos 1.1
        choice:
            linear 8 ypos 1.1
        choice:
            linear 9 ypos 1.1
        choice:
            linear 10 ypos 1.1
        choice:
            linear 10 ypos 1.1
    repeat

image lepestki_krutyatsa:
    contains:
        "ftf_moving_lepestki"
    contains:
        pause 0.5
        "ftf_moving_lepestki"
    contains:
        pause 1.0
        "ftf_moving_lepestki"
    contains:
        pause 1.5
        "ftf_moving_lepestki"
    contains:
        pause 2.0
        "ftf_moving_lepestki"
    contains:
        pause 2.5
        "ftf_moving_lepestki"
    contains:
        pause 3.0
        "ftf_moving_lepestki"
    contains:
        pause 3.5
        "ftf_moving_lepestki"
    contains:
        pause 4.0
        "ftf_moving_lepestki"
    contains:
        pause 4.5
        "ftf_moving_lepestki"
    contains:
        pause 5.0
        "ftf_moving_lepestki"
    contains:
        pause 5.5
        "ftf_moving_lepestki"
    contains:
        pause 6.0
        "ftf_moving_lepestki"
    contains:
        pause 6.5
        "ftf_moving_lepestki"
    contains:
        pause 7.0
        "ftf_moving_lepestki"
    contains:
        pause 7.5
        "ftf_moving_lepestki"
    contains:
        pause 8.0
        "ftf_moving_lepestki"
    contains:
        pause 8.5
        "ftf_moving_lepestki"
    contains:
        pause 9.0
        "ftf_moving_lepestki"
    contains:
        pause 9.5
        "ftf_moving_lepestki"

init:
    $ style.credits = Style(style.default)
    $ style.credits.font  = "fonts/corbelb.ttf"
    $ style.credits.color = "#fff"
    $ style.credits.drop_shadow = [ (1, 1), (1, 1), (1, 1), (1, 1) ]
    $ style.credits.drop_shadow_color = "#000"
    $ style.credits.italic = False
    $ style.credits.bold = False
    $ style.credits.text_align = 0.5
    $ style.credits.xmaximum = 0.8

    define about_text = "\nРазработчики:\nСценарий: BERGEN\nКод, скрипты: BERGEN\nХудожники:\nBERGEN\nBERGEN\nBERGEN\nBERGEN\nBERGEN\nBERGEN\nBERGEN\nТестеры, редакторы:\nBERGEN\nБлагодарности:\nSEXYNOS,\nsleepykid -\nза стимул доделать это говно\nМодам на бесконечное\nлето -\nза спизженный мною код;\nsleepykid - за помощь с мотивацией;\nМеталкорщикам -\nза предоставленные композиции\nна английском языке;\n\nУчастникам канала мемы новошахтинск рус за визуальный контент;\n\nА так же тем, кто помог материально:\nclownl3ss\nНикто\nНикто\nНикто\nНикто\nНикто\nНикто\nНикто\nНикто\nи многим другим, кто не пожертвовал анонимно.\n\nПоддержка: t.me/b3rg3n\n\n\n\n\n\n\n\n\nКОНЕЦ\n"
    define about_text1 = "\nДолбоёбы:\nШизаписания: BERGEN\nКодинг говна: BERGEN\nРисование членом на снегу:\nBERGEN\nBERGEN\nBERGEN\nBERGEN\nBERGEN\nBERGEN\nBERGEN\nГовножуи:\nBERGEN\nБлагодарностей не будет:\nSEXYNOS,\ngl1c1nch1k -\nза отсутсвие стимула доделать это говно\nМодам на бесконечное\nлето -\nза спизженный мною говнокод;\nСамой себе - за помощь с мотивацией;\nМеталкорщикам -\nза предоставленные композиции\nв интсрументальном виде;\n\nУчастникам канала мемы новошахтинск рус за дерьмовый контент;\n\nА так же тем, кто донатил:\nclownl3ss\nНикто\nНикто\nНикто\nНикто\nНикто\nНикто\nНикто\nНикто\nи немногим другим, кто не пожертвовал анонимно.\n\nПоддержка: t.me/b3rg3n\n\n\n\n\n\n\n\n\nКОНЕЦ БЛЯТЬ\n"


label main_menu:
    stop sound fadeout 1
    stop music fadeout 1
    scene menushka
    play music intig11
    call screen main_menu

label splashscreen:

    python:

        if not persistent.set_volumes:
            
            persistent.set_volumes = True
            
            _preferences.volumes['music'] = .65
            _preferences.volumes['sfx'] = 1.0
            _preferences.volumes['voice'] = .65

    scene mall with flash
    play sound z1
    pause 1
    $ renpy.movie_cutscene('screen/z2.ogv')
    scene tolkan
    play sound ebanko
    pause 1.5
    $ renpy.movie_cutscene('screen/z4.ogv')
    scene pomer
    play sound maloletka
    pause 2
    scene black with dissolve
    return


label vibornachala:
    call screen vibornachala1

screen legionos_screen:
    add "intro_legion" xalign 0.0 yalign 0.0

screen kiberbull_screen:
    add "intro_kiberbull" xalign 0.0 yalign 0.0

screen vrt_screen:
    add "intro_vrt" xalign 0.0 yalign 0.0

screen vibornachala1:

    modal False tag menu
    imagemap:
        ground "intro_transparent"
        hotspot ((0, 0, 635, 1080)):
            hovered [Show("legionos_screen", transition=Dissolve(0.5))]
            unhovered [Hide("legionos_screen", transition=Dissolve(1.0))]
            action [Hide("legionos_screen", transition=Dissolve(0.5)), Jump("novoshahtinsk")]
        hotspot ((635, 0, 652, 1080)):
            hovered [Show("kiberbull_screen", transition=Dissolve(0.5))]
            unhovered [Hide("kiberbull_screen", transition=Dissolve(1.0))]
            action [Hide("kiberbull_screen", transition=Dissolve(0.5)), Jump("skeetovijbank")]
        hotspot ((1287, 0, 634, 1080)):
            hovered [Show("vrt_screen", transition=Dissolve(0.5))]
            unhovered [Hide("vrt_screen", transition=Dissolve(1.0))]
            action [Hide("vrt_screen", transition=Dissolve(0.5)), Jump("bergeneblan")]

  # Decompiled by unrpyc_v1.2.0-alpha: https://github.com/CensoredUsername/unrpyc
