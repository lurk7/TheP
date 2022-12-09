# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(None, who_color="#baf8ff", what_font="arial.ttf", what_italic=True, what_size = 25)
define tali = Character("Tali", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define creature = Character("Creature", who_color="#FF0000", what_font="arial.ttf", what_bold=True, what_size = 25)
define serok = Character("Serok", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define unknow = Character("Unknown voice", who_color="#baf8ff", what_font="arial.ttf", what_italic=True, what_size = 25)
define jesora = Character("Jesora", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define deadkrogan = Character("Krogan's voice", who_color="#FF4500", what_font="arial.ttf", what_size = 25)
define asari = Character("Asari", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define krogan = Character("Krogan", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define dis = Dissolve(.5)

image clips = "images/items/clips.png"
image parts = "images/items/parts.png"
image gren = "images/items/grenade.png"
image doorexp = "images/items/doorexp.png"
image keycard1 = "images/items/keycard.png"
image hacknumber = "images/skills/hacker/number.png"
image dogbone = "images/items/dogbone.png"
image lube = "images/items/lub.png"

define flag1 = True
define flag2 = True
define flag3 = True
define heartBorder1 = 0
define heartBorder2 = 0
define heartSlider = False
define days = 1
define whDoor = True
define barracksDoor = True
define comDoor = False
define engDoor = False
define bayDoor = False
define secFirst = True
define hallFirst = True
define prisFirst = True
define prisCum = False
define comCum = False
define jesora1 = False
define tabletHacked = False
define lockQuest = False
define barrackskey = False
define isLube = False

define comroom = True
define engine = False
define warehouse = False
define bay1 = False
define bay1first = True
define bay2 = False
define barracks = False
define prison = False
define hallway = False

define comroom_crate1 = True
define comroom_crate2 = False
define comroom_barrel = True

define whlootbox1 = False
define whlootbox2 = False
define whlootbox3 = False

define barracksloot1 = False
define barracksloot2 = False
define barracksloot3 = False
define barracksloot4 = False
define barracksEnt = True
define barracksTablet = True

define talishiploot1 = False
define talishiploot2 = False
define talishiploot3 = False
define talishiploot4 = False
define talishipdoor = False
define talishipevent = False

define prisonloot1 = False
define prisonloot2 = False
define prisonloot3 = False
define prisonloot4 = False
define prisonbody = True
define prisoncage = True
define prisoncage1 = False

define englootbox1 = False
define englootbox2 = False
define englootbox3 = False

define uloot1 = False
define uloot2 = False
define uloot3 = False
define ulube = True

define whEvent1 = False
define whKrogan = True
define whVent = True
define whCont = False
define engControl = True

define firstHelpChoice = True
define firstTimeScan = True
define firstTimeRoom = True
define firstMap = True
define firstBay1 = True
define encounter = True
define comEncounter = True
define comFirstScene = False
define comIndicator = True
define shipInsideChoice = True
define infection = 0
define suitdur = 100
define sex = 1
# CHANGE TO 1
define lewd = 1
# CHANGE TO 3
define ammo = 3
define grenades = 0
# CHANGE TO 0
define doorexp = 0
define alarm = 0
define parts = 0
define quest = "None"
define enemyhp = 0
define doorSliderValue = 1000
define doorHackJump = 'doorHackFail'
define hackNumber = 3
define hackstep = 3
define hackstage = 0
# CHANGE TO FALSE
define hackOK = False
define partsQuest = False
define crewQuest = False
define redVarrenFirstEnc = True
define asariCrew = False
define vorchaCrew = False
define crewCount = 0
define havedogbone = False
define prisonLock = False
# CHANGE TO FALSE
define act3 = False
define twoHount = False


define enemyID = 0
# change to 1
define roomID = 1
# CHANGE DOOR
define hackID = 0
define slidervalue = 1000
define random = 0
define enc_chance = 0
#change to FALSE
define corridor_fight = False
define door_fight = False

transform shake:
        ease .06 yoffset 24
        ease .06 yoffset -24
        ease .05 yoffset 20
        ease .05 yoffset -20
        ease .04 yoffset 16
        ease .04 yoffset -16
        ease .03 yoffset 12
        ease .03 yoffset -12
        ease .02 yoffset 8
        ease .02 yoffset -8
        ease .01 yoffset 4
        ease .01 yoffset -4
        ease .01 yoffset 0

image doorhack:
    "images/skills/hacker/1.png"
    pause .5
    "images/skills/hacker/2.png"
    pause .5
    "images/skills/hacker/3.png"
    pause .5
    "images/skills/hacker/4.png"
    pause .5
    "images/skills/hacker/5.png"
    pause .5
    "images/skills/hacker/6.png"
    pause .5
    "images/skills/hacker/7.png"
    pause .5
    repeat


image biggybjanim:
    "images/events/comroom/ComRoomEvent/bg combj3.png"
    pause .1
    "images/events/comroom/ComRoomEvent/bg combj4.png"
    pause .1
    "images/events/comroom/ComRoomEvent/bg combj5.png"
    pause .1
    "images/events/comroom/ComRoomEvent/bg combj6.png"
    pause .1
    "images/events/comroom/ComRoomEvent/bg combj7.png"
    pause .1
    function suck1
    "images/events/comroom/ComRoomEvent/bg combj8.png"
    pause .2
    "images/events/comroom/ComRoomEvent/bg combj7.png"
    pause .1
    "images/events/comroom/ComRoomEvent/bg combj6.png"
    pause .1
    "images/events/comroom/ComRoomEvent/bg combj5.png"
    pause .1
    "images/events/comroom/ComRoomEvent/bg combj4.png"
    pause .1
    "images/events/comroom/ComRoomEvent/bg combj3.png"
    repeat

image biggybjanimnext:
    "images/events/comroom/ComRoomEvent/blow/01.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/02.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/03.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/04.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/05.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/06.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/07.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/08.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/09.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/10.png"
    function suck3
    pause .1
    "images/events/comroom/ComRoomEvent/blow/11.png"
    pause .1
    "images/events/comroom/ComRoomEvent/blow/12.png"
    pause .1
    repeat

image comroomanalfront1:
    "images/events/comroom/ComRoomEvent/anal/front1/1.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/2.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/3.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/4.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/5.png"
    function inside
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/6.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/7.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/8.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/9.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/10.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/11.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/12.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front1/13.png"
    pause .1
    repeat

image comroomanalfront2:
    "images/events/comroom/ComRoomEvent/anal/front2/1.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front2/2.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front2/3.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front2/4.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front2/5.png"
    function slap9
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front2/6.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front2/7.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front2/8.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front2/9.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/front2/10.png"
    pause .1
    repeat

image comroomanalback1:
    "images/events/comroom/ComRoomEvent/anal/back1/01.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/02.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/03.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/04.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/05.png"
    function inside
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/06.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/07.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/08.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/09.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/10.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/11.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/12.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back1/13.png"
    pause .1
    repeat

image comroomanalback2:
    "images/events/comroom/ComRoomEvent/anal/back2/01.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back2/02.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back2/03.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back2/04.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back2/05.png"
    function slap9
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back2/06.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back2/07.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back2/08.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back2/09.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/back2/10.png"
    pause .1
    repeat

image comroomanalback2alt:
    "images/events/comroom/ComRoomEvent/anal/back2/01.png"
    pause .05
    "images/events/comroom/ComRoomEvent/anal/back2/02.png"
    function fart2
    pause .05
    "images/events/comroom/ComRoomEvent/anal/back2/03.png"
    pause .05
    "images/events/comroom/ComRoomEvent/anal/back2/04.png"
    pause .05
    "images/events/comroom/ComRoomEvent/anal/back2/05.png"
    function slap4
    pause .05
    "images/events/comroom/ComRoomEvent/anal/back2/06.png"
    pause .05
    "images/events/comroom/ComRoomEvent/anal/back2/07.png"
    pause .05
    "images/events/comroom/ComRoomEvent/anal/back2/08.png"
    pause .05
    "images/events/comroom/ComRoomEvent/anal/back2/09.png"
    pause .05
    "images/events/comroom/ComRoomEvent/anal/back2/10.png"
    pause .05
    repeat

image comroomanalcum:
    "images/events/comroom/ComRoomEvent/anal/cum/01.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/02.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/03.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/04.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/05.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/06.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/07.png"
    function fart
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/08.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/09.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/10.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/11.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/12.png"
    function cumsplash
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/13.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/14.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/15.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/16.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/17.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/18.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/19.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/20.png"
    pause .1
    "images/events/comroom/ComRoomEvent/anal/cum/21.png"
    pause .1

image asari_anim1:
    "images/events/hangar bay/inside ship/shipanim1.png"
    pause .1
    "images/events/hangar bay/inside ship/shipanim2.png"
    pause .1
    "images/events/hangar bay/inside ship/shipanim3.png"
    pause .1
    "images/events/hangar bay/inside ship/shipanim4.png"
    pause .1
    "images/events/hangar bay/inside ship/shipanim5.png"
    function slap1
    pause .1
    "images/events/hangar bay/inside ship/shipanim6.png"
    pause .1
    "images/events/hangar bay/inside ship/shipanim7.png"
    pause .1
    "images/events/hangar bay/inside ship/shipanim8.png"
    pause .1
    "images/events/hangar bay/inside ship/shipanim9.png"
    repeat

image showerevent1:
    "images/events/medbay/shower/scene1/bg showerscene4.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene5.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene6.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene7.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene8.png"
    function lick
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene7.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene6.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene5.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene4.png"
    pause .1
    repeat

image showerevent2:
    "images/events/medbay/shower/scene1/bg showerscene9.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene10.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene11.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene12.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene13.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene14.png"
    function splat
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene13.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene12.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene11.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene10.png"
    pause .1
    "images/events/medbay/shower/scene1/bg showerscene9.png"
    pause .1
    repeat

image whAnimation:
    "images/events/warehouse/event1/anim1/bg whevent1anim1.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim2.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim3.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim4.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim5.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim6.png"
    function inside
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim7.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim8.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim9.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim10.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim11.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim12.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim13.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim14.png"
    pause .1
    "images/events/warehouse/event1/anim1/bg whevent1anim15.png"
    pause .1
    repeat

image cor1bjstart1:
    "images/events/corridor1/bj/cor1bjstart1.png"
    pause .2
    "images/events/corridor1/bj/cor1bjstart2.png"
    pause .2
    "images/events/corridor1/bj/cor1bjstart3.png"
    pause .2
    "images/events/corridor1/bj/cor1bjstart4.png"
    pause .4
    "images/events/corridor1/bj/cor1bjstart3.png"
    pause .2
    "images/events/corridor1/bj/cor1bjstart2.png"
    pause .2
    "images/events/corridor1/bj/cor1bjstart1.png"
    pause .2
    repeat
image cor1bjstart2:
    "images/events/corridor1/bj/cor1bjstart1.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart2.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart3.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart4.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart5.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart6.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart7.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart8.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart9.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart10.png"
    function wetsquish
    pause .1
    "images/events/corridor1/bj/cor1bjstart11.png"
    pause .1
    "images/events/corridor1/bj/cor1bjstart12.png"
    pause .1
image cor1bjloop:
    "images/events/corridor1/bj/cor1bj1.png"
    pause .07
    "images/events/corridor1/bj/cor1bj2.png"
    pause .07
    "images/events/corridor1/bj/cor1bj3.png"
    pause .07
    "images/events/corridor1/bj/cor1bj4.png"
    pause .07
    "images/events/corridor1/bj/cor1bj5.png"
    pause .07
    "images/events/corridor1/bj/cor1bj6.png"
    function suck1
    pause .07
    "images/events/corridor1/bj/cor1bj7.png"
    pause .07
    "images/events/corridor1/bj/cor1bj8.png"
    pause .07
    "images/events/corridor1/bj/cor1bj9.png"
    pause .07
    "images/events/corridor1/bj/cor1bj10.png"
    pause .07
    "images/events/corridor1/bj/cor1bj11.png"
    pause .07
    repeat
image cor1bjcum:
    "images/events/corridor1/bj/cor1bjcum1.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum2.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum3.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum4.png"
    function swallow

image cor1bjcum1:
    "images/events/corridor1/bj/cor1bjcum5.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum6.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum7.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum8.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum9.png"
    function swallow
    pause .4
    "images/events/corridor1/bj/cor1bjcum10.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum11.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum12.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum13.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum14.png"
    function swallow
    pause .4
    "images/events/corridor1/bj/cor1bjcum15.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum16.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum17.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum18.png"
    pause .1
    "images/events/corridor1/bj/cor1bjcum19.png"
    function swallow
    pause .4
    "images/events/corridor1/bj/cor1bjcum20.png"
    pause .2
    "images/events/corridor1/bj/cor1bjcum21.png"
    pause .2

image cor1backstartloop:
    "images/events/corridor1/back/cor1b1.png"
    pause .1
    "images/events/corridor1/back/cor1b2.png"
    pause .1
    "images/events/corridor1/back/cor1b3.png"
    pause .1
    "images/events/corridor1/back/cor1b4.png"
    pause .1
    "images/events/corridor1/back/cor1b5.png"
    pause .1
    "images/events/corridor1/back/cor1b6.png"
    pause .1
    "images/events/corridor1/back/cor1b5.png"
    pause .1
    "images/events/corridor1/back/cor1b4.png"
    pause .1
    "images/events/corridor1/back/cor1b3.png"
    pause .1
    "images/events/corridor1/back/cor1b2.png"
    pause .1
    "images/events/corridor1/back/cor1b1.png"
    pause .1
    repeat

image cor1backcum1:
    "images/events/corridor1/back/cor1cum1.png"
    pause .1
    "images/events/corridor1/back/cor1cum2.png"
    pause .1
    "images/events/corridor1/back/cor1cum3.png"
    pause .1
    "images/events/corridor1/back/cor1cum4.png"
    pause .1
    "images/events/corridor1/back/cor1cum5.png"
    function cum1
    pause .1
    "images/events/corridor1/back/cor1cum6.png"
    pause .1
    "images/events/corridor1/back/cor1cum7.png"
    pause .1
    "images/events/corridor1/back/cor1cum8.png"
    pause .1
    "images/events/corridor1/back/cor1cum9.png"
    pause .1
    "images/events/corridor1/back/cor1cum10.png"
    function cum1
    pause .1
    "images/events/corridor1/back/cor1cum11.png"
    pause .1

image cor1backnextstage1:
    "images/events/corridor1/back/cor1b7.png"
    pause .1
    "images/events/corridor1/back/cor1b8.png"
    pause .1
    "images/events/corridor1/back/cor1b9.png"
    pause .1

image cor1backnextstage2:
    "images/events/corridor1/back/cor1b10.png"
    pause .1
    "images/events/corridor1/back/cor1b11.png"
    pause .1
    "images/events/corridor1/back/cor1b12.png"
    function splat
    pause .1

image cor1backmainloop1:
    "images/events/corridor1/back/cor1b13.png"
    pause .1
    "images/events/corridor1/back/cor1b14.png"
    pause .1
    "images/events/corridor1/back/cor1b15.png"
    pause .1
    "images/events/corridor1/back/cor1b16.png"
    pause .1
    "images/events/corridor1/back/cor1b17.png"
    function slap2
    pause .1
    "images/events/corridor1/back/cor1b18.png"
    pause .1
    "images/events/corridor1/back/cor1b19.png"
    pause .1
    "images/events/corridor1/back/cor1b20.png"
    pause .1
    repeat

image cor1backmainloop2:
    "images/events/corridor1/back/cor1b21.png"
    pause .1
    "images/events/corridor1/back/cor1b22.png"
    pause .1
    "images/events/corridor1/back/cor1b23.png"
    pause .1
    "images/events/corridor1/back/cor1b24.png"
    function slap4
    pause .1
    "images/events/corridor1/back/cor1b25.png"
    pause .1
    "images/events/corridor1/back/cor1b26.png"
    pause .1
    repeat

image cor1backcum2:
    "images/events/corridor1/back/cor1cum12.png"
    pause .15
    "images/events/corridor1/back/cor1cum13.png"
    pause .15
    "images/events/corridor1/back/cor1cum14.png"
    pause .15
    "images/events/corridor1/back/cor1cum15.png"
    function cum1
    pause .15
    "images/events/corridor1/back/cor1cum16.png"
    pause .15
    "images/events/corridor1/back/cor1cum17.png"
    pause .15
    "images/events/corridor1/back/cor1cum18.png"
    function cum1
    pause .15
    "images/events/corridor1/back/cor1cum19.png"
    pause .15
    "images/events/corridor1/back/cor1cum20.png"
    pause .15
    "images/events/corridor1/back/cor1cum21.png"
    function cum1

image cor2loop1:
    "images/events/corridor2/scene1/cor2var1.png"
    pause .1
    "images/events/corridor2/scene1/cor2var2.png"
    pause .1
    "images/events/corridor2/scene1/cor2var3.png"
    pause .1
    "images/events/corridor2/scene1/cor2var4.png"
    pause .1
    "images/events/corridor2/scene1/cor2var5.png"
    pause .1
    "images/events/corridor2/scene1/cor2var6.png"
    pause .1
    "images/events/corridor2/scene1/cor2var7.png"
    pause .1
    "images/events/corridor2/scene1/cor2var8.png"
    pause .1
    "images/events/corridor2/scene1/cor2var9.png"
    pause .1
    "images/events/corridor2/scene1/cor2var10.png"
    pause .1
    "images/events/corridor2/scene1/cor2var9.png"
    pause .1
    "images/events/corridor2/scene1/cor2var8.png"
    pause .1
    "images/events/corridor2/scene1/cor2var7.png"
    pause .1
    "images/events/corridor2/scene1/cor2var6.png"
    pause .1
    "images/events/corridor2/scene1/cor2var5.png"
    pause .1
    "images/events/corridor2/scene1/cor2var4.png"
    pause .1
    "images/events/corridor2/scene1/cor2var3.png"
    pause .1
    "images/events/corridor2/scene1/cor2var2.png"
    pause .1
    "images/events/corridor2/scene1/cor2var1.png"
    pause .1
    repeat

image cor2cum1:
    "images/events/corridor2/scene1/cor2var11.png"
    pause .1
    "images/events/corridor2/scene1/cor2var12.png"
    pause .1
    "images/events/corridor2/scene1/cor2var13.png"
    pause .1
    "images/events/corridor2/scene1/cor2var14.png"
    pause .1
    "images/events/corridor2/scene1/cor2var15.png"
    pause .1
    "images/events/corridor2/scene1/cor2var16.png"
    pause .1
    "images/events/corridor2/scene1/cor2var17.png"
    pause .1
    "images/events/corridor2/scene1/cor2var18.png"
    pause .1
    "images/events/corridor2/scene1/cor2var19.png"
    function cum1
    pause .07
    "images/events/corridor2/scene1/cor2var20.png"
    pause .07
    "images/events/corridor2/scene1/cor2var21.png"
    pause .07
    "images/events/corridor2/scene1/cor2var22.png"
    pause .1
    "images/events/corridor2/scene1/cor2var23.png"
    function cum1
    pause .1
    "images/events/corridor2/scene1/cor2var24.png"
    pause .1
    "images/events/corridor2/scene1/cor2var25.png"
    pause .1
    "images/events/corridor2/scene1/cor2var26.png"
    pause .1
    "images/events/corridor2/scene1/cor2var27.png"
    pause .1
    "images/events/corridor2/scene1/cor2var28.png"
    pause .1
    "images/events/corridor2/scene1/cor2var29.png"
    pause .1
    "images/events/corridor2/scene1/cor2var30.png"
    pause .1
    "images/events/corridor2/scene1/cor2var31.png"
    pause .1
    "images/events/corridor2/scene1/cor2var32.png"
    pause .1
    "images/events/corridor2/scene1/cor2var33.png"
    function cum1
    pause .07
    "images/events/corridor2/scene1/cor2var34.png"
    pause .07
    "images/events/corridor2/scene1/cor2var35.png"
    pause .07
    "images/events/corridor2/scene1/cor2var36.png"
    pause .07
    "images/events/corridor2/scene1/cor2var37.png"
    pause .07
    "images/events/corridor2/scene1/cor2var38.png"
    pause .07
    "images/events/corridor2/scene1/cor2var39.png"
    pause .07
    "images/events/corridor2/scene1/cor2var40.png"
    pause .07
    "images/events/corridor2/scene1/cor2var41.png"

image cor2loop2:
    "images/events/corridor2/scene2/cor2var1.png"
    pause .15
    "images/events/corridor2/scene2/cor2var2.png"
    pause .15
    "images/events/corridor2/scene2/cor2var3.png"
    pause .15
    "images/events/corridor2/scene2/cor2var4.png"
    pause .15
    "images/events/corridor2/scene2/cor2var5.png"
    pause .15
    "images/events/corridor2/scene2/cor2var4.png"
    pause .15
    "images/events/corridor2/scene2/cor2var3.png"
    pause .15
    "images/events/corridor2/scene2/cor2var2.png"
    pause .15
    "images/events/corridor2/scene2/cor2var1.png"
    pause .15
    repeat

image cor2stage11:
    "images/events/corridor2/scene2/cor2var6.png"
    pause .1
    "images/events/corridor2/scene2/cor2var7.png"
    pause .1
    "images/events/corridor2/scene2/cor2var8.png"
    pause .1
    "images/events/corridor2/scene2/cor2var9.png"
    pause .1
    "images/events/corridor2/scene2/cor2var10.png"
    pause .1
    "images/events/corridor2/scene2/cor2var11.png"
    pause .1
    "images/events/corridor2/scene2/cor2var12.png"
    pause .1
    "images/events/corridor2/scene2/cor2var13.png"
    pause .1
    "images/events/corridor2/scene2/cor2var14.png"
    pause .2

image cor2stage12:
    "images/events/corridor2/scene2/cor2var15.png"
    pause .07
    function wetsquish
    "images/events/corridor2/scene2/cor2var16.png"
    pause .07
    "images/events/corridor2/scene2/cor2var17.png"
    pause .07
    "images/events/corridor2/scene2/cor2var18.png"
    pause .07
    "images/events/corridor2/scene2/cor2var19.png"
    pause .07

image cor2loop3:
    "images/events/corridor2/scene2/cor2varmain1.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain2.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain3.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain4.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain5.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain6.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain7.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain8.png"
    function suck2
    pause .08
    "images/events/corridor2/scene2/cor2varmain9.png"
    pause .2
    "images/events/corridor2/scene2/cor2varmain8.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain7.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain6.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain5.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain4.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain3.png"
    pause .08
    "images/events/corridor2/scene2/cor2varmain2.png"
    pause .08
    repeat

image cor2stage21:
    "images/events/corridor2/scene2/cor2var20.png"
    pause .1
    "images/events/corridor2/scene2/cor2var21.png"
    pause .1
    "images/events/corridor2/scene2/cor2var22.png"
    pause .1
    "images/events/corridor2/scene2/cor2var23.png"
    pause .1
    "images/events/corridor2/scene2/cor2var24.png"
    pause .1
    "images/events/corridor2/scene2/cor2var25.png"
    pause .1

image cor2stage22:
    "images/events/corridor2/scene2/cor2var26.png"
    pause .1
    "images/events/corridor2/scene2/cor2var27.png"
    pause .1
    "images/events/corridor2/scene2/cor2var28.png"
    pause .2
    "images/events/corridor2/scene2/cor2var29.png"
    pause .1
    "images/events/corridor2/scene2/cor2var30.png"
    pause .2
    "images/events/corridor2/scene2/cor2var29.png"
    pause .1
    "images/events/corridor2/scene2/cor2var30.png"
    pause .2
    "images/events/corridor2/scene2/cor2var29.png"
    pause .1
    "images/events/corridor2/scene2/cor2var30.png"
    pause .2
    "images/events/corridor2/scene2/cor2var29.png"
    pause .1
    "images/events/corridor2/scene2/cor2var30.png"
    pause .2
    "images/events/corridor2/scene2/cor2var31.png"
    pause .1
    "images/events/corridor2/scene2/cor2var32.png"
    pause .1
    "images/events/corridor2/scene2/cor2var33.png"
    function wetsquish
    pause .1
    "images/events/corridor2/scene2/cor2var34.png"
    pause .1

image cor2loop4:
    "images/events/corridor2/scene2/cor2var33.png"
    pause .1
    "images/events/corridor2/scene2/cor2var32.png"
    pause .1
    "images/events/corridor2/scene2/cor2var31.png"
    pause .1
    "images/events/corridor2/scene2/cor2var30.png"
    pause .1
    "images/events/corridor2/scene2/cor2var29.png"
    pause .1
    "images/events/corridor2/scene2/cor2var28.png"
    pause .1
    "images/events/corridor2/scene2/cor2var27.png"
    pause .2
    "images/events/corridor2/scene2/cor2var28.png"
    pause .1
    "images/events/corridor2/scene2/cor2var29.png"
    pause .1
    "images/events/corridor2/scene2/cor2var30.png"
    pause .1
    "images/events/corridor2/scene2/cor2var31.png"
    pause .1
    "images/events/corridor2/scene2/cor2var32.png"
    function suck1
    pause .1
    repeat

image cor2cum2:
    "images/events/corridor2/scene2/cor2varcum1.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum2.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum3.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum4.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum5.png"
    function cum1
    pause .1
    "images/events/corridor2/scene2/cor2varcum6.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum7.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum8.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum9.png"
    function swallow
    pause .1
    "images/events/corridor2/scene2/cor2varcum10.png"
    pause .3
    "images/events/corridor2/scene2/cor2varcum11.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum12.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum13.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum14.png"
    function cum1
    pause .1
    "images/events/corridor2/scene2/cor2varcum15.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum16.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum17.png"
    function swallow
    pause .1
    "images/events/corridor2/scene2/cor2varcum18.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum19.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum20.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum21.png"
    function cum1
    pause .1
    "images/events/corridor2/scene2/cor2varcum22.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum23.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum24.png"
    pause .1
    "images/events/corridor2/scene2/cor2varcum25.png"
    function swallow
    pause .3

image cor2misloop1:
    "images/events/corridor2/scene3/cor2varmis1.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis2.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis3.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis4.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis5.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis6.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis7.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis8.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis9.png"
    function lick
    pause .1
    "images/events/corridor2/scene3/cor2varmis10.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis9.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis8.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis7.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis6.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis5.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis4.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis3.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis2.png"
    pause .1
    repeat

image cor2misstage1:
    "images/events/corridor2/scene3/cor2varmis11.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis12.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis13.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis14.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis15.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis16.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis17.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis18.png"
    function tier
    pause .1
    "images/events/corridor2/scene3/cor2varmis19.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis20.png"
    pause .2
    "images/events/corridor2/scene3/cor2varmis21.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis22.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis23.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis24.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis25.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis26.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis27.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis28.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis29.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis30.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis31.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis32.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis33.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis34.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis35.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis36.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis37.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis38.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis39.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis40.png"
    pause .03
    "images/events/corridor2/scene3/cor2varmis41.png"
    pause .1

image cor2misloop2:
    "images/events/corridor2/scene3/cor2varmis41.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis42.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis43.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis44.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis45.png"
    pause .08
    "images/events/corridor2/scene3/cor2varmis46.png"
    pause .08
    "images/events/corridor2/scene3/cor2varmis47.png"
    pause .08
    "images/events/corridor2/scene3/cor2varmis48.png"
    pause .08
    "images/events/corridor2/scene3/cor2varmis49.png"
    function slap5
    pause .08
    "images/events/corridor2/scene3/cor2varmis50.png"
    pause .08
    "images/events/corridor2/scene3/cor2varmis49.png"
    pause .08
    "images/events/corridor2/scene3/cor2varmis48.png"
    pause .08
    "images/events/corridor2/scene3/cor2varmis47.png"
    pause .08
    "images/events/corridor2/scene3/cor2varmis46.png"
    pause .08
    "images/events/corridor2/scene3/cor2varmis45.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis44.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis43.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis42.png"
    pause .05
    repeat

image cor2misstage21:
    "images/events/corridor2/scene3/cor2varmis51.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis52.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis53.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis54.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis55.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis56.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis57.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis58.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis59.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis60.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis61.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis62.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis63.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis64.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis65.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis66.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis67.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis68.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis69.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis70.png"
    function splat
    pause .1

image cor2misstage22:
    "images/events/corridor2/scene3/cor2varmis71.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis72.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis73.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis74.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis75.png"
    pause .1

image cor2misloop3:
    "images/events/corridor2/scene3/cor2varmis75.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis76.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis77.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis78.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis79.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis80.png"
    function slap9
    pause .05
    "images/events/corridor2/scene3/cor2varmis81.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis82.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis83.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis84.png"
    pause .05
    "images/events/corridor2/scene3/cor2varmis85.png"
    pause .05
    repeat

image cor2miscum1:
    "images/events/corridor2/scene3/cor2varmis86.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis87.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis88.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis89.png"
    function cum1
    pause .09
    "images/events/corridor2/scene3/cor2varmis90.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis91.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis92.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis93.png"
    function cum1
    pause .09
    "images/events/corridor2/scene3/cor2varmis94.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis95.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis96.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis97.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis98.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis99.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis100.png"
    function cum1
    pause .09
    "images/events/corridor2/scene3/cor2varmis101.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis102.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis103.png"
    pause .09
    "images/events/corridor2/scene3/cor2varmis104.png"
    pause .09

image cor2misstage3:
    "images/events/corridor2/scene3/cor2varmis75.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis76.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis77.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis78.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis79.png"
    pause .1
    "images/events/corridor2/scene3/cor2varmis80.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis1.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis2.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis3.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis4.png"
    pause .2
    "images/events/corridor2/scene4/cor2varmis5.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis6.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis7.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis8.png"

image cor2misloop4:
    "images/events/corridor2/scene4/cor2varmis5.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis6.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis7.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis8.png"
    pause .3
    "images/events/corridor2/scene4/cor2varmis7.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis6.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis5.png"
    pause .1
    repeat

image cor2misstage41:
    "images/events/corridor2/scene4/cor2varmis9.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis10.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis11.png"
    function wetsquish

image cor2misstage42:
    "images/events/corridor2/scene4/cor2varmis12.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis13.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis14.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis15.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis16.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis17.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis18.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis19.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis20.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis21.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis22.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis23.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis24.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis25.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis26.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis27.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis28.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis29.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmis30.png"
    pause .1

image cor2misloop5:
    "images/events/corridor2/scene4/cor2varmis30.png"
    pause .05
    "images/events/corridor2/scene4/cor2varmis31.png"
    pause .05
    "images/events/corridor2/scene4/cor2varmis32.png"
    pause .05
    "images/events/corridor2/scene4/cor2varmis33.png"
    pause .05
    "images/events/corridor2/scene4/cor2varmis34.png"
    pause .05
    "images/events/corridor2/scene4/cor2varmis35.png"
    function slap3
    pause .05
    "images/events/corridor2/scene4/cor2varmis36.png"
    pause .05
    "images/events/corridor2/scene4/cor2varmis37.png"
    pause .05
    "images/events/corridor2/scene4/cor2varmis38.png"
    pause .05
    "images/events/corridor2/scene4/cor2varmis39.png"
    pause .05
    "images/events/corridor2/scene4/cor2varmis40.png"
    pause .05
    repeat

image cor2miscum2:
    "images/events/corridor2/scene4/cor2varmiscum1.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum2.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum3.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum4.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum5.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum6.png"
    function cum1
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum7.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum8.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum9.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum10.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum11.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum12.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum13.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum14.png"
    function cum1
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum15.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum16.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum17.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum18.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum19.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum20.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum21.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum22.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum23.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum24.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum25.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum26.png"
    function cum1
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum27.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum28.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum29.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum30.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum31.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum32.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum33.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum34.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum35.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum36.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum37.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum38.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum39.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum40.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum41.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum42.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum43.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum44.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum45.png"
    function cum1
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum46.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum47.png"
    pause .1
    "images/events/corridor2/scene4/cor2varmiscum48.png"
    pause .1


image doorhackstart:
    "images/events/backevent/pussy/tali back1.png"
    pause .1
    "images/events/backevent/pussy/tali back2.png"
    pause .1
    "images/events/backevent/pussy/tali back3.png"
    pause .1
    "images/events/backevent/pussy/tali back4.png"
    pause .1
    "images/events/backevent/pussy/tali back5.png"
    pause .1
    "images/events/backevent/pussy/tali back6.png"
    pause .1
    "images/events/backevent/pussy/tali back7.png"
    pause .1
    "images/events/backevent/pussy/tali back8.png"
    pause .1
    "images/events/backevent/pussy/tali back9.png"
    function lick
    pause .1
    repeat

image doorhacklick:
    "images/events/backevent/pussy/tali back11.png"
    pause .1
    "images/events/backevent/pussy/tali back12.png"
    pause .1
    "images/events/backevent/pussy/tali back13.png"
    pause .1
    "images/events/backevent/pussy/tali back14.png"
    pause .1
    "images/events/backevent/pussy/tali back15.png"
    pause .1
    "images/events/backevent/pussy/tali back16.png"
    pause .1
    "images/events/backevent/pussy/tali back17.png"
    pause .1
    "images/events/backevent/pussy/tali back18.png"
    pause .1
    "images/events/backevent/pussy/tali back19.png"
    function lick
    pause .1
    repeat

image doorhackpussy1:
    "images/events/backevent/pussy/tali back20.png"
    pause .2
    "images/events/backevent/pussy/tali back21.png"
    pause .2
    "images/events/backevent/pussy/tali back22.png"
    pause .2
    "images/events/backevent/pussy/tali back23.png"
    pause .2
    "images/events/backevent/pussy/tali back22.png"
    pause .2
    "images/events/backevent/pussy/tali back21.png"
    pause .2
    repeat

image doorhackpussy2:
    "images/events/backevent/pussy/tali back20.png"
    pause .2
    "images/events/backevent/pussy/tali back21.png"
    pause .2
    "images/events/backevent/pussy/tali back22.png"
    pause .2
    "images/events/backevent/pussy/tali back23.png"
    pause .2
    "images/events/backevent/pussy/tali back24.png"
    pause .2
    "images/events/backevent/pussy/tali back25.png"
    pause .2
    "images/events/backevent/pussy/tali back26.png"
    pause .2
    "images/events/backevent/pussy/tali back27.png"
    pause .2
    "images/events/backevent/pussy/tali back28.png"
    pause .2
    "images/events/backevent/pussy/tali back29.png"
    pause .2
    "images/events/backevent/pussy/tali back30.png"
    function splat

image doorhackpussyloop1:
    "images/events/backevent/pussy/tali back31.png"
    pause .1
    "images/events/backevent/pussy/tali back32.png"
    pause .1
    "images/events/backevent/pussy/tali back33.png"
    pause .1
    "images/events/backevent/pussy/tali back34.png"
    pause .1
    "images/events/backevent/pussy/tali back35.png"
    function slap1
    pause .1
    "images/events/backevent/pussy/tali back36.png"
    pause .1
    "images/events/backevent/pussy/tali back37.png"
    pause .1
    "images/events/backevent/pussy/tali back38.png"
    pause .1
    repeat

image doorhackpussyloop2:
    "images/events/backevent/pussy/tali back31.png"
    pause .05
    "images/events/backevent/pussy/tali back32.png"
    pause .05
    "images/events/backevent/pussy/tali back33.png"
    pause .05
    "images/events/backevent/pussy/tali back34.png"
    pause .05
    "images/events/backevent/pussy/tali back35.png"
    function slap1
    pause .05
    "images/events/backevent/pussy/tali back36.png"
    pause .05
    "images/events/backevent/pussy/tali back37.png"
    pause .05
    "images/events/backevent/pussy/tali back38.png"
    pause .05
    repeat

image doorhackpussycum:
    "images/events/backevent/pussy/tali backcum1.png"
    pause .1
    "images/events/backevent/pussy/tali backcum2.png"
    pause .1
    "images/events/backevent/pussy/tali backcum3.png"
    pause .1
    "images/events/backevent/pussy/tali backcum4.png"
    pause .1
    "images/events/backevent/pussy/tali backcum5.png"
    pause .1
    "images/events/backevent/pussy/tali backcum6.png"
    pause .1
    "images/events/backevent/pussy/tali backcum7.png"
    function cum1
    pause .1
    "images/events/backevent/pussy/tali backcum8.png"
    pause .1
    "images/events/backevent/pussy/tali backcum9.png"
    pause .1
    "images/events/backevent/pussy/tali backcum10.png"
    pause .1
    "images/events/backevent/pussy/tali backcum11.png"
    pause .1
    "images/events/backevent/pussy/tali backcum12.png"
    function cum1
    pause .1
    "images/events/backevent/pussy/tali backcum13.png"
    pause .1
    "images/events/backevent/pussy/tali backcum14.png"
    pause .1
    "images/events/backevent/pussy/tali backcum15.png"
    pause .1
    "images/events/backevent/pussy/tali backcum16.png"
    pause .1
    "images/events/backevent/pussy/tali backcum17.png"
    pause .1
    "images/events/backevent/pussy/tali backcum1.png"
    pause .15
    "images/events/backevent/pussy/tali backcum2.png"
    pause .15
    "images/events/backevent/pussy/tali backcum3.png"
    pause .15
    "images/events/backevent/pussy/tali backcum4.png"
    pause .15
    "images/events/backevent/pussy/tali backcum5.png"
    pause .15
    "images/events/backevent/pussy/tali backcum6.png"
    pause .15
    "images/events/backevent/pussy/tali backcum7.png"
    function cum1
    pause .15
    "images/events/backevent/pussy/tali backcum8.png"
    pause .15
    "images/events/backevent/pussy/tali backcum9.png"
    pause .15
    "images/events/backevent/pussy/tali backcum10.png"
    pause .15
    "images/events/backevent/pussy/tali backcum11.png"
    pause .15
    "images/events/backevent/pussy/tali backcum12.png"
    function cum1
    pause .15
    "images/events/backevent/pussy/tali backcum13.png"
    pause .15
    "images/events/backevent/pussy/tali backcum14.png"
    pause .15
    "images/events/backevent/pussy/tali backcum15.png"
    pause .15
    "images/events/backevent/pussy/tali backcum16.png"
    pause .15
    "images/events/backevent/pussy/tali backcum17.png"

image doorhjstart:
    "images/events/backevent/handjob/tali hj1.png"
    pause .1
    "images/events/backevent/handjob/tali hj2.png"
    pause .1
    "images/events/backevent/handjob/tali hj3.png"
    pause .1
    "images/events/backevent/handjob/tali hj4.png"
    pause .1
    "images/events/backevent/handjob/tali hj5.png"
    pause .1
    "images/events/backevent/handjob/tali hj6.png"
    function slosh
    pause .1
    "images/events/backevent/handjob/tali hj7.png"
    pause .1
    "images/events/backevent/handjob/tali hj8.png"
    pause .1
    "images/events/backevent/handjob/tali hj9.png"
    pause .1
    "images/events/backevent/handjob/tali hj10.png"
    pause .1
    repeat

image doorhjloop1:
    "images/events/backevent/handjob/tali hj11.png"
    pause .1
    "images/events/backevent/handjob/tali hj12.png"
    pause .1
    "images/events/backevent/handjob/tali hj13.png"
    pause .1
    "images/events/backevent/handjob/tali hj14.png"
    pause .1
    "images/events/backevent/handjob/tali hj15.png"
    pause .1
    "images/events/backevent/handjob/tali hj16.png"
    function slosh
    pause .1
    "images/events/backevent/handjob/tali hj17.png"
    pause .1
    "images/events/backevent/handjob/tali hj18.png"
    pause .1
    "images/events/backevent/handjob/tali hj19.png"
    pause .1
    "images/events/backevent/handjob/tali hj20.png"
    pause .1
    repeat

image doorhjloop2:
    "images/events/backevent/handjob/tali hj21.png"
    pause .1
    "images/events/backevent/handjob/tali hj22.png"
    pause .1
    "images/events/backevent/handjob/tali hj23.png"
    pause .1
    "images/events/backevent/handjob/tali hj24.png"
    function slosh
    pause .1
    "images/events/backevent/handjob/tali hj24.png"
    pause .1
    "images/events/backevent/handjob/tali hj23.png"
    pause .1
    "images/events/backevent/handjob/tali hj22.png"
    pause .1
    "images/events/backevent/handjob/tali hj21.png"
    pause .1
    repeat

image doorhjloop3:
    "images/events/backevent/handjob/tali hj21.png"
    pause .05
    "images/events/backevent/handjob/tali hj22.png"
    pause .05
    "images/events/backevent/handjob/tali hj23.png"
    pause .05
    "images/events/backevent/handjob/tali hj24.png"
    function slosh
    pause .05
    "images/events/backevent/handjob/tali hj24.png"
    pause .05
    "images/events/backevent/handjob/tali hj23.png"
    pause .05
    "images/events/backevent/handjob/tali hj22.png"
    pause .05
    "images/events/backevent/handjob/tali hj21.png"
    pause .05
    repeat

image doorhjcum:
    "images/events/backevent/handjob/cum/1.png"
    pause .15
    "images/events/backevent/handjob/cum/2.png"
    pause .15
    "images/events/backevent/handjob/cum/3.png"
    pause .15
    "images/events/backevent/handjob/cum/4.png"
    pause .15
    "images/events/backevent/handjob/cum/5.png"
    function cum1
    pause .15
    "images/events/backevent/handjob/cum/6.png"
    pause .15
    "images/events/backevent/handjob/cum/7.png"
    pause .15
    "images/events/backevent/handjob/cum/8.png"
    function cum1
    pause .15
    "images/events/backevent/handjob/cum/9.png"
    pause .15
    "images/events/backevent/handjob/cum/10.png"
    function cum1
    pause .15
    "images/events/backevent/handjob/cum/11.png"
    pause .15
    "images/events/backevent/handjob/cum/12.png"
    pause .15
    "images/events/backevent/handjob/cum/13.png"
    pause .15
    "images/events/backevent/handjob/cum/14.png"
    pause .15
    "images/events/backevent/handjob/cum/15.png"
    pause .15
    "images/events/backevent/handjob/cum/16.png"
    pause .15
    "images/events/backevent/handjob/cum/17.png"
    pause .15
    "images/events/backevent/handjob/cum/18.png"
    pause .15
    "images/events/backevent/handjob/cum/19.png"
    pause .15

image dooranalstep1:
    "images/events/backevent/anal/tali backanal2.png"
    pause .1
    "images/events/backevent/anal/tali backanal3.png"
    pause .1
    "images/events/backevent/anal/tali backanal4.png"
    pause .1
    "images/events/backevent/anal/tali backanal5.png"
    pause .1
    "images/events/backevent/anal/tali backanal6.png"
    pause .1
    "images/events/backevent/anal/tali backanal7.png"
    pause .1
    "images/events/backevent/anal/tali backanal8.png"
    pause .1
    "images/events/backevent/anal/tali backanal9.png"
    pause .1
    "images/events/backevent/anal/tali backanal10.png"
    pause .1
    "images/events/backevent/anal/tali backanal11.png"
    pause .1
    "images/events/backevent/anal/tali backanal10.png"
    pause .1
    "images/events/backevent/anal/tali backanal9.png"
    pause .1
    "images/events/backevent/anal/tali backanal8.png"
    pause .1
    "images/events/backevent/anal/tali backanal7.png"
    pause .1
    "images/events/backevent/anal/tali backanal6.png"
    pause .1
    "images/events/backevent/anal/tali backanal5.png"
    pause .1
    "images/events/backevent/anal/tali backanal4.png"
    pause .1
    "images/events/backevent/anal/tali backanal3.png"
    pause .1
    repeat

image dooranalstep2:
    "images/events/backevent/anal/tali backanal12.png"
    pause .15
    "images/events/backevent/anal/tali backanal13.png"
    pause .15
    "images/events/backevent/anal/tali backanal14.png"
    pause .15
    "images/events/backevent/anal/tali backanal15.png"
    pause .15
    "images/events/backevent/anal/tali backanal16.png"
    pause .15
    "images/events/backevent/anal/tali backanal17.png"
    pause .15
    repeat

image dooranalstep3:
    "images/events/backevent/anal/tali backanal18.png"
    pause .1
    "images/events/backevent/anal/tali backanal19.png"
    pause .1
    "images/events/backevent/anal/tali backanal20.png"
    pause .1
    "images/events/backevent/anal/tali backanal21.png"
    pause .1
    "images/events/backevent/anal/tali backanal22.png"
    pause .1
    "images/events/backevent/anal/tali backanal23.png"
    pause .1
    "images/events/backevent/anal/tali backanal24.png"
    pause .1
    "images/events/backevent/anal/tali backanal25.png"
    pause .1
    "images/events/backevent/anal/tali backanal26.png"
    pause .1
    "images/events/backevent/anal/tali backanal27.png"
    pause .1
    repeat

image dooranalstep4:
    "images/events/backevent/anal/tali backanal28.png"
    pause .1
    "images/events/backevent/anal/tali backanal29.png"
    pause .1
    "images/events/backevent/anal/tali backanal30.png"
    pause .1
    "images/events/backevent/anal/tali backanal31.png"
    pause .1
    "images/events/backevent/anal/tali backanal32.png"
    pause .1
    "images/events/backevent/anal/tali backanal33.png"
    pause .1
    "images/events/backevent/anal/tali backanal34.png"
    pause .1
    "images/events/backevent/anal/tali backanal35.png"
    pause .1
    "images/events/backevent/anal/tali backanal36.png"
    pause .1
    "images/events/backevent/anal/tali backanal37.png"
    pause .1
    "images/events/backevent/anal/tali backanal38.png"
    pause .1
    "images/events/backevent/anal/tali backanal39.png"
    pause .1
    "images/events/backevent/anal/tali backanal40.png"
    pause .1
    "images/events/backevent/anal/tali backanal41.png"

image dooranalstep5:
    "images/events/backevent/anal/tali backanal42.png"
    pause .1
    "images/events/backevent/anal/tali backanal43.png"
    pause .1
    "images/events/backevent/anal/tali backanal44.png"
    pause .1
    "images/events/backevent/anal/tali backanal45.png"
    pause .1
    "images/events/backevent/anal/tali backanal46.png"
    function splat
    pause .1
    "images/events/backevent/anal/tali backanal47.png"

image dooranalstep6:
    "images/events/backevent/anal/tali backanal48.png"
    pause .1
    "images/events/backevent/anal/tali backanal49.png"
    pause .1
    "images/events/backevent/anal/tali backanal50.png"
    pause .1
    "images/events/backevent/anal/tali backanal51.png"
    pause .1
    "images/events/backevent/anal/tali backanal52.png"
    pause .1
    "images/events/backevent/anal/tali backanal53.png"
    function slap3
    pause .1
    "images/events/backevent/anal/tali backanal54.png"
    pause .1
    "images/events/backevent/anal/tali backanal55.png"
    pause .1
    "images/events/backevent/anal/tali backanal56.png"
    pause .1
    repeat

image dooranalstep6ext:
    "images/events/backevent/anal/tali backanal57.png"
    pause .1
    "images/events/backevent/anal/tali backanal58.png"
    pause .1
    "images/events/backevent/anal/tali backanal59.png"
    pause .1
    "images/events/backevent/anal/tali backanal60.png"
    pause .1
    "images/events/backevent/anal/tali backanal61.png"
    pause .1
    "images/events/backevent/anal/tali backanal62.png"
    function inside
    pause .1
    "images/events/backevent/anal/tali backanal63.png"
    pause .1
    "images/events/backevent/anal/tali backanal64.png"
    pause .1
    "images/events/backevent/anal/tali backanal65.png"
    pause .1
    "images/events/backevent/anal/tali backanal66.png"
    pause .1
    "images/events/backevent/anal/tali backanal67.png"
    pause .1
    "images/events/backevent/anal/tali backanal68.png"
    pause .1
    "images/events/backevent/anal/tali backanal69.png"
    pause .1
    "images/events/backevent/anal/tali backanal70.png"
    pause .1
    "images/events/backevent/anal/tali backanal71.png"
    pause .1
    "images/events/backevent/anal/tali backanal70.png"
    function inside
    pause .1
    "images/events/backevent/anal/tali backanal69.png"
    pause .1
    "images/events/backevent/anal/tali backanal68.png"
    pause .1
    "images/events/backevent/anal/tali backanal67.png"
    pause .1
    "images/events/backevent/anal/tali backanal66.png"
    pause .1
    "images/events/backevent/anal/tali backanal65.png"
    pause .1
    "images/events/backevent/anal/tali backanal64.png"
    pause .1
    "images/events/backevent/anal/tali backanal63.png"
    pause .1
    "images/events/backevent/anal/tali backanal62.png"
    pause .1
    "images/events/backevent/anal/tali backanal61.png"
    pause .1
    "images/events/backevent/anal/tali backanal60.png"
    pause .1
    "images/events/backevent/anal/tali backanal59.png"
    pause .1
    "images/events/backevent/anal/tali backanal58.png"
    pause .1
    "images/events/backevent/anal/tali backanal57.png"
    pause .1
    repeat

image dooranalstep7:
    "images/events/backevent/anal/tali backanal81.png"
    pause .1
    "images/events/backevent/anal/tali backanal82.png"
    pause .1
    "images/events/backevent/anal/tali backanal83.png"
    pause .1
    "images/events/backevent/anal/tali backanal84.png"
    function slap3
    pause .1
    "images/events/backevent/anal/tali backanal85.png"
    pause .1
    "images/events/backevent/anal/tali backanal86.png"
    pause .1
    repeat

image dooranalstep7alt:
    "images/events/backevent/anal/tali backanal81.png"
    pause .07
    "images/events/backevent/anal/tali backanal82.png"
    pause .07
    "images/events/backevent/anal/tali backanal83.png"
    pause .07
    "images/events/backevent/anal/tali backanal84.png"
    function slap3
    pause .07
    "images/events/backevent/anal/tali backanal85.png"
    pause .07
    "images/events/backevent/anal/tali backanal86.png"
    pause .07
    repeat

image dooranalcum:
    "images/events/backevent/anal/cum/tali backanalcum1.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum2.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum3.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum4.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum5.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum6.png"
    function cum2
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum7.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum8.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum9.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum10.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum11.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum12.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum13.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum14.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum15.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum16.png"
    function cum2
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum17.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum18.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum19.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum20.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum21.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum22.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum23.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum24.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum25.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum26.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum27.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum28.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum29.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum30.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum29.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum28.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum27.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum26.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum27.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum28.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum29.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum30.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum31.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum32.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum33.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum34.png"
    function slosh
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum35.png"
    pause .1
    "images/events/backevent/anal/cum/tali backanalcum36.png"
    pause .1

image doubleBJstep1:
    "images/events/corridorrunevent/bg coridorrun1.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun2.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun3.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun4.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun5.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun4.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun3.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun2.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun1.png"
    pause .1
    repeat

image doubleBJstep2:
    "images/events/corridorrunevent/bg coridorrun6.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun7.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun8.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun9.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun10.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun9.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun8.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun7.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun6.png"
    pause .1
    repeat

image doubleBJstep2next:
    "images/events/corridorrunevent/bg coridorrun6.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun7.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun8.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun9.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun10.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun11.png"
    pause .1
    "images/events/corridorrunevent/bg coridorrun12.png"
    pause .1

image doubleBJstep3:
    "images/events/corridorrunevent/bg corridorrun13.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun14.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun15.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun16.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun17.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun18.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun19.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun20.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun21.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun22.png"
    pause .1
    "images/events/corridorrunevent/bg corridorrun23.png"
    pause .1
    repeat

image doubleBJstep4:
    "images/events/corridorrunevent/cum7.png"
    pause .1
    "images/events/corridorrunevent/cum8.png"
    pause .1
    "images/events/corridorrunevent/cum9.png"
    pause .1
    "images/events/corridorrunevent/cum10.png"
    pause .1
    "images/events/corridorrunevent/cum11.png"
    pause .1
    "images/events/corridorrunevent/cum12.png"
    pause .1
    "images/events/corridorrunevent/cum13.png"
    pause .1
    repeat

image cageButtLoop:
    "images/events/prison/event/1/1.png"
    pause .1
    "images/events/prison/event/1/2.png"
    pause .1
    "images/events/prison/event/1/3.png"
    pause .1
    "images/events/prison/event/1/4.png"
    pause .1
    "images/events/prison/event/1/5.png"
    pause .1
    "images/events/prison/event/1/6.png"
    pause .1
    "images/events/prison/event/1/7.png"
    pause .1
    "images/events/prison/event/1/8.png"
    pause .1
    repeat

image cageHandLoop1:
    "images/events/prison/event/3/1.png"
    pause .1
    "images/events/prison/event/3/2.png"
    pause .1
    "images/events/prison/event/3/3.png"
    pause .1
    "images/events/prison/event/3/4.png"
    pause .1
    "images/events/prison/event/3/5.png"
    pause .1
    "images/events/prison/event/3/6.png"
    function inside
    pause .1
    "images/events/prison/event/3/7.png"
    pause .1
    "images/events/prison/event/3/8.png"
    pause .1
    "images/events/prison/event/3/9.png"
    pause .1
    "images/events/prison/event/3/10.png"
    pause .1
    repeat

image cageHandLoop2:
    "images/events/prison/event/3/11.png"
    pause .1
    "images/events/prison/event/3/12.png"
    pause .1
    "images/events/prison/event/3/13.png"
    pause .1
    "images/events/prison/event/3/14.png"
    pause .1
    "images/events/prison/event/3/15.png"
    pause .1
    "images/events/prison/event/3/16.png"
    function inside
    pause .1
    "images/events/prison/event/3/17.png"
    pause .1
    "images/events/prison/event/3/18.png"
    pause .1
    "images/events/prison/event/3/19.png"
    pause .1
    "images/events/prison/event/3/20.png"
    pause .1
    repeat

image cageHandLoop2alt:
    "images/events/prison/event/3/11.png"
    pause .06
    "images/events/prison/event/3/12.png"
    pause .06
    "images/events/prison/event/3/13.png"
    pause .06
    "images/events/prison/event/3/14.png"
    pause .06
    "images/events/prison/event/3/15.png"
    pause .06
    "images/events/prison/event/3/16.png"
    function inside
    pause .06
    "images/events/prison/event/3/17.png"
    pause .06
    "images/events/prison/event/3/18.png"
    pause .06
    "images/events/prison/event/3/19.png"
    pause .06
    "images/events/prison/event/3/20.png"
    pause .06
    repeat

image cageHandLoop3:
    "images/events/prison/event/2/1.png"
    pause .1
    "images/events/prison/event/2/2.png"
    pause .1
    "images/events/prison/event/2/3.png"
    pause .1
    "images/events/prison/event/2/4.png"
    pause .1
    "images/events/prison/event/2/5.png"
    pause .1
    "images/events/prison/event/2/6.png"
    pause .1
    "images/events/prison/event/2/7.png"
    pause .1
    "images/events/prison/event/2/8.png"
    pause .1
    "images/events/prison/event/2/9.png"
    pause .1
    "images/events/prison/event/2/10.png"
    pause .1
    "images/events/prison/event/2/11.png"
    pause .1
    "images/events/prison/event/2/12.png"
    pause .1
    "images/events/prison/event/2/13.png"
    pause .1
    repeat

image cageHandLoop4:
    "images/events/prison/event/2/14.png"
    pause .1
    "images/events/prison/event/2/15.png"
    pause .1
    "images/events/prison/event/2/16.png"
    pause .1
    "images/events/prison/event/2/17.png"
    pause .1
    "images/events/prison/event/2/18.png"
    pause .1
    "images/events/prison/event/2/19.png"
    function inside
    pause .1
    "images/events/prison/event/2/20.png"
    pause .1
    "images/events/prison/event/2/21.png"
    pause .1
    "images/events/prison/event/2/22.png"
    pause .1
    "images/events/prison/event/2/23.png"
    pause .1
    repeat

image cageHandLoop4alt:
    "images/events/prison/event/2/14.png"
    pause .07
    "images/events/prison/event/2/15.png"
    pause .07
    "images/events/prison/event/2/16.png"
    pause .07
    "images/events/prison/event/2/17.png"
    pause .07
    "images/events/prison/event/2/18.png"
    pause .07
    "images/events/prison/event/2/19.png"
    function inside
    pause .07
    "images/events/prison/event/2/20.png"
    pause .07
    "images/events/prison/event/2/21.png"
    pause .07
    "images/events/prison/event/2/22.png"
    pause .07
    "images/events/prison/event/2/23.png"
    pause .07
    repeat

image cageHandCum1:
    "images/events/prison/event/3/cum/1.png"
    pause .1
    "images/events/prison/event/3/cum/2.png"
    function cum1
    pause .1
    "images/events/prison/event/3/cum/3.png"
    pause .1
    "images/events/prison/event/3/cum/4.png"
    pause .1
    "images/events/prison/event/3/cum/5.png"
    pause .1
    "images/events/prison/event/3/cum/6.png"
    pause .1
    "images/events/prison/event/3/cum/7.png"
    pause .1
    "images/events/prison/event/3/cum/8.png"
    pause .1
    "images/events/prison/event/3/cum/9.png"
    pause .1
    "images/events/prison/event/3/cum/10.png"
    pause .1
    "images/events/prison/event/3/cum/11.png"
    function cum1
    pause .1
    "images/events/prison/event/3/cum/12.png"
    pause .1
    "images/events/prison/event/3/cum/13.png"
    pause .1
    "images/events/prison/event/3/cum/14.png"
    pause .1
    "images/events/prison/event/3/cum/15.png"
    pause .1
    "images/events/prison/event/3/cum/16.png"
    pause .1
    "images/events/prison/event/3/cum/17.png"
    pause .1
    "images/events/prison/event/3/cum/18.png"
    pause .1
    "images/events/prison/event/3/cum/19.png"
    pause .1
    "images/events/prison/event/3/cum/20.png"
    pause .1
    "images/events/prison/event/3/cum/21.png"
    pause .1
    "images/events/prison/event/3/cum/22.png"
    function cum1
    pause .1
    "images/events/prison/event/3/cum/23.png"
    pause .1
    "images/events/prison/event/3/cum/24.png"
    pause .1
    "images/events/prison/event/3/cum/25.png"
    pause .1
    "images/events/prison/event/3/cum/26.png"
    pause .1
    "images/events/prison/event/3/cum/27.png"
    pause .1
    "images/events/prison/event/3/cum/28.png"
    pause .1
    "images/events/prison/event/3/cum/29.png"
    pause .1
    "images/events/prison/event/3/cum/30.png"
    pause .1
    "images/events/prison/event/3/cum/31.png"
    pause .1

image cageHandCum2:
    "images/events/prison/event/2/cum/1.png"
    pause .1
    "images/events/prison/event/2/cum/2.png"
    function cum1
    pause .1
    "images/events/prison/event/2/cum/3.png"
    pause .1
    "images/events/prison/event/2/cum/4.png"
    pause .1
    "images/events/prison/event/2/cum/5.png"
    pause .1
    "images/events/prison/event/2/cum/6.png"
    pause .1
    "images/events/prison/event/2/cum/7.png"
    pause .1
    "images/events/prison/event/2/cum/8.png"
    pause .1
    "images/events/prison/event/2/cum/9.png"
    pause .1
    "images/events/prison/event/2/cum/10.png"
    pause .1
    "images/events/prison/event/2/cum/11.png"
    pause .1
    "images/events/prison/event/2/cum/12.png"
    function cum1
    pause .1
    "images/events/prison/event/2/cum/13.png"
    pause .1
    "images/events/prison/event/2/cum/14.png"
    pause .1
    "images/events/prison/event/2/cum/15.png"
    pause .1
    "images/events/prison/event/2/cum/16.png"
    pause .1
    "images/events/prison/event/2/cum/17.png"
    pause .1
    "images/events/prison/event/2/cum/18.png"
    pause .1
    "images/events/prison/event/2/cum/19.png"
    pause .1
    "images/events/prison/event/2/cum/20.png"
    pause .1
    "images/events/prison/event/2/cum/21.png"
    pause .1
    "images/events/prison/event/2/cum/22.png"
    pause .1
    "images/events/prison/event/2/cum/23.png"
    pause .1
    "images/events/prison/event/2/cum/24.png"
    pause .1
    "images/events/prison/event/2/cum/25.png"
    pause .1
    "images/events/prison/event/2/cum/26.png"
    function cum1
    pause .1
    "images/events/prison/event/2/cum/27.png"
    pause .1
    "images/events/prison/event/2/cum/28.png"
    pause .1
    "images/events/prison/event/2/cum/29.png"
    pause .1
    "images/events/prison/event/2/cum/30.png"
    pause .1
    "images/events/prison/event/2/cum/31.png"
    pause .1

image dogLoop1:
    "images/events/bay1/event/bay1event1.png"
    pause .1
    "images/events/bay1/event/bay1event2.png"
    pause .1
    "images/events/bay1/event/bay1event3.png"
    pause .1
    "images/events/bay1/event/bay1event4.png"
    pause .1
    "images/events/bay1/event/bay1event5.png"
    pause .1
    "images/events/bay1/event/bay1event6.png"
    pause .1
    "images/events/bay1/event/bay1event7.png"
    pause .1
    "images/events/bay1/event/bay1event8.png"
    pause .1
    "images/events/bay1/event/bay1event9.png"
    pause .1
    "images/events/bay1/event/bay1event10.png"
    pause .1
    "images/events/bay1/event/bay1event11.png"
    pause .1
    "images/events/bay1/event/bay1event12.png"
    function lick
    pause .1
    "images/events/bay1/event/bay1event13.png"
    pause .1
    "images/events/bay1/event/bay1event14.png"
    pause .1
    "images/events/bay1/event/bay1event15.png"
    pause .1
    repeat

image dogLoop2:
    "images/events/bay1/event/bay1event16.png"
    pause .1
    "images/events/bay1/event/bay1event17.png"
    pause .1
    "images/events/bay1/event/bay1event18.png"
    pause .1
    "images/events/bay1/event/bay1event19.png"
    pause .1
    "images/events/bay1/event/bay1event20.png"
    pause .1
    "images/events/bay1/event/bay1event21.png"
    pause .1
    "images/events/bay1/event/bay1event22.png"
    pause .1
    "images/events/bay1/event/bay1event23.png"
    pause .1
    "images/events/bay1/event/bay1event24.png"
    pause .1
    "images/events/bay1/event/bay1event25.png"
    pause .1
    "images/events/bay1/event/bay1event26.png"
    pause .1
    "images/events/bay1/event/bay1event27.png"
    pause .1
    "images/events/bay1/event/bay1event28.png"
    pause .1
    "images/events/bay1/event/bay1event29.png"
    pause .1
    "images/events/bay1/event/bay1event30.png"
    pause .1
    repeat

image dogLoop3:
    "images/events/bay1/event/bay1event31.png"
    pause .1
    "images/events/bay1/event/bay1event32.png"
    pause .1
    "images/events/bay1/event/bay1event33.png"
    pause .1
    "images/events/bay1/event/bay1event34.png"
    pause .1
    "images/events/bay1/event/bay1event35.png"
    function inside
    pause .1
    "images/events/bay1/event/bay1event36.png"
    pause .1
    "images/events/bay1/event/bay1event37.png"
    pause .1
    "images/events/bay1/event/bay1event38.png"
    pause .1
    repeat

image dogLoop4:
    "images/events/bay1/event/bay1event39.png"
    pause .15
    "images/events/bay1/event/bay1event40.png"
    pause .15
    "images/events/bay1/event/bay1event41.png"
    pause .15
    "images/events/bay1/event/bay1event42.png"
    function lick
    pause .15
    "images/events/bay1/event/bay1event43.png"
    pause .15
    "images/events/bay1/event/bay1event44.png"
    pause .15
    "images/events/bay1/event/bay1event45.png"
    pause .15
    "images/events/bay1/event/bay1event46.png"
    pause .15
    repeat

image dogLoop5:
    "images/events/bay1/event/bay1event47.png"
    pause .15
    "images/events/bay1/event/bay1event48.png"
    pause .15
    "images/events/bay1/event/bay1event49.png"
    pause .15
    "images/events/bay1/event/bay1event50.png"
    pause .15
    "images/events/bay1/event/bay1event51.png"
    pause .15
    "images/events/bay1/event/bay1event52.png"
    function lick
    pause .15
    "images/events/bay1/event/bay1event53.png"
    pause .15
    "images/events/bay1/event/bay1event54.png"
    pause .15
    repeat

image dogCum:
    "images/events/bay1/event/cum/1.png"
    pause .15
    "images/events/bay1/event/cum/2.png"
    pause .15
    "images/events/bay1/event/cum/3.png"
    function cum1
    pause .15
    "images/events/bay1/event/cum/4.png"
    pause .15
    "images/events/bay1/event/cum/5.png"
    pause .15
    "images/events/bay1/event/cum/6.png"
    pause .15
    "images/events/bay1/event/cum/7.png"
    function cum2
    pause .15
    "images/events/bay1/event/cum/8.png"
    pause .15
    "images/events/bay1/event/cum/9.png"
    pause .15
    "images/events/bay1/event/cum/10.png"
    pause .15
    "images/events/bay1/event/cum/11.png"
    function cum2
    pause .15
    "images/events/bay1/event/cum/12.png"
    pause .15
    "images/events/bay1/event/cum/13.png"
    pause .15
    "images/events/bay1/event/cum/14.png"
    pause .15
    "images/events/bay1/event/cum/15.png"
    pause .15
    "images/events/bay1/event/cum/16.png"
    pause .15
    "images/events/bay1/event/cum/17.png"
    pause .15
    "images/events/bay1/event/cum/18.png"
    pause .15
    "images/events/bay1/event/cum/19.png"
    pause .15
    "images/events/bay1/event/cum/20.png"
    pause .15
    "images/events/bay1/event/cum/21.png"
    pause .15
    "images/events/bay1/event/cum/22.png"
    function cum1
    pause .15
    "images/events/bay1/event/cum/23.png"
    pause .15
    "images/events/bay1/event/cum/24.png"
    pause .15
    "images/events/bay1/event/cum/25.png"
    pause .15
    "images/events/bay1/event/cum/26.png"
    pause .15
    "images/events/bay1/event/cum/27.png"
    pause .15
    "images/events/bay1/event/cum/28.png"
    pause .15
    "images/events/bay1/event/cum/29.png"
    function splat
    pause .15
    "images/events/bay1/event/cum/30.png"
    pause .15
    "images/events/bay1/event/cum/31.png"
    pause .15
    "images/events/bay1/event/cum/32.png"
    pause .15
    "images/events/bay1/event/cum/33.png"
    pause .15
    "images/events/bay1/event/cum/34.png"
    pause .15
    "images/events/bay1/event/cum/35.png"
    pause .15
    "images/events/bay1/event/cum/36.png"
    pause .15
    "images/events/bay1/event/cum/37.png"
    pause .15

image red1_start:
    "images/events/bay1/varren/1.png"
    pause .15
    "images/events/bay1/varren/2.png"
    pause .15
    "images/events/bay1/varren/3.png"
    pause .15
    "images/events/bay1/varren/4.png"
    pause .15
    "images/events/bay1/varren/5.png"
    pause .15
    "images/events/bay1/varren/6.png"
    pause .15
    "images/events/bay1/varren/7.png"
    pause .15
    "images/events/bay1/varren/8.png"
    pause .15
    "images/events/bay1/varren/9.png"
    pause .15
    "images/events/bay1/varren/10.png"
    pause .15
    "images/events/bay1/varren/11.png"
    pause .15
    "images/events/bay1/varren/12.png"
    pause .15
    "images/events/bay1/varren/13.png"
    pause .15
    "images/events/bay1/varren/14.png"
    pause .15
    "images/events/bay1/varren/15.png"
    pause .15
    "images/events/bay1/varren/16.png"
    pause .15
    "images/events/bay1/varren/17.png"
    pause .15
    "images/events/bay1/varren/18.png"
    pause .15
    "images/events/bay1/varren/19.png"
    pause .15
    "images/events/bay1/varren/20.png"
    pause .15
    "images/events/bay1/varren/21.png"
    pause .15
    "images/events/bay1/varren/22.png"
    pause .15
    "images/events/bay1/varren/23.png"
    pause .15
    "images/events/bay1/varren/24.png"
    pause .15
    "images/events/bay1/varren/25.png"
    pause .15
    "images/events/bay1/varren/26.png"
    pause .15
    "images/events/bay1/varren/27.png"
    pause .15
    "images/events/bay1/varren/28.png"
    pause .15
    "images/events/bay1/varren/29.png"
    pause .15
    "images/events/bay1/varren/30.png"
    function inside
    pause .15
    "images/events/bay1/varren/31.png"
    pause .15
    "images/events/bay1/varren/32.png"
    pause .15
    "images/events/bay1/varren/33.png"
    pause .15
    "images/events/bay1/varren/34.png"
    pause .15
    "images/events/bay1/varren/35.png"
    pause .15
    "images/events/bay1/varren/36.png"
    pause .15
    "images/events/bay1/varren/37.png"
    pause .15
    "images/events/bay1/varren/38.png"
    pause .15
    "images/events/bay1/varren/39.png"
    pause .15
    "images/events/bay1/varren/40.png"
    pause .15
    "images/events/bay1/varren/41.png"
    pause .15
    "images/events/bay1/varren/42.png"
    pause .15
    "images/events/bay1/varren/43.png"
    pause .15
    "images/events/bay1/varren/44.png"
    pause .15
    "images/events/bay1/varren/45.png"
    pause .15
    "images/events/bay1/varren/46.png"
    pause .15
    "images/events/bay1/varren/47.png"
    pause .15
    "images/events/bay1/varren/48.png"
    pause .15
    "images/events/bay1/varren/49.png"
    pause .15
    "images/events/bay1/varren/50.png"
    pause .15
    "images/events/bay1/varren/51.png"
    pause .15
    "images/events/bay1/varren/52.png"
    pause .15
    "images/events/bay1/varren/53.png"
    pause .15
    "images/events/bay1/varren/54.png"
    pause .15
    "images/events/bay1/varren/55.png"
    pause .15
    "images/events/bay1/varren/56.png"
    pause .15
    "images/events/bay1/varren/57.png"
    function suck4

image red1_loop1:
    "images/events/bay1/varren/58.png"
    pause .1
    "images/events/bay1/varren/59.png"
    pause .1
    "images/events/bay1/varren/60.png"
    pause .1
    "images/events/bay1/varren/61.png"
    pause .1
    "images/events/bay1/varren/62.png"
    function s2
    pause .1
    "images/events/bay1/varren/63.png"
    pause .1
    repeat

image red1_loop2:
    "images/events/bay1/varren/64.png"
    pause .1
    function suck1
    "images/events/bay1/varren/65.png"
    pause .1
    "images/events/bay1/varren/66.png"
    pause .1
    "images/events/bay1/varren/67.png"
    pause .1
    "images/events/bay1/varren/68.png"
    function s3
    pause .1
    "images/events/bay1/varren/69.png"
    pause .1
    repeat

image red1_loop2_alt:
    "images/events/bay1/varren/64.png"
    pause .07
    function suck2
    "images/events/bay1/varren/65.png"
    pause .07
    "images/events/bay1/varren/66.png"
    pause .07
    "images/events/bay1/varren/67.png"
    pause .07
    "images/events/bay1/varren/68.png"
    function s1
    pause .07
    "images/events/bay1/varren/69.png"
    pause .07
    repeat

image red1_cum:
    "images/events/bay1/varren/cum/1.png"
    pause .15
    "images/events/bay1/varren/cum/2.png"
    pause .15
    "images/events/bay1/varren/cum/3.png"
    function suck4
    pause .15
    "images/events/bay1/varren/cum/4.png"
    pause .15
    "images/events/bay1/varren/cum/5.png"
    pause .15
    "images/events/bay1/varren/cum/6.png"
    pause .15
    "images/events/bay1/varren/cum/7.png"
    pause .15
    "images/events/bay1/varren/cum/8.png"
    pause .15
    "images/events/bay1/varren/cum/9.png"
    pause .15
    "images/events/bay1/varren/cum/10.png"
    pause .15
    "images/events/bay1/varren/cum/11.png"
    pause .15
    "images/events/bay1/varren/cum/12.png"
    pause .15
    "images/events/bay1/varren/cum/13.png"
    pause .15
    function cum1
    "images/events/bay1/varren/cum/14.png"
    pause .15
    "images/events/bay1/varren/cum/15.png"
    pause .15
    "images/events/bay1/varren/cum/16.png"
    pause .15
    "images/events/bay1/varren/cum/17.png"
    pause .15
    "images/events/bay1/varren/cum/18.png"
    pause .15
    "images/events/bay1/varren/cum/19.png"
    pause .15
    "images/events/bay1/varren/cum/20.png"
    pause .15
    "images/events/bay1/varren/cum/21.png"
    pause .15
    "images/events/bay1/varren/cum/22.png"
    pause .15
    "images/events/bay1/varren/cum/23.png"
    pause .15
    "images/events/bay1/varren/cum/24.png"
    function cumsplash
    pause .15
    "images/events/bay1/varren/cum/25.png"
    pause .15
    "images/events/bay1/varren/cum/26.png"
    pause .15
    "images/events/bay1/varren/cum/27.png"
    pause .15
    "images/events/bay1/varren/cum/28.png"
    pause .15
    "images/events/bay1/varren/cum/29.png"
    pause .15
    "images/events/bay1/varren/cum/30.png"
    pause .15
    "images/events/bay1/varren/cum/31.png"
    pause .15
    "images/events/bay1/varren/cum/32.png"
    pause .15
    "images/events/bay1/varren/cum/33.png"
    pause .15
    "images/events/bay1/varren/cum/34.png"
    function swallow
    pause .15
    "images/events/bay1/varren/cum/35.png"
    pause .15
    "images/events/bay1/varren/cum/36.png"
    pause .15
    "images/events/bay1/varren/cum/37.png"
    pause .15

image cageLube_loop1:
    "images/events/prison/event/4/loop1/1.png"
    pause .1
    "images/events/prison/event/4/loop1/2.png"
    pause .1
    "images/events/prison/event/4/loop1/3.png"
    pause .1
    "images/events/prison/event/4/loop1/4.png"
    pause .1
    "images/events/prison/event/4/loop1/5.png"
    pause .1
    "images/events/prison/event/4/loop1/6.png"
    pause .1
    "images/events/prison/event/4/loop1/7.png"
    pause .1
    "images/events/prison/event/4/loop1/8.png"
    pause .1
    "images/events/prison/event/4/loop1/9.png"
    pause .1
    "images/events/prison/event/4/loop1/10.png"
    function inside
    pause .1
    "images/events/prison/event/4/loop1/11.png"
    pause .1
    "images/events/prison/event/4/loop1/12.png"
    pause .1
    "images/events/prison/event/4/loop1/13.png"
    pause .1
    "images/events/prison/event/4/loop1/14.png"
    pause .1
    "images/events/prison/event/4/loop1/15.png"
    pause .1
    "images/events/prison/event/4/loop1/16.png"
    pause .1
    "images/events/prison/event/4/loop1/17.png"
    pause .1
    "images/events/prison/event/4/loop1/18.png"
    pause .1
    "images/events/prison/event/4/loop1/19.png"
    pause .1
    "images/events/prison/event/4/loop1/20.png"
    pause .1
    "images/events/prison/event/4/loop1/21.png"
    pause .1
    repeat

image cageLube_loop2:
    "images/events/prison/event/4/loop2/1.png"
    pause .1
    "images/events/prison/event/4/loop2/2.png"
    pause .1
    "images/events/prison/event/4/loop2/3.png"
    pause .1
    "images/events/prison/event/4/loop2/4.png"
    pause .1
    "images/events/prison/event/4/loop2/5.png"
    function inside
    pause .1
    "images/events/prison/event/4/loop2/6.png"
    pause .1
    "images/events/prison/event/4/loop2/7.png"
    pause .1
    "images/events/prison/event/4/loop2/8.png"
    pause .1
    "images/events/prison/event/4/loop2/9.png"
    pause .1
    "images/events/prison/event/4/loop2/10.png"
    pause .1
    "images/events/prison/event/4/loop2/11.png"
    pause .1
    repeat

image cageLube_loop3:
    "images/events/prison/event/4/loop3/1.png"
    pause .1
    "images/events/prison/event/4/loop3/2.png"
    pause .1
    "images/events/prison/event/4/loop3/3.png"
    pause .1
    "images/events/prison/event/4/loop3/4.png"
    pause .1
    "images/events/prison/event/4/loop3/5.png"
    function slap5
    pause .1
    "images/events/prison/event/4/loop3/6.png"
    pause .1
    "images/events/prison/event/4/loop3/7.png"
    pause .1
    "images/events/prison/event/4/loop3/8.png"
    pause .1
    "images/events/prison/event/4/loop3/9.png"
    pause .1
    repeat

image cageLube_loop3alt:
    "images/events/prison/event/4/loop3/1.png"
    pause .07
    "images/events/prison/event/4/loop3/2.png"
    pause .07
    "images/events/prison/event/4/loop3/3.png"
    pause .07
    "images/events/prison/event/4/loop3/4.png"
    pause .07
    "images/events/prison/event/4/loop3/5.png"
    function slap5
    pause .07
    "images/events/prison/event/4/loop3/6.png"
    pause .07
    "images/events/prison/event/4/loop3/7.png"
    pause .07
    "images/events/prison/event/4/loop3/8.png"
    pause .07
    "images/events/prison/event/4/loop3/9.png"
    pause .07
    repeat

image cageLube_trans:
    "images/events/prison/event/4/trans1/1.png"
    pause .1
    "images/events/prison/event/4/trans1/2.png"
    pause .1
    "images/events/prison/event/4/trans1/3.png"
    pause .1
    "images/events/prison/event/4/trans1/4.png"
    pause .1
    "images/events/prison/event/4/trans1/5.png"
    pause .1
    "images/events/prison/event/4/trans1/6.png"
    pause .1
    "images/events/prison/event/4/trans1/7.png"
    pause .1
    "images/events/prison/event/4/trans1/8.png"
    pause .1
    "images/events/prison/event/4/trans1/9.png"
    pause .1
    "images/events/prison/event/4/trans1/10.png"
    pause .1
    "images/events/prison/event/4/trans1/11.png"
    pause .1
    "images/events/prison/event/4/trans1/12.png"
    pause .1
    "images/events/prison/event/4/trans1/13.png"
    pause .1
    "images/events/prison/event/4/trans1/14.png"
    pause .1
    "images/events/prison/event/4/trans1/15.png"
    pause .1
    "images/events/prison/event/4/trans1/16.png"
    pause .1
    "images/events/prison/event/4/trans1/17.png"
    pause .1
    "images/events/prison/event/4/trans1/18.png"
    pause .1
    "images/events/prison/event/4/trans1/19.png"
    pause .1
    "images/events/prison/event/4/trans1/20.png"
    pause .1
    "images/events/prison/event/4/trans1/21.png"
    pause .1
    "images/events/prison/event/4/trans1/22.png"
    pause .1
    "images/events/prison/event/4/trans1/23.png"
    pause .1
    "images/events/prison/event/4/trans1/24.png"
    pause .1
    "images/events/prison/event/4/trans1/25.png"
    pause .1
    "images/events/prison/event/4/trans1/26.png"
    pause .1
    "images/events/prison/event/4/trans1/27.png"
    function inside
    pause .1
    "images/events/prison/event/4/trans1/28.png"
    pause .1
    "images/events/prison/event/4/trans1/29.png"
    pause .1
    "images/events/prison/event/4/trans1/30.png"
    pause .1

image cageLube_cum:
    "images/events/prison/event/4/cum/1.png"
    pause .1
    "images/events/prison/event/4/cum/2.png"
    pause .1
    "images/events/prison/event/4/cum/3.png"
    pause .1
    "images/events/prison/event/4/cum/4.png"
    pause .1
    "images/events/prison/event/4/cum/5.png"
    pause .1
    "images/events/prison/event/4/cum/6.png"
    pause .1
    "images/events/prison/event/4/cum/7.png"
    pause .1
    "images/events/prison/event/4/cum/8.png"
    pause .1
    "images/events/prison/event/4/cum/9.png"
    pause .1
    "images/events/prison/event/4/cum/10.png"
    pause .1
    "images/events/prison/event/4/cum/11.png"
    pause .1
    "images/events/prison/event/4/cum/12.png"
    pause .1
    "images/events/prison/event/4/cum/13.png"
    pause .1
    "images/events/prison/event/4/cum/14.png"
    pause .1
    "images/events/prison/event/4/cum/15.png"
    function cum1
    pause .1
    "images/events/prison/event/4/cum/16.png"
    pause .1
    "images/events/prison/event/4/cum/17.png"
    pause .1
    "images/events/prison/event/4/cum/18.png"
    pause .1
    "images/events/prison/event/4/cum/19.png"
    pause .1
    "images/events/prison/event/4/cum/20.png"
    function cum1
    pause .1
    "images/events/prison/event/4/cum/21.png"
    pause .1
    "images/events/prison/event/4/cum/22.png"
    pause .1
    "images/events/prison/event/4/cum/23.png"
    pause .1
    "images/events/prison/event/4/cum/24.png"
    pause .1
    "images/events/prison/event/4/cum/25.png"
    pause .1
    "images/events/prison/event/4/cum/26.png"
    function cum2
    pause .1
    "images/events/prison/event/4/cum/27.png"
    pause .1
    "images/events/prison/event/4/cum/28.png"
    pause .1
    "images/events/prison/event/4/cum/29.png"
    pause .1
    "images/events/prison/event/4/cum/30.png"
    pause .1

image double_loop1:
    "images/events/doubleG/loop1/1.png"
    pause .1
    "images/events/doubleG/loop1/2.png"
    pause .1
    "images/events/doubleG/loop1/3.png"
    pause .1
    "images/events/doubleG/loop1/4.png"
    pause .1
    "images/events/doubleG/loop1/5.png"
    function slap5
    pause .1
    "images/events/doubleG/loop1/6.png"
    pause .1
    "images/events/doubleG/loop1/7.png"
    pause .1
    "images/events/doubleG/loop1/8.png"
    pause .1
    "images/events/doubleG/loop1/9.png"
    pause .1
    "images/events/doubleG/loop1/10.png"
    pause .1
    repeat

image double_trans1:
    "images/events/doubleG/trans1/1.png"
    pause .1
    "images/events/doubleG/trans1/2.png"
    pause .1
    "images/events/doubleG/trans1/3.png"
    pause .1
    "images/events/doubleG/trans1/4.png"
    pause .1
    "images/events/doubleG/trans1/5.png"
    pause .1
    "images/events/doubleG/trans1/6.png"
    pause .1
    "images/events/doubleG/trans1/7.png"
    pause .1
    "images/events/doubleG/trans1/8.png"
    function slap1
    pause .1
    "images/events/doubleG/trans1/9.png"
    pause .1
    "images/events/doubleG/trans1/10.png"
    pause .1
    "images/events/doubleG/trans1/11.png"
    pause .1
    "images/events/doubleG/trans1/12.png"
    pause .1
    "images/events/doubleG/trans1/13.png"
    pause .1
    "images/events/doubleG/trans1/14.png"
    pause .1
    "images/events/doubleG/trans1/15.png"
    pause .1
    "images/events/doubleG/trans1/16.png"
    pause .1
    "images/events/doubleG/trans1/17.png"
    pause .1
    "images/events/doubleG/trans1/18.png"
    pause .1
    "images/events/doubleG/trans1/19.png"
    pause .1
    "images/events/doubleG/trans1/20.png"
    pause .1
    "images/events/doubleG/trans1/21.png"
    pause .1
    "images/events/doubleG/trans1/22.png"
    pause .1
    "images/events/doubleG/trans1/23.png"
    pause .1
    "images/events/doubleG/trans1/24.png"
    pause .1
    "images/events/doubleG/trans1/25.png"
    pause .1
    "images/events/doubleG/trans1/26.png"
    pause .1
    "images/events/doubleG/trans1/27.png"
    pause .1
    "images/events/doubleG/trans1/28.png"
    pause .1
    "images/events/doubleG/trans1/29.png"
    pause .1
    "images/events/doubleG/trans1/30.png"
    pause .1
    "images/events/doubleG/trans1/31.png"
    pause .1
    "images/events/doubleG/trans1/32.png"
    pause .1
    "images/events/doubleG/trans1/33.png"
    pause .1

image double_trans2:
    "images/events/doubleG/trans1/34.png"
    pause .1
    "images/events/doubleG/trans1/35.png"
    pause .1
    "images/events/doubleG/trans1/36.png"
    pause .1
    "images/events/doubleG/trans1/37.png"
    pause .1
    "images/events/doubleG/trans1/38.png"
    function s2
    pause .1
    "images/events/doubleG/trans1/39.png"
    pause .1
    "images/events/doubleG/trans1/40.png"
    pause .1

image double_loop2:
    "images/events/doubleG/loop2/1.png"
    pause .08
    "images/events/doubleG/loop2/2.png"
    pause .08
    "images/events/doubleG/loop2/3.png"
    pause .08
    "images/events/doubleG/loop2/4.png"
    pause .08
    "images/events/doubleG/loop2/5.png"
    function slap5
    pause .08
    "images/events/doubleG/loop2/6.png"
    pause .08
    "images/events/doubleG/loop2/7.png"
    pause .08
    "images/events/doubleG/loop2/8.png"
    function s2
    pause .08
    "images/events/doubleG/loop2/9.png"
    pause .08
    "images/events/doubleG/loop2/10.png"
    pause .08
    repeat

image double_cum:
    "images/events/doubleG/cum/1.png"
    pause .1
    "images/events/doubleG/cum/2.png"
    pause .1
    "images/events/doubleG/cum/3.png"
    pause .1
    "images/events/doubleG/cum/4.png"
    pause .1
    "images/events/doubleG/cum/5.png"
    pause .1
    "images/events/doubleG/cum/6.png"
    function cum1
    pause .1
    "images/events/doubleG/cum/7.png"
    pause .1
    "images/events/doubleG/cum/8.png"
    pause .1
    "images/events/doubleG/cum/9.png"
    pause .1
    "images/events/doubleG/cum/10.png"
    pause .1
    "images/events/doubleG/cum/11.png"
    pause .1
    "images/events/doubleG/cum/12.png"
    pause .1
    "images/events/doubleG/cum/13.png"
    pause .1
    "images/events/doubleG/cum/14.png"
    function cum1
    pause .1
    "images/events/doubleG/cum/15.png"
    pause .1
    "images/events/doubleG/cum/16.png"
    pause .1
    "images/events/doubleG/cum/17.png"
    pause .1
    "images/events/doubleG/cum/18.png"
    pause .1
    "images/events/doubleG/cum/19.png"
    pause .1
    "images/events/doubleG/cum/20.png"
    pause .1
    "images/events/doubleG/cum/21.png"
    pause .1
    "images/events/doubleG/cum/22.png"
    function splat
    pause .1
    "images/events/doubleG/cum/23.png"
    pause .1
    "images/events/doubleG/cum/24.png"
    pause .1
    "images/events/doubleG/cum/25.png"
    pause .1
    "images/events/doubleG/cum/26.png"
    pause .1
    "images/events/doubleG/cum/27.png"
    pause .1
    "images/events/doubleG/cum/28.png"
    pause .1
    "images/events/doubleG/cum/29.png"
    pause .1
    "images/events/doubleG/cum/30.png"
    pause .1
    "images/events/doubleG/cum/31.png"
    pause .1
    "images/events/doubleG/cum/32.png"
    pause .1
    "images/events/doubleG/cum/33.png"
    pause .1
    "images/events/doubleG/cum/34.png"
    pause .1
    "images/events/doubleG/cum/35.png"
    pause .1
    "images/events/doubleG/cum/36.png"
    pause .1
    "images/events/doubleG/cum/37.png"
    pause .1
    "images/events/doubleG/cum/38.png"
    pause .1
    "images/events/doubleG/cum/39.png"
    pause .1
    "images/events/doubleG/cum/40.png"
    function fart2
    pause .1
    "images/events/doubleG/cum/41.png"
    pause .1
    "images/events/doubleG/cum/42.png"
    pause .1
    "images/events/doubleG/cum/43.png"
    pause .1
    "images/events/doubleG/cum/44.png"
    pause .1
    "images/events/doubleG/cum/45.png"
    pause .1

image tali1_loop1:
    "images/events/jesora/Tpov/loop1/0.png"
    pause .1
    "images/events/jesora/Tpov/loop1/1.png"
    pause .1
    "images/events/jesora/Tpov/loop1/2.png"
    pause .1
    "images/events/jesora/Tpov/loop1/3.png"
    pause .1
    "images/events/jesora/Tpov/loop1/4.png"
    pause .1
    "images/events/jesora/Tpov/loop1/5.png"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/6.png"
    pause .1
    "images/events/jesora/Tpov/loop1/7.png"
    pause .1
    "images/events/jesora/Tpov/loop1/8.png"
    pause .1
    "images/events/jesora/Tpov/loop1/9.png"
    pause .1
    "images/events/jesora/Tpov/loop1/10.png"
    pause .1
    "images/events/jesora/Tpov/loop1/11.png"
    pause .1
    "images/events/jesora/Tpov/loop1/12.png"
    pause .1
    "images/events/jesora/Tpov/loop1/13.png"
    pause .1
    "images/events/jesora/Tpov/loop1/14.png"
    pause .1
    "images/events/jesora/Tpov/loop1/15.png"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/16.png"
    pause .1
    "images/events/jesora/Tpov/loop1/17.png"
    pause .1
    "images/events/jesora/Tpov/loop1/18.png"
    pause .1
    "images/events/jesora/Tpov/loop1/19.png"
    pause .1
    "images/events/jesora/Tpov/loop1/20.png"
    pause .1
    "images/events/jesora/Tpov/loop1/21.png"
    pause .1
    "images/events/jesora/Tpov/loop1/22.png"
    pause .1
    "images/events/jesora/Tpov/loop1/23.png"
    pause .1
    "images/events/jesora/Tpov/loop1/24.png"
    pause .1
    "images/events/jesora/Tpov/loop1/25.png"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/26.png"
    pause .1
    "images/events/jesora/Tpov/loop1/27.png"
    pause .1
    "images/events/jesora/Tpov/loop1/28.png"
    pause .1
    "images/events/jesora/Tpov/loop1/29.png"
    pause .1
    "images/events/jesora/Tpov/loop1/30.png"
    pause .1
    "images/events/jesora/Tpov/loop1/31.png"
    pause .1
    "images/events/jesora/Tpov/loop1/32.png"
    pause .1
    "images/events/jesora/Tpov/loop1/33.png"
    pause .1
    "images/events/jesora/Tpov/loop1/34.png"
    pause .1
    "images/events/jesora/Tpov/loop1/35.png"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/36.png"
    pause .1
    "images/events/jesora/Tpov/loop1/37.png"
    pause .1
    "images/events/jesora/Tpov/loop1/38.png"
    pause .1
    "images/events/jesora/Tpov/loop1/39.png"
    pause .1
    "images/events/jesora/Tpov/loop1/40.png"
    pause .1
    "images/events/jesora/Tpov/loop1/41.png"
    pause .1
    "images/events/jesora/Tpov/loop1/42.png"
    pause .1
    "images/events/jesora/Tpov/loop1/43.png"
    pause .1
    "images/events/jesora/Tpov/loop1/44.png"
    pause .1
    "images/events/jesora/Tpov/loop1/45.png"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/46.png"
    pause .1
    "images/events/jesora/Tpov/loop1/47.png"
    pause .1
    "images/events/jesora/Tpov/loop1/48.png"
    pause .1
    "images/events/jesora/Tpov/loop1/49.png"
    pause .1
    "images/events/jesora/Tpov/loop1/50.png"
    pause .1
    "images/events/jesora/Tpov/loop1/51.png"
    pause .1
    "images/events/jesora/Tpov/loop1/52.png"
    pause .1
    "images/events/jesora/Tpov/loop1/53.png"
    pause .1
    "images/events/jesora/Tpov/loop1/54.png"
    pause .1
    "images/events/jesora/Tpov/loop1/55.png"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/56.png"
    pause .1
    "images/events/jesora/Tpov/loop1/57.png"
    pause .1
    "images/events/jesora/Tpov/loop1/58.png"
    pause .1
    "images/events/jesora/Tpov/loop1/59.png"
    pause .1
    "images/events/jesora/Tpov/loop1/60.png"
    pause .1
    "images/events/jesora/Tpov/loop1/61.png"
    pause .1
    "images/events/jesora/Tpov/loop1/62.png"
    pause .1
    "images/events/jesora/Tpov/loop1/63.png"
    pause .1
    "images/events/jesora/Tpov/loop1/64.png"
    pause .1
    "images/events/jesora/Tpov/loop1/65.png"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/66.png"
    pause .1
    "images/events/jesora/Tpov/loop1/67.png"
    pause .1
    "images/events/jesora/Tpov/loop1/68.png"
    pause .1
    "images/events/jesora/Tpov/loop1/69.png"
    pause .1
    "images/events/jesora/Tpov/loop1/70.png"
    pause .1
    "images/events/jesora/Tpov/loop1/71.png"
    pause .1
    "images/events/jesora/Tpov/loop1/72.png"
    pause .1
    "images/events/jesora/Tpov/loop1/73.png"
    pause .1
    "images/events/jesora/Tpov/loop1/74.png"
    pause .1
    "images/events/jesora/Tpov/loop1/75.png"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/76.png"
    pause .1
    repeat

image tali1_trans1:
    "images/events/jesora/Tpov/trans1/0077.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0078.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0079.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0080.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0081.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0082.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0083.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0084.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0085.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0086.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0087.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0088.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0089.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0090.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0091.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0092.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0093.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0094.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0095.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0096.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0097.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0098.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0099.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0100.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0101.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0102.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0103.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0104.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0105.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0106.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0107.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0108.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0109.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0110.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0111.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0112.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0113.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0114.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0115.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0116.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0117.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0118.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0119.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0120.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0121.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0122.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0123.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0124.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0125.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0126.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0127.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0128.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0129.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0130.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0131.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0132.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0133.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0134.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0135.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0136.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0137.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0138.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0139.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0140.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0141.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0142.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0143.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0144.png"
    pause .1

image tali1_trans2:
    "images/events/jesora/Tpov/trans1/0145.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0146.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0147.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0148.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0149.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0150.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0151.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0152.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0153.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0154.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0155.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0156.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0157.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0158.png"
    function suck4
    pause .1
    "images/events/jesora/Tpov/trans1/0159.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0160.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0161.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0162.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0163.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0164.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0165.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0166.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0167.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0168.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0169.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0170.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0171.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0172.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0173.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0174.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0175.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0176.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0177.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0178.png"
    pause .1
    "images/events/jesora/Tpov/trans1/0179.png"
    pause .1

image tali1_loop2:
    "images/events/jesora/Tpov/loop2/0180.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0181.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0182.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0183.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0184.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0185.png"
    function suck1
    pause .1
    "images/events/jesora/Tpov/loop2/0186.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0187.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0188.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0189.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0190.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0191.png"
    pause .1
    "images/events/jesora/Tpov/loop2/0192.png"
    pause .1
    repeat

image tali1_trans3:
    "images/events/jesora/Tpov/trans2/0194.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0195.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0196.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0197.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0198.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0199.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0200.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0201.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0202.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0203.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0204.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0205.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0206.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0207.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0208.png"
    function suck4
    pause .1
    "images/events/jesora/Tpov/trans2/0209.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0210.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0211.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0212.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0213.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0214.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0215.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0216.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0217.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0218.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0219.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0220.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0221.png"
    function suck1
    pause .1
    "images/events/jesora/Tpov/trans2/0222.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0223.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0224.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0225.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0226.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0227.png"
    pause .1
    "images/events/jesora/Tpov/trans2/0228.png"
    pause .1

image tali1_loop3:
    "images/events/jesora/Tpov/loop3/0229.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0230.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0231.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0232.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0233.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0234.png"
    function suck4
    pause .1
    "images/events/jesora/Tpov/loop3/0235.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0236.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0237.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0238.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0239.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0240.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0241.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0242.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0243.png"
    function suck3
    pause .1
    "images/events/jesora/Tpov/loop3/0244.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0245.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0246.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0247.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0248.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0249.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0250.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0251.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0252.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0253.png"
    function suck4
    pause .1
    "images/events/jesora/Tpov/loop3/0254.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0255.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0256.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0257.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0258.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0259.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0260.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0261.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0262.png"
    function suck1
    pause .1
    "images/events/jesora/Tpov/loop3/0263.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0264.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0265.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0266.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0267.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0268.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0269.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0270.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0271.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0272.png"
    function suck2
    pause .1
    "images/events/jesora/Tpov/loop3/0273.png"
    pause .1
    "images/events/jesora/Tpov/loop3/0274.png"
    pause .1
    repeat

image tali1_trans4:
    "images/events/jesora/Tpov/trans3/0275.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0276.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0277.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0278.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0279.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0280.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0281.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0282.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0283.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0284.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0285.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0286.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0287.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0288.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0289.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0290.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0291.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0292.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0293.png"
    function s2
    pause .1
    "images/events/jesora/Tpov/trans3/0294.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0295.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0296.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0297.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0298.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0299.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0300.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0301.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0302.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0303.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0304.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0305.png"
    pause .1
    "images/events/jesora/Tpov/trans3/0306.png"
    pause .1

image tali1_loop4:
    "images/events/jesora/Tpov/loop4/0307.png"
    pause .1
    "images/events/jesora/Tpov/loop4/0308.png"
    pause .1
    "images/events/jesora/Tpov/loop4/0309.png"
    pause .1
    "images/events/jesora/Tpov/loop4/0310.png"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop4/0311.png"
    pause .1
    "images/events/jesora/Tpov/loop4/0312.png"
    pause .1
    "images/events/jesora/Tpov/loop4/0313.png"
    pause .1
    "images/events/jesora/Tpov/loop4/0314.png"
    pause .1
    repeat

image tali1_cum:
    "images/events/jesora/Tpov/cum/0321.png"
    pause .1
    "images/events/jesora/Tpov/cum/0322.png"
    pause .1
    "images/events/jesora/Tpov/cum/0323.png"
    pause .1
    "images/events/jesora/Tpov/cum/0324.png"
    pause .1
    "images/events/jesora/Tpov/cum/0325.png"
    pause .1
    "images/events/jesora/Tpov/cum/0326.png"
    pause .1
    "images/events/jesora/Tpov/cum/0327.png"
    pause .1
    "images/events/jesora/Tpov/cum/0328.png"
    function cum1
    pause .1
    "images/events/jesora/Tpov/cum/0329.png"
    pause .1
    "images/events/jesora/Tpov/cum/0330.png"
    pause .1
    "images/events/jesora/Tpov/cum/0331.png"
    pause .1
    "images/events/jesora/Tpov/cum/0332.png"
    pause .1
    "images/events/jesora/Tpov/cum/0333.png"
    pause .1
    "images/events/jesora/Tpov/cum/0334.png"
    pause .1
    "images/events/jesora/Tpov/cum/0335.png"
    pause .1
    "images/events/jesora/Tpov/cum/0336.png"
    pause .1
    "images/events/jesora/Tpov/cum/0337.png"
    pause .1
    "images/events/jesora/Tpov/cum/0338.png"
    pause .1
    "images/events/jesora/Tpov/cum/0339.png"
    function cum1
    pause .1
    "images/events/jesora/Tpov/cum/0340.png"
    pause .1
    "images/events/jesora/Tpov/cum/0341.png"
    pause .1
    "images/events/jesora/Tpov/cum/0342.png"
    pause .1
    "images/events/jesora/Tpov/cum/0343.png"
    pause .1
    "images/events/jesora/Tpov/cum/0344.png"
    pause .1
    "images/events/jesora/Tpov/cum/0345.png"
    pause .1
    "images/events/jesora/Tpov/cum/0346.png"
    pause .1
    "images/events/jesora/Tpov/cum/0347.png"
    pause .1
    "images/events/jesora/Tpov/cum/0348.png"
    pause .1
    "images/events/jesora/Tpov/cum/0349.png"
    pause .1
    "images/events/jesora/Tpov/cum/0350.png"
    pause .1
    "images/events/jesora/Tpov/cum/0351.png"
    pause .1
    "images/events/jesora/Tpov/cum/0352.png"
    pause .1
    "images/events/jesora/Tpov/cum/0353.png"
    pause .1
    "images/events/jesora/Tpov/cum/0354.png"
    pause .1
    "images/events/jesora/Tpov/cum/0355.png"
    function cum2
    pause .1
    "images/events/jesora/Tpov/cum/0356.png"
    pause .1
    "images/events/jesora/Tpov/cum/0357.png"
    pause .1
    "images/events/jesora/Tpov/cum/0358.png"
    pause .1
    "images/events/jesora/Tpov/cum/0359.png"
    pause .1
    "images/events/jesora/Tpov/cum/0360.png"
    pause .1
    "images/events/jesora/Tpov/cum/0361.png"
    pause .1
    "images/events/jesora/Tpov/cum/0362.png"

image hypno:
    "images/events/jesora/hypno/0.png"
    pause 0.20
    "images/events/jesora/hypno/1.png"
    pause 0.20
    "images/events/jesora/hypno/2.png"
    pause 0.20
    "images/events/jesora/hypno/3.png"
    pause 0.20
    "images/events/jesora/hypno/4.png"
    pause 0.20
    "images/events/jesora/hypno/5.png"
    pause 0.20
    "images/events/jesora/hypno/6.png"
    pause 0.20

image jesora1_loop1:
    "images/events/jesora/Jpov/loop1/0000.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0001.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0002.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0003.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0004.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0005.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0006.png"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0007.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0008.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0009.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0010.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0011.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0012.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0013.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0014.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0015.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0016.png"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0017.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0018.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0019.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0020.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0021.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0022.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0023.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0024.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0025.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0026.png"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0027.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0028.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0029.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0030.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0031.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0032.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0033.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0034.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0035.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0036.png"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0037.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0038.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0039.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0040.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0041.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0042.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0043.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0044.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0045.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0046.png"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0047.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0048.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0049.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0050.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0051.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0052.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0053.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0054.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0055.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0056.png"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0057.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0058.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0059.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0060.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0061.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0062.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0063.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0064.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0065.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0066.png"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0067.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0068.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0069.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0070.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0071.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0072.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0073.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0074.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0075.png"
    pause .1
    "images/events/jesora/Jpov/loop1/0076.png"
    function inside
    pause .1
    repeat

image jesora1_trans1:
    "images/events/jesora/Jpov/trans1/0077.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0078.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0079.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0080.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0081.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0082.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0083.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0084.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0085.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0086.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0087.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0088.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0089.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0090.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0091.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0092.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0093.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0094.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0095.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0096.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0097.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0098.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0099.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0100.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0101.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0102.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0103.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0104.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0105.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0106.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0107.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0108.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0109.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0110.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0111.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0112.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0113.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0114.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0115.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0116.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0117.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0118.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0119.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0120.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0121.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0122.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0123.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0124.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0125.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0126.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0127.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0128.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0129.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0130.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0131.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0132.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0133.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0134.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0135.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0136.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0137.png"
    pause .1
    "images/events/jesora/Jpov/trans1/0138.png"
    pause .1

image jesora1_trans2:
    "images/events/jesora/Jpov/trans2/0139.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0140.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0141.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0142.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0143.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0144.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0145.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0146.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0147.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0148.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0149.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0150.png"
    function s2
    pause .1
    "images/events/jesora/Jpov/trans2/0151.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0152.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0153.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0154.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0155.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0156.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0157.png"
    pause .1
    "images/events/jesora/Jpov/trans2/0158.png"
    function suck4
    pause .1
    "images/events/jesora/Jpov/trans2/0159.png"
    pause .1

image jesora1_loop2:
    "images/events/jesora/Jpov/loop2/0160.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0161.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0162.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0163.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0164.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0165.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0166.png"
    function suck1
    pause .1
    "images/events/jesora/Jpov/loop2/0167.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0168.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0169.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0170.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0171.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0172.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0173.png"
    pause .1
    "images/events/jesora/Jpov/loop2/0174.png"
    pause .1
    repeat

image jesora1_loop3:
    "images/events/jesora/Jpov/loop3/0176.png"
    pause .1
    "images/events/jesora/Jpov/loop3/0177.png"
    pause .1
    "images/events/jesora/Jpov/loop3/0178.png"
    pause .1
    "images/events/jesora/Jpov/loop3/0179.png"
    function suck4
    pause .1
    "images/events/jesora/Jpov/loop3/0180.png"
    pause .1
    "images/events/jesora/Jpov/loop3/0181.png"
    pause .1
    "images/events/jesora/Jpov/loop3/0182.png"
    pause .1
    "images/events/jesora/Jpov/loop3/0183.png"
    pause .1
    "images/events/jesora/Jpov/loop3/0184.png"
    pause .1
    "images/events/jesora/Jpov/loop3/0185.png"
    pause .1
    "images/events/jesora/Jpov/loop3/0186.png"
    pause .1
    repeat

image jesora1_trans3:
    "images/events/jesora/Jpov/trans3/0187.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0188.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0189.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0190.png"
    function s2
    pause .1
    "images/events/jesora/Jpov/trans3/0191.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0192.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0193.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0194.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0195.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0196.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0197.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0198.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0199.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0200.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0201.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0202.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0203.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0204.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0205.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0206.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0207.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0208.png"
    pause .1
    "images/events/jesora/Jpov/trans3/0209.png"
    pause .1

image jesora1_loop4:
    "images/events/jesora/Jpov/loop4/0210.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0211.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0212.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0213.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0214.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0215.png"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop4/0216.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0217.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0218.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0219.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0220.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0221.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0222.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0223.png"
    pause .1
    "images/events/jesora/Jpov/loop4/0224.png"
    pause .1
    repeat

image jesora1_cum:
    "images/events/jesora/Jpov/cum/0210.png"
    pause .1
    "images/events/jesora/Jpov/cum/0211.png"
    pause .1
    "images/events/jesora/Jpov/cum/0212.png"
    pause .1
    "images/events/jesora/Jpov/cum/0213.png"
    pause .1
    "images/events/jesora/Jpov/cum/0214.png"
    function cum1
    pause .1
    "images/events/jesora/Jpov/cum/0215.png"
    pause .1
    "images/events/jesora/Jpov/cum/0216.png"
    pause .1
    "images/events/jesora/Jpov/cum/0217.png"
    pause .1
    "images/events/jesora/Jpov/cum/0218.png"
    pause .1
    "images/events/jesora/Jpov/cum/0219.png"
    pause .1
    "images/events/jesora/Jpov/cum/0220.png"
    pause .1
    "images/events/jesora/Jpov/cum/0221.png"
    pause .1
    "images/events/jesora/Jpov/cum/0222.png"
    pause .1
    "images/events/jesora/Jpov/cum/0223.png"
    pause .1
    "images/events/jesora/Jpov/cum/0224.png"
    pause .1
    "images/events/jesora/Jpov/cum/0225.png"
    pause .1
    "images/events/jesora/Jpov/cum/0226.png"
    function cum1
    pause .1
    "images/events/jesora/Jpov/cum/0227.png"
    pause .1
    "images/events/jesora/Jpov/cum/0228.png"
    pause .1
    "images/events/jesora/Jpov/cum/0229.png"
    pause .1
    "images/events/jesora/Jpov/cum/0230.png"
    pause .1
    "images/events/jesora/Jpov/cum/0231.png"
    pause .1
    "images/events/jesora/Jpov/cum/0232.png"
    pause .1
    "images/events/jesora/Jpov/cum/0233.png"
    pause .1
    "images/events/jesora/Jpov/cum/0234.png"
    pause .1
    "images/events/jesora/Jpov/cum/0235.png"
    pause .1
    "images/events/jesora/Jpov/cum/0236.png"
    pause .1
    "images/events/jesora/Jpov/cum/0237.png"
    pause .1
    "images/events/jesora/Jpov/cum/0238.png"
    pause .1
    "images/events/jesora/Jpov/cum/0239.png"
    pause .1
    "images/events/jesora/Jpov/cum/0240.png"
    pause .1
    "images/events/jesora/Jpov/cum/0241.png"
    pause .1
    "images/events/jesora/Jpov/cum/0242.png"
    pause .1
    "images/events/jesora/Jpov/cum/0243.png"
    pause .1
    "images/events/jesora/Jpov/cum/0244.png"
    pause .1
    "images/events/jesora/Jpov/cum/0245.png"
    pause .1
    "images/events/jesora/Jpov/cum/0246.png"
    pause .1
    "images/events/jesora/Jpov/cum/0247.png"
    pause .1
    "images/events/jesora/Jpov/cum/0248.png"
    pause .1
    "images/events/jesora/Jpov/cum/0249.png"
    function cum2
    pause .1
    "images/events/jesora/Jpov/cum/0250.png"
    pause .1
    "images/events/jesora/Jpov/cum/0251.png"
    pause .1
    "images/events/jesora/Jpov/cum/0252.png"
    pause .1
    "images/events/jesora/Jpov/cum/0253.png"
    pause .1
    "images/events/jesora/Jpov/cum/0254.png"
    pause .1
    "images/events/jesora/Jpov/cum/0255.png"
    pause .1
    "images/events/jesora/Jpov/cum/0256.png"
    pause .1
    "images/events/jesora/Jpov/cum/0257.png"
    pause .1
    "images/events/jesora/Jpov/cum/0258.png"
    pause .1


init -1 python:
    def s1(trans, st, at):
        renpy.play("audio/s1.mp3", channel="sound")

    def s2(trans, st, at):
        renpy.play("audio/s2.mp3", channel="sound")

    def s3(trans, st, at):
        renpy.play("audio/s3.mp3", channel="sound")

    def s4(trans, st, at):
        renpy.play("audio/s4.mp3", channel="sound")

    def tier(trans, st, at):
        renpy.play("audio/tier.mp3", channel="sound")

    def wetsquish(trans, st, at):
        renpy.play("audio/wetsquish.mp3", channel="sound")

    def lick(trans, st, at):
        renpy.play("audio/lick.mp3", channel="sound")

    def splat(trans, st, at):
        renpy.play("audio/lewdsplat.mp3", channel="sound")

    def slosh(trans, st, at):
        renpy.play("audio/slosh.ogg", channel="sound")

    def suck1(trans, st, at):
        renpy.play("audio/sucking1.ogg", channel="sound")

    def suck2(trans, st, at):
        renpy.play("audio/sucking2.ogg", channel="sound")

    def suck3(trans, st, at):
        renpy.play("audio/sucking3.ogg", channel="sound")

    def suck4(trans, st, at):
        renpy.play("audio/sucking4.ogg", channel="sound")

    def slap1(trans, st, at):
        renpy.play("audio/slap1.mp3", channel="sound")

    def slap2(trans, st, at):
        renpy.play("audio/slap2.mp3", channel="sound")

    def slap3(trans, st, at):
        renpy.play("audio/slap3.mp3", channel="sound")

    def slap4(trans, st, at):
        renpy.play("audio/slap4.mp3", channel="sound")

    def slap5(trans, st, at):
        renpy.play("audio/slap5.mp3", channel="sound")

    def slap6(trans, st, at):
        renpy.play("audio/slap6.mp3", channel="sound")

    def slap7(trans, st, at):
        renpy.play("audio/slap7.mp3", channel="sound")

    def slap8(trans, st, at):
        renpy.play("audio/slap8.mp3", channel="sound")

    def slap9(trans, st, at):
        renpy.play("audio/slap9.mp3", channel="sound")

    def cum1(trans, st, at):
        renpy.play("audio/cumshot1.ogg", channel="sound")

    def cum2(trans, st, at):
        renpy.play("audio/cumshot2.ogg", channel="sound")

    def swallow(trans, st, at):
        renpy.play("audio/swallow.ogg", channel="sound")

    def inside(trans, st, at):
        renpy.play("audio/inside.mp3", channel="sound")

    def fart(trans, st, at):
        renpy.play("audio/fart.mp3", channel="sound")

    def fart2(trans, st, at):
        renpy.play("audio/fart2.mp3", channel="sound")

    def cumsplash(trans, st, at):
        renpy.play("audio/cumsplash.mp3", channel="sound")








# The game starts here.

label splashscreen:
    scene black
    pause 1
    scene bg disclamer1
    with dis
    $ renpy.pause ()
    scene bg disclamer2
    with Pause(2)
    $ renpy.pause ()
    return


label start:


    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # ================================================ ACT 1 START  =========================================================================================
    scene black
    play music "audio/bg/common_bg.mp3" volume 0.3 loop
    "Somewhere on the outer rim of Terminus Space, far from civilization and farther from the nearest port, the young quarian pilgrim Tali'Zorah hopes to find valuable tech and exciting new discoveries."
    #jump jesoraCabin
    scene bg start1
    with dis
    show tali tool at left
    with dis

    tali "A station? No... a ship? This far out? This is Tali'Zorah, do you copy? This is Tali'Zorah, does anyone read me? Unidentified spacecraft, come in."
    show tali shame at left
    with dis
    tali "Strange. No answer, no identification, or radar tags. It appears to just... drift in orbit. The scans show a functioning generator at least. Still..."
    show tali tool at left
    with dis
    tali "Keelah, who designed that hunk of junk? It looks thrown together! It may be good for salvage but..."
    show tali gunstand at left
    with dis
    tali "Okay. Lets make this quick. Maybe its abandoned, maybe not. Regardless, I can't pass up this opportunity. There might be something in there I can bring back to the Flotilla."

    scene bg start2
    with dis
    "After two passing sweeps around the drifting spacecraft, Tali finally found a half-ruined docking bay to land her ship."
    show tali tool at left
    with dis
    tali "Okay, nice and slow. It's... quiet. Maybe the ship really is abandoned? The docking module seems fucntional. Alright. Time to check the damage."

    scene bg start3
    with dis
    show tali gunstand
    with dis
    tali "The lights seem to work. Filtration systems enabled. How long has this ship been abandoned?"
    show tali tool at left
    with moveinleft
    tali "Alright. Once I've synchronized my omni-tool with the ships local network I should be... there. Lets check if there's anything of note on this floating lump of scrap."
    menu entrance:
        "Scan for life signs" if flag1:
            $ flag1 = False
            tali "This whole ship just lit up like a colony station! What the hell, why was no one responding...?"
        "Download schematics" if flag2:
            $ flag2 = False
            tali "Corrupted. What did I expect? Still this ship is really huge. Its not much but it'll do."
        "Investigate the ship's integrity" if flag3:
            $ flag3 = False
            tali "Critical systems are still operational. Secondary generators are kicking in to compensate for the primary's failure. The engines are functional but disabled. I see... one other ship docked on the other side?"
        "I have a bad feeling about this" if flag1 == False and flag2 == False and flag3 == False:
            show tali gunstand at left
            with dis
            tali "Something is very wrong here. I have to leave. NOW."
            jump GoNext_1

    jump entrance

    label GoNext_1:
        scene bg start4
        with dis
        play sound "audio/explosion.mp3"
        pause 2
        show tali angry at left
        tali "What? No, no, no! My ship!"

    scene bg start5
    with dis
    play sound "audio/creepmany.wav"
    pause 2
    show tali gunstand at left
    play sound "audio/gunready.wav"
    tali "What the hell are those things!? Get back! I'll open fire!"
    show tali gunshoot at left
    play sound "audio/gunshot.mp3"
    pause 1
    play sound "audio/gunshot.mp3"
    tali "I've warned you!"

    scene black
    with dis
    pause 1
    play sound "audio/gunshot.mp3"
    pause 1
    play sound "audio/gunshot.mp3"
    pause .5
    play sound "audio/gunshot.mp3"
    pause .5
    play sound "audio/gunshot.mp3"
    pause .5
    play sound "audio/gunshot.mp3"

    tali "Back!"
    pause 1
    show tali gunstand
    tali "Damnit, there's too many of them! I've got to get out of here fast!"

    scene bg start6
    with dis
    pause .5
    play sound "audio/gunshot.mp3"
    pause 1
    play sound "audio/gunshot.mp3"
    tali "There should be a utility tunnel nearby! I need to hurry!"
    scene bg start7
    play sound "audio/explosion.mp3"
    "No sooner had Tali reached the tunnel before a huge explosion completely destroyed the bay she had just escaped from. Debris flew into the vacuum of space and the shift in pressure locked the wing from further travel."
    scene bg doorcatch1
    show tali guninjured at left
    with dis
    tali "K-Keelah. That was close."
    show tali angry at left
    with dis
    tali "N... now I... huh? Locked? Just my luck. Like I have time for this!"
    show tali tool at left
    with dis
    tali "Calm down Tali. Its not going to plan but you've gotten out of worse. Lets open this. Afterwards I just need to find the communication center and amplify a distress beacon. There should be patrols... I hope."
    show creep stand at right
    with dis
    play sound "audio/creepone.mp3"
    creature "KUAAAAHHRR!"
    show tali gunstand at left
    tali "What the! Where did you come from?!"
    show tali gunshoot at left
    tali "Keelah, I don't have time for this! I'll make this quick!"
    pause 2
    play sound "audio/gunready.wav"
    pause .5
    play sound "audio/gunready.wav"
    pause .5
    play sound "audio/gunready.wav"
    pause .5
    play sound "audio/gunready.wav"
    tali "Huh? Empty? Now?! I must have unloaded the whole clip!"
    show tali tool at left
    tali "I have to open this door FAST! F-Focus Tali, ignore the creature and focus! If I'm fast enough he'll-"
    show creep horny at right
    play sound "audio/creepone.mp3"
    creature "HAUK! GRRRAAAAHHHHH!"
    scene bg doorcatch2 with hpunch
    play sound "audio/punch.mp3"
    tali "Get off of me you filthy animal! D-Don't - h-huh? Is that your tongue?! S-Stop licking me!"
    scene bg doorcatch3
    play sound "audio/lick.mp3"
    pause 1
    play sound "audio/lick.mp3"
    creature "Grrrrrrrrrr..."
    scene bg doorcatch4 with hpunch
    play sound "audio/punch.mp3"
    pause 2
    scene bg doorcatch5
    with dis
    tali "Come on you damn sheet of metal! OPEN! H-He's tearing into my suit!"
    scene bg doorcatch6
    play sound "audio/creepone.mp3"
    "Still trying to handle the door, Tali felt something thick and slimy poke her anus. Her back froze stiff as she knew exactly what it was."
    scene bg doorcatch7
    tali "No, no! What the hell are you - agh!"
    scene bg doorcatch8
    play sound "audio/creepone.mp3"
    creature "Grrraaaaaaaa!"
    scene bg doorcatch9
    play sound "audio/lewdclaps.mp3"
    pause .5
    scene bg doorcatch8
    pause .5
    scene bg doorcatch9
    pause .5
    scene bg doorcatch8
    pause .5
    scene bg doorcatch9
    pause .5
    scene bg doorcatch8
    pause .5
    scene bg doorcatch9
    tali "AGGHH!! His... his animal 'thing' is spreading me apart!"
    scene bg doorcatch10
    play sound "audio/lewdsplat.mp3"
    pause 2
    play sound "audio/lewdsplat.mp3"
    scene bg doorcatch11
    tali "H-Hahn? Did you... Keelah, did you just...?"
    scene bg doorcatch12
    play sound "audio/lewdclaps.mp3"
    tali "N-Not again! Please... let me go. Let me go you filthy, brainle- AGHHH!!"
    scene bg doorcatch13
    play sound "audio/lewdsplat.mp3"
    pause 1
    play sound "audio/lewdsplat.mp3"
    pause 1
    play sound "audio/lewdsplat.mp3"
    pause 2
    play sound "audio/lewdsplat.mp3"
    pause 2
    scene bg doorcatch14
    play sound "audio/lewsquish.mp3"
    pause 5

    label test:
        scene bg doorcatch14
        play sound "audio/lewsquish.mp3"
        pause 5
        tali "{i}M-My... ass. He put that thick, hot rod inside my... K-Keelah. This can't be happening...{/i}"
        scene black
        with Dissolve(5)
        "Tali completely lost the strength and will to resist. She felt her body start to react to the stale air and foreign bacteria around and in her body."
        "Before passing out she heard the familiar beep of her suit auto-enabling antibiotics and deep repair protocols. Head head struck the floor soon after."

    unknow "There she is. Finally! Krax, Jic, grab her and lets get out of here!"
    scene black with hpunch
    play sound "audio/creepone.mp3"
    creature "Graaaahhggg!!!"
    unknow "Kill that pest!"
    play sound "audio/gunshot.mp3"
    pause .5
    play sound "audio/heavyshots.mp3"
    pause 2
    play sound "audio/gunshot.mp3"
    pause 1
    play sound "audio/heavyshots.mp3"
    pause 2
    unknow "She still has a pulse. Good. Bring her to the medical bay."

    scene bg med1
    with dis
    play sound "audio/funmoan.mp3"
    pause 2
    scene bg med2 with hpunch
    play sound "audio/punch.mp3"
    tali "Get your hands away from me!"
    scene bg med3
    with dis
    show tali gunshoot at left
    play sound "audio/gunready.wav"
    tali "Get back or I'll blast your head clean off your shoulders!"
    scene bg med3
    show tali gunshoot at left
    show serok stand at right
    serok "Who was that? Who are you? What was that... thing?! Answer fast, I am not in the mood!"
    show serok smoke at right
    tali "Who the damn you are? Answer fast, i am not in the mood if you haven't noticed yet."
    show serok stand at right
    serok "First: Not at all polite to the crew that just saved you. Second: We both know you don't have ammo."
    show tali guninjured
    tali "That's... I... F-Fine. Keelah I can still... that creatures... what happened?"
    show serok stand at right
    serok "We found you being used up by the local wildlife. Luckily your suit can auto-apply medi-gel and antibiotics. Damned thing can even repair itself. It holds up nicely. Not sure about your pride though."
    show tali shame at left
    tali "Y-You saw... lets just forget anything ever happened."
    show serok reason at right
    serok "Cameras say otherwise, but you're alive right? Pity half my crew can't say the same. If they were all women I'm sure I'd at least be able to find them. Hell, I wouldn't even have left the port back in Dakar!"
    show tali doubt at left
    tali "Could you change the topic please? So who are you? What are you doing here?"
    show serok talk at right
    serok "Head in the game. I like that. The names Serok. My men and I are honest merchants. Don't let the Alliance or their claims of 'unlawful salvaging' tell you otherwise."
    show serok reason at right
    serok "My ship was hit hard when I was spontaneously attacked by some biased captain. We docked for repairs. Unfortunately the locals weren't open for business... but they were hungry. For flesh and... well, you know."
    show serok smoke at right
    tali "Right. Merchants? Sounds to me like you're cut and dry Terminus pirates that smuggle, steal and salvage whatever they can."
    show serok stand at right
    serok "Says who? The quarian? Really? You must be trying to make me laugh. I bet you came here thinking you were gonna walk away with something big and valuable right? Something to take back home?"
    show serok smoke at right
    show tali angry at left
    tali "We don't steal, we only smuggle the essentials and we never threaten anyone over who can claim a hunk of scrap, you bosh'tet!"
    show serok stand at right
    show tali doubt at left
    serok "Hey, suitrat. You just wanted to shoot my men's heads clean off their shoulders, remember?"
    show tali talk at left
    tali "I just wanted... it was just... i-it doesn't matter! I'm tired of this meaningless talk! I have to find the communications station on this ship."
    show serok talk at right
    show tali doubt at left
    serok "You can't. We tried already. Lost most of my crew on the way there. Found only charred metal pieces and junk. No way it'll work. You can check for yourself... if you get there."
    show tali shame at left
    show serok smoke at right
    tali "Ugh! There has to be a way off of this thing..."
    show serok talk at right
    serok "There is. My ship. Its docked on the other end of this vessel. We could help each other. Just go and check whats wrong with it."
    show serok smoke at right
    show tali doubt at left
    tali "What? Don't any of your men know how to patch up a ship?"
    show serok stand at right
    serok "Look at them."
    scene bg med3
    show tali doubt at left
    show vor1 stand at right behind serok
    show vor2 stand behind serok, vor1
    play sound "audio/funmoan.mp3"
    pause 3
    scene bg med3
    show tali doubt at left
    show serok reason at right
    serok "Need I say more? I lost most of my crew, as I said. Unfortunately that included the chief mechanic."
    tali "So you expect me to help? Oh that's rich. Why would I help you?"
    show serok stand at right
    serok "Because that pain in your ass will only get worse, heh-heh. My ship is our only ticket off this rock. You want a seat? Patch her up."
    show serok reason at right
    serok "I'm being reasonable AND generous. Its my gift as a merchant. You quarians are good with tech and ships, aren't you? And what do you know, I happen to have bullets and explosives."
    show serok talk at right
    serok "Fix my ride and you'll have aseat. In the mean time you can look for parts. Trade them in for ammo or explosives to help you on your way. I have to recover my losses somehow. What do you say?"
    show serok smoke at right
    show tali talk at left
    menu firstHelp:
        "Seems I don't have much of a choice." :
            tali "Fine. But no tricks! I'll be watching you..."
            show serok stand at right
            serok "Tricks? Me? I wouldn't dream of it. I just want to get the hell out of here as much as you. But enough talk, lets go see my ship."
            scene black
            play sound "audio/walk.mp3"
            "Hesitantly, Tali follows Serok to docking bay..."
            pause 2
            jump firstChoiceYES
        "Hell no!" :
            $ firstHelpChoice = False
            $ quest = "Check the comroom"
            tali "As if! I'll take my chances with the communications station over a deal with a pirate!"
            show serok stand
            serok "Oh? Yeah, sure. Up to you suitrat. Assuming you learn your lesson after getting that pretty face of yours covered in some beasts cum, you know where to find me. I'll be waiting."
            show tali doubt at left
            show serok smoke at right
            serok "Alright boys, we're leaving. Grab your gear and head back to the ship. Try not to lose whats left of our stuff, ey?"
            scene black
            play sound "audio/walk.mp3"
            "After picking up their equipment Serok and his men leave, though not before passing glances at the defensive quarian."
            pause 2
            $ firstHelpChoice = False
            jump firstChoiceNO

    label firstChoiceNO :
        scene bg med3
        show tali tool at left
        tali "Alright, lets see what we have here. Fully operational medical equipment? I could easily reconfigure it for quarian anatomy."
        tali "Looks like I can use the rejuvination capsules for suit repair and medical assistance. O-Oh! And these antibiotics are top-shelf! I should be safe in the event of prolonged suit damage!"
        show tali shame at left
        tali "Did they have quarians here? Huh. Very... strange. This is some very advanced inventory for a drifting hunk of junk. What was this ship used for?"
        show tali doubt at left
        tali "Alright, I can spend some time taking a look around. But after that, I need to head to check on communications."
        $ quest = "Check the communication room."
        jump define_loot

    label firstChoiceYES:
        scene bg hangar
        show tali doubt at left
        with dis
        show serok smoke at right
        with dis
        tali "That is NOT a merchant ship."
        show serok stand at right
        serok "Well, yeah, you're right. But it's our escape off this ship. Remember whats important."
        show tali talk at left
        tali "Just tell your thugs not to get in my way."
        show serok reason at right
        show tali doubt at left
        serok "Deal. Welcome to the crew! No unions, no steady pay, but Serok will treat you well. Now go and see whats keeping this bird grounded huh?"
        show serok talk at right
        serok "Oh, and look for Jesora. My second officer. She's somewhere on my beauty. Asari, you can't miss her. I'd hoped she was here to introduce you, but I guess you'll meet her on your own. Good luck."
        scene black
        with dis
        play sound "audio/walk.mp3"
        pause 2
        scene bg shipinside
        show tali tool at left
        with dis
        tali "Lets see... Thermal Stabilizers damaged. Heating panels fried. Engines uncalibrated. Keelah, if they launch the engines on full power this ship becomes a spaceborne oven in an instant."
        show tali shame at left
        tali "I'll have to find parts or jury rig a a solution. Maybe in the engine room? The cargo bay would be best for scrap..."
        show tali tool at left
        tali "Navigations are fried as well. I can fix the computer with spare parts."
        play sound "audio/femalemoan.mp3"
        pause 1
        show tali gunstand at left
        tali "What was that?!"
        play sound "audio/funmoan.mp3"
        pause 1
        tali "Sounds like its coming from the adjacent room..."
        menu shipChoice:
            "Investigate (Futa Content)":
                jump shipInsideScene
            "Better return to Serok" :
                $ shipInsideChoice = False
                jump jesoraMeet

    label shipInsideScene:
        $ lewd += 1
        scene bg shipscene0
        tali "... what the hell?"
        play sound "audio/lewdclaps.mp3"
        scene bg shipscene1
        "Mmmmph! Fuck me harder you waste-scrounging vorcha bastards!"
        scene bg shipscene2
        play sound "audio/funmoan.mp3"
        pause 1
        play sound "audio/lewdclaps.mp3"
        pause 1
        scene bg shipscene0
        tali "I, uhm... I think I found Serok's second officer."
        scene bg shipscene3
        jesora "Ughhmmmmmpppppphh..."
        scene bg shipscene4
        "Tali slowly begins to touch herself. Her breathing grows steadily as her fingers rub at her sensitive nerves, rubbing soothing circles through the thin layers of her suit."
        tali "Keelah thats... so... filthy. I-I... Oh Keelah, I hope they wont notice me..."
        scene bg shipscenebg
        show asari_anim1
        $ renpy.pause ()
        scene bg shipscene5
        play sound "audio/lewdsplat.mp3"
        pause 4
        scene bg shipscene6
        play sound "audio/lewsquish.mp3"
        tali "They came so much inside of her... and she's cumming on the floor without any shame. Oh Keelah, they're..."
        scene bg shipscene4
        tali "I-I need to get back to Serok. Before this gets too weird..."
        jump jesoraMeet

    label jesoraMeet:
        scene bg hangar
        with dis
        show tali shame at left
        with dis
        show serok stand at right
        with dis
        serok "Well? Tell me the good news, quarian."
        tali "O-OH! Well, uh... yes. Well, I found the issue. Well, issues. But It won't be an easy fix. Maybe if we..."
        show jesora doubt behind serok
        with dis
        show serok talk at right
        serok "Jesora! Finally. You took your sweet time? What exactly were you up to? Scratch that, doesn't matter. Let me introduce you to our new chief engineer. This quarian will help us to repair the ship."
        show serok stand at right
        serok "Suitgirl, this is Jesora - former asari commando and my second officer. She'll help you with everything that goes bang and boom. Have fun ladies. Now then, I need a drink."
        scene bg hangar
        if shipInsideChoice == False:
            jump jesoraFirstTalk1
        else:
            jump jesoraFirstTalk2

    label taliNoChoice:
        scene bg hangar
        with dis
        show tali shame at left
        with dis
        show serok stand at right
        with dis
        serok "I see you finally listened to the voice of reason."
        tali "Will you stop... looks, right, lets just get this over with."
        show serok stand at right
        show tali doubt at left
        serok "Hmmph. Well, while you were running around fixing scrap, my second officer Jesora diagnosed my ships issues. You can check the results and find what we'll need."
        show serok talk at right
        serok "Here, take it."
        show tali tool at left
        show serok smoke at right
        tali "Alright, lets see... Thermal Stabilizers damaged. Heating panels fried. Engines uncalibrated. Keelah, if they launch the engines on full power this ship becomes a spaceborne oven in an instant."
        tali "I'll have to find parts or jury rig a a solution. Maybe in the engine room? The cargo bay would be best for scrap..."
        tali "Navigations are fried as well. I can fix the computer with spare parts."
        show jesora doubt behind serok
        with dis
        show serok talk at right
        serok "Jesora! Finally. You took your sweet time? What exactly were you up to? Scratch that, doesn't matter. Let me introduce you to our new chief engineer. This quarian will help us to repair the ship."
        show serok stand at right
        serok "Suitgirl, this is Jesora - former asari commando and my second officer. She'll help you with everything that goes bang and boom. Have fun ladies. Now then, I need a drink."
        scene bg hangar
        $ comEncounter = False
        jump jesoraFirstTalk1

    label jesoraFirstTalk1:
        show tali talk at left
        with dis
        show jesora doubt at right
        with dis
        tali "Nice to meet you. I am Tali, my ship was sabotaged and i am stuck here."
        jump jesoraFirstTalk
    label jesoraFirstTalk2:
        show tali talk at left
        with dis
        show jesora doubt at right
        with dis
        tali "Uh. H-Hello again..."
        show jesora stand at right
        jesora "Again? What you mean by that?"
        show tali shame at left
        tali "No! No, I mean... I have some asari friends and... well, I confused you for someone different who... looks like you..."
        tali "J-Just forget it, ok?"
        jump jesoraFirstTalk
    label jesoraFirstTalk:
        show tali doubt at left
        show jesora stand at right
        jesora "Huh. I see. Well we're all on the same boat here, right? You help us, we help you."
        show jesora talk at right
        jesora "We can arrange an exchange here. Bring me any tech parts you find and I'll exchange it for its value in ammo and explosions."
        show tali tool at left
        tali "Wait, I have credits. I could just pay you. Do you have any shotguns or smg's? I could really use the extra firepo-"
        show jesora stand at right
        jesora "Look around, girl. Do it really look like we need money right now? We need tech, not credits. Bring us tech, get ammo."
        show tali angry at left
        tali "Why do YOU need tech is Serok is sending ME to fix everything?!"
        jesora "Our ship barely escaped a fight with an alliance patrol. We have a myriad of issues all over the hull. That can be fixed with the parts you bring us."
        show jesora doubt at right
        show tali doubt at left
        jesora "We can't handle critical system issues. You can. That's the only reason you're here and Serok didn't OK you being some chained up crew relief in the hold."
        show tali angry at left
        tali "That's... Just give me some guns! There's plenty of beasts on this ship! How do you expect me to defend myself?!"
        show tali doubt at left
        show jesora stand at right
        jesora "You HAVE a gun, right? We need ours to defend whats left of our ship. We don't want or need to run around shooting everyone. Just stay silent, hide, and shoot if necessary. Preferably discretely."
        show jesora think at right
        jesora "What we CAN do for you is dismount one of our canons from the ship and rig it up as makeshift sentry turret to protect the medical bay where you'll be residing. Who knows, maybe we'll need it too."
        show tali talk at left
        tali "That's... ugh. Well it's something. At least I can rest easy..."
        show jesora stand at right
        jesora "You're welcome. So, you know what the issues with the ship are?"
        tali "Y-Yes. There are some other issues but the glaring ones are your thermal stabilizers and the navigation system."
        jesora "Navigation huh? Good. Knowing the specifics makes searching less inconvenient. Seroks vorchas didn't find anything, but its hard for them to bring back anything that isn't shiny."
        jesora "Take this."
        scene black
        show doorexp:
            xalign 1.2
            yalign 0.5
        show doorexp with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "Tali take door breaching charge."
        $ doorexp += 1
        show doorexp with move:
            xalign -0.2
            yalign 0.5
        scene bg hangar
        show tali doubt at left
        show jesora stand at right
        jesora "That'll help you blast through any doors too stubborn to hack, or are just flat out annoying. But thats enough talk. Lets go set up your sentry. I'll get the boys on it."
        scene black with dis
        scene bg turret1
        with dis
        jesora "Stop fiddling with the switches you idiot. Just make sure its ON. Yes, like this. Now let me check."
        scene bg turret2
        with dis
        jesora "Serok? Its done. We'll be back soon. All quiet? Affirmitive. Alright, got it."
        show bg turret3
        with dis
        show tali doubt at left
        show jesora stand at right
        with dis
        jesora "Alright girl, we're done here. The turret has enough ammo to resist a small siege. I'll ask the boys to patrol the halls from time to time, just in case."
        show tali talk at left
        tali "Very generous coming from a pirate crew. Thank you. I'll rest for a moment before getting to work."
        jesora "Take your time. If you have any questions, Serok and I will be in the docking bay. But the sooner you find what we need, the faster we can get off this hellhole."
        show jesora talk at right
        jesora "Here's some ammo on the house. Don't use it all on one trip."
        scene black
        show clips:
            xalign 1.2
            yalign 0.5
        show clips with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "10 thermal clips."
        $ ammo += 10
        show clips with move:
            xalign -0.2
            yalign 0.5
        show bg turret3
        show tali doubt at left
        show jesora talk at right
        jesora "Careful now. And good luck."
        $ bay2 = True
        if comEncounter == True:
            jump firstChoiceNO
        else:
            $ firstHelpChoice = True
            $ engine = True
            $ warehouse = True
            $ barracks = True
            $ quest = "Search for tech parts."
            jump MedBayUsual

    label comroom_enter:
        if firstTimeRoom:
            jump comroomtutorial
        else:
            jump comroom

    label medbayafterdefeat :
        $ hackstep = 3
        $ hackNumber = 3
        $ hackID = 0
        $ infection = 0
        $ suitdur = 100
        $ days += 1
        scene black
        with dis
        "Recovery sequence activated."
        scene bg med4
        show tali shame at left
        with dis
        tali "Need to be more careful next time..."
        jump define_loot

    label MedBayUsual :
        if twoHount:
            jump doubleEnc
        hide screen medStats
        scene bg med4
        show tali tool at left
        menu MedBay:
            "Check status" :
                scene bg medscreen
                show screen medStats
                if firstTimeScan:
                    jump statusCheck
                else:
                    "Full scan complete. Results on screen."
            "Rest" if firstTimeScan == False:
                $ havedogbone = True
                $ comCum = False
                $ prisCum = False
                $ infection = 0
                $ suitdur = 100
                $ days += 1
                scene bg medrest
                "Recovery sequence activated."
                tali "Time to rest a bit."
                scene black
                with Dissolve(3)
                if crewCount > 1:
                    $ crewCount = 0
                    jump jesoraCall
                if crewQuest:
                    jump secureDoorRandom
                elif act3:
                    jump secureDoorRandom
                else:
                    if jesora1 == False:
                        if partsQuest and days > 12:
                            if whDoor == False and barracksDoor == False:
                                $ jesora1 = True
                                jump hackQuest

                jump define_loot
            "Take shower" if comEncounter == False:
                $ infection = 0
                scene bg shower1
                with dis
                play sound "audio/shower.mp3"
                tali "Nice."
                scene bg shower2
                with dis
                "........"
            "Go out" if firstTimeScan == False:
                if firstMap:
                    jump maptutorial
                else:
                    jump map
        jump MedBayUsual

    label doubleEnc:
        $ twoHount = False
        scene bg g1
        tali "Can't wait to take a shower... What the..."
        scene bg g2 with hpunch
        play sound "audio/punch.mp3"
        tali "Oh spirits, this is monkey-beast from prison."
        play sound "audio/roar.mp3"
        tali "He is pretty close to my hideout. Hope he don't find the way. What i gonna do now?"
        menu doublechoice:
            "Attack.":
                show bg g3
                play sound "audio/creepone.mp3"
                tali "Remember me?"
                tali "And what about your friend? I guess he is smarter and decide not to go with you."
                scene bg g4
                play sound "audio/creepmany.wav"
                pause 1
                scene bg g5
                tali "Oh, com on Tali, you should have expect this."
                scene bg g8
                $ enemyID = 30
                jump sliderBoss
            "Run.":
                "Gotta go before it gets worse."
                scene black
                play sound "audio/run.ogg"
                pause 2
                jump map

    label double_event1:
        scene black
        $ lewd += 1
        play sound "audio/creepone.mp3"
        pause 2
        play sound "audio/tier.mp3"
        pause 2
        scene bg g9
        tali "Ugh, your mouth smell is disgusting..."
        scene bg g7
        show double_loop1
        $ renpy.pause ()
        scene bg g6
        play sound "audio/gorillaroar.wav"
        tali "Oh keelah, can you just go back to your damn cage!?"
        scene bg g7
        show double_trans1
        pause 4
        tali "It hurts, it hurts! No! Stop, please..."
        scene bg g7
        show double_trans2
        tali "Ah... it even bigger than i thought..."
        scene bg g7
        show double_loop2
        $ renpy.pause ()
        scene bg g7
        show double_cum
        $ renpy.pause ()
        scene bg g8
        show tali fin1 at left
        with dis
        tali "Oh spirits, at least they let me go... Medbay must be close..."
        jump medbayafterdefeat


    label jesoraCall:
        scene bg med3
        show tali tool at left
        with dis
        play sound "audio/message.mp3"
        tali "I got a message but there's a lot of interference."
        play sound "audio/noise.ogg"
        jesora ".............................."
        tali "I need to try and amplify the signal."
        play sound "audio/noise.ogg"
        pause 2
        jesora "... hear me?.... hello?"
        tali "Its Jesora!"
        jesora "help... the hallway near the communication..."
        tali "Signal lost? But she managed to send me her coordinates."
        show tali gunstand at left
        tali "I need to hurry."
        $ hallway = True
        jump secureDoorRandom

    label hackQuest:
        scene bg med3
        show tali tool at left
        with dis
        play sound "audio/message.mp3"
        jesora "Hello? Quarian, do you copy?"
        tali "Jesora? Oh spirits, you fixed communications! Now we can call for help!"
        jesora "No such hopes, quarian. We found a shortwave transmitter and the boys kicked it enough to make it work. Come meet me in hangar bay, we need to talk."
        tali "Oh... I'm on my way."
        scene black
        play sound "audio/walk.mp3"
        pause 2
        scene bg hangar
        with dis
        show tali talk at left
        show jesora stand at right
        tali "What happened?"
        show jesora talk at right
        jesora "First take this, this is a module for you omni-tool with decrypting protocols. It will let you hack almost anything you want."
        play sound "audio/equip.ogg"
        show tali tool at left
        show jesora stand at right
        tali "Finally! I'll set it up quickly, thanks."
        show jesora talk at right
        jesora "Look, we need to fix the navigation system, right? I have an idea where you can find the parts to fix it."
        show tali doubt at left
        tali "What do you have in mind?"
        show jesora talk at right
        jesora "You need to go check on your ships remains on the other docking bay. Some equipment may still salvageable."
        show jesora doubt at right
        show tali angry at left
        tali "You cant be serious? Even if there was something left, that sector was depressurized after the explosion."
        show tali doubt at left
        show jesora talk at right
        jesora "We thought so too, but the ships automated repair seemed to fix enough to patch up the damage. I scaned the area and found it safe."
        show jesora warry at right
        jesora "Serok already sent some of his boys, but they ran into a sealed bulkhead."
        show tali talk at left
        tali "Why not just blow it up? You should have plenty of charges."
        show jesora stand at right
        show tali doubt at left
        jesora "I don't think using an explosive on an already damaged docking sleeve is a good idea. Thats why we need you and your new hacking device down there."
        show tali talk at left
        tali "Alright, sounds like a plan. I'll take a look."
        $ quest = "Go to docking bay #1"
        $ hackOK = True
        $ barracksTablet = False
        $ bay1 = True
        jump jesoratalkmenu

    label hackQuestComplete:
        $ barracksTablet = True
        $ crewQuest = True
        if prisonLock == False:
            $ prisoncage = False
            $ prisoncage1 = True
        $ quest = "Find Jesora and her crew."
        scene bg hangar
        show serok stand at right
        show tali angry at left
        with dis
        tali "Serok! I did it! Navigation systems are operational!"
        show tali doubt at left
        show serok think at right
        serok "Glad to see you in one piece, quarian. Thats great but we have other problems."
        show serok smoke at right
        show tali talk at left
        tali "Huh? Where's Jesora?"
        show serok stand at right
        show tali doubt at left
        serok "She went with some my men to patrol after you. As you know, security doors suddenly began to shut everywhere after the alarm."
        show serok talk at right
        serok "So now they're stuck somewhere on this ship and the creatures are going crazy. Very crazy. Our defenses keep activating and they keep attacking."
        show serok smoke at right
        show tali talk at left
        tali "Where could Jesora be now?"
        show serok stand at right
        show tali doubt at left
        serok "No idea. I lost contact with them after this mess started. Since you're so special and can still walk just fine, do me a favor and look for my men, ey?"
        show serok smoke at right
        tali "Another favor? You're asking a bit much don't you think?"
        show serok reason at right
        serok "Without my crew I this ship will eat us alive. I'm sure you can understand that."
        show tali talk at left
        show serok smoke at right
        tali "Ugh. What about supplies?"
        show serok talk at right
        serok "Hmph. Here, take it. Use it wisely. I'll use the rest to protect whats left of my boys. Whats left of them anyway."
        "Serok gives Tali 10 ammo and 1 grenade."
        $ ammo += 10
        $ grenades += 1
        show tali doubt at left
        show serok stand at right
        serok "Find my crew, quarian. And I will help you with the rest."
        scene black
        with dis
        play sound "audio/walk.mp3"
        "Tali returns to the medbay."
        scene bg med3
        show tali tool at left
        with dis
        tali "Serok was right. Emergency security gates are closing everywhere."
        show tali shame at left
        tali "Looks like I'll have my work cut out for me."
        show tali doubt at left
        "Security doors are shut in most locations, blocking almost every route. Redundant systems will repair and replace hacked or destroyed doors after a day of rest."
        "Tali will encounter security doors at random in most directions and will stay there until Tali hacks or destoys them."
        $ comDoor = True
        $ engDoor = True
        $ bayDoor = True
        $ whDoor = True
        $ barracksDoor = True
        $ vorchaCrew = True
        $ asariCrew = True
        $ prisonloot4 = True
        jump define_loot

    label crewQuestComplete:
        $ quest = "Have fun."
        $ crewQuest = False
        $ act3 = True
        $ barrackskey = True
        scene bg hangar
        show serok stand at right
        show tali talk at left
        with dis
        tali "I found Jesora! She's safe!"
        show jesora smiletalk behind serok
        jesora "Our quarian girl surprises us again. Having you on the team's really turned our luck around."
        show tali doubt at left
        tali "H-Hold on, I am not a part of your team. We had an agreement, got it?"
        show jesora smile behind serok
        jesora "Relaaax, just teasing you. Thanks for the help anyway. Now I need to rest, take a shower and have some drinks."
        show tali angry at left
        tali "Hey, hold it! First you tell me why your own team wants to kill you!"
        show tali doubt at left
        show jesora talk behind serok
        jesora "Serok, give me a hand? I'll see you later guys, its been a long day."
        scene bg hangar
        show tali doubt at left
        show serok talk at right
        serok "Hmph. I guess telling you wouldn't hurt. Might even help."
        show serok smoke at right
        tali "Good. Start talking."
        show serok think at right
        serok "Not just a nice ass, are you? Well we figured we could get out of this rich quick and headed over to the bridge. We found some very weird shit on the way there."
        show serok talk at right
        serok "We tried to find a drone or something to fix up the ship. Instead we found rooms and even labs full of those creatures, swarming and reckless."
        show serok think at right
        serok "It was a massacre. I lost a lot of guys. Too many. The scrap we picked up along the way wasn't worth that kind of loss. To boot, I got stabbed in the back by a couple of ingrates."
        serok "Gral, my second officer. He took half my crew and left for the other front of the ship."
        show serok talk at right
        serok "Let him die, what do I care? But as a last laugh he took the thermal stabilizers. What an asshole."
        show serok smoke at right
        show tali talk at left
        tali "I'm a businessman, not a politician. We all make mistakes."
        show serok stand at right
        serok "You're no exception, packaged tits. Should I remind you how we first met?"
        show tali shame at left
        show serok reason at right
        serok "Gral blamed me for everything and now they're hiding somewhere beyond those shitty labs. If they want to get mauled by those things, no sweat off my back. I won't negotiate or send my crew that way."
        show serok smoke at right
        show tali doubt at left
        tali "Wait, so you knew about the stabilizers from the start? Great. And we're stuck here because of some disagreement that you don't want to man up about."
        show serok stand at right
        serok "I guess so. You looking for an apology suitgirl? You're barking up the wrong tree."
        show serok think at right
        serok "Jesora and I will figure out how to go from here. Hatch a plan and get back to you. Get some rest, you'll need it. We'll call you later."
        serok "And take this. Jesora found it in last patrol."
        scene black
        show keycard1:
            xalign 1.2
            yalign 0.5
        show keycard1 with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "Tali gets the keycard."
        show keycard1 with move:
            xalign -0.2
            yalign 0.5
        scene bg hangar
        show serok stand at right
        show tali doubt at left
        serok "Have no idea what this key card opens but you find out, i am sure."
        scene black
        play sound "audio/walk.mp3"
        "Tali returns to the medbay"
        scene bg med3
        show tali tool at left
        "THE MAIN STORY ENDS HERE. THANKS FOR PLAYING! HOPE YOU ENJOYED IT. YOU CAN CONTINUE TO PLAY TO UNCOVER MORE MORE SCENES!"
        jump define_loot


    label statusCheck:
        "Here you can check on Tali's status and her inventory. Most of these stats will be shown on the upper-left corner of the map screen."
        "Be wary of Infection. Infection will rise with each consecutive defeat up to a maximum of '3'. Once Tali reaches max Infection, she will automatically return to the med bay for healing."
        "The more Tali loses, the higher her Lewd Level becomes. Additional events and dialogue options will unlock the more corrupt Tali's mind becomes."
        "Use ammo and grenades to defeat annoying enemies. Door explosives will clear the way through blocked areas, but take noise will Alarm the locals and increase encounter chance. Alarm level can not be reduced for now."
        "You can always refresh Tali's stats or pass the day by choosing to rest. This will refresh both events and loot in room."
        $ firstTimeScan = False
        jump MedBayUsual

    screen medStats:
        text "Stamina: [suitdur]" xpos 0.23 ypos 0.2
        text "Ammo: [ammo]" xpos 0.23 ypos 0.25
        text "Grenades: [grenades]" xpos 0.23 ypos 0.3
        text "Breaching charges: [doorexp]" xpos 0.23 ypos 0.35
        text "Tech parts: [parts]" xpos 0.23 ypos 0.4
        text "Alarm level: [alarm]" xpos 0.23 ypos 0.45
        text "Lewd level: [lewd]" xpos 0.23 ypos 0.50
        text "Infection: [infection]" xpos 0.23 ypos 0.55
        text "Current quest:" xpos 0.55 ypos 0.2
        text "[quest]" xpos 0.50 ypos 0.3

    label comroomtutorial:
        scene bg comroom
        show tali tool at left
        with dis
        tali "Ngh. The computers are totally trashed. Serok was right, there's no way I can use these."
        show tali shame at left
        tali "No time to waste I guess. I need to check for anything useful I can find."
        show image "images/map/backbutton_idle.png" at right
        show tali back at left
        with dis
        "Every time Tali enters a room, you can search for clickable objects around. Loot and misc items are scattered. You can go back to the map with the bottom-right arrow button."
        scene bg comtutorial1
        show tali back at left
        "Loot is randomly generated and may look different or be in different locatoins every time you visit. Keep those eyes open!"
        scene bg comtutorial2
        show tali back at left
        "This is how it looks when you hover the cursor over such an object. Inside you can find valuable items like ammo or quest items like tech parts. These will be added to your inventory."
        "Common loot is random. Some events may also be triggered depending on Tali's Lewd Level."
        $ firstTimeRoom = False
        jump comroom

    label comroom:
        $ roomID = 1
        if comDoor:
            jump secureDoor
        scene bg comroom
        show tali back at left
        call screen comroom_items



    screen comroom_items():
        modal True
        showif encounter:
            imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump("com_biggy")
        else:
            imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump ("comRoomEncounter")

        showif comroom_crate1:
            imagebutton:
                idle "images/events/comroom/crate1_idle.png"
                hover "images/events/comroom/crate1_hover.png"
                focus_mask True
                action [SetVariable("comroom_crate1", False), Jump ("crate")]

        showif comroom_crate2:
            imagebutton:
                idle "images/events/comroom/crate2_idle.png"
                hover "images/events/comroom/crate2_hover.png"
                focus_mask True
                action [SetVariable("comroom_crate2", False), Jump ("crate")]

        showif comroom_barrel:
            imagebutton:
                idle "images/events/comroom/barrel1_idle.png"
                hover "images/events/comroom/barrel1_hover.png"
                focus_mask True
                action [SetVariable("comroom_barrel", False), Jump ("crate")]

    label crate:
        scene black
        $ random = renpy.random.randint(1, 100)
        if random > 1 and random < 40:
            $ random = renpy.random.randint(1, 3)
            show clips:
                xalign 1.2
                yalign 0.5
            show clips with move:
                xalign 0.5
                yalign 0.5
            play sound "audio/gunready.wav"
            "[random] thermal clips is found"
            $ ammo += random
            show clips with move:
                xalign -0.2
                yalign 0.5
        elif random > 39 and random < 95:
            $ random = renpy.random.randint(1, 3)
            show parts:
                xalign 1.2
                yalign 0.5
            show parts with move:
                xalign 0.5
                yalign 0.5
            play sound "audio/gunready.wav"
            "[random] tech part is found"
            $ parts += random
            show parts with move:
                xalign -0.2
                yalign 0.5
        elif random > 94 and random < 100:
            show gren:
                xalign 1.2
                yalign 0.5
            show gren with move:
                xalign 0.5
                yalign 0.5
            play sound "audio/gunready.wav"
            "Grenade is found"
            $ grenades += 1
            show gren with move:
                xalign -0.2
                yalign 0.5
        if roomID == 1:
            jump comroom
        elif roomID == 2:
            jump warehouse
        elif roomID == 3:
            jump engine
        elif roomID == 6:
            jump barracks
        elif roomID == 7:
            jump bay1_enter
        elif roomID == 8:
            jump prison
        elif roomID == 9:
            jump utilityroom

    label maptutorial:
        $ firstMap = False
        scene bg map tutorial
        "This is the general map of the ship you need to explore. In the upper-left corner you can see a list of character info and location tiles you can select."
        "During exploration there may be new locations you can uncover. Use door explosives to open security doors or try to hack them with your omni-tool."
        jump map

    label map:
        call screen general_map



    screen general_map():
        modal True

        add "images/map/bg map1.png"
        text "Stamina: [suitdur]" xpos 0.02 ypos 0.13 size 20
        text "Ammo: [ammo]" xpos 0.02 ypos 0.18 size 20
        text "Grenades: [grenades]" xpos 0.02 ypos 0.23 size 20
        text "Breaching charges: [doorexp]" xpos 0.02 ypos 0.28 size 20
        text "Tech parts: [parts]" xpos 0.02 ypos 0.33 size 20
        text "Alarm level: [alarm]" xpos 0.02 ypos 0.38 size 20

        showif comroom:
            imagebutton:
                idle "images/map/comroom_idle.png"
                hover "images/map/comroom_hover.png"
                hovered Notify("    Communication room")
                focus_mask True
                action Jump("comroom_enter")
        showif bay1:
            imagebutton:
                idle "images/map/bay1_idle.png"
                hover "images/map/bay1_hover.png"
                hovered Notify("     Docking bay #1")
                focus_mask True
                action [SetVariable("roomID", 7), Jump ("bay1_enter")]
        showif bay2 and firstHelpChoice:
            imagebutton:
                idle "images/map/bay2_idle.png"
                hover "images/map/bay2_hover.png"
                hovered Notify("    Docking bay #2")
                focus_mask True
                action Jump ("bay2_enter")
        showif engine:
            imagebutton:
                idle "images/map/engine_idle.png"
                hover "images/map/engine_hover.png"
                hovered Notify("    Engine room")
                focus_mask True
                action [SetVariable("roomID", 4), Jump ("encounter_chance")]
        imagebutton:
            idle "images/map/med_idle.png"
            hover "images/map/med_hover.png"
            hovered Notify("    Medical bay")
            focus_mask True
            action Jump ("MedBayUsual")
        showif warehouse:
            imagebutton:
                idle "images/map/warehouse_idle.png"
                hover "images/map/warehouse_hover.png"
                hovered Notify("    Warehouse")
                focus_mask True
                action [SetVariable("roomID", 5), Jump ("encounter_chance")]
        showif barracks:
            imagebutton:
                idle "images/map/barracks_idle.png"
                hover "images/map/barracks_hover.png"
                hovered Notify("    Crew barracks")
                focus_mask True
                action [SetVariable("roomID", 6), Jump ("barracksEncounter")]
        showif prison:
            imagebutton:
                idle "images/map/prison_idle.png"
                hover "images/map/prison_hover.png"
                hovered Notify("    Prison")
                focus_mask True
                action Jump ("prisonFirst")

        showif hallway:
            imagebutton:
                idle "images/map/hallway_idle.png"
                hover "images/map/hallway_hover.png"
                hovered Notify("    Hallway")
                focus_mask True
                action Jump ("hallway")

    label hallwayFirst:
        scene bg hall
        play sound "audio/heavyshots.mp3"
        pause 1
        show tali gunstand at left
        with dis
        tali "Jesora! What the hell is going on here?!"
        show jesora gunshout at right
        jesora "Suitgirl, take cover!"
        play sound "audio/gunshot.mp3"
        show tali gunshoot at left
        tali "What the hell!"
        play sound "audio/heavyshots.mp3"
        scene bg hall1
        krogan "Fuck yeah! Take this, you maggots!"
        jesora "Fuck you, Gral! You'll pay for this!"
        scene bg hall2
        play sound "audio/metal door.ogg"
        krogan "Oh ho, ho! Funny! Tell that coward Serok I'll get to him eventually!"
        krogan "See you around, asari!"
        play sound "audio/metalshut.mp3"
        scene bg hall3
        pause 2
        show tali gunstand at left
        show jesora gunstand at right
        with dis
        jesora "Ugh. Good to you see. You came just in time."
        show jesora gunstand at right
        show tali angry at left
        tali "Who were those guys? Why were they shooting at you?"
        show tali doubt at left
        show jesora guntalk at right
        jesora "Long story. Short version is they're former crew. Ours. We got stuck together when the doors started closing. They don't play nice."
        show jesora gunstand at right
        show tali talk at left
        tali "I'd prefer the whole story."
        show jesora guntalk at right
        show tali doubt at left
        jesora "Sure. Lets just get the hell out of this place first."
        scene black
        play sound "audio/walk.mp3"
        "Tali and Jesora carefully trek back to the hangar bay."
        jump crewQuestComplete



    label hallway:
        if hallFirst:
            $ hallFirst = False
            jump hallwayFirst
        scene bg hall3
        show tali back at left
        tali "Nothing interesting here yet."
        call screen hallway_items

    screen hallway_items():
        modal True
        imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump ("map")


    label secureDoorRandom:
        $ random = renpy.random.randint(1, 100)
        if random < 51:
            $ comDoor = True
        $ random = renpy.random.randint(1, 100)
        if random < 51:
            $ engDoor = True
        $ random = renpy.random.randint(1, 100)
        if random < 51:
            $ bayDoor = True
        $ random = renpy.random.randint(1, 100)
        if random < 51:
            $ whDoor = True
        $ random = renpy.random.randint(1, 100)
        if random < 51:
            $ barracksDoor = True
        jump define_loot



    label secureDoor:
        scene bg securedoor1
        if secFirst:
            $ secFirst = False
            show tali tool at left
            with dis
            tali "Hmm... A security door? I should be able to hack it."
            play sound "audio/buzzerror.mp3"
            pause .5
            tali "What? Error? What the hell?!"
            show tali shame at left
            tali "Great. Looks like my omni-tool was damaged after that last incident. I don't have the parts I need to fix it right now. I need to talk with Jesora, I'm sure she can help."
            show tali doubt at left
            tali "I guess breaching charges are the way to go in the meantime."
        show tali back at left
        with dis
        menu secDoor:
            "Use breaching charge" if doorexp > 0:
                $ doorexp -= 1
                scene bg securedoor1
                show tali doorexp
                play sound "audio/equip.ogg"
                "Breaching charge set."
                scene bg securedoor1
                show tali doorstand
                play sound "audio/charge.mp3"
                tali "Its done, need to move away fast."
                show tali exp
                play sound "audio/run.ogg"
                pause 2
                scene bg securedoorblast
                with vpunch
                play sound "audio/explosion.mp3"
                $ alarm += 10
                pause 3
                show bg securedoor13
                show tali gunstand at left
                with dis
                tali "Time to go!"
                scene black
                play sound "audio/walk.mp3"
                "Tali continues on her way..."
                if roomID == 5:
                    $ whDoor = False
                    jump warehouse
                elif roomID == 2:
                    $ whDoor = False
                    jump warehouse
                elif roomID == 6:
                    $ barracksDoor = False
                    jump barracks
                elif roomID == 1:
                    $ comDoor = False
                    jump comroom
                elif roomID == 4:
                    $ engDoor = False
                    jump engine
                elif roomID == 7:
                    $ bayDoor = False
                    jump bay1_enter
            "Hack the door" if hackOK:
                $ hackID = 1
                jump sliderDoor
            "Not now.":
                jump map


    label barracksEncounter:
        if days > 5 and redVarrenFirstEnc:
            $ redVarrenFirstEnc = False
            jump redVarrenCorridor
        else:
            jump barracks

    label redVarrenCorridor:
        scene bg redvarren1
        with dis
        tali "Another gloomy corridor. And look, nothing useful. Again."
        play sound "audio/creepone.mp3"
        pause 2
        scene bg redvarren2
        with dis
        tali "Is that... a red varren? He looks so much bigger than the others! And even more dangerous!"
        scene bg redvarren3
        play sound "audio/gunshot.mp3"
        pause 1
        tali "Stop right there!"
        scene bg redvarren4
        with dis
        tali "Don't think you can trick me!"
        play sound "audio/creepone.mp3"
        tali "Where is he going?!"
        menu redVarren1:
            "Chase the red varren.":
                tali "No way to run!"
                scene black
                play sound "audio/creepone.mp3"
                creature "Arrrrrrr!"
                play sound "audio/gunshot.mp3"
                pause 1
                play sound "audio/gunshot.mp3"
                pause 1
                tali "Bosh'tet!"
                scene bg redvarren5
                with dis
                play sound "audio/walk.mp3"
                tali "I will catch you anyway!"
                play sound "audio/roar.mp3"
                pause 1
                play sound "audio/run.ogg"
                scene bg redvarren6
                with dis
                pause 1
                tali "What the hell? Where did he run off to?"
                tali "Keelah, where am I now? This part of the ship looks abandoned. And this strange door..."
                tali "That damned varren is probably hiding back there. Good. There's no room for him to sneak off."
                scene black
                play sound "audio/metal door.ogg"
                pause 2
                $ prison = True
                jump prisonFirst
            "Let him go.":
                tali "Nah, i have better things to do."
                scene black
                play sound "audio/walk.mp3"
                "Tali continues on her way..."
                $ whEvent1 = True
                jump barracks

    label prisonFirst:
        if prisFirst:
            scene bg prison
            show tali doubt at left
            with dis
            tali "This is... so filthy. Cages, cells, cameras. Definitely a prison... or something much worse."
            show tali tool at left
            tali "I don't see it on the scans. Someone really wanted to hide this chamber from the crew themselves."
            show tali doubt at left
            tali "Lets take a look."
            scene bg prison1
            with dis
            tali "These cages were broken down with brute force alone! I don't want to meet the creature that did this!"
            play sound "audio/creepone.mp3"
            scene bg prison2 with hpunch
            pause 1
            tali "Whoaaa!"
            tali "Easy there, ugly!"
            scene bg prison3
            with dis
            tali "Ugh. I can smell them through my filters. Good luck getting out of those, hah!"
            tali "I need to check the locks to make sure they don't get out."
            play sound "audio/creepone.mp3"
            pause 1
            tali "Yeah, yeah, you heard me right you bosh'tets."
            $ prisFirst = False
            jump prison
        jump prison

    label prison:
        $ roomID = 8
        if prisonLock == False and crewQuest:
            scene bg prison23
        elif prisonLock == False and act3:
            scene bg prison23
        else:
            scene bg prison
        show tali back at left
        call screen prison_items

    screen prison_items():
        modal True
        imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump ("map")

        showif prisonloot1:
            imagebutton:
                idle "images/events/prison/barrel_idle.png"
                hover "images/events/prison/barrel_hover.png"
                focus_mask True
                action [SetVariable("prisonloot1", False), Jump ("crate")]

        showif prisonloot2:
            imagebutton:
                idle "images/events/prison/crate1_idle.png"
                hover "images/events/prison/crate1_hover.png"
                focus_mask True
                action [SetVariable("prisonloot2", False), Jump ("crate")]

        showif prisonloot3:
            imagebutton:
                idle "images/events/prison/crate2_idle.png"
                hover "images/events/prison/crate2_hover.png"
                focus_mask True
                action [SetVariable("prisonloot3", False), Jump ("crate")]

        showif prisonloot4:
            imagebutton:
                idle "images/events/prison/food_idle.png"
                hover "images/events/prison/food_hover.png"
                focus_mask True
                action [SetVariable("prisonloot4", False), Jump ("dogBone")]

        showif prisoncage:
            imagebutton:
                idle "images/events/prison/jail_idle.png"
                hover "images/events/prison/jail_hover.png"
                focus_mask True
                action Jump ("prisonCage")

        showif prisoncage1:
            imagebutton:
                idle "images/events/prison/jail1_idle.png"
                hover "images/events/prison/jail1_hover.png"
                focus_mask True
                action [SetVariable("prisoncage1", False), Jump ("prisonCage1")]

        showif prisonbody:
            imagebutton:
                idle "images/events/prison/body_idle.png"
                hover "images/events/prison/body_hover.png"
                focus_mask True
                action [SetVariable("prisonbody", False), Jump ("prisonBody")]

    label dogBone:
        scene black
        show dogbone:
            xalign 1.2
            yalign 0.5
        show dogbone with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "Dogbone is found"
        $ havedogbone = True
        show dogbone with move:
            xalign -0.2
            yalign 0.5
        if prisonLock == False and crewQuest:
            scene bg prison23
        elif act3:
            scene bg prison23
        else:
            scene bg prison
        show tali doubt at left
        tali "Dogbone? Looks like the varrens toy."
        jump prison


    label prisonBody:
        scene bg prison16
        with dis
        tali "Poor guy never stood a chance. Another dead mercenary."
        scene black
        show clips:
            xalign 1.2
            yalign 0.5
        show clips with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        $ ammo += 5
        "5 thermal clips is found"
        show clips with move:
            xalign -0.2
            yalign 0.5
        scene bg prison16
        tali "Sorry, but you don't need it anymore."
        jump prison

    label prisonCage1:
        scene bg prison23
        show tali doubt at left
        tali "Well... great. Two more ravenous beasts roaming the corridors."
        show tali shame at left
        tali "I should have fixed that lock sooner."
        $ twoHount = True
        jump prison

    label prisonCage:
        scene bg prison3
        with dis
        tali "Well well, how it going, big bad monkeys?"
        menu prison_cage:
            "Check the cage":
                scene bg prison4
                if prisCum:
                    tali "Hmph. What's wrong you ape? Not in the mood for once?"
                    play sound "audio/creepone.mp3"
                    tali "I almost feel offended with this. Enjoy your cell you filthy animal."
                    jump prison
                else:
                    play sound "audio/gorillaroar.wav"
                    tali "Another performance i guess. Not impressed really."
                    scene bg prison5
                    pause .1
                    scene bg prison6
                    pause .1
                    scene bg prison7
                    pause .1
                    scene bg prison8
                    pause .1
                    scene bg prison9
                    pause .1
                    scene bg prison10
                    pause .1
                    scene bg prison11
                    pause .1
                    scene bg prison12
                    pause .1
                    scene bg prison13
                    pause .1
                    scene bg prison14
                    pause 1
                    tali "You have got to be kidding me..."
                    menu cageEvent:
                        "Buttplay" if lewd > 6:
                            jump cageButt
                        "Handjob" if lewd > 11:
                            jump cageHand
                        "Milking" if lewd > 15:
                            jump cageMilk
                        "Use lube" if lewd > 20 and isLube:
                            jump cageLube
                        "No way":
                            tali "No, really, i am leaving... now."
                            jump prison
            "Check the lock" if prisonLock == False:
                scene bg prison17
                with dis
                play sound "audio/error.mp3"
                tali "Another piece of weird technology. Hmmm..."
                play sound "audio/gorillaroar.wav"
                scene bg prison18
                pause 2
                tali "Hey, shut up! I trying to concentrate here for a minute. What a brute..."
                show bg prison17
                tali "Great. More inoperable scrap. The damned thing barely functions. But maybe I can fix it with some tech parts? 10 should do it for sure."
                $ lockQuest = True
                jump prison
            "Fix the lock (10 tech parts)" if parts > 9 and lockQuest:
                scene bg prison17
                with dis
                play sound "audio/uibeep.mp3"
                tali "Here we go."
                scene bg prison3
                with dis
                play sound "audio/creepone.mp3"
                tali "Hah! Bad news, boys. You'll be stuck in here for a long time!"
                $ lockQuest = False
                $ prisonLock = True
                jump prison


    label cageLube:
        $ lewd += 1
        $ prisCum = True
        scene bg prison20 with hpunch
        play sound "audio/punch.mp3"
        tali "I have some idea... Wanna hear?"
        play sound "audio/gorillaroar.wav"
        pause 2
        scene bg prevent1
        with dis
        tali "It might work nicely."
        play sound "audio/lewsquish.mp3"
        scene bg prevent2
        tali "Is that a smile on your ugly face?"
        scene bg prevent3
        tali "Now i can practice in some massage skills..."
        scene bg prevent8 with hpunch
        play sound "audio/punch.mp3"
        tali "Couldn't hold yourself again."
        play sound "audio/roar.mp3"
        tali "A little tribute won't hurt i guess."
        scene bg prevent4
        show cageLube_loop1
        $ renpy.pause ()
        scene bg prevent8
        tali "Oh i can't wait anymore... i want to try this cock."
        scene bg prison24
        play sound "audio/gorillaroar.wav"
        tali "Just let me open it a bit."
        scene bg prison25
        play sound "audio/dress.mp3"
        pause 2
        scene bg prevent7
        tali "I guess you wanted it all of this time, isn't you?"
        scene bg prevent5
        show cageLube_trans
        $ renpy.pause ()
        scene bg prevent5
        show cageLube_loop2
        $ renpy.pause ()
        scene bg prevent6
        show cageLube_loop3
        $ renpy.pause ()
        scene bg prevent6
        show cageLube_loop3
        tali "Ah, didn't expect it to be so good... ah"
        scene bg prevent6
        show cageLube_loop3alt
        tali "Don't dare to cum inside me... ah"
        scene bg prevent5
        show cageLube_cum
        $ renpy.pause ()
        scene black
        pause 1
        play sound "audio/dress.mp3"
        pause 1
        scene bg prison4
        tali "Well...  that's was quite interesting."
        play sound "audio/gorillaroar.wav"
        tali "Ugh, i done all the job for you again."
        jump prison

    label cageButt:
        $ lewd += 1
        scene bg prison20 with hpunch
        play sound "audio/punch.mp3"
        tali "You couldn't be any more pathetic could you? Well... fortunate for you I'm feeling sympathetic right now."
        scene bg prison19
        with dis
        tali "Ugh. Your smell is seeping into my suit. You better appreciate this."
        play sound "audio/gorillaroar.wav"
        pause 1
        tali "I'll... take that as a yes."
        scene bg prisonscene1
        show cageButtLoop
        $ renpy.pause ()
        scene bg prison20 with hpunch
        play sound "audio/roar.mp3"
        pause 1
        tali "Hold it! I'm sympathetic, not gullible. You're not getting any more from me today, got it?"
        scene bg prison14
        play sound "audio/roar.mp3"
        tali "Upset? Too bad. Not my problem. You should bust a nut faster next time. Later, space ape."
        $ prisCum = True
        jump prison

    label cageHand:
        $ lewd += 1
        scene bg prison20 with hpunch
        play sound "audio/punch.mp3"
        tali "Ugh. How do you walk with something so... thick?"
        play sound "audio/gorillaroar.wav"
        scene bg prisonscene4
        show cageHandLoop1
        $ renpy.pause ()
        scene bg prison20
        tali "Don't be so confident, i am just curious."
        scene bg prisonscene5
        show cageHandLoop2
        $ renpy.pause ()
        play sound "audio/roar.mp3"
        tali "How about this? It feels better right?"
        scene bg prisonscene5
        show cageHandLoop2alt
        $ renpy.pause ()
        scene bg prisonscene5
        show cageHandCum1
        $ renpy.pause ()
        scene bg prison4
        play sound "audio/gorillaroar.wav"
        tali "I guess you're happy with yourself now."
        $ prisCum = True
        jump prison

    label cageMilk:
        $ lewd += 1
        scene bg prison20 with hpunch
        play sound "audio/punch.mp3"
        tali "How do you walk with such a big thing..."
        play sound "audio/gorillaroar.wav"
        scene bg prisonscene4
        show cageHandLoop1
        $ renpy.pause ()
        scene bg prison20
        tali "Don't be so confident, i am just curious."
        scene bg prison15 with hpunch
        play sound "audio/punch.mp3"
        tali "GAH! H-HANDS OFF!"
        scene bg prison21 with hpunch
        play sound "audio/gorillaroar.wav"
        tali "Damned persistent, aren't you?"
        scene bg prisonscene2
        show cageHandLoop3
        $ renpy.pause ()
        scene bg prison21
        tali "N-Ngh. He's using my thighs like a fucksleeve. My pussy's getting so... sensitive!"
        scene bg prisonscene3
        show cageHandLoop4
        $ renpy.pause ()
        tali "H-Hmgh. Like this right? Let me milk that beastly load from those fat balls!"
        scene bg prisonscene3
        show cageHandLoop4alt
        $ renpy.pause ()
        scene bg prisonscene3
        show cageHandCum2
        $ renpy.pause ()
        scene bg prison4
        tali "Kmph. Hm. Proud of yourself?"
        play sound "audio/gorillaroar.wav"
        tali "Don't look at me like that."
        $ prisCum = True
        jump prison

    label barracks:
        if barracksDoor:
            jump secureDoor
        if asariCrew:
            $ asariCrew = False
            jump barracksCrew
        scene bg barracks
        show tali back at left
        call screen barracks_items

    label barracksCrew:
        $ crewCount += 1
        scene bg barracks1
        show tali doubt at left
        tali "Keelah, I finally found you! Where's Jesora?"
        show asari talk at right
        asari "Our group was split up not far from the hangar bay. The damn door slammed shut between us - damn near pinched my leg!"
        asari "We haven't heard from her since."
        show tali shame at left
        show asari stand at right
        tali "That's not good."
        show tali talk at left
        tali "The way to the hangar should be clear. Head back to Serok."
        show tali doubt at left
        show asari gun at right
        asari "Thank the Goddess. Thanks. We're leaving team, now!"
        play sound "audio/walk.mp3"
        "Asari leaving."
        jump barracks

    screen barracks_items():
        modal True
        imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump ("map")

        showif barracksloot1:
            imagebutton:
                idle "images/events/barracks/barrel1_idle.png"
                hover "images/events/barracks/barrel1_hover.png"
                focus_mask True
                action [SetVariable("barracksloot1", False), Jump ("crate")]

        showif barracksloot2:
            imagebutton:
                idle "images/events/barracks/barrel2_idle.png"
                hover "images/events/barracks/barrel2_hover.png"
                focus_mask True
                action [SetVariable("barracksloot2", False), Jump ("crate")]

        showif barracksloot3:
            imagebutton:
                idle "images/events/barracks/crate1_idle.png"
                hover "images/events/barracks/crate1_hover.png"
                focus_mask True
                action [SetVariable("barracksloot3", False), Jump ("crate")]

        showif barracksloot4:
            imagebutton:
                idle "images/events/barracks/battery_idle.png"
                hover "images/events/barracks/battery_hover.png"
                focus_mask True
                action [SetVariable("barracksloot4", False), Jump ("crate")]

        showif barracksEnt:
            imagebutton:
                idle "images/events/barracks/door_idle.png"
                hover "images/events/barracks/door_hover.png"
                focus_mask True
                action Jump ("barracksEnt")

        showif barracksTablet:
            imagebutton:
                idle "images/events/barracks/tablet_idle.png"
                hover "images/events/barracks/tablet_hover.png"
                focus_mask True
                action Jump ("barracksTablet")

    label barracksTablet:
        if tabletHacked:
            jump barracksTabletNext
        show tali tool at left
        tali "This holopad belonged to some human scientist who worked here. There are some messages I can view but..."
        show tali doubt at left
        tali "Heavy encryption. They didn't want anyone to read this."
        if hackOK:
            menu hackTablet:
                "Start decryption.":
                    $ hackID = 2
                    $ tabletHacked = True
                    jump sliderDoor
                "Another time.":
                    jump barracks
        else:
            tali "I need to recover my omni-tool to hack it."
        jump barracks

    label barracksTabletNext:
        show tali tool at left
        menu tabletMsg:
            "Read 1st message.":
                "Hey dad. Sorry I can't message you more often. Restrictions are tight and security checks every message in and out. Hope you're doing well."
                "Please stop asking about the ship or my work. Its just a side gig until I can find something better. I should be coming back home soon, word is the projects almost done."
                "Thats all I can say. Restrictions and all that. We'll go out once I get back, don't worry. Say hey to mom for me."
            "Read 2nd message.":
                "Lana, hey. It's Marcus. I got me an encrypted channel to shoot you a message. There's some weird shit happening here. They didn't tell me all the details when they hired me."
                "They pumping some animals with experimental serums and mating different species between each other, trying to breed some kind of super soldier. The boss is some looney Hanar with Cerberus connections?"
                "Don't tell my family, I don't want them to worry. Most of all I don't need them finding a reason to track them down if something goes wrong."
                "I heard we're waiting for another ship to deliver us some fresh cargo, new monsters and mercs. I'll try and stow away in there somehere. I gotta get out of here."
                "I'll contact you when I get to the nearest spaceport. I'll use this pad and its signature, there's no way I can leave it behind."
                show tali doubt at left
                tali "Cerberus. Why doesn't that surprise me. I could guess that Cerberus involved, what a slippery scum..."
            "Read 3rd message.":
                "SECURITY MANAGEMENT REQUEST: User - Marcus. Respond as soon as you have recieved this message. Unregistered encryption and communication was detected from this device to unknown 3rd parties."
                "This is a violation of your NDA and a breach of security. It is recommended you randevouz with your nearest security officer so that an investigation may begin to prove your innocence."
                "Do not forget to bring your private holopad."
            "Thats all.":
                jump barracks
        jump tabletMsg


    label barracksEnt:
        if barrackskey:
            play sound "audio/uibeep.mp3"
            tali "It worked! Door opens."
            jump utilityroom
        tali "Sealed. Looks like an ammo wing with type 2 security locks. No way I can blow this up. I wonder how much firepower's behind it?"
        tali "There's a keycard slot here. Maybe I can find one somewhere?"
        jump barracks

    label utilityroom:
        $ roomID = 9
        scene bg u
        show tali back at left
        call screen utility_items

    screen utility_items():
        modal True
        imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action [SetVariable("roomID", 6), Jump ("barracks")]

        showif uloot1:
            imagebutton:
                idle "images/events/utility/crate1_idle.png"
                hover "images/events/utility/crate1_hover.png"
                focus_mask True
                action [SetVariable("uloot1", False), Jump ("crate")]

        showif uloot2:
            imagebutton:
                idle "images/events/utility/crate2_idle.png"
                hover "images/events/utility/crate2_hover.png"
                focus_mask True
                action [SetVariable("uloot2", False), Jump ("crate")]

        showif uloot3:
            imagebutton:
                idle "images/events/utility/crate3_idle.png"
                hover "images/events/utility/crate3_hover.png"
                focus_mask True
                action [SetVariable("uloot3", False), Jump ("crate")]

        showif ulube:
            imagebutton:
                idle "images/events/utility/lub_idle.png"
                hover "images/events/utility/lub_hover.png"
                focus_mask True
                action [SetVariable("ulube", False), Jump ("uLube")]

    label uLube:
        scene black
        show lube:
            xalign 1.2
            yalign 0.5
        show lube with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "Lube is found"
        $ isLube = True
        show dogbone with move:
            xalign -0.2
            yalign 0.5
        scene bg u
        show tali doubt at left
        tali "Interesting. It says 'Safe to use. Special organic lubricant with isolating antiseptics'."
        tali "Might be helpfull..."
        jump utilityroom


    label bay1_enter:
        if bay1first:
            jump bay1door
        elif firstBay1:
            jump bay1event
        if bayDoor:
            jump secureDoor
        scene bg taliship
        show tali back at left
        call screen taliship_items

    screen taliship_items():
        modal True
        imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump ("map")

        showif talishiploot1:
            imagebutton:
                idle "images/events/bay1/ship/barrel1_idle.png"
                hover "images/events/bay1/ship/barrel1_hover.png"
                focus_mask True
                action [SetVariable("talishiploot1", False), Jump ("crate")]

        showif talishiploot2:
            imagebutton:
                idle "images/events/bay1/ship/crate1_idle.png"
                hover "images/events/bay1/ship/crate1_hover.png"
                focus_mask True
                action [SetVariable("talishiploot2", False), Jump ("crate")]

        showif talishiploot3:
            imagebutton:
                idle "images/events/bay1/ship/crate2_idle.png"
                hover "images/events/bay1/ship/crate2_hover.png"
                focus_mask True
                action [SetVariable("talishiploot3", False), Jump ("crate")]

        showif talishiploot4:
            imagebutton:
                idle "images/events/bay1/ship/crate3_idle.png"
                hover "images/events/bay1/ship/crate3_hover.png"
                focus_mask True
                action [SetVariable("talishiploot4", False), Jump ("crate")]

        showif talishipdoor:
            imagebutton:
                idle "images/events/bay1/ship/door_idle.png"
                hover "images/events/bay1/ship/door_hover.png"
                focus_mask True
                action Jump ("talishipEnt")

        showif havedogbone and lewd > 20:
            imagebutton:
                idle "images/events/bay1/ship/event_idle.png"
                hover "images/events/bay1/ship/event_hover.png"
                focus_mask True
                action Jump ("talishipevent")

    label talishipEnt:
        tali "Nothing more interesting there."
        jump bay1_enter

    label talishipevent:
        scene bg taliship1
        with dis
        tali "Maybe there's something useful in these crates?"
        play sound "audio/roar.mp3"
        scene bg taliship2
        tali "What?"
        scene bg taliship3
        tali "You?! Dare to come to me again?!"
        menu talishipchoice:
            "Attack":
                jump redvarrenfight
            "Play" if lewd > 20:
                jump redvarrenevent1
            "Leave":
                scene bg taliship4
                tali "Better to get out of here before he gets aggressive..."
                jump map

    label redvarrenfight:
        scene bg taliship
        show tali gunshoot at left
        show red stand at right
        play sound "audio/creepone.mp3"
        tali "Prepare to die, bastard!"
        $ enemyID = 20
        $ havedogbone = False
        jump sliderBoss


    label redvarrenevent1:
        $ lewd += 1
        scene bg taliship4
        tali "Huh. I guess you're not as aggressive as your other friends. I think I have something that belongs to you. Eyes up."
        scene bg taliship5
        play sound "audio/roar.mp3"
        pause 2
        scene bg taliship6
        with dis
        tali "Aww, you're just a big lovable varren aren't you? Nothing like those other creatures. Maybe I should give you a name..."
        scene bg taliship7
        with dis
        play sound "audio/dogbreath.mp3"
        tali "Oh! O-Oh Keelah. Is that..."
        scene bg taliship8
        with dis
        tali "Keelah. You must be very glad to see me. Its so thick and... hot. I guess I could... help you with that. Give me a minute..."
        scene bg taliship8
        show dogLoop1
        $ renpy.pause ()
        scene bg bay1event1
        with dis
        tali "You have such a great cock."
        scene bg bay1event1
        show dogLoop2
        $ renpy.pause ()
        scene bg bay1event1
        show dogLoop3
        $ renpy.pause ()
        scene bg bay1event2 with hpunch
        play sound "audio/dogbreath.mp3"
        tali "Y-You can't wait? Don't worry boy. Relax. Tali will take care of this massive dog cock."
        show dogLoop4
        $ renpy.pause ()
        scene bg bay1event2
        show dogLoop5
        $ renpy.pause ()
        scene bg bay1event3
        tali "I can feel your balls clenching. Mmm, give it to me. Paint my slutty quarian face with your got doggy load!"
        scene bg bay1event3
        show dogCum
        $ renpy.pause ()
        scene bg taliship
        show tali fin2 at left
        with dis
        tali "S-So much cum. I should... probably go to the medbay."
        $ havedogbone = False
        jump medbayafterdefeat

    label redtimerevent:
        play sound "audio/fall.ogg"
        show tali fallmask at left
        play sound "audio/glass.mp3"
        "Tali falls down."
        tali "No, dont come closer!"
        jump redvarrenevent2

    label redvarrenevent2:
        $ lewd += 1
        scene bg red1
        play sound "audio/roar.mp3"
        tali "Ok ok, you won, no problem. Maybe i was wrong... Can i just leave now, please?"
        scene bg red2
        play sound "audio/creepone.mp3"
        tali "Wha... what do you want from me?"
        play sound "audio/dogbreath.mp3"
        show red1_start
        $ renpy.pause ()
        scene bg red2
        show red1_loop2
        $ renpy.pause ()
        scene bg red2
        show red1_loop1
        $ renpy.pause ()
        scene bg red2
        show red1_loop2_alt
        $ renpy.pause ()
        scene bg red2
        show red1_cum
        $ renpy.pause ()
        scene bg taliship
        show tali fin2 at left
        with dis
        tali "Ah you filthy moron... i can't breathe..."
        show red stand at right
        play sound "audio/creepone.mp3"
        pause 2
        hide red stand
        play sound "audio/run.ogg"
        tali "I need to hurry..."
        jump medbayafterdefeat

    label bay1event:
        $ firstBay1 = False
        show bg taliship
        show tali gunstand at left
        with dis
        tali "This part of my ship is pretty well preserved. I see the door to the cockpit."
        show tali back at left
        tali "Damn it. It's blocked. The ship's systems aren't responding."
        show tali back at left
        tali "Lets open this fast. I hope the navigation system still works."
        show tali back1 at left
        show tali back1 at shake
        play sound "audio/punch.mp3"
        pause 1
        play sound "audio/creepone.mp3"
        tali "What the hell?! Where did you come from?!"
        scene bg taliship
        show doorhackstart
        $ renpy.pause ()
        scene bg taliship
        show tali back1 at left
        show tali back1 at shake
        play sound "audio/punch.mp3"
        pause 1
        tali "Back off, you moron!"
        show tali gunshoot at left
        play sound "audio/gunready.wav"
        show creep horny at right
        pause 1
        play sound "audio/gunshot.mp3"
        pause .5
        play sound "audio/gunshot.mp3"
        pause 1
        show creep horny at shake
        play sound "audio/punch.mp3"
        pause 1
        play sound "audio/creepone.mp3"
        hide creep horny
        with dis
        pause 2
        show tali gunstand at left
        tali "Not your lucky day, bosh'tet."
        play sound "audio/message.mp3"
        pause 1
        show tali tool at left
        jesora "Hey, you hear me? What goin on there?"
        tali "I got to the cockpit door. There was a distraction but everything's fine now. What was that alarm all across the ship?"
        jesora "Not sure but I got reports from out patrols. Seems a lot of security doors have begun to shut everywhere."
        jesora "Looks like you breaching into the local security system booted up a failsafe. Do what you have to and get back to me."
        tali "Copy."
        scene bg taliship
        $ hackID = 3
        jump sliderDoor

    label bay1cockpit:
        scene bg cockpit
        show tali back at left
        with dis
        tali "I can't believe the cockpit nearly surprised the explosion. Sad the rest couldn't. I wouldn't have to deal with those thugs to get off this ship otherwise."
        show tali shame at left
        tali "Alright, I got the navigation system parts. Now I can fix Serok's ship. There might be some scrap lying around if I ever need it so it couldn't hurt to come back."
        scene black
        play sound "audio/walk.mp3"
        "Tali trekked back to the hangar bay."
        jump hackQuestComplete

    label bay1door:
        $ bay1first = False
        scene bg bay1door
        show tali doubt at left
        with dis
        tali "Whooa, what a smell. This place has... changed a bit since my last visit."
        show tali tool at left
        play sound "audio/equip.ogg"
        tali "Alright, lets check it out."
        show tali tool at left
        tali "I have access to lock commands, but there's some pushback from security."
        show tali shame at left
        tali "Time to get hacking... and listen out for any unwanted attention."
        scene bg bay1doortut
        "Hacking is another simple mini game. In the upper-right corner you can see the descryption screen."
        "Click the HACK command when the blue slider moves between the yellow bars for a successful hack. Failure will result in a retry for that attempt."
        "The yellow number on the left shows how many subroutine Tali will need to hack in order to open the door."
        "Lastly, watch out for enemies. They can be nearby when Tali is hacking and can approach at any given moment."
        "If Tali's Lewd Level is high enough, punk bars will appear during hacking. This works the same as the yellow bars, but the results are entirely different..."
        scene bg bay1door
        jump sliderDoor

    label bay2_enter:
        if crewQuest:
            jump bay2_Serok
        elif act3:
            jump bay2_SerokAct3
        scene bg hangar
        with dis
        show jesora stand at right
        with dis
        show tali doubt at left
        with dis
        jesora "Nice to see you alive, suitgirl. How it going?"
        show tali talk at left
    label jesoratalkmenu:
        show tali doubt at left
        show jesora stand at right
        menu jesoratalk:
            "I want to buy something." :
                if parts > 0 :
                    jesora "Sure, take a look."
                    jump jesorashopmenu
                else:
                    jesora "Looks like you dont have what i need. Another time then."
            "You know something about this ship?" :
                show jesora talk at right
                jesora "We couldn't find any identification or track a drydock record. Its stateless, has no history, and doesn't look like any pirate ships I've ever seen."
                jesora "There are some... bodies of guys that look like high-end mercs. Any idea what outfit they're from?"
                jesora "My guess, professional and highly secretive. Someone's hiding dirty laundry and not pinching any pennies. I'd call myself resourcesful but even those guys I have nothing on."
            "What about those... creatures?" :
                show jesora talk at right
                jesora "If you're male, they'll kill ya. If you're female, you're gonna wish they did. Try not to get caught. I don't know why but I've lost too many girls on this ship already."
                jesora "They might be pets for some deviant or pent up animals they used for experiments. Doesn't matter what they used to be, now they're just predators thinking with their dicks."
            "Can you help me repair my omni-tool?" if secFirst == False and partsQuest == False:
                show jesora stand at right
                jesora "What exactly is broken?"
                show tali shame at left
                tali "A few parts fried after my last... encounter. My decryption protocol can't operate without parts for repair."
                show jesora think at right
                jesora "I see. Yeah I can help with that... but you'll have to do me a favor first."
                show tali doubt at left
                tali "You know I can help us both if I have a working omni-tool right?"
                show jesora stand at right
                jesora "I do. I also know that we both need spare parts to make this ship fly again. Bring me 20 parts and I'll get you what you need."
                $ quest = "Give 20 tech parts to Jesora."
            "Here 20 tech parts" if parts > 19 and partsQuest == False:
                $ parts -= 20
                show jesora talk at right
                jesora "Great. Wonderful. That solves a lot."
                show jesora stand at right
                show tali talk at left
                tali "Alright. What about my omni-tool?"
                show jesora talk at right
                jesora "Give me a minute. I'll let you know after I've scavanged a few parts from some of our expired crew. Take this as a bit of payment in the mean time."
                scene black
                show doorexp:
                    xalign 1.2
                    yalign 0.5
                show doorexp with move:
                    xalign 0.5
                    yalign 0.5
                play sound "audio/gunready.wav"
                "Tali take door breaching charge"
                $ doorexp += 1
                show doorexp with move:
                    xalign -0.2
                    yalign 0.5
                scene bg hangar
                show jesora stand at right
                show tali doubt at left
                tali "Thank you. I hope it won't take long. We'll be in touch."
                $ partsQuest = True
                $ quest = "Continue exploration."

            "I should go." :
                jump map

            #"I saw you having fun with vorchas." if shipInsideChoice:
                #show jesora smile at right
                #"Oh really, you are the little curious one, isnt you?"
                #show tali shame at left
                #show jesora smiletalk at right
                #jesora "Jealous?"
                #show tali angry at left
                #tali "What?! No, no, of course not... But is it weird a bit?"
                #show tali doubt at left
                #show jesora smile at right
                #jesora "Dont be so boring, suitgirl. You need to relax sometimes, right? I see that lewd sparklings in your eyes even through this cloudy helmet glass."
                #show tali shame at left
                #show jesora smiletalk at right
                #jesora "Wanna some fun?"
                #menu jesorafun:
                    #"Well, may be just a little..." if lewd > 15:
                        #$ shipInsideChoice = False
                        #jump jesoratalifun
                    #"No way!" :
                        #show tali doubt at left
                        #show jesora smile at right
                        #jesora "See you next time then, cutie."

        jump jesoratalkmenu

    label bay2_Serok:
        scene bg hangar
        with dis
        show serok stand at right
        with dis
        show tali doubt at left
        with dis
        serok "Hi, cutie. Found my crew yet?"
        show tali talk at left
    label seroktalkmenu:
        show tali doubt at left
        show serok stand at right
        menu seroktalk:
            "Do you always smoke?" :
                serok "Yes. Makes me look more professional when making deals."
                show serok smoke at right
                show tali talk at left
                tali "Aren't you worried about your health? Or, wait, I think you have two pairs of lungs?"
                show tali doubt at left
                show serok reason at right
                serok "I liberate scrap and salvage warships before governments or companies can collect what they lost. On a good day I get shot at twice. I don't expect to go under because of poor health, suitrat."
                show serok talk at right
                serok "I could catch a bullet on this ship or get mauled by some fuck-hungry space gorilla at any moment. If I want to smoke a whole pack in under a minute, I'm well within my right."
                show serok stand at right
                tali "The batarians would have had a great philosopher if you hadn't taken to pirating."
                show serok smoke at right
                pause 1
                show serok stand at right
                serok "Fuck off."
            "How did you manage to persuade Jesora and the other asari to join you?":
                show tali talk at left
                show serok reason at right
                serok "My unmatched charisma and panty-soaking charm."
                show tali doubt at left
                show serok smoke at right
                tali "You've never sounded creepier than just then."
                show serok stand at right
                serok "Jesora and her commandos were scrubbed by Thessia after a botched job. Something about a Spectre. It was a suicide mission at best. When shit went south, she and team were declared AWOL."
                show serok talk at right
                serok "Calling it messy is a disservice. She and her teams trial was set shortly after. She sounded ready to die, but I guess saving her team and seeing my ship nearby have her the push she needed."
            "Where did you get this ship?" :
                serok "I 'borrowed' it from my old boss."
                show tali talk at left
                tali "Oh. Well, he must really like you to let you do that."
                show tali doubt at left
                serok "You bet. He's dead."
                tali "Uhm. Okay then."
            "I should go." :
                jump map
        jump seroktalkmenu

    label jesoratalifun:

    label bay2_SerokAct3:
        scene bg hangar
        with dis
        show serok stand at right
        with dis
        show tali doubt at left
        with dis
        serok "Hi, cutie. Found my crew yet?"
        show tali talk at left
    label seroktalkmenuact3:
        show tali doubt at left
        show serok stand at right
        menu seroktalkact3:
            "Do you always smoke?" :
                serok "Yes. Makes me look more professional when making deals."
                show serok smoke at right
                show tali talk at left
                tali "Aren't you worried about your health? Or, wait, I think you have two pairs of lungs?"
                show tali doubt at left
                show serok reason at right
                serok "I liberate scrap and salvage warships before governments or companies can collect what they lost. On a good day I get shot at twice. I don't expect to go under because of poor health, suitrat."
                show serok talk at right
                serok "I could catch a bullet on this ship or get mauled by some fuck-hungry space gorilla at any moment. If I want to smoke a whole pack in under a minute, I'm well within my right."
                show serok stand at right
                tali "The batarians would have had a great philosopher if you hadn't taken to pirating."
                show serok smoke at right
                pause 1
                show serok stand at right
                serok "Fuck off."
            "How did you manage to persuade Jesora and the other asari to join you?":
                show tali talk at left
                show serok reason at right
                serok "My unmatched charisma and panty-soaking charm."
                show tali doubt at left
                show serok smoke at right
                tali "You've never sounded creepier than just then."
                show serok stand at right
                serok "Jesora and her commandos were scrubbed by Thessia after a botched job. Something about a Spectre. It was a suicide mission at best. When shit went south, she and team were declared AWOL."
                show serok talk at right
                serok "Calling it messy is a disservice. She and her teams trial was set shortly after. She sounded ready to die, but I guess saving her team and seeing my ship nearby have her the push she needed."
            "Where did you get this ship?" :
                serok "I 'borrowed' it from my old boss."
                show tali talk at left
                tali "Oh. Well, he must really like you to let you do that."
                show tali doubt at left
                serok "You bet. He's dead."
                tali "Uhm. Okay then."
            "Where is Jesora?":
                show serok reason at right
                serok "She should be in her cabin. You can go check anytime if want to talk."
                menu jesora_cabin:
                    "Sure.":
                        jump jesoraCabin
                    "Next time.":
                        jump seroktalkmenuact3
            "I should go." :
                jump map
        jump seroktalkmenuact3

    label jesoraCabin:
        scene bg jesorascene1
        with dis
        tali "Hmm, looks like it the right way."
        scene bg jesorascene2
        tali "Someone left the door open..."
        menu cabincheck:
            "Take a look(activate futa content)":
                scene bg jesorascene3
                tali "Oh spirits, this is the real bed! Never thought i'd miss the pillows so much."
                play sound "audio/shower.mp3"
                tali "There are somebody in shower."
                scene bg jesorascene4
                with dis
                play sound "audio/doorslide.mp3"
                pause 2
                scene bg jesorascene5
                tali "Guess i need to come next time."
                scene bg jesorascene6
                tali "Wow, what a thing..."
                scene bg jesorascene3
                show tali shame at left
                show jesora naketalk at right
                jesora "Hey, suitgirl. You wandering around?"
                show jesora nakestand at right
                tali "Ehh, hello Jesora. Just... yeah, looking for something..."
                show jesora naketalk at right
                jesora "You're not going to steal anything, right? Saw something interesting?"
                show tali talk at left
                show jesora nakestand
                tali "Yes... i mean, no... Listen, can you dress a bit?"
                show tali doubt at left
                show jesora naketalk at right
                jesora "Ah sorry, completely forgot about it, give me second."
                play sound "audio/dress.mp3"
                pause 2
                show jesora toweltalk at right
                jesora "Better?"
                show jesora towelstand at right
                show tali shame at left
                tali "Not quite but thanks anyway."
                show jesora toweltalk at right
                jesora "Good you come just in time. Just wanted to invite you for a drink."
                show jesora towelstand at right
                show tali talk at left
                tali "Mee? You sure now is..."
                show tali doubt at left
                show jesora toweltalk at right
                jesora "Sure thing! I want to thank you for the help you done for us. Take a sit, i'll be in moment."
                hide jesora
                tali "Well, i can stay for a bit."
                scene black
                "After some time."
                scene bg jesorascene7
                tali "And i told him like 'you're kidding, i won't take it in my mouth'. Hic!"
                scene bg jesorascene8
                jesora "Damn, really? Was he offended?"
                scene bg jesorascene9
                tali "Yeah... hic... he didn't say anything and then just didn't take me on next mission..."
                scene bg jesorascene7
                jesora "No way."
                tali "Yes. Took that dude Jacob... poor guy was so happy to go at least anywhere. Hic!"
                scene bg jesorascene10
                with dis
                tali "Wha... hic... what you doing?"
                jesora "Just want to be little closer to my fellow quarian."
                jesora "Look at me, Tali..."
                scene bg jesorascene11
                play sound "audio/glassfall.mp3"
                pause 2
                scene bg jesorascene12
                jesora "Just relax..."
                play sound "audio/hypno.mp3"
                show hypno
                $ renpy.pause ()
                scene black
                menu povmenu1:
                    "Jesora POV":
                        jump jesorascene_pov1
                    "Tali POV":
                        jump jesorascene_pov2

    label jesorascene_pov1:
        scene black
        show jesora1_loop1
        $ renpy.pause ()
        scene black
        show jesora1_trans1
        $ renpy.pause ()
        scene bg jesorapov1
        jesora "Good girl. Ready for action? Open wide."
        scene black
        show jesora1_trans2
        $ renpy.pause ()
        scene black
        show jesora1_loop2
        $ renpy.pause ()
        scene bg jesorapov2
        jesora "Ah, you have such a sweet mouth... let's go deeper."
        scene black
        show jesora1_loop3
        $ renpy.pause ()
        scene black
        show jesora1_trans3
        $ renpy.pause ()
        scene black
        show jesora1_loop4
        $ renpy.pause ()
        scene black
        show jesora1_cum
        $ renpy.pause ()
        jesora "What a sharpshooter am i today. Look at your pretty face, hehe."
        jump jesorasceneafter

    label jesorascene_pov2:
        scene black
        show tali1_loop1
        $ renpy.pause ()
        scene black
        show tali1_trans1
        $ renpy.pause ()
        scene bg talipov1
        jesora "Time the say aaaa, cutie. Open your sweet mouth."
        scene black
        show tali1_trans2
        $ renpy.pause ()
        scene black
        show tali1_loop2
        $ renpy.pause ()
        scene black
        show tali1_trans3
        $ renpy.pause ()
        scene bg talipov2
        jesora "Oh, look at you. You far more experienced than i expected. Lets stretch your quarian throat a bit."
        scene black
        show tali1_loop3
        $ renpy.pause ()
        scene black
        show tali1_trans4
        $ renpy.pause ()
        scene black
        show tali1_loop4
        $ renpy.pause ()
        scene black
        show tali1_cum
        $ renpy.pause ()
        jump jesorasceneafter

    label jesorasceneafter:
        scene black
        with dis
        scene bg jesorascene13
        tali "Ahhh... no... let me go..."
        scene bg jesorascene14
        tali "Ugh, what? Where am i?"
        scene bg jesorascene3
        show tali shame69 at left
        show jesora smiletalk at right
        jesora "Hello there, little boozer. Someone overdid it yesterday. Need a headache pill?"
        show jesora smile at right
        show tali talk69 at left
        tali "No thanks, i will be ok. Oh spirits, i don't remember half a day. What happened?"
        show tali doubt69 at left
        show jesora talk at right
        jesora "You drank and passed out on the couch. I put you on the bed."
        show jesora smile at right
        tali "I have a strange taste in the mouth."
        show jesora smiletalk at right
        jesora "Yeah, it a special asari liquor which I treated you yesterday. Very limited edition alcohol."
        show jesora stand at right
        show tali talk69 at left
        tali "Well, thanks for nice talk anyway. Better i return to the medbay."
        jesora "Sure. Anytime, cutie."
        scene black
        play sound "audio/walk.mp3"
        "Tali return to medbay."
        jump MedBayUsual


    label jesorashopmenu:
        show jesora stand at right
        show screen partsshop
        menu jesorashop:
            "Ammo (x3) - 3 tech part" if parts > 2:
                show jesora talk at right
                jesora "Here it is. Try not to spend all at once."
                $ parts -= 3
                $ ammo += 3
            "Grenade - 10 tech parts" if parts > 9:
                show jesora talk at right
                jesora "Be careful with it."
                $ parts -= 10
                $ grenades += 1
            "Breaching charge - 15 tech parts" if parts > 14:
                show jesora talk at right
                jesora "Use it wisely."
                $ parts -= 15
                $ doorexp += 1
            "Thats all for now":
                hide screen partsshop
                jump jesoratalk
        jump jesorashop

    screen partsshop:
        text "Tech parts remains: [parts]" xpos 0.4 ypos 0.1

    label corridor2:
        scene bg cor2walk
        play sound "audio/walk.mp3"
        "Tali walks down the hallway to the warehouse..."
        if corridor_fight:
            $ enemyID = 2
            play sound "audio/roar.mp3"
            scene bg cor2
            show tali gunshoot at left
            show varren stand at right
            with dis
            "Varren attacks!"
            jump sliderFight
        else:
            "Without accidents."
            jump warehouse

    label warehouse:
        if whDoor:
            jump secureDoor
        if vorchaCrew:
            $ whCont = True
            $ vorchaCrew = False
            jump crewWH
        $ roomID = 2
        if crewQuest:
            scene bg wh1
        elif act3:
            scene bg wh1
        else:
            scene bg wh
        show tali back at left
        call screen warehouse_items

    label crewWH:
        scene bg wh1
        show tali doubt at left
        with dis
        tali "There are definitely more bodies here than last time."
        show tali gunstand at left
        play sound "audio/gunready.wav"
        tali "I don't remember this thing here though. Looks like a thermal stabilizer! I need to check it carefully!"
        $ whlootbox1 = False
        $ whlootbox2 = False
        $ whlootbox3 = False
        jump warehouse

    screen warehouse_items():
        modal True
        imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump ("map")

        showif whlootbox1:
            imagebutton:
                idle "images/events/warehouse/whbarrel1_idle.png"
                hover "images/events/warehouse/whbarrel1_hover.png"
                focus_mask True
                action [SetVariable("whlootbox1", False), Jump ("crate")]

        showif whlootbox2:
            imagebutton:
                idle "images/events/warehouse/whbarrel2_idle.png"
                hover "images/events/warehouse/whbarrel2_hover.png"
                focus_mask True
                action [SetVariable("whlootbox2", False), Jump ("crate")]

        showif whlootbox3:
            imagebutton:
                idle "images/events/warehouse/whcrate1_idle.png"
                hover "images/events/warehouse/whcrate1_hover.png"
                focus_mask True
                action [SetVariable("whlootbox3", False), Jump ("crate")]

        showif whEvent1:
            imagebutton:
                idle "images/events/warehouse/whevent_idle.png"
                hover "images/events/warehouse/whevent_hover.png"
                focus_mask True
                action Jump ("whEvent1")

        showif whKrogan:
            imagebutton:
                idle "images/events/warehouse/whkrogan_idle.png"
                hover "images/events/warehouse/whkrogan_hover.png"
                focus_mask True
                action [SetVariable("whKrogan", False), Jump ("whKrogan")]

        #showif whVent:
            #imagebutton:
                #idle "images/events/warehouse/whvent_idle.png"
                #hover "images/events/warehouse/whvent_hover.png"
                #focus_mask True
                #action Jump ("whVent")

        showif whCont:
            imagebutton:
                idle "images/events/warehouse/whcont_idle.png"
                hover "images/events/warehouse/whcont_hover.png"
                focus_mask True
                action Jump ("whContainer")

    label whEvent1:
        tali "Dont remeber this thing there. Looks like thermal stabilizer, buy might to check closer."
        menu whEv:
            "Check closer":
                $ whEvent1 = False
                $ lewd += 1
                scene bg whevent1
                with dis
                tali "How am I supposed to do this...?"
                scene bg whevent2
                with dis
                tali "Ugh. I hate climbing."
                scene bg whevent3
                with dis
                tali "Just a little more... come on."
                scene bg whevent4 with hpunch
                play sound "audio/punch.mp3"
                tali "What? No! Not now!"
                scene bg whevent5 with hpunch
                play sound "audio/fall.ogg"
                tali "Damn it! This was a bad idea from the start!"
                scene bg whevent6
                play sound "audio/fall.ogg"
                pause 2
                scene bg whevent7
                tali "Move you stupid piece of scrap! Why are you so heavy!"
                play sound "audio/creepone.mp3"
                scene bg whevent8
                tali "You again?! How did you..."
                scene bg whevent9
                play sound "audio/creepone.mp3"
                tali "Stop! Where are you going?!"
                scene bg whevent10
                play sound "audio/roar.mp3"
                tali "What are you doing back there?! Don't you-"
                scene black
                play sound "audio/tier.mp3"
                tali "A-AGH! S-Stop doing that!"
                play sound "audio/tier.mp3"
                pause 1
                play sound "audio/creepone.mp3"
                pause 2
                show whAnimation
                tali "K-Keelah, my ass... Why do they love to fuck my ass so mu-uagh! H-Haghn!"
                scene black
                show whAnimation
                $ renpy.pause ()
                scene bg whevent11
                with dis
                play sound "audio/equip.ogg"
                jesora "Look what we have here..."
                tali "Anyone there?! Please, help me!"
                scene bg whevent12
                play sound "audio/creepone.mp3"
                jesora "Hold it!"
                scene black
                play sound "audio/run.ogg"
                "Red varren fled..."
                scene bg wh
                show tali shame at left
                show jesora smile at right
                tali "Well... thank you."
                show jesora smiletalk at right
                jesora "Sorry for interrupting you. You really looked like you were enjoying that."
                show tali angry at left
                tali "Wha... no! Just... look, I was stuck, okay? There's-!"
                show tali shame at left
                jesora "Talk about defensive. I can see that blush through the visor, haha. There you go quarian."
                show tali talk at left
                show jesora stand at right
                tali "That's... thank you. But what are you doing here?"
                show jesora talk at right
                jesora "I'm just patrolling. Checking the halls, seeing if the beasts pushed anything valuable through the corridors."
                show tali doubt at left
                jesora "Speaking of which, I found a little something you might be interested. A nice little room. You should give it a look. I've sent you the coordinates."
                show jesora stand at right
                show tali shame at left
                tali "Oh. Sure, yeah... thanks. But I think I'll visit the medbay first. Because... well..."
                show jesora smile at right
                jesora "You do you, quarian. I'm not here to tell you what to do."
                scene black
                with dis
                play sound "audio/walk.mp3"
                "Tali returns to medbay."
                $ prison = True
                jump medbayafterdefeat
            "Next time maybe.":
                jump warehouse

    label whContainer:
        $ whCont = False
        $ crewCount += 1
        scene bg wh1
        show tali gunstand at left
        play sound "audio/gunready.wav"
        tali "Hmmm... may be."
        play sound "audio/metaldoor.mp3"
        scene bg wh2
        pause 1
        tali "Seriously?"
        play sound "audio/funmoan.mp3"
        pause 1
        tali "Nice to chat with you guys, as always."
        scene bg wh3
        tali "Now move your asses to Serok! Go!"
        scene black
        play sound "audio/walk.mp3"
        "The Vorchas left."
        jump map

    label whKrogan:
        scene bg whkrogan
        with dis
        tali "He looks like a merc. The equipment is very expensive though. Bio-scans read he's been dead for over a month, maybe two. I... don't think Serok's boys killed him."
        tali "The helmet recorder is damaged. Whats here barely helps. Hmm. I think I can repair this with... lets see... Ah! Yes, last recods are available! Lets hear it."
        deadkrogan "This ship is starting to piss me off. Food's shit, everyone's weak. I'm the hired muscle but they just make me feed the varren and all those damned creatures in their cells."
        deadkrogan "The eggheads snatch em up at random, take them to women elsewhere onboard. Human, turian, asari. There's some kinky shit going on, but this isn't a pleasure cruise."
        deadkrogan "I hear some important fuck's coming. Maybe even the guy who organized all this shit. We need to have a talk. I'm not being paid enough to deal with this."
        tali "Looks like that's all there is. What was going on here? I need to keep looking."
        jump warehouse

    label whVent:
        tali "This is ventilation hatch. Its quite wide, i think i can get through there if find the way how to climb so high."
        jump warehouse


    label corridor1:
        scene bg cor1walk
        play sound "audio/walk.mp3"
        "Tali heads down the hallway to the engine room..."
        if corridor_fight:
            $ enemyID = 0
            play sound "audio/creepone.mp3"
            scene bg cor1
            show tali gunshoot at left
            show creep stand at right
            with dis
            "Creature attacks!"
            jump sliderFight
        else:
            "Without accidents."
            jump engine

    label engine:
        if engDoor:
            jump secureDoor
        $ roomID = 3
        scene bg engine
        show tali back at left
        call screen engine_items

    screen engine_items():
        modal True
        imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump ("map")

        showif englootbox1:
            imagebutton:
                idle "images/events/engine/enginebarrel1_idle.png"
                hover "images/events/engine/enginebarrel1_hover.png"
                focus_mask True
                action [SetVariable("englootbox1", False), Jump ("crate")]

        showif englootbox2:
            imagebutton:
                idle "images/events/engine/enginecrate1_idle.png"
                hover "images/events/engine/enginecrate1_hover.png"
                focus_mask True
                action [SetVariable("englootbox2", False), Jump ("crate")]

        showif englootbox3:
            imagebutton:
                idle "images/events/engine/enginecrate2_idle.png"
                hover "images/events/engine/enginecrate2_hover.png"
                focus_mask True
                action [SetVariable("englootbox3", False), Jump ("crate")]

        showif engControl:
            imagebutton:
                idle "images/events/engine/enginecontrol_idle.png"
                hover "images/events/engine/enginecontrol_hover.png"
                focus_mask True
                action Jump ("engControl")

    label engControl:
        tali "How old is this thing? I've never seen such a design. Its like it's assembled from different pieces from a debris field!"
        tali "The engines are working on secondary support. I'm lucky it works at all. Thermal stabilizers are functional. No way I can use it though. The rest of the ship falls apart without it."
        jump engine
    label med:
        "This is medbay"
        jump map


    label corridor1defeat:
        $ lewd += 1
        $ random = renpy.random.randint(1, 3)
        if lewd < 6 :
            jump corridor1scene2
        if lewd > 5 and lewd < 15:
            if random == 1 or random == 2 :
                jump corridor1scene2
            else:
                jump corridor1scene3
        if lewd > 14 :
            if random == 1 :
                jump corridor1scene1
            elif random == 2 :
                jump corridor1scene2
            else :
                jump corridor1scene3

    label corridor2defeat:
        $ lewd += 1
        $ random = renpy.random.randint(1, 4)
        if lewd < 6:
            jump corridor2scene1
        if lewd > 5 and lewd < 15 :
            if random == 1 or random == 2 :
                jump corridor2scene1
            elif random == 3 or random == 4 :
                jump corridor2scene3
        if lewd > 14 :
            if random == 1 :
                jump corridor2scene1
            elif random == 2 :
                jump corridor2scene2
            elif random == 3 :
                jump corridor2scene3
            else :
                jump corridor2scene4

    label corridor1scene1:
        $ infection += 1
        scene bg cor1bj1
        tali "H-His cock is too close... and its soo hard...!"
        scene bg cor1
        show cor1bjstart1
        $ renpy.pause ()
        scene bg cor1
        show cor1bjstart2
        tali "Hmmmppff..."
        scene bg cor1
        show cor1bjloop
        $ renpy.pause ()
        scene bg cor1
        show cor1bjcum
        "The creature pushed its cock deep into Tali's throat, alarming the quarian before filling her mouth with hot jets of its cum."
        scene bg cor1
        show cor1bjcum1
        $ renpy.pause ()
        scene bg cor1
        show tali fin2 at left
        with dis
        if infection < 3:
            tali "T-That was too much cum. My antibiotics should help, but... I need to find my helmet before it gets worse..."
            scene black
            play sound "audio/walk.mp3"
            "Tali continues her way..."
            jump engine
        else :
            tali "I swallow too much... Must go to medbay urgent."
            jump medbayafterdefeat

    label corridor1scene2:
        scene bg cor1back1
        tali "J-Just wait until I grab my gun, you... f-filthy animal!"
        scene bg cor1
        show cor1backstartloop
        $ renpy.pause ()
        scene bg cor1
        show cor1backcum1
        $ renpy.pause ()
        scene bg cor1
        show tali fin1 at left
        with dis
        tali "Ugh... I feel so nasty. My suit is undamaged but... I can keep going after some cleanup."
        scene black
        play sound "audio/walk.mp3"
        "Tali continues her way..."
        jump engine

    label corridor1scene3:
        $ infection += 1
        scene bg cor1back1
        tali "Just wait until i grab my gun, you... you dirty scum!"
        scene bg cor1
        show cor1backstartloop
        $ renpy.pause ()
        scene bg cor1
        show cor1backnextstage1
        tali "What? Wait! W-What are you doing there?! Stop!"
        scene bg cor1
        show cor1backnextstage2
        pause 2
        tali "A-AAAGHH! M-My pussy! He shoved his fat cock into my pussy!"
        scene bg cor1
        show cor1backmainloop1
        $ renpy.pause ()
        scene bg cor1
        show cor1backmainloop2
        $ renpy.pause ()
        scene bg cor1
        show cor1backmainloop2
        tali "Keelah. Keelah! I'm cumming! I'm cu-... cu-... a-ah! Agh!!"
        scene bg cor1
        show cor1backcum2
        $ renpy.pause ()
        tali "M-My toes... m-my body is... trembling... a-ah."
        scene bg cor1
        show tali fin1 at left
        if infection < 3:
            tali "The suit is... damaged from behind. Nothing critical thankfully. Initiate self-repair. With some antibiotics I should be fine... I hope."
            scene black
            play sound "audio/walk.mp3"
            "Tali continues her way..."
            jump engine
        else :
            tali "I cant take it more... must come back to medbay... now."
            jump medbayafterdefeat


    label corridor2scene1:
        scene bg cor2scene1
        tali "Get off me!"
        scene bg cor2
        show cor2loop1
        $ renpy.pause ()
        scene bg cor2
        show cor2cum1
        $ renpy.pause ()
        scene bg cor2
        show tali fin1 at left
        tali "Ugh... I feel so nasty. My suit is undamaged but... I can keep going after some cleanup."
        scene black
        play sound "audio/walk.mp3"
        "Tali continues her way..."
        jump warehouse

    label corridor2scene2:
        $ infection += 1
        scene bg cor2scene2
        tali "Its too close..."
        scene bg cor2
        show cor2loop2
        $ renpy.pause ()
        scene bg cor2
        show cor2stage11
        "Catching Tali off-guard, the varren pushes its cock into Tali's agape mouth."
        scene bg cor2
        show cor2stage12
        $ renpy.pause ()
        scene bg cor2
        show cor2loop3
        $ renpy.pause ()
        scene bg cor2
        show cor2stage21
        tali "Mmmmmhhh... noommghhhh..."
        "Ignoring Tali's moans, the varren delivers a sloppy pant as it steps forward and pushes its cock deep into Tali's throat."
        scene bg cor2
        show cor2stage22
        $ renpy.pause ()
        scene bg cor2
        show cor2loop4
        $ renpy.pause ()
        show cor2loop4
        "Tali gags helplessly as her throat is stretched and her mouth is filled with the taste of varren cock fucking it like a cunt."
        tali "K-Keelah. I can feel him cumming... every inch of his bestial varren cock throbbing... as he marks me like his bitch!"
        scene bg cor2
        show cor2cum2
        $ renpy.pause ()
        scene bg cor2
        show tali fin2 at left
        if infection < 3:
            tali "Oh, this is lot of jizz. Antibiotics will save me again this time. Need to find my helmet or it will get worse."
            scene black
            play sound "audio/walk.mp3"
            "Tali continue her way..."
            jump warehouse
        else :
            tali "I swallow too much... Must go to meday urgent."
            jump medbayafterdefeat

    label corridor2scene3:
        $ infection += 1
        scene bg cor2scene3
        tali "Stop it! No, what are you doing... ah..."
        scene bg cor2
        show cor2misloop1
        $ renpy.pause ()
        scene bg cor2
        show cor2misstage1
        pause 3
        scene bg cor2
        show cor2misloop2
        $ renpy.pause ()
        scene bg cor2
        show cor2misstage21
        tali "Keelah... so deep... ah ah"
        scene bg cor2
        show cor2misstage22
        pause 1
        scene bg cor2
        show cor2misloop3
        $ renpy.pause ()
        scene bg cor2
        show cor2miscum1
        $ renpy.pause ()
        scene bg cor2
        show tali fin1 at left
        if infection < 3:
            tali "Suit damaged... down there but nothing critical. Initiating self repair sequence. Some antibiotics and i will be ok."
            scene black
            play sound "audio/walk.mp3"
            "Tali continue her way..."
            jump warehouse
        else :
            tali "Ah keelah... my body in fire. I need to come back in medbay."
            jump medbayafterdefeat

    label corridor2scene4:
        $ infection += 1
        scene bg cor2scene3
        tali "Stop it! No, what are you doing... ah..."
        scene bg cor2
        show cor2misloop1
        $ renpy.pause ()
        scene bg cor2
        show cor2misstage1
        pause 3
        scene bg cor2
        show cor2misloop2
        $ renpy.pause ()
        scene bg cor2
        show cor2misstage21
        tali "Keelah... so deep... ah ah"
        scene bg cor2
        show cor2misstage22
        scene bg cor2
        show cor2misloop3
        $ renpy.pause ()
        scene bg cor2
        show cor2misstage3
        tali "W-What? Why did you stop?"
        scene bg cor2
        show cor2misloop4
        tali "Wait. Wait! WaitwaitwaitWAIT! There's no room left! D-Don't!"
        scene bg cor2
        show cor2misstage41
        tali "A-AGHHHHH! Y-Your knot! Your thick varren knot! I-It's so thick! Its so FAT!"
        scene bg cor2
        show cor2misstage42
        pause 2
        scene bg cor2
        show cor2misloop5
        $ renpy.pause ()
        scene bg cor2
        show cor2misloop5
        tali "Fuck me, fuck me, fuck me! Drill your bitch's cunt and give her a burning fat load! I'm cumming! Keelah, I'm cumming! A-AGH!"
        scene bg cor2
        show cor2miscum2
        $ renpy.pause ()
        scene bg cor2
        show tali fin1 at left
        if infection < 3:
            tali "Suit damaged... down there but nothing critical. Initiating self repair sequence. Some antibiotics and i will be ok."
            scene black
            play sound "audio/walk.mp3"
            "Tali continue her way..."
            jump warehouse
        else :
            tali "Ah keelah... my body in fire. I need to come back in medbay."
            jump medbayafterdefeat

    label com_biggy:
        $ enemyID = 1
        $ encounter = False
        scene black
        play sound "audio/roar.mp3"
        scene bg comscene1
        with dis
        tali "Another animal? Where did he come from?!"
        scene bg comscene2
        play sound "audio/gorillaroar.wav"
        tali "Damn it, he's blocking the way out! I'll kill you if I have to! Leave if you know whats best for you!"
        scene bg comtutorial3
        "Looks like its gonna be the hard way. Fighting will be handled through a simple mini-game the player will interact with."
        "A slider in the bottom-center will show the distane between Tali and the enemy. You have a limited window of opportunity before its hands or paws are on her."
        "Above the slider there are buttons which provide a number of options available to you. Dependong on your inventory you may have ammo, explosives, or just want to run away."
        "Each action has a chance to fail. Each enemy has their own difficulty level. All stats afterwards are generally random. Notice: Shooting and especially explosives will increase the alarm level."
        scene bg comroom
        jump sliderFight

    label comRoomEncounter:
        if comCum == False:
            $ random = renpy.random.randint(1, 100)
            if random > 60:
                $ comCum = True
                $ enemyID = 1
                scene black
                play sound "audio/roar.mp3"
                scene bg comscene1
                with dis
                tali "You again? Didn't you have enough last time?!"
                scene bg comscene2
                play sound "audio/gorillaroar.wav"
                tali "Alright then. Time to teach you another lesson!"
                scene bg comroom
                jump sliderFight
            else:
                jump map
        else:
            jump map


    label comRoomScenes:
        if comFirstScene == False:
            $ comFirstScene = True
            jump comRoomBJ1
        else:
            if (crewQuest):
                $ random = renpy.random.randint(1, 100)
                if random > 60:
                    jump comRoomAnal
                else:
                    jump comRoomBJ2
            elif (act3):
                $ random = renpy.random.randint(1, 100)
                if random > 60:
                    jump comRoomAnal
                else:
                    jump comRoomBJ2
            else:
                jump comRoomBJ2

    label comRoomBJ1:
        $ sex += 1
        $ lewd += 1
        $ infection += 1
        scene black
        with dis
        creature "Aggrrrrr"
        play sound "audio/roar.mp3"
        scene bg comscene3
        tali "No, let me go!"
        scene bg comscene4
        play sound "audio/gorillaroar.wav"
        creature "..."
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 2
        scene bg comscene4
        pause 2
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 1
        tali "Stop doing this, you bosh'tet!"
        scene bg comscene6 with hpunch
        play sound "audio/punch.mp3"
        pause 2
        scene bg comscene7 with hpunch
        play sound "audio/punch.mp3"
        tali "Get your hands off me! D-Don't touch that!"
        scene bg comscene8
        play sound "audio/roar.mp3"
        creature "Grrrrrrrrrr"
        scene bg combj1 with hpunch
        play sound "audio/punch.mp3"
        tali "Get that thing away from me!"
        tali "{i}Why is it so big!{/i}"
        scene bg combj2
        play sound "audio/gorillaroar.wav"
        tali "Noohhhmmmhm..."
        scene bg combj3
        play sound "audio/wetsquish.mp3"
        creature "Ughhrrr"
        show biggybjanim
        pause 10
        scene bg combj9
        tali "Nnnhhhhrrrrrr!!!"
        play sound "audio/gorillaroar.wav"
        scene bg combj10
        play sound "audio/lewdkiss.mp3"
        pause 1
        scene bg combj11
        pause 0.5
        scene bg combj10
        pause .5
        scene bg combj11
        pause .5
        scene bg combj10
        pause .5
        scene bg combj11
        pause 1
        scene bg combj12
        play sound "audio/lewdsplat.mp3"
        pause 1
        scene bg combj13
        play sound "audio/lewdsplat.mp3"
        pause 1
        scene bg combj14
        play sound "audio/gorillaroar.wav"
        tali "Stop it, please..."
        scene black
        with dis
        creature "..."
        play sound "audio/gorillaroar.wav"
        "Finally satisfied, the creature leaves Tali alone."
        scene bg comroom
        show tali fin2 at left
        with dis
        if infection < 3:
            tali "Oh, this is lot of jizz. Antibiotics will save me again this time. Need to find my helmet or it will get worse."
            scene black
            play sound "audio/walk.mp3"
            "Tali continue her way..."
            jump map
        else :
            tali "I swallow too much... Must go to medbay urgent."
            jump medbayafterdefeat

    label comRoomBJ2:
        $ lewd += 1
        $ infection += 1
        scene black
        with dis
        play sound "audio/roar.mp3"
        creature "Arrrrrrrr..."
        scene bg combj9
        play sound "audio/wetsquish.mp3"
        if lewd > 10:
            tali "Ugh. His dick's rolling across my tongue. It's so nasty... a-and its so thick and hard..."
        else:
            tali "I can't believe this is happening again... I-It's too big for my mouth!"
        show biggybjanim
        $ renpy.pause ()
        if lewd > 10:
            scene bg combj9
            tali "I-I'll use my tongue and make him cum faster. T-That should get this over with quickly."
            show biggybjanimnext
            $ renpy.pause ()
            scene bg combjcum1
            play sound "audio/sucking3.ogg"
            tali "Keelah, why won't you cum?"
            scene bg combjcum2
            play sound "audio/cumshot1.ogg"
            tali "K...Keelah... there's... too much..."
            play sound "audio/swallow.ogg"
            pause 1
            scene bg combjcum3
            play sound "audio/cumshot2.ogg"
            tali "M-My throat is... sooo... f-full..."
            scene bg combjcum4
            play sound "audio/wetsquish.mp3"
            pause 3
            if lewd > 20:
                scene bg combjcum5alt
                tali "L-Look what you've done you bosh'tet. You like that? Then let me show you a trick..."
                scene bg combjcum6
                play sound "audio/swallow.ogg"
                pause 2
                scene bg combjcum7
                tali "Aaaaaaaah..."
                play sound "audio/gorillaroar.wav"
            else:
                scene bg combjcum5
                tali "Aaaaaaaaah..."
                play sound "audio/gorillaroar.wav"
            scene bg comroom
            show tali fin2 at left
            # REMOVE TEST
            #jump comRoomAnal
            with dis
            if infection < 3:
                tali "T-That was too much cum. My antibiotics should help, but... I need to find my helmet before it gets worse..."
                scene black
                play sound "audio/walk.mp3"
                "Tali continue her way..."
                jump map
            else :
                tali "I swallow too much... Must go to medbay urgent."
                jump medbayafterdefeat
        else:
            play sound "audio/gorillaroar.wav"
            scene bg combj10
            play sound "audio/lewdkiss.mp3"
            pause 1
            scene bg combj11
            pause 0.5
            scene bg combj10
            pause .5
            scene bg combj11
            pause .5
            scene bg combj10
            pause .5
            scene bg combj11
            pause 1
            scene bg combj12
            play sound "audio/lewdsplat.mp3"
            pause 1
            scene bg combj13
            play sound "audio/lewdsplat.mp3"
            pause 1
            scene bg combj14
            play sound "audio/gorillaroar.wav"
            tali "Stop it, please..."
            scene black
            with dis
            creature "..."
            play sound "audio/gorillaroar.wav"
            "Finally satisfied, the creature left Tali alone."
            # REMOVE TEST
            #jump comRoomAnal
            scene bg comroom
            show tali fin2 at left
            with dis
            if infection < 3:
                tali "Oh, this is lot of jizz. Antibiotics will save me again this time. Need to find my helmet or it will get worse."
                scene black
                play sound "audio/walk.mp3"
                "Tali continue her way..."
                jump map
            else:
                tali "I swallow too much... Must go to medbay urgent."
                jump medbayafterdefeat

    label comRoomAnal:
        $ lewd += 1
        $ infection += 1
        scene black
        with dis
        play sound "audio/roar.mp3"
        creature "Aggrrrrr"
        scene bg comscene3
        tali "Keelah! Looks live I've been caught again!"
        scene bg comscene4
        play sound "audio/gorillaroar.wav"
        pause 2
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 2
        scene bg comscene4
        if lewd > 20:
            tali "H-Harder! Slap my thick purple cheeks harder!"
        pause 2
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 1
        if lewd > 20:
            tali "N-Ngh! S-Slap my bubbly quarian ass! I've been a very bad suitrat!"
        else:
            tali "Ah, stop doing this..."
        scene bg combj9
        play sound "audio/wetsquish.mp3"
        if lewd > 20:
            tali "Keelah, it's been too long. Shove that cock down my throat!"
        else:
            tali "I can't believe this is happening again... I-It's too big for my mouth."
        show biggybjanimnext
        $ renpy.pause ()
        if lewd > 20:
            scene bg comanal1
            play sound "audio/wetsquish.mp3"
            pause 2
            scene bg comanal2
            play sound "audio/lewdkiss.mp3"
            pause 1
            tali "Mnn. Such a nice, fat cock for me. K-Keelah. A-And the smell... I-It's..."
            scene black
            play sound "audio/gorillaroar.wav"
            tali "M-Mngh! Put it h-here... g-good boy."
            scene bg comanal3
            tali "Oh keelah, its feels so good!"
            show comroomanalfront1
            $ renpy.pause ()
            scene bg comanal3
            show comroomanalback1
            $ renpy.pause ()
            scene bg comanal7 with hpunch
            play sound "audio/punch.mp3"
            tali "F-Fuck! FUCK! S-Stretch me out! Fuck your quarian cockslut deeper!"
            scene bg comanal7
            show comroomanalback2
            $ renpy.pause ()
            scene bg comanal4
            play sound "audio/gorillaroar.wav"
            show comroomanalfront2
            $ renpy.pause ()
            scene bg comanal5
            tali "Yes! YES! I'm your little bitch! Your quarian jizzrag! Use me like a condom and dump your balls in me!"
            show comroomanalback2alt
            $ renpy.pause ()
            scene bg comanal8 with hpunch
            play sound "audio/cumshot2.ogg"
            tali "K-Keelah! KEELAH! Fill me with your cum! Empty your balls in me! I was born to be a cumdump!"
            scene bg comanal6 with hpunch
            play sound "audio/cumshot2.ogg"
            pause 2
        else:
            scene bg combjcum1
            play sound "audio/wetsquish.mp3"
            pause 2
            scene bg combj10
            play sound "audio/lewdkiss.mp3"
            tali "Oh, make it faster please..."
            play sound "audio/gorillaroar.wav"
            tali "He's not cumming yet? W-What does he have in mind? Keelah, I don't like this..."
            scene black
            play sound "audio/tier.mp3"
            tali "What?! No! Don't do that you bosh'tet!"
            scene bg comanal10
            play sound "audio/gorillaroar.wav"
            tali "Dont touch me, bosh'tet!"
            scene bg comanal7
            tali "What do you think you're doing?! Y-You can't grab me like this! I'm not a sex toy!"
            scene bg comanal8
            play sound "audio/lewdsplat.mp3"
            tali "N-NGHH! I... I can... feel him in m... my stomach!"
            scene bg comanal8
            show comroomanalback2
            $ renpy.pause ()
            scene bg comanal8
            show comroomanalfront2
            $ renpy.pause ()
            scene bg comanal5
            tali "Keelah. M-My poor ass has been stretched so hard..."
            scene bg comanal5
            show comroomanalback2alt
            $ renpy.pause ()
            scene bg comanal6
            play sound "audio/lewsquish.mp3"
            tali "N-Not inside, damn you! No-AGH!!"
        scene bg comanal6
        show comroomanalcum
        $ renpy.pause ()
        if lewd > 20:
            scene bg comanal9
            play sound "audio/gorillaroar.wav"
            tali "Cum. Hot, nasty, steaming cum. S-Sho good. S-Sho thick. F-Fuck me more daddy. Fill your cumdump up. Breed my quarian pussy until I forget my name...!"
            scene bg comroom
            show tali fin2 at left
            with dis
            tali "O-Oh. I got carried away there. Keelah, I need to hurry to the medbay."
            jump medbayafterdefeat
        else:
            scene bg comroom
            show tali fin2 at left
            with dis
            tali "My body in fire... i must hurry to medbay."
            jump medbayafterdefeat

    label comevent1:
        $ comFirstScene = True
        $ comIndicator = False
        $ sex += 1
        $ lewd += 1
        $ suitdur = 69
        scene black
        with dis
        creature "Aggrrrrr"
        play sound "audio/roar.mp3"
        scene bg comscene3
        tali "No, let me go!"
        scene bg comscene4
        play sound "audio/gorillaroar.wav"
        creature "..."
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 2
        scene bg comscene4
        pause 2
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 1
        tali "Stop doing this, you bosh'tet!"
        scene bg comscene6 with hpunch
        play sound "audio/punch.mp3"
        pause 2
        scene bg comscene7 with hpunch
        play sound "audio/punch.mp3"
        tali "Get your hand off! Dont touch this!"
        scene bg comscene8
        play sound "audio/roar.mp3"
        creature "Grrrrrrrrrr"
        scene bg combj1 with hpunch
        play sound "audio/punch.mp3"
        tali "Take this thing away from me!"
        tali "{i}Why is it so big!{/i}"
        scene bg combj2
        play sound "audio/gorillaroar.wav"
        tali "Noohhhmmmhm..."
        scene bg combj3
        play sound "audio/wetsquish.mp3"
        creature "Ughhrrr"
        show biggybjanim
        pause 10
        scene bg combj9
        tali "Nnnhhhhrrrrrr!!!"
        play sound "audio/gorillaroar.wav"
        scene bg combj10
        play sound "audio/lewdkiss.mp3"
        pause 1
        scene bg combj11
        pause 0.5
        scene bg combj10
        pause .5
        scene bg combj11
        pause .5
        scene bg combj10
        pause .5
        scene bg combj11
        pause 1
        scene bg combj12
        play sound "audio/lewdsplat.mp3"
        pause 1
        scene bg combj13
        play sound "audio/lewdsplat.mp3"
        pause 1
        scene bg combj14
        play sound "audio/gorillaroar.wav"
        tali "Stop it, please..."
        scene black
        with dis
        creature "..."
        play sound "audio/gorillaroar.wav"
        "Finally satisfied, the creature left Tali alone."
        if comEncounter == True:
            jump afterComEvent
        else:
            jump rooms


    label afterComEvent:
        $ comEncounter = False
        scene bg map
        with dis
        show tali shame at left
        tali "Ugh. What a waste. Nothing here but more filthy animals. I need some rest. I think I saw a shower in the medbay? I hope it still works."
        scene black
        with dis
        "Tali returned to medbay"
        scene bg shower1
        with dis
        play sound "audio/shower.mp3"
        tali "Mmm. Yesss. Finally, some comfort..."
        scene bg shower2
        with dis
        "........"
        if firstHelpChoice == False:
            jump showerEvent1
        scene bg shower3
        play sound "audio/heavyshots.mp3"
        tali "H-Huh? That sounded like the turret going off?"
        scene bg turret4
        with dis
        tali "What a mess. I should thank Jesora the next time I find see her. The things these creatures could have done to me..."
        $ engine = True
        $ warehouse = True
        $ barracks = True
        $ quest = "Search for tech parts"
        jump MedBayUsual

    label showerEvent1:
        $ lewd += 1
        scene bg shower3
        play sound "audio/buzzing.mp3"
        tali "What was that?!"
        scene bg showerscene1
        play sound "audio/buzzing.mp3"
        tali "Huh?"
        scene bg showerscene2
        play sound "audio/punch.mp3"
        tali "Aaaaa! What else is this?!"
        scene black
        play sound "audio/buzzing.mp3"
        tali "D-Don't try it!"
        play sound "audio/punch.mp3"
        tali "You little...! W-What the hell are you doing!"
        scene bg showerscene3
        tali "Its claws are scratching my skin!"
        show showerevent1
        pause 10
        tali "I-It's licking me?! How would it even...?!"
        scene bg showerscene9
        pause .1
        scene bg showerscene10
        pause .1
        scene bg showerscene11
        pause .1
        scene bg showerscene12
        pause .1
        scene bg showerscene13
        pause .1
        scene bg showerscene14
        play sound "audio/lewdsplat.mp3"
        tali "Aaaaaaaaah..."
        scene bg showerscene15
        tali "A-AH! I-It's inside me?!"
        show showerevent2
        pause 10
        scene bg showerscene15
        tali "I... It feels... so good. T-Try not to moan T-Tali. Just... Keelah..."
        scene bg showerscene16
        play sound "audio/buzzing.mp3"
        creature "Bzzzzzzzzz..."
        scene bg showerscene17
        play sound "audio/lewsquish.mp3"
        pause 3
        scene bg showerscene18
        pause 3
        scene bg showerscene19
        play sound "audio/lewdkiss.mp3"
        tali "Aaaaaah..."
        scene black
        play sound "audio/buzzing.mp3"
        "WWhile Tali tried to control herself, the creature disappeared as quickly as it came."
        scene bg med3
        with dis
        show tali shame at left
        with dis
        tali "That was... unexpected. I cant handle this alone, this ship is crawling with monsters."
        show tali doubt at left
        tali "I need to visit Serok in the hangar bay and ask for cover. He's a sleazebag but... Pride can come after we're off this ship."
        jump taliNoChoice

    label sliderDoor:
        $ heartSlider = False
        $ hackstage = 0
        $ borderValue1 = renpy.random.randint(1, 800)
        $ borderValue2 = borderValue1 + 100
        show tali back at left
        if door_fight:
            play sound "audio/creepone.mp3"
            tali "Oh, that was not a good sound. It came from behind. I need to hurry and open this door!"
        show doorhack
        show hacknumber:
            xalign 0.65
            yalign 0.08
        call screen sliderDoorHack

    label sliderDoorEnc:
        $ hackstep = 3
        $ borderValue1 = renpy.random.randint(1, 800)
        $ borderValue2 = borderValue1 + 50
        if hackstage == 1:
            if lewd > 10:
                $ heartSlider = True
                if borderValue1 < 450:
                    $ heartBorder1 = renpy.random.randint(550, 800)
                    $ heartBorder2 = heartBorder1 + 50
                else:
                    $ heartBorder1 = renpy.random.randint(0, 400)
                    $ heartBorder2 = heartBorder1 + 50
            else:
                $ heartSlider = False
            show tali back1 at left
            show tali back1 at shake
            play sound "audio/punch.mp3"
            tali "Keelah, this can't be happening. Not again! Open damn you!"
            scene bg securedoor1
            show doorhackstart
        elif hackstage == 2:
            $ heartSlider = False
            if lewd > 20:
                $ heartSlider = True
                if borderValue1 < 450:
                    $ heartBorder1 = renpy.random.randint(550, 800)
                    $ heartBorder2 = heartBorder1 + 50
                else:
                    $ heartBorder1 = renpy.random.randint(0, 400)
                    $ heartBorder2 = heartBorder1 + 50
            else:
                $ heartSlider = False
            scene bg securedoor1
            show tali back10 at left
            show tali back10 at shake
            play sound "audio/tier.mp3"
            tali "Damnit! OPEN! Why aren't you opening!"
            scene bg securedoor1
            show doorhacklick
        elif hackstage == 3:
            jump doorHackEvent
        show doorhack
        show hacknumber:
            xalign 0.65
            yalign 0.08
        call screen sliderDoorHack

    label doorHackEvent:
        hide screen sliderDoorHack
        scene bg securedoor1
        show doorhackpussy1
        $ renpy.pause ()
        scene bg securedoor1
        show doorhackpussy2
        pause 2
        tali "Ah, he is inside me..."
        scene bg securedoor1
        show doorhackpussyloop1
        $ renpy.pause ()
        scene bg securedoor1
        show doorhackpussyloop2
        tali "Ah oh no, not so fast... wait..."
        $ renpy.pause ()
        scene bg securedoor1
        show doorhackpussycum
        $ renpy.pause ()
        scene bg securedoor1
        show tali fin1 at left
        with dis
        tali "My body in fire... i must hurry to medbay."
        $ lewd += 1
        $ door_fight = False
        $ hackNumber = 3
        jump medbayafterdefeat


    screen sliderDoorHack:
        modal True
        text "[hackNumber]" xpos 0.63 ypos 0.11 size 90 color "#FFCC00"
        timer .01 repeat True action If(doorSliderValue > 0, true = SetVariable('doorSliderValue', doorSliderValue - hackstep), false=[Hide('sliderDoorHack'), Jump(doorHackJump)])
        imagebutton:
            idle "images/skills/hacker/button_idle.png"
            hover "images/skills/hacker/button_hover.png"
            focus_mask True
            xpos 0.7
            ypos 0.28
            action Jump("doorhackresult")

        bar:
            left_bar "images/skills/sliderbar1_idle.png"
            right_bar "images/skills/sliderbar1_empty.png"
            thumb "images/skills/thumb.png"
            value doorSliderValue
            range 1000
            xalign 0.95
            yalign 0.15
            xysize(500,70)

        bar:
            left_bar "images/skills/sliderbar1_empty.png"
            right_bar "images/skills/sliderbar1_empty.png"
            value StaticValue(borderValue1, 1000)
            thumb "images/skills/border.png"
            xalign 0.95
            yalign 0.15
            xysize(500,70)

        bar:
            left_bar "images/skills/sliderbar1_empty.png"
            right_bar "images/skills/sliderbar1_empty.png"
            value StaticValue(borderValue2, 1000)
            thumb "images/skills/border.png"
            xalign 0.95
            yalign 0.15
            xysize(500,70)

        showif heartSlider == True:
            bar:
                left_bar "images/skills/sliderbar1_empty.png"
                right_bar "images/skills/sliderbar1_empty.png"
                value StaticValue(heartBorder1, 1000)
                thumb "images/skills/borderheart.png"
                xalign 0.95
                yalign 0.15
                xysize(500,70)

        showif heartSlider == True:
            bar:
                left_bar "images/skills/sliderbar1_empty.png"
                right_bar "images/skills/sliderbar1_empty.png"
                value StaticValue(heartBorder2, 1000)
                thumb "images/skills/borderheart.png"
                xalign 0.95
                yalign 0.15
                xysize(500,70)

    label doorhackresult:
        if doorSliderValue > borderValue1 and doorSliderValue < borderValue2:
            play sound "audio/uibeep.mp3"
            "Success!"
            $ hackNumber -= 1
            if hackNumber == 0:
                $ doorSliderValue = 1000
                $ hackNumber = 3
                $ hackstep = 3
                if hackID == 1:
                    play sound "audio/dooropen.mp3"
                    scene bg securedoor1
                    pause .1
                    scene bg securedoor2
                    pause .1
                    scene bg securedoor3
                    pause .1
                    scene bg securedoor4
                    pause .1
                    scene bg securedoor5
                    pause .1
                    scene bg securedoor6
                    pause .1
                    scene bg securedoor7
                    pause .1
                    scene bg securedoor8
                    pause .1
                    scene bg securedoor9
                    pause .1
                    scene bg securedoor10
                    pause .1
                    scene bg securedoor11
                    pause .1
                    scene bg securedoor12
                    pause .5
                    scene black
                    if hackstage > 0:
                        play sound "audio/punch.mp3"
                        tali "Get off me!"
                        play sound "audio/run.ogg"
                        "Tali successfully escapes from enemy."
                    play sound "audio/walk.mp3"
                    $ door_fight = False
                    "Tali continue her way..."
                    $ hackID = 0
                    if roomID == 5:
                        $ whDoor = False
                        jump warehouse
                    elif roomID == 2:
                        $ whDoor = False
                        jump warehouse
                    elif roomID == 6:
                        $ barracksDoor = False
                        jump barracks
                    elif roomID == 1:
                        $ comDoor = False
                        jump comroom
                    elif roomID == 3:
                        $ engDoor = False
                        jump engine
                    elif roomID == 4:
                        $ engDoor = False
                        jump engine
                    elif roomID == 7:
                        $ bayDoor = False
                        jump bay1_enter
                elif hackID == 2:
                    $ hackID = 0
                    jump barracksTabletNext
                elif hackID == 3:
                    $ hackID = 0
                    jump bay1cockpit
                elif roomID == 7:
                    scene bg bay1door
                    show tali angry at left
                    play sound "audio/dooropen.mp3"
                    tali "Yes! Finally!"
                    play sound "audio/alert.mp3"
                    pause 1
                    show tali gunstand at left
                    tali "That's... odd. Sounded like the ship's general alert?"
                    show tali tool at left
                    play sound "audio/message.mp3"
                    tali "Jesora, do you copy? Anyone? Hello?"
                    play sound "audio/alert.mp3"
                    pause 2
                    show tali gunstand at left
                    play sound "audio/gunready.wav"
                    tali "No response... Lets move forward then. I can deal with it later."
                    jump bay1_enter



            $ hackstep += 1
        elif doorSliderValue > heartBorder1 and doorSliderValue < heartBorder2:
            "Success!"
            if hackstage == 1:
                jump backhandjob
            elif hackstage == 2:
                jump backanal

        else:
            play sound "audio/error.mp3"
            "Miss!"
        $ doorSliderValue = 1000
        if door_fight:
            $ hackstage += 1
            jump sliderDoorEnc
        if hackID == 1 and hackNumber < 3:
            jump door_chance
        else:
            jump sliderDoor


    label doorHackFail:
        play sound "audio/error.mp3"
        "Fail"
        $ doorSliderValue = 1000
        if door_fight:
            $ hackstage += 1
            jump sliderDoorEnc
        if hackID == 1 and hackNumber < 3:
            jump door_chance
        else:
            jump sliderDoor


    label backhandjob:
        scene bg securedoor1
        show tali hj1 at left
        show tali hj1 at shake
        play sound "audio/punch.mp3"
        tali "Look what we have here... Want me to take care of it?"
        scene bg securedoor1
        show doorhjstart
        $ renpy.pause ()
        scene bg securedoor1
        show tali hj11 at left
        tali "Mmm. You like that, don't you? Let me use my other hand..."
        scene bg securedoor1
        show doorhjloop1
        $ renpy.pause ()
        scene bg securedoor1
        show doorhjloop2
        $ renpy.pause ()
        scene bg securedoor1
        show doorhjloop3
        tali "Mph. You're close. I can feel it... Well, go on then. Dump your load over my face you dirty creature!"
        scene bg securedoor1
        show doorhjcum
        $ lewd += 1
        $ renpy.pause ()
        scene bg securedoor1
        show tali fin1 at left
        with dis
        tali "Keelah, what am I doing? I-It's so hard to resist..."
        scene black
        $ door_fight = False
        $ hackNumber = 3
        jump map


    label backanal:
        scene bg securedoor1
        show tali hj1 at left
        show tali hj1 at shake
        play sound "audio/punch.mp3"
        tali "Look what we have here... Want me to take care of it?"
        scene bg securedoor1
        show doorhjstart
        $ renpy.pause ()
        scene bg securedoor1
        show tali backanal1
        tali "Let me lube myself for you. K-Keelah, I can't..."
        scene bg securedoor1
        show dooranalstep1
        $ renpy.pause ()
        scene bg securedoor1
        show dooranalstep2
        $ renpy.pause ()
        scene bg securedoor1
        show tali backanal12
        tali "Y-You like that, right? Wanna try it?"
        scene bg securedoor1
        show dooranalstep3
        $ renpy.pause ()
        scene bg securedoor1
        show tali backanal27
        tali "Let me push it a bit..."
        scene bg securedoor1
        show dooranalstep4
        pause 2
        tali "Y-Your turn. Time to claim your prize, big boy..."
        scene bg securedoor1
        show dooranalstep5
        pause 1
        tali "Oh, yeah... i feel it."
        scene bg securedoor1
        show dooranalstep6
        $ renpy.pause ()
        if lewd > 25:
            scene bg securedoor1
            show tali backanal57
            tali "Like this... ah, let me do it..."
            scene bg securedoor1
            show dooranalstep6ext
            $ renpy.pause ()
        scene bg securedoor1
        show dooranalstep7
        $ renpy.pause ()
        scene bg securedoor1
        show dooranalstep7alt
        tali "Oh keelah, fuck my butt deeper!"
        scene bg securedoor1
        show dooranalcum
        $ renpy.pause ()
        scene bg securedoor1
        show tali fin1 at left
        with dis
        tali "That was... s-so good. My body is... Keelah, I'm shaking. I should... I should go to the medical bay."
        scene black
        $ door_fight = False
        $ hackNumber = 3
        jump medbayafterdefeat



    label sliderFight:
        $ enemyhp = renpy.random.randint(1, 5)
        show tali gunshoot at left
        if enemyID == 0:
            show creep stand at right
        elif enemyID == 1:
            show biggy stand at right
        elif enemyID == 2:
            show varren stand at right
        call screen slider

    screen slider():
        modal True
        showif ammo > 0:
            imagebutton:
                idle "images/skills/shoot_idle.png"
                hover "images/skills/shoot_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.3
                action Jump("shoot_skill")
        showif grenades > 0:
            imagebutton:
                idle "images/skills/grenskill_idle.png"
                hover "images/skills/grenskill_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.4
                action Jump("grenade_skill")
        imagebutton:
            idle "images/skills/escape_idle.png"
            hover "images/skills/escape_hover.png"
            focus_mask True
            xpos 0.45
            ypos 0.5
            action Jump("escape_skill")
        bar:
            left_bar "images/skills/sliderbar_idle.png"
            right_bar "images/skills/sliderbar_empty.png"
            thumb "images/skills/enemyicon.png"
            value AnimatedValue(0, 1000, 5, slidervalue)
            xalign 0.5
            yalign 0.7
            xysize(500,70)
        if roomID == 1 and enemyID == 1:
            if comIndicator:
                timer 5.5 action Jump("comevent1")
            else:
                timer 5.5 action Jump("comRoomScenes")
        if roomID == 4:
            timer 5.5 action Jump("corridor1defeat")
        if roomID == 5:
            timer 5.5 action Jump("corridor2defeat")


    label shoot_skill:
        $ alarm += 1
        $ ammo -= 1
        play sound "audio/gunshot.mp3"
        "Tali shoots!"
        $ random = renpy.random.randint(1, 100)
        if random > 1 and random < 70:
            play sound "audio/punch.mp3"
            if enemyID == 0:
                show creep stand at shake
                "Hit!"
            elif enemyID == 1:
                show biggy stand at shake
                "Hit!"
            elif enemyID == 2:
                show varren stand at shake
                "Hit!"
            $ enemyhp -= 1
            if enemyhp == 0 :
                if enemyID == 0:
                    show creep stand at right
                    hide creep stand
                    with Dissolve(2)
                elif enemyID == 1:
                    show biggy stand at right
                    hide biggy stand
                    with Dissolve(2)
                elif enemyID == 2:
                    show varren stand at right
                    hide varren stand
                    with Dissolve(2)
                "Enemy dead."
                $ corridor_fight = False
                if suitdur < 80:
                    $ suitdur += 20
            else:
                show tali gunshoot at shake
                play sound "audio/punch.mp3"
                "Emeny hits Tali!"
                $ suitdur -= random
                if suitdur < 1:
                    $ suitdur = 20
                    play sound "audio/fall.ogg"
                    show tali fall at left
                    "Tali falls down."
                    $ corridor_fight = False
                    tali "No, dont come closer!"
                    if roomID == 1 and enemyID == 1:
                        if comIndicator:
                            jump comevent1
                        else:
                            jump comRoomScenes
                    if roomID == 4:
                        show creep horny at right
                        show creep horny at left with move
                        play sound "audio/creepone.mp3"
                        scene black
                        with Dissolve(.5)
                        jump corridor1defeat
                    if roomID == 5:
                        show varren stand at right
                        show varren stand at left with move
                        play sound "audio/roar.mp3"
                        scene black
                        with Dissolve(.5)
                        jump corridor2defeat
                else:
                    call screen slider
            scene black
            play sound "audio/walk.mp3"
            "Tali continue her way..."
            if comEncounter == True:
                jump afterComEvent
            if roomID == 4:
                $ roomID = 3
            elif roomID == 5:
                $ roomID = 2
            elif roomID == 1:
                jump map
            jump rooms
        else:
            $ random = renpy.random.randint(15, 30)
            play sound "audio/miss.mp3"
            "Miss!"
            show tali gunshoot at shake
            play sound "audio/punch.mp3"
            "Emeny hits Tali!"
            $ suitdur -= random
            if suitdur < 1:
                $ suitdur = 20
                play sound "audio/fall.ogg"
                show tali fall at left
                "Tali falls down."
                $ corridor_fight = False
                tali "No, dont come closer!"
                if roomID == 1 and enemyID == 1:
                    if comIndicator:
                        jump comevent1
                    else:
                        jump comRoomScenes
                if roomID == 4:
                    show creep horny at right
                    show creep horny at left with move
                    play sound "audio/creepone.mp3"
                    scene black
                    with Dissolve(.5)
                    jump corridor1defeat
                if roomID == 5:
                    show varren stand at right
                    show varren stand at left with move
                    play sound "audio/roar.mp3"
                    scene black
                    with Dissolve(.5)
                    jump corridor2defeat
            else:
                call screen slider

    label grenade_skill:
        $ alarm += 5
        $ grenades -= 1
        play sound "audio/gunready.wav"
        show tali grenade at left
        "Fire in the hole!"
        if enemyID == 0:
            show creep stand at shake
            play sound "audio/explosion.mp3"
            "Devastating!"
            show creep stand at right
            hide creep stand
            with Dissolve(2)
        elif enemyID == 1:
            show biggy stand at shake
            play sound "audio/explosion.mp3"
            "Devastating!"
            show biggy stand at right
            hide biggy stand
            with Dissolve(2)
        elif enemyID == 2:
            show varren stand at shake
            play sound "audio/explosion.mp3"
            "Devastating!"
            show varren stand at right
            hide varren stand
            with Dissolve(2)
        "Enemy dead."
        scene black
        play sound "audio/walk.mp3"
        "Tali continue her way..."
        if comEncounter == True:
            jump afterComEvent
        if roomID == 4:
            $ roomID = 3
        elif roomID == 5:
            $ roomID = 2
        elif roomID == 1:
            jump map
        jump rooms


    label escape_skill:
        $ random = renpy.random.randint(1, 100)
        "Tali trying to run away!"
        if random > 1 and random < 50:
            play sound "audio/run.ogg"
            scene black
            "Escape successful."
            if comEncounter == True:
                jump afterComEvent
            jump map
        elif random > 50 and random < 100:
            play sound "audio/creepone.mp3"
            scene black
            "Escape failed..."
            if roomID == 1 and enemyID == 1:
                if comIndicator:
                    jump comevent1
                else:
                    jump comRoomScenes
            if roomID == 4:
                jump corridor1defeat
            if roomID == 5:
                jump corridor2defeat


    label rooms:
        if hackID == 1:
            jump sliderDoor
        elif roomID == 1:
            jump comroom
        elif roomID == 2:
            jump warehouse
        elif roomID == 3:
            jump engine
        elif roomID == 4:
            jump corridor1
        elif roomID == 5:
            jump corridor2
        elif roomID == 6:
            jump barracks



    label encounter_chance:
        $ random = renpy.random.randint(1, 100)
        if alarm < 21:
            $ enc_chance = 30
        elif alarm > 20 and alarm < 41:
            $ enc_chance = 50
        elif alarm > 40:
            $ enc_chance = 70
        if enc_chance / random >= 1:
            $ corridor_fight = True
        else:
            $ corridor_fight = False
        jump rooms

    label door_chance:
        $ random = renpy.random.randint(1, 100)
        if alarm < 21:
            $ enc_chance = 30
        elif alarm > 20 and alarm < 41:
            $ enc_chance = 40
        elif alarm > 40:
            $ enc_chance = 50
        if enc_chance / random >= 1:
            $ door_fight = True
        else:
            $ door_fight = False
        jump sliderDoor




    label define_loot:
        $ uloot1 = False
        $ uloot2 = False
        $ uloot3 = False
        $ whlootbox1 = False
        $ whlootbox2 = False
        $ whlootbox3 = False
        $ comroom_crate1 = False
        $ comroom_crate2 = False
        $ comroom_crate3 = False
        $ englootbox1 = False
        $ englootbox2 = False
        $ englootbox3 = False
        $ barracksloot1 = False
        $ barracksloot2 = False
        $ barracksloot3 = False
        $ barracksloot4 = False
        $ talishiploot1 = False
        $ talishiploot2 = False
        $ talishiploot3 = False
        $ talishiploot4 = False
        $ prisonloot1 = False
        $ prisonloot2 = False
        $ prisonloot3 = False
        $ random = renpy.random.randint(1, 200)
        if random > 1 and random < 41:
            $ uloot1 = True
        elif random > 40 and random < 81:
            $ uloot2 = True
        elif random > 80 and random < 121:
            $ uloot3 = True
        elif random > 120 and random < 151:
            $ uloot1 = True
            $ uloot3 = True
        elif random > 150 and random < 181:
            $ uloot2 = True
            $ uloot3 = True
        elif random > 180 and random < 200:
            $ uloot1 = True
            $ uloot2 = True
            $ uloot3 = True
        $ random = renpy.random.randint(1, 200)
        if random > 1 and random < 41:
            $ whlootbox1 = True
        elif random > 40 and random < 81:
            $ whlootbox2 = True
        elif random > 80 and random < 121:
            $ whlootbox3 = True
        elif random > 120 and random < 151:
            $ whlootbox1 = True
            $ whlootbox3 = True
        elif random > 150 and random < 181:
            $ whlootbox2 = True
            $ whlootbox3 = True
        elif random > 180 and random < 200:
            $ whlootbox1 = True
            $ whlootbox2 = True
            $ whlootbox3 = True
        $ random = renpy.random.randint(1, 200)
        if random > 1 and random < 41:
            $ comroom_crate1 = True
        elif random > 40 and random < 81:
            $ comroom_crate2 = True
        elif random > 80 and random < 121:
            $ comroom_barrel = True
        elif random > 120 and random < 151:
            $ comroom_crate1 = True
            $ comroom_barrel = True
        elif random > 150 and random < 181:
            $ comroom_crate1 = True
            $ comroom_crate2 = True
        elif random > 180 and random < 201:
            $ comroom_crate1 = True
            $ comroom_barrel = True
            $ comroom_crate2 = True
        $ random = renpy.random.randint(1, 200)
        if random > 1 and random < 41:
            $ englootbox1 = True
        elif random > 40 and random < 81:
            $ englootbox2 = True
        elif random > 80 and random < 121:
            $ englootbox3 = True
        elif random > 120 and random < 151:
            $ englootbox1 = True
            $ englootbox2 = True
        elif random > 150 and random < 181:
            $ englootbox1 = True
            $ englootbox3 = True
        elif random > 180 and random < 201:
            $ englootbox1 = True
            $ englootbox2 = True
            $ englootbox3 = True
        $ random = renpy.random.randint(1, 200)
        if random > 1 and random < 31:
            $ barracksloot1 = True
        elif random > 30 and random < 61:
            $ barracksloot2 = True
        elif random > 60 and random < 91:
            $ barracksloot3 = True
        elif random > 90 and random < 121:
            $ barracksloot1 = True
            $ barracksloot4 = True
        elif random > 120 and random < 151:
            $ barracksloot3 = True
            $ barracksloot2 = True
        elif random > 150 and random < 181:
            $ barracksloot1 = True
            $ barracksloot2 = True
            $ barracksloot3 = True
        elif random > 180 and random < 201:
            $ barracksloot1 = True
            $ barracksloot2 = True
            $ barracksloot3 = True
            $ barracksloot4 = True
        $ random = renpy.random.randint(1, 200)
        if random > 1 and random < 31:
            $ talishiploot1 = True
        elif random > 30 and random < 61:
            $ talishiploot2 = True
        elif random > 60 and random < 91:
            $ talishiploot3 = True
        elif random > 90 and random < 121:
            $ talishiploot1 = True
            $ talishiploot4 = True
        elif random > 120 and random < 151:
            $ talishiploot3 = True
            $ talishiploot2 = True
        elif random > 150 and random < 181:
            $ talishiploot1 = True
            $ talishiploot2 = True
            $ talishiploot3 = True
        elif random > 180 and random < 201:
            $ talishiploot1 = True
            $ talishiploot2 = True
            $ talishiploot3 = True
            $ talishiploot4 = True
        $ random = renpy.random.randint(1, 200)
        if random > 1 and random < 41:
            $ prisonloot1 = True
        elif random > 40 and random < 81:
            $ prisonloot2 = True
        elif random > 80 and random < 121:
            $ prisonloot3 = True
        elif random > 120 and random < 141:
            $ prisonloot1 = True
            $ prisonloot3 = True
        elif random > 140 and random < 181:
            $ prisonloot3 = True
            $ prisonloot2 = True
        elif random > 180 and random < 201:
            $ prisonloot1 = True
            $ prisonloot2 = True
            $ prisonloot3 = True

        jump MedBayUsual

    label sliderBoss:
        stop music
        play music "audio/bg/fight_bg.mp3" volume 0.6 loop
        $ enemyhp = 10
        $ suitdoor = 100
        show tali gunshoot at left
        if enemyID == 20:
            show red stand at right
        elif enemyID == 30:
            show monk stand at right
        call screen bossslider

    screen bossslider():
        modal True
        showif ammo > 0:
            imagebutton:
                idle "images/skills/shoot_idle.png"
                hover "images/skills/shoot_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.3
                action Jump("bossshoot_skill")
        showif grenades > 0:
            imagebutton:
                idle "images/skills/grenskill_idle.png"
                hover "images/skills/grenskill_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.4
                action Jump("bossgrenade_skill")
        bar:
            left_bar "images/skills/sliderbar_idle.png"
            right_bar "images/skills/sliderbar_empty.png"
            thumb "images/skills/enemyicon.png"
            value AnimatedValue(0, 1000, 5, slidervalue)
            xalign 0.5
            yalign 0.7
            xysize(500,70)
        if enemyID == 20:
            timer 5.5 action Jump("redtimerevent")
        if enemyID == 30:
            timer 5.5 action Jump("double_event1")

    label bossshoot_skill:
        $ alarm += 1
        $ ammo -= 1
        play sound "audio/gunshot.mp3"
        "Tali shoots!"
        $ random = renpy.random.randint(1, 100)
        if random > 1 and random < 70:
            if enemyID == 20:
                show red stand at shake
            elif enemyID == 30:
                show monk stand at shake
            play sound "audio/punch.mp3"
            "Hit!"
            $ enemyhp -= 1
            if enemyhp == 0 :
                if enemyID == 20:
                    show red stand at right
                    hide red stand
                    with Dissolve(1)
                    play sound "audio/run.ogg"
                    "Red varren fleed!"
                elif enemyID == 30:
                    show monk stand at right
                    hide monk stand
                    with Dissolve(1)
                    play sound "audio/run.ogg"
                    "Beasts fled!"
                if suitdur < 80:
                    $ suitdur += 20
            else:
                show tali gunshoot at shake
                play sound "audio/punch.mp3"
                "Emeny hits Tali!"
                $ random = renpy.random.randint(15, 30)
                $ suitdur -= random
                if suitdur < 1:
                    $ suitdur = 20
                    if enemyID == 20:
                        show tali fallmask at left
                        play sound "audio/glass.mp3"
                    elif enemyID == 30:
                        show tali fall at left
                        play sound "audio/fall.ogg"
                    "Tali falls down."
                    stop music
                    play music "audio/bg/common_bg.mp3" volume 0.3 loop
                    tali "No, dont come closer!"
                    if enemyID == 20:
                        jump redvarrenevent2
                    elif enemyID == 30:
                        jump double_event1
                else:
                    call screen bossslider
            show tali gunstand at left
            stop music
            play music "audio/bg/common_bg.mp3" volume 0.3 loop
            if enemyID == 20:
                tali "Right, run, you idiot! I will find you anyway."
                show tali doubt at left
                tali "It was hard but you done it, Tali."
                jump map
            elif enemyID == 30:
                tali "Yeah, run like little bitches! This time i owned you both, stupid monkeys."
                show tali doubt at left
                tali "Finally the way is clear."
                jump MedBayUsual
        else:
            $ random = renpy.random.randint(15, 30)
            play sound "audio/miss.mp3"
            "Miss!"
            show tali gunshoot at shake
            play sound "audio/punch.mp3"
            "Emeny hits Tali!"
            $ suitdur -= random
            if suitdur < 1:
                if enemyID == 20:
                    show tali fallmask at left
                    play sound "audio/glass.mp3"
                elif enemyID == 30:
                    show tali fall at left
                    play sound "audio/fall.ogg"
                "Tali falls down."
                stop music
                play music "audio/bg/common_bg.mp3" volume 0.3 loop
                tali "No, dont come closer!"
                if enemyID == 20:
                    jump redvarrenevent2
                elif enemyID == 30:
                    jump double_event1
            else:
                call screen bossslider

    label bossgrenade_skill:
        $ alarm += 5
        $ grenades -= 1
        play sound "audio/gunready.wav"
        show tali grenade at left
        "Fire in the hole!"
        if enemyID == 20:
            show red stand at shake
        elif enemyID == 30:
            show monk stand at shake
        play sound "audio/explosion.mp3"
        "Enemy was hit hard!"
        $ enemyhp -= 7
        if enemyhp < 1 :
            if enemyID == 20:
                show red stand at right
                hide red stand
                with Dissolve(1)
                play sound "audio/run.ogg"
                "Red varren fleed!"
            elif enemyID == 30:
                show monk stand at right
                hide monk stand
                with Dissolve(1)
                play sound "audio/run.ogg"
                "Beasts fled!"
            if suitdur < 80:
                $ suitdur += 20
        else:
            show tali gunshoot at shake
            play sound "audio/punch.mp3"
            "Emeny hits Tali!"
            $ random = renpy.random.randint(15, 30)
            $ suitdur -= random
            if suitdur < 1:
                if enemyID == 20:
                    show tali fallmask at left
                    play sound "audio/glass.mp3"
                elif enemyID == 30:
                    show tali fall at left
                    play sound "audio/fall.ogg"
                "Tali falls down."
                stop music
                play music "audio/bg/common_bg.mp3" volume 0.3 loop
                tali "No, dont come closer!"
                if enemyID == 20:
                    jump redvarrenevent2
                elif enemyID == 30:
                    jump double_event1
            else:
                call screen bossslider
        show tali gunstand at left
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        if enemyID == 20:
            tali "Right, run, you idiot! I will find you anyway."
            show tali doubt at left
            tali "It was hard but you done it, Tali."
            jump map
        elif enemyID == 30:
            tali "Yeah, run like little bitches! This time i owned you both, stupid monkeys."
            show tali doubt at left
            tali "Finally the way is clear."
            jump MedBayUsual
        else:
            $ random = renpy.random.randint(15, 30)
            play sound "audio/miss.mp3"
            "Miss!"
            show tali gunshoot at shake
            play sound "audio/punch.mp3"
            "Emeny hits Tali!"
            $ suitdur -= random
            if suitdur < 1:
                if enemyID == 20:
                    show tali fallmask at left
                    play sound "audio/glass.mp3"
                elif enemyID == 30:
                    show tali fall at left
                    play sound "audio/fall.ogg"
                "Tali falls down."
                stop music
                play music "audio/bg/common_bg.mp3" volume 0.3 loop
                tali "No, dont come closer!"
                if enemyID == 20:
                    jump redvarrenevent2
                elif enemyID == 30:
                    jump double_event1
            else:
                call screen bossslider









    return
