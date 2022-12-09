﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(None, who_color="#baf8ff", what_font="arial.ttf", what_italic=True, what_size = 25)
define tali = Character("Tali", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define ami = Character("AMI", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define creature = Character("Creature", who_color="#FF0000", what_font="arial.ttf", what_bold=True, what_size = 25)
define serok = Character("Serok", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define unknow = Character("Unknown voice", who_color="#baf8ff", what_font="arial.ttf", what_italic=True, what_size = 25)
define jesora = Character("Jesora", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define deadkrogan = Character("Krogan's voice", who_color="#FF4500", what_font="arial.ttf", what_size = 25)
define asari = Character("Asari", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define krogan = Character("Krogan", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define vorcha = Character("Vorcha", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define zeltan = Character("Zeltan", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define nyun = Character("Nyun", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define phantom = Character("Phantom", who_color="#baf8ff", what_font="arial.ttf", what_size = 25)
define dis = Dissolve(.5)
define nest = Character("Nest", who_color="#FF0000", what_font="arial.ttf", what_bold=True, what_size = 25)
image cell = "images/items/cell.png"
image egg = "images/items/egg.png"

image clips = "images/items/clips.png"
image parts = "images/items/parts.png"
image gren = "images/items/grenade.png"
image doorexp = "images/items/doorexp.png"
image keycard1 = "images/items/keycard.png"
image hacknumber = "images/skills/hacker/number.png"
image dogbone = "images/items/dogbone.png"
image lube = "images/items/lub.png"
image poolimg = "images/map/pool_idle.png"
image bay1img = "images/map/bay1_idle.png"
image prisonimg = "images/map/prison_idle.png"
image hallwayimg = "images/map/hallway_idle.png"
image comimg = "images/map/comroom_idle.png"
image bay2img = "images/map/bay2_idle.png"
image engineimg = "images/map/engine_idle.png"
image medimg = "images/map/med_idle.png"
image wareimg = "images/map/warehouse_idle.png"
image barimg = "images/map/barracks_idle.png"

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
define reddead = False
define secureDoors = True


define comroom = True
define engine = False
define warehouse = False
define bay1 = False
define bay1first = True
define bay2 = False
define barracks = False
define prison = False
define hallway = False
define hallwaydest = False
define pool = False
define poolnew = False
define poolFirst = True

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

define poolloot1 = False
define poolloot2 = False
define poolloot3 = False
define poolcomp = False

define whEvent1 = False
define whKrogan = True
define whVent = True
define whCont = False
define engControl = True

define barjesora = True
define barelkor = True
define barserok = True
define barnyun = True
define barvorcha = False
define barvar = False


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
define suit = 10
define sex = 1
# CHANGE TO 1
define lewd = 1
# CHANGE TO 3
define ammo = 3
# CHANGE TO 0
define run_ok = False
define run1 = False
define run2 = False
define run3 = False
define run4 = False
define darts = 0
define lovedart = False
define dartfirst = True
define grenades = 0
# CHANGE TO 0
define doorexp = 0
define alarm = 0
define parts = 0
define quest = "None"
define sidequest = "..."
define enemyhp = 0
define doorSliderValue = 1000
define doorHackJump = 'doorHackFail'
define hackNumber = 3
define hackstep = 3
define hackstage = 0
define fuckstage = 1
define fuckpose = 0
define sexpose = 0
define sexstage = 1
# CHANGE TO FALSE
define hackOK = False
define scanOK = False
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
define twoWinFirst = False
define twoCount = 0
define varHunt = False
define varCount = 0
define poolQuest = False
define barfirst = True
define gatesQuest = False
define gatesFlag = True
define bitchQuest = False
define scanQuest = False
define nyunfirst = True
define elkorFirst = True
define bugcount = 0
define bugfirst = True
define bugquest = False
define bugsact = False
define bugscene = 1
define barcount = 1
define zeltanhide = False
define zeltanengine = False
define zeltanhallway = False
define zeltanhappy = False
define zeltansex = False
define ventquest = False
define ventcount = 0
define poolvent = False
define z1 = False
define z2 = False
define z3 = False
define z4 = False

# change to 0
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

# --------------------- VENTS VARIABLES ------------------------------
define ventsopen = False
define vquest = "..."
define ventsidequest = "..."

define nyun1 = True
define nyun2 = True
define nyun3 = True
define nyun4 = True
define nyunover = False
define nyunquest = False
define nyunblock = False
define nyunhatch = False
define nyunami = False
define nyunsaved = False

define flesh1 = True

define ventID = 0
define fwd_ok = True
define left_ok = False
define right_ok = False
define aft_ok = False
define action_ok = True

#define quest = ""
define eggs = 0
define cells = 0
define hearts = 0
define arousal = 0
#define infection = 0
define nest1 = "Active"
define nest2 = "N/A"
define nest3 = "N/A"

define nestfirst = True

define slidervalue = 1000

define vent1 = True
define vent2 = True
define vent3 = True
define vent4 = False
define vent5 = True
define vent6 = True
define vent6seal = False

define catch1 = False
define catch2 = False
define catch3 = False
define catch4 = False
define catch5 = False

define shots = 0

define egg1 = False
define egg2 = False
define egg3 = False
define egg4 = False
define egg5 = False
define egg6 = False
define egg7 = False
define eggfirst = True

define bug1count = 0

define labcell = True

#CLICKER
default points = 25
default minus = 1
default plus = 5
default max_point = 50
default clicked = True

# SHOOTER
default points1 = 50
default minus1 = 2
default max_point1 = 50
default clicked1 = True
default hpcurrent = 100
default hpmax = 100
default hpdmg = 20


define encID = 0
define amifound = False
define amifirst = True

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
    "images/events/medbay/shower/scene1/anim1/0001.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim1/0002.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim1/0003.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim1/0004.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim1/0005.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim1/0006.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim1/0007.jpg"
    function lick
    pause 0.12
    "images/events/medbay/shower/scene1/anim1/0008.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim1/0009.jpg"
    pause 0.12
    repeat

image showerevent2:
    "images/events/medbay/shower/scene1/anim2/0001.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim2/0002.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim2/0003.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim2/0004.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim2/0005.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim2/0006.jpg"
    function splat
    pause 0.12
    "images/events/medbay/shower/scene1/anim2/0007.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim2/0008.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim2/0009.jpg"
    pause 0.12
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
    "images/events/bay1/event/bay1event1.jpg"
    pause .1
    "images/events/bay1/event/bay1event2.jpg"
    pause .1
    "images/events/bay1/event/bay1event3.jpg"
    pause .1
    "images/events/bay1/event/bay1event4.jpg"
    pause .1
    "images/events/bay1/event/bay1event5.jpg"
    pause .1
    "images/events/bay1/event/bay1event6.jpg"
    pause .1
    "images/events/bay1/event/bay1event7.jpg"
    pause .1
    "images/events/bay1/event/bay1event8.jpg"
    pause .1
    "images/events/bay1/event/bay1event9.jpg"
    pause .1
    "images/events/bay1/event/bay1event10.jpg"
    pause .1
    "images/events/bay1/event/bay1event11.jpg"
    pause .1
    "images/events/bay1/event/bay1event12.jpg"
    function lick
    pause .1
    "images/events/bay1/event/bay1event13.jpg"
    pause .1
    "images/events/bay1/event/bay1event14.jpg"
    pause .1
    "images/events/bay1/event/bay1event15.jpg"
    pause .1
    repeat

image dogLoop2:
    "images/events/bay1/event/bay1event16.jpg"
    pause .1
    "images/events/bay1/event/bay1event17.jpg"
    pause .1
    "images/events/bay1/event/bay1event18.jpg"
    pause .1
    "images/events/bay1/event/bay1event19.jpg"
    pause .1
    "images/events/bay1/event/bay1event20.jpg"
    pause .1
    "images/events/bay1/event/bay1event21.jpg"
    pause .1
    "images/events/bay1/event/bay1event22.jpg"
    pause .1
    "images/events/bay1/event/bay1event23.jpg"
    pause .1
    "images/events/bay1/event/bay1event24.jpg"
    pause .1
    "images/events/bay1/event/bay1event25.jpg"
    pause .1
    "images/events/bay1/event/bay1event26.jpg"
    pause .1
    "images/events/bay1/event/bay1event27.jpg"
    pause .1
    "images/events/bay1/event/bay1event28.jpg"
    pause .1
    "images/events/bay1/event/bay1event29.jpg"
    pause .1
    "images/events/bay1/event/bay1event30.jpg"
    pause .1
    repeat

image dogLoop3:
    "images/events/bay1/event/bay1event31.jpg"
    pause .1
    "images/events/bay1/event/bay1event32.jpg"
    pause .1
    "images/events/bay1/event/bay1event33.jpg"
    pause .1
    "images/events/bay1/event/bay1event34.jpg"
    pause .1
    "images/events/bay1/event/bay1event35.jpg"
    function inside
    pause .1
    "images/events/bay1/event/bay1event36.jpg"
    pause .1
    "images/events/bay1/event/bay1event37.jpg"
    pause .1
    "images/events/bay1/event/bay1event38.jpg"
    pause .1
    repeat

image dogLoop4:
    "images/events/bay1/event/bay1event39.jpg"
    pause .15
    "images/events/bay1/event/bay1event40.jpg"
    pause .15
    "images/events/bay1/event/bay1event41.jpg"
    pause .15
    "images/events/bay1/event/bay1event42.jpg"
    function lick
    pause .15
    "images/events/bay1/event/bay1event43.jpg"
    pause .15
    "images/events/bay1/event/bay1event44.jpg"
    pause .15
    "images/events/bay1/event/bay1event45.jpg"
    pause .15
    "images/events/bay1/event/bay1event46.jpg"
    pause .15
    repeat

image dogLoop5:
    "images/events/bay1/event/bay1event47.jpg"
    pause .15
    "images/events/bay1/event/bay1event48.jpg"
    pause .15
    "images/events/bay1/event/bay1event49.jpg"
    pause .15
    "images/events/bay1/event/bay1event50.jpg"
    pause .15
    "images/events/bay1/event/bay1event51.jpg"
    pause .15
    "images/events/bay1/event/bay1event52.jpg"
    function lick
    pause .15
    "images/events/bay1/event/bay1event53.jpg"
    pause .15
    "images/events/bay1/event/bay1event54.jpg"
    pause .15
    repeat

image dogCum:
    "images/events/bay1/event/cum/1.jpg"
    pause .15
    "images/events/bay1/event/cum/2.jpg"
    pause .15
    "images/events/bay1/event/cum/3.jpg"
    function cum1
    pause .15
    "images/events/bay1/event/cum/4.jpg"
    pause .15
    "images/events/bay1/event/cum/5.jpg"
    pause .15
    "images/events/bay1/event/cum/6.jpg"
    pause .15
    "images/events/bay1/event/cum/7.jpg"
    function cum2
    pause .15
    "images/events/bay1/event/cum/8.jpg"
    pause .15
    "images/events/bay1/event/cum/9.jpg"
    pause .15
    "images/events/bay1/event/cum/10.jpg"
    pause .15
    "images/events/bay1/event/cum/11.jpg"
    function cum2
    pause .15
    "images/events/bay1/event/cum/12.jpg"
    pause .15
    "images/events/bay1/event/cum/13.jpg"
    pause .15
    "images/events/bay1/event/cum/14.jpg"
    pause .15
    "images/events/bay1/event/cum/15.jpg"
    pause .15
    "images/events/bay1/event/cum/16.jpg"
    pause .15
    "images/events/bay1/event/cum/17.jpg"
    pause .15
    "images/events/bay1/event/cum/18.jpg"
    pause .15
    "images/events/bay1/event/cum/19.jpg"
    pause .15
    "images/events/bay1/event/cum/20.jpg"
    pause .15
    "images/events/bay1/event/cum/21.jpg"
    pause .15
    "images/events/bay1/event/cum/22.jpg"
    function cum1
    pause .15
    "images/events/bay1/event/cum/23.jpg"
    pause .15
    "images/events/bay1/event/cum/24.jpg"
    pause .15
    "images/events/bay1/event/cum/25.jpg"
    pause .15
    "images/events/bay1/event/cum/26.jpg"
    pause .15
    "images/events/bay1/event/cum/27.jpg"
    pause .15
    "images/events/bay1/event/cum/28.jpg"
    pause .15
    "images/events/bay1/event/cum/29.jpg"
    function splat
    pause .15
    "images/events/bay1/event/cum/30.jpg"
    pause .15
    "images/events/bay1/event/cum/31.jpg"
    pause .15
    "images/events/bay1/event/cum/32.jpg"
    pause .15
    "images/events/bay1/event/cum/33.jpg"
    pause .15
    "images/events/bay1/event/cum/34.jpg"
    pause .15
    "images/events/bay1/event/cum/35.jpg"
    pause .15
    "images/events/bay1/event/cum/36.jpg"
    pause .15
    "images/events/bay1/event/cum/37.jpg"
    pause .15

image red1_start:
    "images/events/bay1/varren/1.jpg"
    pause .15
    "images/events/bay1/varren/2.jpg"
    pause .15
    "images/events/bay1/varren/3.jpg"
    pause .15
    "images/events/bay1/varren/4.jpg"
    pause .15
    "images/events/bay1/varren/5.jpg"
    pause .15
    "images/events/bay1/varren/6.jpg"
    pause .15
    "images/events/bay1/varren/7.jpg"
    pause .15
    "images/events/bay1/varren/8.jpg"
    pause .15
    "images/events/bay1/varren/9.jpg"
    pause .15
    "images/events/bay1/varren/10.jpg"
    pause .15
    "images/events/bay1/varren/11.jpg"
    pause .15
    "images/events/bay1/varren/12.jpg"
    pause .15
    "images/events/bay1/varren/13.jpg"
    pause .15
    "images/events/bay1/varren/14.jpg"
    pause .15
    "images/events/bay1/varren/15.jpg"
    pause .15
    "images/events/bay1/varren/16.jpg"
    pause .15
    "images/events/bay1/varren/17.jpg"
    pause .15
    "images/events/bay1/varren/18.jpg"
    pause .15
    "images/events/bay1/varren/19.jpg"
    pause .15
    "images/events/bay1/varren/20.jpg"
    pause .15
    "images/events/bay1/varren/21.jpg"
    pause .15
    "images/events/bay1/varren/22.jpg"
    pause .15
    "images/events/bay1/varren/23.jpg"
    pause .15
    "images/events/bay1/varren/24.jpg"
    pause .15
    "images/events/bay1/varren/25.jpg"
    pause .15
    "images/events/bay1/varren/26.jpg"
    pause .15
    "images/events/bay1/varren/27.jpg"
    pause .15
    "images/events/bay1/varren/28.jpg"
    pause .15
    "images/events/bay1/varren/29.jpg"
    pause .15
    "images/events/bay1/varren/30.jpg"
    function inside
    pause .15
    "images/events/bay1/varren/31.jpg"
    pause .15
    "images/events/bay1/varren/32.jpg"
    pause .15
    "images/events/bay1/varren/33.jpg"
    pause .15
    "images/events/bay1/varren/34.jpg"
    pause .15
    "images/events/bay1/varren/35.jpg"
    pause .15
    "images/events/bay1/varren/36.jpg"
    pause .15
    "images/events/bay1/varren/37.jpg"
    pause .15
    "images/events/bay1/varren/38.jpg"
    pause .15
    "images/events/bay1/varren/39.jpg"
    pause .15
    "images/events/bay1/varren/40.jpg"
    pause .15
    "images/events/bay1/varren/41.jpg"
    pause .15
    "images/events/bay1/varren/42.jpg"
    pause .15
    "images/events/bay1/varren/43.jpg"
    pause .15
    "images/events/bay1/varren/44.jpg"
    pause .15
    "images/events/bay1/varren/45.jpg"
    pause .15
    "images/events/bay1/varren/46.jpg"
    pause .15
    "images/events/bay1/varren/47.jpg"
    pause .15
    "images/events/bay1/varren/48.jpg"
    pause .15
    "images/events/bay1/varren/49.jpg"
    pause .15
    "images/events/bay1/varren/50.jpg"
    pause .15
    "images/events/bay1/varren/51.jpg"
    pause .15
    "images/events/bay1/varren/52.jpg"
    pause .15
    "images/events/bay1/varren/53.jpg"
    pause .15
    "images/events/bay1/varren/54.jpg"
    pause .15
    "images/events/bay1/varren/55.jpg"
    pause .15
    "images/events/bay1/varren/56.jpg"
    pause .15
    "images/events/bay1/varren/57.jpg"
    function suck4

image red1_loop1:
    "images/events/bay1/varren/58.jpg"
    pause .1
    "images/events/bay1/varren/59.jpg"
    pause .1
    "images/events/bay1/varren/60.jpg"
    pause .1
    "images/events/bay1/varren/61.jpg"
    pause .1
    "images/events/bay1/varren/62.jpg"
    function s2
    pause .1
    "images/events/bay1/varren/63.jpg"
    pause .1
    repeat

image red1_loop2:
    "images/events/bay1/varren/64.jpg"
    pause .1
    function suck1
    "images/events/bay1/varren/65.jpg"
    pause .1
    "images/events/bay1/varren/66.jpg"
    pause .1
    "images/events/bay1/varren/67.jpg"
    pause .1
    "images/events/bay1/varren/68.jpg"
    function s3
    pause .1
    "images/events/bay1/varren/69.jpg"
    pause .1
    repeat

image red1_loop2_alt:
    "images/events/bay1/varren/64.jpg"
    pause .07
    function suck2
    "images/events/bay1/varren/65.jpg"
    pause .07
    "images/events/bay1/varren/66.jpg"
    pause .07
    "images/events/bay1/varren/67.jpg"
    pause .07
    "images/events/bay1/varren/68.jpg"
    function s1
    pause .07
    "images/events/bay1/varren/69.jpg"
    pause .07
    repeat

image red1_cum:
    "images/events/bay1/varren/cum/1.jpg"
    pause .15
    "images/events/bay1/varren/cum/2.jpg"
    pause .15
    "images/events/bay1/varren/cum/3.jpg"
    function suck4
    pause .15
    "images/events/bay1/varren/cum/4.jpg"
    pause .15
    "images/events/bay1/varren/cum/5.jpg"
    pause .15
    "images/events/bay1/varren/cum/6.jpg"
    pause .15
    "images/events/bay1/varren/cum/7.jpg"
    pause .15
    "images/events/bay1/varren/cum/8.jpg"
    pause .15
    "images/events/bay1/varren/cum/9.jpg"
    pause .15
    "images/events/bay1/varren/cum/10.jpg"
    pause .15
    "images/events/bay1/varren/cum/11.jpg"
    pause .15
    "images/events/bay1/varren/cum/12.jpg"
    pause .15
    "images/events/bay1/varren/cum/13.jpg"
    pause .15
    function cum1
    "images/events/bay1/varren/cum/14.jpg"
    pause .15
    "images/events/bay1/varren/cum/15.jpg"
    pause .15
    "images/events/bay1/varren/cum/16.jpg"
    pause .15
    "images/events/bay1/varren/cum/17.jpg"
    pause .15
    "images/events/bay1/varren/cum/18.jpg"
    pause .15
    "images/events/bay1/varren/cum/19.jpg"
    pause .15
    "images/events/bay1/varren/cum/20.jpg"
    pause .15
    "images/events/bay1/varren/cum/21.jpg"
    pause .15
    "images/events/bay1/varren/cum/22.jpg"
    pause .15
    "images/events/bay1/varren/cum/23.jpg"
    pause .15
    "images/events/bay1/varren/cum/24.jpg"
    function cumsplash
    pause .15
    "images/events/bay1/varren/cum/25.jpg"
    pause .15
    "images/events/bay1/varren/cum/26.jpg"
    pause .15
    "images/events/bay1/varren/cum/27.jpg"
    pause .15
    "images/events/bay1/varren/cum/28.jpg"
    pause .15
    "images/events/bay1/varren/cum/29.jpg"
    pause .15
    "images/events/bay1/varren/cum/30.jpg"
    pause .15
    "images/events/bay1/varren/cum/31.jpg"
    pause .15
    "images/events/bay1/varren/cum/32.jpg"
    pause .15
    "images/events/bay1/varren/cum/33.jpg"
    pause .15
    "images/events/bay1/varren/cum/34.jpg"
    function swallow
    pause .15
    "images/events/bay1/varren/cum/35.jpg"
    pause .15
    "images/events/bay1/varren/cum/36.jpg"
    pause .15
    "images/events/bay1/varren/cum/37.jpg"
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
    "images/events/jesora/Tpov/loop1/0.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/1.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/2.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/3.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/4.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/5.jpg"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/6.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/7.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/8.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/9.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/10.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/11.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/12.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/13.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/14.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/15.jpg"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/16.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/17.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/18.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/19.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/20.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/21.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/22.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/23.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/24.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/25.jpg"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/26.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/27.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/28.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/29.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/30.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/31.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/32.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/33.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/34.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/35.jpg"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/36.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/37.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/38.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/39.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/40.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/41.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/42.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/43.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/44.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/45.jpg"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/46.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/47.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/48.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/49.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/50.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/51.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/52.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/53.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/54.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/55.jpg"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/56.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/57.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/58.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/59.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/60.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/61.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/62.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/63.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/64.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/65.jpg"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/66.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/67.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/68.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/69.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/70.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/71.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/72.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/73.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/74.jpg"
    pause .1
    "images/events/jesora/Tpov/loop1/75.jpg"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop1/76.jpg"
    pause .1
    repeat

image tali1_trans1:
    "images/events/jesora/Tpov/trans1/0077.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0078.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0079.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0080.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0081.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0082.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0083.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0084.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0085.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0086.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0087.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0088.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0089.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0090.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0091.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0092.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0093.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0094.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0095.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0096.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0097.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0098.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0099.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0100.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0101.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0102.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0103.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0104.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0105.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0106.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0107.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0108.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0109.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0110.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0111.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0112.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0113.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0114.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0115.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0116.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0117.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0118.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0119.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0120.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0121.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0122.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0123.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0124.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0125.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0126.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0127.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0128.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0129.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0130.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0131.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0132.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0133.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0134.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0135.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0136.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0137.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0138.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0139.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0140.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0141.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0142.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0143.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0144.jpg"
    pause .1

image tali1_trans2:
    "images/events/jesora/Tpov/trans1/0145.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0146.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0147.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0148.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0149.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0150.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0151.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0152.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0153.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0154.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0155.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0156.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0157.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0158.jpg"
    function suck4
    pause .1
    "images/events/jesora/Tpov/trans1/0159.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0160.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0161.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0162.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0163.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0164.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0165.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0166.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0167.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0168.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0169.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0170.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0171.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0172.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0173.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0174.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0175.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0176.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0177.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0178.jpg"
    pause .1
    "images/events/jesora/Tpov/trans1/0179.jpg"
    pause .1

image tali1_loop2:
    "images/events/jesora/Tpov/loop2/0180.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0181.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0182.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0183.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0184.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0185.jpg"
    function suck1
    pause .1
    "images/events/jesora/Tpov/loop2/0186.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0187.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0188.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0189.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0190.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0191.jpg"
    pause .1
    "images/events/jesora/Tpov/loop2/0192.jpg"
    pause .1
    repeat

image tali1_trans3:
    "images/events/jesora/Tpov/trans2/0194.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0195.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0196.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0197.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0198.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0199.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0200.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0201.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0202.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0203.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0204.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0205.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0206.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0207.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0208.jpg"
    function suck4
    pause .1
    "images/events/jesora/Tpov/trans2/0209.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0210.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0211.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0212.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0213.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0214.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0215.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0216.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0217.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0218.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0219.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0220.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0221.jpg"
    function suck1
    pause .1
    "images/events/jesora/Tpov/trans2/0222.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0223.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0224.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0225.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0226.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0227.jpg"
    pause .1
    "images/events/jesora/Tpov/trans2/0228.jpg"
    pause .1

image tali1_loop3:
    "images/events/jesora/Tpov/loop3/0229.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0230.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0231.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0232.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0233.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0234.jpg"
    function suck4
    pause .1
    "images/events/jesora/Tpov/loop3/0235.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0236.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0237.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0238.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0239.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0240.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0241.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0242.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0243.jpg"
    function suck3
    pause .1
    "images/events/jesora/Tpov/loop3/0244.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0245.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0246.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0247.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0248.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0249.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0250.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0251.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0252.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0253.jpg"
    function suck4
    pause .1
    "images/events/jesora/Tpov/loop3/0254.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0255.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0256.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0257.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0258.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0259.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0260.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0261.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0262.jpg"
    function suck1
    pause .1
    "images/events/jesora/Tpov/loop3/0263.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0264.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0265.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0266.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0267.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0268.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0269.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0270.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0271.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0272.jpg"
    function suck2
    pause .1
    "images/events/jesora/Tpov/loop3/0273.jpg"
    pause .1
    "images/events/jesora/Tpov/loop3/0274.jpg"
    pause .1
    repeat

image tali1_trans4:
    "images/events/jesora/Tpov/trans3/0275.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0276.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0277.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0278.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0279.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0280.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0281.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0282.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0283.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0284.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0285.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0286.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0287.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0288.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0289.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0290.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0291.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0292.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0293.jpg"
    function s2
    pause .1
    "images/events/jesora/Tpov/trans3/0294.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0295.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0296.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0297.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0298.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0299.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0300.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0301.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0302.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0303.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0304.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0305.jpg"
    pause .1
    "images/events/jesora/Tpov/trans3/0306.jpg"
    pause .1

image tali1_loop4:
    "images/events/jesora/Tpov/loop4/0307.jpg"
    pause .1
    "images/events/jesora/Tpov/loop4/0308.jpg"
    pause .1
    "images/events/jesora/Tpov/loop4/0309.jpg"
    pause .1
    "images/events/jesora/Tpov/loop4/0310.jpg"
    function inside
    pause .1
    "images/events/jesora/Tpov/loop4/0311.jpg"
    pause .1
    "images/events/jesora/Tpov/loop4/0312.jpg"
    pause .1
    "images/events/jesora/Tpov/loop4/0313.jpg"
    pause .1
    "images/events/jesora/Tpov/loop4/0314.jpg"
    pause .1
    repeat

image tali1_cum:
    "images/events/jesora/Tpov/cum/0321.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0322.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0323.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0324.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0325.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0326.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0327.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0328.jpg"
    function cum1
    pause .1
    "images/events/jesora/Tpov/cum/0329.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0330.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0331.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0332.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0333.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0334.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0335.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0336.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0337.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0338.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0339.jpg"
    function cum1
    pause .1
    "images/events/jesora/Tpov/cum/0340.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0341.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0342.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0343.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0344.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0345.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0346.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0347.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0348.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0349.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0350.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0351.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0352.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0353.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0354.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0355.jpg"
    function cum2
    pause .1
    "images/events/jesora/Tpov/cum/0356.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0357.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0358.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0359.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0360.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0361.jpg"
    pause .1
    "images/events/jesora/Tpov/cum/0362.jpg"

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
    "images/events/jesora/Jpov/loop1/0000.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0001.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0002.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0003.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0004.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0005.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0006.jpg"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0007.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0008.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0009.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0010.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0011.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0012.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0013.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0014.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0015.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0016.jpg"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0017.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0018.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0019.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0020.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0021.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0022.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0023.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0024.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0025.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0026.jpg"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0027.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0028.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0029.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0030.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0031.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0032.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0033.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0034.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0035.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0036.jpg"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0037.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0038.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0039.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0040.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0041.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0042.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0043.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0044.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0045.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0046.jpg"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0047.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0048.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0049.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0050.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0051.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0052.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0053.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0054.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0055.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0056.jpg"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0057.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0058.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0059.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0060.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0061.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0062.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0063.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0064.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0065.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0066.jpg"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop1/0067.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0068.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0069.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0070.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0071.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0072.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0073.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0074.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0075.jpg"
    pause .1
    "images/events/jesora/Jpov/loop1/0076.jpg"
    function inside
    pause .1
    repeat

image jesora1_trans1:
    "images/events/jesora/Jpov/trans1/0077.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0078.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0079.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0080.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0081.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0082.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0083.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0084.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0085.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0086.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0087.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0088.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0089.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0090.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0091.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0092.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0093.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0094.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0095.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0096.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0097.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0098.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0099.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0100.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0101.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0102.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0103.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0104.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0105.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0106.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0107.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0108.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0109.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0110.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0111.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0112.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0113.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0114.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0115.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0116.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0117.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0118.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0119.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0120.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0121.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0122.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0123.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0124.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0125.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0126.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0127.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0128.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0129.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0130.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0131.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0132.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0133.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0134.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0135.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0136.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0137.jpg"
    pause .1
    "images/events/jesora/Jpov/trans1/0138.jpg"
    pause .1

image jesora1_trans2:
    "images/events/jesora/Jpov/trans2/0139.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0140.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0141.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0142.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0143.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0144.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0145.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0146.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0147.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0148.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0149.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0150.jpg"
    function s2
    pause .1
    "images/events/jesora/Jpov/trans2/0151.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0152.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0153.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0154.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0155.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0156.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0157.jpg"
    pause .1
    "images/events/jesora/Jpov/trans2/0158.jpg"
    function suck4
    pause .1
    "images/events/jesora/Jpov/trans2/0159.jpg"
    pause .1

image jesora1_loop2:
    "images/events/jesora/Jpov/loop2/0160.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0161.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0162.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0163.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0164.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0165.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0166.jpg"
    function suck1
    pause .1
    "images/events/jesora/Jpov/loop2/0167.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0168.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0169.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0170.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0171.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0172.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0173.jpg"
    pause .1
    "images/events/jesora/Jpov/loop2/0174.jpg"
    pause .1
    repeat

image jesora1_loop3:
    "images/events/jesora/Jpov/loop3/0176.jpg"
    pause .1
    "images/events/jesora/Jpov/loop3/0177.jpg"
    pause .1
    "images/events/jesora/Jpov/loop3/0178.jpg"
    pause .1
    "images/events/jesora/Jpov/loop3/0179.jpg"
    function suck4
    pause .1
    "images/events/jesora/Jpov/loop3/0180.jpg"
    pause .1
    "images/events/jesora/Jpov/loop3/0181.jpg"
    pause .1
    "images/events/jesora/Jpov/loop3/0182.jpg"
    pause .1
    "images/events/jesora/Jpov/loop3/0183.jpg"
    pause .1
    "images/events/jesora/Jpov/loop3/0184.jpg"
    pause .1
    "images/events/jesora/Jpov/loop3/0185.jpg"
    pause .1
    "images/events/jesora/Jpov/loop3/0186.jpg"
    pause .1
    repeat

image jesora1_trans3:
    "images/events/jesora/Jpov/trans3/0187.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0188.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0189.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0190.jpg"
    function s2
    pause .1
    "images/events/jesora/Jpov/trans3/0191.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0192.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0193.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0194.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0195.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0196.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0197.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0198.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0199.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0200.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0201.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0202.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0203.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0204.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0205.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0206.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0207.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0208.jpg"
    pause .1
    "images/events/jesora/Jpov/trans3/0209.jpg"
    pause .1

image jesora1_loop4:
    "images/events/jesora/Jpov/loop4/0210.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0211.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0212.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0213.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0214.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0215.jpg"
    function inside
    pause .1
    "images/events/jesora/Jpov/loop4/0216.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0217.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0218.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0219.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0220.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0221.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0222.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0223.jpg"
    pause .1
    "images/events/jesora/Jpov/loop4/0224.jpg"
    pause .1
    repeat

image jesora1_cum:
    "images/events/jesora/Jpov/cum/0210.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0211.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0212.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0213.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0214.jpg"
    function cum1
    pause .1
    "images/events/jesora/Jpov/cum/0215.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0216.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0217.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0218.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0219.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0220.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0221.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0222.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0223.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0224.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0225.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0226.jpg"
    function cum1
    pause .1
    "images/events/jesora/Jpov/cum/0227.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0228.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0229.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0230.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0231.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0232.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0233.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0234.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0235.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0236.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0237.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0238.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0239.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0240.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0241.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0242.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0243.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0244.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0245.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0246.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0247.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0248.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0249.jpg"
    function cum2
    pause .1
    "images/events/jesora/Jpov/cum/0250.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0251.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0252.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0253.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0254.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0255.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0256.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0257.jpg"
    pause .1
    "images/events/jesora/Jpov/cum/0258.jpg"
    pause .1

image meddp1_loop1:
    "images/events/medbay/double/loop1/0001.jpg"
    pause .1
    "images/events/medbay/double/loop1/0002.jpg"
    pause .1
    "images/events/medbay/double/loop1/0003.jpg"
    pause .1
    "images/events/medbay/double/loop1/0004.jpg"
    function slap1
    pause .1
    "images/events/medbay/double/loop1/0005.jpg"
    pause .1
    "images/events/medbay/double/loop1/0006.jpg"
    pause .1
    "images/events/medbay/double/loop1/0007.jpg"
    pause .1
    "images/events/medbay/double/loop1/0008.jpg"
    pause .1
    "images/events/medbay/double/loop1/0009.jpg"
    pause .1
    repeat

image meddp1_loop2:
    "images/events/medbay/double/loop2/0025.jpg"
    pause .1
    "images/events/medbay/double/loop2/0026.jpg"
    pause .1
    "images/events/medbay/double/loop2/0027.jpg"
    pause .1
    "images/events/medbay/double/loop2/0028.jpg"
    pause .1
    "images/events/medbay/double/loop2/0029.jpg"
    pause .1
    "images/events/medbay/double/loop2/0030.jpg"
    function s2
    pause .1
    "images/events/medbay/double/loop2/0031.jpg"
    pause .1
    "images/events/medbay/double/loop2/0032.jpg"
    pause .1
    "images/events/medbay/double/loop2/0033.jpg"
    pause .1
    repeat

image meddp1_loop3:
    "images/events/medbay/double/loop3/0001.jpg"
    pause .1
    "images/events/medbay/double/loop3/0002.jpg"
    pause .1
    "images/events/medbay/double/loop3/0003.jpg"
    pause .1
    "images/events/medbay/double/loop3/0004.jpg"
    function inside
    pause .1
    "images/events/medbay/double/loop3/0005.jpg"
    pause .1
    "images/events/medbay/double/loop3/0006.jpg"
    pause .1
    "images/events/medbay/double/loop3/0007.jpg"
    pause .1
    "images/events/medbay/double/loop3/0008.jpg"
    pause .1
    "images/events/medbay/double/loop3/0009.jpg"
    pause .1
    repeat

image meddp1_loop3alt:
    "images/events/medbay/double/loop3/0001.jpg"
    pause .07
    "images/events/medbay/double/loop3/0002.jpg"
    pause .07
    "images/events/medbay/double/loop3/0003.jpg"
    pause .07
    "images/events/medbay/double/loop3/0004.jpg"
    function inside
    pause .07
    "images/events/medbay/double/loop3/0005.jpg"
    pause .07
    "images/events/medbay/double/loop3/0006.jpg"
    pause .07
    "images/events/medbay/double/loop3/0007.jpg"
    pause .07
    "images/events/medbay/double/loop3/0008.jpg"
    pause .07
    "images/events/medbay/double/loop3/0009.jpg"
    pause .07
    repeat

image meddp1_trans:
    "images/events/medbay/double/trans1/0010.jpg"
    pause .1
    "images/events/medbay/double/trans1/0011.jpg"
    pause .1
    "images/events/medbay/double/trans1/0012.jpg"
    pause .1
    "images/events/medbay/double/trans1/0013.jpg"
    pause .1
    "images/events/medbay/double/trans1/0014.jpg"
    function s2
    pause .1
    "images/events/medbay/double/trans1/0015.jpg"
    pause .1
    "images/events/medbay/double/trans1/0016.jpg"
    pause .1
    "images/events/medbay/double/trans1/0017.jpg"
    pause .1
    "images/events/medbay/double/trans1/0018.jpg"
    pause .1
    "images/events/medbay/double/trans1/0019.jpg"
    pause .1
    "images/events/medbay/double/trans1/0020.jpg"
    pause .1
    "images/events/medbay/double/trans1/0021.jpg"
    pause .1
    "images/events/medbay/double/trans1/0022.jpg"
    function suck4
    pause .1
    "images/events/medbay/double/trans1/0023.jpg"
    pause .1
    "images/events/medbay/double/trans1/0024.jpg"
    pause .1
    "images/events/medbay/double/trans1/0025.jpg"
    pause .1

image meddp1_cum1:
    "images/events/medbay/double/cum1/0025.jpg"
    pause .1
    "images/events/medbay/double/cum1/0026.jpg"
    pause .1
    "images/events/medbay/double/cum1/0027.jpg"
    pause .1
    "images/events/medbay/double/cum1/0028.jpg"
    pause .1
    "images/events/medbay/double/cum1/0029.jpg"
    pause .1
    "images/events/medbay/double/cum1/0030.jpg"
    pause .1
    "images/events/medbay/double/cum1/0031.jpg"
    pause .1
    "images/events/medbay/double/cum1/0032.jpg"
    function suck4
    pause .1
    "images/events/medbay/double/cum1/0033.jpg"
    pause .1
    "images/events/medbay/double/cum1/0034.jpg"
    pause .1
    "images/events/medbay/double/cum1/0035.jpg"
    pause .1
    "images/events/medbay/double/cum1/0036.jpg"
    pause .1
    "images/events/medbay/double/cum1/0037.jpg"
    pause .1
    "images/events/medbay/double/cum1/0038.jpg"
    pause .1
    "images/events/medbay/double/cum1/0039.jpg"
    pause .1
    "images/events/medbay/double/cum1/0040.jpg"
    function cum1
    pause .1
    "images/events/medbay/double/cum1/0041.jpg"
    pause .1
    "images/events/medbay/double/cum1/0042.jpg"
    pause .1
    "images/events/medbay/double/cum1/0043.jpg"
    pause .1
    "images/events/medbay/double/cum1/0044.jpg"
    pause .1
    "images/events/medbay/double/cum1/0045.jpg"
    function wetsquish
    pause .1
    "images/events/medbay/double/cum1/0046.jpg"
    pause .1
    "images/events/medbay/double/cum1/0047.jpg"
    pause .1
    "images/events/medbay/double/cum1/0048.jpg"
    pause .1
    "images/events/medbay/double/cum1/0049.jpg"
    pause .1
    "images/events/medbay/double/cum1/0050.jpg"
    pause .1

image meddp1_cum2:
    "images/events/medbay/double/cum2/0051.jpg"
    pause .1
    "images/events/medbay/double/cum2/0052.jpg"
    function cough
    pause .1
    "images/events/medbay/double/cum2/0053.jpg"
    pause .1
    "images/events/medbay/double/cum2/0054.jpg"
    pause .1
    "images/events/medbay/double/cum2/0055.jpg"
    pause .1
    "images/events/medbay/double/cum2/0056.jpg"
    pause .1
    "images/events/medbay/double/cum2/0057.jpg"
    pause .1
    "images/events/medbay/double/cum2/0058.jpg"
    pause .1
    "images/events/medbay/double/cum2/0059.jpg"
    function splat
    pause .1
    "images/events/medbay/double/cum2/0060.jpg"
    pause .1

image meddp1_cum3:
    "images/events/medbay/double/cum3/0006.jpg"
    pause .1
    "images/events/medbay/double/cum3/0007.jpg"
    pause .1
    "images/events/medbay/double/cum3/0008.jpg"
    pause .1
    "images/events/medbay/double/cum3/0009.jpg"
    pause .1
    "images/events/medbay/double/cum3/0010.jpg"
    pause .1
    "images/events/medbay/double/cum3/0011.jpg"
    pause .1
    "images/events/medbay/double/cum3/0012.jpg"
    pause .1
    "images/events/medbay/double/cum3/0013.jpg"
    pause .1
    "images/events/medbay/double/cum3/0014.jpg"
    pause .1
    "images/events/medbay/double/cum3/0015.jpg"
    pause .1
    "images/events/medbay/double/cum3/0016.jpg"
    function cumsplash
    pause .1
    "images/events/medbay/double/cum3/0017.jpg"
    pause .1
    "images/events/medbay/double/cum3/0018.jpg"
    pause .1
    "images/events/medbay/double/cum3/0019.jpg"
    pause .1
    "images/events/medbay/double/cum3/0020.jpg"
    pause .1
    "images/events/medbay/double/cum3/0021.jpg"
    pause .1
    "images/events/medbay/double/cum3/0022.jpg"
    pause .1
    "images/events/medbay/double/cum3/0023.jpg"
    pause .1

image cockpit1_trans1:
    "images/events/bay1/cockpit/trans1/0001.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0002.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0003.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0004.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0005.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0006.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0007.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0008.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0009.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0010.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0011.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0012.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0013.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0014.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0015.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0016.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0017.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0018.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0019.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0020.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0021.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0022.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0023.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0024.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0025.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0026.jpg"
    pause .1
    "images/events/bay1/cockpit/trans1/0027.jpg"
    pause .1

image cockpit1_loop1:
    "images/events/bay1/cockpit/loop2/0001.jpg"
    pause .1
    "images/events/bay1/cockpit/loop2/0002.jpg"
    pause .1
    "images/events/bay1/cockpit/loop2/0003.jpg"
    pause .1
    "images/events/bay1/cockpit/loop2/0004.jpg"
    pause .1
    "images/events/bay1/cockpit/loop2/0005.jpg"
    pause .1
    "images/events/bay1/cockpit/loop2/0006.jpg"
    pause .1
    "images/events/bay1/cockpit/loop2/0007.jpg"
    pause .1
    "images/events/bay1/cockpit/loop2/0008.jpg"
    pause .1
    "images/events/bay1/cockpit/loop2/0009.jpg"
    pause .1
    repeat

image cockpit1_trans2:
    "images/events/bay1/cockpit/trans2/0001.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0002.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0003.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0004.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0005.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0006.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0007.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0008.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0009.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0010.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0011.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0012.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0013.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0014.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0015.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0016.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0017.jpg"
    pause .1

image cockpit1_trans3:
    "images/events/bay1/cockpit/trans2/0018.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0019.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0020.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0021.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0022.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0023.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0024.jpg"
    function slap1
    pause .1
    "images/events/bay1/cockpit/trans2/0025.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0026.jpg"
    pause .1
    "images/events/bay1/cockpit/trans2/0027.jpg"
    pause .1

image cockpit1_loop2:
    "images/events/bay1/cockpit/loop3/0001.jpg"
    pause .1
    "images/events/bay1/cockpit/loop3/0002.jpg"
    pause .1
    "images/events/bay1/cockpit/loop3/0003.jpg"
    pause .1
    "images/events/bay1/cockpit/loop3/0004.jpg"
    pause .1
    "images/events/bay1/cockpit/loop3/0005.jpg"
    pause .1
    "images/events/bay1/cockpit/loop3/0006.jpg"
    function slap1
    pause .1
    "images/events/bay1/cockpit/loop3/0007.jpg"
    pause .1
    "images/events/bay1/cockpit/loop3/0008.jpg"
    pause .1
    "images/events/bay1/cockpit/loop3/0009.jpg"
    pause .1
    repeat

image cockpit1_loop3:
    "images/events/bay1/cockpit/loop1/1.jpg"
    pause .1
    "images/events/bay1/cockpit/loop1/2.jpg"
    pause .1
    "images/events/bay1/cockpit/loop1/3.jpg"
    pause .1
    "images/events/bay1/cockpit/loop1/4.jpg"
    pause .1
    "images/events/bay1/cockpit/loop1/5.jpg"
    function s1
    pause .1
    "images/events/bay1/cockpit/loop1/6.jpg"
    pause .1
    "images/events/bay1/cockpit/loop1/7.jpg"
    pause .1
    "images/events/bay1/cockpit/loop1/8.jpg"
    pause .1
    "images/events/bay1/cockpit/loop1/9.jpg"
    pause .1
    repeat

image cockpit1_loop4:
    "images/events/bay1/cockpit/loop4/0001.jpg"
    pause .07
    "images/events/bay1/cockpit/loop4/0002.jpg"
    pause .07
    "images/events/bay1/cockpit/loop4/0003.jpg"
    pause .07
    "images/events/bay1/cockpit/loop4/0004.jpg"
    pause .07
    "images/events/bay1/cockpit/loop4/0005.jpg"
    pause .07
    "images/events/bay1/cockpit/loop4/0006.jpg"
    function slap2
    pause .07
    "images/events/bay1/cockpit/loop4/0007.jpg"
    pause .07
    "images/events/bay1/cockpit/loop4/0008.jpg"
    pause .07
    "images/events/bay1/cockpit/loop4/0009.jpg"
    pause .07
    repeat

image cockpit1_cum1:
    "images/events/bay1/cockpit/cum1/0001.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0002.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0003.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0004.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0005.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0006.jpg"
    function slap2
    pause .1
    "images/events/bay1/cockpit/cum1/0007.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0008.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0009.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0010.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0011.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0012.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0013.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0014.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0015.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0016.jpg"
    function splat
    pause .1
    "images/events/bay1/cockpit/cum1/0017.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0018.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0019.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0020.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0021.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0022.jpg"
    function punch
    pause .1
    "images/events/bay1/cockpit/cum1/0023.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0024.jpg"
    pause .1
    "images/events/bay1/cockpit/cum1/0025.jpg"

image cockpit1_cum2:
    "images/events/bay1/cockpit/cum2/0006.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0007.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0008.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0009.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0010.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0011.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0012.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0013.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0014.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0015.jpg"
    function s2
    pause .1
    "images/events/bay1/cockpit/cum2/0016.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0017.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0018.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0019.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0020.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0021.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0022.jpg"
    function cumsplash
    pause .1
    "images/events/bay1/cockpit/cum2/0023.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0024.jpg"
    pause .1
    "images/events/bay1/cockpit/cum2/0025.jpg"

image cageLubeAnal_trans1:
    "images/events/prison/anal/trans1/1.jpg"
    pause .1
    "images/events/prison/anal/trans1/2.jpg"
    pause .1
    "images/events/prison/anal/trans1/3.jpg"
    pause .1
    "images/events/prison/anal/trans1/4.jpg"
    pause .1
    "images/events/prison/anal/trans1/5.jpg"
    pause .1
    "images/events/prison/anal/trans1/6.jpg"
    pause .1
    "images/events/prison/anal/trans1/7.jpg"
    function inside
    pause .1

image cageLubeAnal_trans2:
    "images/events/prison/anal/trans2/1.jpg"
    pause .1
    "images/events/prison/anal/trans2/2.jpg"
    pause .1
    "images/events/prison/anal/trans2/3.jpg"
    pause .1
    "images/events/prison/anal/trans2/4.jpg"
    pause .1
    "images/events/prison/anal/trans2/5.jpg"
    pause .1
    "images/events/prison/anal/trans2/6.jpg"
    pause .1
    "images/events/prison/anal/trans2/7.jpg"
    pause .1
    "images/events/prison/anal/trans2/8.jpg"
    pause .1
    "images/events/prison/anal/trans2/9.jpg"
    function s1
    pause .1
    "images/events/prison/anal/trans2/10.jpg"
    pause .1
    "images/events/prison/anal/trans2/11.jpg"
    pause .1
    "images/events/prison/anal/trans2/12.jpg"
    pause .1
    "images/events/prison/anal/trans2/13.jpg"
    pause .1
    "images/events/prison/anal/trans2/14.jpg"
    pause .1
    "images/events/prison/anal/trans2/15.jpg"
    pause .1
    "images/events/prison/anal/trans2/16.jpg"
    pause .1
    "images/events/prison/anal/trans2/17.jpg"
    pause .1
    "images/events/prison/anal/trans2/18.jpg"
    pause .1
    "images/events/prison/anal/trans2/19.jpg"
    function splat
    pause .1
    "images/events/prison/anal/trans2/20.jpg"
    pause .1

image cageLubeAnal_loop1:
    "images/events/prison/anal/loop1/1.jpg"
    pause .1
    "images/events/prison/anal/loop1/2.jpg"
    pause .1
    "images/events/prison/anal/loop1/3.jpg"
    pause .1
    "images/events/prison/anal/loop1/4.jpg"
    function s4
    pause .1
    "images/events/prison/anal/loop1/5.jpg"
    pause .1
    "images/events/prison/anal/loop1/6.jpg"
    function fart2
    pause .1
    "images/events/prison/anal/loop1/7.jpg"
    pause .1
    "images/events/prison/anal/loop1/8.jpg"
    pause .1
    "images/events/prison/anal/loop1/9.jpg"
    pause .1
    "images/events/prison/anal/loop1/10.jpg"
    function s4
    pause .1
    "images/events/prison/anal/loop1/11.jpg"
    pause .1
    "images/events/prison/anal/loop1/12.jpg"
    pause .1
    "images/events/prison/anal/loop1/13.jpg"
    pause .1
    "images/events/prison/anal/loop1/14.jpg"
    function s2
    pause .1
    "images/events/prison/anal/loop1/15.jpg"
    pause .1
    "images/events/prison/anal/loop1/16.jpg"
    pause .1
    "images/events/prison/anal/loop1/17.jpg"
    pause .1
    "images/events/prison/anal/loop1/18.jpg"
    pause .1
    "images/events/prison/anal/loop1/19.jpg"
    pause .1
    "images/events/prison/anal/loop1/20.jpg"
    function s3
    pause .1
    repeat

image cageLubeAnal_loop2:
    "images/events/prison/anal/loop2/1.jpg"
    pause .1
    "images/events/prison/anal/loop2/2.jpg"
    pause .1
    "images/events/prison/anal/loop2/3.jpg"
    pause .1
    "images/events/prison/anal/loop2/4.jpg"
    pause .1
    "images/events/prison/anal/loop2/5.jpg"
    pause .1
    "images/events/prison/anal/loop2/6.jpg"
    function slap5
    pause .1
    "images/events/prison/anal/loop2/7.jpg"
    pause .1
    "images/events/prison/anal/loop2/8.jpg"
    pause .1
    "images/events/prison/anal/loop2/9.jpg"
    pause .1
    repeat

image cageLubeAnal_cum:
    "images/events/prison/anal/cum/1.jpg"
    pause .1
    "images/events/prison/anal/cum/2.jpg"
    pause .1
    "images/events/prison/anal/cum/3.jpg"
    pause .1
    "images/events/prison/anal/cum/4.jpg"
    pause .1
    "images/events/prison/anal/cum/5.jpg"
    pause .1
    "images/events/prison/anal/cum/6.jpg"
    pause .1
    "images/events/prison/anal/cum/7.jpg"
    pause .1
    "images/events/prison/anal/cum/8.jpg"
    pause .1
    "images/events/prison/anal/cum/9.jpg"
    pause .1
    "images/events/prison/anal/cum/10.jpg"
    pause .1
    "images/events/prison/anal/cum/11.jpg"
    pause .1
    "images/events/prison/anal/cum/12.jpg"
    pause .1
    "images/events/prison/anal/cum/13.jpg"
    pause .1
    "images/events/prison/anal/cum/14.jpg"
    pause .1
    "images/events/prison/anal/cum/15.jpg"
    pause .1
    "images/events/prison/anal/cum/16.jpg"
    pause .1
    "images/events/prison/anal/cum/17.jpg"
    pause .1
    "images/events/prison/anal/cum/18.jpg"
    function fart
    pause .1
    "images/events/prison/anal/cum/19.jpg"
    pause .1
    "images/events/prison/anal/cum/20.jpg"
    pause .1
    "images/events/prison/anal/cum/21.jpg"
    pause .1
    "images/events/prison/anal/cum/22.jpg"
    pause .1
    "images/events/prison/anal/cum/23.jpg"
    pause .1
    "images/events/prison/anal/cum/24.jpg"
    pause .1
    "images/events/prison/anal/cum/25.jpg"
    function splat
    pause .1

image medvar1_loop1:
    "images/events/medbay/varrens/loop2/0060.jpg"
    pause .1
    "images/events/medbay/varrens/loop2/0061.jpg"
    pause .1
    "images/events/medbay/varrens/loop2/0062.jpg"
    pause .1
    "images/events/medbay/varrens/loop2/0063.jpg"
    pause .1
    "images/events/medbay/varrens/loop2/0064.jpg"
    pause .1
    "images/events/medbay/varrens/loop2/0065.jpg"
    function s1
    pause .1
    "images/events/medbay/varrens/loop2/0066.jpg"
    pause .1
    "images/events/medbay/varrens/loop2/0067.jpg"
    pause .1
    repeat

image medvar1_loop2:
    "images/events/medbay/varrens/loop1/0060.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0061.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0062.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0063.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0064.jpg"
    function slap3
    pause .1
    "images/events/medbay/varrens/loop1/0065.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0066.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0067.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0068.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0069.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0070.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0071.jpg"
    function slap3
    pause .1
    "images/events/medbay/varrens/loop1/0072.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0073.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0074.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0075.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0076.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0077.jpg"
    function slap3
    pause .1
    "images/events/medbay/varrens/loop1/0078.jpg"
    pause .1
    "images/events/medbay/varrens/loop1/0079.jpg"
    function s2
    pause .1
    "images/events/medbay/varrens/loop1/0080.jpg"
    pause .1
    repeat

image medvar1_loop3:
    "images/events/medbay/varrens/loop3/0060.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0061.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0062.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0063.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0064.jpg"
    function slap1
    pause .1
    "images/events/medbay/varrens/loop3/0065.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0066.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0067.jpg"
    function suck1
    pause .1
    "images/events/medbay/varrens/loop3/0068.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0069.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0070.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0071.jpg"
    function slap4
    pause .1
    "images/events/medbay/varrens/loop3/0072.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0073.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0074.jpg"
    function suck2
    pause .1
    "images/events/medbay/varrens/loop3/0075.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0076.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0077.jpg"
    function slap6
    pause .1
    "images/events/medbay/varrens/loop3/0078.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0079.jpg"
    pause .1
    "images/events/medbay/varrens/loop3/0080.jpg"
    pause .1
    repeat

image medvar1_loop4:
    "images/events/medbay/varrens/loop4/1.jpg"
    pause .1
    "images/events/medbay/varrens/loop4/2.jpg"
    pause .1
    "images/events/medbay/varrens/loop4/3.jpg"
    function slap1
    pause .1
    "images/events/medbay/varrens/loop4/4.jpg"
    pause .1
    "images/events/medbay/varrens/loop4/5.jpg"
    function s2
    pause .1
    "images/events/medbay/varrens/loop4/6.jpg"
    pause .1
    repeat

image medvar1_trans:
    "images/events/medbay/varrens/trans1/0060.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0061.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0062.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0063.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0064.jpg"
    function slap3
    pause .1
    "images/events/medbay/varrens/trans1/0065.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0066.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0067.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0068.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0069.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0070.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0071.jpg"
    function slap2
    pause .1
    "images/events/medbay/varrens/trans1/0072.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0073.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0074.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0075.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0076.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0077.jpg"
    function slap8
    pause .1
    "images/events/medbay/varrens/trans1/0078.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0079.jpg"
    pause .1
    "images/events/medbay/varrens/trans1/0080.jpg"
    function suck4
    pause .1

image medvar1_cum1:
    "images/events/medbay/varrens/cum1/0081.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0082.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0083.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0084.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0085.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0086.jpg"
    function suck4
    pause .15
    "images/events/medbay/varrens/cum1/0087.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0088.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0089.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0090.jpg"
    function wetsquish
    pause .15
    "images/events/medbay/varrens/cum1/0091.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0092.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0093.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0094.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0095.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0096.jpg"
    function suck1
    pause .15
    "images/events/medbay/varrens/cum1/0097.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0098.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0099.jpg"
    pause .15
    "images/events/medbay/varrens/cum1/0100.jpg"
    function swallow
    pause .15

image medvar1_cum2:
    "images/events/medbay/varrens/cum2/1.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/2.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/3.jpg"
    function slap8
    pause .15
    "images/events/medbay/varrens/cum2/4.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/5.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/6.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/7.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/8.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/9.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/10.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/11.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/12.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/13.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/14.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/15.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/16.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/17.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/18.jpg"
    function fart2
    pause .15
    "images/events/medbay/varrens/cum2/19.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/20.jpg"
    pause .15
    "images/events/medbay/varrens/cum2/21.jpg"
    function cum1
    pause .15

image omnimed:
    "images/events/medbay/varrens/omni/1.png"
    pause .15
    "images/events/medbay/varrens/omni/2.png"
    pause .15
    "images/events/medbay/varrens/omni/3.png"
    pause .15
    "images/events/medbay/varrens/omni/4.png"
    pause .15
    "images/events/medbay/varrens/omni/5.png"
    pause .15

image frontmask1:
    "images/events/w1/front/mask1/0001.png"
    pause 0.15
    "images/events/w1/front/mask1/0002.png"
    pause 0.15
    "images/events/w1/front/mask1/0003.png"
    pause 0.15
    "images/events/w1/front/mask1/0004.png"
    function s3
    pause 0.15
    "images/events/w1/front/mask1/0005.png"
    pause 0.15
    "images/events/w1/front/mask1/0006.png"
    pause 0.15
    "images/events/w1/front/mask1/0007.png"
    pause 0.15
    "images/events/w1/front/mask1/0008.png"
    pause 0.15
    "images/events/w1/front/mask1/0009.png"
    pause 0.15
    "images/events/w1/front/mask1/0010.png"
    pause 0.15
    repeat

image frontmask2:
    "images/events/w1/front/mask2/0001.png"
    pause 0.15
    "images/events/w1/front/mask2/0002.png"
    pause 0.15
    "images/events/w1/front/mask2/0003.png"
    pause 0.15
    "images/events/w1/front/mask2/0004.png"
    function inside
    pause 0.15
    "images/events/w1/front/mask2/0005.png"
    pause 0.15
    "images/events/w1/front/mask2/0006.png"
    pause 0.15
    "images/events/w1/front/mask2/0007.png"
    pause 0.15
    repeat

image frontmaskcum:
    "images/events/w1/front/maskcum/0001.png"
    pause 0.15
    "images/events/w1/front/maskcum/0002.png"
    pause 0.15
    "images/events/w1/front/maskcum/0003.png"
    pause 0.15
    "images/events/w1/front/maskcum/0004.png"
    pause 0.15
    "images/events/w1/front/maskcum/0005.png"
    pause 0.15
    "images/events/w1/front/maskcum/0006.png"
    function cum1
    pause 0.15
    "images/events/w1/front/maskcum/0007.png"
    pause 0.15
    "images/events/w1/front/maskcum/0008.png"
    pause 0.15
    "images/events/w1/front/maskcum/0009.png"
    pause 0.15
    "images/events/w1/front/maskcum/0010.png"
    pause 0.15
    "images/events/w1/front/maskcum/0011.png"
    pause 0.15
    "images/events/w1/front/maskcum/0012.png"
    pause 0.15
    "images/events/w1/front/maskcum/0013.png"
    pause 0.15
    "images/events/w1/front/maskcum/0014.png"
    pause 0.15
    "images/events/w1/front/maskcum/0015.png"
    function cum1
    pause 0.15
    "images/events/w1/front/maskcum/0016.png"
    pause 0.15
    "images/events/w1/front/maskcum/0017.png"
    pause 0.15
    "images/events/w1/front/maskcum/0018.png"
    pause 0.15
    "images/events/w1/front/maskcum/0019.png"
    pause 0.15
    "images/events/w1/front/maskcum/0020.png"
    pause 0.15
    "images/events/w1/front/maskcum/0021.png"
    pause 0.15
    "images/events/w1/front/maskcum/0022.png"
    pause 0.15

image frontnomask1:
    "images/events/w1/front/nomask1/0001.png"
    pause 0.15
    "images/events/w1/front/nomask1/0002.png"
    pause 0.15
    "images/events/w1/front/nomask1/0003.png"
    pause 0.15
    "images/events/w1/front/nomask1/0004.png"
    function s3
    pause 0.15
    "images/events/w1/front/nomask1/0005.png"
    pause 0.15
    "images/events/w1/front/nomask1/0006.png"
    pause 0.15
    "images/events/w1/front/nomask1/0007.png"
    pause 0.15
    "images/events/w1/front/nomask1/0008.png"
    pause 0.15
    "images/events/w1/front/nomask1/0009.png"
    pause 0.15
    "images/events/w1/front/nomask1/0010.png"
    pause 0.15
    repeat

image frontnomask2:
    "images/events/w1/front/nomask2/0001.png"
    pause 0.15
    "images/events/w1/front/nomask2/0002.png"
    pause 0.15
    "images/events/w1/front/nomask2/0003.png"
    pause 0.15
    "images/events/w1/front/nomask2/0004.png"
    pause 0.15
    "images/events/w1/front/nomask2/0005.png"
    pause 0.15
    "images/events/w1/front/nomask2/0006.png"
    function suck1
    pause 0.15
    "images/events/w1/front/nomask2/0007.png"
    pause 0.15
    "images/events/w1/front/nomask2/0008.png"
    pause 0.15
    "images/events/w1/front/nomask2/0009.png"
    pause 0.15
    repeat

image frontnomaskcum:
    "images/events/w1/front/nomaskcum/0001.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0002.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0003.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0004.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0005.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0006.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0007.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0008.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0009.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0010.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0011.png"
    function cum1
    pause 0.15
    "images/events/w1/front/nomaskcum/0012.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0013.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0014.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0015.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0016.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0017.png"
    function cum1
    pause 0.15
    "images/events/w1/front/nomaskcum/0018.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0019.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0020.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0021.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0022.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0023.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0024.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0025.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0026.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0027.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0028.png"
    function s2
    pause 0.15
    "images/events/w1/front/nomaskcum/0029.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0030.png"
    pause 0.15
    "images/events/w1/front/nomaskcum/0031.png"
    pause 0.15

image frontdamaged1:
    "images/events/w1/front/damaged1/0001.png"
    pause 0.15
    "images/events/w1/front/damaged1/0002.png"
    pause 0.15
    "images/events/w1/front/damaged1/0003.png"
    pause 0.15
    "images/events/w1/front/damaged1/0004.png"
    pause 0.15
    "images/events/w1/front/damaged1/0005.png"
    pause 0.15
    "images/events/w1/front/damaged1/0006.png"
    function suck1
    pause 0.15
    "images/events/w1/front/damaged1/0007.png"
    pause 0.15
    "images/events/w1/front/damaged1/0008.png"
    pause 0.15
    "images/events/w1/front/damaged1/0009.png"
    pause 0.15
    repeat

image frontdamaged2:
    "images/events/w1/front/damaged1/0001.png"
    pause 0.07
    "images/events/w1/front/damaged1/0002.png"
    pause 0.07
    "images/events/w1/front/damaged1/0003.png"
    pause 0.07
    "images/events/w1/front/damaged1/0004.png"
    pause 0.07
    "images/events/w1/front/damaged1/0005.png"
    pause 0.07
    "images/events/w1/front/damaged1/0006.png"
    function suck2
    pause 0.07
    "images/events/w1/front/damaged1/0007.png"
    pause 0.07
    "images/events/w1/front/damaged1/0008.png"
    pause 0.07
    "images/events/w1/front/damaged1/0009.png"
    pause 0.07
    repeat

image frontdamagedcum:
    "images/events/w1/front/damagedcum/0001.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0002.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0003.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0004.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0005.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0006.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0007.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0008.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0009.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0010.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0011.png"
    function cum1
    pause 0.15
    "images/events/w1/front/damagedcum/0012.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0013.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0014.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0015.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0016.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0017.png"
    function cum1
    pause 0.15
    "images/events/w1/front/damagedcum/0018.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0019.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0020.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0021.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0022.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0023.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0024.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0025.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0026.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0027.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0028.png"
    function s2
    pause 0.15
    "images/events/w1/front/damagedcum/0029.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0030.png"
    pause 0.15
    "images/events/w1/front/damagedcum/0031.png"
    pause 0.15

image backmask1:
    "images/events/w1/back/mask1/0001.png"
    pause 0.15
    "images/events/w1/back/mask1/0002.png"
    pause 0.15
    "images/events/w1/back/mask1/0003.png"
    pause 0.15
    "images/events/w1/back/mask1/0004.png"
    pause 0.15
    "images/events/w1/back/mask1/0005.png"
    pause 0.15
    "images/events/w1/back/mask1/0006.png"
    function slap0
    pause 0.15
    "images/events/w1/back/mask1/0007.png"
    pause 0.15
    "images/events/w1/back/mask1/0008.png"
    pause 0.15
    "images/events/w1/back/mask1/0009.png"
    pause 0.15
    "images/events/w1/back/mask1/0010.png"
    pause 0.15
    repeat

image backmask2:
    "images/events/w1/back/mask2/0001.png"
    pause 0.15
    "images/events/w1/back/mask2/0002.png"
    pause 0.15
    "images/events/w1/back/mask2/0003.png"
    pause 0.15
    "images/events/w1/back/mask2/0004.png"
    pause 0.15
    "images/events/w1/back/mask2/0005.png"
    pause 0.15
    "images/events/w1/back/mask2/0006.png"
    function inside
    pause 0.15
    "images/events/w1/back/mask2/0007.png"
    pause 0.15
    "images/events/w1/back/mask2/0008.png"
    pause 0.15
    "images/events/w1/back/mask2/0009.png"
    pause 0.15
    "images/events/w1/back/mask2/0010.png"
    pause 0.15
    repeat

image backmaskcum:
    "images/events/w1/back/maskcum/0001.png"
    pause 0.15
    "images/events/w1/back/maskcum/0002.png"
    pause 0.15
    "images/events/w1/back/maskcum/0003.png"
    pause 0.15
    "images/events/w1/back/maskcum/0004.png"
    pause 0.15
    "images/events/w1/back/maskcum/0005.png"
    function cum1
    pause 0.15
    "images/events/w1/back/maskcum/0006.png"
    pause 0.15
    "images/events/w1/back/maskcum/0007.png"
    pause 0.15
    "images/events/w1/back/maskcum/0008.png"
    pause 0.15
    "images/events/w1/back/maskcum/0009.png"
    pause 0.15
    "images/events/w1/back/maskcum/0010.png"
    pause 0.15
    "images/events/w1/back/maskcum/0011.png"
    pause 0.15
    "images/events/w1/back/maskcum/0012.png"
    pause 0.15
    "images/events/w1/back/maskcum/0013.png"
    pause 0.15
    "images/events/w1/back/maskcum/0014.png"
    pause 0.15
    "images/events/w1/back/maskcum/0015.png"
    function cum1
    pause 0.15
    "images/events/w1/back/maskcum/0016.png"
    pause 0.15
    "images/events/w1/back/maskcum/0017.png"
    pause 0.15
    "images/events/w1/back/maskcum/0018.png"
    pause 0.15
    "images/events/w1/back/maskcum/0019.png"
    pause 0.15
    "images/events/w1/back/maskcum/0020.png"
    pause 0.15
    "images/events/w1/back/maskcum/0021.png"
    pause 0.15

image backdamaged1:
    "images/events/w1/back/damaged1/0001.png"
    pause 0.15
    "images/events/w1/back/damaged1/0002.png"
    pause 0.15
    "images/events/w1/back/damaged1/0003.png"
    pause 0.15
    "images/events/w1/back/damaged1/0004.png"
    pause 0.15
    "images/events/w1/back/damaged1/0005.png"
    function slosh
    pause 0.15
    "images/events/w1/back/damaged1/0006.png"
    pause 0.15
    "images/events/w1/back/damaged1/0007.png"
    pause 0.15
    "images/events/w1/back/damaged1/0008.png"
    pause 0.15
    "images/events/w1/back/damaged1/0009.png"
    function slap9
    pause 0.15
    "images/events/w1/back/damaged1/0010.png"
    pause 0.15
    "images/events/w1/back/damaged1/0011.png"
    pause 0.15
    "images/events/w1/back/damaged1/0012.png"
    pause 0.15

image backdamaged2:
    "images/events/w1/back/damaged2/0007.png"
    pause 0.15
    "images/events/w1/back/damaged2/0008.png"
    pause 0.15
    "images/events/w1/back/damaged2/0009.png"
    function slap3
    pause 0.15
    "images/events/w1/back/damaged2/0010.png"
    pause 0.15
    "images/events/w1/back/damaged2/0011.png"
    pause 0.15
    repeat

image backdamaged3:
    "images/events/w1/back/damaged2/0007.png"
    pause 0.07
    "images/events/w1/back/damaged2/0008.png"
    pause 0.07
    "images/events/w1/back/damaged2/0009.png"
    function slap8
    pause 0.07
    "images/events/w1/back/damaged2/0010.png"
    pause 0.07
    "images/events/w1/back/damaged2/0011.png"
    pause 0.07
    repeat

image backdamagedcum:
    "images/events/w1/back/damagedcum/0007.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0008.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0009.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0010.png"
    function cum1
    pause 0.15
    "images/events/w1/back/damagedcum/0011.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0012.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0013.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0014.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0015.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0016.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0017.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0018.png"
    pause 0.15
    "images/events/w1/back/damagedcum/0019.png"
    function cum1
    pause 0.15

image sex1:
    "images/events/w2/front/mask1/0001.png"
    pause 0.15
    "images/events/w2/front/mask1/0002.png"
    pause 0.15
    "images/events/w2/front/mask1/0003.png"
    pause 0.15
    "images/events/w2/front/mask1/0004.png"
    pause 0.15
    "images/events/w2/front/mask1/0005.png"
    function inside
    pause 0.15
    "images/events/w2/front/mask1/0006.png"
    pause 0.15
    "images/events/w2/front/mask1/0007.png"
    pause 0.15
    "images/events/w2/front/mask1/0008.png"
    pause 0.15
    "images/events/w2/front/mask1/0009.png"
    pause 0.15
    repeat

image sex2:
    "images/events/w2/front/mask2/0001.png"
    pause 0.15
    "images/events/w2/front/mask2/0002.png"
    pause 0.15
    "images/events/w2/front/mask2/0003.png"
    pause 0.15
    "images/events/w2/front/mask2/0004.png"
    function inside
    pause 0.15
    "images/events/w2/front/mask2/0005.png"
    pause 0.15
    "images/events/w2/front/mask2/0006.png"
    pause 0.15
    "images/events/w2/front/mask2/0007.png"
    pause 0.15
    "images/events/w2/front/mask2/0008.png"
    pause 0.15
    "images/events/w2/front/mask2/0009.png"
    pause 0.15
    repeat

image cum1:
    "images/events/w2/front/maskcum/0001.png"
    pause 0.15
    "images/events/w2/front/maskcum/0002.png"
    pause 0.15
    "images/events/w2/front/maskcum/0003.png"
    pause 0.15
    "images/events/w2/front/maskcum/0004.png"
    pause 0.15
    "images/events/w2/front/maskcum/0005.png"
    function cum1
    pause 0.15
    "images/events/w2/front/maskcum/0006.png"
    pause 0.15
    "images/events/w2/front/maskcum/0007.png"
    pause 0.15
    "images/events/w2/front/maskcum/0008.png"
    pause 0.15
    "images/events/w2/front/maskcum/0009.png"
    function cum2
    pause 0.15
    "images/events/w2/front/maskcum/0010.png"
    pause 0.15
    "images/events/w2/front/maskcum/0011.png"
    pause 0.15
    "images/events/w2/front/maskcum/0012.png"
    pause 0.15
    "images/events/w2/front/maskcum/0013.png"
    pause 0.15
    "images/events/w2/front/maskcum/0014.png"
    function cum1
    pause 0.15
    "images/events/w2/front/maskcum/0015.png"
    pause 0.15
    "images/events/w2/front/maskcum/0016.png"
    pause 0.15
    "images/events/w2/front/maskcum/0017.png"
    pause 0.15
    "images/events/w2/front/maskcum/0018.png"
    pause 0.15
    "images/events/w2/front/maskcum/0019.png"

image sex3:
    "images/events/w2/front/nomask1/0001.png"
    pause 0.15
    "images/events/w2/front/nomask1/0002.png"
    pause 0.15
    "images/events/w2/front/nomask1/0003.png"
    pause 0.15
    "images/events/w2/front/nomask1/0004.png"
    pause 0.15
    "images/events/w2/front/nomask1/0005.png"
    function inside
    pause 0.15
    "images/events/w2/front/nomask1/0006.png"
    pause 0.15
    "images/events/w2/front/nomask1/0007.png"
    pause 0.15
    "images/events/w2/front/nomask1/0008.png"
    pause 0.15
    "images/events/w2/front/nomask1/0009.png"
    pause 0.15
    repeat

image sex3alt:
    "images/events/w2/front/nomask1/0001.png"
    pause 0.07
    "images/events/w2/front/nomask1/0002.png"
    pause 0.07
    "images/events/w2/front/nomask1/0003.png"
    pause 0.07
    "images/events/w2/front/nomask1/0004.png"
    pause 0.07
    "images/events/w2/front/nomask1/0005.png"
    function inside
    pause 0.07
    "images/events/w2/front/nomask1/0006.png"
    pause 0.07
    "images/events/w2/front/nomask1/0007.png"
    pause 0.07
    "images/events/w2/front/nomask1/0008.png"
    pause 0.07
    "images/events/w2/front/nomask1/0009.png"
    pause 0.07
    repeat

image sex4:
    "images/events/w2/front/nomask2/0001.png"
    pause 0.15
    "images/events/w2/front/nomask2/0002.png"
    pause 0.15
    "images/events/w2/front/nomask2/0003.png"
    pause 0.15
    "images/events/w2/front/nomask2/0004.png"
    pause 0.15
    "images/events/w2/front/nomask2/0005.png"
    function s2
    pause 0.15
    "images/events/w2/front/nomask2/0006.png"
    pause 0.15
    "images/events/w2/front/nomask2/0007.png"
    pause 0.15
    "images/events/w2/front/nomask2/0008.png"
    pause 0.15
    "images/events/w2/front/nomask2/0009.png"
    pause 0.15
    repeat

image sex4alt:
    "images/events/w2/front/nomask2/0001.png"
    pause 0.07
    "images/events/w2/front/nomask2/0002.png"
    pause 0.07
    "images/events/w2/front/nomask2/0003.png"
    pause 0.07
    "images/events/w2/front/nomask2/0004.png"
    function s4
    pause 0.07
    "images/events/w2/front/nomask2/0005.png"
    pause 0.07
    "images/events/w2/front/nomask2/0006.png"
    pause 0.07
    "images/events/w2/front/nomask2/0007.png"
    pause 0.07
    "images/events/w2/front/nomask2/0008.png"
    pause 0.07
    "images/events/w2/front/nomask2/0009.png"
    pause 0.07
    repeat

image sex5:
    "images/events/w2/front/nomask3/0001.png"
    pause 0.15
    "images/events/w2/front/nomask3/0002.png"
    pause 0.15
    "images/events/w2/front/nomask3/0003.png"
    pause 0.15
    "images/events/w2/front/nomask3/0004.png"
    pause 0.15
    "images/events/w2/front/nomask3/0005.png"
    pause 0.15
    "images/events/w2/front/nomask3/0006.png"
    pause 0.15
    "images/events/w2/front/nomask3/0007.png"
    pause 0.15
    "images/events/w2/front/nomask3/0008.png"
    pause 0.15
    "images/events/w2/front/nomask3/0009.png"
    function choke3
    pause 0.15
    "images/events/w2/front/nomask3/0010.png"
    pause 0.15
    "images/events/w2/front/nomask3/0011.png"
    pause 0.15
    "images/events/w2/front/nomask3/0012.png"
    pause 0.15
    "images/events/w2/front/nomask3/0013.png"
    pause 0.15
    "images/events/w2/front/nomask3/0014.png"
    function suck4
    pause 0.15
    "images/events/w2/front/nomask3/0015.png"
    pause 0.15
    "images/events/w2/front/nomask3/0016.png"
    pause 0.15
    "images/events/w2/front/nomask3/0017.png"
    pause 0.15

image sex6:
    "images/events/w2/front/nomask4/0005.png"
    function slurp
    pause 0.15
    "images/events/w2/front/nomask4/0006.png"
    pause 0.15
    "images/events/w2/front/nomask4/0007.png"
    pause 0.15
    "images/events/w2/front/nomask4/0008.png"
    pause 0.15
    "images/events/w2/front/nomask4/0009.png"
    pause 0.15
    "images/events/w2/front/nomask4/0010.png"
    pause 0.15
    "images/events/w2/front/nomask4/0011.png"
    pause 0.15
    "images/events/w2/front/nomask4/0012.png"
    pause 0.15
    "images/events/w2/front/nomask4/0013.png"
    pause 0.15
    repeat

image sex6alt:
    "images/events/w2/front/nomask4/0005.png"
    pause 0.07
    "images/events/w2/front/nomask4/0006.png"
    pause 0.07
    "images/events/w2/front/nomask4/0007.png"
    pause 0.07
    "images/events/w2/front/nomask4/0008.png"
    pause 0.07
    "images/events/w2/front/nomask4/0009.png"
    pause 0.07
    "images/events/w2/front/nomask4/0010.png"
    function suck1
    pause 0.07
    "images/events/w2/front/nomask4/0011.png"
    pause 0.07
    "images/events/w2/front/nomask4/0012.png"
    pause 0.07
    "images/events/w2/front/nomask4/0013.png"
    pause 0.07
    repeat

image cum2:
    "images/events/w2/front/nomaskcum2/0001.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0002.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0003.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0004.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0005.png"
    function cum1
    pause 0.15
    "images/events/w2/front/nomaskcum2/0006.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0007.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0008.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0009.png"
    function cum2
    pause 0.15
    "images/events/w2/front/nomaskcum2/0010.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0011.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0012.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0013.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0014.png"
    function cum1
    pause 0.15
    "images/events/w2/front/nomaskcum2/0015.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0016.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0017.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0018.png"
    pause 0.15
    "images/events/w2/front/nomaskcum2/0019.png"

image cum3:
    "images/events/w2/front/nomaskcum1/0005.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0006.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0007.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0008.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0009.png"
    function cum1
    pause 0.15
    "images/events/w2/front/nomaskcum1/0010.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0011.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0012.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0013.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0014.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0015.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0016.png"
    function cum1
    pause 0.15
    "images/events/w2/front/nomaskcum1/0017.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0018.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0019.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0020.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0021.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0022.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0023.png"
    function swallow
    pause 0.15
    "images/events/w2/front/nomaskcum1/0024.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0025.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0026.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0027.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0028.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0029.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0030.png"
    function slurp
    pause 0.15
    "images/events/w2/front/nomaskcum1/0031.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0032.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0033.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0034.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0035.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0036.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0037.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0038.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0039.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0040.png"
    pause 0.15
    "images/events/w2/front/nomaskcum1/0041.png"

image sex7:
    "images/events/v2/mask1/0001.png"
    pause 0.15
    "images/events/v2/mask1/0002.png"
    pause 0.15
    "images/events/v2/mask1/0003.png"
    pause 0.15
    "images/events/v2/mask1/0004.png"
    pause 0.15
    "images/events/v2/mask1/0005.png"
    pause 0.15
    "images/events/v2/mask1/0006.png"
    function inside
    pause 0.15
    "images/events/v2/mask1/0007.png"
    pause 0.15
    "images/events/v2/mask1/0008.png"
    pause 0.15
    "images/events/v2/mask1/0009.png"
    pause 0.15
    repeat

image sex8:
    "images/events/v2/mask2/0001.png"
    pause 0.15
    "images/events/v2/mask2/0002.png"
    pause 0.15
    "images/events/v2/mask2/0003.png"
    pause 0.15
    "images/events/v2/mask2/0004.png"
    pause 0.15
    "images/events/v2/mask2/0005.png"
    pause 0.15
    "images/events/v2/mask2/0006.png"
    function inside
    pause 0.15
    "images/events/v2/mask2/0007.png"
    pause 0.15
    "images/events/v2/mask2/0008.png"
    pause 0.15
    "images/events/v2/mask2/0009.png"
    pause 0.15
    repeat

image cum4:
    "images/events/v2/maskcum1/0001.png"
    pause 0.15
    "images/events/v2/maskcum1/0002.png"
    pause 0.15
    "images/events/v2/maskcum1/0003.png"
    pause 0.15
    "images/events/v2/maskcum1/0004.png"
    function cum1
    pause 0.15
    "images/events/v2/maskcum1/0005.png"
    pause 0.15
    "images/events/v2/maskcum1/0006.png"
    pause 0.15
    "images/events/v2/maskcum1/0007.png"
    pause 0.15
    "images/events/v2/maskcum1/0008.png"
    pause 0.15
    "images/events/v2/maskcum1/0009.png"
    function cum1
    pause 0.15
    "images/events/v2/maskcum1/0010.png"
    pause 0.15
    "images/events/v2/maskcum1/0011.png"
    pause 0.15
    "images/events/v2/maskcum1/0012.png"
    pause 0.15
    "images/events/v2/maskcum1/0013.png"
    pause 0.15
    "images/events/v2/maskcum1/0014.png"
    pause 0.15
    "images/events/v2/maskcum1/0015.png"
    pause 0.15
    "images/events/v2/maskcum1/0016.png"
    pause 0.15
    "images/events/v2/maskcum1/0017.png"
    pause 0.15
    "images/events/v2/maskcum1/0018.png"
    pause 0.15
    "images/events/v2/maskcum1/0019.png"
    pause 0.15
    "images/events/v2/maskcum1/0020.png"
    pause 0.15

image sex9:
    "images/events/v2/nomask1/0001.png"
    pause 0.15
    "images/events/v2/nomask1/0002.png"
    pause 0.15
    "images/events/v2/nomask1/0003.png"
    pause 0.15
    "images/events/v2/nomask1/0004.png"
    pause 0.15
    "images/events/v2/nomask1/0005.png"
    pause 0.15
    "images/events/v2/nomask1/0006.png"
    function inside
    pause 0.15
    "images/events/v2/nomask1/0007.png"
    pause 0.15
    "images/events/v2/nomask1/0008.png"
    pause 0.15
    "images/events/v2/nomask1/0009.png"
    pause 0.15
    repeat

image sex10:
    "images/events/v2/nomask2/0001.png"
    pause 0.15
    "images/events/v2/nomask2/0002.png"
    pause 0.15
    "images/events/v2/nomask2/0003.png"
    pause 0.15
    "images/events/v2/nomask2/0004.png"
    pause 0.15
    "images/events/v2/nomask2/0005.png"
    function lick
    pause 0.15
    "images/events/v2/nomask2/0006.png"
    pause 0.15
    "images/events/v2/nomask2/0007.png"
    pause 0.15
    "images/events/v2/nomask2/0008.png"
    pause 0.15
    "images/events/v2/nomask2/0009.png"
    pause 0.15
    repeat

image sex11:
    "images/events/v2/nomask3/0001.png"
    pause 0.15
    "images/events/v2/nomask3/0002.png"
    pause 0.15
    "images/events/v2/nomask3/0003.png"
    pause 0.15
    "images/events/v2/nomask3/0004.png"
    pause 0.15
    "images/events/v2/nomask3/0005.png"
    pause 0.15
    "images/events/v2/nomask3/0006.png"
    function suck4
    pause 0.15
    "images/events/v2/nomask3/0007.png"
    pause 0.15
    "images/events/v2/nomask3/0008.png"
    pause 0.15
    "images/events/v2/nomask3/0009.png"
    pause 0.15
    repeat

image cum5:
    "images/events/v2/nomaskcum1/0001.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0002.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0003.png"
    function cum1
    pause 0.15
    "images/events/v2/nomaskcum1/0004.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0005.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0006.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0007.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0008.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0009.png"
    function cum1
    pause 0.15
    "images/events/v2/nomaskcum1/0010.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0011.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0012.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0013.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0014.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0015.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0016.png"
    function splat
    pause 0.15
    "images/events/v2/nomaskcum1/0017.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0018.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0019.png"
    pause 0.15
    "images/events/v2/nomaskcum1/0020.png"
    pause 0.15

image cum6:
    "images/events/v2/nomaskcum2/0001.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0002.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0003.png"
    function s2
    pause 0.15
    "images/events/v2/nomaskcum2/0004.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0005.png"
    function cum1
    pause 0.15
    "images/events/v2/nomaskcum2/0006.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0007.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0008.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0009.png"
    function cum1
    pause 0.15
    "images/events/v2/nomaskcum2/0010.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0011.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0012.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0013.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0014.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0015.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0016.png"
    function splat
    pause 0.15
    "images/events/v2/nomaskcum2/0017.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0018.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0019.png"
    pause 0.15
    "images/events/v2/nomaskcum2/0020.png"
    pause 0.15

image cum7:
    "images/events/v2/nomaskcum4/0001.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0002.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0003.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0004.png"
    function cum1
    pause 0.15
    "images/events/v2/nomaskcum4/0005.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0006.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0007.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0008.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0009.png"
    function s2
    pause 0.15
    "images/events/v2/nomaskcum4/0010.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0011.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0012.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0013.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0014.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0015.png"
    function swallow
    pause 0.15
    "images/events/v2/nomaskcum4/0016.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0017.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0018.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0019.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0020.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0021.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0022.png"
    function suck2
    pause 0.15
    "images/events/v2/nomaskcum4/0023.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0024.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0025.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0026.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0027.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0028.png"
    function choke3
    pause 0.15
    "images/events/v2/nomaskcum4/0029.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0030.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0031.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0032.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0033.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0034.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0035.png"
    function wetsquish
    pause 0.15
    "images/events/v2/nomaskcum4/0036.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0037.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0038.png"
    pause 0.15
    "images/events/v2/nomaskcum4/0039.png"
    function swallow
    pause 0.15
    "images/events/v2/nomaskcum4/0040.png"
    pause 0.15

image cum8:
    "images/events/v2/nomaskcum5/0040.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0041.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0042.png"
    function slurp
    pause 0.15
    "images/events/v2/nomaskcum5/0043.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0044.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0045.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0046.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0047.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0048.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0049.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0050.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0051.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0052.png"
    pause 0.15
    "images/events/v2/nomaskcum5/0053.png"
    pause 0.15
    repeat

image cum9:
    "images/events/v2/nomaskcum6/0054.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0055.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0056.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0057.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0058.png"
    function slurp
    pause 0.15
    "images/events/v2/nomaskcum6/0059.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0060.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0061.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0062.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0063.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0064.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0065.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0066.png"
    function s2
    pause 0.15
    "images/events/v2/nomaskcum6/0067.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0068.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0069.png"
    pause 0.15
    "images/events/v2/nomaskcum6/0070.png"
    pause 0.15

image frontvarmask1:
    "images/events/v1/front/mask1/0001.png"
    pause 0.15
    "images/events/v1/front/mask1/0002.png"
    pause 0.15
    "images/events/v1/front/mask1/0003.png"
    function s1
    pause 0.15
    "images/events/v1/front/mask1/0004.png"
    pause 0.15
    "images/events/v1/front/mask1/0005.png"
    pause 0.15
    "images/events/v1/front/mask1/0006.png"
    pause 0.15
    "images/events/v1/front/mask1/0007.png"
    pause 0.15
    "images/events/v1/front/mask1/0008.png"
    pause 0.15
    "images/events/v1/front/mask1/0009.png"
    pause 0.15
    repeat

image frontvarmask2:
    "images/events/v1/front/mask2/0001.png"
    pause 0.15
    "images/events/v1/front/mask2/0002.png"
    pause 0.15
    "images/events/v1/front/mask2/0003.png"
    pause 0.15
    "images/events/v1/front/mask2/0004.png"
    pause 0.15
    "images/events/v1/front/mask2/0005.png"
    function s1
    pause 0.15
    "images/events/v1/front/mask2/0006.png"
    pause 0.15
    "images/events/v1/front/mask2/0007.png"
    pause 0.15
    "images/events/v1/front/mask2/0008.png"
    pause 0.15
    "images/events/v1/front/mask2/0009.png"
    pause 0.15
    repeat

image frontvarmaskcum:
    "images/events/v1/front/maskcum/0001.png"
    pause 0.15
    "images/events/v1/front/maskcum/0002.png"
    pause 0.15
    "images/events/v1/front/maskcum/0003.png"
    pause 0.15
    "images/events/v1/front/maskcum/0004.png"
    function cum1
    pause 0.15
    "images/events/v1/front/maskcum/0005.png"
    pause 0.15
    "images/events/v1/front/maskcum/0006.png"
    pause 0.15
    "images/events/v1/front/maskcum/0007.png"
    pause 0.15
    "images/events/v1/front/maskcum/0008.png"
    pause 0.15
    "images/events/v1/front/maskcum/0009.png"
    pause 0.15
    "images/events/v1/front/maskcum/0010.png"
    pause 0.15
    "images/events/v1/front/maskcum/0011.png"
    pause 0.15
    "images/events/v1/front/maskcum/0012.png"
    pause 0.15
    "images/events/v1/front/maskcum/0013.png"
    function cum1
    pause 0.15
    "images/events/v1/front/maskcum/0014.png"
    pause 0.15
    "images/events/v1/front/maskcum/0015.png"
    pause 0.15
    "images/events/v1/front/maskcum/0016.png"
    pause 0.15
    "images/events/v1/front/maskcum/0017.png"
    pause 0.15
    "images/events/v1/front/maskcum/0018.png"
    pause 0.15
    "images/events/v1/front/maskcum/0019.png"
    pause 0.15
    "images/events/v1/front/maskcum/0020.png"
    pause 0.15

image frontvarnomask1:
    "images/events/v1/front/nomask1/0001.png"
    pause 0.15
    "images/events/v1/front/nomask1/0002.png"
    pause 0.15
    "images/events/v1/front/nomask1/0003.png"
    pause 0.15
    "images/events/v1/front/nomask1/0004.png"
    pause 0.15
    "images/events/v1/front/nomask1/0005.png"
    function s1
    pause 0.15
    "images/events/v1/front/nomask1/0006.png"
    pause 0.15
    "images/events/v1/front/nomask1/0007.png"
    pause 0.15
    "images/events/v1/front/nomask1/0008.png"
    pause 0.15
    "images/events/v1/front/nomask1/0009.png"
    pause 0.15
    repeat

image frontvarnomask2:
    "images/events/v1/front/nomask2/0001.png"
    pause 0.15
    "images/events/v1/front/nomask2/0002.png"
    pause 0.15
    "images/events/v1/front/nomask2/0003.png"
    pause 0.15
    "images/events/v1/front/nomask2/0004.png"
    pause 0.15
    "images/events/v1/front/nomask2/0005.png"
    pause 0.15
    "images/events/v1/front/nomask2/0006.png"
    function suck3
    pause 0.15
    "images/events/v1/front/nomask2/0007.png"
    pause 0.15
    "images/events/v1/front/nomask2/0008.png"
    pause 0.15
    "images/events/v1/front/nomask2/0009.png"
    pause 0.15
    repeat

image frontvarnomask3:
    "images/events/v1/front/nomask3/0001.png"
    pause 0.15
    "images/events/v1/front/nomask3/0002.png"
    pause 0.15
    "images/events/v1/front/nomask3/0003.png"
    pause 0.15
    "images/events/v1/front/nomask3/0004.png"
    pause 0.15
    "images/events/v1/front/nomask3/0005.png"
    pause 0.15
    "images/events/v1/front/nomask3/0006.png"
    pause 0.15
    "images/events/v1/front/nomask3/0007.png"
    pause 0.15
    "images/events/v1/front/nomask3/0008.png"
    pause 0.15
    "images/events/v1/front/nomask3/0009.png"
    pause 0.15
    "images/events/v1/front/nomask3/0010.png"
    pause 0.15
    "images/events/v1/front/nomask3/0011.png"
    pause 0.15
    "images/events/v1/front/nomask3/0012.png"
    pause 0.15
    "images/events/v1/front/nomask3/0013.png"
    pause 0.15
    "images/events/v1/front/nomask3/0014.png"
    function wetsquish
    pause 0.15
    "images/events/v1/front/nomask3/0015.png"
    pause 0.15

image frontvarnomask4:
    "images/events/v1/front/nomask4/0015.png"
    pause 0.07
    "images/events/v1/front/nomask4/0016.png"
    pause 0.07
    "images/events/v1/front/nomask4/0017.png"
    pause 0.07
    "images/events/v1/front/nomask4/0018.png"
    pause 0.07
    "images/events/v1/front/nomask4/0019.png"
    pause 0.07
    "images/events/v1/front/nomask4/0020.png"
    pause 0.07
    "images/events/v1/front/nomask4/0021.png"
    pause 0.07
    "images/events/v1/front/nomask4/0022.png"
    pause 0.07
    "images/events/v1/front/nomask4/0023.png"
    pause 0.07
    "images/events/v1/front/nomask4/0024.png"
    function suck4
    pause 0.07
    repeat

image frontvarnomask5:
    "images/events/v1/front/nomask5/0020.png"
    pause 0.15
    "images/events/v1/front/nomask5/0021.png"
    pause 0.15
    "images/events/v1/front/nomask5/0022.png"
    pause 0.15
    "images/events/v1/front/nomask5/0023.png"
    pause 0.15
    "images/events/v1/front/nomask5/0024.png"
    pause 0.15
    "images/events/v1/front/nomask5/0025.png"
    pause 0.15
    "images/events/v1/front/nomask5/0026.png"
    function choke3
    pause 0.15
    "images/events/v1/front/nomask5/0027.png"
    pause 0.15
    "images/events/v1/front/nomask5/0028.png"
    pause 0.15
    "images/events/v1/front/nomask5/0029.png"
    pause 0.15
    "images/events/v1/front/nomask5/0030.png"
    pause 0.15
    "images/events/v1/front/nomask5/0031.png"
    pause 0.15
    "images/events/v1/front/nomask5/0032.png"
    pause 0.15
    "images/events/v1/front/nomask5/0033.png"
    pause 0.15
    "images/events/v1/front/nomask5/0034.png"
    function splat
    pause 0.15
    "images/events/v1/front/nomask5/0035.png"
    pause 0.15
    "images/events/v1/front/nomask5/0036.png"
    pause 0.15
    "images/events/v1/front/nomask5/0037.png"
    pause 0.15
    "images/events/v1/front/nomask5/0038.png"
    pause 0.15
    "images/events/v1/front/nomask5/0039.png"
    pause 0.15
    "images/events/v1/front/nomask5/0040.png"
    pause 0.15

image frontvarnomask6:
    "images/events/v1/front/nomask6/0040.png"
    pause 0.15
    "images/events/v1/front/nomask6/0041.png"
    pause 0.15
    "images/events/v1/front/nomask6/0042.png"
    pause 0.15
    "images/events/v1/front/nomask6/0043.png"
    function swallow
    pause 0.15
    "images/events/v1/front/nomask6/0044.png"
    pause 0.15
    "images/events/v1/front/nomask6/0045.png"
    pause 0.15
    "images/events/v1/front/nomask6/0046.png"
    pause 0.15
    "images/events/v1/front/nomask6/0047.png"
    pause 0.15
    "images/events/v1/front/nomask6/0048.png"
    pause 0.15
    repeat

image frontvarnomaskcum1:
    "images/events/v1/front/nomaskcum1/0001.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0002.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0003.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0004.png"
    function cum1
    pause 0.15
    "images/events/v1/front/nomaskcum1/0005.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0006.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0007.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0008.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0009.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0010.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0011.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0012.png"
    function cum1
    pause 0.15
    "images/events/v1/front/nomaskcum1/0013.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0014.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0015.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0016.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0017.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0018.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0019.png"
    pause 0.15
    "images/events/v1/front/nomaskcum1/0020.png"
    pause 0.15

image frontvarnomaskcum2:
    "images/events/v1/front/nomaskcum2/0040.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0041.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0042.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0043.png"
    function suck4
    pause 0.15
    "images/events/v1/front/nomaskcum2/0044.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0045.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0046.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0047.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0048.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0049.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0050.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0051.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0052.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0053.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0054.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0055.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0056.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0057.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0058.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0059.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0060.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0061.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0062.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0063.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0064.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0065.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0066.png"
    function s2
    pause 0.15
    "images/events/v1/front/nomaskcum2/0067.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0068.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0069.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0070.png"
    pause 0.15
    "images/events/v1/front/nomaskcum2/0071.png"
    pause 0.15

image frontvardamaged1:
    "images/events/v1/front/damaged1/0001.png"
    pause 0.15
    "images/events/v1/front/damaged1/0002.png"
    pause 0.15
    "images/events/v1/front/damaged1/0003.png"
    pause 0.15
    "images/events/v1/front/damaged1/0004.png"
    pause 0.15
    "images/events/v1/front/damaged1/0005.png"
    pause 0.15
    "images/events/v1/front/damaged1/0006.png"
    function suck3
    pause 0.15
    "images/events/v1/front/damaged1/0007.png"
    pause 0.15
    "images/events/v1/front/damaged1/0008.png"
    pause 0.15
    "images/events/v1/front/damaged1/0009.png"
    pause 0.15
    repeat

image frontvardamaged2:
    "images/events/v1/front/damaged1/0001.png"
    pause 0.07
    "images/events/v1/front/damaged1/0002.png"
    pause 0.07
    "images/events/v1/front/damaged1/0003.png"
    pause 0.07
    "images/events/v1/front/damaged1/0004.png"
    pause 0.07
    "images/events/v1/front/damaged1/0005.png"
    pause 0.07
    "images/events/v1/front/damaged1/0006.png"
    function suck3
    pause 0.07
    "images/events/v1/front/damaged1/0007.png"
    pause 0.07
    "images/events/v1/front/damaged1/0008.png"
    pause 0.07
    "images/events/v1/front/damaged1/0009.png"
    pause 0.07
    repeat

image frontvardamagedcum:
    "images/events/v1/front/damagedcum/0001.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0002.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0003.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0004.png"
    function cum1
    pause 0.15
    "images/events/v1/front/damagedcum/0005.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0006.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0007.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0008.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0009.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0010.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0011.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0012.png"
    function cum1
    pause 0.15
    "images/events/v1/front/damagedcum/0013.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0014.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0015.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0016.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0017.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0018.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0019.png"
    pause 0.15
    "images/events/v1/front/damagedcum/0020.png"
    pause 0.15


image backvar1:
    "images/events/v1/back/damaged1/0001.png"
    pause .15
    "images/events/v1/back/damaged1/0002.png"
    pause .15
    "images/events/v1/back/damaged1/0003.png"
    pause .15
    "images/events/v1/back/damaged1/0004.png"
    pause .15
    "images/events/v1/back/damaged1/0005.png"
    pause .15
    "images/events/v1/back/damaged1/0006.png"
    function lick
    pause .15
    "images/events/v1/back/damaged1/0007.png"
    pause .15
    "images/events/v1/back/damaged1/0008.png"
    pause .15
    "images/events/v1/back/damaged1/0009.png"
    pause .15
    repeat

image backvar2:
    "images/events/v1/back/damaged2/0001.png"
    pause .15
    "images/events/v1/back/damaged2/0002.png"
    pause .15
    "images/events/v1/back/damaged2/0003.png"
    pause .15
    "images/events/v1/back/damaged2/0004.png"
    pause .15
    "images/events/v1/back/damaged2/0005.png"
    pause .15
    "images/events/v1/back/damaged2/0006.png"
    function slap1
    pause .15
    "images/events/v1/back/damaged2/0007.png"
    pause .15
    "images/events/v1/back/damaged2/0008.png"
    pause .15
    "images/events/v1/back/damaged2/0009.png"
    pause .15
    repeat

image backvar3:
    "images/events/v1/back/damaged3/0001.png"
    pause .15
    "images/events/v1/back/damaged3/0002.png"
    pause .15
    "images/events/v1/back/damaged3/0003.png"
    pause .15
    "images/events/v1/back/damaged3/0004.png"
    pause .15
    "images/events/v1/back/damaged3/0005.png"
    pause .15
    "images/events/v1/back/damaged3/0006.png"
    function lick
    pause .15
    "images/events/v1/back/damaged3/0007.png"
    pause .15
    "images/events/v1/back/damaged3/0008.png"
    pause .15
    "images/events/v1/back/damaged3/0009.png"
    pause .15
    repeat

image backvar4:
    "images/events/v1/back/damaged4/0001.png"
    pause .15
    "images/events/v1/back/damaged4/0002.png"
    pause .15
    "images/events/v1/back/damaged4/0003.png"
    pause .15
    "images/events/v1/back/damaged4/0004.png"
    pause .15
    "images/events/v1/back/damaged4/0005.png"
    function slap1
    pause .15
    "images/events/v1/back/damaged4/0006.png"
    pause .15
    "images/events/v1/back/damaged4/0007.png"
    pause .15
    repeat

image backvarcum1:
    "images/events/v1/back/damagedcum/0001.png"
    pause .15
    "images/events/v1/back/damagedcum/0002.png"
    pause .15
    "images/events/v1/back/damagedcum/0003.png"
    pause .15
    "images/events/v1/back/damagedcum/0004.png"
    pause .15
    "images/events/v1/back/damagedcum/0005.png"
    function cum1
    pause .15
    "images/events/v1/back/damagedcum/0006.png"
    pause .15
    "images/events/v1/back/damagedcum/0007.png"
    pause .15
    "images/events/v1/back/damagedcum/0008.png"
    pause .15
    "images/events/v1/back/damagedcum/0009.png"
    pause .15
    "images/events/v1/back/damagedcum/0010.png"
    pause .15
    "images/events/v1/back/damagedcum/0011.png"
    pause .15
    "images/events/v1/back/damagedcum/0012.png"
    pause .15
    "images/events/v1/back/damagedcum/0013.png"
    pause .15
    "images/events/v1/back/damagedcum/0014.png"
    pause .15
    "images/events/v1/back/damagedcum/0015.png"
    pause .15
    "images/events/v1/back/damagedcum/0016.png"
    function cum1
    pause .15
    "images/events/v1/back/damagedcum/0017.png"
    pause .15
    "images/events/v1/back/damagedcum/0018.png"
    pause .15
    "images/events/v1/back/damagedcum/0019.png"
    pause .15
    "images/events/v1/back/damagedcum/0020.png"
    pause .15
    "images/events/v1/back/damagedcum/0021.png"
    pause .15
    "images/events/v1/back/damagedcum/0022.png"
    function splat
    pause .15
    "images/events/v1/back/damagedcum/0023.png"
    pause .15
    "images/events/v1/back/damagedcum/0024.png"
    pause .15
    "images/events/v1/back/damagedcum/0025.png"
    pause .15

image nyunbar1:
    "images/events/bar/event/anim1/0001.jpg"
    pause 0.1
    "images/events/bar/event/anim1/0002.jpg"
    pause 0.1
    "images/events/bar/event/anim1/0003.jpg"
    pause 0.1
    "images/events/bar/event/anim1/0004.jpg"
    pause 0.1
    "images/events/bar/event/anim1/0005.jpg"
    pause 0.1
    "images/events/bar/event/anim1/0006.jpg"
    function suck4
    pause 0.1
    "images/events/bar/event/anim1/0007.jpg"
    pause 0.1
    "images/events/bar/event/anim1/0008.jpg"
    pause 0.1
    "images/events/bar/event/anim1/0009.jpg"
    pause 0.1
    repeat

image nyunbar2:
    "images/events/bar/event/anim2/0001.jpg"
    pause 0.1
    "images/events/bar/event/anim2/0002.jpg"
    pause 0.1
    "images/events/bar/event/anim2/0003.jpg"
    pause 0.1
    "images/events/bar/event/anim2/0004.jpg"
    pause 0.1
    "images/events/bar/event/anim2/0005.jpg"
    pause 0.1
    "images/events/bar/event/anim2/0006.jpg"
    function suck4
    pause 0.1
    "images/events/bar/event/anim2/0007.jpg"
    pause 0.1
    "images/events/bar/event/anim2/0008.jpg"
    pause 0.1
    "images/events/bar/event/anim2/0009.jpg"
    pause 0.1
    repeat

image nyunbar3:
    "images/events/bar/event/anim3/0001.jpg"
    pause 0.1
    "images/events/bar/event/anim3/0002.jpg"
    pause 0.1
    "images/events/bar/event/anim3/0003.jpg"
    pause 0.1
    "images/events/bar/event/anim3/0004.jpg"
    pause 0.1
    "images/events/bar/event/anim3/0005.jpg"
    pause 0.1
    "images/events/bar/event/anim3/0006.jpg"
    function suck4
    pause 0.1
    "images/events/bar/event/anim3/0007.jpg"
    pause 0.1
    "images/events/bar/event/anim3/0008.jpg"
    pause 0.1
    "images/events/bar/event/anim3/0009.jpg"
    pause 0.1
    repeat

image commis1:
    "images/events/comroom/ComRoomEvent/mis/2/0001.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/2/0002.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/2/0003.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/2/0004.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/2/0005.jpg"
    function slap1
    pause .1
    "images/events/comroom/ComRoomEvent/mis/2/0006.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/2/0007.jpg"
    pause .1
    repeat

image commis2:
    "images/events/comroom/ComRoomEvent/mis/1/0001.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/1/0002.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/1/0003.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/1/0004.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/1/0005.jpg"
    function slap1
    pause .1
    "images/events/comroom/ComRoomEvent/mis/1/0006.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/1/0007.jpg"
    pause .1
    repeat

image commis3:
    "images/events/comroom/ComRoomEvent/mis/3/0004.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/3/0005.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/3/0006.jpg"
    function slurp
    pause .12
    "images/events/comroom/ComRoomEvent/mis/3/0007.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/3/0008.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/3/0009.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/3/0010.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/3/0011.jpg"
    pause .12
    repeat

image commis4:
    "images/events/comroom/ComRoomEvent/mis/4/0012.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/4/0013.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/4/0014.jpg"
    function s2
    pause .12
    "images/events/comroom/ComRoomEvent/mis/4/0015.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/4/0016.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/4/0017.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/4/0018.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/4/0019.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/4/0020.jpg"
    pause .12

image commis5:
    "images/events/comroom/ComRoomEvent/mis/5/0020.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/5/0021.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/5/0022.jpg"
    function inside
    pause .12
    "images/events/comroom/ComRoomEvent/mis/5/0023.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/5/0024.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/5/0025.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/5/0026.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/5/0027.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/5/0028.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/5/0029.jpg"
    pause .12
    repeat

image commis6:
    "images/events/comroom/ComRoomEvent/mis/6/0001.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0002.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0003.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0004.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0005.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0006.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0007.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0008.jpg"
    function slap4
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0009.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0010.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0011.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0012.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0013.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0014.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0015.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/6/0016.jpg"
    pause .12

image commis7:
    "images/events/comroom/ComRoomEvent/mis/7/0016.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/7/0017.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/7/0018.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/7/0019.jpg"
    function slap5
    pause .1
    "images/events/comroom/ComRoomEvent/mis/7/0020.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/7/0021.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/7/0022.jpg"
    pause .1
    repeat

image commis8:
    "images/events/comroom/ComRoomEvent/mis/8/0016.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/8/0017.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/8/0018.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/8/0019.jpg"
    function slap5
    pause .1
    "images/events/comroom/ComRoomEvent/mis/8/0020.jpg"
    pause .1
    repeat

image commis9:
    "images/events/comroom/ComRoomEvent/mis/9/0016.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/9/0017.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/9/0018.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/9/0019.jpg"
    function slap5
    pause .1
    "images/events/comroom/ComRoomEvent/mis/9/0020.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/9/0021.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/9/0022.jpg"
    pause .1
    repeat

image commis10:
    "images/events/comroom/ComRoomEvent/mis/10/0016.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/10/0017.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/10/0018.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/10/0019.jpg"
    function slap5
    pause .1
    "images/events/comroom/ComRoomEvent/mis/10/0020.jpg"
    pause .1
    repeat

image commis11:
    "images/events/comroom/ComRoomEvent/mis/11/0016.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0017.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0018.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0019.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0020.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0021.jpg"
    function inside
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0022.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0023.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0024.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0025.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0026.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0027.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0028.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0029.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0030.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/11/0031.jpg"
    pause .1
    repeat

image commis13:
    "images/events/comroom/ComRoomEvent/mis/13/0016.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0017.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0018.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0019.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0020.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0021.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0022.jpg"
    function s1
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0023.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0024.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0025.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0026.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0027.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0028.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0029.jpg"
    function choke3
    "images/events/comroom/ComRoomEvent/mis/13/0030.jpg"
    pause .12

image commis13alt:
    "images/events/comroom/ComRoomEvent/mis/13/0031.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0032.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0033.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0034.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0035.jpg"
    function slurp
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0036.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0037.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0038.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0039.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0040.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0041.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0042.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0043.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0044.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0045.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0046.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0047.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0048.jpg"
    function suck4
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0049.jpg"
    pause .12
    "images/events/comroom/ComRoomEvent/mis/13/0050.jpg"
    pause .12

image commis14:
    "images/events/comroom/ComRoomEvent/mis/14/0016.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/14/0017.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/14/0018.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/14/0019.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/14/0020.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/14/0021.jpg"
    function suck1
    pause .1
    "images/events/comroom/ComRoomEvent/mis/14/0022.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/14/0023.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/14/0024.jpg"
    pause .1
    repeat

image commis15:
    "images/events/comroom/ComRoomEvent/mis/15/0034.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0035.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0036.jpg"
    function slurp
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0037.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0038.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0039.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0040.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0041.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0042.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0043.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0044.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0045.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0046.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0047.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0048.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0049.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0050.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0051.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0052.jpg"
    function wetsquish
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0053.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0054.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0055.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0056.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0057.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0058.jpg"
    function swallow
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0059.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0060.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0061.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0062.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0063.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0064.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0065.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0066.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0067.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0068.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0069.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0070.jpg"
    function suck2
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0071.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0072.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0073.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0074.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0075.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0076.jpg"
    function suck2
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0077.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0078.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0079.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0080.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0081.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0082.jpg"
    function suck2
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0083.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0084.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0085.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0086.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0087.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0088.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0089.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0090.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0091.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0092.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0093.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0094.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0095.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0096.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0097.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0098.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0099.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0100.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0101.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0102.jpg"
    function s2
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0103.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0104.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/15/0105.jpg"
    pause .1

image commis16:
    "images/events/comroom/ComRoomEvent/mis/16/0016.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0017.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0018.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0019.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0020.jpg"
    function slap1
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0021.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0022.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0023.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0024.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0025.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0026.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0027.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0028.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0029.jpg"
    function cum1
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0030.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0031.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0032.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0033.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0034.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0035.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0036.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0037.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0038.jpg"
    function cum1
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0039.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0040.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0041.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0042.jpg"
    function cum1
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0043.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0044.jpg"
    pause .1
    "images/events/comroom/ComRoomEvent/mis/16/0045.jpg"
    pause .1

image bay1anal1:
    "images/events/bay1/escape/1/0001.jpg"
    pause .1
    "images/events/bay1/escape/1/0002.jpg"
    pause .1
    "images/events/bay1/escape/1/0003.jpg"
    pause .1
    "images/events/bay1/escape/1/0004.jpg"
    pause .1
    "images/events/bay1/escape/1/0005.jpg"
    pause .1
    "images/events/bay1/escape/1/0006.jpg"
    pause .1
    "images/events/bay1/escape/1/0007.jpg"
    function lick
    pause .1
    "images/events/bay1/escape/1/0008.jpg"
    pause .1
    "images/events/bay1/escape/1/0009.jpg"
    pause .1
    "images/events/bay1/escape/1/0010.jpg"
    pause .1
    repeat

image bay1anal2:
    "images/events/bay1/escape/2/0001.jpg"
    pause .1
    "images/events/bay1/escape/2/0002.jpg"
    pause .1
    "images/events/bay1/escape/2/0003.jpg"
    pause .1
    "images/events/bay1/escape/2/0004.jpg"
    pause .1
    "images/events/bay1/escape/2/0005.jpg"
    pause .1
    "images/events/bay1/escape/2/0006.jpg"
    pause .1
    "images/events/bay1/escape/2/0007.jpg"
    function lick
    pause .1
    "images/events/bay1/escape/2/0008.jpg"
    pause .1
    "images/events/bay1/escape/2/0009.jpg"
    pause .1
    "images/events/bay1/escape/2/0010.jpg"
    pause .1
    repeat

image bay1anal3:
    "images/events/bay1/escape/3/0001.jpg"
    pause .1
    "images/events/bay1/escape/3/0002.jpg"
    pause .1
    "images/events/bay1/escape/3/0003.jpg"
    pause .1
    "images/events/bay1/escape/3/0004.jpg"
    pause .1
    "images/events/bay1/escape/3/0005.jpg"
    pause .1
    "images/events/bay1/escape/3/0006.jpg"
    pause .1
    "images/events/bay1/escape/3/0007.jpg"
    pause .1
    "images/events/bay1/escape/3/0008.jpg"
    pause .1
    "images/events/bay1/escape/3/0009.jpg"
    pause .1
    "images/events/bay1/escape/3/0010.jpg"
    pause .1
    "images/events/bay1/escape/3/0011.jpg"
    pause .1
    "images/events/bay1/escape/3/0012.jpg"
    pause .1
    "images/events/bay1/escape/3/0013.jpg"
    pause .1
    "images/events/bay1/escape/3/0014.jpg"
    pause .1
    "images/events/bay1/escape/3/0015.jpg"
    pause .1
    "images/events/bay1/escape/3/0016.jpg"
    pause .1
    "images/events/bay1/escape/3/0017.jpg"
    pause .1
    "images/events/bay1/escape/3/0018.jpg"
    pause .1
    "images/events/bay1/escape/3/0019.jpg"
    pause .1
    "images/events/bay1/escape/3/0020.jpg"
    pause .1
    "images/events/bay1/escape/3/0021.jpg"
    pause .1
    "images/events/bay1/escape/3/0022.jpg"
    pause .1
    "images/events/bay1/escape/3/0023.jpg"
    pause .1
    "images/events/bay1/escape/3/0024.jpg"
    pause .1
    "images/events/bay1/escape/3/0025.jpg"
    pause .1
    "images/events/bay1/escape/3/0026.jpg"
    pause .1
    function s4

image bay1anal3alt:
    "images/events/bay1/escape/3/0027.jpg"
    pause .1
    "images/events/bay1/escape/3/0028.jpg"
    pause .1
    "images/events/bay1/escape/3/0029.jpg"
    pause .1
    "images/events/bay1/escape/3/0030.jpg"
    pause .1
    "images/events/bay1/escape/3/0031.jpg"
    pause .1
    "images/events/bay1/escape/3/0032.jpg"
    pause .1
    "images/events/bay1/escape/3/0033.jpg"
    pause .1
    "images/events/bay1/escape/3/0034.jpg"
    pause .1
    "images/events/bay1/escape/3/0035.jpg"
    pause .1
    "images/events/bay1/escape/3/0036.jpg"
    function inside
    pause .1
    "images/events/bay1/escape/3/0037.jpg"
    pause .1
    "images/events/bay1/escape/3/0038.jpg"
    pause .1
    "images/events/bay1/escape/3/0039.jpg"
    pause .1
    "images/events/bay1/escape/3/0040.jpg"
    pause .1
    "images/events/bay1/escape/3/0041.jpg"
    pause .1
    "images/events/bay1/escape/3/0042.jpg"
    pause .1
    "images/events/bay1/escape/3/0043.jpg"
    pause .1
    "images/events/bay1/escape/3/0044.jpg"
    pause .1
    "images/events/bay1/escape/3/0045.jpg"
    pause .1
    "images/events/bay1/escape/3/0046.jpg"
    function s2
    pause .1
    "images/events/bay1/escape/3/0047.jpg"
    pause .1
    "images/events/bay1/escape/3/0048.jpg"
    pause .1
    "images/events/bay1/escape/3/0049.jpg"
    pause .1
    "images/events/bay1/escape/3/0050.jpg"
    pause .1

image bay1anal4:
    "images/events/bay1/escape/4/0001.jpg"
    pause .1
    "images/events/bay1/escape/4/0002.jpg"
    pause .1
    "images/events/bay1/escape/4/0003.jpg"
    pause .1
    "images/events/bay1/escape/4/0004.jpg"
    pause .1
    "images/events/bay1/escape/4/0005.jpg"
    function slap8
    pause .1
    "images/events/bay1/escape/4/0006.jpg"
    pause .1
    "images/events/bay1/escape/4/0007.jpg"
    pause .1
    repeat

image bay1anal5:
    "images/events/bay1/escape/5/0001.jpg"
    pause .1
    "images/events/bay1/escape/5/0002.jpg"
    pause .1
    "images/events/bay1/escape/5/0003.jpg"
    pause .1
    "images/events/bay1/escape/5/0004.jpg"
    pause .1
    "images/events/bay1/escape/5/0005.jpg"
    function slap8
    pause .1
    "images/events/bay1/escape/5/0006.jpg"
    pause .1
    "images/events/bay1/escape/5/0007.jpg"
    pause .1
    "images/events/bay1/escape/5/0008.jpg"
    pause .1
    "images/events/bay1/escape/5/0009.jpg"
    pause .1
    "images/events/bay1/escape/5/0010.jpg"
    pause .1
    "images/events/bay1/escape/5/0011.jpg"
    pause .1
    "images/events/bay1/escape/5/0012.jpg"
    function slap8
    pause .1
    "images/events/bay1/escape/5/0013.jpg"
    pause .1
    "images/events/bay1/escape/5/0014.jpg"
    pause .1
    "images/events/bay1/escape/5/0015.jpg"
    pause .1
    "images/events/bay1/escape/5/0016.jpg"
    pause .1
    "images/events/bay1/escape/5/0017.jpg"
    pause .1
    "images/events/bay1/escape/5/0018.jpg"
    pause .1
    "images/events/bay1/escape/5/0019.jpg"
    function slap8
    pause .1
    "images/events/bay1/escape/5/0020.jpg"
    pause .1
    "images/events/bay1/escape/5/0021.jpg"
    pause .1

image bay1anal6:
    "images/events/bay1/escape/6/0022.jpg"
    pause .1
    "images/events/bay1/escape/6/0023.jpg"
    pause .1
    "images/events/bay1/escape/6/0024.jpg"
    pause .1
    "images/events/bay1/escape/6/0025.jpg"
    pause .1
    "images/events/bay1/escape/6/0026.jpg"
    function slap8
    pause .1
    "images/events/bay1/escape/6/0027.jpg"
    pause .1
    "images/events/bay1/escape/6/0028.jpg"
    pause .1
    repeat

image bay1anal7:
    "images/events/bay1/escape/7/0050.jpg"
    pause .1
    "images/events/bay1/escape/7/0051.jpg"
    pause .1
    "images/events/bay1/escape/7/0052.jpg"
    pause .1
    "images/events/bay1/escape/7/0053.jpg"
    function slap2
    pause .1
    "images/events/bay1/escape/7/0054.jpg"
    pause .1
    "images/events/bay1/escape/7/0055.jpg"
    pause .1
    function s2
    repeat

image bay1anal8:
    "images/events/bay1/escape/8/0050.jpg"
    pause .1
    "images/events/bay1/escape/8/0051.jpg"
    pause .1
    "images/events/bay1/escape/8/0052.jpg"
    pause .1
    "images/events/bay1/escape/8/0053.jpg"
    function slap2
    pause .1
    "images/events/bay1/escape/8/0054.jpg"
    pause .1
    "images/events/bay1/escape/8/0055.jpg"
    pause .1
    "images/events/bay1/escape/8/0056.jpg"
    pause .1
    "images/events/bay1/escape/8/0057.jpg"
    function cum1
    pause .1
    "images/events/bay1/escape/8/0058.jpg"
    pause .1
    "images/events/bay1/escape/8/0059.jpg"
    pause .1
    "images/events/bay1/escape/8/0060.jpg"
    pause .1
    "images/events/bay1/escape/8/0061.jpg"
    pause .1
    "images/events/bay1/escape/8/0062.jpg"
    pause .1
    "images/events/bay1/escape/8/0063.jpg"
    pause .1
    "images/events/bay1/escape/8/0064.jpg"
    function squish
    pause .1
    "images/events/bay1/escape/8/0065.jpg"
    pause .1
    "images/events/bay1/escape/8/0066.jpg"
    pause .1
    "images/events/bay1/escape/8/0067.jpg"
    pause .1
    "images/events/bay1/escape/8/0068.jpg"
    pause .1
    "images/events/bay1/escape/8/0069.jpg"
    pause .1
    "images/events/bay1/escape/8/0070.jpg"
    pause .1
    "images/events/bay1/escape/8/0071.jpg"
    pause .1
    "images/events/bay1/escape/8/0072.jpg"
    pause .1
    "images/events/bay1/escape/8/0073.jpg"
    pause .1
    "images/events/bay1/escape/8/0074.jpg"
    pause .1
    "images/events/bay1/escape/8/0075.jpg"
    function s1
    pause .1
    "images/events/bay1/escape/8/0076.jpg"
    pause .1
    "images/events/bay1/escape/8/0077.jpg"
    pause .1
    "images/events/bay1/escape/8/0078.jpg"
    pause .1
    "images/events/bay1/escape/8/0079.jpg"
    function s2
    pause .1
    "images/events/bay1/escape/8/0080.jpg"
    pause .1
    "images/events/bay1/escape/8/0081.jpg"
    pause .1
    "images/events/bay1/escape/8/0082.jpg"
    pause .1
    "images/events/bay1/escape/8/0083.jpg"
    pause .1
    "images/events/bay1/escape/8/0084.jpg"
    pause .1
    "images/events/bay1/escape/8/0085.jpg"
    pause .1
    "images/events/bay1/escape/8/0086.jpg"
    pause .1
    "images/events/bay1/escape/8/0087.jpg"
    pause .1
    "images/events/bay1/escape/8/0088.jpg"
    pause .1

image bay1anal9:
    "images/events/bay1/escape/9/0008.jpg"
    pause .1
    "images/events/bay1/escape/9/0009.jpg"
    pause .1
    "images/events/bay1/escape/9/0010.jpg"
    pause .1
    "images/events/bay1/escape/9/0011.jpg"
    pause .1
    "images/events/bay1/escape/9/0012.jpg"
    pause .1
    "images/events/bay1/escape/9/0013.jpg"
    pause .1
    "images/events/bay1/escape/9/0014.jpg"
    pause .1
    "images/events/bay1/escape/9/0015.jpg"
    pause .1
    "images/events/bay1/escape/9/0016.jpg"
    pause .1
    "images/events/bay1/escape/9/0017.jpg"
    pause .1

image bay1anal9alt:
    "images/events/bay1/escape/9/0018.jpg"
    pause .1
    "images/events/bay1/escape/9/0019.jpg"
    pause .1
    "images/events/bay1/escape/9/0020.jpg"
    pause .1
    "images/events/bay1/escape/9/0021.jpg"
    pause .1
    "images/events/bay1/escape/9/0022.jpg"
    pause .1
    "images/events/bay1/escape/9/0023.jpg"
    pause .1
    "images/events/bay1/escape/9/0024.jpg"
    function s1
    pause .1
    "images/events/bay1/escape/9/0025.jpg"
    pause .1
    "images/events/bay1/escape/9/0026.jpg"
    pause .1

image bay1anal10:
    "images/events/bay1/escape/10/0050.jpg"
    pause .1
    "images/events/bay1/escape/10/0051.jpg"
    pause .1
    "images/events/bay1/escape/10/0052.jpg"
    function s2
    pause .1
    "images/events/bay1/escape/10/0053.jpg"
    pause .1
    "images/events/bay1/escape/10/0054.jpg"
    pause .1
    "images/events/bay1/escape/10/0055.jpg"
    function fart2
    pause .1
    "images/events/bay1/escape/10/0056.jpg"
    pause .1
    repeat

image bay1anal11:
    "images/events/bay1/escape/11/0001.jpg"
    pause .1
    "images/events/bay1/escape/11/0002.jpg"
    pause .1
    "images/events/bay1/escape/11/0003.jpg"
    pause .1
    "images/events/bay1/escape/11/0004.jpg"
    pause .1
    "images/events/bay1/escape/11/0005.jpg"
    function cum1
    pause .1
    "images/events/bay1/escape/11/0006.jpg"
    pause .1
    "images/events/bay1/escape/11/0007.jpg"
    pause .1
    "images/events/bay1/escape/11/0008.jpg"
    pause .1
    "images/events/bay1/escape/11/0009.jpg"
    pause .1
    "images/events/bay1/escape/11/0010.jpg"
    function cum1
    pause .1
    "images/events/bay1/escape/11/0011.jpg"
    pause .1
    "images/events/bay1/escape/11/0012.jpg"
    pause .1
    "images/events/bay1/escape/11/0013.jpg"
    pause .1
    "images/events/bay1/escape/11/0014.jpg"
    pause .1
    "images/events/bay1/escape/11/0015.jpg"
    pause .1
    "images/events/bay1/escape/11/0016.jpg"
    pause .1
    "images/events/bay1/escape/11/0017.jpg"
    function cum2
    pause .1
    "images/events/bay1/escape/11/0018.jpg"
    pause .1
    "images/events/bay1/escape/11/0019.jpg"
    pause .1
    "images/events/bay1/escape/11/0020.jpg"
    pause .1

image run_start:
    "images/events/run/start/0001.jpg"
    pause .12
    "images/events/run/start/0002.jpg"
    pause .12
    "images/events/run/start/0003.jpg"
    pause .12
    "images/events/run/start/0004.jpg"
    function step1
    pause .12
    "images/events/run/start/0005.jpg"
    pause .12
    "images/events/run/start/0006.jpg"
    pause .12
    "images/events/run/start/0007.jpg"
    pause .12
    "images/events/run/start/0008.jpg"
    pause .12
    "images/events/run/start/0009.jpg"
    pause .12
    "images/events/run/start/0010.jpg"
    pause .12
    "images/events/run/start/0011.jpg"
    pause .12
    "images/events/run/start/0012.jpg"
    pause .12
    "images/events/run/start/0013.jpg"
    function horrorstart
    pause .12
    "images/events/run/start/0014.jpg"
    pause .12
    "images/events/run/start/0015.jpg"
    pause .12
    "images/events/run/start/0016.jpg"
    pause .12
    "images/events/run/start/0017.jpg"
    pause .12
    "images/events/run/start/0018.jpg"
    pause .12
    "images/events/run/start/0019.jpg"
    pause .12
    "images/events/run/start/0020.jpg"
    pause .12
    "images/events/run/start/0021.jpg"
    pause .12
    "images/events/run/start/0022.jpg"
    pause .12
    "images/events/run/start/0023.jpg"
    pause .12
    "images/events/run/start/0024.jpg"
    pause .12
    "images/events/run/start/0025.jpg"
    pause .12
    "images/events/run/start/0026.jpg"
    pause .12
    "images/events/run/start/0027.jpg"
    pause .12
    "images/events/run/start/0028.jpg"
    pause .12
    "images/events/run/start/0029.jpg"
    pause .12
    "images/events/run/start/0030.jpg"
    pause .12
    "images/events/run/start/0031.jpg"
    function krokroar
    pause .12
    "images/events/run/start/0032.jpg"
    pause .12
    "images/events/run/start/0033.jpg"
    pause .12
    "images/events/run/start/0034.jpg"
    pause .12
    "images/events/run/start/0035.jpg"
    pause .12
    "images/events/run/start/0036.jpg"
    pause .12
    "images/events/run/start/0037.jpg"
    pause .12
    "images/events/run/start/0038.jpg"
    pause .12
    "images/events/run/start/0039.jpg"
    pause .12
    "images/events/run/start/0040.jpg"
    pause .12
    "images/events/run/start/0041.jpg"
    pause .12
    "images/events/run/start/0042.jpg"
    function runhit
    pause .12
    "images/events/run/start/0043.jpg"
    pause .12

image run_startalt:
    "images/events/run/start/0044.jpg"
    pause .12
    "images/events/run/start/0045.jpg"
    pause .12
    "images/events/run/start/0046.jpg"
    pause .12
    "images/events/run/start/0047.jpg"
    pause .12
    "images/events/run/start/0048.jpg"
    pause .12
    "images/events/run/start/0049.jpg"
    pause .12
    "images/events/run/start/0050.jpg"
    pause .12
    "images/events/run/start/0051.jpg"
    pause .12

image run_startalt1:
    "images/events/run/start/0052.jpg"
    pause .12
    "images/events/run/start/0053.jpg"
    pause .12
    "images/events/run/start/0054.jpg"
    pause .12
    "images/events/run/start/0055.jpg"
    pause .12
    "images/events/run/start/0056.jpg"
    pause .12
    "images/events/run/start/0057.jpg"
    pause .12
    "images/events/run/start/0058.jpg"
    pause .12
    "images/events/run/start/0059.jpg"
    pause .12
    "images/events/run/start/0060.jpg"
    pause .12
    "images/events/run/start/0061.jpg"
    pause .12
    "images/events/run/start/0062.jpg"
    pause .12
    "images/events/run/start/0063.jpg"
    pause .12
    "images/events/run/start/0064.jpg"
    pause .12
    "images/events/run/start/0065.jpg"
    pause .12
    "images/events/run/start/0066.jpg"
    pause .12
    "images/events/run/start/0067.jpg"
    pause .12
    "images/events/run/start/0068.jpg"
    pause .12
    "images/events/run/start/0069.jpg"
    pause .12
    "images/events/run/start/0070.jpg"
    pause .12

image run_left1:
    "images/events/run/right1/0071.jpg"
    pause .12
    "images/events/run/right1/0072.jpg"
    pause .12
    "images/events/run/right1/0073.jpg"
    pause .12
    "images/events/run/right1/0074.jpg"
    pause .12
    "images/events/run/right1/0075.jpg"
    pause .12
    "images/events/run/right1/0076.jpg"
    pause .12
    "images/events/run/right1/0077.jpg"
    pause .12
    "images/events/run/right1/0078.jpg"
    pause .12
    "images/events/run/right1/0079.jpg"
    pause .12
    "images/events/run/right1/0080.jpg"
    function runjump
    pause .12
    "images/events/run/right1/0081.jpg"
    pause .12
    "images/events/run/right1/0082.jpg"
    pause .12
    "images/events/run/right1/0083.jpg"
    pause .12
    "images/events/run/right1/0084.jpg"
    pause .12
    "images/events/run/right1/0085.jpg"
    pause .12
    "images/events/run/right1/0086.jpg"
    pause .12
    "images/events/run/right1/0087.jpg"
    pause .12
    "images/events/run/right1/0088.jpg"
    pause .12
    "images/events/run/right1/0089.jpg"
    pause .12
    "images/events/run/right1/0090.jpg"
    pause .12

image run_left_door:
    "images/events/run/right1door/0091.jpg"
    pause .12
    "images/events/run/right1door/0092.jpg"
    pause .12
    "images/events/run/right1door/0093.jpg"
    pause .12
    "images/events/run/right1door/0094.jpg"
    pause .12
    "images/events/run/right1door/0095.jpg"
    pause .12
    "images/events/run/right1door/0096.jpg"
    pause .12
    "images/events/run/right1door/0097.jpg"
    pause .12
    "images/events/run/right1door/0098.jpg"
    function metaldoor
    pause .12
    "images/events/run/right1door/0099.jpg"
    pause .12
    "images/events/run/right1door/0100.jpg"
    pause .12
    "images/events/run/right1door/0101.jpg"
    pause .12
    "images/events/run/right1door/0102.jpg"
    pause .12
    "images/events/run/right1door/0103.jpg"
    pause .12
    "images/events/run/right1door/0104.jpg"
    function krokroar
    pause .12
    "images/events/run/right1door/0105.jpg"
    pause .12

image run_left_catch:
    "images/events/run/right1b/0091.jpg"
    pause .12
    "images/events/run/right1b/0092.jpg"
    pause .12
    "images/events/run/right1b/0093.jpg"
    pause .12
    "images/events/run/right1b/0094.jpg"
    pause .12
    "images/events/run/right1b/0095.jpg"
    pause .12
    "images/events/run/right1b/0096.jpg"
    pause .12
    "images/events/run/right1b/0097.jpg"
    pause .12
    "images/events/run/right1b/0098.jpg"
    pause .12
    "images/events/run/right1b/0099.jpg"
    pause .12
    "images/events/run/right1b/0100.jpg"
    pause .12
    "images/events/run/right1b/0101.jpg"
    function fall
    pause .12
    "images/events/run/right1b/0102.jpg"
    pause .12
    "images/events/run/right1b/0103.jpg"
    pause .12
    "images/events/run/right1b/0104.jpg"
    pause .12
    "images/events/run/right1b/0105.jpg"
    pause .12

image run_right1:
    "images/events/run/left1/0070.jpg"
    pause .12
    "images/events/run/left1/0071.jpg"
    pause .12
    "images/events/run/left1/0072.jpg"
    pause .12
    "images/events/run/left1/0073.jpg"
    pause .12
    "images/events/run/left1/0074.jpg"
    pause .12
    "images/events/run/left1/0075.jpg"
    pause .12
    "images/events/run/left1/0076.jpg"
    pause .12
    "images/events/run/left1/0077.jpg"
    pause .12
    "images/events/run/left1/0078.jpg"
    pause .12
    "images/events/run/left1/0079.jpg"
    pause .12
    "images/events/run/left1/0080.jpg"
    function runjump
    pause .12
    "images/events/run/left1/0081.jpg"
    pause .12
    "images/events/run/left1/0082.jpg"
    pause .12
    "images/events/run/left1/0083.jpg"
    pause .12
    "images/events/run/left1/0084.jpg"
    pause .12
    "images/events/run/left1/0085.jpg"
    pause .12

image run_right1_right:
    "images/events/run/left1left/0086.jpg"
    pause .12
    "images/events/run/left1left/0087.jpg"
    pause .12
    "images/events/run/left1left/0088.jpg"
    pause .12
    "images/events/run/left1left/0089.jpg"
    pause .12
    "images/events/run/left1left/0090.jpg"
    pause .12
    "images/events/run/left1left/0091.jpg"
    pause .12
    "images/events/run/left1left/0092.jpg"
    pause .12
    "images/events/run/left1left/0093.jpg"
    pause .12
    "images/events/run/left1left/0094.jpg"
    pause .12
    "images/events/run/left1left/0095.jpg"
    pause .12
    "images/events/run/left1left/0096.jpg"
    pause .12
    "images/events/run/left1left/0097.jpg"
    pause .12
    "images/events/run/left1left/0098.jpg"
    pause .12
    "images/events/run/left1left/0099.jpg"
    pause .12
    "images/events/run/left1left/0100.jpg"
    pause .12
    "images/events/run/left1left/0101.jpg"
    pause .12
    "images/events/run/left1left/0102.jpg"
    pause .12
    "images/events/run/left1left/0103.jpg"
    pause .12
    "images/events/run/left1left/0104.jpg"
    pause .12
    "images/events/run/left1left/0105.jpg"
    pause .12
    "images/events/run/left1left/0106.jpg"
    pause .12
    "images/events/run/left1left/0107.jpg"
    pause .12
    "images/events/run/left1left/0108.jpg"
    pause .12
    "images/events/run/left1left/0109.jpg"
    pause .12
    "images/events/run/left1left/0110.jpg"
    pause .12
    "images/events/run/left1left/0111.jpg"
    pause .12
    "images/events/run/left1left/0112.jpg"
    pause .12
    "images/events/run/left1left/0113.jpg"
    pause .12
    "images/events/run/left1left/0114.jpg"
    pause .12
    "images/events/run/left1left/0115.jpg"
    function doorhit
    pause .12
    "images/events/run/left1left/0116.jpg"
    pause .12
    "images/events/run/left1left/0117.jpg"
    pause .12
    "images/events/run/left1left/0118.jpg"
    pause .12
    "images/events/run/left1left/0119.jpg"
    pause .12
    "images/events/run/left1left/0120.jpg"
    function doorhit
    pause .12
    "images/events/run/left1left/0121.jpg"
    pause .12
    "images/events/run/left1left/0122.jpg"
    pause .12
    "images/events/run/left1left/0123.jpg"
    pause .12
    "images/events/run/left1left/0124.jpg"
    pause .12
    "images/events/run/left1left/0125.jpg"
    function krokroar
    pause .12
    "images/events/run/left1left/0126.jpg"
    pause .12
    "images/events/run/left1left/0127.jpg"
    pause .12
    "images/events/run/left1left/0128.jpg"
    pause .12
    "images/events/run/left1left/0129.jpg"
    pause .12
    "images/events/run/left1left/0130.jpg"
    pause .12
    "images/events/run/left1left/0131.jpg"
    pause .12
    "images/events/run/left1left/0132.jpg"
    pause .12
    "images/events/run/left1left/0133.jpg"
    pause .12
    "images/events/run/left1left/0134.jpg"
    pause .12
    "images/events/run/left1left/0135.jpg"
    pause .12

image run_right1_left:
    "images/events/run/left1right1/0086.jpg"
    pause .12
    "images/events/run/left1right1/0087.jpg"
    pause .12
    "images/events/run/left1right1/0088.jpg"
    pause .12
    "images/events/run/left1right1/0089.jpg"
    pause .12
    "images/events/run/left1right1/0090.jpg"
    pause .12
    "images/events/run/left1right1/0091.jpg"
    pause .12
    "images/events/run/left1right1/0092.jpg"
    pause .12
    "images/events/run/left1right1/0093.jpg"
    pause .12
    "images/events/run/left1right1/0094.jpg"
    pause .12
    "images/events/run/left1right1/0095.jpg"
    pause .12
    "images/events/run/left1right1/0096.jpg"
    pause .12
    "images/events/run/left1right1/0097.jpg"
    pause .12
    "images/events/run/left1right1/0098.jpg"
    pause .12

image run_right1_left_catch:
    "images/events/run/left1right1a/0098.jpg"
    pause .12
    "images/events/run/left1right1a/0099.jpg"
    pause .12
    "images/events/run/left1right1a/0100.jpg"
    pause .12
    "images/events/run/left1right1a/0101.jpg"
    pause .12
    "images/events/run/left1right1a/0102.jpg"
    pause .12
    "images/events/run/left1right1a/0103.jpg"
    function fall
    pause .12
    "images/events/run/left1right1a/0104.jpg"
    pause .12
    "images/events/run/left1right1a/0105.jpg"
    pause .12

image run_right1_left_run:
    "images/events/run/left1right1b/0098.jpg"
    pause .12
    "images/events/run/left1right1b/0099.jpg"
    pause .12
    "images/events/run/left1right1b/0100.jpg"
    pause .12
    "images/events/run/left1right1b/0101.jpg"
    pause .12
    "images/events/run/left1right1b/0102.jpg"
    pause .12
    "images/events/run/left1right1b/0103.jpg"
    function fall
    pause .12
    "images/events/run/left1right1b/0104.jpg"
    pause .12
    "images/events/run/left1right1b/0105.jpg"
    pause .12
    "images/events/run/left1right1b/0106.jpg"
    pause .12
    "images/events/run/left1right1b/0107.jpg"
    pause .12
    "images/events/run/left1right1b/0108.jpg"
    pause .12
    "images/events/run/left1right1b/0109.jpg"
    pause .12
    "images/events/run/left1right1b/0110.jpg"
    pause .12
    "images/events/run/left1right1b/0111.jpg"
    pause .12
    "images/events/run/left1right1b/0112.jpg"
    pause .12
    "images/events/run/left1right1b/0113.jpg"
    pause .12
    "images/events/run/left1right1b/0114.jpg"
    function krokroar
    pause .12
    "images/events/run/left1right1b/0115.jpg"
    pause .12

image krok1:
    "images/events/crok/1/0001.jpg"
    pause .12
    "images/events/crok/1/0002.jpg"
    pause .12
    "images/events/crok/1/0003.jpg"
    pause .12
    "images/events/crok/1/0004.jpg"
    pause .12
    "images/events/crok/1/0005.jpg"
    pause .12
    "images/events/crok/1/0006.jpg"
    pause .12
    "images/events/crok/1/0007.jpg"
    pause .12
    "images/events/crok/1/0008.jpg"
    pause .12
    "images/events/crok/1/0009.jpg"
    pause .12
    "images/events/crok/1/0010.jpg"
    pause .12
    "images/events/crok/1/0011.jpg"
    pause .12
    "images/events/crok/1/0012.jpg"
    pause .12
    "images/events/crok/1/0013.jpg"
    pause .12
    repeat

image krok2:
    "images/events/crok/2/0001.jpg"
    pause .12
    "images/events/crok/2/0002.jpg"
    pause .12
    "images/events/crok/2/0003.jpg"
    pause .12
    "images/events/crok/2/0004.jpg"
    pause .12
    "images/events/crok/2/0005.jpg"
    pause .12
    "images/events/crok/2/0006.jpg"
    pause .12
    "images/events/crok/2/0007.jpg"
    pause .12
    "images/events/crok/2/0008.jpg"
    function inside
    pause .12
    "images/events/crok/2/0009.jpg"
    pause .12
    "images/events/crok/2/0010.jpg"
    pause .12
    "images/events/crok/2/0011.jpg"
    pause .12
    "images/events/crok/2/0012.jpg"
    pause .12
    "images/events/crok/2/0013.jpg"
    pause .12
    repeat

image krok3:
    "images/events/crok/3/0001.jpg"
    pause .12
    "images/events/crok/3/0002.jpg"
    pause .12
    "images/events/crok/3/0003.jpg"
    pause .12
    "images/events/crok/3/0004.jpg"
    pause .12
    "images/events/crok/3/0005.jpg"
    pause .12
    "images/events/crok/3/0006.jpg"
    function inside
    pause .12
    "images/events/crok/3/0007.jpg"
    pause .12
    "images/events/crok/3/0008.jpg"
    pause .12
    "images/events/crok/3/0009.jpg"
    pause .12
    "images/events/crok/3/0010.jpg"
    pause .12
    "images/events/crok/3/0011.jpg"
    pause .12
    repeat

image krok4:
    "images/events/crok/4/0001.jpg"
    pause .12
    "images/events/crok/4/0002.jpg"
    pause .12
    "images/events/crok/4/0003.jpg"
    function s1
    pause .12
    "images/events/crok/4/0004.jpg"
    pause .12
    "images/events/crok/4/0005.jpg"
    pause .12
    "images/events/crok/4/0006.jpg"
    pause .12
    "images/events/crok/4/0007.jpg"
    pause .12
    "images/events/crok/4/0008.jpg"
    pause .12
    "images/events/crok/4/0009.jpg"
    pause .12
    "images/events/crok/4/0010.jpg"
    pause .12
    "images/events/crok/4/0011.jpg"
    pause .12
    "images/events/crok/4/0012.jpg"
    function s4
    pause .12
    "images/events/crok/4/0013.jpg"
    pause .12

image krok5:
    "images/events/crok/5/0001.jpg"
    pause .12
    "images/events/crok/5/0002.jpg"
    pause .12
    "images/events/crok/5/0003.jpg"
    pause .12
    "images/events/crok/5/0004.jpg"
    pause .12
    "images/events/crok/5/0005.jpg"
    pause .12
    "images/events/crok/5/0006.jpg"
    function s1
    pause .12
    "images/events/crok/5/0007.jpg"
    pause .12
    "images/events/crok/5/0008.jpg"
    pause .12
    "images/events/crok/5/0009.jpg"
    pause .12
    repeat

image krok6:
    "images/events/crok/6/0001.jpg"
    pause .1
    "images/events/crok/6/0002.jpg"
    pause .1
    "images/events/crok/6/0003.jpg"
    pause .1
    "images/events/crok/6/0004.jpg"
    pause .1
    "images/events/crok/6/0005.jpg"
    pause .1
    "images/events/crok/6/0006.jpg"
    function s2
    pause .1
    "images/events/crok/6/0007.jpg"
    pause .1
    "images/events/crok/6/0008.jpg"
    pause .1
    repeat

image krok7:
    "images/events/crok/7/0013.jpg"
    pause .1
    "images/events/crok/7/0014.jpg"
    pause .1
    "images/events/crok/7/0015.jpg"
    pause .1
    "images/events/crok/7/0016.jpg"
    pause .1
    "images/events/crok/7/0017.jpg"
    pause .1
    "images/events/crok/7/0018.jpg"
    pause .1
    "images/events/crok/7/0019.jpg"
    pause .1
    "images/events/crok/7/0020.jpg"
    function inside
    pause .1
    "images/events/crok/7/0021.jpg"
    pause .1
    "images/events/crok/7/0022.jpg"
    pause .1
    "images/events/crok/7/0023.jpg"
    pause .1
    "images/events/crok/7/0024.jpg"
    pause .1
    repeat

image krok8:
    "images/events/crok/8/0013.jpg"
    pause .08
    "images/events/crok/8/0014.jpg"
    pause .08
    "images/events/crok/8/0015.jpg"
    pause .08
    "images/events/crok/8/0016.jpg"
    pause .08
    "images/events/crok/8/0017.jpg"
    pause .08
    "images/events/crok/8/0018.jpg"
    function slap1
    pause .08
    "images/events/crok/8/0019.jpg"
    pause .08
    "images/events/crok/8/0020.jpg"
    pause .08
    "images/events/crok/8/0021.jpg"
    pause .08
    repeat

image krok9:
    "images/events/crok/9/0001.jpg"
    pause .15
    "images/events/crok/9/0002.jpg"
    pause .15
    "images/events/crok/9/0003.jpg"
    pause .15
    "images/events/crok/9/0004.jpg"
    pause .15
    "images/events/crok/9/0005.jpg"
    pause .15
    "images/events/crok/9/0006.jpg"
    pause .15
    "images/events/crok/9/0007.jpg"
    function s1
    pause .15
    "images/events/crok/9/0008.jpg"
    pause .15
    "images/events/crok/9/0009.jpg"
    pause .15
    "images/events/crok/9/0010.jpg"
    pause .15
    "images/events/crok/9/0011.jpg"
    pause .15
    "images/events/crok/9/0012.jpg"
    pause .15
    "images/events/crok/9/0013.jpg"
    pause .15
    "images/events/crok/9/0013.jpg"
    pause .15
    "images/events/crok/9/0014.jpg"
    pause .15
    "images/events/crok/9/0015.jpg"
    pause .15
    "images/events/crok/9/0016.jpg"
    pause .15
    "images/events/crok/9/0017.jpg"
    pause .15
    "images/events/crok/9/0018.jpg"
    pause .15
    "images/events/crok/9/0019.jpg"
    pause .15
    "images/events/crok/9/0020.jpg"
    pause .15
    "images/events/crok/9/0021.jpg"
    function inside
    pause .15
    "images/events/crok/9/0022.jpg"
    pause .15

image krok9alt:
    "images/events/crok/9/0023.jpg"
    pause .15
    "images/events/crok/9/0024.jpg"
    pause .15
    "images/events/crok/9/0025.jpg"
    pause .15
    "images/events/crok/9/0026.jpg"
    function inside
    pause .15
    "images/events/crok/9/0027.jpg"
    pause .15
    "images/events/crok/9/0028.jpg"
    pause .15
    "images/events/crok/9/0029.jpg"
    pause .15
    "images/events/crok/9/0030.jpg"
    pause .15
    "images/events/crok/9/0031.jpg"
    pause .15
    "images/events/crok/9/0032.jpg"
    pause .15
    "images/events/crok/9/0033.jpg"
    pause .15
    "images/events/crok/9/0034.jpg"
    pause .15
    "images/events/crok/9/0035.jpg"
    pause .15

image krok10:
    "images/events/crok/10/0036.jpg"
    pause .12
    "images/events/crok/10/0037.jpg"
    pause .12
    "images/events/crok/10/0038.jpg"
    pause .12
    "images/events/crok/10/0039.jpg"
    pause .12
    "images/events/crok/10/0040.jpg"
    function s1
    pause .12
    "images/events/crok/10/0041.jpg"
    pause .12
    "images/events/crok/10/0042.jpg"
    pause .12
    "images/events/crok/10/0043.jpg"
    pause .12
    "images/events/crok/10/0044.jpg"
    pause .12
    "images/events/crok/10/0045.jpg"
    pause .12
    repeat

image krok11:
    "images/events/crok/11/0046.jpg"
    pause .12
    "images/events/crok/11/0047.jpg"
    pause .12
    "images/events/crok/11/0048.jpg"
    pause .12
    "images/events/crok/11/0049.jpg"
    pause .12
    "images/events/crok/11/0050.jpg"
    pause .12
    "images/events/crok/11/0051.jpg"
    pause .12
    "images/events/crok/11/0052.jpg"
    pause .12
    "images/events/crok/11/0053.jpg"
    pause .12
    "images/events/crok/11/0054.jpg"
    pause .12
    "images/events/crok/11/0055.jpg"
    pause .12
    "images/events/crok/11/0056.jpg"
    function s1
    pause .12
    "images/events/crok/11/0057.jpg"
    pause .12
    "images/events/crok/11/0058.jpg"
    pause .12
    "images/events/crok/11/0059.jpg"
    pause .12
    "images/events/crok/11/0060.jpg"
    pause .12
    "images/events/crok/11/0061.jpg"
    pause .12
    "images/events/crok/11/0062.jpg"
    pause .12
    "images/events/crok/11/0063.jpg"
    pause .12
    "images/events/crok/11/0064.jpg"
    pause .12
    "images/events/crok/11/0065.jpg"
    pause .12
    "images/events/crok/11/0066.jpg"
    pause .12
    "images/events/crok/11/0067.jpg"
    pause .12
    "images/events/crok/11/0068.jpg"
    function inside
    pause .12
    "images/events/crok/11/0069.jpg"
    pause .12
    "images/events/crok/11/0070.jpg"
    pause .12
    "images/events/crok/11/0071.jpg"
    pause .12
    "images/events/crok/11/0072.jpg"
    pause .12
    "images/events/crok/11/0073.jpg"
    pause .12
    "images/events/crok/11/0074.jpg"
    pause .12
    "images/events/crok/11/0075.jpg"
    pause .12
    "images/events/crok/11/0076.jpg"
    pause .12
    "images/events/crok/11/0077.jpg"
    pause .12
    "images/events/crok/11/0078.jpg"
    pause .12
    "images/events/crok/11/0079.jpg"
    pause .12
    "images/events/crok/11/0080.jpg"
    pause .12
    "images/events/crok/11/0081.jpg"
    function fart2
    pause .12
    "images/events/crok/11/0082.jpg"
    pause .12
    "images/events/crok/11/0083.jpg"
    pause .12
    "images/events/crok/11/0084.jpg"
    pause .12
    "images/events/crok/11/0085.jpg"
    pause .12

image krok12:
    "images/events/crok/12/0086.jpg"
    pause .12
    "images/events/crok/12/0087.jpg"
    pause .12
    "images/events/crok/12/0088.jpg"
    pause .12
    "images/events/crok/12/0089.jpg"
    function fart2
    pause .12
    "images/events/crok/12/0090.jpg"
    pause .12
    "images/events/crok/12/0091.jpg"
    function inside
    pause .12
    "images/events/crok/12/0092.jpg"
    pause .12
    "images/events/crok/12/0093.jpg"
    pause .12
    "images/events/crok/12/0094.jpg"
    pause .12
    repeat

image krok13:
    "images/events/crok/13/0091.jpg"
    pause .12
    "images/events/crok/13/0092.jpg"
    pause .12
    "images/events/crok/13/0093.jpg"
    pause .12
    "images/events/crok/13/0094.jpg"
    pause .12
    "images/events/crok/13/0095.jpg"
    function cum2
    pause .12
    "images/events/crok/13/0096.jpg"
    pause .12
    "images/events/crok/13/0097.jpg"
    pause .12
    "images/events/crok/13/0098.jpg"
    pause .12
    "images/events/crok/13/0099.jpg"
    pause .12
    "images/events/crok/13/0100.jpg"
    pause .12
    "images/events/crok/13/0101.jpg"
    pause .12
    "images/events/crok/13/0102.jpg"
    function cum1
    pause .12
    "images/events/crok/13/0103.jpg"
    pause .12
    "images/events/crok/13/0104.jpg"
    pause .12
    "images/events/crok/13/0105.jpg"
    pause .12
    "images/events/crok/13/0106.jpg"
    pause .12
    "images/events/crok/13/0107.jpg"
    pause .12
    "images/events/crok/13/0108.jpg"
    function cum1
    pause .12
    "images/events/crok/13/0109.jpg"
    pause .12
    "images/events/crok/13/0110.jpg"
    pause .12
    "images/events/crok/13/0111.jpg"
    pause .12
    "images/events/crok/13/0112.jpg"
    pause .12
    "images/events/crok/13/0113.jpg"
    pause .12
    "images/events/crok/13/0114.jpg"
    pause .12
    "images/events/crok/13/0115.jpg"
    function fart
    pause .12
    "images/events/crok/13/0116.jpg"
    pause .12
    "images/events/crok/13/0117.jpg"
    pause .12
    "images/events/crok/13/0118.jpg"
    pause .12
    "images/events/crok/13/0119.jpg"
    function cumsplash
    pause .12
    "images/events/crok/13/0120.jpg"
    pause .12

image krok14:
    "images/events/crok/14/0006.jpg"
    pause .12
    "images/events/crok/14/0007.jpg"
    pause .12
    "images/events/crok/14/0008.jpg"
    pause .12
    "images/events/crok/14/0009.jpg"
    pause .12
    "images/events/crok/14/0010.jpg"
    function cum1
    pause .12
    "images/events/crok/14/0011.jpg"
    pause .12
    "images/events/crok/14/0012.jpg"
    pause .12
    "images/events/crok/14/0013.jpg"
    pause .12
    "images/events/crok/14/0013.jpg"
    pause .12
    "images/events/crok/14/0014.jpg"
    pause .12
    "images/events/crok/14/0015.jpg"
    pause .12
    "images/events/crok/14/0016.jpg"
    pause .12
    "images/events/crok/14/0017.jpg"
    pause .12
    "images/events/crok/14/0018.jpg"
    pause .12
    "images/events/crok/14/0019.jpg"
    pause .12
    "images/events/crok/14/0020.jpg"
    pause .12
    "images/events/crok/14/0021.jpg"
    pause .12
    "images/events/crok/14/0022.jpg"
    function cum1
    pause .12
    "images/events/crok/14/0023.jpg"
    pause .12
    "images/events/crok/14/0024.jpg"
    pause .12
    "images/events/crok/14/0025.jpg"
    pause .12
    "images/events/crok/14/0026.jpg"
    pause .12
    "images/events/crok/14/0027.jpg"
    pause .12
    "images/events/crok/14/0028.jpg"
    function s2
    pause .12
    "images/events/crok/14/0029.jpg"
    pause .12
    "images/events/crok/14/0030.jpg"
    pause .12
    "images/events/crok/14/0031.jpg"
    pause .12
    "images/events/crok/14/0032.jpg"
    pause .12

image krok15:
    "images/events/crok/15/0020.jpg"
    pause .12
    "images/events/crok/15/0021.jpg"
    pause .12
    "images/events/crok/15/0022.jpg"
    pause .12
    "images/events/crok/15/0023.jpg"
    pause .12
    "images/events/crok/15/0024.jpg"
    function squish
    pause .12
    "images/events/crok/15/0025.jpg"
    pause .12
    "images/events/crok/15/0026.jpg"
    pause .12
    "images/events/crok/15/0027.jpg"
    pause .12
    "images/events/crok/15/0028.jpg"
    pause .12
    "images/events/crok/15/0029.jpg"
    pause .12
    "images/events/crok/15/0030.jpg"
    pause .12
    "images/events/crok/15/0031.jpg"
    pause .12
    "images/events/crok/15/0032.jpg"
    pause .12
    "images/events/crok/15/0033.jpg"
    pause .12
    "images/events/crok/15/0034.jpg"
    pause .12
    "images/events/crok/15/0035.jpg"
    pause .12
    "images/events/crok/15/0036.jpg"
    pause .12
    "images/events/crok/15/0037.jpg"
    pause .12
    "images/events/crok/15/0038.jpg"
    pause .12
    "images/events/crok/15/0039.jpg"
    pause .12
    "images/events/crok/15/0040.jpg"
    pause .12
    "images/events/crok/15/0041.jpg"
    pause .12
    "images/events/crok/15/0042.jpg"
    function s2
    pause .12
    "images/events/crok/15/0043.jpg"
    pause .12
    "images/events/crok/15/0044.jpg"
    pause .12
    "images/events/crok/15/0045.jpg"
    pause .12

image scan:
    "images/map/scan/1.png"
    pause .15
    "images/map/scan/2.png"
    pause .15
    "images/map/scan/3.png"
    pause .15
    "images/map/scan/4.png"
    pause .15
    "images/map/scan/5.png"
    pause .15
    "images/map/scan/6.png"
    pause .15
    "images/map/scan/7.png"
    pause .15
    "images/map/scan/8.png"
    pause .15

image poolscan:
    "images/map/poolspot/1.png"
    pause .15
    "images/map/poolspot/2.png"
    pause .15
    "images/map/poolspot/3.png"
    pause .15
    "images/map/poolspot/4.png"
    pause .15

image poolopen:
    "images/events/pool/open/0001.jpg"
    pause 0.15
    "images/events/pool/open/0002.jpg"
    pause 0.15
    "images/events/pool/open/0003.jpg"
    pause 0.15
    "images/events/pool/open/0004.jpg"
    pause 0.15
    "images/events/pool/open/0005.jpg"
    pause 0.15
    "images/events/pool/open/0006.jpg"
    pause 0.15
    "images/events/pool/open/0007.jpg"
    pause 0.15
    "images/events/pool/open/0008.jpg"
    pause 0.15
    "images/events/pool/open/0009.jpg"
    pause 0.15
    "images/events/pool/open/0010.jpg"
    pause 0.15
    "images/events/pool/open/0011.jpg"
    pause 0.15
    "images/events/pool/open/0012.jpg"
    pause 0.15
    "images/events/pool/open/0013.jpg"
    pause 0.15
    "images/events/pool/open/0014.jpg"
    pause 0.15
    "images/events/pool/open/0015.jpg"
    pause 0.15

image krokpool:
    "images/events/pool/cutscene/scene/0015.jpg"
    0.15
    "images/events/pool/cutscene/scene/0016.jpg"
    0.15
    "images/events/pool/cutscene/scene/0017.jpg"
    0.15
    "images/events/pool/cutscene/scene/0018.jpg"
    0.15
    "images/events/pool/cutscene/scene/0019.jpg"
    0.15
    "images/events/pool/cutscene/scene/0020.jpg"
    0.15
    "images/events/pool/cutscene/scene/0021.jpg"
    0.15
    "images/events/pool/cutscene/scene/0022.jpg"
    0.15
    "images/events/pool/cutscene/scene/0023.jpg"
    0.15
    "images/events/pool/cutscene/scene/0024.jpg"
    function krokroar
    0.15
    "images/events/pool/cutscene/scene/0025.jpg"
    0.15
    "images/events/pool/cutscene/scene/0026.jpg"
    0.15
    "images/events/pool/cutscene/scene/0027.jpg"
    0.15
    "images/events/pool/cutscene/scene/0028.jpg"
    0.15

image newdoor1:
    "images/events/doorCatch/anim1/0001.jpg"
    pause 0.12
    "images/events/doorCatch/anim1/0002.jpg"
    pause 0.12
    "images/events/doorCatch/anim1/0003.jpg"
    pause 0.12
    "images/events/doorCatch/anim1/0004.jpg"
    pause 0.12
    "images/events/doorCatch/anim1/0005.jpg"
    pause 0.12
    "images/events/doorCatch/anim1/0006.jpg"
    function slap2
    pause 0.12
    "images/events/doorCatch/anim1/0007.jpg"
    pause 0.12
    repeat

image newdoor2:
    "images/events/doorCatch/anim2/0001.jpg"
    pause 0.12
    "images/events/doorCatch/anim2/0002.jpg"
    pause 0.12
    "images/events/doorCatch/anim2/0003.jpg"
    pause 0.12
    "images/events/doorCatch/anim2/0004.jpg"
    pause 0.12
    "images/events/doorCatch/anim2/0005.jpg"
    pause 0.12
    "images/events/doorCatch/anim2/0006.jpg"
    function slap2
    pause 0.12
    "images/events/doorCatch/anim2/0007.jpg"
    pause 0.12
    repeat

image newdoor3:
    "images/events/doorCatch/anim3/0008.jpg"
    pause 0.12
    "images/events/doorCatch/anim3/0009.jpg"
    pause 0.12
    "images/events/doorCatch/anim3/0010.jpg"
    pause 0.12
    "images/events/doorCatch/anim3/0011.jpg"
    function slap3
    pause 0.12
    "images/events/doorCatch/anim3/0012.jpg"
    pause 0.12
    "images/events/doorCatch/anim3/0013.jpg"
    pause 0.12
    repeat

image newdoorcum1:
    "images/events/doorCatch/cum1/0014.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0015.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0016.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0017.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0018.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0019.jpg"
    function cum1
    pause 0.12
    "images/events/doorCatch/cum1/0020.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0021.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0022.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0023.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0024.jpg"
    function cum1
    pause 0.12
    "images/events/doorCatch/cum1/0025.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0026.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0027.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0028.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0029.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0030.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0031.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0032.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0033.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0034.jpg"
    function splat
    pause 0.12
    "images/events/doorCatch/cum1/0035.jpg"
    pause 0.12
    "images/events/doorCatch/cum1/0036.jpg"
    pause 0.12

image newdoorcum2:
    "images/events/doorCatch/cum2/0036.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0037.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0038.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0039.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0040.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0041.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0042.jpg"
    function s2
    pause 0.12
    "images/events/doorCatch/cum2/0043.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0044.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0045.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0046.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0047.jpg"
    function squish
    pause 0.12
    "images/events/doorCatch/cum2/0048.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0049.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0050.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0051.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0052.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0053.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0054.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0055.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0056.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0057.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0058.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0059.jpg"
    pause 0.12
    "images/events/doorCatch/cum2/0060.jpg"
    pause 0.12

image newshowercum:
    "images/events/medbay/shower/scene1/anim3/0007.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim3/0008.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim3/0009.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim3/0010.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim3/0011.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim3/0012.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim3/0013.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim3/0014.jpg"
    pause 0.12
    "images/events/medbay/shower/scene1/anim3/0015.jpg"
    pause 0.12

image ventclose:
    "images/events/medbay/vent/0001.jpg"
    pause .12
    "images/events/medbay/vent/0002.jpg"
    pause .12
    "images/events/medbay/vent/0003.jpg"
    pause .12
    "images/events/medbay/vent/0004.jpg"
    pause .12
    "images/events/medbay/vent/0005.jpg"
    function doorhit
    pause .12
    "images/events/medbay/vent/0006.jpg"
    pause .12
    "images/events/medbay/vent/0007.jpg"
    pause .12
    "images/events/medbay/vent/0008.jpg"
    pause .12
    "images/events/medbay/vent/0009.jpg"
    pause .12
    "images/events/medbay/vent/0010.jpg"
    pause .12
    "images/events/medbay/vent/0011.jpg"
    pause .12
    "images/events/medbay/vent/0012.jpg"
    pause .12
    "images/events/medbay/vent/0013.jpg"
    pause .12
    "images/events/medbay/vent/0014.jpg"
    pause .12

image ventclose1:
    "images/events/medbay/vent/0001.jpg"
    pause .12
    "images/events/medbay/vent/0002.jpg"
    pause .12
    "images/events/medbay/vent/0003.jpg"
    pause .12
    "images/events/medbay/vent/0004.jpg"
    pause .12
    "images/events/medbay/vent/0015.jpg"
    function doorhit

image showerbug1:
    "images/events/medbay/shower/scene2/anim1/0001.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim1/0002.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim1/0003.jpg"
    function inside
    pause .12
    "images/events/medbay/shower/scene2/anim1/0004.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim1/0005.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim1/0006.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim1/0007.jpg"
    function s2
    pause .12
    "images/events/medbay/shower/scene2/anim1/0008.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim1/0009.jpg"
    pause .12
    repeat

image showerbug2:
    "images/events/medbay/shower/scene2/anim2/0001.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim2/0002.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim2/0003.jpg"
    function suck1
    pause .12
    "images/events/medbay/shower/scene2/anim2/0004.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim2/0005.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim2/0006.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim2/0007.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim2/0008.jpg"
    function suck4
    pause .12
    "images/events/medbay/shower/scene2/anim2/0009.jpg"
    pause .12
    repeat

image showerbugcum1:
    "images/events/medbay/shower/scene2/anim3/0001.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0002.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0003.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0004.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0005.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0006.jpg"
    function cum1
    pause .12
    "images/events/medbay/shower/scene2/anim3/0007.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0008.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0009.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0010.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0011.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0012.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0013.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0014.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0015.jpg"
    function splat
    pause .12
    "images/events/medbay/shower/scene2/anim3/0016.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0017.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0018.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0019.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0020.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0021.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0022.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0023.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0024.jpg"
    function squish
    pause .12
    "images/events/medbay/shower/scene2/anim3/0025.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0026.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0027.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim3/0028.jpg"
    pause .12

image showerbugcum2:
    "images/events/medbay/shower/scene2/anim4/0001.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0002.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0003.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0004.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0005.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0006.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0007.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0008.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0009.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0010.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0011.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0012.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0013.jpg"
    function cum1
    pause .12
    "images/events/medbay/shower/scene2/anim4/0014.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0015.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0016.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0017.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0018.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0019.jpg"
    function wetsquish
    pause .12
    "images/events/medbay/shower/scene2/anim4/0020.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0021.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0022.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0023.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0024.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0025.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0026.jpg"
    function squish
    pause .12
    "images/events/medbay/shower/scene2/anim4/0027.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0028.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0029.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0030.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0031.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0032.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0033.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0034.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim4/0035.jpg"
    pause .12

image showerbug3:
    "images/events/medbay/shower/scene2/anim5/0001.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim5/0002.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim5/0003.jpg"
    function inside
    pause .12
    "images/events/medbay/shower/scene2/anim5/0004.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim5/0005.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim5/0006.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim5/0007.jpg"
    function s2
    pause .12
    "images/events/medbay/shower/scene2/anim5/0008.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim5/0009.jpg"
    pause .12
    repeat

image showerbug4:
    "images/events/medbay/shower/scene2/anim6/0001.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0002.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0003.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0004.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0005.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0006.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0007.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0008.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0009.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0010.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0011.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0012.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0013.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0014.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0015.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0016.jpg"
    function s1
    pause .12
    "images/events/medbay/shower/scene2/anim6/0017.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0018.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0019.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0020.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0021.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0022.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0023.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0024.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0025.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0026.jpg"
    function s2
    pause .12
    "images/events/medbay/shower/scene2/anim6/0027.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim6/0028.jpg"
    pause .12

image showerbug5:
    "images/events/medbay/shower/scene2/anim7/0001.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0002.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0003.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0004.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0005.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0006.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0007.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0008.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0009.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0010.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0011.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0012.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0013.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0014.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0015.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0016.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0017.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0018.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0019.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0020.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0021.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0022.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0023.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0024.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0025.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0026.jpg"
    function suck1
    pause .12
    "images/events/medbay/shower/scene2/anim7/0027.jpg"
    pause .12
    "images/events/medbay/shower/scene2/anim7/0028.jpg"
    pause .12

image medelcor1:
    "images/events/medbay/elcor/anim1/0001.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0002.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0003.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0004.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0005.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0006.jpg"
    function inside
    pause .12
    "images/events/medbay/elcor/anim1/0007.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0008.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0009.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0010.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0011.jpg"
    pause .12
    "images/events/medbay/elcor/anim1/0012.jpg"
    pause .12
    repeat

image medelcor2:
    "images/events/medbay/elcor/anim2/0001.jpg"
    pause .12
    "images/events/medbay/elcor/anim2/0002.jpg"
    pause .12
    "images/events/medbay/elcor/anim2/0003.jpg"
    pause .12
    "images/events/medbay/elcor/anim2/0004.jpg"
    function inside
    pause .12
    "images/events/medbay/elcor/anim2/0005.jpg"
    pause .12
    "images/events/medbay/elcor/anim2/0006.jpg"
    pause .12
    "images/events/medbay/elcor/anim2/0007.jpg"
    pause .12
    "images/events/medbay/elcor/anim2/0008.jpg"
    pause .12
    repeat

image medelcor3:
    "images/events/medbay/elcor/anim3/0001.jpg"
    pause .12
    "images/events/medbay/elcor/anim3/0002.jpg"
    pause .12
    "images/events/medbay/elcor/anim3/0003.jpg"
    pause .12
    "images/events/medbay/elcor/anim3/0004.jpg"
    function inside
    pause .12
    "images/events/medbay/elcor/anim3/0005.jpg"
    pause .12
    "images/events/medbay/elcor/anim3/0006.jpg"
    pause .12
    "images/events/medbay/elcor/anim3/0007.jpg"
    pause .12
    "images/events/medbay/elcor/anim3/0008.jpg"
    pause .12
    repeat

image medelcor4:
    "images/events/medbay/elcor/anim4/0001.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0002.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0003.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0004.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0005.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0006.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0007.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0008.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0009.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0010.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0011.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0012.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0013.jpg"
    function s2
    pause .12
    "images/events/medbay/elcor/anim4/0014.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0015.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0016.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0017.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0018.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0019.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0020.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0021.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0022.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0023.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0024.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0025.jpg"
    function slurp
    pause .12
    "images/events/medbay/elcor/anim4/0026.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0027.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0028.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0029.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0030.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0031.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0032.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0033.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0034.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0035.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0036.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0037.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0038.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0039.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0040.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0041.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0042.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0043.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0044.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0045.jpg"
    function slurp
    pause .12
    "images/events/medbay/elcor/anim4/0046.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0047.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0048.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0049.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0050.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0051.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0052.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0053.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0054.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0055.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0056.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0057.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0058.jpg"
    pause .12
    "images/events/medbay/elcor/anim4/0059.jpg"
    pause .12

image medelcor5:
    "images/events/medbay/elcor/anim5/0080.jpg"
    pause .12
    "images/events/medbay/elcor/anim5/0081.jpg"
    pause .12
    "images/events/medbay/elcor/anim5/0082.jpg"
    pause .12
    "images/events/medbay/elcor/anim5/0083.jpg"
    pause .12
    "images/events/medbay/elcor/anim5/0084.jpg"
    function splat2
    pause .12
    "images/events/medbay/elcor/anim5/0085.jpg"
    pause .12
    "images/events/medbay/elcor/anim5/0086.jpg"
    pause .12
    "images/events/medbay/elcor/anim5/0087.jpg"
    pause .12
    "images/events/medbay/elcor/anim5/0088.jpg"
    pause .12
    repeat

image medelcor6:
    "images/events/medbay/elcor/anim6/0059.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0060.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0061.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0062.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0063.jpg"
    function s4
    pause .12
    "images/events/medbay/elcor/anim6/0064.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0065.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0066.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0067.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0068.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0069.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0070.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0071.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0072.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0073.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0074.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0075.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0076.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0077.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0078.jpg"
    pause .12
    "images/events/medbay/elcor/anim6/0079.jpg"
    function s1
    pause .12

image medelcor7:
    "images/events/medbay/elcor/anim7/0090.jpg"
    pause .12
    "images/events/medbay/elcor/anim7/0091.jpg"
    pause .12
    "images/events/medbay/elcor/anim7/0092.jpg"
    pause .12
    "images/events/medbay/elcor/anim7/0093.jpg"
    pause .12
    "images/events/medbay/elcor/anim7/0094.jpg"
    pause .12
    "images/events/medbay/elcor/anim7/0095.jpg"
    function splat1
    pause .12
    "images/events/medbay/elcor/anim7/0096.jpg"
    pause .12
    "images/events/medbay/elcor/anim7/0097.jpg"
    pause .12
    repeat

image medelcor7alt:
    "images/events/medbay/elcor/anim7/0090.jpg"
    pause .08
    "images/events/medbay/elcor/anim7/0091.jpg"
    pause .08
    "images/events/medbay/elcor/anim7/0092.jpg"
    pause .08
    "images/events/medbay/elcor/anim7/0093.jpg"
    pause .08
    "images/events/medbay/elcor/anim7/0094.jpg"
    pause .08
    "images/events/medbay/elcor/anim7/0095.jpg"
    function splat1
    pause .08
    "images/events/medbay/elcor/anim7/0096.jpg"
    pause .08
    "images/events/medbay/elcor/anim7/0097.jpg"
    pause .08
    repeat

image medelcorcum1:
    "images/events/medbay/elcor/cum/0001.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0002.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0003.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0004.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0005.jpg"
    function cum1
    pause .12
    "images/events/medbay/elcor/cum/0006.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0007.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0008.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0009.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0010.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0011.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0012.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0013.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0014.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0015.jpg"
    function splat2
    pause .12
    "images/events/medbay/elcor/cum/0016.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0017.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0018.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0019.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0020.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0021.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0022.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0023.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0024.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0025.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0026.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0027.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0028.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0029.jpg"
    pause .12
    "images/events/medbay/elcor/cum/0030.jpg"
    pause .12

image medelcorcum2:
    "images/events/medbay/elcor/cum1/0089.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0090.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0091.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0092.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0093.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0094.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0095.jpg"
    function s2
    pause .12
    "images/events/medbay/elcor/cum1/0096.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0097.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0098.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0099.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0100.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0101.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0102.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0103.jpg"
    pause .12
    "images/events/medbay/elcor/cum1/0104.jpg"
    pause .12

image medelcorcum3:
    "images/events/medbay/elcor/cum2/0090.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0091.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0092.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0093.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0094.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0095.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0096.jpg"
    function splat1
    pause .12
    "images/events/medbay/elcor/cum2/0097.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0098.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0099.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0100.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0101.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0102.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0103.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0104.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0105.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0106.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0107.jpg"
    function splat
    pause .12
    "images/events/medbay/elcor/cum2/0108.jpg"
    pause .12
    "images/events/medbay/elcor/cum2/0109.jpg"
    pause .12

image lizsex1:
    "images/events/l2/front/mask1/0001.png"
    pause .12
    "images/events/l2/front/mask1/0002.png"
    pause .12
    "images/events/l2/front/mask1/0003.png"
    pause .12
    "images/events/l2/front/mask1/0004.png"
    pause .12
    "images/events/l2/front/mask1/0005.png"
    function inside
    pause .12
    "images/events/l2/front/mask1/0006.png"
    pause .12
    "images/events/l2/front/mask1/0007.png"
    pause .12
    "images/events/l2/front/mask1/0008.png"
    pause .12
    repeat

image lizsex2:
    "images/events/l2/front/mask2/0001.png"
    pause .12
    "images/events/l2/front/mask2/0002.png"
    pause .12
    "images/events/l2/front/mask2/0003.png"
    pause .12
    "images/events/l2/front/mask2/0004.png"
    pause .12
    "images/events/l2/front/mask2/0005.png"
    function inside
    pause .12
    "images/events/l2/front/mask2/0006.png"
    pause .12
    "images/events/l2/front/mask2/0007.png"
    pause .12
    "images/events/l2/front/mask2/0008.png"
    pause .12
    repeat

image lizsex3:
    "images/events/l2/front/nomask1/0001.png"
    pause .12
    "images/events/l2/front/nomask1/0002.png"
    pause .12
    "images/events/l2/front/nomask1/0003.png"
    pause .12
    "images/events/l2/front/nomask1/0004.png"
    pause .12
    "images/events/l2/front/nomask1/0005.png"
    function inside
    pause .12
    "images/events/l2/front/nomask1/0006.png"
    pause .12
    "images/events/l2/front/nomask1/0007.png"
    pause .12
    "images/events/l2/front/nomask1/0008.png"
    pause .12
    repeat

image lizsex4:
    "images/events/l2/front/nomask2/0001.png"
    pause .12
    "images/events/l2/front/nomask2/0002.png"
    pause .12
    "images/events/l2/front/nomask2/0003.png"
    pause .12
    "images/events/l2/front/nomask2/0004.png"
    pause .12
    "images/events/l2/front/nomask2/0005.png"
    function inside
    pause .12
    "images/events/l2/front/nomask2/0006.png"
    pause .12
    "images/events/l2/front/nomask2/0007.png"
    pause .12
    "images/events/l2/front/nomask2/0008.png"
    pause .12
    repeat

image lizcum1:
    "images/events/l2/front/maskcum/0001.png"
    pause .12
    "images/events/l2/front/maskcum/0002.png"
    pause .12
    "images/events/l2/front/maskcum/0003.png"
    pause .12
    "images/events/l2/front/maskcum/0004.png"
    function cum1
    pause .12
    "images/events/l2/front/maskcum/0005.png"
    pause .12
    "images/events/l2/front/maskcum/0006.png"
    pause .12
    "images/events/l2/front/maskcum/0007.png"
    pause .12
    "images/events/l2/front/maskcum/0008.png"
    function cum1
    pause .12
    "images/events/l2/front/maskcum/0009.png"
    pause .12
    "images/events/l2/front/maskcum/0010.png"
    pause .12
    "images/events/l2/front/maskcum/0011.png"
    pause .12
    "images/events/l2/front/maskcum/0012.png"
    pause .12
    "images/events/l2/front/maskcum/0013.png"
    pause .12
    "images/events/l2/front/maskcum/0014.png"
    function cum2
    pause .12
    "images/events/l2/front/maskcum/0015.png"
    pause .12
    "images/events/l2/front/maskcum/0016.png"
    pause .12
    "images/events/l2/front/maskcum/0017.png"
    pause .12
    "images/events/l2/front/maskcum/0018.png"
    pause .12
    "images/events/l2/front/maskcum/0019.png"
    pause .12
    "images/events/l2/front/maskcum/0020.png"
    pause .12
    "images/events/l2/front/maskcum/0021.png"
    pause .12
    "images/events/l2/front/maskcum/0022.png"
    pause .12
    "images/events/l2/front/maskcum/0023.png"
    pause .12
    "images/events/l2/front/maskcum/0024.png"
    pause .12
    "images/events/l2/front/maskcum/0025.png"
    pause .12

image lizcum2:
    "images/events/l2/front/nomaskcum1/0001.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0002.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0003.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0004.png"
    function cum1
    pause .12
    "images/events/l2/front/nomaskcum1/0005.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0006.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0007.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0008.png"
    function cum1
    pause .12
    "images/events/l2/front/nomaskcum1/0009.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0010.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0011.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0012.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0013.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0014.png"
    function cum2
    pause .12
    "images/events/l2/front/nomaskcum1/0015.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0016.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0017.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0018.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0019.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0020.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0021.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0022.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0023.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0024.png"
    pause .12
    "images/events/l2/front/nomaskcum1/0025.png"
    pause .12

image lizsex5:
    "images/events/l2/front/nomask3/0001.png"
    pause .12
    "images/events/l2/front/nomask3/0002.png"
    pause .12
    "images/events/l2/front/nomask3/0003.png"
    pause .12
    "images/events/l2/front/nomask3/0004.png"
    pause .12
    "images/events/l2/front/nomask3/0005.png"
    pause .12
    "images/events/l2/front/nomask3/0006.png"
    function slurp
    pause .12
    "images/events/l2/front/nomask3/0007.png"
    pause .12
    "images/events/l2/front/nomask3/0008.png"
    pause .12
    "images/events/l2/front/nomask3/0009.png"
    pause .12
    "images/events/l2/front/nomask3/0010.png"
    pause .12
    "images/events/l2/front/nomask3/0011.png"
    pause .12
    "images/events/l2/front/nomask3/0012.png"
    pause .12
    "images/events/l2/front/nomask3/0013.png"
    pause .12
    "images/events/l2/front/nomask3/0014.png"
    pause .12
    "images/events/l2/front/nomask3/0015.png"
    pause .12
    "images/events/l2/front/nomask3/0016.png"
    function s2
    pause .12
    "images/events/l2/front/nomask3/0017.png"
    pause .12
    "images/events/l2/front/nomask3/0018.png"
    pause .12
    "images/events/l2/front/nomask3/0019.png"
    pause .12
    "images/events/l2/front/nomask3/0020.png"
    pause .12
    repeat

image lizsex6:
    "images/events/l2/front/nomask4/0001.png"
    pause .12
    "images/events/l2/front/nomask4/0002.png"
    pause .12
    "images/events/l2/front/nomask4/0003.png"
    pause .12
    "images/events/l2/front/nomask4/0004.png"
    pause .12
    "images/events/l2/front/nomask4/0005.png"
    pause .12
    "images/events/l2/front/nomask4/0006.png"
    function wetsquish
    pause .12
    "images/events/l2/front/nomask4/0007.png"
    pause .12
    "images/events/l2/front/nomask4/0008.png"
    pause .12
    "images/events/l2/front/nomask4/0009.png"
    pause .12
    "images/events/l2/front/nomask4/0010.png"
    pause .12
    "images/events/l2/front/nomask4/0011.png"
    pause .12
    "images/events/l2/front/nomask4/0012.png"
    pause .12
    "images/events/l2/front/nomask4/0013.png"
    pause .12
    "images/events/l2/front/nomask4/0014.png"
    pause .12
    "images/events/l2/front/nomask4/0015.png"
    pause .12

image lizsex7:
    "images/events/l2/front/nomask5/0015.png"
    pause .12
    "images/events/l2/front/nomask5/0016.png"
    pause .12
    "images/events/l2/front/nomask5/0017.png"
    pause .12
    "images/events/l2/front/nomask5/0018.png"
    function wetsquish
    pause .12
    "images/events/l2/front/nomask5/0019.png"
    pause .12
    repeat

image lizcum3:
    "images/events/l2/front/nomaskcum2/0001.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0002.png"
    function splat1
    pause .12
    "images/events/l2/front/nomaskcum2/0003.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0004.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0005.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0006.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0007.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0008.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0009.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0010.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0011.png"
    function splat1
    pause .12
    "images/events/l2/front/nomaskcum2/0012.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0013.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0014.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0015.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0016.png"
    function splat2
    pause .12
    "images/events/l2/front/nomaskcum2/0017.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0018.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0019.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0020.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0021.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0022.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0023.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0024.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0025.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0026.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0027.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0028.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0029.png"
    pause .12
    "images/events/l2/front/nomaskcum2/0030.png"
    pause .12

image lizcum4:
    "images/events/l2/front/nomaskcum3/0015.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0016.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0017.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0018.png"
    function choke3
    pause .12
    "images/events/l2/front/nomaskcum3/0019.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0020.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0021.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0022.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0023.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0024.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0025.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0026.png"
    function splat2
    pause .12
    "images/events/l2/front/nomaskcum3/0027.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0028.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0029.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0030.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0031.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0032.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0033.png"
    function wetsquish
    pause .12
    "images/events/l2/front/nomaskcum3/0034.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0035.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0036.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0037.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0038.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0039.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0040.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0041.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0042.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0043.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0044.png"
    function splat1
    pause .12
    "images/events/l2/front/nomaskcum3/0045.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0046.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0047.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0048.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0049.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0050.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0051.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0052.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0053.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0054.png"
    pause .12
    "images/events/l2/front/nomaskcum3/0055.png"
    pause .12

image liz1f1:
    "images/events/l1/front/mask1/0001.png"
    pause .12
    "images/events/l1/front/mask1/0002.png"
    pause .12
    "images/events/l1/front/mask1/0003.png"
    pause .12
    "images/events/l1/front/mask1/0004.png"
    pause .12
    "images/events/l1/front/mask1/0005.png"
    pause .12
    "images/events/l1/front/mask1/0006.png"
    pause .12
    "images/events/l1/front/mask1/0007.png"
    function s1
    pause .12
    "images/events/l1/front/mask1/0008.png"
    pause .12
    "images/events/l1/front/mask1/0009.png"
    pause .12
    repeat

image liz1f2:
    "images/events/l1/front/mask2/0001.png"
    pause .12
    "images/events/l1/front/mask2/0002.png"
    pause .12
    "images/events/l1/front/mask2/0003.png"
    pause .12
    "images/events/l1/front/mask2/0004.png"
    pause .12
    "images/events/l1/front/mask2/0005.png"
    function inside
    pause .12
    "images/events/l1/front/mask2/0006.png"
    pause .12
    "images/events/l1/front/mask2/0007.png"
    pause .12
    repeat

image liz1f3:
    "images/events/l1/front/nomask1/0001.png"
    pause .12
    "images/events/l1/front/nomask1/0002.png"
    pause .12
    "images/events/l1/front/nomask1/0003.png"
    pause .12
    "images/events/l1/front/nomask1/0004.png"
    pause .12
    "images/events/l1/front/nomask1/0005.png"
    function inside
    pause .12
    "images/events/l1/front/nomask1/0006.png"
    pause .12
    "images/events/l1/front/nomask1/0007.png"
    pause .12
    repeat

image liz1f4:
    "images/events/l1/front/nomask2/0001.png"
    pause .12
    "images/events/l1/front/nomask2/0002.png"
    pause .12
    "images/events/l1/front/nomask2/0003.png"
    pause .12
    "images/events/l1/front/nomask2/0004.png"
    pause .12
    "images/events/l1/front/nomask2/0005.png"
    pause .12
    "images/events/l1/front/nomask2/0006.png"
    function suck1
    pause .12
    "images/events/l1/front/nomask2/0007.png"
    pause .12
    "images/events/l1/front/nomask2/0008.png"
    pause .12
    "images/events/l1/front/nomask2/0009.png"
    pause .12
    "images/events/l1/front/nomask2/0010.png"
    pause .12
    repeat

image liz1f5:
    "images/events/l1/front/nomask3/0025.png"
    pause .12
    "images/events/l1/front/nomask3/0026.png"
    pause .12
    "images/events/l1/front/nomask3/0027.png"
    pause .12
    "images/events/l1/front/nomask3/0028.png"
    function choke3
    pause .12
    "images/events/l1/front/nomask3/0029.png"
    pause .12
    "images/events/l1/front/nomask3/0030.png"
    function splat2
    pause .12
    repeat

image liz1f6:
    "images/events/l1/front/nomask4/0025.png"
    pause .12
    "images/events/l1/front/nomask4/0026.png"
    pause .12
    "images/events/l1/front/nomask4/0027.png"
    pause .12
    "images/events/l1/front/nomask4/0028.png"
    function choke3
    pause .12
    "images/events/l1/front/nomask4/0029.png"
    pause .12
    "images/events/l1/front/nomask4/0030.png"
    pause .12
    "images/events/l1/front/nomask4/0031.png"
    pause .12
    "images/events/l1/front/nomask4/0032.png"
    pause .12
    "images/events/l1/front/nomask4/0033.png"
    pause .12
    "images/events/l1/front/nomask4/0034.png"
    pause .12
    "images/events/l1/front/nomask4/0035.png"
    pause .12
    "images/events/l1/front/nomask4/0036.png"
    pause .12
    "images/events/l1/front/nomask4/0037.png"
    pause .12
    "images/events/l1/front/nomask4/0038.png"
    function suck4
    pause .12
    "images/events/l1/front/nomask4/0039.png"
    pause .12
    "images/events/l1/front/nomask4/0040.png"
    pause .12
    "images/events/l1/front/nomask4/0041.png"
    pause .12
    "images/events/l1/front/nomask4/0042.png"
    pause .12
    "images/events/l1/front/nomask4/0043.png"
    pause .12
    "images/events/l1/front/nomask4/0044.png"
    pause .12
    "images/events/l1/front/nomask4/0045.png"
    pause .12
    "images/events/l1/front/nomask4/0046.png"
    pause .12
    "images/events/l1/front/nomask4/0047.png"
    function wetsquish
    pause .12
    "images/events/l1/front/nomask4/0048.png"
    pause .12
    "images/events/l1/front/nomask4/0049.png"
    pause .12
    "images/events/l1/front/nomask4/0050.png"
    pause .12

image liz1f7:
    "images/events/l1/front/nomask5/0050.png"
    pause .12
    "images/events/l1/front/nomask5/0051.png"
    pause .12
    "images/events/l1/front/nomask5/0052.png"
    pause .12
    "images/events/l1/front/nomask5/0053.png"
    pause .12
    "images/events/l1/front/nomask5/0054.png"
    pause .12
    "images/events/l1/front/nomask5/0055.png"
    function suck1
    pause .12
    "images/events/l1/front/nomask5/0056.png"
    pause .12
    "images/events/l1/front/nomask5/0057.png"
    pause .12
    repeat

image liz1f8:
    "images/events/l1/front/damaged1/0001.png"
    pause .12
    "images/events/l1/front/damaged1/0002.png"
    pause .12
    "images/events/l1/front/damaged1/0003.png"
    pause .12
    "images/events/l1/front/damaged1/0004.png"
    pause .12
    "images/events/l1/front/damaged1/0005.png"
    pause .12
    "images/events/l1/front/damaged1/0006.png"
    function suck1
    pause .12
    "images/events/l1/front/damaged1/0007.png"
    pause .12
    "images/events/l1/front/damaged1/0008.png"
    pause .12
    "images/events/l1/front/damaged1/0009.png"
    pause .12
    "images/events/l1/front/damaged1/0010.png"
    pause .12
    repeat

image liz1f9:
    "images/events/l1/front/nomask6/0011.png"
    pause .12
    "images/events/l1/front/nomask6/0012.png"
    pause .12
    "images/events/l1/front/nomask6/0013.png"
    pause .12
    "images/events/l1/front/nomask6/0014.png"
    pause .12
    "images/events/l1/front/nomask6/0015.png"
    pause .12
    "images/events/l1/front/nomask6/0016.png"
    pause .12
    "images/events/l1/front/nomask6/0017.png"
    pause .12
    "images/events/l1/front/nomask6/0018.png"
    pause .12
    "images/events/l1/front/nomask6/0019.png"
    pause .12
    "images/events/l1/front/nomask6/0020.png"
    pause .12
    "images/events/l1/front/nomask6/0021.png"
    pause .12
    "images/events/l1/front/nomask6/0022.png"
    pause .12
    "images/events/l1/front/nomask6/0023.png"
    pause .12
    "images/events/l1/front/nomask6/0024.png"
    pause .12
    "images/events/l1/front/nomask6/0025.png"
    pause .12

image liz1fcum1:
    "images/events/l1/front/maskcum/0001.png"
    pause .12
    "images/events/l1/front/maskcum/0002.png"
    pause .12
    "images/events/l1/front/maskcum/0003.png"
    pause .12
    "images/events/l1/front/maskcum/0004.png"
    pause .12
    "images/events/l1/front/maskcum/0005.png"
    function cum1
    pause .12
    "images/events/l1/front/maskcum/0006.png"
    pause .12
    "images/events/l1/front/maskcum/0007.png"
    pause .12
    "images/events/l1/front/maskcum/0008.png"
    pause .12
    "images/events/l1/front/maskcum/0009.png"
    pause .12
    "images/events/l1/front/maskcum/0010.png"
    pause .12
    "images/events/l1/front/maskcum/0011.png"
    pause .12
    "images/events/l1/front/maskcum/0012.png"
    function cum1
    pause .12
    "images/events/l1/front/maskcum/0013.png"
    pause .12
    "images/events/l1/front/maskcum/0014.png"
    pause .12
    "images/events/l1/front/maskcum/0015.png"
    pause .12
    "images/events/l1/front/maskcum/0016.png"
    pause .12
    "images/events/l1/front/maskcum/0017.png"
    pause .12
    "images/events/l1/front/maskcum/0018.png"
    pause .12
    "images/events/l1/front/maskcum/0019.png"
    pause .12
    "images/events/l1/front/maskcum/0020.png"
    pause .12
    "images/events/l1/front/maskcum/0021.png"
    pause .12
    "images/events/l1/front/maskcum/0022.png"
    pause .12

image liz1fcum2:
    "images/events/l1/front/nomaskcum1/0001.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0002.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0003.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0004.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0005.png"
    function cum1
    pause .12
    "images/events/l1/front/nomaskcum1/0006.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0007.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0008.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0009.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0010.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0011.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0012.png"
    function cum1
    pause .12
    "images/events/l1/front/nomaskcum1/0013.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0014.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0015.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0016.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0017.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0018.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0019.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0020.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0021.png"
    pause .12
    "images/events/l1/front/nomaskcum1/0022.png"
    pause .12

image liz1fcum3:
    "images/events/l1/front/nomaskcum2/0050.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0051.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0052.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0053.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0054.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0055.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0056.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0057.png"
    function cum1
    pause .12
    "images/events/l1/front/nomaskcum2/0058.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0059.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0060.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0061.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0062.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0063.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0064.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0065.png"
    function cum1
    pause .12
    "images/events/l1/front/nomaskcum2/0066.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0067.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0068.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0069.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0070.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0071.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0072.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0073.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0074.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0075.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0076.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0077.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0078.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0079.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0080.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0081.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0082.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0083.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0084.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0085.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0086.png"
    function cough
    pause .12
    "images/events/l1/front/nomaskcum2/0087.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0088.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0089.png"
    function squish
    pause .12
    "images/events/l1/front/nomaskcum2/0090.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0091.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0092.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0093.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0094.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0095.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0096.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0097.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0098.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0099.png"
    pause .12
    "images/events/l1/front/nomaskcum2/0100.png"
    pause .12

image liz1b1:
    "images/events/l1/back/damaged1/0011.png"
    pause .12
    "images/events/l1/back/damaged1/0012.png"
    pause .12
    "images/events/l1/back/damaged1/0013.png"
    pause .12
    "images/events/l1/back/damaged1/0014.png"
    pause .12
    "images/events/l1/back/damaged1/0015.png"
    pause .12
    "images/events/l1/back/damaged1/0016.png"
    pause .12
    "images/events/l1/back/damaged1/0017.png"
    function s2
    pause .12
    "images/events/l1/back/damaged1/0018.png"
    pause .12
    "images/events/l1/back/damaged1/0019.png"
    pause .12
    "images/events/l1/back/damaged1/0020.png"
    pause .12
    "images/events/l1/back/damaged1/0021.png"
    pause .12
    "images/events/l1/back/damaged1/0022.png"
    pause .12
    "images/events/l1/back/damaged1/0023.png"
    pause .12
    "images/events/l1/back/damaged1/0024.png"
    pause .12
    "images/events/l1/back/damaged1/0025.png"
    pause .12
    "images/events/l1/back/damaged1/0026.png"
    pause .12
    "images/events/l1/back/damaged1/0027.png"
    pause .12
    "images/events/l1/back/damaged1/0028.png"
    pause .12
    "images/events/l1/back/damaged1/0029.png"
    pause .12
    "images/events/l1/back/damaged1/0030.png"
    pause .12
    "images/events/l1/back/damaged1/0031.png"
    function s1
    pause .12
    "images/events/l1/back/damaged1/0032.png"
    pause .12
    "images/events/l1/back/damaged1/0033.png"
    pause .12
    "images/events/l1/back/damaged1/0034.png"
    pause .12
    "images/events/l1/back/damaged1/0035.png"
    pause .12
    "images/events/l1/back/damaged1/0036.png"
    pause .12
    "images/events/l1/back/damaged1/0037.png"
    pause .12
    "images/events/l1/back/damaged1/0038.png"
    pause .12
    "images/events/l1/back/damaged1/0039.png"
    function fart2
    pause .12
    "images/events/l1/back/damaged1/0040.png"
    pause .12

image liz1b2:
    "images/events/l1/back/damaged2/0042.png"
    pause .12
    "images/events/l1/back/damaged2/0043.png"
    pause .12
    "images/events/l1/back/damaged2/0044.png"
    pause .12
    "images/events/l1/back/damaged2/0045.png"
    function slap1
    pause .12
    "images/events/l1/back/damaged2/0046.png"
    pause .12
    "images/events/l1/back/damaged2/0047.png"
    pause .12
    repeat

image liz1b3:
    "images/events/l1/back/damaged3/0025.png"
    pause .12
    "images/events/l1/back/damaged3/0026.png"
    pause .12
    "images/events/l1/back/damaged3/0027.png"
    pause .12
    "images/events/l1/back/damaged3/0028.png"
    pause .12
    "images/events/l1/back/damaged3/0029.png"
    pause .12
    "images/events/l1/back/damaged3/0030.png"
    pause .12
    "images/events/l1/back/damaged3/0031.png"
    function s1
    pause .12
    "images/events/l1/back/damaged3/0032.png"
    pause .12
    "images/events/l1/back/damaged3/0033.png"
    pause .12
    "images/events/l1/back/damaged3/0034.png"
    pause .12
    "images/events/l1/back/damaged3/0035.png"
    pause .12
    "images/events/l1/back/damaged3/0036.png"
    pause .12
    "images/events/l1/back/damaged3/0037.png"
    pause .12
    "images/events/l1/back/damaged3/0038.png"
    pause .12
    "images/events/l1/back/damaged3/0039.png"
    function fart2
    pause .12
    "images/events/l1/back/damaged3/0040.png"
    pause .12

image liz1b4:
    "images/events/l1/back/damaged4/0042.png"
    pause .12
    "images/events/l1/back/damaged4/0043.png"
    pause .12
    "images/events/l1/back/damaged4/0044.png"
    pause .12
    "images/events/l1/back/damaged4/0045.png"
    function slap1
    pause .12
    "images/events/l1/back/damaged4/0046.png"
    pause .12
    "images/events/l1/back/damaged4/0047.png"
    pause .12
    repeat

image liz1b5:
    "images/events/l1/back/damaged5/0048.png"
    pause .12
    "images/events/l1/back/damaged5/0049.png"
    pause .12
    "images/events/l1/back/damaged5/0050.png"
    function slap2
    pause .12
    "images/events/l1/back/damaged5/0051.png"
    pause .12
    "images/events/l1/back/damaged5/0052.png"
    pause .12
    repeat

image liz1bcum1:
    "images/events/l1/back/damagedcum1/0048.png"
    pause .12
    "images/events/l1/back/damagedcum1/0049.png"
    pause .12
    "images/events/l1/back/damagedcum1/0050.png"
    pause .12
    "images/events/l1/back/damagedcum1/0051.png"
    pause .12
    "images/events/l1/back/damagedcum1/0052.png"
    pause .12
    "images/events/l1/back/damagedcum1/0053.png"
    function cum1
    pause .12
    "images/events/l1/back/damagedcum1/0054.png"
    pause .12
    "images/events/l1/back/damagedcum1/0055.png"
    pause .12
    "images/events/l1/back/damagedcum1/0056.png"
    pause .12
    "images/events/l1/back/damagedcum1/0057.png"
    function cum1
    pause .12
    "images/events/l1/back/damagedcum1/0058.png"
    pause .12
    "images/events/l1/back/damagedcum1/0059.png"
    pause .12
    "images/events/l1/back/damagedcum1/0060.png"
    pause .12
    "images/events/l1/back/damagedcum1/0061.png"
    function slap0
    pause .12
    "images/events/l1/back/damagedcum1/0062.png"
    pause .12
    "images/events/l1/back/damagedcum1/0063.png"
    pause .12
    "images/events/l1/back/damagedcum1/0064.png"
    pause .12
    "images/events/l1/back/damagedcum1/0065.png"
    pause .12

image liz1bcum2:
    "images/events/l1/back/damagedcum2/0053.png"
    pause .12
    "images/events/l1/back/damagedcum2/0054.png"
    pause .12
    "images/events/l1/back/damagedcum2/0055.png"
    pause .12
    "images/events/l1/back/damagedcum2/0056.png"
    pause .12
    "images/events/l1/back/damagedcum2/0057.png"
    function splat
    pause .12
    "images/events/l1/back/damagedcum2/0058.png"
    pause .12
    "images/events/l1/back/damagedcum2/0059.png"
    pause .12
    "images/events/l1/back/damagedcum2/0060.png"
    pause .12
    "images/events/l1/back/damagedcum2/0061.png"
    pause .12
    "images/events/l1/back/damagedcum2/0062.png"
    pause .12
    "images/events/l1/back/damagedcum2/0063.png"
    pause .12
    "images/events/l1/back/damagedcum2/0064.png"
    pause .12
    "images/events/l1/back/damagedcum2/0065.png"
    pause .12
    "images/events/l1/back/damagedcum2/0066.png"
    function splat2
    pause .12
    "images/events/l1/back/damagedcum2/0067.png"
    pause .12
    "images/events/l1/back/damagedcum2/0068.png"
    pause .12
    "images/events/l1/back/damagedcum2/0069.png"
    pause .12
    "images/events/l1/back/damagedcum2/0070.png"
    pause .12
    "images/events/l1/back/damagedcum2/0071.png"
    pause .12
    "images/events/l1/back/damagedcum2/0072.png"
    pause .12
    "images/events/l1/back/damagedcum2/0073.png"
    pause .12
    "images/events/l1/back/damagedcum2/0074.png"
    function splat1
    pause .12
    "images/events/l1/back/damagedcum2/0075.png"
    pause .12
    "images/events/l1/back/damagedcum2/0076.png"
    pause .12
    "images/events/l1/back/damagedcum2/0077.png"
    pause .12
    "images/events/l1/back/damagedcum2/0078.png"
    pause .12
    "images/events/l1/back/damagedcum2/0079.png"
    pause .12
    "images/events/l1/back/damagedcum2/0080.png"
    function splat1
    pause .12
    "images/events/l1/back/damagedcum2/0081.png"
    pause .12
    "images/events/l1/back/damagedcum2/0082.png"
    pause .12
    "images/events/l1/back/damagedcum2/0083.png"
    pause .12
    "images/events/l1/back/damagedcum2/0084.png"
    pause .12
    "images/events/l1/back/damagedcum2/0085.png"
    pause .12
    "images/events/l1/back/damagedcum2/0086.png"
    pause .12
    "images/events/l1/back/damagedcum2/0087.png"
    pause .12
    "images/events/l1/back/damagedcum2/0088.png"
    pause .12
    "images/events/l1/back/damagedcum2/0089.png"
    pause .12
    "images/events/l1/back/damagedcum2/0090.png"
    pause .12
    "images/events/l1/back/damagedcum2/0091.png"
    pause .12
    "images/events/l1/back/damagedcum2/0092.png"
    pause .12
    "images/events/l1/back/damagedcum2/0093.png"
    pause .12
    "images/events/l1/back/damagedcum2/0094.png"
    pause .12
    "images/events/l1/back/damagedcum2/0095.png"
    pause .12

image pooldry:
    "images/events/pool/dry/0015.jpg"
    pause .12
    "images/events/pool/dry/0016.jpg"
    pause .12
    "images/events/pool/dry/0017.jpg"
    pause .12
    "images/events/pool/dry/0018.jpg"
    pause .12
    "images/events/pool/dry/0019.jpg"
    pause .12
    "images/events/pool/dry/0020.jpg"
    pause .12
    "images/events/pool/dry/0021.jpg"
    pause .12
    "images/events/pool/dry/0022.jpg"
    pause .12
    "images/events/pool/dry/0023.jpg"
    pause .12
    "images/events/pool/dry/0024.jpg"
    pause .12

# ------------------ VENTS ANIMATIONS START --------------------------

image nesttrans1:
    "images/nest/trans1/0095.jpg"
    pause .12
    "images/nest/trans1/0096.jpg"
    pause .12
    "images/nest/trans1/0097.jpg"
    pause .12
    "images/nest/trans1/0098.jpg"
    pause .12
    "images/nest/trans1/0099.jpg"
    pause .12
    "images/nest/trans1/0100.jpg"
    pause .12
    "images/nest/trans1/0101.jpg"
    pause .12
    "images/nest/trans1/0102.jpg"
    pause .12
    "images/nest/trans1/0103.jpg"
    pause .12
    "images/nest/trans1/0104.jpg"
    function s4
    pause .12
    "images/nest/trans1/0105.jpg"
    pause .12
    "images/nest/trans1/0106.jpg"
    pause .12
    "images/nest/trans1/0107.jpg"
    pause .12

image neststruggle:
    "images/nest/trans1/0108.jpg"
    pause .12
    "images/nest/trans1/0109.jpg"
    pause .12
    "images/nest/trans1/0110.jpg"
    pause .12
    "images/nest/trans1/0111.jpg"
    pause .12
    "images/nest/trans1/0112.jpg"
    pause .12
    "images/nest/trans1/0113.jpg"
    pause .12
    "images/nest/trans1/0114.jpg"
    pause .12
    "images/nest/trans1/0115.jpg"
    pause .12
    repeat

image nesttrans1alt:
    "images/nest/trans1/0116.jpg"
    pause .12
    "images/nest/trans1/0117.jpg"
    pause .12
    "images/nest/trans1/0118.jpg"
    pause .12
    "images/nest/trans1/0119.jpg"
    pause .12
    "images/nest/trans1/0120.jpg"
    pause .12
    "images/nest/trans1/0121.jpg"
    pause .12
    "images/nest/trans1/0122.jpg"
    pause .12
    "images/nest/trans1/0123.jpg"
    pause .12
    "images/nest/trans1/0124.jpg"
    pause .12
    "images/nest/trans1/0125.jpg"
    pause .12
    "images/nest/trans1/0126.jpg"
    pause .12
    "images/nest/trans1/0127.jpg"
    pause .12

image nesttrans2:
    "images/nest/trans2/0130.jpg"
    pause .12
    "images/nest/trans2/0131.jpg"
    pause .12
    "images/nest/trans2/0132.jpg"
    pause .12
    "images/nest/trans2/0133.jpg"
    pause .12
    "images/nest/trans2/0134.jpg"
    pause .12
    "images/nest/trans2/0135.jpg"
    pause .12
    "images/nest/trans2/0136.jpg"
    pause .12
    "images/nest/trans2/0137.jpg"
    pause .12
    "images/nest/trans2/0138.jpg"
    pause .12
    "images/nest/trans2/0139.jpg"
    function tier
    pause .12
    "images/nest/trans2/0140.jpg"
    pause .12
    "images/nest/trans2/0141.jpg"
    pause .12
    "images/nest/trans2/0142.jpg"
    pause .12
    "images/nest/trans2/0143.jpg"
    pause .12
    "images/nest/trans2/0144.jpg"
    pause .12
    "images/nest/trans2/0145.jpg"
    pause .12
    "images/nest/trans2/0146.jpg"
    pause .12
    "images/nest/trans2/0147.jpg"
    pause .12
    "images/nest/trans2/0148.jpg"
    pause .12
    "images/nest/trans2/0149.jpg"
    pause .12
    "images/nest/trans2/0150.jpg"
    pause .12

image nesttrans2alt:
    "images/nest/trans2/0151.jpg"
    pause .12
    "images/nest/trans2/0152.jpg"
    function s1
    pause .12
    "images/nest/trans2/0153.jpg"
    pause .12
    "images/nest/trans2/0154.jpg"
    pause .12
    "images/nest/trans2/0155.jpg"
    pause .12
    "images/nest/trans2/0156.jpg"
    pause .12
    "images/nest/trans2/0157.jpg"
    function s2
    pause .12
    "images/nest/trans2/0158.jpg"
    pause .12
    "images/nest/trans2/0159.jpg"
    pause .12
    "images/nest/trans2/0160.jpg"
    pause .12
    "images/nest/trans2/0161.jpg"
    pause .12
    "images/nest/trans2/0162.jpg"
    pause .12
    "images/nest/trans2/0163.jpg"
    function s4
    pause .12
    "images/nest/trans2/0164.jpg"
    pause .12
    "images/nest/trans2/0165.jpg"
    pause .12
    "images/nest/trans2/0166.jpg"
    pause .12
    "images/nest/trans2/0167.jpg"
    function fart2
    pause .12
    "images/nest/trans2/0168.jpg"
    pause .12
    "images/nest/trans2/0169.jpg"
    pause .12
    "images/nest/trans2/0170.jpg"
    pause .12

image nestloop1:
    "images/nest/loop1/0170.jpg"
    pause .12
    "images/nest/loop1/0171.jpg"
    pause .12
    "images/nest/loop1/0172.jpg"
    pause .12
    "images/nest/loop1/0173.jpg"
    function s2
    pause .12
    "images/nest/loop1/0174.jpg"
    pause .12
    "images/nest/loop1/0175.jpg"
    pause .12
    "images/nest/loop1/0176.jpg"
    function s1
    pause .12
    "images/nest/loop1/0177.jpg"
    pause .12
    "images/nest/loop1/0178.jpg"
    pause .12
    "images/nest/loop1/0179.jpg"
    pause .12
    "images/nest/loop1/0180.jpg"
    pause .12
    "images/nest/loop1/0181.jpg"
    function splat
    pause .12
    "images/nest/loop1/0182.jpg"
    pause .12
    "images/nest/loop1/0183.jpg"
    pause .12
    repeat

image nesttrans3:
    "images/nest/trans3/0170.jpg"
    pause .12
    "images/nest/trans3/0171.jpg"
    pause .12
    "images/nest/trans3/0172.jpg"
    pause .12
    "images/nest/trans3/0173.jpg"
    function s2
    pause .12
    "images/nest/trans3/0174.jpg"
    pause .12
    "images/nest/trans3/0175.jpg"
    pause .12
    "images/nest/trans3/0176.jpg"
    function s1
    pause .12
    "images/nest/trans3/0177.jpg"
    pause .12
    "images/nest/trans3/0178.jpg"
    pause .12
    "images/nest/trans3/0179.jpg"
    function fart2
    pause .12
    "images/nest/trans3/0180.jpg"
    pause .12
    "images/nest/trans3/0181.jpg"
    pause .12
    "images/nest/trans3/0182.jpg"
    pause .12
    "images/nest/trans3/0183.jpg"
    pause .12
    "images/nest/trans3/0184.jpg"
    pause .12

image nesttrans3alt:
    "images/nest/trans3/0185.jpg"
    pause .12
    "images/nest/trans3/0186.jpg"
    pause .12
    "images/nest/trans3/0187.jpg"
    pause .12
    "images/nest/trans3/0188.jpg"
    pause .12
    "images/nest/trans3/0189.jpg"
    pause .12
    "images/nest/trans3/0190.jpg"
    pause .12
    "images/nest/trans3/0190.jpg"
    pause .12
    "images/nest/trans3/0191.jpg"
    pause .12
    "images/nest/trans3/0192.jpg"
    pause .12
    "images/nest/trans3/0193.jpg"
    pause .12
    "images/nest/trans3/0194.jpg"
    pause .12
    "images/nest/trans3/0195.jpg"
    pause .12
    "images/nest/trans3/0196.jpg"
    pause .12
    "images/nest/trans3/0197.jpg"
    pause .12

image nestloop2:
    "images/nest/loop2/0130.jpg"
    pause .12
    "images/nest/loop2/0131.jpg"
    pause .12
    "images/nest/loop2/0132.jpg"
    pause .12
    "images/nest/loop2/0133.jpg"
    pause .12
    "images/nest/loop2/0134.jpg"
    pause .12
    "images/nest/loop2/0135.jpg"
    pause .12
    "images/nest/loop2/0136.jpg"
    pause .12
    "images/nest/loop2/0137.jpg"
    pause .12
    "images/nest/loop2/0138.jpg"
    pause .12
    "images/nest/loop2/0139.jpg"
    pause .12
    "images/nest/loop2/0140.jpg"
    pause .12
    "images/nest/loop2/0141.jpg"
    pause .12
    repeat

image nesttrans4:
    "images/nest/trans4/0150.jpg"
    pause .12
    "images/nest/trans4/0151.jpg"
    pause .12
    "images/nest/trans4/0152.jpg"
    pause .12
    "images/nest/trans4/0153.jpg"
    pause .12
    "images/nest/trans4/0154.jpg"
    pause .12
    "images/nest/trans4/0155.jpg"
    pause .12
    "images/nest/trans4/0156.jpg"
    pause .12
    "images/nest/trans4/0157.jpg"
    pause .12
    "images/nest/trans4/0158.jpg"
    pause .12
    "images/nest/trans4/0159.jpg"
    pause .12
    "images/nest/trans4/0160.jpg"
    pause .12
    "images/nest/trans4/0161.jpg"
    pause .12
    "images/nest/trans4/0162.jpg"
    pause .12
    "images/nest/trans4/0163.jpg"
    pause .12
    "images/nest/trans4/0164.jpg"
    pause .12
    "images/nest/trans4/0165.jpg"
    pause .12
    "images/nest/trans4/0166.jpg"
    function n1
    pause .12
    "images/nest/trans4/0167.jpg"
    pause .12
    "images/nest/trans4/0168.jpg"
    pause .12
    "images/nest/trans4/0169.jpg"
    pause .12
    "images/nest/trans4/0170.jpg"
    pause .12
    "images/nest/trans4/0171.jpg"
    pause .12
    "images/nest/trans4/0172.jpg"
    pause .12
    "images/nest/trans4/0173.jpg"
    pause .12
    "images/nest/trans4/0174.jpg"
    pause .12
    "images/nest/trans4/0175.jpg"
    pause .12
    "images/nest/trans4/0176.jpg"
    pause .12
    "images/nest/trans4/0177.jpg"
    pause .12

image nesttrans5:
    "images/nest/trans5/0177.jpg"
    pause .12
    function n1
    "images/nest/trans5/0178.jpg"
    pause .12
    "images/nest/trans5/0179.jpg"
    pause .12
    "images/nest/trans5/0180.jpg"
    pause .12
    "images/nest/trans5/0181.jpg"
    pause .12
    "images/nest/trans5/0182.jpg"
    pause .12
    "images/nest/trans5/0183.jpg"
    pause .12
    "images/nest/trans5/0184.jpg"
    pause .12
    "images/nest/trans5/0185.jpg"
    pause .12
    "images/nest/trans5/0186.jpg"
    pause .12
    "images/nest/trans5/0187.jpg"
    pause .12
    "images/nest/trans5/0188.jpg"
    pause .12
    "images/nest/trans5/0189.jpg"
    pause .12
    "images/nest/trans5/0190.jpg"
    pause .12
    "images/nest/trans5/0190.jpg"
    pause .12
    "images/nest/trans5/0191.jpg"
    pause .12
    "images/nest/trans5/0192.jpg"
    pause .12
    "images/nest/trans5/0193.jpg"
    pause .12
    "images/nest/trans5/0194.jpg"
    pause .12
    "images/nest/trans5/0195.jpg"
    pause .12
    "images/nest/trans5/0196.jpg"
    pause .12
    "images/nest/trans5/0197.jpg"
    pause .12
    "images/nest/trans5/0198.jpg"
    pause .12
    "images/nest/trans5/0199.jpg"
    pause .12
    "images/nest/trans5/0200.jpg"
    pause .12
    "images/nest/trans5/0201.jpg"
    pause .12
    "images/nest/trans5/0202.jpg"
    pause .12
    "images/nest/trans5/0203.jpg"
    pause .12
    "images/nest/trans5/0204.jpg"
    pause .12
    "images/nest/trans5/0205.jpg"
    pause .12
    "images/nest/trans5/0206.jpg"
    pause .12
    "images/nest/trans5/0207.jpg"
    pause .12
    "images/nest/trans5/0208.jpg"
    pause .12
    "images/nest/trans5/0209.jpg"
    function s2
    pause .12
    "images/nest/trans5/0210.jpg"
    pause .12

image nesttrans6:
    "images/nest/trans6/0210.jpg"
    pause .12
    "images/nest/trans6/0211.jpg"
    pause .12
    "images/nest/trans6/0212.jpg"
    pause .12
    "images/nest/trans6/0213.jpg"
    pause .12
    "images/nest/trans6/0214.jpg"
    pause .12
    "images/nest/trans6/0215.jpg"
    pause .12
    "images/nest/trans6/0216.jpg"
    pause .12
    "images/nest/trans6/0217.jpg"
    pause .12
    "images/nest/trans6/0218.jpg"
    pause .12
    "images/nest/trans6/0219.jpg"
    pause .12
    "images/nest/trans6/0220.jpg"
    pause .12
    "images/nest/trans6/0221.jpg"
    pause .12
    "images/nest/trans6/0222.jpg"
    pause .12
    "images/nest/trans6/0223.jpg"
    pause .12
    "images/nest/trans6/0224.jpg"
    pause .12
    "images/nest/trans6/0225.jpg"
    pause .12
    "images/nest/trans6/0226.jpg"
    pause .12
    "images/nest/trans6/0227.jpg"
    pause .12
    "images/nest/trans6/0228.jpg"
    pause .12
    "images/nest/trans6/0229.jpg"
    pause .12
    "images/nest/trans6/0230.jpg"
    pause .12
    "images/nest/trans6/0231.jpg"
    pause .12
    "images/nest/trans6/0232.jpg"
    pause .12
    "images/nest/trans6/0233.jpg"
    pause .12
    "images/nest/trans6/0234.jpg"
    pause .12
    "images/nest/trans6/0235.jpg"
    pause .12

image nestloop3:
    "images/nest/loop3/0210.jpg"
    pause .12
    "images/nest/loop3/0211.jpg"
    pause .12
    "images/nest/loop3/0212.jpg"
    pause .12
    "images/nest/loop3/0213.jpg"
    pause .12
    "images/nest/loop3/0214.jpg"
    function s4
    pause .12
    "images/nest/loop3/0215.jpg"
    function fart2
    pause .12
    "images/nest/loop3/0216.jpg"
    pause .12
    repeat

image nestcum:
    "images/nest/cum/0213.jpg"
    pause .12
    "images/nest/cum/0214.jpg"
    pause .12
    "images/nest/cum/0215.jpg"
    pause .12
    "images/nest/cum/0216.jpg"
    pause .12
    "images/nest/cum/0217.jpg"
    pause .12
    "images/nest/cum/0218.jpg"
    pause .12
    "images/nest/cum/0219.jpg"
    pause .12
    "images/nest/cum/0220.jpg"
    pause .12
    "images/nest/cum/0221.jpg"
    pause .12
    "images/nest/cum/0222.jpg"
    pause .12
    "images/nest/cum/0223.jpg"
    pause .12
    "images/nest/cum/0224.jpg"
    pause .12
    "images/nest/cum/0225.jpg"
    pause .12
    "images/nest/cum/0226.jpg"
    pause .12
    "images/nest/cum/0227.jpg"
    pause .12
    "images/nest/cum/0228.jpg"
    pause .12
    "images/nest/cum/0229.jpg"
    pause .12
    "images/nest/cum/0230.jpg"
    pause .12
    "images/nest/cum/0231.jpg"
    pause .12
    "images/nest/cum/0232.jpg"
    pause .12
    "images/nest/cum/0233.jpg"
    pause .12
    "images/nest/cum/0234.jpg"
    pause .12
    "images/nest/cum/0235.jpg"
    pause .12
    "images/nest/cum/0236.jpg"
    pause .12
    "images/nest/cum/0237.jpg"
    pause .12
    "images/nest/cum/0238.jpg"
    pause .12
    "images/nest/cum/0239.jpg"
    function cough
    pause .12
    "images/nest/cum/0240.jpg"
    pause .12
    "images/nest/cum/0241.jpg"
    pause .12
    "images/nest/cum/0242.jpg"
    pause .12
    "images/nest/cum/0243.jpg"
    pause .12
    "images/nest/cum/0244.jpg"
    pause .12
    "images/nest/cum/0245.jpg"
    pause .12
    "images/nest/cum/0246.jpg"
    pause .12
    "images/nest/cum/0247.jpg"
    pause .12
    "images/nest/cum/0248.jpg"
    pause .12
    "images/nest/cum/0249.jpg"
    pause .12
    "images/nest/cum/0250.jpg"
    pause .12
    "images/nest/cum/0251.jpg"
    pause .12
    "images/nest/cum/0252.jpg"
    pause .12
    "images/nest/cum/0253.jpg"
    pause .12
    "images/nest/cum/0254.jpg"
    pause .12
    "images/nest/cum/0255.jpg"
    pause .12
    "images/nest/cum/0256.jpg"
    pause .12
    "images/nest/cum/0257.jpg"
    pause .12
    "images/nest/cum/0258.jpg"
    pause .12
    "images/nest/cum/0259.jpg"
    pause .12
    "images/nest/cum/0260.jpg"
    pause .12

image frog1_loop1 = Generate_Animation("images/enemy1/loop1", 10)
image frog1_trans1 = Generate_Animation("images/enemy1/trans1", 10)
image frog1_trans2 = Generate_Animation("images/enemy1/trans2", 10)
image frog1_loop2 = Generate_Animation("images/enemy1/loop2", 10)

image dp1_1:
    "images/enemy2/scene1/trans1/0065.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0066.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0067.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0068.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0069.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0070.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0071.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0072.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0073.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0074.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0075.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0076.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0077.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0078.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0079.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0080.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0081.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0082.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0083.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0084.jpg"
    pause .12

image dp1_2:
    "images/enemy2/scene1/trans1/0085.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0086.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0087.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0088.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0089.jpg"
    function suck4
    pause .12
    "images/enemy2/scene1/trans1/0090.jpg"
    pause .12
    "images/enemy2/scene1/trans1/0091.jpg"
    pause .12

image dp1_3loop:
    "images/enemy2/scene1/loop1/0092.jpg"
    pause .12
    "images/enemy2/scene1/loop1/0093.jpg"
    pause .12
    "images/enemy2/scene1/loop1/0094.jpg"
    pause .12
    "images/enemy2/scene1/loop1/0095.jpg"
    function suck4
    pause .12
    "images/enemy2/scene1/loop1/0096.jpg"
    pause .12
    "images/enemy2/scene1/loop1/0097.jpg"
    pause .12
    "images/enemy2/scene1/loop1/0098.jpg"
    pause .12
    "images/enemy2/scene1/loop1/0099.jpg"
    pause .12
    "images/enemy2/scene1/loop1/0100.jpg"
    pause .12
    "images/enemy2/scene1/loop1/0102.jpg"
    function suck1
    pause .12
    "images/enemy2/scene1/loop1/0103.jpg"
    pause .12
    repeat

image dp1_4loop:
    "images/enemy2/scene1/loop2/0092.jpg"
    pause .12
    "images/enemy2/scene1/loop2/0093.jpg"
    pause .12
    "images/enemy2/scene1/loop2/0094.jpg"
    pause .12
    "images/enemy2/scene1/loop2/0095.jpg"
    function suck3
    pause .12
    "images/enemy2/scene1/loop2/0096.jpg"
    pause .12
    "images/enemy2/scene1/loop2/0097.jpg"
    function slurp2
    pause .12
    repeat

image dp1_5loop:
    "images/enemy2/scene1/loop3/0092.jpg"
    function inside
    pause .12
    "images/enemy2/scene1/loop3/0093.jpg"
    pause .12
    "images/enemy2/scene1/loop3/0094.jpg"
    pause .12
    "images/enemy2/scene1/loop3/0095.jpg"
    pause .12
    "images/enemy2/scene1/loop3/0096.jpg"
    pause .12
    "images/enemy2/scene1/loop3/0097.jpg"
    pause .12
    "images/enemy2/scene1/loop3/0098.jpg"
    pause .12
    "images/enemy2/scene1/loop3/0099.jpg"
    pause .12
    "images/enemy2/scene1/loop3/0100.jpg"
    function s1
    pause .12
    "images/enemy2/scene1/loop3/0102.jpg"
    pause .12
    "images/enemy2/scene1/loop3/0103.jpg"
    pause .12
    repeat

image dp1_6cum:
    "images/enemy2/scene1/cum1/0092.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0093.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0094.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0095.jpg"
    function suck4
    pause .12
    "images/enemy2/scene1/cum1/0096.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0097.jpg"
    function splat2
    pause .12
    "images/enemy2/scene1/cum1/0098.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0099.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0100.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0102.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0103.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0104.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0105.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0106.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0107.jpg"
    function slurp2
    pause .12
    "images/enemy2/scene1/cum1/0108.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0109.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0110.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0111.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0112.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0113.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0114.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0115.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0116.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0117.jpg"
    function wetsquish
    pause .12
    "images/enemy2/scene1/cum1/0118.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0119.jpg"
    pause .12
    "images/enemy2/scene1/cum1/0120.jpg"
    pause .12

image dp1_7cum:
    "images/enemy2/scene1/cum2/0092.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0093.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0094.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0095.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0096.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0097.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0098.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0099.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0100.jpg"
    function splat2
    pause .12
    "images/enemy2/scene1/cum2/0102.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0103.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0104.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0105.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0106.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0107.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0108.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0109.jpg"
    function cum1
    pause .12
    "images/enemy2/scene1/cum2/0110.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0111.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0112.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0113.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0114.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0115.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0116.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0117.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0118.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0119.jpg"
    pause .12
    "images/enemy2/scene1/cum2/0120.jpg"
    pause .12


image medlabon:
    "images/medlab/anim/1.jpg"
    pause .5
    "images/medlab/anim/2.jpg"
    pause .5
    "images/medlab/anim/3.jpg"
    pause .5
    "images/medlab/anim/4.jpg"
    pause .5
    "images/medlab/anim/5.jpg"
    pause .5
    "images/medlab/anim/6.jpg"
    pause .5


image vent1_1GateRed:
    "images/vent1_1gate/0031.jpg"
    pause .12
    "images/vent1_1gate/0032.jpg"
    pause .12
    "images/vent1_1gate/0033.jpg"
    pause .12
    "images/vent1_1gate/0034.jpg"
    pause .12
    "images/vent1_1gate/0035.jpg"
    pause .12

image vent1_1GateGreen:
    "images/vent1_1gate/0036.jpg"
    pause .12
    "images/vent1_1gate/0037.jpg"
    pause .12
    "images/vent1_1gate/0038.jpg"
    pause .12
    "images/vent1_1gate/0039.jpg"
    pause .12
    "images/vent1_1gate/0040.jpg"
    pause .12
    "images/vent1_1gate/0041.jpg"
    pause .12
    "images/vent1_1gate/0042.jpg"
    pause .12
    "images/vent1_1gate/0043.jpg"
    function frog1
    pause .12
    "images/vent1_1gate/0044.jpg"
    pause .12
    "images/vent1_1gate/0045.jpg"
    pause .12

image vent1_3Loop:
    "images/vent1_3Loop/0085.jpg"
    pause .12
    "images/vent1_3Loop/0086.jpg"
    pause .12
    "images/vent1_3Loop/0087.jpg"
    pause .12
    "images/vent1_3Loop/0088.jpg"
    pause .12
    "images/vent1_3Loop/0089.jpg"
    pause .12
    "images/vent1_3Loop/0090.jpg"
    function frog2
    pause .12
    "images/vent1_3Loop/0091.jpg"
    pause .12
    "images/vent1_3Loop/0092.jpg"
    pause .12
    "images/vent1_3Loop/0093.jpg"
    pause .12
    "images/vent1_3Loop/0094.jpg"
    pause .12
    repeat

image vent1_3Vent1:
    "images/vent1_3Vent/0071.jpg"
    pause .12
    "images/vent1_3Vent/0072.jpg"
    pause .12
    "images/vent1_3Vent/0073.jpg"
    pause .12
    "images/vent1_3Vent/0074.jpg"
    pause .12
    "images/vent1_3Vent/0075.jpg"
    pause .12
    "images/vent1_3Vent/0076.jpg"
    pause .12
    "images/vent1_3Vent/0077.jpg"
    pause .12
    "images/vent1_3Vent/0078.jpg"
    pause .12
    "images/vent1_3Vent/0079.jpg"
    pause .12
    "images/vent1_3Vent/0080.jpg"
    pause .12
    "images/vent1_3Vent/0081.jpg"
    pause .12
    "images/vent1_3Vent/0082.jpg"
    pause .12
    "images/vent1_3Vent/0083.jpg"
    pause .12
    "images/vent1_3Vent/0084.jpg"
    pause .12
    "images/vent1_3Vent/0085.jpg"
    pause .12

image vent1_3Vent2:
    "images/vent1_3Vent/0085.jpg"
    pause .12
    "images/vent1_3Vent/0084.jpg"
    pause .12
    "images/vent1_3Vent/0083.jpg"
    pause .12
    "images/vent1_3Vent/0082.jpg"
    pause .12
    "images/vent1_3Vent/0081.jpg"
    pause .12
    "images/vent1_3Vent/0080.jpg"
    pause .12
    "images/vent1_3Vent/0079.jpg"
    pause .12
    "images/vent1_3Vent/0078.jpg"
    pause .12
    "images/vent1_3Vent/0077.jpg"
    pause .12
    "images/vent1_3Vent/0076.jpg"
    pause .12
    "images/vent1_3Vent/0075.jpg"
    pause .12
    "images/vent1_3Vent/0074.jpg"
    pause .12
    "images/vent1_3Vent/0073.jpg"
    pause .12
    "images/vent1_3Vent/0072.jpg"
    pause .12
    "images/vent1_3Vent/0071.jpg"
    pause .12

image vent1_4Hatch1:
    "images/vent1_4Hatch/0086.jpg"
    pause .12
    "images/vent1_4Hatch/0087.jpg"
    pause .12
    "images/vent1_4Hatch/0088.jpg"
    pause .12
    "images/vent1_4Hatch/0089.jpg"
    pause .12
    "images/vent1_4Hatch/0090.jpg"
    pause .12

image vent1_4Hatch2:
    "images/vent1_4Hatch/0090.jpg"
    pause .12
    "images/vent1_4Hatch/0091.jpg"
    pause .12
    "images/vent1_4Hatch/0092.jpg"
    pause .12
    "images/vent1_4Hatch/0093.jpg"
    pause .12
    "images/vent1_4Hatch/0094.jpg"
    pause .12
    "images/vent1_4Hatch/0095.jpg"
    pause .12

image vent1_4nest1:
    "images/vent1_4Hatch/0095.jpg"
    pause .12
    "images/vent1_4Hatch/0096.jpg"
    pause .12
    "images/vent1_4Hatch/0097.jpg"
    pause .12
    "images/vent1_4Hatch/0098.jpg"
    pause .12
    "images/vent1_4Hatch/0099.jpg"
    pause .12
    "images/vent1_4Hatch/0100.jpg"
    pause .12

image vent1_4nest2:
    "images/vent1_4Hatch/0100.jpg"
    pause .12
    "images/vent1_4Hatch/0099.jpg"
    pause .12
    "images/vent1_4Hatch/0098.jpg"
    pause .12
    "images/vent1_4Hatch/0097.jpg"
    pause .12
    "images/vent1_4Hatch/0096.jpg"
    pause .12
    "images/vent1_4Hatch/0095.jpg"
    pause .12


image vent1_4nestloop:
    "images/vent1_4Hatch/0100.jpg"
    pause .12
    "images/vent1_4Hatch/0101.jpg"
    pause .12
    "images/vent1_4Hatch/0102.jpg"
    pause .12
    "images/vent1_4Hatch/0103.jpg"
    pause .12
    "images/vent1_4Hatch/0104.jpg"
    pause .12
    "images/vent1_4Hatch/0105.jpg"
    pause .12
    repeat

image vent1_7look:
    "images/vent1_7enter/0096.jpg"
    pause .12
    "images/vent1_7enter/0097.jpg"
    pause .12
    "images/vent1_7enter/0098.jpg"
    pause .12
    "images/vent1_7enter/0099.jpg"
    pause .12
    "images/vent1_7enter/0100.jpg"
    pause .12
    "images/vent1_7enter/0101.jpg"
    pause .12
    "images/vent1_7enter/0102.jpg"
    pause .12
    "images/vent1_7enter/0103.jpg"
    pause .12
    "images/vent1_7enter/0104.jpg"
    pause .12
    "images/vent1_7enter/0105.jpg"
    pause .12
    "images/vent1_7enter/0106.jpg"
    pause .12
    "images/vent1_7enter/0107.jpg"
    pause .12
    "images/vent1_7enter/0108.jpg"
    pause .12
    "images/vent1_7enter/0109.jpg"
    pause .12
    "images/vent1_7enter/0110.jpg"
    pause .12

image vent1_7unlook:
    "images/vent1_7enter/0110.jpg"
    pause .12
    "images/vent1_7enter/0109.jpg"
    pause .12
    "images/vent1_7enter/0108.jpg"
    pause .12
    "images/vent1_7enter/0107.jpg"
    pause .12
    "images/vent1_7enter/0106.jpg"
    pause .12
    "images/vent1_7enter/0105.jpg"
    pause .12
    "images/vent1_7enter/0104.jpg"
    pause .12
    "images/vent1_7enter/0103.jpg"
    pause .12
    "images/vent1_7enter/0102.jpg"
    pause .12
    "images/vent1_7enter/0101.jpg"
    pause .12
    "images/vent1_7enter/0100.jpg"
    pause .12
    "images/vent1_7enter/0099.jpg"
    pause .12
    "images/vent1_7enter/0098.jpg"
    pause .12
    "images/vent1_7enter/0097.jpg"
    pause .12
    "images/vent1_7enter/0096.jpg"
    pause .12

image vent1_7break:
    "images/vent1_7enter/0111.jpg"
    pause .12
    "images/vent1_7enter/0112.jpg"
    pause .12
    "images/vent1_7enter/0113.jpg"
    pause .12
    "images/vent1_7enter/0114.jpg"
    pause .12
    "images/vent1_7enter/0115.jpg"
    pause .12
    "images/vent1_7enter/0116.jpg"
    pause .12
    "images/vent1_7enter/0117.jpg"
    pause .12
    "images/vent1_7enter/0118.jpg"
    pause .12
    "images/vent1_7enter/0119.jpg"
    pause .12
    "images/vent1_7enter/0120.jpg"
    function metal2
    pause .12
    "images/vent1_7enter/0121.jpg"
    pause .12
    "images/vent1_7enter/0122.jpg"
    pause .12
    "images/vent1_7enter/0123.jpg"
    pause .12
    "images/vent1_7enter/0124.jpg"
    pause .12
    "images/vent1_7enter/0125.jpg"
    pause .12
    "images/vent1_7enter/0126.jpg"
    pause .12
    "images/vent1_7enter/0127.jpg"
    function metal1
    pause .12
    "images/vent1_7enter/0128.jpg"
    pause .12
    "images/vent1_7enter/0129.jpg"
    pause .12
    "images/vent1_7enter/0130.jpg"
    pause .12
    "images/vent1_7enter/0131.jpg"
    pause .12
    "images/vent1_7enter/0132.jpg"
    pause .12
    "images/vent1_7enter/0134.jpg"
    pause .12
    "images/vent1_7enter/0135.jpg"
    pause .12
    "images/vent1_7enter/0136.jpg"
    pause .12
    "images/vent1_7enter/0137.jpg"
    pause .12
    "images/vent1_7enter/0138.jpg"
    pause .12
    "images/vent1_7enter/0139.jpg"
    pause .12
    "images/vent1_7enter/0140.jpg"
    pause .12
    "images/vent1_7enter/0141.jpg"
    pause .12
    "images/vent1_7enter/0142.jpg"
    pause .12
    "images/vent1_7enter/0143.jpg"
    pause .12
    "images/vent1_7enter/0144.jpg"
    pause .12
    "images/vent1_7enter/0145.jpg"
    pause .12
    "images/vent1_7enter/0146.jpg"
    pause .12


image medroom_catch:
    "images/enemy1/catch/0230.jpg"
    pause .12
    "images/enemy1/catch/0231.jpg"
    pause .12
    "images/enemy1/catch/0232.jpg"
    pause .12
    "images/enemy1/catch/0233.jpg"
    pause .12
    "images/enemy1/catch/0234.jpg"
    pause .12
    "images/enemy1/catch/0235.jpg"
    pause .12
    "images/enemy1/catch/0236.jpg"
    pause .12
    "images/enemy1/catch/0237.jpg"
    pause .12
    "images/enemy1/catch/0238.jpg"
    function fall
    pause .12
    "images/enemy1/catch/0239.jpg"
    pause .12
    "images/enemy1/catch/0240.jpg"
    pause .12

image medroom_kill:
    "images/enemy1/kill/0230.jpg"
    pause .12
    "images/enemy1/kill/0231.jpg"
    pause .12
    "images/enemy1/kill/0232.jpg"
    pause .12
    "images/enemy1/kill/0233.jpg"
    pause .12
    "images/enemy1/kill/0234.jpg"
    pause .12
    "images/enemy1/kill/0235.jpg"
    pause .12
    "images/enemy1/kill/0236.jpg"
    function shot
    pause .12
    "images/enemy1/kill/0237.jpg"
    pause .12
    "images/enemy1/kill/0238.jpg"
    pause .12
    "images/enemy1/kill/0239.jpg"
    pause .12
    "images/enemy1/kill/0240.jpg"
    pause .12
    "images/enemy1/kill/0241.jpg"
    pause .12
    "images/enemy1/kill/0242.jpg"
    pause .12
    "images/enemy1/kill/0243.jpg"
    pause .12
    "images/enemy1/kill/0244.jpg"
    pause .12

image vent14catch2:
    "images/events/catch1/grab2/0107.jpg"
    pause .12
    "images/events/catch1/grab2/0108.jpg"
    pause .12
    "images/events/catch1/grab2/0109.jpg"
    pause .12
    "images/events/catch1/grab2/0110.jpg"
    pause .12
    "images/events/catch1/grab2/0111.jpg"
    function fall
    pause .12
    "images/events/catch1/grab2/0112.jpg"
    pause .12
    "images/events/catch1/grab2/0113.jpg"
    pause .12

image vent14catchdrag:
    "images/events/catch1/grab1/0115.jpg"
    pause .12
    "images/events/catch1/grab1/0116.jpg"
    pause .12
    "images/events/catch1/grab1/0117.jpg"
    pause .12
    "images/events/catch1/grab1/0118.jpg"
    pause .12
    "images/events/catch1/grab1/0119.jpg"
    pause .12
    "images/events/catch1/grab1/0120.jpg"
    pause .12
    "images/events/catch1/grab1/0121.jpg"
    pause .12
    "images/events/catch1/grab1/0122.jpg"
    pause .12
    "images/events/catch1/grab1/0123.jpg"
    pause .12
    "images/events/catch1/grab1/0124.jpg"
    pause .12
    "images/events/catch1/grab1/0125.jpg"
    pause .12
    "images/events/catch1/grab1/0126.jpg"
    pause .12
    "images/events/catch1/grab1/0127.jpg"
    pause .12
    "images/events/catch1/grab1/0128.jpg"
    pause .12
    "images/events/catch1/grab1/0129.jpg"
    pause .12
    "images/events/catch1/grab1/0130.jpg"
    pause .12
    "images/events/catch1/grab1/0131.jpg"
    pause .12
    "images/events/catch1/grab1/0132.jpg"
    pause .12
    "images/events/catch1/grab1/0133.jpg"
    pause .12
    "images/events/catch1/grab1/0134.jpg"
    pause .12
    "images/events/catch1/grab1/0135.jpg"
    pause .12
    "images/events/catch1/grab1/0136.jpg"
    pause .12

image vent14catch1:
    "images/events/catch1/0090.jpg"
    pause .12
    "images/events/catch1/0091.jpg"
    pause .12
    "images/events/catch1/0092.jpg"
    pause .12
    "images/events/catch1/0093.jpg"
    pause .12
    "images/events/catch1/0094.jpg"
    pause .12
    "images/events/catch1/0095.jpg"
    pause .12
    "images/events/catch1/0096.jpg"
    pause .12

image vent14struggle = Generate_Animation("images/events/catch1/strug", 8)

image vent14trans1:
    "images/events/catch1/grab2/0115.jpg"
    pause .12
    "images/events/catch1/grab2/0116.jpg"
    pause .12
    "images/events/catch1/grab2/0117.jpg"
    pause .12
    "images/events/catch1/grab2/0118.jpg"
    pause .12
    "images/events/catch1/grab2/0119.jpg"
    pause .12
    "images/events/catch1/grab2/0120.jpg"
    pause .12
    "images/events/catch1/grab2/0121.jpg"
    pause .12
    "images/events/catch1/grab2/0122.jpg"
    pause .12
    "images/events/catch1/grab2/0123.jpg"
    pause .12
    "images/events/catch1/grab2/0124.jpg"
    pause .12
    "images/events/catch1/grab2/0125.jpg"
    pause .12
    "images/events/catch1/grab2/0126.jpg"
    pause .12
    "images/events/catch1/grab2/0127.jpg"
    pause .12
    "images/events/catch1/grab2/0128.jpg"
    pause .12
    "images/events/catch1/grab2/0129.jpg"
    pause .12
    "images/events/catch1/grab2/0130.jpg"
    pause .12
    "images/events/catch1/grab2/0131.jpg"
    pause .12
    "images/events/catch1/grab2/0132.jpg"
    pause .12
    "images/events/catch1/grab2/0133.jpg"
    pause .12
    "images/events/catch1/grab2/0134.jpg"
    pause .12
    "images/events/catch1/grab2/0135.jpg"
    pause .12
    "images/events/catch1/grab2/0136.jpg"
    pause .12
    "images/events/catch1/grab2/0137.jpg"
    pause .12
    "images/events/catch1/grab2/0138.jpg"
    pause .12
    "images/events/catch1/grab2/0139.jpg"
    pause .12
    "images/events/catch1/grab2/0140.jpg"
    pause .12
    "images/events/catch1/grab2/0141.jpg"
    pause .12
    "images/events/catch1/grab2/0142.jpg"
    pause .12
    "images/events/catch1/grab2/0143.jpg"
    pause .12
    "images/events/catch1/grab2/0144.jpg"
    function s1
    pause .12
    "images/events/catch1/grab2/0145.jpg"
    pause .12
    "images/events/catch1/grab2/0146.jpg"
    pause .12
    "images/events/catch1/grab2/0147.jpg"
    pause .12
    "images/events/catch1/grab2/0148.jpg"
    pause .12
    "images/events/catch1/grab2/0149.jpg"
    function s2
    pause .12
    "images/events/catch1/grab2/0150.jpg"
    pause .12

image vent14loop1:
    "images/events/catch1/grab2/loop1/0150.jpg"
    pause .10
    "images/events/catch1/grab2/loop1/0151.jpg"
    pause .10
    "images/events/catch1/grab2/loop1/0152.jpg"
    pause .10
    "images/events/catch1/grab2/loop1/0153.jpg"
    function s1
    pause .10
    "images/events/catch1/grab2/loop1/0154.jpg"
    pause .10
    repeat

image vent14trans2:
    "images/events/catch1/grab2/trans1/0155.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0156.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0157.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0158.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0159.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0160.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0161.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0162.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0163.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0164.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0165.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0166.jpg"
    function fart2
    pause .12
    "images/events/catch1/grab2/trans1/0167.jpg"
    pause .12
    "images/events/catch1/grab2/trans1/0168.jpg"
    pause .12

image vent14loop2:
    "images/events/catch1/grab2/loop2/0168.jpg"
    pause .10
    "images/events/catch1/grab2/loop2/0169.jpg"
    pause .10
    "images/events/catch1/grab2/loop2/0170.jpg"
    pause .10
    "images/events/catch1/grab2/loop2/0171.jpg"
    function s4
    pause .10
    "images/events/catch1/grab2/loop2/0172.jpg"
    pause .10
    repeat

image vent14trans3:
    "images/events/catch1/grab2/trans2/0168.jpg"
    pause .12
    "images/events/catch1/grab2/trans2/0169.jpg"
    pause .12
    "images/events/catch1/grab2/trans2/0170.jpg"
    pause .12
    "images/events/catch1/grab2/trans2/0171.jpg"
    function splat2
    pause .12
    "images/events/catch1/grab2/trans2/0172.jpg"
    pause .12
    "images/events/catch1/grab2/trans2/0173.jpg"
    pause .12
    "images/events/catch1/grab2/trans2/0174.jpg"
    pause .12
    "images/events/catch1/grab2/trans2/0175.jpg"
    pause .12
    "images/events/catch1/grab2/trans2/0176.jpg"
    pause .12
    "images/events/catch1/grab2/trans2/0177.jpg"
    pause .12

image vent14loop3:
    "images/events/catch1/grab2/loop3/0178.jpg"
    pause .10
    "images/events/catch1/grab2/loop3/0179.jpg"
    pause .10
    "images/events/catch1/grab2/loop3/0180.jpg"
    pause .10
    "images/events/catch1/grab2/loop3/0181.jpg"
    function splat1
    pause .10
    "images/events/catch1/grab2/loop3/0182.jpg"
    pause .10
    repeat

image vent14cum:
    "images/events/catch1/grab2/cum/0178.jpg"
    pause .10
    "images/events/catch1/grab2/cum/0179.jpg"
    pause .10
    "images/events/catch1/grab2/cum/0180.jpg"
    pause .10
    "images/events/catch1/grab2/cum/0181.jpg"
    pause .10
    "images/events/catch1/grab2/cum/0182.jpg"
    pause .10
    "images/events/catch1/grab2/cum/0183.jpg"
    pause .10
    "images/events/catch1/grab2/cum/0184.jpg"
    pause .10
    "images/events/catch1/grab2/cum/0185.jpg"
    function splat
    pause .10
    "images/events/catch1/grab2/cum/0186.jpg"
    pause .10
    "images/events/catch1/grab2/cum/0187.jpg"
    pause .10
    "images/events/catch1/grab2/cum/0188.jpg"
    pause .10

image medlabloop1:
    "images/enemy1/event1/loop1/0198.jpg"
    pause .12
    "images/enemy1/event1/loop1/0199.jpg"
    pause .12
    "images/enemy1/event1/loop1/0200.jpg"
    pause .12
    "images/enemy1/event1/loop1/0201.jpg"
    function suck1
    pause .12
    "images/enemy1/event1/loop1/0202.jpg"
    pause .12
    "images/enemy1/event1/loop1/0203.jpg"
    pause .12
    "images/enemy1/event1/loop1/0204.jpg"
    pause .12
    "images/enemy1/event1/loop1/0205.jpg"
    pause .12
    "images/enemy1/event1/loop1/0206.jpg"
    function suck1
    pause .12
    "images/enemy1/event1/loop1/0207.jpg"
    pause .12
    repeat

image medlabloop2:
    "images/enemy1/event1/loop2/0198.jpg"
    pause .12
    "images/enemy1/event1/loop2/0199.jpg"
    pause .12
    "images/enemy1/event1/loop2/0200.jpg"
    pause .12
    "images/enemy1/event1/loop2/0201.jpg"
    function suck3
    pause .12
    "images/enemy1/event1/loop2/0202.jpg"
    pause .12
    "images/enemy1/event1/loop2/0203.jpg"
    pause .12
    "images/enemy1/event1/loop2/0204.jpg"
    pause .12
    "images/enemy1/event1/loop2/0205.jpg"
    pause .12
    "images/enemy1/event1/loop2/0206.jpg"
    function suck3
    pause .12
    "images/enemy1/event1/loop2/0207.jpg"
    pause .12
    repeat

image medlabcum:
    "images/enemy1/event1/cum/0198.jpg"
    pause .12
    "images/enemy1/event1/cum/0199.jpg"
    pause .12
    "images/enemy1/event1/cum/0200.jpg"
    pause .12
    "images/enemy1/event1/cum/0201.jpg"
    function suck4
    pause .12
    "images/enemy1/event1/cum/0202.jpg"
    pause .12
    "images/enemy1/event1/cum/0203.jpg"
    pause .12
    "images/enemy1/event1/cum/0204.jpg"
    pause .12
    "images/enemy1/event1/cum/0205.jpg"
    pause .12
    "images/enemy1/event1/cum/0206.jpg"
    function cum1
    pause .12
    "images/enemy1/event1/cum/0207.jpg"
    pause .12
    "images/enemy1/event1/cum/0208.jpg"
    pause .12
    "images/enemy1/event1/cum/0209.jpg"
    pause .12
    "images/enemy1/event1/cum/0210.jpg"
    pause .12
    "images/enemy1/event1/cum/0211.jpg"
    function splat1
    pause .12
    "images/enemy1/event1/cum/0212.jpg"
    pause .12
    "images/enemy1/event1/cum/0213.jpg"
    pause .12
    "images/enemy1/event1/cum/0214.jpg"
    pause .12
    "images/enemy1/event1/cum/0215.jpg"
    pause .12
    "images/enemy1/event1/cum/0216.jpg"
    pause .12
    "images/enemy1/event1/cum/0217.jpg"
    pause .12
    "images/enemy1/event1/cum/0218.jpg"
    function wetsquish
    pause .12
    "images/enemy1/event1/cum/0219.jpg"
    pause .12
    "images/enemy1/event1/cum/0220.jpg"
    pause .12
    "images/enemy1/event1/cum/0221.jpg"
    pause .12
    "images/enemy1/event1/cum/0222.jpg"
    pause .12
    "images/enemy1/event1/cum/0223.jpg"
    pause .12
    "images/enemy1/event1/cum/0224.jpg"
    pause .12
    "images/enemy1/event1/cum/0225.jpg"
    pause .12
    "images/enemy1/event1/cum/0226.jpg"
    pause .12
    "images/enemy1/event1/cum/0227.jpg"
    pause .12
    "images/enemy1/event1/cum/0228.jpg"
    pause .12
    "images/enemy1/event1/cum/0229.jpg"
    pause .12
    "images/enemy1/event1/cum/0230.jpg"
    pause .12

image runtrans:
    "images/enemy2/trans1/0095.jpg"
    pause .12
    "images/enemy2/trans1/0096.jpg"
    pause .12
    "images/enemy2/trans1/0097.jpg"
    pause .12
    "images/enemy2/trans1/0098.jpg"
    function frog1
    pause .12
    "images/enemy2/trans1/0099.jpg"
    pause .12
    "images/enemy2/trans1/0100.jpg"
    pause .12
    "images/enemy2/trans1/0101.jpg"
    pause .12
    "images/enemy2/trans1/0102.jpg"
    pause .12
    "images/enemy2/trans1/0103.jpg"
    pause .12
    "images/enemy2/trans1/0104.jpg"
    pause .12
    "images/enemy2/trans1/0105.jpg"
    function frog2
    pause .12
    "images/enemy2/trans1/0106.jpg"
    pause .12
    "images/enemy2/trans1/0107.jpg"
    pause .12
    "images/enemy2/trans1/0108.jpg"
    pause .12
    "images/enemy2/trans1/0109.jpg"
    pause .12
    "images/enemy2/trans1/0110.jpg"
    pause .12
    "images/enemy2/trans1/0111.jpg"
    pause .12


image tenttrans1:
    "images/vent1_5fwd/0110.jpg"
    pause .12
    "images/vent1_5fwd/0111.jpg"
    pause .12
    "images/tentacle/trans1/0083.jpg"
    pause .12
    "images/tentacle/trans1/0084.jpg"
    pause .12
    "images/tentacle/trans1/0085.jpg"
    pause .12
    "images/tentacle/trans1/0086.jpg"
    pause .12
    "images/tentacle/trans1/0087.jpg"
    pause .12
    "images/tentacle/trans1/0088.jpg"
    pause .12
    "images/tentacle/trans1/0089.jpg"
    pause .12
    "images/tentacle/trans1/0090.jpg"
    pause .12
    "images/tentacle/trans1/0091.jpg"
    pause .12
    "images/tentacle/trans1/0092.jpg"
    pause .12
    "images/tentacle/trans1/0093.jpg"
    pause .12
    "images/tentacle/trans1/0094.jpg"
    pause .12
    "images/tentacle/trans1/0095.jpg"
    pause .12
    "images/tentacle/trans1/0096.jpg"
    pause .12
    "images/tentacle/trans1/0097.jpg"
    pause .12
    "images/tentacle/trans1/0099.jpg"
    pause .12
    "images/tentacle/trans1/0100.jpg"
    pause .12
    "images/tentacle/trans1/0101.jpg"
    pause .12
    "images/tentacle/trans1/0102.jpg"
    pause .12
    "images/tentacle/trans1/0103.jpg"
    function s1
    pause .12

image tentstruggle:
    "images/tentacle/loop1/0103.jpg"
    pause .12
    "images/tentacle/loop1/0104.jpg"
    pause .12
    "images/tentacle/loop1/0105.jpg"
    pause .12
    "images/tentacle/loop1/0106.jpg"
    pause .12
    "images/tentacle/loop1/0107.jpg"
    pause .12
    "images/tentacle/loop1/0108.jpg"
    pause .12
    "images/tentacle/loop1/0109.jpg"
    pause .12
    "images/tentacle/loop1/0110.jpg"
    pause .12
    "images/tentacle/loop1/0111.jpg"
    pause .12
    repeat

image tentescape:
    "images/tentacle/escape1/0103.jpg"
    pause .12
    "images/tentacle/escape1/0104.jpg"
    pause .12
    "images/tentacle/escape1/0105.jpg"
    pause .12
    "images/tentacle/escape1/0106.jpg"
    pause .12
    "images/tentacle/escape1/0107.jpg"
    pause .12
    "images/tentacle/escape1/0108.jpg"
    pause .12
    "images/tentacle/escape1/0109.jpg"
    pause .12
    "images/tentacle/escape1/0110.jpg"
    pause .12
    "images/tentacle/escape1/0111.jpg"
    pause .12
    "images/tentacle/escape1/0112.jpg"
    pause .12
    "images/tentacle/escape1/0113.jpg"
    pause .12
    "images/tentacle/escape1/0114.jpg"
    pause .12
    "images/tentacle/escape1/0115.jpg"
    pause .12
    "images/tentacle/escape1/0116.jpg"
    pause .12
    "images/tentacle/escape1/0117.jpg"
    pause .12
    "images/tentacle/escape1/0118.jpg"
    pause .12

image tenttrans2:
    "images/tentacle/trans2/0112.jpg"
    pause .12
    "images/tentacle/trans2/0113.jpg"
    pause .12
    "images/tentacle/trans2/0114.jpg"
    pause .12
    "images/tentacle/trans2/0115.jpg"
    pause .12
    "images/tentacle/trans2/0116.jpg"
    pause .12
    "images/tentacle/trans2/0117.jpg"
    pause .12
    "images/tentacle/trans2/0118.jpg"
    pause .12
    "images/tentacle/trans2/0119.jpg"
    function strap
    pause .12
    "images/tentacle/trans2/0120.jpg"
    pause .12
    "images/tentacle/trans2/0121.jpg"
    pause .12
    "images/tentacle/trans2/0122.jpg"
    pause .12
    "images/tentacle/trans2/0123.jpg"
    pause .12
    "images/tentacle/trans2/0124.jpg"
    pause .12
    "images/tentacle/trans2/0125.jpg"
    pause .12
    "images/tentacle/trans2/0126.jpg"
    pause .12
    "images/tentacle/trans2/0127.jpg"
    pause .12
    "images/tentacle/trans2/0128.jpg"
    pause .12
    "images/tentacle/trans2/0129.jpg"
    pause .12
    "images/tentacle/trans2/0130.jpg"
    pause .12

image tenttrans3:
    "images/tentacle/trans3/0130.jpg"
    pause .12
    "images/tentacle/trans3/0131.jpg"
    pause .12
    "images/tentacle/trans3/0132.jpg"
    pause .12
    "images/tentacle/trans3/0133.jpg"
    pause .12
    "images/tentacle/trans3/0134.jpg"
    pause .12
    "images/tentacle/trans3/0135.jpg"
    pause .12
    "images/tentacle/trans3/0136.jpg"
    pause .12
    "images/tentacle/trans3/0137.jpg"
    pause .12
    "images/tentacle/trans3/0138.jpg"
    pause .12
    "images/tentacle/trans3/0139.jpg"
    pause .12

image tentloop1:
    "images/tentacle/loop2/0139.jpg"
    pause .12
    "images/tentacle/loop2/0140.jpg"
    pause .12
    "images/tentacle/loop2/0141.jpg"
    function s4
    pause .12
    "images/tentacle/loop2/0142.jpg"
    pause .12
    "images/tentacle/loop2/0143.jpg"
    pause .12
    "images/tentacle/loop2/0144.jpg"
    pause .12
    repeat

image tenttrans4:
    "images/tentacle/trans4/0130.jpg"
    pause .12
    "images/tentacle/trans4/0131.jpg"
    pause .12
    "images/tentacle/trans4/0132.jpg"
    pause .12
    "images/tentacle/trans4/0133.jpg"
    pause .12
    "images/tentacle/trans4/0134.jpg"
    pause .12
    "images/tentacle/trans4/0135.jpg"
    pause .12
    "images/tentacle/trans4/0136.jpg"
    pause .12
    "images/tentacle/trans4/0137.jpg"
    pause .12
    "images/tentacle/trans4/0138.jpg"
    pause .12
    "images/tentacle/trans4/0139.jpg"
    pause .12
    "images/tentacle/trans4/0140.jpg"
    function n1
    pause .12
    "images/tentacle/trans4/0141.jpg"
    pause .12
    "images/tentacle/trans4/0142.jpg"
    pause .12
    "images/tentacle/trans4/0143.jpg"
    pause .12
    "images/tentacle/trans4/0144.jpg"
    pause .12
    "images/tentacle/trans4/0145.jpg"
    pause .12
    "images/tentacle/trans4/0146.jpg"
    pause .12
    "images/tentacle/trans4/0147.jpg"
    pause .12
    "images/tentacle/trans4/0148.jpg"
    pause .12
    "images/tentacle/trans4/0149.jpg"
    pause .12
    "images/tentacle/trans4/0150.jpg"
    pause .12

image tentloop2:
    "images/tentacle/loop3/0150.jpg"
    pause .12
    "images/tentacle/loop3/0151.jpg"
    pause .12
    "images/tentacle/loop3/0152.jpg"
    pause .12
    "images/tentacle/loop3/0153.jpg"
    pause .12
    "images/tentacle/loop3/0154.jpg"
    pause .12
    "images/tentacle/loop3/0155.jpg"
    function inside
    pause .12
    "images/tentacle/loop3/0156.jpg"
    pause .12
    "images/tentacle/loop3/0157.jpg"
    pause .12
    "images/tentacle/loop3/0158.jpg"
    pause .12
    repeat

image tenttrans5:
    "images/tentacle/trans5/0159.jpg"
    pause .12
    "images/tentacle/trans5/0160.jpg"
    pause .12
    "images/tentacle/trans5/0161.jpg"
    pause .12
    "images/tentacle/trans5/0162.jpg"
    pause .12
    "images/tentacle/trans5/0163.jpg"
    pause .12
    "images/tentacle/trans5/0164.jpg"
    pause .12
    "images/tentacle/trans5/0165.jpg"
    pause .12
    "images/tentacle/trans5/0166.jpg"
    pause .12
    "images/tentacle/trans5/0167.jpg"
    pause .12
    "images/tentacle/trans5/0168.jpg"
    pause .12
    "images/tentacle/trans5/0169.jpg"
    pause .12
    "images/tentacle/trans5/0170.jpg"
    pause .12
    "images/tentacle/trans5/0171.jpg"
    pause .12
    "images/tentacle/trans5/0172.jpg"
    function s1
    pause .12
    "images/tentacle/trans5/0173.jpg"
    pause .12
    "images/tentacle/trans5/0174.jpg"
    pause .12
    "images/tentacle/trans5/0175.jpg"
    pause .12
    "images/tentacle/trans5/0176.jpg"
    pause .12
    "images/tentacle/trans5/0177.jpg"
    pause .12
    "images/tentacle/trans5/0178.jpg"
    function s2
    pause .12
    "images/tentacle/trans5/0179.jpg"
    pause .12
    "images/tentacle/trans5/0180.jpg"
    pause .12
    "images/tentacle/trans5/0181.jpg"
    pause .12
    "images/tentacle/trans5/0182.jpg"
    pause .12
    "images/tentacle/trans5/0183.jpg"
    function splat2
    pause .12
    "images/tentacle/trans5/0184.jpg"
    pause .12
    "images/tentacle/trans5/0185.jpg"
    pause .12
    "images/tentacle/trans5/0186.jpg"
    pause .12
    "images/tentacle/trans5/0187.jpg"
    pause .12

image tentloop3:
    "images/tentacle/loop4/0180.jpg"
    pause .12
    "images/tentacle/loop4/0181.jpg"
    pause .12
    "images/tentacle/loop4/0182.jpg"
    pause .12
    "images/tentacle/loop4/0183.jpg"
    pause .12
    "images/tentacle/loop4/0184.jpg"
    function splat1
    pause .12
    "images/tentacle/loop4/0185.jpg"
    pause .12
    "images/tentacle/loop4/0186.jpg"
    pause .12
    "images/tentacle/loop4/0187.jpg"
    pause .12
    repeat

image tentcum:
    "images/tentacle/cum/0188.jpg"
    pause .12
    "images/tentacle/cum/0189.jpg"
    pause .12
    "images/tentacle/cum/0190.jpg"
    pause .12
    "images/tentacle/cum/0191.jpg"
    pause .12
    "images/tentacle/cum/0192.jpg"
    pause .12
    "images/tentacle/cum/0193.jpg"
    pause .12
    "images/tentacle/cum/0194.jpg"
    pause .12
    "images/tentacle/cum/0195.jpg"
    pause .12
    "images/tentacle/cum/0196.jpg"
    pause .12
    "images/tentacle/cum/0197.jpg"
    pause .12
    "images/tentacle/cum/0198.jpg"
    pause .12
    "images/tentacle/cum/0199.jpg"
    function splat2
    pause .12
    "images/tentacle/cum/0200.jpg"
    pause .12
    "images/tentacle/cum/0201.jpg"
    pause .12
    "images/tentacle/cum/0202.jpg"
    pause .12
    "images/tentacle/cum/0203.jpg"
    pause .12
    "images/tentacle/cum/0204.jpg"
    pause .12
    "images/tentacle/cum/0205.jpg"
    pause .12
    "images/tentacle/cum/0206.jpg"
    pause .12
    "images/tentacle/cum/0207.jpg"
    pause .12
    "images/tentacle/cum/0208.jpg"
    function cum1
    pause .12
    "images/tentacle/cum/0209.jpg"
    pause .12
    "images/tentacle/cum/0210.jpg"
    pause .12
    "images/tentacle/cum/0211.jpg"
    pause .12
    "images/tentacle/cum/0212.jpg"
    pause .12
    "images/tentacle/cum/0213.jpg"
    pause .12
    "images/tentacle/cum/0214.jpg"
    pause .12
    "images/tentacle/cum/0215.jpg"
    pause .12
    "images/tentacle/cum/0216.jpg"
    pause .12
    "images/tentacle/cum/0217.jpg"
    pause .12
    "images/tentacle/cum/0218.jpg"
    function cum1
    pause .12
    "images/tentacle/cum/0219.jpg"
    pause .12
    "images/tentacle/cum/0220.jpg"
    pause .12
    "images/tentacle/cum/0221.jpg"
    function squish
    pause .12
    "images/tentacle/cum/0222.jpg"
    pause .12
    "images/tentacle/cum/0223.jpg"
    pause .12
    "images/tentacle/cum/0224.jpg"
    pause .12
    "images/tentacle/cum/0225.jpg"
    pause .12
    "images/tentacle/cum/0226.jpg"
    pause .12
    "images/tentacle/cum/0227.jpg"
    function s2
    pause .12
    "images/tentacle/cum/0228.jpg"
    pause .12
    "images/tentacle/cum/0229.jpg"
    pause .12
    "images/tentacle/cum/0230.jpg"
    pause .12
    "images/tentacle/cum/0231.jpg"
    pause .12
    "images/tentacle/cum/0232.jpg"
    pause .12
    "images/tentacle/cum/0233.jpg"
    pause .12
    "images/tentacle/cum/0234.jpg"
    pause .12
    "images/tentacle/cum/0235.jpg"
    pause .12
    "images/tentacle/cum/0236.jpg"
    pause .12
    "images/tentacle/cum/0237.jpg"
    pause .12
    "images/tentacle/cum/0238.jpg"
    pause .12
    "images/tentacle/cum/0239.jpg"
    pause .12
    "images/tentacle/cum/0240.jpg"
    pause .12

image 16event1:
    "images/events/catch2/trans1/0066.jpg"
    pause .12
    "images/events/catch2/trans1/0067.jpg"
    pause .12
    "images/events/catch2/trans1/0068.jpg"
    pause .12
    "images/events/catch2/trans1/0069.jpg"
    pause .12
    "images/events/catch2/trans1/0070.jpg"
    pause .12
    "images/events/catch2/trans1/0071.jpg"
    pause .12
    "images/events/catch2/trans1/0072.jpg"
    pause .12
    "images/events/catch2/trans1/0073.jpg"
    pause .12
    "images/events/catch2/trans1/0074.jpg"
    pause .12
    "images/events/catch2/trans1/0075.jpg"
    pause .12
    "images/events/catch2/trans1/0078.jpg"
    pause .12
    "images/events/catch2/trans1/0077.jpg"
    pause .12
    "images/events/catch2/trans1/0078.jpg"
    pause .12
    "images/events/catch2/trans1/0079.jpg"
    pause .12
    "images/events/catch2/trans1/0080.jpg"
    function fall
    pause .12
    "images/events/catch2/trans1/0081.jpg"
    pause .12

image 16event2:
    "images/events/catch2/trans2/0082.jpg"
    pause .12
    "images/events/catch2/trans2/0083.jpg"
    pause .12
    "images/events/catch2/trans2/0084.jpg"
    pause .12
    "images/events/catch2/trans2/0085.jpg"
    pause .12
    "images/events/catch2/trans2/0086.jpg"
    pause .12
    "images/events/catch2/trans2/0087.jpg"
    pause .12
    "images/events/catch2/trans2/0088.jpg"
    pause .12
    "images/events/catch2/trans2/0089.jpg"
    pause .12
    "images/events/catch2/trans2/0090.jpg"
    pause .12
    "images/events/catch2/trans2/0091.jpg"
    pause .12
    "images/events/catch2/trans2/0092.jpg"
    pause .12
    "images/events/catch2/trans2/0093.jpg"
    pause .12
    "images/events/catch2/trans2/0094.jpg"
    pause .12
    "images/events/catch2/trans2/0095.jpg"
    pause .12
    "images/events/catch2/trans2/0096.jpg"
    pause .12
    "images/events/catch2/trans2/0097.jpg"
    pause .12
    "images/events/catch2/trans2/0098.jpg"
    pause .12
    "images/events/catch2/trans2/0099.jpg"
    pause .12
    "images/events/catch2/trans2/0100.jpg"
    pause .12

image 16eventstruggle:
    "images/events/catch2/struggle/0101.jpg"
    pause .12
    "images/events/catch2/struggle/0102.jpg"
    pause .12
    "images/events/catch2/struggle/0103.jpg"
    pause .12
    "images/events/catch2/struggle/0104.jpg"
    pause .12
    "images/events/catch2/struggle/0105.jpg"
    pause .12
    "images/events/catch2/struggle/0106.jpg"
    pause .12
    "images/events/catch2/struggle/0107.jpg"
    pause .12
    "images/events/catch2/struggle/0108.jpg"
    pause .12
    "images/events/catch2/struggle/0109.jpg"
    pause .12
    "images/events/catch2/struggle/0110.jpg"
    pause .12
    repeat

image 16event3:
    "images/events/catch2/loop1/0112.jpg"
    pause .12
    "images/events/catch2/loop1/0113.jpg"
    pause .12
    "images/events/catch2/loop1/0114.jpg"
    pause .12
    "images/events/catch2/loop1/0115.jpg"
    pause .12
    "images/events/catch2/loop1/0116.jpg"
    pause .12
    "images/events/catch2/loop1/0117.jpg"
    pause .12
    "images/events/catch2/loop1/0118.jpg"
    function inside
    pause .12
    "images/events/catch2/loop1/0119.jpg"
    pause .12
    "images/events/catch2/loop1/0120.jpg"
    pause .12
    "images/events/catch2/loop1/0121.jpg"
    pause .12
    repeat

image 16event4:
    "images/events/catch2/trans3/0125.jpg"
    pause .12
    "images/events/catch2/trans3/0126.jpg"
    pause .12
    "images/events/catch2/trans3/0127.jpg"
    pause .12
    "images/events/catch2/trans3/0128.jpg"
    pause .12
    "images/events/catch2/trans3/0129.jpg"
    pause .12
    "images/events/catch2/trans3/0130.jpg"
    pause .12
    "images/events/catch2/trans3/0131.jpg"
    pause .12
    "images/events/catch2/trans3/0132.jpg"
    function splat1
    pause .12
    "images/events/catch2/trans3/0133.jpg"
    pause .12
    "images/events/catch2/trans3/0134.jpg"
    pause .12
    "images/events/catch2/trans3/0135.jpg"
    pause .12

image 16event5:
    "images/events/catch2/loop2/0135.jpg"
    pause .12
    "images/events/catch2/loop2/0136.jpg"
    pause .12
    "images/events/catch2/loop2/0137.jpg"
    pause .12
    "images/events/catch2/loop2/0138.jpg"
    function slap1
    pause .12
    "images/events/catch2/loop2/0139.jpg"
    pause .12
    "images/events/catch2/loop2/0140.jpg"
    pause .12
    "images/events/catch2/loop2/0141.jpg"
    pause .12
    repeat

image 16eventcum:
    "images/events/catch2/cum/0142.jpg"
    pause .12
    "images/events/catch2/cum/0143.jpg"
    pause .12
    "images/events/catch2/cum/0144.jpg"
    pause .12
    "images/events/catch2/cum/0145.jpg"
    pause .12
    "images/events/catch2/cum/0146.jpg"
    function splat2
    pause .12
    "images/events/catch2/cum/0147.jpg"
    pause .12
    "images/events/catch2/cum/0148.jpg"
    pause .12
    "images/events/catch2/cum/0149.jpg"
    pause .12
    "images/events/catch2/cum/0150.jpg"
    pause .12
    "images/events/catch2/cum/0151.jpg"
    pause .12
    "images/events/catch2/cum/0152.jpg"
    function cum1
    pause .12
    "images/events/catch2/cum/0153.jpg"
    pause .12
    "images/events/catch2/cum/0154.jpg"
    pause .12
    "images/events/catch2/cum/0155.jpg"
    pause .12
    "images/events/catch2/cum/0156.jpg"
    pause .12
    "images/events/catch2/cum/0157.jpg"
    pause .12
    "images/events/catch2/cum/0158.jpg"
    function cum1
    pause .12
    "images/events/catch2/cum/0159.jpg"
    pause .12
    "images/events/catch2/cum/0160.jpg"
    pause .12
    "images/events/catch2/cum/0161.jpg"
    pause .12
    "images/events/catch2/cum/0162.jpg"
    pause .12
    "images/events/catch2/cum/0163.jpg"
    pause .12
    "images/events/catch2/cum/0164.jpg"
    pause .12
    "images/events/catch2/cum/0165.jpg"
    pause .12
    "images/events/catch2/cum/0166.jpg"
    pause .12
    "images/events/catch2/cum/0167.jpg"
    pause .12
    "images/events/catch2/cum/0168.jpg"
    pause .12
    "images/events/catch2/cum/0169.jpg"
    pause .12
    "images/events/catch2/cum/0170.jpg"
    pause .12

image flesh1dead1:
    "images/explosion/1/0085.jpg"
    pause .12
    "images/explosion/1/0086.jpg"
    pause .12
    "images/explosion/1/0087.jpg"
    pause .12
    "images/explosion/1/0088.jpg"
    pause .12
    "images/explosion/1/0089.jpg"
    pause .12
    "images/explosion/1/0090.jpg"
    pause .12
    "images/explosion/1/0091.jpg"
    pause .12
    "images/explosion/1/0092.jpg"
    pause .12
    "images/explosion/1/0093.jpg"
    pause .12
    "images/explosion/1/0094.jpg"
    pause .12
    "images/explosion/1/0095.jpg"
    pause .12

image flesh1dead2:
    "images/explosion/2/0095.jpg"
    pause .12
    "images/explosion/2/0096.jpg"
    pause .12
    "images/explosion/2/0097.jpg"
    pause .12
    "images/explosion/2/0098.jpg"
    pause .12
    "images/explosion/2/0099.jpg"
    pause .12
    "images/explosion/2/0100.jpg"
    pause .12
    "images/explosion/2/0101.jpg"
    pause .12
    "images/explosion/2/0102.jpg"
    pause .12
    "images/explosion/2/0103.jpg"
    pause .12
    "images/explosion/2/0104.jpg"
    pause .12
    "images/explosion/2/0105.jpg"
    pause .12

image vent5open:
    "images/vent4_0hatch/0085.jpg"
    pause .12
    "images/vent4_0hatch/0086.jpg"
    pause .12
    "images/vent4_0hatch/0087.jpg"
    pause .12
    "images/vent4_0hatch/0088.jpg"
    pause .12
    "images/vent4_0hatch/0089.jpg"
    pause .12
    "images/vent4_0hatch/0090.jpg"
    pause .12
    "images/vent4_0hatch/0091.jpg"
    function metal2
    pause .12
    "images/vent4_0hatch/0092.jpg"
    pause .12
    "images/vent4_0hatch/0093.jpg"
    pause .12
    "images/vent4_0hatch/0094.jpg"
    pause .12
    "images/vent4_0hatch/0095.jpg"
    pause .12

image amihatch1:
    "images/vent5_5hatch/0001.jpg"
    pause .12
    "images/vent5_5hatch/0002.jpg"
    pause .12
    "images/vent5_5hatch/0003.jpg"
    pause .12
    "images/vent5_5hatch/0004.jpg"
    pause .12
    "images/vent5_5hatch/0005.jpg"
    pause .12

image amihatch2:
    "images/vent5_5hatch/0005.jpg"
    pause .12
    "images/vent5_5hatch/0004.jpg"
    pause .12
    "images/vent5_5hatch/0003.jpg"
    pause .12
    "images/vent5_5hatch/0002.jpg"
    pause .12
    "images/vent5_5hatch/0001.jpg"
    pause .12

image amihatch3:
    "images/vent5_5hatch/0005.jpg"
    pause .12
    "images/vent5_5hatch/0006.jpg"
    pause .12
    "images/vent5_5hatch/0007.jpg"
    pause .12
    "images/vent5_5hatch/0008.jpg"
    function metaldoor
    pause .12
    "images/vent5_5hatch/0009.jpg"
    pause .12
    "images/vent5_5hatch/0010.jpg"
    pause .12
    "images/vent5_5hatch/0011.jpg"
    pause .12
    "images/vent5_5hatch/0012.jpg"
    pause .12
    "images/vent5_5hatch/0013.jpg"
    pause .12
    "images/vent5_5hatch/0014.jpg"
    pause .12
    "images/vent5_5hatch/0015.jpg"
    pause .12

image ami1:
    "images/ami/1/0001.jpg"
    pause 0.1
    "images/ami/1/0002.jpg"
    pause 0.1
    "images/ami/1/0003.jpg"
    pause 0.1
    "images/ami/1/0004.jpg"
    pause 0.1
    "images/ami/1/0005.jpg"
    pause 0.1
    "images/ami/1/0006.jpg"
    pause 0.1
    "images/ami/1/0007.jpg"
    function inside
    pause 0.1
    "images/ami/1/0008.jpg"
    pause 0.1
    "images/ami/1/0009.jpg"
    pause 0.1
    repeat

image ami2:
    "images/ami/2/0010.jpg"
    pause 0.1
    "images/ami/2/0011.jpg"
    pause 0.1
    "images/ami/2/0012.jpg"
    pause 0.1
    "images/ami/2/0013.jpg"
    pause 0.1
    "images/ami/2/0014.jpg"
    pause 0.1
    "images/ami/2/0015.jpg"
    pause 0.1
    "images/ami/2/0016.jpg"
    function s3
    pause 0.1
    "images/ami/2/0017.jpg"
    pause 0.1
    "images/ami/2/0018.jpg"
    pause 0.1
    "images/ami/2/0019.jpg"
    pause 0.1
    "images/ami/2/0020.jpg"
    pause 0.1
    "images/ami/2/0021.jpg"
    pause 0.1
    "images/ami/2/0022.jpg"
    pause 0.1
    "images/ami/2/0023.jpg"
    pause 0.1
    "images/ami/2/0024.jpg"
    function s4
    pause 0.1
    "images/ami/2/0025.jpg"
    pause 0.1
    "images/ami/2/0026.jpg"
    pause 0.1
    "images/ami/2/0027.jpg"
    pause 0.1
    "images/ami/2/0028.jpg"
    pause 0.1
    "images/ami/2/0029.jpg"
    pause 0.1
    "images/ami/2/0030.jpg"
    pause 0.1
    "images/ami/2/0031.jpg"
    pause 0.1
    "images/ami/2/0032.jpg"
    pause 0.1
    "images/ami/2/0033.jpg"
    pause 0.1
    "images/ami/2/0034.jpg"
    pause 0.1
    "images/ami/2/0035.jpg"
    pause 0.1
    "images/ami/2/0036.jpg"
    pause 0.1
    "images/ami/2/0037.jpg"
    function s1
    pause 0.1
    "images/ami/2/0038.jpg"
    pause 0.1
    "images/ami/2/0039.jpg"
    pause 0.1
    "images/ami/2/0040.jpg"
    pause 0.1
    "images/ami/2/0041.jpg"
    pause 0.1
    "images/ami/2/0042.jpg"
    pause 0.1
    "images/ami/2/0043.jpg"
    pause 0.1
    "images/ami/2/0044.jpg"
    pause 0.1
    "images/ami/2/0045.jpg"
    pause 0.1
    "images/ami/2/0046.jpg"
    function s2
    pause 0.1
    "images/ami/2/0047.jpg"
    pause 0.1
    "images/ami/2/0048.jpg"
    pause 0.1
    "images/ami/2/0049.jpg"
    pause 0.1
    "images/ami/2/0050.jpg"
    pause 0.1

image ami3:
    "images/ami/3/0050.jpg"
    pause 0.1
    "images/ami/3/0051.jpg"
    pause 0.1
    "images/ami/3/0052.jpg"
    pause 0.1
    "images/ami/3/0053.jpg"
    function slurp
    pause 0.1
    "images/ami/3/0054.jpg"
    pause 0.1
    "images/ami/3/0055.jpg"
    pause 0.1
    "images/ami/3/0056.jpg"
    pause 0.1
    "images/ami/3/0057.jpg"
    pause 0.1
    "images/ami/3/0058.jpg"
    pause 0.1
    "images/ami/3/0059.jpg"
    pause 0.1
    "images/ami/3/0060.jpg"
    pause 0.1
    "images/ami/3/0061.jpg"
    pause 0.1
    "images/ami/3/0062.jpg"
    pause 0.1
    repeat

image ami4:
    "images/ami/4/0063.jpg"
    pause 0.12
    "images/ami/4/0064.jpg"
    function cum1
    pause 0.12
    "images/ami/4/0065.jpg"
    pause 0.12
    "images/ami/4/0066.jpg"
    pause 0.12
    "images/ami/4/0067.jpg"
    pause 0.12
    "images/ami/4/0068.jpg"
    pause 0.12
    "images/ami/4/0069.jpg"
    pause 0.12
    "images/ami/4/0070.jpg"
    pause 0.12
    "images/ami/4/0071.jpg"
    pause 0.12
    "images/ami/4/0072.jpg"
    pause 0.12
    "images/ami/4/0073.jpg"
    function splat1
    pause 0.12
    "images/ami/4/0074.jpg"
    pause 0.12
    "images/ami/4/0075.jpg"
    pause 0.12
    "images/ami/4/0076.jpg"
    pause 0.12
    "images/ami/4/0077.jpg"
    pause 0.12
    function splat2
    "images/ami/4/0078.jpg"
    pause 0.12
    "images/ami/4/0079.jpg"
    pause 0.12
    "images/ami/4/0080.jpg"
    pause 0.12

image ami5:
    "images/ami/5/0015.jpg"
    pause 0.1
    "images/ami/5/0016.jpg"
    pause 0.1
    "images/ami/5/0017.jpg"
    pause 0.1
    "images/ami/5/0018.jpg"
    pause 0.1
    "images/ami/5/0019.jpg"
    pause 0.1
    "images/ami/5/0020.jpg"
    pause 0.1
    "images/ami/5/0021.jpg"
    pause 0.1
    "images/ami/5/0022.jpg"
    pause 0.1
    "images/ami/5/0023.jpg"
    pause 0.1
    "images/ami/5/0024.jpg"
    pause 0.1
    "images/ami/5/0025.jpg"
    pause 0.1
    "images/ami/5/0026.jpg"
    pause 0.1
    "images/ami/5/0027.jpg"
    pause 0.1
    "images/ami/5/0028.jpg"
    pause 0.1
    "images/ami/5/0029.jpg"
    pause 0.1
    "images/ami/5/0030.jpg"
    pause 0.1
    "images/ami/5/0031.jpg"
    pause 0.1
    "images/ami/5/0032.jpg"
    pause 0.1
    "images/ami/5/0033.jpg"
    pause 0.1
    "images/ami/5/0034.jpg"
    pause 0.1
    "images/ami/5/0035.jpg"
    pause 0.1
    "images/ami/5/0036.jpg"
    pause 0.1
    "images/ami/5/0037.jpg"
    pause 0.1
    "images/ami/5/0038.jpg"
    pause 0.1
    "images/ami/5/0039.jpg"
    pause 0.1
    "images/ami/5/0040.jpg"
    pause 0.1
    "images/ami/5/0041.jpg"
    pause 0.1
    "images/ami/5/0042.jpg"
    pause 0.1
    "images/ami/5/0043.jpg"
    pause 0.1
    "images/ami/5/0044.jpg"
    pause 0.1
    "images/ami/5/0045.jpg"
    pause 0.1
    "images/ami/5/0046.jpg"
    pause 0.1
    "images/ami/5/0047.jpg"
    pause 0.1
    "images/ami/5/0048.jpg"
    pause 0.1
    "images/ami/5/0049.jpg"
    pause 0.1
    "images/ami/5/0050.jpg"
    pause 0.1
    "images/ami/5/0051.jpg"
    pause 0.1
    "images/ami/5/0052.jpg"
    pause 0.1
    "images/ami/5/0053.jpg"
    pause 0.1
    "images/ami/5/0054.jpg"
    pause 0.1
    "images/ami/5/0055.jpg"
    pause 0.1
    "images/ami/5/0056.jpg"
    pause 0.1
    "images/ami/5/0057.jpg"
    pause 0.1
    "images/ami/5/0058.jpg"
    pause 0.1
    "images/ami/5/0059.jpg"
    pause 0.1
    "images/ami/5/0060.jpg"
    pause 0.1
    "images/ami/5/0061.jpg"
    pause 0.1
    "images/ami/5/0062.jpg"
    pause 0.1
    "images/ami/5/0063.jpg"
    pause 0.1
    "images/ami/5/0064.jpg"
    pause 0.1
    "images/ami/5/0065.jpg"
    pause 0.1
    "images/ami/5/0066.jpg"
    pause 0.1
    "images/ami/5/0067.jpg"
    pause 0.1
    "images/ami/5/0068.jpg"
    pause 0.1
    "images/ami/5/0069.jpg"
    pause 0.1
    "images/ami/5/0070.jpg"
    pause 0.1

image 59hatch1:
    "images/vent5_9hatch/1/0195.jpg"
    pause .12
    "images/vent5_9hatch/1/0196.jpg"
    pause .12
    "images/vent5_9hatch/1/0197.jpg"
    pause .12
    "images/vent5_9hatch/1/0198.jpg"
    pause .12
    "images/vent5_9hatch/1/0199.jpg"
    pause .12
    "images/vent5_9hatch/1/0200.jpg"
    pause .12
    "images/vent5_9hatch/1/0201.jpg"
    pause .12
    "images/vent5_9hatch/1/0202.jpg"
    pause .12
    "images/vent5_9hatch/1/0203.jpg"
    pause .12
    "images/vent5_9hatch/1/0204.jpg"
    pause .12
    "images/vent5_9hatch/1/0205.jpg"
    pause .12

image 59hatch2:
    "images/vent5_9hatch/1/0205.jpg"
    pause .12
    "images/vent5_9hatch/1/0204.jpg"
    pause .12
    "images/vent5_9hatch/1/0203.jpg"
    pause .12
    "images/vent5_9hatch/1/0202.jpg"
    pause .12
    "images/vent5_9hatch/1/0201.jpg"
    pause .12
    "images/vent5_9hatch/1/0200.jpg"
    pause .12
    "images/vent5_9hatch/1/0199.jpg"
    pause .12
    "images/vent5_9hatch/1/0198.jpg"
    pause .12
    "images/vent5_9hatch/1/0197.jpg"
    pause .12
    "images/vent5_9hatch/1/0196.jpg"
    pause .12
    "images/vent5_9hatch/1/0195.jpg"
    pause .12

image 59hatch3:
    "images/vent5_9hatch/2/0195.jpg"
    pause .12
    "images/vent5_9hatch/2/0196.jpg"
    pause .12
    "images/vent5_9hatch/2/0197.jpg"
    pause .12
    "images/vent5_9hatch/2/0198.jpg"
    pause .12
    "images/vent5_9hatch/2/0199.jpg"
    pause .12
    "images/vent5_9hatch/2/0200.jpg"
    pause .12
    "images/vent5_9hatch/2/0201.jpg"
    pause .12
    "images/vent5_9hatch/2/0202.jpg"
    pause .12
    "images/vent5_9hatch/2/0203.jpg"
    pause .12
    "images/vent5_9hatch/2/0204.jpg"
    pause .12
    "images/vent5_9hatch/2/0205.jpg"
    pause .12

image 59hatch4:
    "images/vent5_9hatch/2/0205.jpg"
    pause .12
    "images/vent5_9hatch/2/0204.jpg"
    pause .12
    "images/vent5_9hatch/2/0203.jpg"
    pause .12
    "images/vent5_9hatch/2/0202.jpg"
    pause .12
    "images/vent5_9hatch/2/0201.jpg"
    pause .12
    "images/vent5_9hatch/2/0200.jpg"
    pause .12
    "images/vent5_9hatch/2/0199.jpg"
    pause .12
    "images/vent5_9hatch/2/0198.jpg"
    pause .12
    "images/vent5_9hatch/2/0197.jpg"
    pause .12
    "images/vent5_9hatch/2/0196.jpg"
    pause .12
    "images/vent5_9hatch/2/0195.jpg"
    pause .12

image 59hatch5:
    "images/vent5_9hatch/3/0195.jpg"
    pause .12
    "images/vent5_9hatch/3/0196.jpg"
    pause .12
    "images/vent5_9hatch/3/0197.jpg"
    pause .12
    "images/vent5_9hatch/3/0198.jpg"
    pause .12
    "images/vent5_9hatch/3/0199.jpg"
    pause .12
    "images/vent5_9hatch/3/0200.jpg"
    pause .12
    "images/vent5_9hatch/3/0201.jpg"
    pause .12
    "images/vent5_9hatch/3/0202.jpg"
    pause .12
    "images/vent5_9hatch/3/0203.jpg"
    pause .12
    "images/vent5_9hatch/3/0204.jpg"
    pause .12
    "images/vent5_9hatch/3/0205.jpg"
    pause .12


image nyunvent1:
    "images/nyun/1/0010.jpg"
    pause .1
    "images/nyun/1/0011.jpg"
    pause .1
    "images/nyun/1/0012.jpg"
    pause .1
    "images/nyun/1/0013.jpg"
    pause .1
    "images/nyun/1/0014.jpg"
    pause .1
    "images/nyun/1/0015.jpg"
    pause .1
    "images/nyun/1/0016.jpg"
    function splat1
    pause .1
    "images/nyun/1/0017.jpg"
    pause .1
    "images/nyun/1/0018.jpg"
    pause .1
    repeat

image nyunvent2:
    "images/nyun/2/0010.jpg"
    pause .1
    "images/nyun/2/0011.jpg"
    pause .1
    "images/nyun/2/0012.jpg"
    pause .1
    "images/nyun/2/0013.jpg"
    pause .1
    "images/nyun/2/0014.jpg"
    pause .1
    "images/nyun/2/0015.jpg"
    pause .1
    "images/nyun/2/0016.jpg"
    function splat1
    pause .1
    "images/nyun/2/0017.jpg"
    pause .1
    "images/nyun/2/0018.jpg"
    pause .1
    repeat

image nyunvent3:
    "images/nyun/3/0019.jpg"
    pause .1
    "images/nyun/3/0020.jpg"
    pause .1
    "images/nyun/3/0021.jpg"
    pause .1
    "images/nyun/3/0022.jpg"
    pause .1
    "images/nyun/3/0023.jpg"
    pause .1
    "images/nyun/3/0024.jpg"
    function s2
    pause .1
    "images/nyun/3/0025.jpg"
    pause .1
    "images/nyun/3/0026.jpg"
    pause .1
    "images/nyun/3/0027.jpg"
    pause .1
    "images/nyun/3/0028.jpg"
    pause .1
    "images/nyun/3/0029.jpg"
    pause .1
    "images/nyun/3/0030.jpg"
    pause .1
    "images/nyun/3/0031.jpg"
    pause .1
    "images/nyun/3/0032.jpg"
    pause .1
    "images/nyun/3/0033.jpg"
    pause .1
    "images/nyun/3/0034.jpg"
    pause .1
    "images/nyun/3/0035.jpg"
    pause .1
    "images/nyun/3/0036.jpg"
    pause .1
    "images/nyun/3/0037.jpg"
    pause .1
    "images/nyun/3/0038.jpg"
    pause .1
    "images/nyun/3/0039.jpg"
    pause .1
    "images/nyun/3/0040.jpg"
    pause .1
    "images/nyun/3/0041.jpg"
    pause .1
    "images/nyun/3/0042.jpg"
    pause .1
    "images/nyun/3/0043.jpg"
    function s1
    pause .1
    "images/nyun/3/0044.jpg"
    pause .1
    "images/nyun/3/0045.jpg"
    pause .1
    "images/nyun/3/0046.jpg"
    pause .1
    "images/nyun/3/0047.jpg"
    pause .1
    "images/nyun/3/0048.jpg"
    pause .1
    "images/nyun/3/0049.jpg"
    pause .1
    "images/nyun/3/0050.jpg"
    function splat1
    pause .1
    "images/nyun/3/0051.jpg"
    pause .1
    "images/nyun/3/0052.jpg"
    pause .1
    "images/nyun/3/0053.jpg"
    pause .1
    "images/nyun/3/0054.jpg"
    pause .1
    "images/nyun/3/0055.jpg"
    pause .1
    "images/nyun/3/0056.jpg"
    pause .1

image nyunvent4:
    "images/nyun/4/0057.jpg"
    pause .1
    "images/nyun/4/0058.jpg"
    pause .1
    "images/nyun/4/0059.jpg"
    pause .1
    "images/nyun/4/0060.jpg"
    pause .1
    "images/nyun/4/0061.jpg"
    function s4
    pause .1
    "images/nyun/4/0062.jpg"
    pause .1
    "images/nyun/4/0063.jpg"
    pause .1
    repeat

image nyunvent5:
    "images/nyun/5/0019.jpg"
    pause .1
    "images/nyun/5/0020.jpg"
    pause .1
    "images/nyun/5/0021.jpg"
    pause .1
    "images/nyun/5/0022.jpg"
    function s4
    pause .1
    "images/nyun/5/0023.jpg"
    pause .1
    "images/nyun/5/0024.jpg"
    pause .1
    "images/nyun/5/0025.jpg"
    pause .1
    repeat

image nyunvent6:
    "images/nyun/6/0064.jpg"
    pause .1
    "images/nyun/6/0065.jpg"
    pause .1
    "images/nyun/6/0066.jpg"
    pause .1
    "images/nyun/6/0067.jpg"
    pause .1
    "images/nyun/6/0068.jpg"
    pause .1
    "images/nyun/6/0069.jpg"
    function splat1
    pause .1
    "images/nyun/6/0070.jpg"
    pause .1
    "images/nyun/6/0071.jpg"
    pause .1
    "images/nyun/6/0072.jpg"
    pause .1
    "images/nyun/6/0073.jpg"
    pause .1
    "images/nyun/6/0074.jpg"
    pause .1
    "images/nyun/6/0075.jpg"
    pause .1
    "images/nyun/6/0076.jpg"
    pause .1
    "images/nyun/6/0077.jpg"
    pause .1
    "images/nyun/6/0078.jpg"
    pause .1
    "images/nyun/6/0079.jpg"
    pause .1
    "images/nyun/6/0080.jpg"
    pause .1
    "images/nyun/6/0081.jpg"
    pause .1
    "images/nyun/6/0082.jpg"
    pause .1
    "images/nyun/6/0083.jpg"
    pause .1
    "images/nyun/6/0084.jpg"
    pause .1
    "images/nyun/6/0085.jpg"
    pause .1
    "images/nyun/6/0086.jpg"
    function splat2
    pause .1
    "images/nyun/6/0087.jpg"
    pause .1
    "images/nyun/6/0088.jpg"
    pause .1
    "images/nyun/6/0089.jpg"
    pause .1

image nyunvent7:
    "images/nyun/7/0023.jpg"
    pause .1
    "images/nyun/7/0024.jpg"
    pause .1
    "images/nyun/7/0025.jpg"
    pause .1
    "images/nyun/7/0026.jpg"
    pause .1
    "images/nyun/7/0027.jpg"
    pause .1
    "images/nyun/7/0028.jpg"
    pause .1
    "images/nyun/7/0029.jpg"
    pause .1
    "images/nyun/7/0030.jpg"
    pause .1
    "images/nyun/7/0031.jpg"
    pause .1
    "images/nyun/7/0032.jpg"
    pause .1
    "images/nyun/7/0033.jpg"
    function splat2
    pause .1
    "images/nyun/7/0034.jpg"
    pause .1
    "images/nyun/7/0035.jpg"
    pause .1
    "images/nyun/7/0036.jpg"
    pause .1
    "images/nyun/7/0037.jpg"
    pause .1
    "images/nyun/7/0038.jpg"
    pause .1
    "images/nyun/7/0039.jpg"
    pause .1
    "images/nyun/7/0040.jpg"
    pause .1
    "images/nyun/7/0041.jpg"
    pause .1
    "images/nyun/7/0042.jpg"
    pause .1
    "images/nyun/7/0043.jpg"
    pause .1
    "images/nyun/7/0044.jpg"
    function suck4
    pause .1
    "images/nyun/7/0045.jpg"
    pause .1
    "images/nyun/7/0046.jpg"
    pause .1

image nyunvent8:
    "images/nyun/8/0046.jpg"
    pause .1
    "images/nyun/8/0047.jpg"
    pause .1
    "images/nyun/8/0048.jpg"
    pause .1
    "images/nyun/8/0049.jpg"
    pause .1
    "images/nyun/8/0050.jpg"
    pause .1
    "images/nyun/8/0051.jpg"
    pause .1
    "images/nyun/8/0052.jpg"
    pause .1
    "images/nyun/8/0053.jpg"
    pause .1
    "images/nyun/8/0054.jpg"
    function splat2
    pause .1
    "images/nyun/8/0055.jpg"
    pause .1
    "images/nyun/8/0056.jpg"
    pause .1
    "images/nyun/8/0057.jpg"
    pause .1
    "images/nyun/8/0058.jpg"
    pause .1
    "images/nyun/8/0059.jpg"
    pause .1
    "images/nyun/8/0060.jpg"
    pause .1
    "images/nyun/8/0061.jpg"
    pause .1
    "images/nyun/8/0062.jpg"
    pause .1
    "images/nyun/8/0063.jpg"
    pause .1
    "images/nyun/8/0064.jpg"
    pause .1
    "images/nyun/8/0065.jpg"
    function splat2
    pause .1
    "images/nyun/8/0066.jpg"
    pause .1
    "images/nyun/8/0067.jpg"
    pause .1
    "images/nyun/8/0068.jpg"
    pause .1
    "images/nyun/8/0069.jpg"
    pause .1
    "images/nyun/8/0070.jpg"
    pause .1
    "images/nyun/8/0071.jpg"
    pause .1
    "images/nyun/8/0072.jpg"
    pause .1
    "images/nyun/8/0073.jpg"
    pause .1
    "images/nyun/8/0074.jpg"
    pause .1
    "images/nyun/8/0075.jpg"
    pause .1
    "images/nyun/8/0076.jpg"
    pause .1
    "images/nyun/8/0077.jpg"
    function squish
    pause .1
    "images/nyun/8/0078.jpg"
    pause .1
    "images/nyun/8/0079.jpg"
    pause .1

image nyunvent9:
    "images/nyun/9/0001.jpg"
    pause .1
    "images/nyun/9/0002.jpg"
    pause .1
    "images/nyun/9/0003.jpg"
    pause .1
    "images/nyun/9/0004.jpg"
    pause .1
    "images/nyun/9/0005.jpg"
    function s4
    pause .1
    "images/nyun/9/0006.jpg"
    pause .1
    repeat

image nyunvent10:
    "images/nyun/10/0007.jpg"
    pause .1
    "images/nyun/10/0008.jpg"
    pause .1
    "images/nyun/10/0009.jpg"
    pause .1
    "images/nyun/10/0010.jpg"
    pause .1
    "images/nyun/10/0011.jpg"
    function splat1
    pause .1
    "images/nyun/10/0012.jpg"
    pause .1
    repeat

image nyunvent11:
    "images/nyun/11/0007.jpg"
    pause .1
    "images/nyun/11/0008.jpg"
    pause .1
    "images/nyun/11/0009.jpg"
    pause .1
    "images/nyun/11/0010.jpg"
    pause .1
    "images/nyun/11/0011.jpg"
    pause .1
    "images/nyun/11/0012.jpg"
    function suck1
    pause .1
    "images/nyun/11/0013.jpg"
    pause .1
    "images/nyun/11/0014.jpg"
    pause .1
    "images/nyun/11/0015.jpg"
    function splat2
    pause .1
    "images/nyun/11/0016.jpg"
    pause .1
    "images/nyun/11/0017.jpg"
    pause .1
    "images/nyun/11/0018.jpg"
    pause .1
    "images/nyun/11/0019.jpg"
    pause .1
    "images/nyun/11/0020.jpg"
    pause .1
    "images/nyun/11/0021.jpg"
    pause .1
    "images/nyun/11/0022.jpg"
    pause .1
    "images/nyun/11/0023.jpg"
    function splat2
    pause .1
    "images/nyun/11/0024.jpg"
    pause .1
    "images/nyun/11/0025.jpg"
    pause .1
    "images/nyun/11/0026.jpg"
    pause .1
    "images/nyun/11/0027.jpg"
    pause .1
    "images/nyun/11/0028.jpg"
    pause .1
    "images/nyun/11/0029.jpg"
    pause .1
    "images/nyun/11/0030.jpg"
    function squish
    pause .1
    "images/nyun/11/0031.jpg"
    pause .1
    "images/nyun/11/0032.jpg"
    pause .1
    "images/nyun/11/0033.jpg"
    pause .1
    "images/nyun/11/0034.jpg"
    pause .1
    "images/nyun/11/0035.jpg"
    pause .1
    "images/nyun/11/0036.jpg"
    pause .1
    "images/nyun/11/0037.jpg"
    pause .1
    "images/nyun/11/0038.jpg"
    pause .1
    "images/nyun/11/0039.jpg"
    pause .1
    "images/nyun/11/0040.jpg"
    pause .1

image nyunvent12:
    "images/nyun/12/0040.jpg"
    pause .1
    "images/nyun/12/0041.jpg"
    pause .1
    "images/nyun/12/0042.jpg"
    pause .1
    "images/nyun/12/0043.jpg"
    pause .1
    "images/nyun/12/0044.jpg"
    pause .1
    "images/nyun/12/0045.jpg"
    function s2
    pause .1
    "images/nyun/12/0046.jpg"
    pause .1
    "images/nyun/12/0047.jpg"
    pause .1
    "images/nyun/12/0048.jpg"
    pause .1
    "images/nyun/12/0049.jpg"
    pause .1
    repeat

image 43hatch1:
    "images/vent4_3hatch/0120.jpg"
    pause .12
    "images/vent4_3hatch/0121.jpg"
    pause .12
    "images/vent4_3hatch/0122.jpg"
    pause .12
    "images/vent4_3hatch/0123.jpg"
    pause .12
    "images/vent4_3hatch/0124.jpg"
    pause .12
    "images/vent4_3hatch/0125.jpg"
    pause .12

image 43hatch2:
    "images/vent4_3hatch/0125.jpg"
    pause .12
    "images/vent4_3hatch/0124.jpg"
    pause .12
    "images/vent4_3hatch/0123.jpg"
    pause .12
    "images/vent4_3hatch/0122.jpg"
    pause .12
    "images/vent4_3hatch/0121.jpg"
    pause .12
    "images/vent4_3hatch/0120.jpg"
    pause .12

image 43hatch3:
    "images/vent4_3hatch/0125.jpg"
    pause .12
    "images/vent4_3hatch/0126.jpg"
    pause .12
    "images/vent4_3hatch/0127.jpg"
    pause .12
    "images/vent4_3hatch/0128.jpg"
    pause .12
    "images/vent4_3hatch/0129.jpg"
    pause .12
    "images/vent4_3hatch/0130.jpg"
    pause .12

image bughatch1:
    "images/bugevent/1/0150.jpg"
    pause .12
    "images/bugevent/1/0151.jpg"
    pause .12
    "images/bugevent/1/0152.jpg"
    pause .12
    "images/bugevent/1/0153.jpg"
    pause .12
    "images/bugevent/1/0154.jpg"
    pause .12
    "images/bugevent/1/0155.jpg"
    pause .12
    "images/bugevent/1/0156.jpg"
    pause .12
    "images/bugevent/1/0157.jpg"
    pause .12
    "images/bugevent/1/0158.jpg"
    pause .12
    function metal1
    "images/bugevent/1/0159.jpg"
    pause .12
    "images/bugevent/1/0160.jpg"
    pause .12
    "images/bugevent/1/0161.jpg"
    pause .12
    "images/bugevent/1/0162.jpg"
    pause .12
    "images/bugevent/1/0163.jpg"
    pause .12
    "images/bugevent/1/0164.jpg"
    pause .12
    "images/bugevent/1/0165.jpg"
    pause .12
    "images/bugevent/1/0166.jpg"
    pause .12
    "images/bugevent/1/0167.jpg"
    pause .12
    "images/bugevent/1/0168.jpg"
    pause .12
    "images/bugevent/1/0169.jpg"
    pause .12
    "images/bugevent/1/0170.jpg"
    pause .12
    "images/bugevent/1/0171.jpg"
    pause .12
    "images/bugevent/1/0172.jpg"
    pause .12
    "images/bugevent/1/0173.jpg"
    function step3
    pause .12
    "images/bugevent/1/0174.jpg"
    pause .12
    "images/bugevent/1/0175.jpg"
    pause .12
    "images/bugevent/1/0176.jpg"
    pause .12
    "images/bugevent/1/0177.jpg"
    pause .12
    "images/bugevent/1/0178.jpg"
    pause .12

image bughatch2:
    "images/bugevent/2/0179.jpg"
    pause .12
    "images/bugevent/2/0180.jpg"
    pause .12
    "images/bugevent/2/0181.jpg"
    pause .12
    "images/bugevent/2/0182.jpg"
    pause .12
    "images/bugevent/2/0183.jpg"
    pause .12
    "images/bugevent/2/0184.jpg"
    pause .12
    "images/bugevent/2/0185.jpg"
    pause .12
    "images/bugevent/2/0186.jpg"
    pause .12
    "images/bugevent/2/0187.jpg"
    pause .12
    "images/bugevent/2/0188.jpg"
    pause .12
    "images/bugevent/2/0189.jpg"
    pause .12
    "images/bugevent/2/0190.jpg"
    pause .12
    "images/bugevent/2/0191.jpg"
    pause .12
    "images/bugevent/2/0192.jpg"
    pause .12
    "images/bugevent/2/0193.jpg"
    pause .12
    "images/bugevent/2/0194.jpg"
    pause .12
    "images/bugevent/2/0195.jpg"
    pause .12
    "images/bugevent/2/0196.jpg"
    pause .12
    "images/bugevent/2/0197.jpg"
    pause .12
    "images/bugevent/2/0198.jpg"
    function fall
    pause .12
    "images/bugevent/2/0199.jpg"
    pause .12
    "images/bugevent/2/0200.jpg"
    pause .12
    "images/bugevent/2/0201.jpg"
    pause .12

image bughatch3:
    "images/bugevent/3/0201.jpg"
    pause .12
    "images/bugevent/3/0202.jpg"
    pause .12
    "images/bugevent/3/0203.jpg"
    pause .12
    "images/bugevent/3/0204.jpg"
    pause .12
    "images/bugevent/3/0205.jpg"
    pause .12
    "images/bugevent/3/0206.jpg"
    pause .12
    "images/bugevent/3/0207.jpg"
    pause .12
    "images/bugevent/3/0208.jpg"
    pause .12
    repeat

image bughatch4:
    "images/bugevent/4/0208.jpg"
    pause .12
    "images/bugevent/4/0209.jpg"
    pause .12
    "images/bugevent/4/0210.jpg"
    pause .12
    "images/bugevent/4/0211.jpg"
    pause .12
    "images/bugevent/4/0212.jpg"
    pause .12
    "images/bugevent/4/0213.jpg"
    pause .12
    "images/bugevent/4/0214.jpg"
    function punch
    pause .12
    "images/bugevent/4/0215.jpg"
    pause .12
    "images/bugevent/4/0216.jpg"
    pause .12
    "images/bugevent/4/0217.jpg"
    pause .12
    "images/bugevent/4/0218.jpg"
    pause .12
    "images/bugevent/4/0219.jpg"
    pause .12
    "images/bugevent/4/0220.jpg"
    pause .12
    "images/bugevent/4/0221.jpg"
    pause .12

image bughatch5:
    "images/bugevent/5/0227.jpg"
    pause .12
    "images/bugevent/5/0228.jpg"
    pause .12
    "images/bugevent/5/0229.jpg"
    pause .12
    "images/bugevent/5/0230.jpg"
    pause .12
    "images/bugevent/5/0231.jpg"
    pause .12
    "images/bugevent/5/0232.jpg"
    pause .12
    "images/bugevent/5/0233.jpg"
    pause .12
    function fall
    "images/bugevent/5/0234.jpg"
    pause .12

image bughatch6:
    "images/bugevent/6/0234.jpg"
    pause .12
    "images/bugevent/6/0235.jpg"
    pause .12
    "images/bugevent/6/0236.jpg"
    pause .12
    "images/bugevent/6/0237.jpg"
    pause .12
    "images/bugevent/6/0238.jpg"
    pause .12
    "images/bugevent/6/0239.jpg"
    pause .12
    "images/bugevent/6/0240.jpg"
    function s1
    pause .12
    "images/bugevent/6/0241.jpg"
    pause .12
    "images/bugevent/6/0242.jpg"
    pause .12
    "images/bugevent/6/0243.jpg"
    pause .12
    "images/bugevent/6/0244.jpg"
    pause .12
    "images/bugevent/6/0245.jpg"
    pause .12
    "images/bugevent/6/0246.jpg"
    pause .12
    "images/bugevent/6/0247.jpg"
    pause .12
    "images/bugevent/6/0248.jpg"
    pause .12
    "images/bugevent/6/0249.jpg"
    pause .12
    "images/bugevent/6/0250.jpg"
    pause .12
    "images/bugevent/6/0251.jpg"
    pause .12
    function suck1
    "images/bugevent/6/0252.jpg"
    pause .12
    "images/bugevent/6/0253.jpg"
    pause .12
    "images/bugevent/6/0254.jpg"
    pause .12

image bughatch7:
    "images/bugevent/7/0255.jpg"
    pause .12
    "images/bugevent/7/0256.jpg"
    pause .12
    "images/bugevent/7/0257.jpg"
    pause .12
    "images/bugevent/7/0258.jpg"
    pause .12
    function suck2
    "images/bugevent/7/0259.jpg"
    pause .12
    "images/bugevent/7/0260.jpg"
    pause .12
    "images/bugevent/7/0261.jpg"
    pause .12
    repeat

image bughatch8:
    "images/bugevent/8/0255.jpg"
    pause .12
    "images/bugevent/8/0256.jpg"
    pause .12
    "images/bugevent/8/0257.jpg"
    pause .12
    "images/bugevent/8/0258.jpg"
    pause .12
    function suck1
    "images/bugevent/8/0259.jpg"
    pause .12
    "images/bugevent/8/0260.jpg"
    pause .12
    "images/bugevent/8/0261.jpg"
    pause .12
    "images/bugevent/8/0262.jpg"
    pause .12
    "images/bugevent/8/0263.jpg"
    pause .12
    "images/bugevent/8/0264.jpg"
    pause .12
    "images/bugevent/8/0265.jpg"
    pause .12
    "images/bugevent/8/0266.jpg"
    pause .12
    "images/bugevent/8/0267.jpg"
    pause .12
    "images/bugevent/8/0268.jpg"
    pause .12
    "images/bugevent/8/0269.jpg"
    pause .12
    "images/bugevent/8/0270.jpg"
    pause .12
    "images/bugevent/8/0271.jpg"
    pause .12
    function suck4
    "images/bugevent/8/0272.jpg"
    pause .12
    "images/bugevent/8/0273.jpg"
    pause .12
    "images/bugevent/8/0274.jpg"
    pause .12

image bughatch9:
    "images/bugevent/9/0274.jpg"
    pause .12
    "images/bugevent/9/0275.jpg"
    pause .12
    "images/bugevent/9/0276.jpg"
    pause .12
    "images/bugevent/9/0277.jpg"
    pause .12
    "images/bugevent/9/0278.jpg"
    pause .12
    "images/bugevent/9/0279.jpg"
    pause .12
    function splat2
    "images/bugevent/9/0280.jpg"
    pause .12
    "images/bugevent/9/0281.jpg"
    pause .12
    "images/bugevent/9/0282.jpg"
    pause .12
    "images/bugevent/9/0283.jpg"
    pause .12
    "images/bugevent/9/0284.jpg"
    pause .12
    "images/bugevent/9/0285.jpg"
    pause .12
    "images/bugevent/9/0286.jpg"
    pause .12
    "images/bugevent/9/0287.jpg"
    pause .12
    "images/bugevent/9/0288.jpg"
    pause .12
    function splat2
    "images/bugevent/9/0289.jpg"
    pause .12
    "images/bugevent/9/0290.jpg"
    pause .12
    "images/bugevent/9/0291.jpg"
    pause .12
    "images/bugevent/9/0292.jpg"
    pause .12
    "images/bugevent/9/0293.jpg"
    pause .12
    "images/bugevent/9/0294.jpg"
    pause .12
    "images/bugevent/9/0295.jpg"
    pause .12
    "images/bugevent/9/0296.jpg"
    pause .12
    "images/bugevent/9/0297.jpg"
    pause .12
    "images/bugevent/9/0298.jpg"
    pause .12
    function splat2
    "images/bugevent/9/0299.jpg"
    pause .12
    "images/bugevent/9/0300.jpg"
    pause .12
    "images/bugevent/9/0301.jpg"
    pause .12
    "images/bugevent/9/0302.jpg"
    pause .12
    "images/bugevent/9/0303.jpg"
    pause .12
    "images/bugevent/9/0304.jpg"
    pause .12
    "images/bugevent/9/0305.jpg"
    pause .12
    "images/bugevent/9/0306.jpg"
    pause .12
    "images/bugevent/9/0307.jpg"
    pause .12
    "images/bugevent/9/0308.jpg"
    pause .12
    "images/bugevent/9/0309.jpg"
    pause .12
    "images/bugevent/9/0310.jpg"
    pause .12

image bughatch10:
    "images/bugevent/10/0226.jpg"
    pause .12
    "images/bugevent/10/0227.jpg"
    pause .12
    "images/bugevent/10/0228.jpg"
    pause .12
    "images/bugevent/10/0229.jpg"
    pause .12
    "images/bugevent/10/0230.jpg"
    pause .12
    "images/bugevent/10/0231.jpg"
    pause .12
    "images/bugevent/10/0232.jpg"
    pause .12
    "images/bugevent/10/0233.jpg"
    pause .12
    "images/bugevent/10/0234.jpg"
    pause .12
    "images/bugevent/10/0235.jpg"
    pause .12
    "images/bugevent/10/0236.jpg"
    pause .12

image bugshoot1:
    "images/bugevent/shoot/0221.jpg"
    pause .12
    function shot
    "images/bugevent/shoot/0222.jpg"
    pause .12
    "images/bugevent/shoot/0223.jpg"
    pause .12
    "images/bugevent/shoot/0224.jpg"
    pause .12
    "images/bugevent/shoot/0225.jpg"
    pause .12
    "images/bugevent/shoot/0226.jpg"
    pause .12


# -------------------- VENT MOVEMENTS ---------------------

image vent1_1 = Generate_Animation("images/vent1_1", 10)

image vent1_2 = Generate_Animation("images/vent1_2", 10)

image vent1_2back = Generate_Animation("images/vent1_2back", 8)

image vent1_2backb = Generate_Animation("images/vent1_2backb", 8)

image vent1_3 = Generate_Animation("images/vent1_3", 10)

image vent1_3b = Generate_Animation("images/vent1_3b", 10)

image vent1_3fwd = Generate_Animation("images/vent1_3fwd", 8)

image vent1_4 = Generate_Animation("images/vent1_4", 8)

image vent1_4open = Generate_Animation("images/vent1_4open", 8)

image vent1_5back = Generate_Animation("images/vent1_5back", 8)

image vent1_5fwd = Generate_Animation("images/vent1_5fwd", 8)

image vent1_5 = Generate_Animation("images/vent1_5", 8)

image vent1_5b = Generate_Animation("images/vent1_5b", 8)

image vent1_5c = Generate_Animation("images/vent1_5c", 8)

image vent1_6 = Generate_Animation("images/vent1_6", 8)

image vent1_6back = Generate_Animation("images/vent1_6back", 8)

image vent1_7 = Generate_Animation("images/vent1_7", 8)

image vent2_0back = Generate_Animation("images/vent2_0back", 8)

image vent2_1 = Generate_Animation("images/vent2_1", 8)

image vent2_2 = Generate_Animation("images/vent2_2", 8)

image vent2_3 = Generate_Animation("images/vent2_3", 8)

image vent2_3back = Generate_Animation("images/vent2_3back", 8)

image vent2_4 = Generate_Animation("images/vent2_4", 8)

image vent2_4left = Generate_Animation("images/vent2_4left", 8)

image vent3_0back1 = Generate_Animation("images/vent3_0back1", 8)

image vent3_0back2 = Generate_Animation("images/vent3_0back2", 8)

image vent3_1 = Generate_Animation("images/vent3_1", 8)

image vent3_1back = Generate_Animation("images/vent3_1back", 8)

image vent4_01 = Generate_Animation("images/vent4_0/1", 8)
image vent4_02 = Generate_Animation("images/vent4_0/2", 8)
image vent4_03 = Generate_Animation("images/vent4_0/3", 8)
image vent4left = Generate_Animation("images/vent4_0left", 8)

image vent4_1 = Generate_Animation("images/vent4_1", 8)

image vent4_1back = Generate_Animation("images/vent4_1back", 8)

image vent4_2 = Generate_Animation("images/vent4_2", 8)

image vent4_2left = Generate_Animation("images/vent4_2left", 8)

image vent4_2right = Generate_Animation("images/vent4_2right", 8)

image vent4_3 = Generate_Animation("images/vent4_3", 8)

image vent5_01 = Generate_Animation("images/vent5_0back/1", 8)
image vent5_02 = Generate_Animation("images/vent5_0back/2", 8)

image vent5back = Generate_Animation("images/vent5_0backback", 8)

image vent5_1 = Generate_Animation("images/vent5_1", 8)

image vent5_2 = Generate_Animation("images/vent5_2", 8)

image vent5_2left = Generate_Animation("images/vent5_2left", 8)

image vent5_2right = Generate_Animation("images/vent5_2right", 8)

image vent5_3 = Generate_Animation("images/vent5_3", 8)

image vent5_4 = Generate_Animation("images/vent5_4", 8)

image vent5_5fwd = Generate_Animation("images/vent5_5fwd", 8)

image vent5_5left = Generate_Animation("images/vent5_5left", 8)

image vent5_5right = Generate_Animation("images/vent5_5right", 8)

image vent5_6back = Generate_Animation("images/vent5_6back", 8)

image vent5_7 = Generate_Animation("images/vent5_7", 8)

image vent5_7left = Generate_Animation("images/vent5_7left", 8)

image vent5_7right = Generate_Animation("images/vent5_7right", 8)

image vent5_8 = Generate_Animation("images/vent5_8", 8)

image vent5_9 = Generate_Animation("images/vent5_9", 8)

image vent6_0back = Generate_Animation("images/vent6_0back", 8)

image vent6_1 = Generate_Animation("images/vent6_1", 8)

image vent6_2 = Generate_Animation("images/vent6_2", 8)

image vent7_0 = Generate_Animation("images/vent7_0", 8)

image vent7_1 = Generate_Animation("images/vent7_1", 8)

image vent7_2 = Generate_Animation("images/vent7_2", 8)
image vent7_2back = Generate_Animation("images/vent7_2back", 8)

image vent7_3 = Generate_Animation("images/vent7_3", 8)
image vent7_3back = Generate_Animation("images/vent7_3back", 8)


#------------------ VENTS ANIMATIONS END -------------------------

init -1 python:
    def shot(trans, st, at):
        renpy.play("audio/gunshot.mp3", channel="sound")

    def n2(trans, st, at):
        renpy.play("audio/nest2.mp3", channel="sound")

    def n1(trans, st, at):
        renpy.play("audio/nest1.mp3", channel="sound")

    def strap(trans, st, at):
        renpy.play("audio/strap.mp3", channel="sound")

    def shot(trans, st, at):
        renpy.play("audio/gunshot.mp3", channel="sound")

    def metal1(trans, st, at):
        renpy.play("audio/metalnoise1.mp3", channel="sound")

    def metal2(trans, st, at):
        renpy.play("audio/metalnoise2.mp3", channel="sound")

    def frog1(trans, st, at):
        renpy.play("audio/frog1.mp3", channel="sound")

    def frog2(trans, st, at):
        renpy.play("audio/frog2.mp3", channel="sound")

    def splat2(trans, st, at):
        renpy.play("audio/splat2.mp3", channel="sound")

    def splat1(trans, st, at):
        renpy.play("audio/splat1.mp3", channel="sound")

    def runjump(trans, st, at):
        renpy.play("audio/runjump.mp3", channel="sound")

    def doorhit(trans, st, at):
        renpy.play("audio/metaldoorhit.mp3", channel="sound")

    def fall(trans, st, at):
        renpy.play("audio/fall.ogg", channel="sound")

    def metaldoor(trans, st, at):
        renpy.play("audio/metaldoor.mp3", channel="sound")

    def runhit(trans, st, at):
        renpy.play("audio/runmetalhit.mp3", channel="sound")

    def step1(trans, st, at):
        renpy.play("audio/step1.mp3", channel="sound")

    def step2(trans, st, at):
        renpy.play("audio/step2.mp3", channel="sound")

    def step3(trans, st, at):
        renpy.play("audio/step3.mp3", channel="sound")

    def horrorstart(trans, st, at):
        renpy.play("audio/horrorstart.mp3", channel="sound")

    def krokroar(trans, st, at):
        renpy.play("audio/krokroar.mp3", channel="sound")

    def squish(trans, st, at):
        renpy.play("audio/lewsquish.mp3", channel="sound")

    def slurp2(trans, st, at):
        renpy.play("audio/slurp2.mp3", channel="sound")

    def slurp(trans, st, at):
        renpy.play("audio/slurp.mp3", channel="sound")

    def choke3(trans, st, at):
        renpy.play("audio/choke3.mp3", channel="sound")

    def punch(trans, st, at):
        renpy.play("audio/punch.mp3", channel="sound")

    def cough(trans, st, at):
        renpy.play("audio/cough.mp3", channel="sound")

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

    def slap0(trans, st, at):
        renpy.play("audio/slap.mp3", channel="sound")

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



# image testing = animate_images()

init 2 python :
    test_val = Generate_Animation("images/vent5_7", 8)
    test_val = renpy.easy.displayable('images/bugevent/10/0226.jpg')
    gen_anim = Animation('images/bugevent/10/0226.jpg',.2,'images/bugevent/10/0227.jpg',.2)
    renpy.log(type(gen_anim))
    renpy.log(dir(gen_anim))
    test_val = gen_anim.visit()
    renpy.log(test_val)
    renpy.log(type(test_val))
    renpy.log(test_val[0])
    renpy.log(type(test_val[0]))
    renpy.log(gen_anim.delays)
    test_val = renpy.image("testttt",gen_anim)

# init 3 python :
#     renpy.image("test3",['images/bugevent/10/0226.jpg',.2])

# --------------------- ANIMATION PLAYER ------------------------
init python:
    config.log = 'log.log'
    renpy.image("test_name","images/skills/hacker/1.png")
    def Generate_Animation(directory,fps=24):
        #Give the image a serial number we'll use to reference it
        serial_number = 0
        for i in range(20):
            serial_number += renpy.random.randint(1,9)*pow(10,i)
        serial_number = str(serial_number)

        #Set up some basic containers for our animation generation loop
        animation_list = []
        pause_duration = 1.0/fps
        image_types = ["jpg","png","webp"]

        #Generate the list of images and pauses that will become the animation
        for path in renpy.list_files():
            file = path.split("/").pop()
            file_type = file.lower().split(".").pop()

            if path.startswith(directory) and file_type in image_types:
                animation_list.append(path)
                animation_list.append(pause_duration)

        #Generate and return the actual animation
        renpy.image(serial_number,Animation(*animation_list))
        return serial_number


    def animate_images():
        olist = []
        olist.append(renpy.easy.displayable('images/bugevent/10/0226.jpg'))
        # olist.append(.2)
        olist.append(renpy.easy.displayable('images/bugevent/10/0227.jpg'))
        # olist.append(.2)
        # renpy.log('image type '+ str(type(renpy.easy.displayable('images/bugevent/10/0226.jpg'))))
        return 'images/bugevent/10/0226.jpg'

    # def animate_images():
    #     output_list = []
    #     output_list.append(renpy.display.im.image('images/bugevent/10/0226.jpg'))
    #     output_list.append(.2)
    #     output_list.append(renpy.display.im.image('images/bugevent/10/0227.jpg'))
    #     # output_list.append(.2)
    #     return anim.TransitionAnimation(*output_list)





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
    
    "test dialogue"
    show testttt

    # python:
    #     test_val = Generate_Animation("images/vent5_7", 8)
    #     renpy.log(str(test_val))
    #     renpy.log(type(test_val))
    #     renpy.log(dir(test_val))
    #     renpy.log(test_val.__str__)
    #     renpy.log(test_val.__doc__)
    scene black
    $ sidequest = "..."
    play music "audio/bg/common_bg.mp3" volume 0.3 loop
    "With her commander grounded and her friends too busy, the young quarian Tali'Zorah ventures out into the unknown fringes of Terminus Space, busying herself with chores to find valuable tech and exciting discoveries she can report back to the Migrant Fleet."
    #jump poolcompevent
    scene bg start1
    with dis
    show tali tool at left
    with dis

    tali "Is that a station? No, that's a ship. This far out? Keelah look at the size of that thing. This is Tali'Zorah vas Normandy, do you copy? Unidentified craft, come in."

    show tali shame at left
    with dis
    tali "Mmn. That's no good. No answer, no identification, no reg tags. Looks like it's just drifting in orbit. Scans show a functioning generator at least."
    show tali tool at left
    with dis
    tali "No return ping either. Ugh, who designed that hunk of junk? Even if it wasn't for scrap it looks thrown together. It may be good for salvage but..."
    show tali gunstand at left
    with dis
    tali "Alright. Lets make this quick. Maybe its abandoned, maybe not. Regardless, I can't pass up this opportunity. There might be something in there I can bring back to the Flotilla."

    scene bg start2
    with dis
    "With repeated attempts to hail the vessel failing, Tali gives in to her inquisitive nature and docks her ship on a half-ruined docking tube that works suspiciously too well."
    show tali tool at left
    with dis
    tali "Tethers in place. Pressurization complete. Docking sequence finished. It's... quiet. Dead quiet. I can hear my own breathing. Not spooky at all. For floating scrap its docking subroutines work a little too well. Alright. Time to check the damage."

    scene bg start3
    with dis
    show tali gunstand
    with dis
    tali "The lights seem to work. Filtration systems enabled. How long has this ship been abandoned?"
    show tali tool at left
    with moveinleft
    tali "Alright. Once I've synchronized my omni-tool with the ships local network I should be... There we go. Lets check if there's anything of note on this orbiting moon of scrap."
    menu entrance:
        "Scan for life signs" if flag1:
            $ flag1 = False
            tali "This whole ship just lit up like a colony station! What the hell, why was no one responding...?"
        "Download schematics" if flag2:
            $ flag2 = False
            tali "Corrupted. Great. What did I expect? Seems it responded to my presence and built a local map based on my position. Its not much and it'll do but even this part of the ship is a speck compared to the rest!"
        "Investigate the ship's integrity" if flag3:
            $ flag3 = False
            tali "Critical systems are still operational. Secondary generators are kicking in to compensate for the primary's failure. The engines are functional but disabled. There's... one other ship docked on the other side? What the...?"
        "I should go" if flag1 == False and flag2 == False and flag3 == False:
            show tali gunstand at left
            with dis
            tali "Way to go Tali. You bit off way more than you could chew with this one. Nothing's responding to me here so I'd better leave while they don't know I'm here."
            jump GoNext_1

    jump entrance

    label GoNext_1:
        scene bg start4
        with dis
        play sound "audio/explosion.mp3"
        pause 2
        show tali angry at left
        tali "What? No! My ship!"

    scene bg start5
    with dis
    play sound "audio/creepmany.wav"
    pause 2
    show tali gunstand at left
    play sound "audio/gunready.wav"
    tali "What the hell are those things?! Get back! I'll open fire!"
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

    tali "GET! BACK!!"
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
    "Just seconds after turning the corner, Tali's head rang as the boom of an explosion rocked the corridor and caused the lights across the ship to flicker from the vibrations. Behind her the door sealed shut, locked at the highest level, and left no hopes of going back with a single phrase: DAMAGED HULL."
    scene bg doorcatch1
    show tali guninjured at left
    with dis
    tali "Ngh. Keelah that was close."
    show tali angry at left
    with dis
    tali "Wonderful. Now I need to find a solution for the mess my damned curiosity got me into. This day couldn't get any worse! No use standing around. I'll just open this and... Locked? Like I have time for this!"
    show tali tool at left
    with dis
    tali "Calm down Tali. Its not exactly how you planned today on going but you've gotten out of worse. Lets open this. Afterwards I just need to find the communication center and amplify a distress beacon. There should be patrols... I hope."
    show creep stand at right
    with dis
    play sound "audio/creepone.mp3"
    creature "KUAAAAHHRR!"
    show tali gunstand at left
    tali "What the?! Where did you come from?!"
    show tali gunshoot at left
    tali "You think you stand a chance all alone? Admirable tenacity but I'm afraid I don't have time to play with you."
    pause 2
    play sound "audio/gunready.wav"
    pause .5
    play sound "audio/gunready.wav"
    pause .5
    play sound "audio/gunready.wav"
    pause .5
    play sound "audio/gunready.wav"
    tali "...Awkward. I knew my pistol felt light. An extra clip would've been great if MY SHIP HADN'T BLOWN UP!"
    show tali tool at left
    tali "OKAY. Just stand over there while I open this door, alright? Good. Maybe think about life for a second? I'm sure your two brain cells would finally love to meet eachother. Focus Tali, ignore the creature and focus! If I'm fast enough he'll-"
    show creep horny at right
    play sound "audio/creepone.mp3"
    creature "HAUK! GRRRAAAAHHHHH!"
    scene bg doorcatch2 with hpunch
    play sound "audio/punch.mp3"
    tali "NGH! Get away you filthy animal! Don't lick me there! Oh god, why is your tongue so girthy?!"
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
    tali "Come on you damned sheet of metal, OPEN! He's tearing into my suit!"
    scene bg doorcatch6
    play sound "audio/creepone.mp3"
    "Tali could feel the still air of the station kiss her skin and cradle her large quarian ass. She bit her lip and could feel sweat trickle down her face, but she fought hard to ignore it as she had almost finished unlocking the door. Just then however her body froze stiff as she felt the creatures claws on her fat purle cheeks, and between them the large, bulbous tip of its slimy bestial cock."
    scene bg doorcatch7
    tali "No! Stop! What are you-?!"
    scene bg doorcatch8
    play sound "audio/creepone.mp3"
    creature "Grrraaaaaaaa!"
    scene black
    show newdoor1
    $ renpy.pause ()
    tali "AGGHHHN?!! Stop! Quarians are sensitive to physical stimuli! Mnngh! Gross, it's too thick and slimy! You're splitting my ass apart!"
    scene black
    show newdoor2
    $ renpy.pause ()
    tali "H-Hahhn... Oh ffuucckk. It's so hot and pasty. My insides are on fire..."
    scene black
    show newdoor3
    $ renpy.pause ()
    tali "No! Please! I'm still sensitive! Ah! Oh Keelah! Let me go! Let me go you filthy, brainle- AGHHH!!"
    scene black
    show newdoorcum1
    $ renpy.pause ()
    scene black
    show newdoorcum2
    pause 4

    label test:
        tali "{i}A-Agh. My ass. He fucked my ass like he... meant to breed with me. Keelah, his sperm is so thick. This can't be happening...{/i}"
        scene black
        with Dissolve(5)
        "Exhausted, Tali completely lost the strength and will to resist. She slumped and fell helmet-first to the ground, her body twitching from orgasms she was too humiliated to admit she had. As cum seeped out of her ass she could feel the cool, stale air finalizing her welcome aboard the unknown ship, along with the distant ache of foreign bacteria welcoming itself into her body."
        "Before passing out she heard the familiar beep of her suit auto-enabling antibiotics and deep repair protocols. Before she passed out from the experience altogether, she could feel the beasts hands on her ass again, ready to continue. What kind of hellish ship did she board?"

    unknow "...There's the newcomer. Finally! Krax, Jic, grab her and lets get out of here!"
    scene black with hpunch
    play sound "audio/creepone.mp3"
    creature "KRAGHH!!!"
    unknow "Perfect, more vermin. Kill that thing and lets go!!"
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
    tali "GET the HELL away from me!"
    scene bg med3
    with dis
    show tali gunshoot at left
    play sound "audio/gunready.wav"
    tali "Get back or I'll blast your head clean off your shoulders!"
    scene bg med3
    show tali gunshoot at left
    show serok stand at right
    tali "Who was that? Who are you?! What was that... thing?!! You'd better start talking quick, I am NOT in the mood!"
    show serok smoke at right
    serok "First: Not at all polite to the crew that just saved you. Second: We both know you don't have ammo."
    show tali guninjured
    tali "That... Alright. Ngh. Keelah I can still feel its... What happened??"
    show serok stand at right
    serok "Our sensors aren't worth a damn, but you don't need sensors to know there was an explosion on this hunk of metal. We found you being used up by the local wildlife. Luckily your suit can auto-apply medi-gel and antibiotics. Damned thing can even repair itself. It holds up nicely. Can't say the same for your pride I bet."
    show tali shame at left
    tali "You saw... Right. Lets forget that ever happened."
    show serok reason at right
    serok "We found you through one of the cam feeds. Didn't get to you fast enough but you're alive right? Pity half my crew can't say the same. If they were all female I'm sure I'd at least be able to find them. Hell, I wouldn't even have left the port back in Dakar with a crew like that!"
    show tali doubt at left
    tali "Could you change the topic please? So who are you? What are you doing here?"
    show serok talk at right
    serok "You've got your head in the game. I like that. The names Serok. My men and I are honest merchants. Don't let the Alliance or their claims of 'unlawful salvaging' tell you otherwise."
    show serok reason at right
    serok "My ship was hit hard when I was illegally attacked by some maniac captain with a vendetta against honest folks. Typical Alliance hire. We docked for repairs here. Figured I could trade some goods for some elbow grease or even offer repairs on some trashed systems, but the locals weren't interested in what I was selling. They only wanted food and... well, you know.."
    show serok smoke at right
    tali "Right. Merchants? Sounds to me like you're cut and dry Terminus pirates that smuggle, steal and salvage whatever they can."
    show serok stand at right
    serok "Says who? The quarian? Really? You must be trying to make me laugh. I bet you came here thinking you were gonna walk away with something big and valuable right? Something to take back home?"
    show serok smoke at right
    show tali angry at left
    tali "We don't steal! We only salvage the essentials and never threaten anyone over who can claim a chunk of scrap, you bosh'tet!"
    show serok stand at right
    show tali doubt at left
    serok "Hey suitgirl, you just threatened to blow my head clean off my shoulders, remember?"
    show tali talk at left
    tali "I just... That's besides the point! Talking's getting me nowhere! I need to find the communications station on this ship."
    show serok talk at right
    show tali doubt at left
    serok "You can't. We tried already. Lost most of my crew on the way there. Found only charred metal fragments and scrap bigger than a krogan's well-nourished hump. No way it'll work. You can check for yourself... if you get there."
    show tali shame at left
    show serok smoke at right
    tali "Ugh! There has to be a way off of this thing..."
    show serok talk at right
    serok "You're in luck. There's a ship called 'my junk hauler' that sounds like your ticket off this drifting rock. Problem is the old girl has some trouble walking. My crew's gotten light since being here so fortunate for you I need to make some emergency hires. We might have room for one more if you lend us your expertise."
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
    serok "Need I say more? They live and die like pyjaks but compared to what's on this ship they're the strongest damned things around, assuming you don't charge faster than they can fire. Unfortunately I need brains, not brawn. This environment isn't easy for my technical crew and thanks to some particularly crafty pests, we've lost our chief mechanic."
    tali "So you expect me to help? Oh that's rich. Why would I help you?"
    show serok stand at right
    serok "Because that pain in your ass will only get worse the longer you loiter on a ship full of monsters looking to empty their balls. My ship is our only ticket off this rock. You want a seat? Patch her up."
    show serok reason at right
    serok "I'm being reasonable AND generous. Its my curse as an honest merchant. You quarians are good with ships and stuff, aren't you? I'm lacking there, and you seem to have no bullets for that paperweight you're carrying around. But wouldn't you know it? I happen to have bullets and explosives to spare."
    show serok talk at right
    serok "Fix my ride and you'll have a seat. In the mean time you can look for the parts we need. Trade them in for ammo or explosives and whaddayouknow? We've scratched eachothers backs. I have to recover my losses somehow. What do you say?"
    show serok smoke at right
    show tali talk at left
    menu firstHelp:
        "Seems I don't have much of a choice." :
            tali "Fine. But no tricks! I'll be watching you..."
            show serok stand at right
            serok "Tricks? Maybe on a good day but I've been on this heap of metal too damn long. You do right by me and I'll return the favor, on my honor. But enough talk, lets go see my ship."
            scene black
            play sound "audio/walk.mp3"
            "Hesitantly, Tali follows Serok to the docking bay..."
            pause 2
            jump firstChoiceYES
        "Hell no!" :
            $ firstHelpChoice = False
            $ quest = "Check the comroom"
            tali "As if! I'll take my chances with the communications station over a deal with a pirate!"
            show serok stand
            serok "Oh yeah? Sure. Up to you suitgirl. Assuming you learn your lesson after getting that pretty face of yours covered in creatures breed batter, you know where to find me. I'll be waiting."
            show tali doubt at left
            show serok smoke at right
            serok "Pack it up boys, we're done here. Grab your gear and head back to the ship. Try not to lose whats left of our stuff, ey?"
            scene black
            play sound "audio/walk.mp3"
            "After picking up their equipment Serok and his men left. The batarian didn't seem to at all care for Tali, but his vorcha didn't hesitate to pass a few odd glances over at the defensive, lonesome quarian."
            pause 2
            $ firstHelpChoice = False
            jump firstChoiceNO

    label firstChoiceNO :
        scene bg med3
        show tali tool at left
        tali "Alright, lets see what we have here. Fully operational medical equipment? I could easily reconfigure it for quarian anatomy."
        tali "Looks like I can use the rejuvenation capsules for suit repair and medical assistance. Oh! And these antibiotics are top-shelf! I should be safe in the event of prolonged suit damage!"
        show tali shame at left
        tali "Did they have quarians here? Huh. Very... strange. This is some very advanced inventory for a drifting hunk of junk. What was this ship used for?"
        show tali doubt at left
        tali "No use wondering. I can relax here a little but I need to head over to communications once I'm well and ready."
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
        serok "Well, yeah, you're right. But it's our escape off this hellhole. Remember what's important."
        show tali talk at left
        tali "Just tell your thugs not to get in my way."
        show serok reason at right
        show tali doubt at left
        serok "Deal. Welcome to the crew! No unions, no steady pay, but Serok will treat you right. Now go and see whats keeping this bird grounded would ya?"
        show serok talk at right
        serok "Oh, and keep an eye out for Jesora. My second officer. She's somewhere on my bird. Asari, you can't miss her. I'd hoped she was here to introduce you, but I guess you'll meet her on your own. Good luck."
        scene black
        with dis
        play sound "audio/walk.mp3"
        pause 2
        scene bg shipinside
        show tali tool at left
        with dis
        tali "Lets see... thermal stabilizers damaged. Heating panels fried. Engines uncalibrated. Keelah, if they take off on full power this ship will become a spaceworthy oven in an instant!"
        show tali shame at left
        tali "I'll have to find parts or jury rig a solution. Maybe in the engine room? The cargo bay would be best for scrap..."
        show tali tool at left
        tali "Navigations are fried as well. I should be able to fix the computer with spare parts."
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
        tali "...What the hell?"
        play sound "audio/lewdclaps.mp3"
        scene bg shipscene1
        "Mmmmph! Fuck me harder you waste-scrounging vorcha bastards!"
        scene bg shipscene2
        play sound "audio/funmoan.mp3"
        pause 1
        play sound "audio/lewdclaps.mp3"
        pause 1
        scene bg shipscene0
        tali "I... think I found Serok's second officer."
        scene bg shipscene3
        jesora "Ughhmmmmmpppppphh..."
        scene bg shipscene4
        "Tali felt obliged to leave, but the sight of the officer being fucked by her subordinates caused her heart to race and her mind to wander. Before she knew it she began to touch herself, breathing misty breaths of hot air in her helmet as her fingers rubbed her sensitive nerves."
        tali "Keelah that's so... filthy. I-I hope they don't notice me..."
        scene bg shipscenebg
        show asari_anim1
        $ renpy.pause ()
        scene bg shipscene5
        play sound "audio/lewdsplat.mp3"
        pause 4
        scene bg shipscene6
        play sound "audio/lewsquish.mp3"
        tali "They must've been really backed up for so long. There's so much cum, it's dripping out of her ass. And she has a dick? Asari can have those? Keelah, it's throbbing so much. It's painting the deck white..."
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
        tali "Serok? Well, uh... I found the issue. Or issues. It won't be an easy fix but..."
        show jesora doubt behind serok
        with dis
        show serok talk at right
        serok "Jesora! Finally. You took your sweet time huh? What exactly were you up to? Scratch that, doesn't matter. Let me introduce you to our new chief engineer. This quarian will help us to repair the ship."
        show serok stand at right
        serok "Suitgirl, this is Jesora - former asari commando and my latest second officer. She'll help you with everything that goes bang and boom. Have fun ladies. Now then, I need a drink."
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
        serok "Had enough fun with the locals?"
        tali "Will you stop... look, lets just get this over with."
        show serok stand at right
        show tali doubt at left
        serok "Hmmph. Well while you were running around wasting time, my second officer Jesora diagnosed my ships issues. You can check the results and find what we'll need."
        show serok talk at right
        serok "Here, take it."
        show tali tool at left
        show serok smoke at right
        tali "Lets see... Thermal stabilizers damaged. Heating panels fried. Engines uncalibrated. Keelah, if they take off on full power this ship will become a spaceworthy oven in an instant!"
        tali "I'll have to find parts or jury rig a solution. Maybe in the engine room? The cargo bay would be best for scrap..."
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
        tali "Nice to meet you. My name is Tali'Zorah. My ship was sabotaged and now I'm stuck here."
        jump jesoraFirstTalk
    label jesoraFirstTalk2:
        show tali talk at left
        with dis
        show jesora doubt at right
        with dis
        tali "Uh. Hello again."
        show jesora stand at right
        jesora "Again? What do you mean by that?"
        show tali shame at left
        tali "No, I mean... I have some asari friends and... well, I confused you for someone different who... looks like you..."
        tali "Just forget it, ok?"
        jump jesoraFirstTalk
    label jesoraFirstTalk:
        show tali doubt at left
        show jesora stand at right
        jesora "I see. We're all on the same boat here. You help us, we help you."
        show jesora talk at right
        jesora "We can arrange an exchange here. Bring me any tech parts you find and I'll exchange it for its value worth in ammo and explosives."
        show tali tool at left
        tali "Wait, I have credits. I could just pay you. Do you have any Shotguns or SMGs? I could really use the extra firepower."
        show jesora stand at right
        jesora "Look around girl. Does it really look like we need money right now? We need components, not credits. You bring tech, you get ammo."
        show tali angry at left
        tali "Why do YOU need tech if Serok is sending ME to fix everything?!"
        jesora "Our ship barely escaped a fight with an alliance patrol. We have a myriad of issues all over the hull. Those issues can be fixed with the parts you bring us. Is that clear enough for you to understand?"
        show jesora doubt at right
        show tali doubt at left
        jesora "We can't handle critical system issues. You can. That's the only reason you're here and Serok didn't OK you being some chained up crew relief in the hold while we sort this mess out, got it?"
        show tali angry at left
        tali "That's... Just give me some guns! There's plenty of beasts on this ship! How do you expect me to defend myself?!"
        show tali doubt at left
        show jesora stand at right
        jesora "You HAVE a gun, right? We need ours to defend whats left of our ship. We don't want or need to run around shooting everyone. Just stay silent, hide, and shoot if necessary. Preferably discreetly."
        show jesora think at right
        jesora "What we CAN do for you is dismount one of our older canons from the ship and rig it up as makeshift sentry turret to protect the medical bay where you'll be residing. Who knows, maybe we'll need that bay too if it really hits the shitter."
        show tali talk at left
        tali "That's... ugh. Well it's something. At least I can rest easy..."
        show jesora stand at right
        jesora "You're welcome. So, you know what the issues with the ship are or what?"
        tali "Yes. There are some other issues but the important ones are your thermal stabilizers and the navigation system."
        jesora "Navigation huh? Good. Knowing the specifics makes searching less inconvenient. Seroks vorcha haven't found anything, but its hard for them to bring back something that isn't obvious or shiny."
        jesora "Take this."
        scene black
        show doorexp:
            xalign 1.2
            yalign 0.5
        show doorexp with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "Tali received a door breaching charge"
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
        jesora "Stop fiddling with the switches you idiot. Just make sure it's ON. Yes, like that. Now let me check."
        scene bg turret2
        with dis
        jesora "Serok? Its done. We'll be back soon. All quiet? Affirmitive. Alright, got it."
        show bg turret3
        with dis
        show tali doubt at left
        show jesora stand at right
        with dis
        jesora "Alright girl, we're done here. The turret has enough charge to resist a small siege. It's an older model so it shouldn't technically run out of ammo. Can't say the same if anything huge or bulky comes along that can absorb all that punch and cause it to overheat. I'll ask the boys to patrol the halls from time to time, just in case."
        show tali talk at left
        tali "Very generous coming from a pirate crew. Thank you. I'll rest for a moment before getting to work."
        jesora "Take your time. If you have any questions, Serok and I will be in the docking bay. But the sooner you find what we need, the faster we can get off this hellhole."
        show jesora talk at right
        jesora "Here's some ammo, on the house. Don't use it all on one trip."
        scene black
        show clips:
            xalign 1.2
            yalign 0.5
        show clips with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "Received 10 thermal clips."
        $ ammo += 10
        show clips with move:
            xalign -0.2
            yalign 0.5
        show bg turret3
        show tali doubt at left
        show jesora talk at right
        jesora "Careful now. And good luck."
        $ bay2 = True
        $ bugsact = True
        $ bugfirst = False
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
        $ lovedart = False
        $ fuckstage = 1
        $ sexstage = 1
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
        tali "I need to be more careful next time..."
        jump define_loot

    label meddoubleenc:
        $ twoWinFirst = False
        $ twoCount = 0
        scene bg med3
        show tali shame at left
        tali "Ugh. Looks like I slept on my neck again..."
        play sound "audio/heavyshots.mp3"
        pause 1
        play sound "audio/creepone.mp3"
        show tali doubt at left
        tali "Oh? Sounds like some more beasts tried their luck. Too bad. Guess I'll see if they were carrying anything useful..."
        scene bg meddp3
        with dis
        play sound "audio/gorillaroar.wav"
        stop music
        play music "audio/bg/fight_bg.mp3" volume 0.6 loop
        tali "What the hell?! How did you two get here?!"
        scene bg meddp4
        show monk stand at right
        show tali gunstand at left
        play sound "audio/creepone.mp3"
        tali "Don't even think about it! Go back the way you came and no one gets hurt, got it?"
        scene bg med3
        show tali gunshoot at left
        show monk stand at right
        with dis
        tali "I said go away! Stay where you are! This is your last warning!"
        $ enemyID = 31
        jump sliderBoss

    label meddp1Bad:
        play sound "audio/fall.ogg"
        show tali fallmask at left
        play sound "audio/glass.mp3"
        "Tali stumbles and falls, her gun sliding towards the duo of beasts."
        tali "Stay back! I'm warning you!"
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        scene bg meddp5 with hpunch
        play sound "audio/creepone.mp3"
        tali "Again. I've lost... again. This time they'll..."
        scene bg black
        show meddp1_loop1
        $ renpy.pause ()
        scene bg meddp1
        play sound "audio/creepone.mp3"
        tali "No, please, it's too thick! I barely held on last time. If you fuck me with that I don't think I can-"
        scene bg meddp2 with hpunch
        play sound "audio/punch.mp3"
        tali "...Please."
        $ renpy.pause ()
        scene bg black
        show meddp1_trans
        $ renpy.pause ()
        show meddp1_loop3
        $ renpy.pause ()
        scene bg black
        show meddp1_loop2
        $ renpy.pause ()
        scene bg black
        show meddp1_loop3alt
        $ renpy.pause ()
        scene bg black
        show meddp1_cum1
        $ renpy.pause ()
        scene bg meddp6
        play sound "audio/cumshot1.ogg"
        pause 1
        scene bg black
        show meddp1_cum3
        $ renpy.pause ()
        play sound "audio/lewsquish.mp3"
        scene bg meddp
        pause 3
        scene bg black
        show meddp1_cum2
        $ renpy.pause ()
        jump BadEnd

    label meddp1Good:
        scene bg meddp7 with hpunch
        play sound "audio/creepone.mp3"
        pause 1
        scene bg meddp8 with hpunch
        play sound "audio/fleshhit1.mp3"
        pause 2
        scene bg meddp9
        tali "Shut up for good, you boshtet!"
        scene bg meddp11
        play sound "audio/creepmany.wav"
        pause 2
        scene bg meddp10
        play sound "audio/gunready.wav"
        tali "Always thought you were moving too fast. Time to change that."
        scene bg meddp12
        play sound "audio/gunshot.mp3"
        pause 1
        scene bg meddp13
        play sound "audio/gunshot.mp3"
        pause 1
        play sound "audio/fleshhit.mp3"
        pause 1
        scene bg meddp14 with hpunch
        play sound "audio/fall.ogg"
        pause 1
        play sound "audio/creepone.mp3"
        pause 1
        scene bg meddp15
        tali "Sorry boys, our time together was very fun."
        play sound "audio/equip.ogg"
        scene bg meddp16
        tali "But my parents didn't like you."
        scene bg meddp17 with hpunch
        play sound "audio/fleshhit1.mp3"
        pause 2
        scene black
        with dis
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        jump medaftermess

    label medvarrenenc:
        $ varHunt = False
        $ varCount = 0
        play sound "audio/crushing.mp3"
        pause 1
        show bg medvarrens1
        with dis
        tali "Mmmm? Huh? What was that noise?"
        scene bg medvarrens2
        play sound "audio/roar.mp3"
        tali "What the hell?! How do you get here?!"
        scene bg med3
        show tali gunshoot at left
        show red2 stand at right
        play sound "audio/equip.ogg"
        tali "Damnit! This'll teach you to barge into my home!"
        $ enemyID = 21
        jump sliderBoss

    label redmedbad:
        scene black
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        play sound "audio/creepone.mp3"
        pause 2
        play sound "audio/tier.mp3"
        pause 2
        scene black
        show medvar1_loop1
        $ renpy.pause ()
        scene bg medvarrens4
        tali "I'm sorry for thinking I could fight back! Keelah, your thick knot is splitting my tight ass wide!"
        scene black
        show medvar1_loop2
        $ renpy.pause ()
        scene black
        show medvar1_trans
        pause 2
        show bg medvarrens5
        tali "M-Mmph! Naughty stray! I caught you... Now I won't let you go until I've emptied your balls!"
        scene black
        show medvar1_loop3
        $ renpy.pause ()
        scene black
        show medvar1_cum1
        $ renpy.pause ()
        scene bg medvarrens6
        tali "K-Knot me harder...!"
        scene black
        show medvar1_loop4
        $ renpy.pause ()
        scene black
        show medvar1_cum2
        $ renpy.pause ()
        scene bg medvarrens7
        tali "Yes! Cream my ass! Push your cock... in my stomach..."
        scene bg medvarrens3
        with dis
        play sound "audio/lewsquish.mp3"
        pause 3
        jump BadEnd

    label redmedgood:
        scene bg medvarrens8
        play sound "audio/gunshot.mp3"
        pause 2
        scene bg medvarrens9 with vpunch
        play sound "audio/fleshhit1.mp3"
        pause 2
        scene bg medvarrens10
        play sound "audio/creepmany.wav"
        pause 1
        scene bg medvarrens11
        play sound "audio/equip.ogg"
        pause 1
        scene bg medvarrens12 with vpunch
        play sound "audio/fall.ogg"
        pause 1
        scene bg medvarrens13 with vpunch
        play sound "audio/fall.ogg"
        tali "You stupid beast, let go of me!"
        play sound "audio/dogroar.mp3"
        pause 1
        scene bg medvarrens14
        tali "I said... LET... ME... GO!"
        show omnimed
        play sound "audio/omnicharge.mp3"
        pause 2
        scene bg medvarrens15 with vpunch
        play sound "audio/fleshhit1.mp3"
        pause 1
        play sound "audio/beastdying.mp3"
        pause 2
        scene black
        with dis
        pause 2
        scene bg med4
        show tali guninjured at right
        tali "Ugh... That was a close one..."
        $ reddead = True
        jump medaftermess





    label medaftermess:
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        scene bg med4
        show tali tool at left
        play sound "audio/message.mp3"
        tali "Serok, Jesora, anyone copy?"
        serok "What is it?"
        tali "I need some assistance with clean up here, can you give me a hand?"
        serok "Sigh. Lets see the damage."
        scene bg med3
        with dis
        show tali doubt at left
        show serok stand at right
        serok "Well holy shit. That's a mess, girl. You didn't give them a chance, did you?"
        show serok talk at right
        serok "With all those gadgets and skills, you could really help out my crew. Hell, I'd even make you an officer. Think on it."
        show serok smoke at right
        show tali talk at left
        tali "Aha, maybe later. Just after i leave this ship."
        show tali angry at left
        show serok stand at right
        tali "And how the hell did this even happen in the first place? Your damned turret isn't working! These creeps came in here like it was their home!"
        show tali doubt at left
        show serok reason at right
        serok "Of course it's not working. There damn thing's fried."
        show tali angry at left
        show serok smoke at right
        tali "What?! I thought Jesora was taking care of it!"
        show serok stand at right
        serok "Well I guess she didn't take into account just how popular that big ass of yours would be with the locals..."
        show tali doubt at left
        tali "...You just can't stop thinking about it, can you?"
        show serok reason at right
        serok "Go ahead. Turn around in disgust. I haven't gotten a good look at it since I've been here, heh."
        tali "Ugh..."
        show serok reason at right
        serok "Alright back to business. My boys have been fixing it since we got here so its core should be relatively fresh and new now. It's the best we can do for a turret that old. But this is the last time we repair it. Maybe you can run some maintenance on it or check for alternatives when you have the time."
        show serok smoke at right
        show tali angry at left
        tali "Just perfect. And what should I do now?"
        show serok talk at right
        serok "Scavenge and loot, as always."
        show serok think at right
        show tali doubt at left
        serok "Listen I'm really sorry for this. I guess we can find another way, but I need some time to figure out what the hell's going on. I hate thinking long-term but with how poor it's going I might need to start actually giving a fuck about fortifications and scheduled patrols. Fucking wonderful."
        serok "For now just be careful. Keep that turret running or you're gonna have a lot of problems."
        show serok stand at right
        serok "Ah, and good news. Jesora finally has a plan. You can go and talk with her about that, all this talking's making me thirsty. See you later."
        hide serok stand
        with dis
        play sound "audio/walk.mp3"
        pause 1
        show tali shame at left
        tali "Great. Another headache for me to deal with."
        $ quest = "Talk with Jesora."
        $ poolQuest = True
        jump MedBayUsual

    label runrandom:
        $ random = renpy.random.randint(1, 100)
        if random > 0 and random < 26:
            $ run1 = True
        elif random > 20 and random < 51:
            $ run2 = True
        elif random > 50 and random < 76:
            $ run3 = True
        elif random > 75 and random < 101:
            $ run4 = True
        jump MedBayUsual




    label runstart:
        $ run1 = False
        $ run2 = False
        $ run3 = False
        $ run4 = False
        stop music
        scene black
        show run_start
        pause 5.7
        scene black
        show run_startalt
        pause 1.0
        play music "audio/bg/run_bg.mp3" volume 0.3 loop
        scene black
        show run_startalt1
        pause 2.3
        "Crossroads ahead! Which way do you run?"
        menu run1:
            "Run left.":
                jump runleft1
            "Run right.":
                jump runright1

    label runleft1:
        scene black
        show run_left1
        pause 2.5
        tali "There's a security door ahead! I can try to close it behind me quickly!"
        menu run2:
            "Try to close the door.":
                jump runleft1door
            "Keep running.":
                jump runleft1catch

    label runleft1door:
        scene black
        show run_left_door
        pause 2
        jump run_escape

    label runleft1catch:
        scene black
        show run_left_catch
        pause 2
        jump run_catch

    label runright1:
        scene black
        show run_right1
        pause 2.0
        tali "Dammit! Another crossroad!"
        menu run3:
            "Run left.":
                jump runright1left
            "Run right.":
                jump runright1right

    label runright1left:
        scene black
        show run_right1_left
        pause 1.8
        menu run4:
            "Jump left.":
                jump runright1leftrun
            "Jump right.":
                jump runright1leftcatch

    label runright1leftrun:
        scene black
        show run_right1_left_run
        pause 2.3
        jump run_escape

    label runright1leftcatch:
        scene black
        show run_right1_left_catch
        pause 1
        jump run_catch

    label runright1right:
        scene black
        show run_right1_right
        pause 6
        tali "No, no, no! Please... stay back!"
        jump run_catch

    label run_catch:
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        scene bg krok1 with hpunch
        play sound "audio/punch.mp3"
        tali "Ngh! You filthy beast! L-Let me go!"
        play sound "audio/creepone.mp3"
        pause 1
        scene black
        show krok1
        $ renpy.pause ()
        scene bg krok1 with hpunch
        play sound "audio/tier.mp3"
        pause 1
        scene black
        show krok2
        $ renpy.pause ()
        scene bg krok2
        tali "Hnngh! H-His fat fingers are... making me so wet! I need to do something before it gets worse..!"
        menu catchmenu:
            "Submit.":
                scene black
                show krok5
                $ renpy.pause ()
                scene bg krok3 with hpunch
                play sound "audio/punch.mp3"
                pause 1
                tali "NGH?!! K-Keelah! That... huge ribbed cock... I can feel every inch of it inside... rubbing my insides!"
                scene black
                show krok6
                $ renpy.pause ()
                tali "Ah... I-I'm going to... c-cum...!"
                scene black
                show krok14
                pause 3.5
                tali "Ah... H-Haghn. My pussy... S-So much cum. Please... leave me alone now..."
                jump medbayafterdefeat
            "Try to run.":
                scene bg krok4 with hpunch
                play sound "audio/punch.mp3"
                pause 1
                play sound "audio/creepone.mp3"
                tali "...S-Shit. I fucked up big time. I hope he isn't too angry..."
                scene black
                show krok9
                pause 3.5
                tali "Ngh... K-Keelah, I'm so wet..."
                scene black
                show krok9alt
                pause 2
                tali "Wha... do you think... no, no, don't do that. Not there! Please..."
                scene black
                show krok10
                $ renpy.pause ()
                tali "Keelah... he's preparing my ass... he wants to punish my ass with his thick, massive cock..."
                scene bg krok5 with hpunch
                play sound "audio/creepone.mp3"
                tali "No, please! I-It's too big! What are you doing...?!"
                scene black
                show krok11
                pause 5
                tali "H-HAGHHGNGH?! Keelah! He's tearing me apart!"
                scene black
                show krok12
                $ renpy.pause ()
                tali "Too big! My mind's going blank! You're stretching my guts! H-HAGHHN?! I can feel you... rubbing my pussy from the inside! My pussy's leaking so much!"
                scene black
                show krok13
                $ renpy.pause ()
                tali "I... I can't feel my legs... his cum's in my stomach... I can almost... taste it in my mouth."
                jump medbayafterdefeat
            "Use dart." if lewd > 30:
                scene bg krok6
                tali "Hey, big fella, look what I have here..."
                scene bg krok7 with hpunch
                play sound "audio/dart.mp3"
                pause 1
                scene bg krok8 with hpunch
                play sound "audio/fall.ogg"
                tali "Hmph. Didn't expect that, did you?"
                play sound "audio/roar.mp3"
                pause 1
                scene bg krok9
                tali "Oh, and what do we have here? Such a huge, fat cock you have. And those balls must be so full of your filthy, beastly spunk. Lets see if I can help you with it."
                scene black
                show krok3
                $ renpy.pause ()
                tali "Mmmh. Your cock's making me so wet. Such a massive, ribbed cock. My tight pussy is hungry for it..."
                scene black
                show krok4
                pause 1.5
                tali "Oh Keelah, yes! That tranquilizer had better work long enough for me to enjoy this...!"
                scene black
                show krok7
                $ renpy.pause ()
                scene black
                show krok8
                $ renpy.pause ()
                tali "Yes! Oh FUCK! So good! Keelah, I'm cumming!"
                scene black
                show krok15
                $ renpy.pause ()
                jump medbayafterdefeat




    label run_escape:
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        scene bg map
        show tali guninjured at left
        with dis
        tali "Oh Keelah... That was close... I need to catch my breath."
        jump map
















    label rest:
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
            if varHunt:
                $ varCount += 1
            if varCount > 4:
                jump medvarrenenc
            if twoWinFirst:
                $ twoCount += 1
            if twoCount > 2:
                jump meddoubleenc
            else:
                jump secureDoorRandom

        else:
            if jesora1 == False:
                if partsQuest and days > 12:
                    if whDoor == False and barracksDoor == False:
                        $ jesora1 = True
                        jump hackQuest

        jump define_loot

    label medevent1:
        if twoHount:
            jump doubleEnc
        else:
            jump MedBayUsual



    label MedBayUsual:
        hide screen medStats
        scene bg med4
        show tali tool at left
        menu MedBay:
            "Check status" :
                if run_ok:
                    $ quest = "Search for answers in pool location."
                    if ventsopen == False:
                        $ ventquest = True
                scene bg medscreen
                show screen medStats
                if firstTimeScan:
                    jump statusCheck
                else:
                    "Full scan complete. Results on screen."
            "Rest" if firstTimeScan == False:
                #if poolFirst == False:
                    #$ scanQuest = True
                if bugquest:
                    $ bugcount += 1
                if act3:
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
                    if varHunt:
                        $ varCount += 1
                    if varCount > 4:
                        jump medvarrenenc
                    if twoWinFirst:
                        $ twoCount += 1
                    if twoCount > 2:
                        jump meddoubleenc
                    else:
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
                tali "Mmm. I needed this."
                scene bg shower2
                with dis
                if bugsact:
                    jump showerEvent1
                elif bugcount > 2 and bugquest:
                    jump showerEvent2
                "........"
            "Close the hatch" if bugquest and parts > 29:
                $ parts -= 30
                $ bugquest = False
                scene bg vent2
                tali "Time to solve this."
                scene black
                show ventclose1
                pause 1
                scene bg med3
                show tali doubt at left
                tali "Great, one problem less."
                $ sidequest = "..."
                jump MedBayUsual

            "Deactivate security doors." if act3 and secureDoors:
                $ secureDoors = False
            "Activate security doors" if act3 and secureDoors == False:
                $ secureDoors = True
            #"Activate runaway event":
                #$ run_ok = True
                #"Try to check the hallway now."
            #"Make Tali super lewd.":
                #$ lewd = 50
                #"Naughty, naughty..."
            "Explore the ship" if firstTimeScan == False:
                if firstMap:
                    jump maptutorial
                else:
                    jump map
        jump MedBayUsual


    label doubleEnc:
        $ twoHount = False
        $ twoWinFirst = True
        scene bg g1
        tali "Ugh. I can't wait to take a shower... What the...?"
        scene bg g2 with hpunch
        play sound "audio/punch.mp3"
        tali "Keelah, that's the monkey-beast from the cells!"
        play sound "audio/roar.mp3"
        tali "He's pretty close to my hideout. If they find the medbay it'll be impossible for me to stay safe! What am I gonna do now?"
        menu doublechoice:
            "Attack.":
                show bg g3
                play sound "audio/creepone.mp3"
                tali "I'll solve the problem before it gets worse! Remember me you freak?!"
                tali "Hah! Looks like your friend left you all alone! Just like an animal, he knows when he doesn't stand a chance!"
                scene bg g4
                play sound "audio/creepmany.wav"
                pause 1
                scene bg g5
                tali "Oh, come on Tali, you should have expect this."
                scene bg g8
                $ enemyID = 30
                jump sliderBoss
            "I SHOULD GO.":
                "I'm not ready for a fight. I need to get away while they don't notice me."
                scene black
                play sound "audio/run.ogg"
                pause 2
                jump map

    label double_event1:
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        scene black
        $ lewd += 1
        play sound "audio/creepone.mp3"
        pause 2
        play sound "audio/tier.mp3"
        pause 2
        scene bg g9
        tali "Ugh, your breath smells so disgusting...!"
        scene bg g7
        show double_loop1
        $ renpy.pause ()
        scene bg g6
        play sound "audio/gorillaroar.wav"
        tali "No, one is more than enough! Can you just go back to your damn cage!?"
        scene bg g7
        show double_trans1
        pause 4
        tali "It hurts, it hurts! No, please stop...!"
        scene bg g7
        show double_trans2
        tali "A-Ah... it's even bigger than I thought..."
        scene bg g7
        show double_loop2
        $ renpy.pause ()
        scene bg g7
        show double_cum
        $ renpy.pause ()
        scene bg g8
        show tali fin1 at left
        with dis
        tali "At least they let me go... N-Ngh, the medbay must be close..."
        jump medbayafterdefeat


    label jesoraCall:
        scene bg med3
        show tali tool at left
        with dis
        play sound "audio/message.mp3"
        tali "I got a message but there's a lot of interference."
        play sound "audio/noise.ogg"
        jesora ".............................."
        tali "I need to try and isolate the signal."
        play sound "audio/noise.ogg"
        pause 2
        jesora "... hear me?.... hello?"
        tali "Its Jesora!"
        jesora "...help... the hallway near the communication..."
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
        tali "Jesora? You fixed communications! Now we can call for help!"
        jesora "We're not that lucky, quarian. We found a shortwave transmitter and the boys kicked it hard enough to make it work. Come meet me in the hangar bay, we need to talk."
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
        jesora "First take this, this is a module for your omni-tool with decrypting protocols. It will let you hack almost anything you want."
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
        tali "You can't be serious? Even if there was something left, that sector was depressurized after the explosion."
        show tali doubt at left
        show jesora talk at right
        jesora "We thought so too, but the ships automated repair seemed to fix enough to patch up the damage. I scanned the area and sure enough it's safe."
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
        serok "Glad to see you in one piece, girl. That's great but we have a bit of a problem."
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
        serok "Without my crew this ship will eat us alive. I'm sure you can understand that."
        show tali talk at left
        show serok smoke at right
        tali "Ugh. What about supplies?"
        show serok talk at right
        serok "Hmph. Here, take it. Use it wisely. I'll use the rest to protect whats left of my boys. What hasn't been gnawed off them anyway."
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
        "Tali will encounter security doors at random in most directions and will stay there until she hacks or destoys them."
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
        $ quest = "Wait for Serok call."
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
        tali "Hold on, I am not a part of your team. We have an arrangement, got it?"
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
        serok "Not just a nice ass, are you? Well when we first arrived we figured we could get out of this rich and quick so we headed over to the bridge. We found some very weird shit on the way there."
        show serok talk at right
        serok "We tried to find a drone or something to fix up the ship. Instead we found rooms and labs full of those creatures, swarming and reckless."
        show serok think at right
        serok "It was a massacre. I lost a lot of guys. Too many. The scrap we picked up along the way isn't worth that kind of loss. To boot, I got stabbed in the back by a couple of ingrates."
        serok "Gral, my original second officer. He took half my crew and left for the other front of the ship. Something about getting us all killed over a bad haul. It'd be a great haul if he just listened. Personally I think he just wanted an excuse. He seemed the union type."
        show serok talk at right
        serok "Let them die, what do I care? But as a last laugh he took the thermal stabilizers. What an asshole."
        show serok smoke at right
        show tali talk at left
        tali "Couldn't you just apologize? We all make mistakes."
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
        serok "Jesora and I will figure out how to go from here. We'll hatch a plan and get back to you. Get some rest, you'll need it. We'll call you later."
        serok "And take this. Jesora found it on her last patrol."
        scene black
        show keycard1:
            xalign 1.2
            yalign 0.5
        show keycard1 with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "Tali received a keycard."
        show keycard1 with move:
            xalign -0.2
            yalign 0.5
        scene bg hangar
        show serok stand at right
        show tali doubt at left
        serok "I got no clue what this keycard opens, but I'm sure you will. Have fun."
        scene black
        play sound "audio/walk.mp3"
        "Tali returns to the medbay"
        scene bg med3
        show tali tool at left
        $ days = 0
        jump define_loot


    label statusCheck:
        "Here you can check on Tali's status and her inventory. Most of these stats will be shown on the upper-left corner of the map screen."
        "Be wary of infection. Infection will rise with each consecutive defeat up to a maximum of '3'. Once Tali reaches max Infection, she will automatically return to the medbay for healing and a day will pass."
        "The more Tali loses, the higher her lewd level becomes. Additional events and dialogue options will unlock the more corrupt Tali's mind becomes."
        "Use ammo and grenades to defeat your enemies! Door explosives will clear the way through blocked areas, but beware! The noise will alarm the locals and increase encounter chance. Alarm level can not be reduced for now."
        "You can help Tali refresh her stamina and infection levels by choosing to rest at the Medical Bay. This will also refresh both events and loot in rooms you've visited."
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
        text "Current quests:" xpos 0.55 ypos 0.2
        text "[quest]" xpos 0.50 ypos 0.3
        text "[sidequest]" xpos 0.50 ypos 0.4

    label comroomtutorial:
        scene bg comroom
        show tali tool at left
        with dis
        tali "No luck. The terminals are completely trashed. Serok was right, there's no way I can use these."
        show tali shame at left
        tali "Great. Well I'm already here. May as well check for anything useful."
        show image "images/map/backbutton_idle.png" at right
        show tali back at left
        with dis
        "Every time Tali enters a room, you can search for clickable objects around. Loot and misc items are scattered. You can go back to the map with the bottom-right arrow button."
        scene bg comtutorial1
        show tali back at left
        "Loot is randomly generated and may look different depending on the room. It could even be in a different spot than the last time you've visited! Loot won't respawn if you've already visited the room on the same day. Rest at the medbay ro reroll what you find. Keep those eyes open!"
        scene bg comtutorial2
        show tali back at left
        "This is how it looks when you hover the cursor over such an object. Inside you can find valuable items like ammo or quest items like tech parts. These will be added to your inventory."
        "Common loot is random. Some events may also be triggered depending on Tali's Lewd Level."
        $ firstTimeRoom = False
        jump comroom

    label comroom:
        if run4:
            jump runstart
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
        if random > 0 and random < 40:
            $ random = renpy.random.randint(2, 6)
            show clips:
                xalign 1.2
                yalign 0.5
            show clips with move:
                xalign 0.5
                yalign 0.5
            play sound "audio/gunready.wav"
            "[random] thermal clips found"
            $ ammo += random
            show clips with move:
                xalign -0.2
                yalign 0.5
        elif random > 39 and random < 95:
            $ random = renpy.random.randint(1, 5)
            show parts:
                xalign 1.2
                yalign 0.5
            show parts with move:
                xalign 0.5
                yalign 0.5
            play sound "audio/gunready.wav"
            "[random] tech parts found"
            $ parts += random
            show parts with move:
                xalign -0.2
                yalign 0.5
        elif random > 94 and random < 101:
            show gren:
                xalign 1.2
                yalign 0.5
            show gren with move:
                xalign 0.5
                yalign 0.5
            play sound "audio/gunready.wav"
            "Grenade found"
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
        elif roomID == 11:
            jump pool


    label maptutorial:
        $ firstMap = False
        scene bg map tutorial
        "This is the general map of the ship you need to explore. In the upper-left corner you can see a list of Tali's current stats, as well as location tiles you can select across the ship."
        "During exploration there may be new locations you can uncover. Use breach charges to open security doors or try to hack them with your omni-tool once you have the tool."
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

        showif scanOK:
            imagebutton:
                idle "images/map/scan/scan_idle.png"
                hover "images/map/scan/scan_hover.png"
                focus_mask True
                xpos 0.017
                ypos 0.43
                action Jump("scanmap")

        showif pool:
            imagebutton:
                idle "images/map/pool_idle.png"
                hover "images/map/pool_hover.png"
                hovered Notify("    Pool")
                focus_mask True
                action Jump("pool_enter")

        showif poolnew:
            imagebutton:
                idle "images/map/pool_idle.png"
                hover "images/map/pool_hover.png"
                hovered Notify("    Pool")
                focus_mask True
                action [SetVariable("roomID", 11), Jump ("encounter_chance")]

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
            action Jump ("medevent1")
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

    label pool_enter:
        if poolFirst:
            $ scanQuest = True
            $ poolFirst = False
            $ quest = "Check pool later."
            scene bg pool
            show tali doubt at left
            tali "Would you look at that? They even have a pool. I guess no one'll miss summer on this ship after all."
            show tali tool at left
            play sound "audio/message.mp3"
            jesora "Hey, suitgirl. Did you find something?"
            tali "Your scanner worked. I found a room after making a few odd turns. This place looks like some experimental pool. Give me minute, I'll look closer."
            scene bg pool1
            with dis
            tali "Good news. There's a grate over the water. If anything's in there, it's trapped and locked tight."
            jesora "See anything or anyone? Any traces of our mystery bitch?"
            tali "No, but I guess this pool is caged for a reason. I don't want to know what could be hiding under there."
            jesora "Forget about the pool. Just search for that piece of shit."
            scene bg pool
            show tali doubt at left
            tali "Maybe I need to check this later?"
        elif scanQuest:
            $ pool = False
            $ poolnew = True
            $ scanQuest = False
            jump phantomcut
        else:
            $ random = renpy.random.randint(1, 2)
            if random == 1:
                $ run_ok = True
            if run_ok:
                $ run_ok = False
                jump runstart
        scene bg pool
        show tali back at left
        call screen pool_items

    label pool:
        if ventsopen:
            scene bg poolwater
        elif run_ok:
            scene bg poolopen
        else:
            scene bg pool
        show tali back at left
        call screen pool_items

    screen pool_items():
        modal True
        imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump ("map")
        showif poolloot1:
            imagebutton:
                idle "images/events/pool/crate1_idle.png"
                hover "images/events/pool/crate1_hover.png"
                focus_mask True
                action [SetVariable("poolloot1", False), Jump ("crate")]

        showif poolloot2:
            imagebutton:
                idle "images/events/pool/crate2_idle.png"
                hover "images/events/pool/crate2_hover.png"
                focus_mask True
                action [SetVariable("poolloot2", False), Jump ("crate")]

        showif poolloot3:
            imagebutton:
                idle "images/events/pool/crate3_idle.png"
                hover "images/events/pool/crate3_hover.png"
                focus_mask True
                action [SetVariable("poolloot3", False), Jump ("crate")]

        showif ventquest:
            imagebutton:
                idle "images/events/pool/comp_idle.png"
                hover "images/events/pool/comp_hover.png"
                focus_mask True
                action [SetVariable("poolcomp", False), Jump ("poolcompevent")]

        showif ventsopen:
            imagebutton:
                idle "images/events/pool/water_idle.png"
                hover "images/events/pool/water_hover.png"
                focus_mask True
                action Jump ("ventsenter")

    label ventsenter:
        menu poolmenu1:
            "Enter vents.":
                jump ventsenter1
            "No.":
                jump pool


    label poolcompevent:
        scene bg poolopen
        show tali tool at left
        tali "Finally some peace and quiet. Time to check this without distractions..."
        play sound "audio/equip.ogg"
        pause 1
        tali "Hmm... scans show a very large area under this pool."
        show tali doubt at left
        tali "I don't see an entrance nearby but it's definitely here somewhere."
        show tali tool at left
        tali "This terminal can be used to pump the water out. Hopefully it's still functional."
        show tali doubt at left
        tali "Guess this might be the path forward we need. I'd better call reinforcements before committing to this though."
        menu calljesora:
            "Call Jesora.":
                $ ventquest = False
                show tali tool at left
                play sound "audio/message.mp3"
                tali "Hey Jesora. I think I found an alternate path to the ship's bridge."
                jesora "No kidding? Way to go Tali! Where are you?"
                tali "Come over to the pool... and bring some firepower."
                jesora "On my way."
                scene black
                play sound "audio/walk.mp3"
                "Moments later Jesora arrives with a crew."
                scene bg poolopen
                with dis
                show tali doubt at left
                show jesora doubt at right
                jesora "Well? Don't tell me you just wanted to have a beach party."
                tali "Were that the case you should have brought some drinks."
                show jesora smile at right
                jesora "No drinks I'm afraid, but I brought Nyun for a festive mood."
                show nyun doubt behind jesora
                nyun "Hello sweetie."
                show tali talk at left
                tali "Nyun? Why did you come here?"
                show nyun talk behind jesora
                nyun "I'm tired of sitting at the bar all the time, so I volunteered. I always wanted to see our stunning technician in action."
                show tali facepalm at left
                tali "I really hope that won't be necessary."
                show tali doubt at left
                show jesora stand at right
                show nyun doubt behind jesora
                jesora "Alright ladies, enough flirting. Show me what you've found Tali."
                show tali tool at left
                tali "Give me minute. I need to pump out the water from the pool. Get ready."
                scene black
                play sound "audio/water1.mp3"
                show pooldry
                pause 3
                scene bg pool2
                with dis
                show tali gunstand at left
                show jesora guntalk at right
                jesora "I'll be damned. This looks like what we've been looking for. We need scouts in there STAT."
                scene bg pool3 with dis
                nyun "This looks... scary. Ugh, and it stinks like the toilets back on Omega."
                tali "Already regret coming?"
                jesora "Alright girls, step aside. Let's..."
                scene bg pool3 with hpunch
                play sound "audio/creepone.mp3"
                pause 1
                play sound "audio/creepone.mp3"
                scene bg pool4 with hpunch
                stop music
                play music "audio/bg/run_bg.mp3" loop
                jesora "Shit, not this guy again!"
                nyun "Oh no! Are those the monsters I've heard about?! They look dangerous!"
                scene bg pool2
                show tali gunstand at left
                show jesora gunshout at right
                play sound "audio/heavyshots.mp3"
                jesora "They keep coming and I don't know how to kill this huge fucker! Run and we'll hold them back!"
                tali "Are you kidding?! You want me go in there alone?!"
                jesora "No choice, sweet cheeks! You're our only hope to leave this place. Go and find the thermal stabilizers. And take Nyun with you, she don't survive this fight!"
                tali "...FUCK!"
                scene black
                play sound "audio/run.ogg"
                pause 1
                scene bg pool5
                play sound "audio/gunshot.mp3"
                pause .5
                play sound "audio/gunshot.mp3"
                nyun "Oh Goddess, It's a deadend Tali!"
                show bg pool6 with hpunch
                play sound "audio/punch.mp3"
                nyun "We'll die here! Why did I leave the ship?! It was better to stay in that dirty club than come here!"
                show bg pool7
                tali "Hey! Get a hold of yourself and check that hatch behind you! It has to open somehow!"
                show bg pool8
                play sound "audio/gunshot.mp3"
                pause .5
                play sound "audio/gunshot.mp3"
                tali "Come on you freaky bastards! Someday I'll take you all down!"
                scene bg pool9
                play sound "audio/metalshut.mp3"
                pause 2
                scene bg pool10
                tali "Keelah, they keep coming! Did you get it open yet? Nyun?!"
                scene bg pool11
                tali "What the hell?! Nyun you've got to be kidding me right now!!"
                scene black
                play sound "audio/metalshut.mp3"
                pause 2
                jump VentsStart

            "Later.":
                jump pool


    label phantomcut:
        scene bg poolcut1 with hpunch
        play sound "audio/fall.ogg"
        tali "!! Looks like she didn't notice me..."
        scene bg poolcut2
        play sound "audio/uibeep.mp3"
        tali "What the hell is she doing there?"
        scene bg poolcut3
        play sound "audio/message.mp3"
        tali "Jesora, do you copy? She's here, in the corridor to the pool! Jesora?"
        scene bg poolcut4
        tali "...What the? Where did she go?!"
        scene bg poolcut5
        play sound "audio/sword.mp3"
        pause 1
        tali "Oh shi..."
        scene bg poolcut6 with hpunch
        play sound "audio/gunshot.mp3"
        pause .5
        play sound "audio/gunshot.mp3"
        pause .5
        scene bg poolcut7
        play sound "audio/omnicharge.mp3"
        tali "I have a bad feeling about this!"
        scene bg poolcut8 with hpunch
        play sound "audio/explosion.mp3"
        pause 2
        scene bg poolcut9
        jesora "Yeah! That's how we do it in my neighborhood, bitch!"
        scene bg poolcut10
        pause 1
        scene bg poolcut11
        play sound "audio/electric.mp3"
        phantom "Nnn-nnghh... "
        scene bg poolcut12
        phantom "You will pay for that!"
        scene bg poolcut13
        jesora "She survived?! How the fucking fuck is that possible?!"
        scene bg poolcor
        show tali guninjured at left
        show jesora guntalk at right
        jesora "Get up, suitgirl! She's running for the pool, we can't waste time."
        show tali angry at left
        show jesora gunstand at right
        tali "What the hell?! Could you wait for me to move away before firing a rocket?!"
        show jesora guntalk at right
        jesora "And miss my shot? No way. Besides, one more second and she could have cut you to shreds. Just be glad you didn't end up like Fodder 29."
        show tali guninjured at left
        tali "You call your vorcha... Look, fine. Just give me a second to catch my breath..."
        scene bg pool
        with dis
        show tali gunstand at left
        show jesora guntalk at right
        jesora "She must be in here somewhere!"
        scene bg poolcut14
        play sound "audio/uibeep.mp3"
        tali "There she is! Hey! Get away from terminal!"
        scene bg poolcut16
        jesora "Stop right there you bitch! One wrong move and I will NOT hesitate to kill you!"
        show bg poolcut15
        phantom "I can give you so much more than one move, asari..."
        scene black
        play sound "audio/metal door.ogg"
        show poolopen
        pause 3
        scene bg poolcut17
        play sound "audio/water.mp3"
        tali "That... does not sound friendly."
        scene black
        show krokpool
        pause 2
        scene black
        play sound "audio/heavyshots.mp3"
        jesora "Shoot him!"
        play sound "audio/krokroar.mp3"
        pause 2
        scene bg poolcor
        show tali guninjured at left
        show jesora gunshout at right
        jesora "That fucking beast is invincible! These gun's aren't doing shit to him!"
        show jesora gunstand at right
        play sound "audio/krokroar.mp3"
        pause 1
        show tali gunstand at left
        tali "He's coming! Run!"
        play sound "audio/run.ogg"
        pause 2
        scene bg hangar
        show tali guninjured at left
        show jesora guntalk at right
        jesora "Great. Another brutal monster set free. I hope our turrets can at least scare him away."
        show jesora gunstand at right
        show tali talk at left
        tali "Is it optimistic to hope he went back and killed that woman?"
        show jesora guntalk at right
        jesora "For all I know she could be his fuckmeat, but that's TOO optimistic. Anyway we need to search another way to reach the forward part of the ship. I have plenty to think about so I'll see you later. I know how to reach you if I need you. In the mean time you use that scanner and search. Maybe you'll lucky."
        #"THE MAIN STORY ENDS HERE. THANKS FOR PLAYING! HOPE YOU ENJOYED IT. YOU CAN CONTINUE TO PLAY TO UNCOVER MORE SCENES!"
        $ quest = "Search for answers in pool location."
        $ ventquest = True
        $ run_ok = True
        jump MedBayUsual











    label scanmap:
        scene bg map
        show medimg
        show barimg
        show wareimg
        show bay2img
        show comimg
        show engineimg
        if pool:
            show poolimg
        if poolnew:
            show poolimg
        if bay1:
            show bay1img
        if prison:
            show prisonimg
        if hallway:
            show hallwayimg

        play sound "audio/scan.mp3"
        show scan
        pause 1.2
        if pool == False and poolnew == False:
            play sound "audio/scandet.mp3"
            show poolscan
            pause 1
            $ pool = True
            $ quest = "Check the pool."
        jump map




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
        krogan "Fuck yeah! Take this you maggots!"
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
        jesora "Long story. Short version is they're former crew. Ours from before we found you. We got stuck together when the doors started closing. They don't play nice."
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
        if gatesQuest:
            scene bg hall4
            with dis
            show tali doubt at left
            show jesora stand at right
            jesora "You're here? Great. See this big thing in front of the door? Take care of it."
            show jesora smiletalk at right
            jesora "With anyone else I'd check their work, but you're a good who knows how to handle big ones."
            show tali talk at left
            tali "Uh. Alright... well, let me check it."
            scene bg hall5
            show tali tool at left
            with dis
            tali "Really? It's actually pretty simple. Even a vorcha could use it if you trained him to press a single button long enough. Just a moment..."
            show bg hall6
            play sound "audio/beamlaser.mp3"
            pause 1
            show tali angry at left
            tali "Got it! It's working!"
            show jesora talk at right
            jesora "Never doubted you for a moment, suitgirl."
            scene bg hall7
            play sound "audio/phantomshot.mp3"
            pause 1
            scene bg hall8
            play sound "audio/fleshhit1.mp3"
            pause 2
            play sound "audio/fleshhit1.mp3"
            scene bg hall9 with hpunch
            pause 2
            play sound "audio/sword.mp3"
            scene bg hall10
            pause 1
            scene bg hall11
            play sound "audio/fall.ogg"
            pause 2
            scene bg hall15
            jesora "Do you have ANY idea how long it took me to teach him left from right?! Open fire!"
            play sound "audio/machinegun.mp3"
            pause 1
            scene bg hall12
            pause 2
            scene bg hall13
            play sound "audio/omnicharge.mp3"
            pause 1
            show bg hall14 with hpunch
            pause 1
            scene bg hall16
            play sound "audio/explosion.mp3"
            pause 2
            scene black
            with dis
            pause 3
            jesora "Suitgirl, you alive? You hear me?"
            scene bg hall18
            with dis
            show tali facepalm at left
            show jesora gunstand at right
            tali "Ngh. My head... What happened?"
            show jesora guntalk at right
            jesora "Some crazy bitch happened. I don't know who she is but I've never seen a soldier with skills like that."
            show tali talk at left
            tali "It's a miracle we survived..."
            jesora "Looks like she just wanted to destroy the laser. I lost three men. This damn ship's costing us too many lives. We need to find a way off this floating tomb."
            show jesora gunstand at right
            tali "You're right... but the laser's done for. I don't think we'll be able to fix it with anything on this station! Suggestions?"
            show tali doubt at left
            show jesora guntalk at right
            jesora "First we need to find out who that bitch was and what she knows. I might have an idea. Visit me at the bar when you the have time."
            show tali facepalm at left
            tali "Alright... I'll go and rest up a bit. I'll see you later."
            $ quest = "Meet Jesora at the bar"
            $ gatesQuest = False
            $ bitchQuest = True
            jump medbayafterdefeat
        if hallFirst:
            $ hallFirst = False
            jump hallwayFirst
        if bitchQuest:
            scene bg hall18
        elif hallwaydest:
            scene bg hall18
        else:
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
        if secureDoors:
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
        else:
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
            $ quest = "Talk with Jesora about fixing the omni-tool."
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
        tali "Is that... a red varren? He looks so much bigger than the others! And even more dangerous! All the more reason to finish him off here!"
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
                tali "You won't get away that easily!"
                scene black
                play sound "audio/creepone.mp3"
                creature "Arrrrrr!"
                play sound "audio/gunshot.mp3"
                pause 1
                play sound "audio/gunshot.mp3"
                pause 1
                tali "Stop dodging you bosh'tet!"
                scene bg redvarren5
                with dis
                play sound "audio/walk.mp3"
                tali "Hah! A dead end! Time to-!"
                play sound "audio/roar.mp3"
                pause 1
                play sound "audio/run.ogg"
                scene bg redvarren6
                with dis
                pause 1
                tali "What the hell? Where did he run off to?"
                tali "Great, where am I now? This part of the ship looks abandoned. And this strange door..."
                tali "That damned varren is probably hiding back there. Good. There's no room for him to sneak off."
                scene black
                play sound "audio/metal door.ogg"
                pause 2
                $ prison = True
                jump prisonFirst
            "Let him go.":
                tali "I'd better not. Some varren are craftier than others. He might be leading me down a trap..."
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
            tali "I don't see it on the scans. Someone really wanted to tuck this chamber away... maybe even from the crew."
            show tali doubt at left
            tali "Lets take a look."
            scene bg prison1
            with dis
            tali "Those cages were broken down with brute force alone! I don't want to meet the monster that did that!"
            play sound "audio/creepone.mp3"
            scene bg prison2 with hpunch
            pause 1
            tali "Whoaaa!"
            tali "Easy there, ugly!"
            scene bg prison3
            with dis
            tali "Ugh. I can smell you two through my filters. Good luck getting out of those, hah!"
            tali "I need to check the locks to make sure they don't get out."
            play sound "audio/creepone.mp3"
            pause 1
            tali "Yeah, you heard me right you creeps!"
            $ prisFirst = False
            jump prison
        jump prison

    label prison:
        if run3:
            jump runstart
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
        "Dogbone was found"
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
        tali "A dogbone? Looks like a varrens toy."
        jump prison


    label prisonBody:
        scene bg prison16
        with dis
        tali "They really did a number on you didn't they? Another dead mercenary."
        scene black
        show clips:
            xalign 1.2
            yalign 0.5
        show clips with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        $ ammo += 5
        "5 thermal clips were found"
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
        tali "Hmph. Not so tough behind bars, are you? I'm so busy fighting you freaks I didn't even realize how ugly you really were."
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
                    tali "All huff and puff I see. If it wasn't for your strength, you'd make some decent zoo animals."
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
                        "Handjob" if lewd > 14:
                            jump cageHand
                        "Milking" if lewd > 20:
                            jump cageMilk
                        "Use lube (vaginal)" if lewd > 25 and isLube:
                            jump cageLube
                        "Use lube (anal)" if lewd > 30 and isLube:
                            jump cageLubeAnal
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
                $ varHunt = True
                jump prison
            "Another time.":
                jump prison

    label cageLubeAnal:
        $ lewd += 1
        $ prisCum = True
        scene bg prison20 with hpunch
        play sound "audio/punch.mp3"
        tali "Today's your lucky day, ape. I'm feeling particularly adventurous."
        play sound "audio/gorillaroar.wav"
        pause 2
        scene bg prevent1
        with dis
        tali "Lets see... It should go on like this."
        play sound "audio/lewsquish.mp3"
        scene bg prevent2
        tali "Is that a smile on your ugly face?"
        scene bg prevent3
        tali "There. Now to spread it around..."
        scene bg prevent8 with hpunch
        play sound "audio/punch.mp3"
        tali "Ngh, hey! Couldn't stop yourself for one minute could you?"
        play sound "audio/roar.mp3"
        tali "Ugh. I guess I could let you, for being such an obedient ape..."
        scene bg prevent4
        show cageLube_loop1
        $ renpy.pause ()
        scene bg prevent8
        tali "Keelah, why is he good at this? I can't wait anymore. I want to see how well it works..."
        scene bg prison24
        play sound "audio/gorillaroar.wav"
        tali "Mmm. There we go. Piece by piece..."
        scene bg prison25
        play sound "audio/dress.mp3"
        pause 2
        scene bg prevent7
        tali "Keelah, it's hot and throbbing. I guess you want it a lot more than I do, huh?"
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
        tali "A-Ah. Mnph. I didn't expect it to be so good... ah"
        scene black
        show cageLubeAnal_trans1
        pause 1
        tali "Ah? Mnph. You slipped out? No problem, I can just-"
        play sound "audio/punch.mp3"
        scene bg prisonanal2 with hpunch
        pause 1
        tali "Wha.. what the hell are you doing?! Let me go this instant you overgrown monkey! "
        scene black
        show cageLubeAnal_trans2
        pause 2
        tali "N-NGHH!! Oh Keelah. I thought you'd never guess it right..."
        scene bg prisonanal1
        tali "Mph. I can't help myself. Let me jack it off with my ass."
        scene black
        show cageLubeAnal_loop1
        $ renpy.pause ()
        scene bg prisonanal4 with hpunch
        play sound "audio/creepone.mp3"
        tali "A-Ah! This position?! But your cock's lined up with my...!!"
        play sound "audio/gorillaroar.wav"
        scene black
        show cageLubeAnal_loop2
        $ renpy.pause ()
        scene bg prisonanal3 with hpunch
        play sound "audio/cumshot1.ogg"
        tali "Aughhh! Yes! Fill me up you filthy animal! Dump all that hot monkey jizz!"
        scene black
        show cageLubeAnal_cum
        $ renpy.pause ()
        play sound "audio/lewsquish.mp3"
        scene bg prisonanal5
        tali "Ugh. H-Happy now? You pumped my ass so full of your cum. Ngh. Your dirty beast dreams came true, I guess."
        scene bg prisonanal6 with hpunch
        play sound "audio/creepone.mp3"
        tali "Yeah... at least you're still stay in your cage. And I need to head back to the medbay..."
        jump medbayafterdefeat

    label cageLube:
        $ lewd += 1
        $ prisCum = True
        scene bg prison20 with hpunch
        play sound "audio/punch.mp3"
        tali "Today's your lucky day, ape. I'm feeling particularly adventurous."
        play sound "audio/gorillaroar.wav"
        pause 2
        scene bg prevent1
        with dis
        tali "Lets see... It should go on like this."
        play sound "audio/lewsquish.mp3"
        scene bg prevent2
        tali "You're grinning a little too hard there, ape."
        scene bg prevent3
        tali "There. Now to spread it around..."
        scene bg prevent8 with hpunch
        play sound "audio/punch.mp3"
        tali "Hey! Don't make me stop!"
        play sound "audio/roar.mp3"
        tali "Mmn. I'll overlook it this once. Keelah, why are you so good at feeling up women?"
        scene bg prevent4
        show cageLube_loop1
        $ renpy.pause ()
        scene bg prevent8
        tali "Ngh. That should be more than enough. L-Lets move on."
        scene bg prison24
        play sound "audio/gorillaroar.wav"
        tali "There we are... piece by piece."
        scene bg prison25
        play sound "audio/dress.mp3"
        pause 2
        scene bg prevent7
        tali "Ngh? It's so slimy and sticky today. How backed up are you?"
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
        tali "Ah! Ahn! Why does it feel so good?"
        scene bg prevent6
        show cageLube_loop3alt
        tali "D-Don't you dare cum inside! That's an or-!"
        scene bg prevent5
        show cageLube_cum
        $ renpy.pause ()
        scene black
        pause 1
        play sound "audio/dress.mp3"
        pause 1
        scene bg prison4
        tali "Hmph. Guess it was too much for you. Well, I'm feeling generous, so no punishment today."
        play sound "audio/gorillaroar.wav"
        tali "Keelah, you are insatiable. You even made me do all the work!"
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
        tali "Don't get ahead of yourself. I'm just curious right now."
        scene bg prisonscene5
        show cageHandLoop2
        $ renpy.pause ()
        play sound "audio/roar.mp3"
        tali "How about this? It feels better right? Maybe if I rub the tip with my thumbs? You look so silly."
        scene bg prisonscene5
        show cageHandLoop2alt
        $ renpy.pause ()
        scene bg prisonscene5
        show cageHandCum1
        $ renpy.pause ()
        scene bg prison4
        play sound "audio/gorillaroar.wav"
        tali "Hmph. You'd better appreciate that you ape. Now go play with yourself without me around."
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
        tali "Oh? You're harder than usual. Did you fail to cum by yourself or something?"
        scene bg prison15 with hpunch
        play sound "audio/punch.mp3"
        tali "GAH! HANDS OFF!"
        scene bg prison21 with hpunch
        play sound "audio/gorillaroar.wav"
        tali "Damned persistent, aren't you?"
        scene bg prisonscene2
        show cageHandLoop3
        $ renpy.pause ()
        scene bg prison21
        tali "Ngh. He's using my thighs like a fucksleeve. My pussy's getting so... sensitive!"
        scene bg prisonscene3
        show cageHandLoop4
        $ renpy.pause ()
        tali "Hmgh. You like it like this right? Let me milk that beastly load from those fat balls!"
        scene bg prisonscene3
        show cageHandLoop4alt
        $ renpy.pause ()
        scene bg prisonscene3
        show cageHandCum2
        $ renpy.pause ()
        scene bg prison4
        tali "Hmph. Proud of yourself?"
        play sound "audio/gorillaroar.wav"
        tali "Don't look at me like that."
        $ prisCum = True
        jump prison

    label barracks:
        if run1:
            jump runstart
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
        tali "I finally found you! Where's Jesora?"
        show asari talk at right
        asari "Our group was split up not far from the hangar bay. The damn door slammed shut between us - nearly pinched my leg!"
        asari "We haven't heard from her since."
        show tali shame at left
        show asari stand at right
        tali "That's not good."
        show tali talk at left
        tali "The way to the hangar should be clear. Head back to Serok."
        show tali doubt at left
        show asari gun at right
        asari "Thank the Goddess. We're leaving team, now!"
        play sound "audio/walk.mp3"
        "Better organized than the vorcha could ever hope to be, the asari group left."
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
                "They're pumping some animals with experimental serums and mating different species between each other, trying to breed some kind of super soldier. The boss is some looney Hanar with Cerberus connections?"
                "Don't tell my family, I don't want them to worry. Most of all I don't need them finding a reason to track them down if something goes wrong."
                "I heard we're waiting for another ship to deliver us some fresh cargo, new monsters and mercs. I'll try and stow away in there somehere. I gotta get out of here."
                "I'll contact you when I get to the nearest spaceport. I'll use this pad and its signature, there's no way I can leave it behind."
                show tali doubt at left
                tali "Cerberus. Why doesn't that surprise me? I should've known that sick organization was involved in this. What slippery scum..."
            "Read 3rd message.":
                "SECURITY MANAGEMENT REQUEST: User - Marcus. Respond as soon as you have recieved this message. Unregistered encryption and communication was detected from this device to unknown 3rd parties."
                "This is a violation of your NDA and a breach of security. It is recommended you rendezvous with your nearest security officer so that an investigation may begin to prove your innocence."
                "Do not forget to bring your private holopad."
            "Thats all.":
                jump barracks
        jump tabletMsg


    label barracksEnt:
        if barrackskey:
            play sound "audio/uibeep.mp3"
            tali "It worked! The door's opening."
            jump utilityroom
        tali "Sealed. Looks like an ammo wing with type 2 security locks. No way I can blow this up. I wonder how much firepower's behind it?"
        tali "There's a keycard slot here. Maybe I can find one somewhere?"
        jump barracks

    label utilityroom:
        if zeltanhallway:
            $ zeltanhallway = False
            scene bg u
            show tali facepalm at left
            show zeltan stand at right
            tali "Zeltan... Oh Keelah."
            show tali angry at left
            tali "How the hell did you even get into this room? The door looks too narrow for you."
            show tali doubt at left
            zeltan "Desperately. Why did you come here? I don't want to go back."
            menu zeltan2:
                "Want to try again?":
                    zeltan "Doubtful. Are you wanting to laugh at me again?"
                    show tali talk at left
                    tali "No. Why would you think that? I was actually pretty horny back then. You aren't as bad as you think."
                    show tali doubt at left
                    zeltan "Hopeful elation. You really liked it? I knew my unique sense of humor would shatter your defenses. Ha. Ha. Ha."
                    tali "Yeah... I'm surprised myself."
                    zeltan "Shyly. So... how will it happen? What you want me to do?"
                    tali "Don't warry. I will take care of it."
                    jump zeltanmed2
                "Convince him to go back.":
                    show tali talk at left
                    tali "Listen, Zeltan, you're a nice guy. Forget about what happened, ok? I'm just not your type. You're an elcor, remember?"
                    show tali doubt at left
                    tali "I know this. I studied interspecies biology and quarians are not suitable for sex with elcors. I was... just drunk."
                    zeltan "Dejected. Yes, of course. We are different species. How could I forget that. This is the reason."
                    tali "See? Now just go back to the ship. Serok and his team can't survive without you, tough guy!"
                    scene bg map
                    show tali facepalm at left
                    tali "Ahh, shit. I guess its time to ask Serok for extra pay for babbysitting."
                    $ barelkor = True
                    jump map
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
        "Lube was found"
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
        if run2:
            jump runstart
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

        showif havedogbone and reddead == False:
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
        tali "You?! Figured I'd find you sooner or later."
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
        tali "I can't let you leave. I'll make it quick!"
        $ enemyID = 20
        $ havedogbone = False
        jump sliderBoss


    label redvarrenevent1:
        $ lewd += 1
        $ havedogbone = False
        scene bg taliship4
        tali "Huh. I guess you're not as aggressive as your other friends. I think I have something that belongs to you. Eyes up."
        scene bg taliship5
        play sound "audio/roar.mp3"
        pause 2
        scene bg taliship6
        with dis
        tali "Aww, you're just a big lovable varren aren't you? Nothing like those other brutes. Maybe I should give you a name..."
        scene bg taliship7
        with dis
        play sound "audio/dogbreath.mp3"
        tali "Oh! Is that..."
        scene bg taliship8
        with dis
        tali "Keelah. Its so thick and hot. I guess I could... help you with that. Give me a minute..."
        scene bg taliship8
        show dogLoop1
        $ renpy.pause ()
        scene bg bay1event1
        with dis
        tali "Mmph. It's so sticky and hot. And the taste is just..."
        scene bg bay1event1
        show dogLoop2
        $ renpy.pause ()
        scene bg bay1event1
        show dogLoop3
        $ renpy.pause ()
        scene bg bay1event2 with hpunch
        play sound "audio/dogbreath.mp3"
        tali "Mmm. Can't wait? Don't worry boy. Let me take care of this fat cock."
        menu redbaychoice:
            "Licking":
                show dogLoop4
                $ renpy.pause ()
                scene bg bay1event2
                show dogLoop5
                $ renpy.pause ()
                scene bg bay1event3
                tali "I can feel your balls throbbing. Good boy. Give Tali all that pent up cum!"
                scene bg bay1event3
                show dogCum
                $ renpy.pause ()
                scene bg taliship
                show tali fin2 at left
                with dis
                tali "Looks like I overdid it. I should head over to the medbay."
                jump medbayafterdefeat
            "Cockpit action":
                scene bg bay1event1
                tali "Mmm. Maybe my ship's still useful after all..."
                scene bg cockpit1
                with dis
                tali "Come here boy. I know somewhere small and tight we can enjoy eachothers company."
                scene black
                with dis
                "Some time later..."
                stop music
                play music "audio/bg/void_bg.mp3" loop
                scene black
                show cockpit1_trans1
                pause 2.7
                show cockpit1_loop1
                $ renpy.pause ()
                show cockpit1_trans2
                pause 1.7
                stop music
                play music "audio/bg/common_bg.mp3" volume 0.3 loop
                scene black
                show cockpit1_trans3
                pause 1
                scene black
                scene cockpit1_loop2
                $ renpy.pause ()
                scene bg cockpit2
                tali "That's it! Fuck my pussy raw you mangy, fat cocked mutt!!"
                scene black
                show cockpit1_loop3
                $ renpy.pause ()
                scene black
                show cockpit1_loop4
                $ renpy.pause ()
                scene bg cockpit3
                tali "Yes! I'm cumming! Give me that fat varren knot!! Oh Keelah!"
                scene bg black
                show cockpit1_cum1
                $ renpy.pause ()
                scene black
                show cockpit1_cum2
                $ renpy.pause ()
                scene bg cockpit4
                play sound "audio/dogbreath.mp3"
                tali "Mmm. Such a good, strong boy. I feel so good..."
                scene bg cockpit5
                play sound "audio/lick.mp3"
                tali "Oh, you know how to please female. Unfortunately I have to go. Behave."
                jump medbayafterdefeat




    label redtimerevent:
        play sound "audio/fall.ogg"
        show tali fallmask at left
        play sound "audio/glass.mp3"
        "Tali falls down and loses sight of her weapon. She raises a hand to protect herself from the growling varren."
        tali "Easy boy! Don't come any closer!"
        jump redvarrenevent2

    label redvarrenevent2:
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        $ lewd += 1
        scene bg red1
        play sound "audio/roar.mp3"
        tali "A-Alright, alright. Please stop growling at me. Just go. I won't chase after you, alright? Please?"
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
        tali "C-COUGH. I never thought he'd back off!"
        show red stand at right
        play sound "audio/creepone.mp3"
        pause 2
        hide red stand
        play sound "audio/run.ogg"
        tali "He's gone. I have to get to the medbay quickly..."
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
        tali "Back off, crazy eyes!"
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
        jesora "Hey, you hear me? What's going on out there?"
        tali "I got to the cockpit door. There was a distraction but everything's fine now. What was that alarm all across the ship?"
        jesora "Not sure but I got reports from our patrols. Seems a lot of security doors have begun to shut everywhere."
        jesora "Looks like you breaching into the local security system booted up a failsafe. Do what you have to and get back to me."
        tali "Copy."
        scene bg taliship
        $ hackID = 3
        jump sliderDoor

    label bay1cockpit:
        scene bg cockpit
        show tali back at left
        with dis
        tali "I can't believe the cockpit nearly survived the explosion! Sad the rest couldn't. I wouldn't have to deal with those pirates to get off this ship otherwise."
        show tali shame at left
        tali "Alright, I got the navigation parts. Now I can fix Serok's ship. There might be some scrap lying around if I ever need it so it couldn't hurt to come back."
        scene black
        play sound "audio/walk.mp3"
        "Tali trekked back to the hangar bay."
        jump hackQuestComplete

    label bay1door:
        $ bay1first = False
        scene bg bay1door
        show tali doubt at left
        with dis
        tali "Whoa, what a smell. This place is different than I remembered."
        show tali tool at left
        play sound "audio/equip.ogg"
        tali "Alright, lets check it out."
        show tali tool at left
        tali "I have access to lock commands, but there's some pushback from security."
        show tali shame at left
        tali "Time to get hacking... and listen out for any unwanted attention."
        scene bg bay1doortut
        "Hacking is another simple mini game. In the upper-right corner you can see the decryption screen."
        "Click the HACK command when the blue slider moves between the yellow bars for a successful hack. Failure will result in a retry for that attempt."
        "The yellow number on the left shows how many subroutine Tali will need to hack in order to open the door."
        "Lastly, watch out for enemies. They can be nearby when Tali is hacking and can approach at any given moment."
        "If Tali's lewd level is high enough, pink bars will appear during hacking. This works the same as the yellow bars, but the results are entirely different..."
        scene bg bay1door
        jump sliderDoor

    label bay2_enter:
        if barfirst == False:
            jump bay2_vorcha
        if poolQuest:
            jump bay2_bar
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
                tali "There are some... bodies of guys that look like high-end mercs. Any idea what outfit they're from?"
                jesora "My guess? Professional and elite. Someone's hiding dirty laundry and aren't pinching pennies to keep it that way. I'd call myself resourceful but even those guys I've got nothing on."
            "What about those... creatures?" :
                show jesora talk at right
                jesora "If you're male, they'll kill you. If you're female, you're gonna wish they had. Try not to get caught. I've lost too many girls on this ship already. Trackers are one thing, but you'll get carried somewhere no one can find you if you're not careful."
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
                jesora "Oh? Lets see here. Well look at that, all 20. You really are something, huh?"
                show jesora stand at right
                show tali talk at left
                tali "Alright. What about my omni-tool?"
                show jesora talk at right
                jesora "Give me a minute. I'll let you know after I've scavenged a few parts from some of our expired crew. Take this as a bit of payment in the mean time."
                scene black
                show doorexp:
                    xalign 1.2
                    yalign 0.5
                show doorexp with move:
                    xalign 0.5
                    yalign 0.5
                play sound "audio/gunready.wav"
                "Tali received a door breaching charge"
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

            #"I saw you having fun with the vorcha." if shipInsideChoice:
                #show jesora smile at right
                #"Really? You are a curious one, aren't you?"
                #show tali shame at left
                #show jesora smiletalk at right
                #jesora "Jealous?"
                #show tali angry at left
                #tali "What?! No I... Of course not. But it's a little weird isn't it?"
                #show tali doubt at left
                #show jesora smile at right
                #jesora "Dont be so dull, miss Zorah. Even you need to relax sometimes, right? Play cute all you'd like, I see that same sparkle in your eyes that's in every whore I've met in Omega. Maybe even brighter."
                #show tali shame at left
                #show jesora smiletalk at right
                #jesora "So... you interested in some fun?"
                #menu jesorafun:
                    #"Well, may be just a little..." if lewd > 15:
                        #$ shipInsideChoice = False
                        #jump jesoratalifun
                    #"I should go" :
                        #show tali doubt at left
                        #show jesora smile at right
                        #jesora "See you next time then, cutie."

        jump jesoratalkmenu

    label bay2_vorcha:
        scene bg hangar
        show vor1 stand at right
        show tali doubt at left
        play sound "audio/funmoan.mp3"
        if z1:
            $ z1 = False
            vorcha "Aggrh... little quarian love... big cocks!"
            show tali facepalm at left
            tali "Oh... i gonna kill this stupid elcor."
        show tali doubt at left
        tali "You again."
        menu bay2_menu:
            "The bar.":
                jump bay2_bar
            "Jesora's cabin.":
                jump jesoraCabin
            "Back.":
                jump map



    label bay2_bar:
        if barvar:
            $ barjesora = False
            $ barvorcha = True
            $ barserok = False
            $ barelkor = False
            $ barnyun = False
            scene bg bar3
            show tali doubt at left
            tali "Hm, not so crowded today..."
        if barfirst:
            jump bar_first
        scene bg bar3
        #if zeltanhide:
            #tali "Hmm. Where is Zeltan? I guess we have to talk."
        call screen bar_items


    screen bar_items():
        modal True
        imagebutton xpos 0.9 ypos 0.8:
            idle "images/map/backbutton_idle.png"
            hover "images/map/backbutton_hover.png"
            focus_mask True
            action Jump ("map")
        showif barjesora and days % 2 == 0:
            imagebutton:
                idle "images/events/bar/jesora_idle.png"
                hover "images/events/bar/jesora_hover.png"
                focus_mask True
                action Jump ("jesorabar")

        showif barvorcha:
            imagebutton:
                idle "images/events/bar/vorcha_idle.png"
                hover "images/events/bar/vorcha_hover.png"
                focus_mask True
                action Jump ("vorchabarevent")

        showif barserok:
            imagebutton:
                idle "images/events/bar/serok_idle.png"
                hover "images/events/bar/serok_hover.png"
                focus_mask True
                action Jump ("serokbar")

        showif barelkor:
            imagebutton:
                idle "images/events/bar/elkor_idle.png"
                hover "images/events/bar/elkor_hover.png"
                focus_mask True
                action Jump ("elkorbar")

        showif barnyun:
            imagebutton:
                idle "images/events/bar/nyun_idle.png"
                hover "images/events/bar/nyun_hover.png"
                focus_mask True
                action Jump ("nyunbar")

    label vorchabarevent:
        show tali doubt at left
        tali "What's he doing here?"
        scene bg barevent1
        with dis
        tali "Hey ugly, have you seen Nyun?"
        play sound "audio/wetsquish.mp3"
        pause 1
        play sound "audio/funmoan.mp3"
        show bg barevent2
        tali "...Are you serious?"
        play sound "audio/sucking4.ogg"
        tali "There's a vorcha dick in your mouth, Nyun. If you haven't noticed."
        menu barnyun:
            "Stay.":
                scene black
                show nyunbar1
                $ renpy.pause ()
                scene bg barevent2
                tali "Alright then. Guess it's self service today. You wouldn't mind if I..."
                play sound "audio/wetsquish.mp3"
                pause 1
                tali "Thanks Nyun."
                scene bg barevent8
                with dis
                tali "Hmmm. Doesn't it hurt to bang your head against the counter every time..."
                tali "Nyun? You alright?"
                play sound "audio/wetsquish.mp3"
                pause 1
                tali "...I think she's alright."
                scene black
                show nyunbar2
                $ renpy.pause ()
                scene bg barevent3
                play sound "audio/straw.mp3"
                pause 1
                play sound "audio/funmoan.mp3"
                nyun "Mmm. Oh yeah... come on you big bad monster, you caught me and nobody's willing to help me. Why don't you fuck my throat like a beast in heat?"
                show bg barevent4
                tali "Meh...how do you know?"
                scene black
                show nyunbar3
                $ renpy.pause ()
                scene bg barevent5
                nyun "GLLLPHH! GLUUGK! Yes! Yes, give it to me! Desecrate my innocent mouth with your hot, filthy cum!"
                play sound "audio/cumshot1.ogg"
                pause 2
                tali "Finished? Finally."
                show bg barevent6
                pause 2
                show bg barevent7
                play sound "audio/swallow.ogg"
                pause 2
                scene bg bar2
                show tali doubt at left
                show nyun curvy at right
                nyun "Mmmmmm. Momma needed it..."
                tali "Yeah. That was kinda... weird."
                show nyun smile at right
                nyun "Sweetie, don't be so selfish. You have so much fun out there with all those beasties. Poor old Nyun also needs some relief."
                show nyun stand at right
                show tali talk at left
                tali "I don't... Uh, sure. Why not. Thanks for drinks anyway Nyun. And I guess you'll go thank the vorcha for his... drink. Er. Well see you later."
                $ barvar = False
                $ barjesora = True
                $ barvorcha = False
                $ barserok = True
                $ barelkor = True
                $ barnyun = True
                jump map
            "Leave.":
                $ barvar = False
                $ barjesora = True
                $ barvorcha = False
                $ barserok = True
                $ barelkor = True
                $ barnyun = True
                jump map








    label jesorabar:
        scene bg bar2
        show tali doubt at left
        show jesora smiletalk at right
        if z2:
            $ z2 = False
            jesora "Hey there, big dick tamer. I heard you had a lot of fun recently."
            show tali shame at left
            tali "Ahh... he told you."
            show jesora smile at right
            jesora "Sure he did. Elcor can't show emotions but I swear I can see the glow of euphoria around him."
            show tali facepalm at left
            tali "Alright, let's just move on."
            show jesora smiletalk at right
            jesora "You sure? Don't feel like something's missing in your hands... or mouth?"
            show tali angry at left
            tali "Just shut up! I don't want to talk about it!"
            show jesora smile at right
            show tali doubt at left
            jesora "Yeah, I heard you can be very bossy bitch."
            show jesora think at right
            jesora "Hmmm... Where did I hear that from? Let me remember..."
            show jesora smiletalk at right
            show tali angry at left
            tali "Nah, fuck off!"
            jump bay2_bar
        jesora "Hey there vermin slayer. Come to join my little party?"
        menu jesora_bar:
            "Can I buy something?":
                show jesora talk at right
                jesora "Cute. I don't handle sales anymore. Since bunkering down, we've given that job to someone more suitable. Ask the big guy at the entrance."
                show tali talk at left
                tali "You mean..."
                show jesora smiletalk at right
                jesora "Yes, exactly. The very big one. In all cases."
            "You saw Zeltan?" if zeltanhide:
                show jesora stand at right
                jesora "Here? Not today. Maybe Serok sent him to patrol."
            "What's next?" if bitchQuest:
                $ bitchQuest = False
                $ hallwaydest = True
                $ quest = "Use the scanner on map."
                show jesora stand at right
                jesora "Here. Take this. Use it to improve your omni-tool."
                show tali tool at left
                tali "This is... this is broadband scanner utility!"
                show jesora doubt at right
                show tali angry at left
                tali "Where did you get it? Hell, why didn't you give it to me sooner?"
                show tali doubt at left
                show jesora stand at right
                jesora "That info's need-to-know and you don't need to know. Just use it to scan the ship. Let me know if, when and where you find bitch."
                $ scanOK = True
            "What's the plan?" if gatesQuest == False and gatesFlag:
                $ gatesFlag = False
                $ gatesQuest = True
                show jesora stand at right
                jesora "Gral and his dimwits have made their nest on the ships bridge. You remember where you found me? It's behind those gates."
                show jesora talk at right
                jesora "Without the thermal stabilizers they stole we can't do anything. So, the plan is pretty simple - let's go and get it back."
                show jesora doubt at right
                show tali talk at left
                tali "I hope you're not planning on sending me alone over there. Serok talked about some dangerous labs."
                show tali doubt at left
                show jesora talk at right
                jesora "Of course not. I've gathered my team over there. We've hauled an excavation-grade drill beam over there. It's from a mining site we had a job in before this hellhole."
                show jesora doubt at right
                show tali talk at left
                tali "Why not just blow up the door with breach charges?"
                show jesora stand at right
                jesora "We tried. Apparently it's not your usual security door like the ones you run into every so often. This gate was designed to protect the crew and high officers behind it."
                jesora "In other words - the door would survive even if you blew up the entire ship. It takes some serious money to get that kind of material."
                show jesora doubt at right
                tali "Where do I come in then?"
                show tali doubt at left
                show jesora talk at right
                jesora "You need to make sure this laser works. I don't have a tech specialist. Meet my crew in the hallway and make sure everything's up and running right. After that, well... get ready for a fight."
                show jesora doubt at right
                show tali talk at left
                tali "Alright."
            "I should go.":
                jump bay2_bar
        jump jesora_bar

    label serokbar:
        scene bg bar3
        show serok stand at right
        show tali doubt at left
        serok "What now?"
        menu serok_bar:
            "Why did you decide to pirate?":
                show serok talk at right
                serok "I had an opportunity, I used it. Took a ship and left that shitty Khar'shan behind me. I'd rather die than go back there."
                show serok smoke at right
                show tali talk at left
                tali "That bad? I've never heard of a batarian hating his homeworld. I've only every heard good things from them."
                show tali doubt at left
                show serok reason at right
                serok "Sure you do. No 'wrong' info is leaked outside that planet. Generations of dictators and iron-fisted despots tend to know how to keep the wrong information from getting out."
                show serok talk at right
                serok "Those dumb fucks are gonna be the end of us as a species. They've got red sand so far up their asses they probably have to shit out their mouths. It might not be in my lifetime but something'll knock their asses off their thrones. Either they wake up, my people get smart, or batarians will just be some homework project for future archeologists."
                serok "Year after year our government spends untold trilions to convince us we're hated across the galaxy. They end up believing it to the point where it's a self-fulfilling prophecy."
                show serok stand at right
                serok "But I know the truth. And it's even worse - no one gives a fuck. Who wants to deal with a monkey holding a grenade?"
                show serok smoke at right
                show tali talk at left
                tali "You're pretty grim when you aren't being sleazy, Serok. But at least you have a home you can go back to."
                show serok stand at right
                serok "Yeah, I know the story, girl. And as I understand it's kinda your fault, not much different than us. Regardless of the reasons, the outcomes remain the same. By the time we realize we're on the brink of extinction we'll be too late to do anything about it. Keep your head down, sure, but doing nothing is what got us in the mess to begin with."
                show serok smoke at right
            "What can you tell me about Gral?":
                show serok stand at right
                serok "Big, strong and clever. Not a usual combination for krogan. He knows how to keep men in check."
                show serok smoke at right
                show tali talk at left
                tali "That's... some unexpectedly good feedback about a guy who betrayed you."
                show tali doubt at left
                show serok reason at right
                serok "I know talent when I see it. Can't deny his skills or his ability to get shit done."
                show serok stand at right
                serok "I should have known this'd happen and shot him in his sleep. What an asshole."
            "Where is Zeltan?" if zeltanhide:
                show serok talk at right
                serok "Last time I saw him he was acting weird. Darted from corner to corner like he lost something."
                show serok stand at right
                serok "When I asked him what's going on, he said nothing and went in the direction of the main engine room."
                show serok reason at right
                serok "You know what happened to him?"
                show tali shame at left
                show serok smoke at right
                tali "Well... not really. Just wanted to buy some stuff."
                show serok stand at right
                serok "I see. If you see him, tell him to get back to his post!"
                $ zeltanengine = True
                $ zeltanhide = False
            "Zeltan didn't tell you anything... did he?" if z3:
                $ z3 = False
                show serok stand at right
                show tali shame at left
                serok "I guess you're talking about how you had sex with him. I'm not sure there's anyone left who doesn't know."
                show serok smoke at right
                tali "Keelah... what a shame."
                show serok reason at right
                serok "You're walking through a ship full of sex addicted beasts and you care that much about it?"
                show tali doubt at left
                show serok talk at right
                serok "Relax girl. Everyone will forget about it in a day or two."
                show serok smoke at right
                show tali talk at left
                tali "You talk so calmly about it. You don't care when your crew do something like that?"
                show serok stand at right
                serok "Like what? Having sex? I understand everyone needs to relieve stress sometimes. We're all here in a difficult situation."
                show tali doubt at left
                serok "You think I don't know Jesora goes on wild fuck fests with the vorcha? Unless it affects her duties, I don't care."
                show serok reason at right
                serok "Zeltan left his post - That bothers me. And I will punish him for it."
                show serok stand at right
                serok "Anyway he is so happy that won't notice it. Good for me. And thanks to you, girl."
            "Later.":
                jump bay2_bar
        jump serok_bar

    label elkorbar:
        scene bg bar3
        show tali doubt at left
        show zeltan stand at right
        if elkorFirst:
            $ elkorFirst = False
            show zeltan stand at right
            with dis
            show tali angry at left
            tali "What the hell is that?!"
            zeltan "Curious. Have you never seen an elcor before?"
            show tali talk at left
            tali "I'm talking about that thing on your back! I'm sure you don't use it to paint walls with!"
            zeltan "Brutal joke. Only if the paint was the blood of my enemies. Ha. Ha. Ha."
            show tali facepalm at left
            tali "Oh Keelah. Ass-hungry apes, asari with dicks, battle elcor with a sense of humor... What else will I run into?"
            zeltan "Obscene joke. Hey baby. I can protect your ass from apes and make it not so hungry. Ha. Ha. Ha."
            tali "...Sometimes I wish I'd blown up with my ship."
        if zeltanhappy:
            $ zeltanhappy = False
            zeltan "Confidently. Hey babe. Come to say hello to your greatest lover?"
            tali "I assume your jokes will be even worse from now. Does everyone know?"
            zeltan "Defensively. Don't judge me too much. It was the most fascinating moment in my life. I can not wait for next time."
            tali "That's cute. But I'm not sure about 'next time'. Can't you keep your mouth shut?"
            zeltan "Naughtily. It is just a matter of time before you succumb to my charms again."
            show tali facepalm at left
            tali "Oh Keelah, I already regret about what happened."
        show tali doubt at left
        menu elkor_bar:
            "Jesora said we can do business.":
                zeltan "Double meaning statement. Exactly. Come closer and check my big business, little lady."
                show tali facepalm at left
                tali "Oh gods, give me strength..."
                show tali doubt at left
                label elkorshopmenu:
                    show zeltan stand at right
                    show screen partsshop
                    menu elkorshop:
                        "Ammo (x3) - 3 tech parts" if parts > 2:
                            $ parts -= 3
                            $ ammo += 3
                        "Grenade - 10 tech parts" if parts > 9:
                            $ parts -= 10
                            $ grenades += 1
                        "Tranquilizer dart - 5 tech parts" if parts > 4:
                            if dartfirst:
                                $ dartfirst = False
                                show tali talk at left
                                tali "Tranquilizer dart? Am I seriously supposed to use this?"
                                show tali doubt at left
                                zeltan "Pleased. Glad you noticed it. We found crates of the stuff here on the ship."
                                zeltan "Reasonable assumption. We think the local crew used it to keep the monsters calm. We use other applications. Makes beasts less aggressive. Less dangerous. Easier targets."
                                tali "Hmm. Interesting... i can use it also... for safe reasons."
                                zeltan "Interesting clarification. The substance in the dart also works as a disinfectant. It helps to prevent disease from spreading around. Inquisitive theory. The serum makes beasts docile. The liquid itself could have been used as an ointment. Two purposes, one product."
                                show tali talk at left
                                tali "Yeah, sure, interesting, so the darts? They're primed for use?"
                                zeltan "Obscene joke. You can try it on me, but I can swear to you that nothing will stop the untamed beast within from making you happy. Ha. Ha. Ha."
                                show tali doubt at left
                                tali "Just. Stop. Please. Back to business."
                                jump elkorshopmenu
                            $ parts -= 5
                            $ darts += 1
                        "Thats all for now":
                            hide screen partsshop
                            jump bay2_bar
                    jump elkorshop
            "What is that on your back?":
                zeltan "Proud statement. This is the battle platform 'Lowrider MK8' as used by the esteemed elcor combatants in their fight against tyranny."
                show tali talk at left
                tali "So why are you carrying it?"
                zeltan "Amazement. Our ship is under constant threat of monsters. Serok ordered me to protect this place and our supplies."
                tali "Well, alright. Just try not to poke my face with that long barrel or..."
                show tali angry at left
                tali "Wait, no! That's not what I wanted to say! Elcor, don't you dare-"
                zeltan "Filthy hint..."
                show tali facepalm at left
                tali "..."
                zeltan "I always have a charged gun ready for poking you hard, hot mama. Ha. Ha. Ha."
                tali "I guess I deserve it."
            "I should go.":
                jump bay2_bar
        jump elkorbar


    label nyunbar:
        scene bg bar2
        show tali doubt at left
        if nyunfirst:
            $ nyunfirst = False
            show nyun talk at right
            nyun "Hello, flower. You're that clever quarian girl helping Jesora fix the ship? Have a seat, order whatever you want."
            show nyun stand at right
            show tali talk at left
            tali "Ugh, thanks. I'm sorry, have we met?"
            show tali doubt at left
            show nyun talk at right
            nyun "Call me Nyun, your best friend and gossip hoarder."
        show nyun stand at right
        if z4:
            $ z4 = False
            show nyun smile at right
            nyun "So... i was right. You love to be impaled on a huge elcor cock."
            show tali facepalm
            tali "Never thought that elcors could talk so much."
            nyun "Don't judge yourself harshly, sweetie. Just don't forget to invite me next time."
            show nyun stand at right
            show tali angry at left
            tali "Are you serious?!"
            show nyun curvy at right
            nyun "Oh dear, i always serious concerning... big dicks."
            show tali facepalm at left
            tali "Keelah..."
            jump bay2_bar
        nyun "What're your plans for today, child of the Flotilla?"
        menu nyun_bar:
            "How did you get here?":
                show nyun talk at right
                nyun "Oh, I was a dancer on Omega. Jesora suggested I go with them. I always wanted to leave night club and go on a road full of adventures."
                show tali talk at left
                tali "Omega? Do you know Aria?"
                show nyun doubt at right
                nyun "Of course I do. Who wouldn't on Omega? That bitch is as crazy as she is dangerous. I did my best to avoid meeting her in person."
                tali "You aren't the only one."
            "Free drinks?":
                show nyun smile at right
                nyun "Of course. Serok told me to give you access to all of our reserves. You are our little helper after all."
                show nyun stand at right
                tali "At least my hard work's earned me SOME rewards."
                nyun "Enjoy."
            "I'd like a drink.":
                show nyun smile at right
                nyun "Sure, hun. Be my guest."
                menu bardrinks:
                    "Regular drinks.":
                        $ barcount += 1
                        scene black
                        with dis
                        "After some hours..."
                        if barcount > 2 and zeltansex == False:
                            $ barcount = 0
                            scene bg bar2
                            show tali angry at left
                            show nyun stand at right
                            tali "And I found porn... hic... on the extranet... like three krogans fucking a human girl. I swear she ABSOLUTELY looked like Miranda... hic."
                            show nyun talk at right
                            nyun "Oh darling. I think you've had too much today."
                            show tali talk at left
                            tali "No, no... you listen... hic. I came in her cabin like 'hey... look what I found!'"
                            show tali angry at left
                            tali "And you know what? Hic! This bitch just snatched the datapad from my hands and broke it with her bionics... hic. Fuckin whore..."
                            show nyun smile at right
                            nyun "...Wanna try it?"
                            show tali talk at left
                            tali "Wanna try what? Hic!"
                            nyun "Three krogan?"
                            show nyun stand at right
                            show tali angry at left
                            tali "No! No..."
                            show tali doubt at left
                            tali "Maybe... hic."
                            show nyun talk at right
                            nyun "Alright sweetie, I need to find someone to escort you to your medbay."
                            show tali angry at left
                            tali "I..I'm good... i have a gun, see! Oh, where is it...?"
                            show nyun smile at right
                            nyun "Just stay here, give me a minute"
                            scene black
                            pause 1
                            scene bg bar2
                            show tali doubt at left
                            show zeltan stand at right
                            zeltan "Indulgently. Little quarian girl needs big guy protection on the way home."
                            tali "Huh? Oh... You again. Hic."
                            zeltan "Naughtily. Just walk ahead so I can watch your sweet ass all the way through. Ha. Ha. Ha."
                            tali "I think... hic, even now this qurian's not drunk enough for your jokes, Zeltan."
                            scene black
                            play sound "audio/walk.mp3"
                            pause 1
                            scene bg med3
                            show tali doubt at left
                            show zeltan stand at right
                            tali "Here we go. Try not to break anything with your... body."
                            zeltan "Smugly. The only thing I want to break is your will to resist my sexy body. Ha. Ha. Ha."
                            tali "Sure... hic."
                            zeltan "Seriously. Now I need go back to my duty."
                            zeltan "Hintingly. Maybe next time I could stay for coffee? Ha. Ha. Ha."
                            menu zeltan1:
                                "Tease him.":
                                    $ zeltansex = True
                                    jump zeltanmed1
                                "Let him go.":
                                    jump rest
                        scene bg bar2
                        show tali angry at left
                        show nyun stand at right
                        tali "Damn door... hic... didn't want to open... And he fucked my ass! Yeah... like that... grabbed his stupid dick and push inside my ass... hic."
                        show nyun curvy at right
                        nyun "How devious! And so... exciting. How many monsters did you meet on your way?"
                        show tali talk at left
                        tali "TOO. DAMN. MANY! And you know what? Every time they want to fuck me! Hic... I've never seen so much dick in my whole life... and I've used the extranet for over half of it!"
                        nyun "Mmmm. I hope you'll be able to tame a couple... sometime."
                        show tali angry at left
                        tali "AND SIZES! Oh keelah, sometimes... hic... d-dont't tell anyone... I think about taking... you know... two at the same time... like they bump into each other from both ends... somewhere inside me."
                        show nyun smile at right
                        nyun "Oh my dear, you are so depraved when you're drunk, haha."
                        tali "No, no, no...hic. I don't want them to fuck me... that bad... I'm just thinking. Hypo-somethingcal. Like how it could feel."
                        show nyun talk at right
                        nyun "Alright sweetie. I think you've had enough for today, hah. I will ask someone to walk you back to your medbay."
                        $ barvar = True
                        scene black
                        with dis
                        jump rest
                    "Space cow milk (-10 lewd)":
                        tali "It has a... strange taste."
                        $ lewd -= 10
                        jump nyun_bar
            "You saw Zeltan?" if zeltanhide:
                show nyun talk at right
                nyun "I thought he is still with you. Did you two have a good time in the medbay together?"
                show tali angry at left
                tali "What do you think we did in there?!"
                show nyun smile at right
                nyun "Oh I don't know, but if he vanished he definitely didn't come back here. He disappeared right after your last booze. What a coincidence."
                show tali doubt at left
                tali "So what? Just... get that lustful smile off your face."
            "See you next time.":
                jump bay2_bar
        jump nyun_bar


    label zeltanmed1:
        $ lewd += 3
        $ zeltanhide = True
        $ barelkor = False
        scene bg med3
        show tali talk at left
        show zeltan stand at right
        tali "You know what? Fine. Lets see what you're all about."
        zeltan "Awkwardly. You drank too much, cute girl. I can't understand what you saying. Ha. Ha. Ha."
        show tali doubt at left
        tali "You heard me, big guy. I'm drunk and I'm curious. Isn't that what you wanted? Show me everything you've got down there."
        zeltan "Nervously. What... What am I supposed to do? Maybe I should go."
        show tali angry at left
        tali "Are you fucking serious right now?!"
        zeltan "Timidly. Do you want to come closer? I didn't think I'd actually make it this far."
        show tali doubt at left
        tali "Hey, this is not the time for your stupid jokes! Let me see what I'm working with."
        scene bg medelcor8 with hpunch
        play sound "audio/punch.mp3"
        tali "Shouldn't this thing be bigger?"
        zeltan "Concerned. Please don't be rude. I am very sensitive right now."
        scene black
        show medelcor1
        $ renpy.pause ()
        scene bg medelcor8
        tali "Are you kidding me? You aren't even hard!"
        zeltan "Defensively. My mother raised a gentleman."
        tali "Oh keelah, fine. Let me try another way."
        scene black
        show medelcor2
        $ renpy.pause ()
        tali "I don't get it, are you even feeling anything? I'm trying really hard here..."
        zeltan "..."
        scene black
        show medelcor3
        $ renpy.pause ()
        tali "Come on... I want this cock hard. Hey, are you sleeping up there?!"
        scene black
        show medelcorcum1
        $ renpy.pause ()
        scene bg med3
        show tali angry at left
        show zeltan stand at right
        tali "Fuck, what was that?! Is it so hard to warn me, you idiot?!"
        zeltan "Panicking. I need to go!"
        play sound "audio/run.ogg"
        hide zeltan stand
        show tali doubt at left
        tali "Great. What a mess..."
        jump MedBayUsual

    label zeltanmed2:
        $ lewd += 3
        scene bg med3
        show tali doubt at left
        show zeltan stand at right
        zeltan "Timidly. So, here it is. I will try to do my best."
        show tali talk at left
        tali "Just relax. Tali will take care of you."
        scene bg medelcor1
        tali "Alright. Where did we stop last time?"
        zeltan "Shyly. So... what happens next? What you want me to do?"
        tali "Don't worry, I'll make your first time special. Trust me."
        scene bg medelcor2
        tali "Let me put it... here."
        scene bg medelcor3
        tali "Mmm... yes, such a thick gun deserves nice care."
        scene black
        show medelcor4
        pause 7
        zeltan "Excited. I feel... so warm down there. Like my dick is submerged in a hot bath."
        tali "Hmmmrgghh..."
        scene bg medelcor4
        tali "Finally! A nice hard cock for the only quarian on the ship... Are you happy now, Zeltan?"
        scene bg medelcor5
        zeltan "Horny. I guess... I am ready. Why have you brought a chair?"
        tali "Preparing myself for a wild ride..."
        scene black
        show medelcor6
        pause 2.6
        tali "Ah, nice... Here we go."
        scene black
        show medelcor5
        $ renpy.pause ()
        scene bg medelcor6
        tali "Mmmm... this cock fills up my tight hole completely..."
        zeltan "Sensitive. I believe I've fallen in love."
        scene bg medelcor7
        tali "Can you just shut up and fuck me already?! Start moving your hips, don't just stand there like a statue."
        zeltan "Confused. Yes... Sure, as you wish. Let me try..."
        scene black
        show medelcor7
        $ renpy.pause ()
        tali "Mmmph... Ah.... Yes... So good. Keep it up... g-good elcor... fuck me harder."
        zeltan "Grateful. I'm so glad I met you, Tali. Every other girl has always turned me down..."
        scene bg medelcor7
        tali "Hey, knock that shit off! If you have to talk, say something dirty at least."
        zeltan "Confused. Alright... You're so... bad. Dirty quarian... let me have sex with you."
        tali "Oh Keelah, where did that obscene Zeltan from the bar go? Just repeat 'you little quarian bitch, I will make you my cock slut and use your tiny body like my personal dick strap'"
        zeltan "Embarrassed. You're very pushy. I never expected such a good girl to say that."
        tali "Then stop talking and push your cock deeper inside my pussy!"
        scene black
        show medelcor7alt
        $ renpy.pause ()
        scene bg medelcor9
        tali "Aaaahhh, yes! I'm cumming! Keelah!"
        scene black
        show medelcorcum3
        $ renpy.pause ()
        scene black
        show medelcorcum2
        $ renpy.pause ()
        scene bg med3
        show tali doubt at left
        show zeltan stand at right
        tali "See? That wasn't bad at all. But you need more practice."
        zeltan "Happy. It was so amazing. Finally, I've had sex with real girl. I have to tell everyone about this. Mommy's little boy became a man!"
        show tali angry at left
        tali "Wha... No, wait!"
        hide zeltan stand
        play sound "audio/run.ogg"
        pause 1
        show tali facepalm at left
        $ zeltanhappy = True
        $ z1 = True
        $ z2 = True
        $ z3 = True
        $ z4 = True
        $ barelkor = True
        tali "Oh Keelah..."
        jump MedBayUsual








    label bar_first:
        $ days = 2
        $ barfirst = False
        scene bg hangar
        show tali doubt at left
        with dis
        tali "Hello? Jesora? Serok?! Where the hell are-"
        show vor1 stand at right
        play sound "audio/funmoan.mp3"
        pause 1
        show tali angry at left
        tali "You're not either of them you idiot! Ugh. Where's your boss?"
        show tali doubt at left
        vorcha "Seeerrrok... on the ship. Go."
        tali "Wow. You don't say. Alright then."
        scene black
        play sound "audio/walk.mp3"
        pause 1
        scene bg shipinside
        with dis
        show tali angry at left
        tali "Hello?! Serok?! Anyone..."
        show tali doubt at left
        show serok talk at right
        with dis
        serok "Why so loud, girl? Are you trying to get all the monsters to come down on us as a horde?"
        show serok stand at right
        show tali talk at left
        tali "You said I should talk with Jesora. Well here I am. Is she in her cabin?"
        show tali doubt at left
        show serok reason at right
        serok "It's coffee time right now, most of crew is resting, except the sentries."
        show serok stand at right
        serok "Hmm. Follow me. I'll show you something."
        scene black
        play sound "audio/walk.mp3"
        pause 2
        scene bg bar1
        with dis
        show serok smoke at right
        show tali angry at left
        tali "What? You have a real bar here and I didn't know about it?!"
        show tali doubt at left
        show serok stand at right
        serok "Used to be full of ammo crates, sweet cheeks. About halfway down we decided to stop being sober and miserable and start being drunk and miserable. Not my first call but thanks to Gral I had to cave to SOME demands from the crew to keep them loyal."
        show serok smoke at right
        show tali talk at left
        tali "That's... somehow the best and worst idea at the same time for the situation."
        show serok reason at right
        serok "Yeah, Serok and Sons Taphouse! Feel free to empty my pockets with the free drinks!"
        show tali doubt at left
        show serok smoke at right
        tali "Don't tell me you actually have some sons."
        show serok talk at right
        serok "Who the hell knows? This guy's been to so many starports and met so many fine women, anything's possible."
        show serok reason at right
        serok "...Quarians included."
        show tali facepalm at left
        show serok smoke at right
        tali "Free drinks... just think of free drinks..."
        show serok stand at right
        serok "He-he. No need to be rude with old pirate, girl."
        show serok reason at right
        show tali doubt at left
        serok "Anyway. Enjoy my hospitality! I saw Jesora at the counter, and don't be a stranger. You might make a few friends here. Or 'friends' if you now what I mean, heh."
        jump bay2_bar




    label bay2_Serok:
        scene bg hangar
        with dis
        show serok stand at right
        with dis
        show tali doubt at left
        with dis
        serok "Hey cutie. Found my crew yet?"
        show tali talk at left
    label seroktalkmenu:
        show tali doubt at left
        show serok stand at right
        menu seroktalk:
            "Do you always smoke?" :
                serok "Yup. Makes me look more professional when making deals."
                show serok smoke at right
                show tali talk at left
                tali "Aren't you worried about your health? Or, wait, I think you have two pairs of lungs?"
                show tali doubt at left
                show serok reason at right
                serok "I liberate scrap and salvage warships before governments or companies can collect what they lost. On a good day I get shot at twice. Smoking is the LAST thing that will kill me."
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
                serok "Jesora and her commandos were scrubbed by Thessia after a botched job. Something about a Spectre. It was a suicide mission at best and the ones who didn't die scrambled back to a government that wanted nothing to do with them. They were declared AWOL to save the asari government any accountability."
                show serok talk at right
                serok "Calling it messy is a disservice. It was fucking terrible. Their 'trial' was set shortly after they met up with their 'pickup'. Poor girl didn't have an ounce of a will to live after, but I guess saving her team meant more to her than saving herself. And what would you know, a dashing captain and his ship just hapened to be nearby to help her escape."
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
        serok "Hi, cutie. What's up?"
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
                serok "Jesora and her commandos were scrubbed by Thessia after a botched job. Something about a Spectre. It was a suicide mission at best. When shit went south, she and her team were declared AWOL."
                show serok talk at right
                serok "Calling it messy is a disservice. Their trial was set shortly after. She sounded ready to die, but I guess saving her team and seeing my ship nearby gave her the push she needed to save their lives."
            "Where did you get this ship?" :
                serok "I borrowed it from my old boss."
                show tali talk at left
                tali "Oh. Well he must really like you to let you do that."
                show tali doubt at left
                serok "You bet. He's dead."
                tali "Uhm. Okay then."
            "Where is Jesora?":
                show serok reason at right
                serok "She should be in her cabin. You can go check anytime if you want to talk."
                menu jesora_cabin:
                    "Sure.":
                        jump jesoraCabin
                    "Another time maybe.":
                        jump seroktalkmenuact3
            "I should go." :
                jump map
        jump seroktalkmenuact3

    label jesoraCabin:
        if days % 2 == 0:
            scene bg jesorascene3
            tali "No one is home..."
            if poolQuest:
                jump bay2_vorcha
            else:
                jump bay2_SerokAct3
        else:
            scene bg jesorascene1
            with dis
            tali "Hmm. This looks like the right way."
            scene bg jesorascene2
            tali "Someone left the door open..."
            menu cabincheck:
                "Take a look(activate futa content)":
                    scene bg jesorascene3
                    tali "Keelah, a real bed! I never thought I'd miss a mattress so much."
                    play sound "audio/shower.mp3"
                    tali "Oh? The shower's in use. I think they're about done?"
                    scene bg jesorascene4
                    with dis
                    play sound "audio/doorslide.mp3"
                    pause 2
                    scene bg jesorascene5
                    tali "I should probably come back at a better time."
                    scene bg jesorascene6
                    tali "Oh. Oh Keelah, what a cock."
                    scene bg jesorascene3
                    show tali shame at left
                    show jesora naketalk at right
                    jesora "Hey, suitgirl. You wandering around?"
                    show jesora nakestand at right
                    tali "Uhm, hello Jesora. Just... yeah, looking for something..."
                    show jesora naketalk at right
                    jesora "You're not going to steal anything, right? Saw something interesting?"
                    show tali talk at left
                    show jesora nakestand
                    tali "Yes... I mean, no... Listen, can you put on some clothes?"
                    show tali doubt at left
                    show jesora naketalk at right
                    jesora "Hmm. You're cute when you're flustered, haha. But alright, give me a second."
                    play sound "audio/dress.mp3"
                    pause 2
                    show jesora toweltalk at right
                    jesora "Better?"
                    show jesora towelstand at right
                    show tali shame at left
                    tali "That's not what I... well anyway..."
                    show jesora toweltalk at right
                    jesora "You've come at a good time, suitgirl. I've been meaning to invite you for a drink for saving my skin."
                    show jesora towelstand at right
                    show tali talk at left
                    tali "Me? Well I didn't... I mean, are you sure that now is...?"
                    show tali doubt at left
                    show jesora toweltalk at right
                    jesora "I can see that blush from here, hah! Come over and sit, I'll pour you a glass in a moment."
                    hide jesora
                    tali "Well, I guess I can stay for a bit."
                    scene black
                    "Fortunately for Tali Jesora had a reserve of alcohol built almost specifically for her kind. Some time passed and one drink became many..."
                    scene bg jesorascene7
                    tali "And I told him like 'You have to be kidding! I can't put that in my mouth!' Hic!"
                    scene bg jesorascene8
                    jesora "Damn, really? Was he offended?"
                    scene bg jesorascene9
                    tali "Y-Yeah... hic... he didn't say anything and then just didn't take me on next mission..."
                    scene bg jesorascene7
                    jesora "No way."
                    tali "Yes way. He took that guy... Jacon? Jasob? Poor guy was so happy to go at least anywhere. Hic!"
                    scene bg jesorascene10
                    with dis
                    tali "Wha... hic... what you doing?"
                    jesora "I figured my fellow crewmate wouldn't mind me getting just a little closer."
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
                        "Jesora's POV":
                            jump jesorascene_pov1
                        "Tali's POV":
                            jump jesorascene_pov2
                "Better not bother her.":
                    if poolQuest:
                        jump bay2_vorcha
                    else:
                        jump bay2_SerokAct3



    label jesorascene_pov1:
        scene black
        show jesora1_loop1
        $ renpy.pause ()
        scene black
        show jesora1_trans1
        $ renpy.pause ()
        scene bg jesorapov1
        jesora "Just like any other quarian. So submissive. So obedient. I'll enjoy fucking that pretty face of yours."
        scene black
        show jesora1_trans2
        $ renpy.pause ()
        scene black
        show jesora1_loop2
        $ renpy.pause ()
        scene bg jesorapov2
        jesora "Mmm. You have such a sweet mouth... let's go deeper."
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
        jesora "The perfect prize for a perfect cocksucker, wouldn't you agree? Your face looks so filthy with that cum... but you aren't complete without it are you?"
        jump jesorasceneafter

    label jesorascene_pov2:
        scene black
        show tali1_loop1
        $ renpy.pause ()
        scene black
        show tali1_trans1
        $ renpy.pause ()
        scene bg talipov1
        jesora "Mmm. You quarian girls are always something else, aren't you? Go on then Tali. Follow your instincts. Open your mouth for my cock. Open wide... and say 'aaaaah.'"
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
        jesora "Oh, look at you. You are far more experienced than I expected, even for that story. Maybe you've been a bad girl before now... or maybe you've gotten a little too friendly with the locals. No matter. Let's stretch your quarian throat a bit."
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
        tali "Mnnph... No... Let me go..."
        scene bg jesorascene14
        tali "Ugh, what? Where am I?"
        scene bg jesorascene3
        show tali shame69 at left
        show jesora smiletalk at right
        jesora "Hello there, little boozer. Someone overdid it yesterday. Need something for the headache?"
        show jesora smile at right
        show tali talk69 at left
        tali "No thanks, I should be alright. Let me just... Oh Keelah, half a twelve hours? I don't remember half a day. What happened?"
        show tali doubt69 at left
        show jesora talk at right
        jesora "You drank and passed out on the couch. Maybe that alcohol was too strong for you. You should have seen your face, haha. I put you on the bed."
        show jesora smile at right
        tali "Mmn. Something tastes strange in my mouth..."
        show jesora smiletalk at right
        jesora "Yeah, its a special asari liquor which I treated you yesterday. Very limited edition alcohol."
        show jesora stand at right
        show tali talk69 at left
        tali "I see. Alright, well thanks for looking after me Jesora. I'd better return to the medbay and start looking for more parts."
        jesora "Sure. Anytime, cutie."
        scene black
        play sound "audio/walk.mp3"
        "Unable to stop licking her teeth, Tali returned to medbay."
        jump MedBayUsual


    label jesorashopmenu:
        show jesora stand at right
        show screen partsshop
        menu jesorashop:
            "Ammo (x3) - 3 tech parts" if parts > 2:
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
        text "Tech parts remaining: [parts]" xpos 0.4 ypos 0.1

    label corridor2:
        scene bg cor2walk
        play sound "audio/walk.mp3"
        "Carefully watching her steps, Tali walks down the hallway to the warehouse..."
        if corridor_fight:
            $ enemyID = 2
            play sound "audio/roar.mp3"
            scene bg cor2
            show tali gunshoot at left
            show varren stand at right
            with dis
            "Smelling prey, a varren attacks!"
            $ fuckpose = renpy.random.randint(1, 2)
            $ enemyhp = 5
            jump sliderBattleFuck2
        else:
            "The way was clear."
            jump warehouse

    label corridor3:
        scene bg poolcor1
        play sound "audio/walk.mp3"
        "Carefully watching her steps, Tali walks down the hallway to the pool..."
        if corridor_fight:
            $ enemyID = 3
            play sound "audio/frog2.mp3"
            scene bg poolcor
            show tali gunshoot at left
            show lizard stand at right
            with dis
            "Enemy attacks!"
            $ fuckpose = renpy.random.randint(1, 2)
            $ enemyhp = 5
            jump sliderBattleFuck3
        else:
            "The way was clear."
            jump pool

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
        tali "I need to be careful!"
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
        tali "I don't remeber this thing being here. It looks like a thermal stabilizer, but I need to look closer."
        menu whEv:
            "Look closer":
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
                tali "AGH! Stop doing that!"
                play sound "audio/tier.mp3"
                pause 1
                play sound "audio/creepone.mp3"
                pause 2
                show whAnimation
                tali "Why do they love to fuck my ass so mu-uagh! H-Haghn!"
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
                tali "No! Just... look, I was stuck, okay? There's-!"
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
        tali "Hmmm... maybe."
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
        "With 'at least you tried' energy, the vorcha left."
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
        tali "That's a ventilation hatch. Hmm. It's quite wide. I think I can use it if I can find a way to get up there."
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
            "Sensing a female, a creature springs out!"
            $ fuckpose = renpy.random.randint(1, 2)
            $ enemyhp = 5
            jump sliderBattleFuck1
        else:
            "The way was clear."
            jump engine

    label engine:
        if zeltanengine:
            $ zeltanengine = False
            $ zeltanhallway = True
            scene bg engine
            show tali doubt at left
            show zeltan stand at right
            tali "Zeltan! That's where you were!"
            zeltan "Sadly. Can you just leave me alone?"
            show tali angry at left
            tali "What the hell is going on with you?! Why did you leave the ship?"
            zeltan "Ashamed. There is no place for me there any more. I dishonor my ancestors."
            show tali facepalm at left
            tali "Keelah, I know I'll regret it but..."
            show tali talk at left
            tali "What you talking about?"
            zeltan "Touchy. I see you're still laughing at me. Please just go away."
            show tali doubt at left
            tali "Is this about what happened in the medbay? Are you worried about that?"
            zeltan "Depressively. Don't remind me. Now all other elcor will make fun of me. Because I couldn't satisfy a woman."
            show tali talk at left
            tali "Ah... Listen, it happens sometimes. It's no big deal right? Is this the first time it's happened to you?"
            zeltan "..."
            tali "First time... with a quarian?"
            zeltan "Unconfidently. Perhaps."
            tali "Wait, you can't... Are you a virgin?!"
            hide zeltan stand
            play sound "audio/run.ogg"
            pause 1
            show tali angry at left
            tali "Oh come on! What did I say wrong this time?!"
            scene bg map
            show tali doubt at left
            tali "Where'd he go?"
            jump map
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
        tali "How old is this thing? Some of the software hasn't been patched in a long time... but some of it is new as well? It's like some throwaway test cruiser the owners check on every other decade!"
        tali "The engines are working on secondary support. I'm lucky it works at all. Thermal stabilizers are functional. No way I can use it though. The rest of the ship would fall apart without it."

        jump engine
    label med:
        "This is the medbay"
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
            tali "I swallowed too much... I have to go to the medbay urgently."
            jump medbayafterdefeat

    label corridor1scene2:
        scene bg cor1back1
        tali "Almost... got my gun!"
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
        tali "Ngh?! Stop! What are you doing back there?!"
        scene bg cor1
        show cor1backnextstage2
        pause 2
        tali "Aaaa! Your cock is... inside me! Keelah it's so thick!"
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
        tali "Why did that feel so... goood...?"
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
            tali "So much cum. They probably fuck anything until they find a girl like me. Keelah, they must have gallons prepared. I need to find my helmet."
            scene black
            play sound "audio/walk.mp3"
            "Tali continued on her way......"
            jump warehouse
        else :
            tali "I swallowed too much... I have to go to the medbay urgently."
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
            "Tali continued on her way......"
            jump warehouse
        else :
            tali "My body is on fire... I'd better rush to the medbay."
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
            "Tali continued on her way......"
            jump warehouse
        else :
            tali "My body is on fire... I'd better rush to the medbay."
            jump medbayafterdefeat

    label com_biggy:
        $ enemyID = 1
        $ encounter = False
        scene black
        play sound "audio/roar.mp3"
        scene bg comscene1
        with dis
        tali "What? Where did he come from?!"
        scene bg comscene2
        play sound "audio/gorillaroar.wav"
        tali "Damn it, he's blocking the way out! I'll have to take care of him first!"
        scene bg comtutorial3
        "Looks like you've attracted some unwanted attention. Fighting will be handled through a simple mini-game the players can interact with."
        "A slider in the bottom-center will show the distance between Tali and the enemy. You have a limited window of opportunity before they're too close for her to stop them."
        "Above the slider there are buttons which provide a number of options available to you. Depending on your inventory you can shoot your opponent, bomb them, or try to escape."
        "Each action has a chance to fail. Enemy stats vary according to their own difficulty level. All stats afterwards are generally random. Notice: Shooting an enemy and especially the use of explosives will increase your alarm level."
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
                tali "You again? Looks like last time wasn't enough!"
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
            if crewQuest:
                $ random = renpy.random.randint(1, 100)
                if random > 60:
                    jump comRoomAnal
                else:
                    jump comRoomBJ2
            elif act3:
                $ random = renpy.random.randint(1, 3)
                if random == 1:
                    jump comRoomAnal
                elif random == 2:
                    jump comRoomBJ2
                else:
                    jump comRoomMis1
            else:
                jump comRoomBJ2

    label comRoomMis1:
        $ random = renpy.random.randint(1, 2)
        $ lewd += 1
        scene black
        scene black
        with dis
        play sound "audio/roar.mp3"
        creature "Aggrrrrr"
        scene bg comscene3
        tali "That's... a tight grip!"
        scene bg comscene4
        play sound "audio/gorillaroar.wav"
        pause 2
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 2
        scene bg comscene4
        if lewd > 20:
            tali "Ah! Please stop slapping my ass!"
        else:
            tali "Stop that you bosh'tet!"
        pause 2
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 1
        scene black
        pause 1
        play sound "audio/tier.mp3"
        if lewd > 20:
            tali "W-What are you thinking...?"
        else:
            tali "What? Hey, no, stop!!"
        scene black
        show commis1
        $ renpy.pause ()
        scene bg commis1
        if lewd > 30:
            tali "GLMPHH!! H-HNNGPHH!! MNGKK!!"
        elif lewd > 20:
            tali "M-MMPH!! GLMMGHHPH!! KMMNGGHH!!"
        else:
            tali "SHLLUUURRRPT!! THLLUUURRRPPT!! HUUUAAAAK!!"
        scene black
        show commis2
        $ renpy.pause ()
        if lewd > 30:
            if random == 1:
                scene black
                show commis3
                $ renpy.pause ()
                scene bg commis2
                tali "I wish this was another fat ape cock!"
                scene black
                show commis4
                pause 1
                scene black
                show commis5
                $ renpy.pause ()
                scene bg commis3
                tali "Won't you fuck my tight little throat? You know what I want... give it to me, you boshtet..."
                scene black
                show commis11
                $ renpy.pause ()
                scene bg commis4
                tali "I want that whole... slimy... dick."
                scene black
                show commis13
                pause 2
                tali "Oh, no rush, big boy... my tight quarian throat isn't ready for such a fat cock... lets stretch it a first..."
                scene black
                show commis13alt
                pause 2
                tali "F-Finally. Please use my face to stroke off your cock."
                scene black
                show commis14
                $ renpy.pause ()
                scene bg commis5
                tali "Give me your cum daddy. Fill my mouth with that hot, sticky load!"
                scene black
                show commis15
                $ renpy.pause ()
            else:
                scene black
                show commis6
                pause 2
                tali "A-Ah. You want it rough? Go ahead... fuck me."
                scene black
                show commis9
                $ renpy.pause ()
                scene bg commis6
                tali "Ah! Yes! Fuck me, daddy! I deserve punishment...!"
                scene black
                show commis10
                $ renpy.pause ()
                scene black
                show commis16
                $ renpy.pause ()
            scene bg comroom
            show tali fin3 at left
            with dis
            tali "O-Oh fuck. That was... intense."
            jump medbayafterdefeat
        elif lewd > 20:
            scene black
            show commis6
            pause 2
            tali "Ah... Go ahead you animal. Fuck me harder..."
            scene black
            show commis9
            $ renpy.pause ()
            scene bg commis6
            tali "Yes... Fuck me, daddy... Punish me for thinking I could beat you...!"
            scene black
            show commis10
            $ renpy.pause ()
            scene black
            show commis16
            $ renpy.pause ()
            scene bg comroom
            show tali fin3 at left
            with dis
            tali "Mngh. Keelah. A ball drainer's job is never done, is it?"
            jump medbayafterdefeat
        else:
            play sound "audio/punch.mp3"
            scene bg commis7 with hpunch
            tali "Don't you dare to grab me like this... you monster!"
            scene black
            show commis7
            $ renpy.pause ()
            scene bg commis8
            tali "Augh! Stop! You're fucking me too hard! Please slow down!"
            scene black
            show commis8
            $ renpy.pause ()
            scene black
            show commis16
            $ renpy.pause ()
            scene bg comroom
            show tali fin3 at left
            with dis
            tali "A-Ah... H-Hah... N-Need... to get... to medbay...."
            jump medbayafterdefeat











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
        tali "Stop that you bosh'tet!"
        scene bg comscene6 with hpunch
        play sound "audio/punch.mp3"
        pause 2
        scene bg comscene7 with hpunch
        play sound "audio/punch.mp3"
        tali "Get your hand off! Don't touch that!"
        scene bg comscene8
        play sound "audio/roar.mp3"
        creature "GRAUR"
        scene bg combj1 with hpunch
        play sound "audio/punch.mp3"
        tali "Ngh! K-Keelah, you stink! Shouldn't you have some instinct for bathing?!"
        tali "{i}Keelah, why is it so big? Don't show it you're scared Tali. Like any animal it should lose interest once you-{/i}"
        scene bg combj2
        play sound "audio/gorillaroar.wav"
        tali "NOUGHNMMPHH...?!"
        scene bg combj3
        play sound "audio/wetsquish.mp3"
        creature "GRRRRRGHHHH"
        show biggybjanim
        pause 10
        scene bg combj9
        tali "GUUAAAARRRKK!! SCHLUUUURRRRRPPT!! HUUAAAAKKKPHHHH!!"
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
        tali "It's so bitter. I thought I was going to pass out. Keelah, you stretched my throat just trying to push it down. And the smell of your cum..."
        scene black
        with dis
        creature "..."
        play sound "audio/gorillaroar.wav"
        "Finally satisfied, the creature grunted happily and left Tali alone."
        scene bg comroom
        show tali fin2 at left
        with dis
        if infection < 3:
            tali "Ngh. Great Tali. Now your breath AND your suit smell like cum. Keelah, why does it taste so bitter? I need to find my helmet and wash up at the medbay."
            scene black
            play sound "audio/walk.mp3"
            "Tali continued on her way..."
            jump map
        else :
            tali "I swallowed too much... Must go to medbay urgent."
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
            tali "Again. His cock is down my throat again?!"
        else:
            tali "How is this is happening again? Am I really that weak? His grip is too strong!"
        show biggybjanim
        $ renpy.pause ()
        if lewd > 10:
            scene bg combj9
            tali "It's so nasty. I'll use my tongue and make him cum faster. That should help him unload those nasty, fat balls faster!"
            show biggybjanimnext
            $ renpy.pause ()
            scene bg combjcum1
            play sound "audio/sucking3.ogg"
            tali "Why won't you cum?"
            scene bg combjcum2
            play sound "audio/cumshot1.ogg"
            tali "Oh... Oh no. It's too much. It's too... tthhiicckk!"
            play sound "audio/swallow.ogg"
            pause 1
            play sound "audio/swallow.ogg"
            pause 1
            scene bg combjcum3
            play sound "audio/cumshot2.ogg"
            tali "It's sticking to my throat. Whenever I swallow there's another fat load ready to wash my tongue with his disgusting taste..."
            scene bg combjcum4
            play sound "audio/wetsquish.mp3"
            pause 3
            if lewd > 20:
                scene bg combjcum5alt
                tali "Ngh! Don't underestimate me! I-I'm not afraid of your fat, filthy cock!"
                scene bg combjcum6
                play sound "audio/swallow.ogg"
                pause 2
                scene bg combjcum7
                tali "H-Hahgh. I can taste it. Keelah I can taste every wriggling sperm in that disgusting ape's cock batter. My pussy's so hot... "
                play sound "audio/gorillaroar.wav"
            else:
                scene bg combjcum5
                tali "A-Aaaaaaaaah..."
                play sound "audio/gorillaroar.wav"
            scene bg comroom
            show tali fin2 at left
            # REMOVE TEST
            #jump comRoomAnal
            with dis
            if infection < 3:
                tali "Mnph. He must have cum over a gallon. My antibiotics should help... but I should really find my helmet and return to the medbay."
                scene black
                play sound "audio/walk.mp3"
                "Tali continued on her way..."
                jump map
            else :
                tali "I swallowed too much... I have to go to the medbay urgently."
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
            tali "Your cum is too thick. Ngh, my breath smells like your balls..."
            scene black
            with dis
            creature "..."
            play sound "audio/gorillaroar.wav"
            "Having dumped its load, the creature barked a taunting laugh before leaving Tali alone."
            # REMOVE TEST
            #jump comRoomAnal
            scene bg comroom
            show tali fin2 at left
            with dis
            if infection < 3:
                tali "Keelah, how backed up were you? Ngh. Antibiotics should do the trick but I need to find my helmet or it'll get worse."
                scene black
                play sound "audio/walk.mp3"
                "Tali continued on her way......"
                jump map
            else:
                tali "I swallowed too much... I have to go to the medbay urgently."
                jump medbayafterdefeat

    label comRoomAnal:
        $ lewd += 1
        $ infection += 1
        scene black
        with dis
        play sound "audio/roar.mp3"
        creature "Aggrrrrr"
        scene bg comscene3
        tali "That's... a tight grip!"
        scene bg comscene4
        play sound "audio/gorillaroar.wav"
        pause 2
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 2
        scene bg comscene4
        if lewd > 20:
            tali "Ah! W-Why does that feel so good?!"
        pause 2
        scene bg comscene5 with hpunch
        play sound "audio/slap.mp3"
        pause 1
        if lewd > 20:
            tali "Mmm! Teach me a lesson daddy! I've been a naughty quarian!"
        else:
            tali "Ahg! Stop it!"
        scene bg combj9
        play sound "audio/wetsquish.mp3"
        if lewd > 20:
            tali "Don't worry big boy, Tali knows what you want..."
        else:
            tali "Not again. Keelah, why is your cock this big? It's like it was designed to fuck a woman's face..."
        show biggybjanimnext
        $ renpy.pause ()
        if lewd > 20:
            scene bg comanal1
            play sound "audio/wetsquish.mp3"
            pause 2
            scene bg comanal2
            play sound "audio/lewdkiss.mp3"
            pause 1
            tali "Ahhh. Did you like that? Look! I didn't spill a drop..."
            scene black
            play sound "audio/gorillaroar.wav"
            tali "Mmm... whatever you want..."
            scene bg comanal3
            tali "Oh fuck, that feels so good!"
            show comroomanalfront1
            $ renpy.pause ()
            scene bg comanal3
            show comroomanalback1
            $ renpy.pause ()
            scene bg comanal7 with hpunch
            play sound "audio/punch.mp3"
            tali "Please teach this ignorant girl some manners!"
            scene bg comanal7
            show comroomanalback2
            $ renpy.pause ()
            scene bg comanal4
            play sound "audio/gorillaroar.wav"
            show comroomanalfront2
            $ renpy.pause ()
            scene bg comanal5
            tali "Ah! Oh Keelah you're so deep! Keep using my fat purple ass!"
            show comroomanalback2alt
            $ renpy.pause ()
            scene bg comanal8 with hpunch
            play sound "audio/cumshot2.ogg"
            tali "Fuck! Keep cumming inside me! Oh Keelah, your sperm is so hot!"
            scene bg comanal6 with hpunch
            play sound "audio/cumshot2.ogg"
            pause 2
        else:
            scene bg combjcum1
            play sound "audio/wetsquish.mp3"
            pause 2
            scene bg combj10
            play sound "audio/lewdkiss.mp3"
            tali "C-Cough. It tastes terrible! What gives your kind a need to have cocks this huge?"
            play sound "audio/gorillaroar.wav"
            tali "Why haven't you cummed yet? Don't tell me..."
            scene black
            play sound "audio/tier.mp3"
            tali "No! Don't tear that you bosh'tet!"
            scene bg comanal10
            play sound "audio/gorillaroar.wav"
            tali "Put me down! Augh! Your breath stinks! And what's... no! No! You better not!"
            scene bg comanal7
            tali "I'm being serious! I'm not a quarian-sized sex toy for you mangy beasts! Are you listening?!"
            scene bg comanal8
            play sound "audio/lewdsplat.mp3"
            tali "N-NGHHAAHH!! Big! Too big! Keelah, I can feel him in my stomach!"
            scene bg comanal8
            show comroomanalback2
            $ renpy.pause ()
            scene bg comanal8
            show comroomanalfront2
            $ renpy.pause ()
            scene bg comanal5
            tali "It's stretching me out! Why are you so damn thick you ugly bastard!"
            scene bg comanal5
            show comroomanalback2alt
            $ renpy.pause ()
            scene bg comanal6
            play sound "audio/lewsquish.mp3"
            tali "NGGH!! Cumming! He's cumming so much! Where is it all coming from?!!"
        scene bg comanal6
        show comroomanalcum
        $ renpy.pause ()
        if lewd > 20:
            scene bg comanal9
            play sound "audio/gorillaroar.wav"
            tali "A-Ah... Thank you for that long, hard lesson. I promise I'll be a good girl from now on..."
            scene bg comroom
            show tali fin2 at left
            with dis
            tali "O-Oh. I got carried away there. Keelah, I need to hurry to the medbay."
            jump medbayafterdefeat
        else:
            scene bg comroom
            show tali fin2 at left
            with dis
            tali "My body is on fire... I'd better rush to the medbay."
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
        tali "Stop doing that, you bosh'tet!"
        scene bg comscene6 with hpunch
        play sound "audio/punch.mp3"
        pause 2
        scene bg comscene7 with hpunch
        play sound "audio/punch.mp3"
        tali "Get your hand off! Dont touch that!"
        scene bg comscene8
        play sound "audio/roar.mp3"
        creature "Grrrrrrrrrr"
        scene bg combj1 with hpunch
        play sound "audio/punch.mp3"
        tali "Am I supposed to be impressed? Ugh, stinks! You think I'm afraid of a dick this small?"
        tali "{i}Keelah, it's fumes are making me lightheaded. It's so heavy and sticky too. Calm down Tali, you can-{/i}"
        scene bg combj2
        play sound "audio/gorillaroar.wav"
        tali "HRLMMMPGHH..?!"
        scene bg combj3
        play sound "audio/wetsquish.mp3"
        creature "Ughhrrr"
        show biggybjanim
        pause 10
        scene bg combj9
        tali "SCHLUUURRRPTT!! HAAAUUUKKKGHH AUGGHHHHHKKT!!"
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
        tali "M-My head's spinning. It's so gross... and his cum is so thick..."
        scene black
        with dis
        creature "..."
        play sound "audio/gorillaroar.wav"
        "Happy to have finally found a female, the monster snorts before leaving Tali alone."
        if comEncounter == True:
            jump afterComEvent
        else:
            jump rooms


    label afterComEvent:
        $ comEncounter = False
        scene bg map
        with dis
        show tali shame at left
        tali "Ngh. What a waste. Nothing here but more filthy animals. I need some rest. I think I saw a shower in the medbay? I hope it still works."
        scene black
        with dis
        "Tali returned to the medbay"
        scene bg shower1
        with dis
        play sound "audio/shower.mp3"
        tali "Keelah. Just what I needed..."
        scene bg shower2
        with dis
        "........"
        if firstHelpChoice == False:
            jump showerEvent1
        scene bg shower3
        play sound "audio/heavyshots.mp3"
        tali "Huh? That sounded like the turret going off?"
        scene bg turret4
        with dis
        tali "What a mess. I should thank Jesora the next time I see her. The things these creatures could have done to me..."
        $ engine = True
        $ warehouse = True
        $ barracks = True
        $ quest = "Search for tech parts"
        jump MedBayUsual

    label showerEvent1:
        $ lewd += 1
        scene bg shower3
        play sound "audio/buzzing.mp3"
        tali "What was that?"
        scene bg showerscene1
        play sound "audio/buzzing.mp3"
        tali "Huh?"
        scene bg showerscene2
        play sound "audio/punch.mp3"
        tali "Aaaaa! What is that?!"
        scene black
        play sound "audio/buzzing.mp3"
        tali "Stop! Don't try it!"
        play sound "audio/punch.mp3"
        tali "You little...! What the hell are you doing?!"
        scene bg showerscene3
        tali "Ngh! Its got me tight!"
        scene black
        show showerevent1
        $ renpy.pause ()
        tali "It's licking me?! No. That's not a tongue!"
        scene bg showerscene20
        play sound "audio/lewdsplat.mp3"
        tali "NGH! It's... inside..."
        scene black
        show showerevent2
        $ renpy.pause ()
        scene bg showerscene15
        tali "Why is it so... thick? Keelah, its so fat..."
        play sound "audio/buzzing.mp3"
        scene bg showerscene20
        play sound "audio/lewsquish.mp3"
        creature "BZZzzzZzZZZzz..."
        scene black
        show newshowercum
        $ renpy.pause ()
        tali "A-Aaaaaah..."
        scene black
        play sound "audio/buzzing.mp3"
        "While Tali tried to control herself, the creature escaped without a trace."
        if bugfirst:
            $ bugfirst = False
            scene bg med3
            with dis
            show tali shame at left
            with dis
            tali "That was... unexpected. I cant handle this alone, this ship is crawling with monsters."
            show tali doubt at left
            tali "I need to visit Serok in the hangar bay and ask for cover. He's a sleazebag but my options aren't exactly limitless."
            jump taliNoChoice
        scene bg med3
        show tali shame at left
        tali "Ah... What's happening to me? After this... creature came inside me, my body started trembling and I'm feeling so... excited. Like I started losing control of myself..."
        show tali doubt at left
        tali "Alright Tali, focus. The bug came from somewhere. I need to scan the room and find out where."
        scene black
        play sound "audio/equip.ogg"
        pause 2
        scene bg vent1
        with dis
        tali "Here it is I think. Scans indicate the recent remains of organic materials. Something pried this vent hatch open for some reason."
        tali "Let me see..."
        scene black
        show ventclose
        pause 2
        scene bg vent2
        tali "Ngh! Does anything work on this damn ship? I guess I need some spare parts to fix this hatch."
        $ bugquest = True
        $ sidequest = "Fix vent in medbay(30 tech parts)"
        $ bugsact = False
        jump MedBayUsual

    label showerEvent2:
        $ bugcount = 0
        $ lewd += 1
        if bugscene == 1:
            $ bugscene += 1
            scene bg showerscene2
            play sound "audio/punch.mp3"
            tali "Aaaaaaa! Not them again!"
            scene black
            play sound "audio/buzzing.mp3"
            tali "Stop! Don't do that!"
            scene bg showerscene20
            tali "Ah, no! This can't be happening again...!"
            scene black
            show showerevent2
            $ renpy.pause ()
            play sound "audio/buzzing.mp3"
            tali "Wha... That sound? Are there more of you filthy little pests?"
            scene black
            show showerbug4
            pause 3.5
            tali "Aaaaaaa! No! There's two of them! My ass... Oh Keelah..."
            scene black
            show showerbug1
            $ renpy.pause ()
            scene black
            show showerbugcum1
            pause 4
            "When the creatures cum pumped into Tali's body, she started to feel herself lose control of her own body and mind."
            scene black
            "Grasping at the fleeting remnants of her will, at last she took control of her body, driving away the invasive thoughts of pleasure that tried hard to convince her that becoming breedmeat for bugs was a life she'd love to have."
            "When she finally opened her eyes, there were no insects in sight."
            scene bg med3
            show tali facepalm at left
            with dis
            tali "Oh keelah. There is definitely something wrong with these insects cum. I felt like I was in trance..."
            show tali doubt at left
            tali "Very similar to how Rachni affects their victims. Сould these bugs be bred from their DNA?"
            show tali facepalm at left
            tali "Ahhh, I need to shut that hatch."
            jump MedBayUsual
        elif bugscene == 2:
            scene bg showerscene2
            play sound "audio/punch.mp3"
            tali "Aaaaaaa! Not them again!"
            scene black
            play sound "audio/buzzing.mp3"
            tali "Stop! Don't do that!"
            scene bg showerscene20
            tali "Ah, no! This can't be happening again...!"
            scene black
            show showerevent2
            $ renpy.pause ()
            play sound "audio/buzzing.mp3"
            tali "Wha... That sound? Are there more of you filthy little pests?"
            scene black
            show showerbug4
            pause 3.5
            tali "Aaaaaaa! No! There's two of them! My ass... Oh Keelah..."
            scene black
            show showerbug1
            $ renpy.pause ()
            scene black
            play sound "audio/buzzing.mp3"
            show showerbug5
            pause 3.5
            tali "GLUUGGKKK?!"
            scene black
            show showerbug2
            $ renpy.pause ()
            scene black
            show showerbug3
            $ renpy.pause ()
            scene black
            show showerbugcum2
            $ renpy.pause ()
            tali "Yes... fuck me hard, give me your cum, fill me up."
            scene black
            "Grasping at the fleeting remnants of her will, at last she took control of her body, driving away the invasive thoughts of pleasure that tried hard to convince her that becoming breedmeat for bugs was a life she'd love to have."
            "When she finally opened her eyes, there were no insects in sight."
            scene bg med3
            show tali facepalm at left
            with dis
            tali "Ah... I swallowed too much. These things are taking over my mind. I feel like that's the last time I'll be able to resist."
            show tali facepalm at left
            tali "I have to... I NEED to close this hatch urgently."
            jump MedBayUsual

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
            tali "Not again! Open damn you!"
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
        tali "Ah, he's inside me..."
        scene bg securedoor1
        show doorhackpussyloop1
        $ renpy.pause ()
        scene bg securedoor1
        show doorhackpussyloop2
        tali "Ah oh no, not so fast... wait...!"
        $ renpy.pause ()
        scene bg securedoor1
        show doorhackpussycum
        $ renpy.pause ()
        scene bg securedoor1
        show tali fin1 at left
        with dis
        tali "My body is on fire... I'd better rush to the medbay."
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
                        "Tali successfully escapes from the enemy."
                    play sound "audio/walk.mp3"
                    $ door_fight = False
                    "Tali continued on her way......"
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
                    tali "Finally!"
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
        tali "Hold it! Thought you were gonna get away with doing something filthy, right? Too bad. Now stand still! If you're nice I might even help you out..."
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
        tali "Mph. You're close. I can feel it... Well, go on then. Dump your load all over my helmet you stupid animal!"
        scene bg securedoor1
        show doorhjcum
        $ lewd += 1
        $ renpy.pause ()
        scene bg securedoor1
        show tali fin1 at left
        with dis
        tali "Keelah, what am I doing? It's so hard to resist..."
        scene black
        $ door_fight = False
        $ hackNumber = 3
        $ hackID = 0
        jump map


    label backanal:
        $ lewd += 1
        scene bg securedoor1
        show tali hj1 at left
        show tali hj1 at shake
        play sound "audio/punch.mp3"
        tali "You're an assertive one, aren't you? I have just the job for you..."
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
        tali "Y-You like that, right? That fat quarian ass waiting for your hard cock to fuck? Wanna try it?"
        scene bg securedoor1
        show dooranalstep3
        $ renpy.pause ()
        scene bg securedoor1
        show tali backanal27
        tali "Ngh. Let me push it a bit..."
        scene bg securedoor1
        show dooranalstep4
        pause 2
        tali "Mmm. Your turn. Time to claim your prize, big boy..."
        scene bg securedoor1
        show dooranalstep5
        pause 1
        tali "Keelah... It's so hot. It feels... so right."
        scene bg securedoor1
        show dooranalstep6
        $ renpy.pause ()
        if lewd > 25:
            scene bg securedoor1
            show tali backanal57
            tali "Mmmph! Fuck my ass you disgusting creature! Show me what that fat dick can do!"
            scene bg securedoor1
            show dooranalstep6ext
            $ renpy.pause ()
        scene bg securedoor1
        show dooranalstep7
        $ renpy.pause ()
        scene bg securedoor1
        show dooranalstep7alt
        tali "Oh keelah, fuck my ass deeper!"
        scene bg securedoor1
        show dooranalcum
        $ renpy.pause ()
        scene bg securedoor1
        show tali fin1 at left
        with dis
        tali "That was... so good. My body is... Keelah, I'm shaking. I should... I should go to the medical bay."
        scene black
        $ door_fight = False
        $ hackNumber = 3
        $ hackID = 0
        jump medbayafterdefeat

    label sliderBattleFuck1:
        $ fuckpose = renpy.random.randint(1, 2)
        scene bg cor1
        if suit > 8:
            show tali gunshoot at left
        if suit == 8:
            show tali gunshoot69 at left
        if suit == 7:
            show tali gunshoot7 at left
        if suit < 7:
            show tali gunshoot6 at left
        show creep stand at right
        call screen sliderfuck1

    label sliderBattleFuck2:
        scene bg cor2
        if suit > 8:
            show tali gunshoot at left
        if suit == 8:
            show tali gunshoot69 at left
        if suit == 7:
            show tali gunshoot7 at left
        if suit < 7:
            show tali gunshoot6 at left
        show varren stand at right
        call screen sliderfuck2

    label sliderBattleFuck3:
        $ fuckpose = renpy.random.randint(1, 2)
        scene bg poolcor
        if suit > 8:
            show tali gunshoot at left
        if suit == 8:
            show tali gunshoot69 at left
        if suit == 7:
            show tali gunshoot7 at left
        if suit < 7:
            show tali gunshoot6 at left
        show lizard stand at right
        call screen sliderfuck3


    screen sliderfuck1():
        modal True
        showif ammo > 0:
            imagebutton:
                idle "images/skills/shoot_idle.png"
                hover "images/skills/shoot_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.2
                action Jump("shoot_skill1")
        showif grenades > 0:
            imagebutton:
                idle "images/skills/grenskill_idle.png"
                hover "images/skills/grenskill_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.3
                action Jump("grenade_skill1")
        showif darts > 0 and lovedart == False and suit > 6:
            imagebutton:
                idle "images/skills/dart_idle.png"
                hover "images/skills/dart_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.4
                action Jump("dart_skill")
        showif lewd > 20 and suit > 6 and lovedart:
            imagebutton:
                idle "images/skills/lips_idle.png"
                hover "images/skills/lips_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.5
                action Jump("sex_skill")
        showif lewd > 10 and suit > 6:
            imagebutton:
                idle "images/skills/tease_idle.png"
                hover "images/skills/tease_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.6
                action Jump("tease_skill")
        imagebutton:
            idle "images/skills/escape_idle.png"
            hover "images/skills/escape_hover.png"
            focus_mask True
            xpos 0.45
            ypos 0.7
            action Jump("escape_skill1")
        bar:
            left_bar "images/skills/sliderbar_idle.png"
            right_bar "images/skills/sliderbar_empty.png"
            thumb "images/skills/enemyicon.png"
            value AnimatedValue(0, 1000, 5, slidervalue)
            xalign 0.5
            yalign 0.9
            xysize(500,70)
        timer 5.5 action Jump("suittier1")

    screen sliderfuck2():
        modal True
        showif ammo > 0:
            imagebutton:
                idle "images/skills/shoot_idle.png"
                hover "images/skills/shoot_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.1
                action Jump("shoot_skill1")
        showif grenades > 0:
            imagebutton:
                idle "images/skills/grenskill_idle.png"
                hover "images/skills/grenskill_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.2
                action Jump("grenade_skill1")
        showif darts > 0 and lovedart == False and suit > 7:
            imagebutton:
                idle "images/skills/dart_idle.png"
                hover "images/skills/dart_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.3
                action Jump("dart_skill")
        showif lewd > 20 and suit > 7 and lovedart:
            imagebutton:
                idle "images/skills/lips_idle.png"
                hover "images/skills/lips_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.4
                action Jump("sex_skill")
        showif lewd > 10:
            imagebutton:
                idle "images/skills/tease_idle.png"
                hover "images/skills/tease_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.5
                action Jump("tease_skill1")
        showif lewd > 10:
            imagebutton:
                idle "images/skills/tease_idle.png"
                hover "images/skills/tease_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.6
                action Jump("tease_skill2")        
        imagebutton:
            idle "images/skills/escape_idle.png"
            hover "images/skills/escape_hover.png"
            focus_mask True
            xpos 0.45
            ypos 0.7
            action Jump("escape_skill1")
        bar:
            left_bar "images/skills/sliderbar_idle.png"
            right_bar "images/skills/sliderbar_empty.png"
            thumb "images/skills/enemyicon.png"
            value AnimatedValue(0, 1000, 5, slidervalue)
            xalign 0.5
            yalign 0.9
            xysize(500,70)
        timer 5.5 action Jump("suittier2")

    screen sliderfuck3():
        modal True
        showif ammo > 0:
            imagebutton:
                idle "images/skills/shoot_idle.png"
                hover "images/skills/shoot_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.2
                action Jump("shoot_skill1")
        showif grenades > 0:
            imagebutton:
                idle "images/skills/grenskill_idle.png"
                hover "images/skills/grenskill_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.3
                action Jump("grenade_skill1")
        showif darts > 0 and lovedart == False and suit > 7:
            imagebutton:
                idle "images/skills/dart_idle.png"
                hover "images/skills/dart_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.4
                action Jump("dart_skill")
        showif lewd > 20 and suit > 7 and lovedart:
            imagebutton:
                idle "images/skills/lips_idle.png"
                hover "images/skills/lips_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.5
                action Jump("sex_skill")
        showif lewd > 10 and suit > 7:
            imagebutton:
                idle "images/skills/tease_idle.png"
                hover "images/skills/tease_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.6
                action Jump("tease_skill")
        imagebutton:
            idle "images/skills/escape_idle.png"
            hover "images/skills/escape_hover.png"
            focus_mask True
            xpos 0.45
            ypos 0.7
            action Jump("escape_skill1")
        bar:
            left_bar "images/skills/sliderbar_idle.png"
            right_bar "images/skills/sliderbar_empty.png"
            thumb "images/skills/enemyicon.png"
            value AnimatedValue(0, 1000, 5, slidervalue)
            xalign 0.5
            yalign 0.9
            xysize(500,70)
        timer 5.5 action Jump("suittier3")
    label tease_skill1:
        $ sexpose = 1
        jump tease_skill

    label tease_skill2:
        $ sexpose = 2
        jump tease_skill

    label tease_skill:
        if suit > 8:
            show tali tease at left
            show tali tease at shake
        if suit == 8:
            show tali tease69 at left
            show tali tease69 at shake
        if suit == 7:
            show tali tease7 at left
            show tali tease7 at shake
        if suit < 7:
            show tali tease7 at left
            show tali tease7 at shake
        play sound "audio/slap.mp3"
        if sexpose == 1:
            "Want this fat quarian ass? Come and get it."
        if sexpose == 2:
            "You Like the look of these quarian lips? Come and get them."
        play sound "audio/creepone.mp3"
        pause 1
        if enemyID == 0:
            jump suittier1
        elif enemyID == 2:
            jump suittier2
        elif enemyID == 3:
            jump suittier3

    label dart_skill:
        $ lovedart = True
        $ darts -= 1
        if suit > 8:
            show tali dart at left
        if suit == 8:
            show tali dart69 at left
        if suit == 7:
            show tali dart7 at left
        if suit < 7:
            show tali dart6 at left
        play sound "audio/equip.ogg"
        "Firing tranquilizer!"
        play sound "audio/dart.mp3"
        pause 1
        play sound "audio/roar.mp3"
        "The beast looks more calm now. You can try to get closer."
        if enemyID == 0:
            jump sliderBattleFuck1
        elif enemyID == 2:
            jump sliderBattleFuck2
        elif enemyID == 3:
            jump sliderBattleFuck3



    label sex_skill:
        if enemyID == 0:
            jump sex_skill1
        if enemyID == 2:
            jump sex_skill2
        if enemyID == 3:
            jump sex_skill3

    label sex_skill1:
        "Tali tries getting closer..."
        $ random = renpy.random.randint(1, 100)
        if random > 30:
            play sound "audio/fall.ogg"
            scene bg cor1
            if suit > 8:
                show tali grab1 at shake
            elif suit > 6 and suit < 9:
                show tali grab3 at shake
            "Success!"
            if suit > 8:
                if sexstage == 1:
                    $ sexstage += 1
                    scene bg cor1
                    show sex1
                    $ renpy.pause ()
                elif sexstage == 2:
                    $ sexstage += 1
                    scene bg cor1
                    show sex2
                    $ renpy.pause ()
                elif sexstage == 3:
                    $ sexstage = 1
                    scene bg cor1
                    show sex2
                    $ renpy.pause ()
                    scene bg cor1
                    show cum1
                    $ renpy.pause ()
                    scene bg cor1
                    show tali fin1 at left
                    $ lewd += 1
                    tali "Ngh. So much cum... "
                    scene black
                    play sound "audio/walk.mp3"
                    "Tali continues on her way..."
                    $ suit = 10
                    jump engine
            elif suit > 6:
                if sexstage == 1:
                    $ sexstage += 1
                    scene bg cor1
                    show sex3
                    $ renpy.pause()
                elif sexstage == 2:
                    $ sexstage += 1
                    if lewd < 30:
                        scene bg cor1
                        show sex3alt
                        $ renpy.pause ()
                    elif lewd < 40:
                        scene bg cor1
                        show tali grab3
                        tali "So hard. I think I can do much better..."
                        scene bg cor1
                        show sex4
                        $ renpy.pause ()
                    elif lewd > 40:
                        scene bg cor1
                        show tali grab3
                        tali "You like staring at my lips? Let me give you something to really look at..."
                        scene bg cor1
                        show sex4
                        $ renpy.pause ()
                        scene bg cor1
                        show tali grab4
                        tali "Keelah... I want him deep in my throat..."
                        scene bg cor1
                        show sex5
                        pause 3
                        scene bg cor1
                        show sex6
                        $ renpy.pause ()
                elif sexstage == 3:
                    $ lewd += 1
                    $ lovedart = False
                    $ sexstage = 1
                    if lewd < 30:
                        scene bg cor1
                        show sex3alt
                        $ renpy.pause ()
                        scene bg cor1
                        show cum2
                        $ renpy.pause ()
                        scene bg cor1
                        show tali doubt69 at left
                        tali "Well... one way or another."
                    elif lewd < 41:
                        scene bg cor1
                        show sex4alt
                        $ renpy.pause ()
                        scene bg cor1
                        show cum2
                        $ renpy.pause ()
                        scene bg cor1
                        show tali doubt69 at left
                        tali "Done. Now where's me helmet...?"
                    elif lewd > 40:
                        scene bg cor1
                        show sex5
                        pause 3
                        scene bg cor1
                        show sex6alt
                        $ renpy.pause ()
                        scene bg cor1
                        show tali grab5
                        tali "Mmm. My lips are wrapped so tight around your fat cock. Go on then... give me your cum. I don't want to spill a single drop."
                        scene bg cor1
                        show cum3
                        $ renpy.pause ()
                        scene bg cor1
                        show tali fin2 at left
                        tali "Silly girl, you went a little too crazy..."
                    scene black
                    play sound "audio/walk.mp3"
                    "Tali continues her way..."
                    $ suit = 10
                    jump engine
        else:
            if suit > 8:
                show tali evade at left
                show tali evade at shake
            if suit == 8:
                show tali evade69 at left
                show tali evade69 at shake
            if suit == 7:
                show tali evade7 at left
                show tali evade7 at shake
            if suit < 7:
                show tali evade6 at left
                show tali evade6 at shake
            play sound "audio/creepone.mp3"
            "Pushed back!"
            $ random = renpy.random.randint(1, 100)
            play sound "audio/creepone.mp3"
            if enemyID == 0:
                show creep stand at shake
            elif enemyID == 1:
                show biggy stand at shake
            elif enemyID == 2:
                show varren stand at shake
            "Enemy attacks!"
            if random > 30:
                play sound "audio/miss.mp3"
                if suit > 8:
                    show tali evade at left
                if suit == 8:
                    show tali evade69 at left
                if suit == 7:
                    show tali evade7 at left
                if suit < 7:
                    show tali evade6 at left
                "Miss!"
                if enemyID == 0:
                    jump sliderBattleFuck1
                elif enemyID == 2:
                    jump sliderBattleFuck2
            else:
                $ random = renpy.random.randint(1, 100)
                play sound "audio/creepone.mp3"
                show creep stand at shake
                "Enemy attacks!"
                if random > 60:
                    play sound "audio/miss.mp3"
                    if suit > 8:
                        show tali evade at left
                    if suit == 8:
                        show tali evade69 at left
                    if suit == 7:
                        show tali evade7 at left
                    if suit < 7:
                        show tali evade6 at left
                    "Miss!"
                    jump sliderBattleFuck1
                else:
                    jump suittier1
        jump sliderBattleFuck1


    label sex_skill2:
        "Tali tries to get closer..."
        $ random = renpy.random.randint(1, 100)
        if random > 30:
            play sound "audio/fall.ogg"
            scene bg cor2
            if suit > 8:
                show tali grab6 at shake
            elif suit > 6 and suit < 9:
                show tali grab7 at shake
            "Success!"
            if suit > 8:
                if sexstage == 1:
                    $ sexstage += 1
                    scene bg cor2
                    show sex7
                    $ renpy.pause ()
                elif sexstage == 2:
                    $ sexstage += 1
                    scene bg cor2
                    show sex8
                    $ renpy.pause ()
                elif sexstage == 3:
                    $ lewd += 1
                    $ sexstage = 1
                    $ lovedart = False
                    scene bg cor2
                    show sex8
                    $ renpy.pause ()
                    scene bg cor2
                    show cum4
                    $ renpy.pause ()
                    scene bg cor2
                    show tali fin1 at left
                    tali "Ah, so much sperm... "
                    scene black
                    play sound "audio/walk.mp3"
                    "Tali continues her way..."
                    $ suit = 10
                    jump warehouse
            elif suit == 8:
                if sexstage == 1:
                    $ sexstage += 1
                    scene bg cor2
                    show sex9
                    $ renpy.pause()
                elif sexstage == 2:
                    $ sexstage += 1
                    if lewd < 30:
                        scene bg cor2
                        show sex10
                        $ renpy.pause ()
                    elif lewd < 41:
                        scene bg cor2
                        show sex10
                        $ renpy.pause ()
                        scene bg cor2
                        show tali grab7
                        tali "Such a nice red lollipop you have... Let me take some measurements..."
                        scene bg cor2
                        show sex11
                        $ renpy.pause ()
                    elif lewd > 40:
                        scene bg cor2
                        show sex10
                        $ renpy.pause ()
                        scene bg cor2
                        show tali grab7
                        tali "Such a thick, bad doggy. Tali will have to punish you..."
                        scene bg cor2
                        show sex11
                        $ renpy.pause ()
                elif sexstage == 3:
                    $ lewd += 1
                    $ lovedart = False
                    $ sexstage = 1
                    if lewd < 30:
                        scene bg cor2
                        show sex10
                        $ renpy.pause ()
                        scene bg cor2
                        show cum5
                        $ renpy.pause ()
                        scene bg cor2
                        show tali doubt69 at left
                        tali "Well... one way or another."
                    elif lewd < 41:
                        scene bg cor2
                        show sex11
                        $ renpy.pause ()
                        scene bg cor2
                        show cum6
                        $ renpy.pause ()
                        scene bg cor2
                        show tali doubt69 at left
                        tali "Now where did I put my helmet...?"
                    elif lewd > 40:
                        scene bg cor2
                        show sex11
                        $ renpy.pause ()
                        scene bg cor2
                        show cum7
                        $ renpy.pause ()
                        scene bg cor2
                        show tali grab8
                        tali "Mmmm, you filthy stray. You're not going anywhere until your cock is clean and polished..."
                        scene bg cor2
                        show cum8
                        $ renpy.pause ()
                        scene bg cor2
                        show cum9
                        $ renpy.pause ()
                        scene bg cor2
                        show tali fin2 at left
                        tali "Okay. Maybe I was a little too into it..."
                    scene black
                    play sound "audio/walk.mp3"
                    "Tali continues her way..."
                    $ suit = 10
                    jump warehouse

        else:
            if suit > 8:
                show tali evade at left
                show tali evade at shake
            if suit == 8:
                show tali evade69 at left
                show tali evade69 at shake
            if suit == 7:
                show tali evade7 at left
                show tali evade7 at shake
            if suit < 7:
                show tali evade6 at left
                show tali evade6 at shake
            play sound "audio/creepone.mp3"
            "Pushed back!"
            $ random = renpy.random.randint(1, 100)
            play sound "audio/creepone.mp3"
            show varren stand at shake
            "Enemy attacks!"
            if random > 60:
                play sound "audio/miss.mp3"
                if suit > 8:
                    show tali evade at left
                if suit == 8:
                    show tali evade69 at left
                if suit == 7:
                    show tali evade7 at left
                if suit < 7:
                    show tali evade6 at left
                "Miss!"
                jump sliderBattleFuck2
            else:
                jump suittier2
        jump sliderBattleFuck2

    label sex_skill3:
        "Tali tries to get closer..."
        $ random = renpy.random.randint(1, 100)
        if random > 30:
            play sound "audio/fall.ogg"
            scene bg poolcor
            if suit > 8:
                show tali grab9 at shake
            elif suit > 6 and suit < 9:
                show tali grab10 at shake
            "Success!"
            if suit > 8:
                if sexstage == 1:
                    $ sexstage += 1
                    scene bg poolcor
                    show lizsex1
                    $ renpy.pause ()
                elif sexstage == 2:
                    $ sexstage += 1
                    scene bg poolcor
                    show lizsex2
                    $ renpy.pause ()
                elif sexstage == 3:
                    $ lewd += 1
                    $ sexstage = 1
                    $ lovedart = False
                    scene bg poolcor
                    show lizsex2
                    $ renpy.pause ()
                    scene bg poolcor
                    show lizcum1
                    $ renpy.pause ()
                    scene bg poolcor
                    show tali fin1 at left
                    tali "Ah, so much sperm... "
                    scene black
                    play sound "audio/walk.mp3"
                    "Tali continues her way..."
                    $ suit = 10
                    jump pool
            elif suit == 8:
                if sexstage == 1:
                    $ sexstage += 1
                    scene bg poolcor
                    show lizsex3
                    $ renpy.pause()
                elif sexstage == 2:
                    $ sexstage += 1
                    if lewd < 30:
                        scene bg poolcor
                        show lizsex4
                        $ renpy.pause ()
                    elif lewd < 41:
                        tali "Mmm, let me take care of this with my mouth."
                        scene bg poolcor
                        show lizsex5
                        $ renpy.pause ()
                    elif lewd > 40:
                        tali "Mmm, let me take care of this with my mouth."
                        scene bg poolcor
                        show lizsex5
                        $ renpy.pause ()
                elif sexstage == 3:
                    $ lewd += 1
                    $ lovedart = False
                    $ sexstage = 1
                    if lewd < 30:
                        scene bg poolcor
                        show lizsex4
                        tali "Ah, you're ready to cum..."
                        scene bg poolcor
                        show lizcum2
                        $ renpy.pause ()
                        scene bg poolcor
                        show tali doubt69 at left
                        tali "Well... one way or another."
                    elif lewd < 41:
                        scene bg poolcor
                        show lizsex5
                        $ renpy.pause ()
                        tali "Mmm... his dick is throbbing in pleasure. Here. Dump your load between my tight, drooling lips."
                        scene bg poolcor
                        show lizcum3
                        $ renpy.pause ()
                        scene bg poolcor
                        show tali doubt69 at left
                        tali "Now where did I put my helmet...?"
                    elif lewd > 40:
                        $ random = renpy.random.randint(1, 2)
                        scene bg poolcor
                        show lizsex5
                        $ renpy.pause ()
                        if random == 1:
                            scene bg poolcor
                            show tali grab11 with hpunch
                            play sound "audio/frog2.mp3"
                            tali "What? W-Wait, you shouldn't be able to...!"
                            scene bg poolcor
                            show lizsex6
                            pause 2
                            tali "HMMPHPP!? The... tranquilizer... didn't work?!"
                            scene bg poolcor
                            show lizsex7
                            $ renpy.pause ()
                            tali "Oh Keelah yes... Fuck my face with your fat cock... Stretch my tight throat and clog it with your cum!"
                            scene bg poolcor
                            show lizcum4
                            $ renpy.pause ()
                        else:
                            scene bg poolcor
                            show lizsex5
                            $ renpy.pause ()
                            tali "MMm... his dick is throbbing in pleasure. Let me empty your balls in my mouth."
                            scene bg poolcor
                            show lizcum3
                            $ renpy.pause ()
                        scene bg poolcor
                        show tali fin2 at left
                        tali "Okay. Maybe I was a little too into it..."
                    scene black
                    play sound "audio/walk.mp3"
                    "Tali continues her way..."
                    $ suit = 10
                    jump pool

        else:
            if suit > 8:
                show tali evade at left
                show tali evade at shake
            if suit == 8:
                show tali evade69 at left
                show tali evade69 at shake
            if suit == 7:
                show tali evade7 at left
                show tali evade7 at shake
            if suit < 7:
                show tali evade6 at left
                show tali evade6 at shake
            play sound "audio/frog2.mp3"
            "Pushed back!"
            $ random = renpy.random.randint(1, 100)
            play sound "audio/frog2.mp3"
            show lizard stand at shake
            "Enemy attacks!"
            if random > 60:
                play sound "audio/miss.mp3"
                if suit > 8:
                    show tali evade at left
                if suit == 8:
                    show tali evade69 at left
                if suit == 7:
                    show tali evade7 at left
                if suit < 7:
                    show tali evade6 at left
                "Miss!"
                jump sliderBattleFuck3
            else:
                jump suittier3
        jump sliderBattleFuck3


    label suittier1:
        hide creep stand
        $ random = renpy.random.randint(1, 100)
        play sound "audio/fall.ogg"
        if suit > 8:
            show tali a11 at left
            show tali a11 at shake
        if suit == 8:
            show tali a12 at left
            show tali a12 at shake
        if suit == 7:
            show tali a13 at left
            show tali a13 at shake
        if suit < 7:
            show tali a14 at left
            show tali a14 at shake
        "Tali failed to dodge!"
        if suit > 8:
            if random > 50:
                if fuckstage == 1:
                    $ fuckstage += 1
                    if fuckpose == 1:
                        scene bg cor1
                        show frontmask1
                        $ renpy.pause ()
                    else:
                        scene bg cor1
                        show backmask1
                        $ renpy.pause ()
                elif fuckstage == 2:
                    $ fuckstage += 1
                    if fuckpose == 1:
                        scene bg cor1
                        show frontmask2
                        $ renpy.pause ()
                    else:
                        scene bg cor1
                        show backmask2
                        $ renpy.pause ()
                elif fuckstage == 3:
                    $ lewd += 1
                    $ fuckstage = 1
                    if fuckpose == 1:
                        scene bg cor1
                        show frontmask2
                        $ renpy.pause ()
                        scene bg cor1
                        show frontmaskcum
                        $ renpy.pause ()
                    else:
                        scene bg cor1
                        show backmask2
                        $ renpy.pause ()
                        scene bg cor1
                        show backmaskcum
                        $ renpy.pause ()
                    scene bg cor1
                    show tali fin1 at left
                    tali "Ugh... I feel so nasty. My suit is undamaged but... I can keep going after some cleanup."
                    scene black
                    play sound "audio/walk.mp3"
                    "Tali continues her way..."
                    $ lovedart = False
                    $ suit = 10
                    jump engine
            else:
                $ suit -= 1
                if suit == 8:
                    play sound "audio/glass.mp3"
                    "Helmet damaged!"
        elif suit == 8:
            if random > 50:
                if fuckstage == 1:
                    $ fuckstage += 1
                    scene bg cor1
                    show frontnomask1
                    $ renpy.pause ()
                elif fuckstage == 2:
                    $ fuckstage += 1
                    scene bg cor1
                    show frontnomask2
                    $ renpy.pause ()
                elif fuckstage == 3:
                    $ lewd += 1
                    $ infection += 1
                    $ fuckstage = 1
                    scene bg cor1
                    show frontnomask2
                    $ renpy.pause ()
                    scene bg cor1
                    show frontnomaskcum
                    $ renpy.pause ()
                    scene bg cor1
                    show tali fin2 at left
                    if infection < 3:
                        tali "T-That was too much cum. My antibiotics should help, but... I need to find my helmet before it gets worse..."
                        scene black
                        play sound "audio/walk.mp3"
                        "Tali continues her way..."
                        $ suit = 10
                        $ lovedart = False
                        jump engine
                    else :
                        tali "I swallowed too much... I have to go to the medbay urgently."
                        $ lovedart = False
                        $ suit = 10
                        jump medbayafterdefeat
            else:
                $ suit -= 1
                play sound "audio/tier.mp3"
                "Suit damaged!"
        elif suit == 7:
            if random > 50:
                if fuckstage == 1:
                    $ fuckstage += 1
                    scene bg cor1
                    show frontnomask1
                    $ renpy.pause ()
                elif fuckstage == 2:
                    $ fuckstage += 1
                    scene bg  cor1
                    show frontnomask2
                    $ renpy.pause ()
                elif fuckstage == 3:
                    $ lewd += 1
                    $ infection += 1
                    $ fuckstage = 1
                    scene bg cor1
                    show frontnomaskcum
                    $ renpy.pause ()
                    scene bg cor1
                    show tali fin2 at left
                    if infection < 3:
                        tali "T-That was too much cum. My antibiotics should help, but... I need to activate suit recover sequence before it gets worse..."
                        scene black
                        play sound "audio/walk.mp3"
                        "Tali continues her way..."
                        $ lovedart = False
                        $ suit = 10
                        jump engine
                    else :
                        tali "I swallowed too much... I have to go to the medbay urgently."
                        $ lovedart = False
                        $ suit = 10
                        jump medbayafterdefeat
            else:
                $ suit -= 1
                play sound "audio/tier.mp3"
                "Suit damaged!"
        elif suit < 7:
            if fuckstage == 1:
                $ fuckstage += 1
                if fuckpose == 1:
                    scene bg cor1
                    show frontdamaged1
                    $ renpy.pause ()
                else:
                    scene bg cor1
                    show backdamaged1
                    pause 2
                    scene bg cor1
                    show backdamaged2
                    $ renpy.pause ()
            elif fuckstage == 2:
                $ fuckstage += 1
                if fuckpose == 1:
                    scene bg cor1
                    show frontdamaged2
                    $ renpy.pause ()
                else:
                    scene bg cor1
                    show backdamaged2
                    $ renpy.pause ()
            elif fuckstage == 3:
                $ lewd += 1
                $ infection += 1
                $ fuckstage = 1
                if fuckpose == 1:
                    scene bg cor1
                    show frontdamaged2
                    $ renpy.pause ()
                    scene bg cor1
                    show frontdamagedcum
                    $ renpy.pause ()
                else:
                    scene bg cor1
                    show backdamaged2
                    $ renpy.pause ()
                    scene bg cor1
                    show backdamagedcum
                    $ renpy.pause ()
                scene bg cor1
                show tali fin3 at left
                tali "K-Keelah. My suit's in tatters... and my body's on fire. I need to head back to the medbay..."
                scene black
                play sound "audio/walk.mp3"
                $ lovedart = False
                $ suit = 10
                jump medbayafterdefeat
        play sound "audio/punch.mp3"
        show creep stand at right
        show creep stand at shake
        jump sliderBattleFuck1

    label suittier2:
        hide varren stand
        $ random = renpy.random.randint(1, 100)
        $ lewd_action = 1
        $ defeated = 0
        play sound "audio/fall.ogg"
        if suit > 8:
            show tali a21 at left
            show tali a21 at shake
        if suit == 8:
            show tali a22 at left
            show tali a22 at shake
        if suit == 7:
            show tali a23 at left
            show tali a23 at shake
        if suit < 7:
            show tali a24 at left
            show tali a24 at shake
        "Tali failed to dodge! suit:[suit] sexpose:[sexpose] fuckstage:[fuckstage]"

        if random < 0 and suit > 6:
            # suit damage action
            $ lewd_action = 0
            if suit == 9:
                play sound "audio/glass.mp3"
                "Helmet damaged!"
            if suit in [7,8]:
                play sound "audio/tier.mp3"
                "Suit damaged!"
            $ suit -= 1
        else:
            # lewd action
            scene bg cor2
            if suit > 8:
                #mask facial  
                if fuckstage == 1:
                    show frontvarmask1
                elif fuckstage == 2:
                    show frontvarmask2
                elif fuckstage == 3:
                    show frontvarmask2
                    $ renpy.pause ()
                    scene bg cor2
                    show frontvarmaskcum
                    $ renpy.pause ()
                    scene bg cor2
                    show tali fin1 at left
                    tali "Ugh... I feel so nasty. My suit is undamaged but... I think I can keep going after cleaning up."
            elif suit == 8:
                # no mask facial
                if fuckstage == 1:
                    if lewd > 25:
                        show frontvarnomask2
                    else:
                        show frontvarnomask1
                elif fuckstage == 2:
                    if lewd > 25:
                        show frontvarnomask2
                        $ renpy.pause ()
                        scene bg cor2
                        show frontvarnomask3
                        pause 2.5
                        scene bg cor2
                        show frontvarnomask4
                    else:
                        show frontvarnomask2
                elif fuckstage == 3:
                    $ infection += 1
                    if lewd > 25:
                        show frontvarnomask4
                        $ renpy.pause ()
                        scene bg cor2
                        show frontvarnomask5
                        pause 4
                        scene bg cor2
                        show frontvarnomask6
                        $ renpy.pause ()
                        scene bg cor2
                        show frontvarnomaskcum2
                    else:
                        show frontvarnomask2
                        $ renpy.pause ()
                        scene bg cor2
                        show frontvarnomaskcum1
                    scene bg cor2
                    show tali fin2 at left
                    if infection < 3:
                        tali "T-That was way too much cum. My antibiotics should help, but... I really need to find my helmet before it gets any worse..."
                    else :
                        tali "I swallowed way too much... I have to get back to the medbay urgently."
                        $ defeated = 1      
            elif suit == 7:
            # blowjob or mount
                if fuckstage == 1:
                # mount 1
                    if fuckpose == 1:
                        show backvar1
                # blow 1
                    else:
                        show frontvardamaged1
                elif fuckstage == 2:
                # mount 2
                    if fuckpose == 1:
                        show backvar2
                    else:
                # blow 2
                        show frontvardamaged2
                elif fuckstage == 3:
                # blow 2 + cum
                    $ infection += 1
                    show frontvardamaged2
                    $ renpy.pause ()
                    scene bg cor2
                    show frontvardamagedcum
                    $ renpy.pause ()
                    scene bg cor2
                    show tali fin2 at left
                    if infection < 3:
                        tali "T-That was too much cum. My antibiotics should help, but... I need to activate my suit's recover sequence before it gets worse..."
                    else :
                        tali "I swallowed too much... I have to get to the medbay urgently."
                        $ defeated = 1
            elif suit < 7:
                # mount 1
                if fuckstage == 1:
                    show backvar3
                elif fuckstage == 2:
                # mount 2
                    show backvar4
                elif fuckstage == 3:
                # mount 2 + cum
                    $ infection += 1
                    show backvar4
                    $ renpy.pause ()
                    scene bg cor2
                    show backvarcum1
                    $ renpy.pause ()
                    scene bg cor2
                    show tali fin3 at left
                    tali "Ahhh. My suit's in tatters... and my body's on fire. I hope I can make it back to the medbay..."
                    $ defeated = 1
                
        if lewd_action == 1:
            $ fuckstage += 1
            $ renpy.pause ()
        
        if fuckstage == 4:
            # event over
            $ fuckstage = 1
            $ lewd += 1
            $ lovedart = False
            $ suit = 10
            if defeated == 0:
                scene black
                tali "Tali continues on her way..."
                play sound "audio/walk.mp3"
                jump warehouse
            else:
                jump medbayafterdefeat

        play sound "audio/punch.mp3"
        show varren stand at right
        show varren stand at shake    
        jump sliderBattleFuck2

    label suittier3:
        hide lizard stand
        $ random = renpy.random.randint(1, 100)
        play sound "audio/fall.ogg"
        if suit > 8:
            show tali a31 at left
            show tali a31 at shake
        if suit == 8:
            show tali a32 at left
            show tali a32 at shake
        if suit == 7:
            show tali a33 at left
            show tali a33 at shake
        if suit < 7:
            show tali a34 at left
            show tali a34 at shake
        "Tali failed to dodge!"
        if suit > 8:
            if random > 50:
                if fuckstage == 1:
                    $ fuckstage += 1
                    scene bg poolcor
                    show liz1f1
                    $ renpy.pause ()
                elif fuckstage == 2:
                    $ fuckstage += 1
                    scene bg poolcor
                    show liz1f2
                    $ renpy.pause ()
                elif fuckstage == 3:
                    $ lewd += 1
                    $ fuckstage = 1
                    scene bg poolcor
                    show liz1f2
                    $ renpy.pause ()
                    scene bg poolcor
                    show liz1fcum1
                    $ renpy.pause ()
                    scene bg poolcor
                    show tali fin1 at left
                    tali "Ugh... I feel so nasty. My suit is undamaged but... I can keep going after some cleanup."
                    scene black
                    play sound "audio/walk.mp3"
                    "Tali continues on her way..."
                    $ lovedart = False
                    $ suit = 10
                    jump pool
            else:
                $ suit -= 1
                if suit == 8:
                    play sound "audio/glass.mp3"
                    "Helmet damaged!"
        elif suit == 8:
            if random > 50:
                if fuckstage == 1:
                    $ fuckstage += 1
                    if lewd > 25:
                        scene bg poolcor
                        show liz1f4
                        $ renpy.pause ()
                    else:
                        scene bg poolcor
                        show liz1f3
                        $ renpy.pause ()
                elif fuckstage == 2:
                    $ fuckstage += 1
                    if lewd > 25:
                        scene bg poolcor
                        show liz1f4
                        $ renpy.pause ()
                        scene bg poolcor
                        show liz1f9
                        pause 2
                        scene bg poolcor
                        show liz1f5
                        $ renpy.pause ()
                    else:
                        scene bg poolcor
                        show liz1f4
                        $ renpy.pause ()
                elif fuckstage == 3:
                    $ lewd += 1
                    $ infection += 1
                    $ fuckstage = 1
                    if lewd > 25:
                        scene bg poolcor
                        show liz1f5
                        $ renpy.pause ()
                        scene bg poolcor
                        show liz1f6
                        pause 3.3
                        scene bg poolcor
                        show liz1f7
                        $ renpy.pause ()
                        scene bg poolcor
                        show liz1fcum3
                        $ renpy.pause ()
                    else:
                        scene bg poolcor
                        show liz1f4
                        $ renpy.pause ()
                        scene bg poolcor
                        show liz1fcum2
                        $ renpy.pause ()
                    scene bg poolcor
                    show tali fin2 at left
                    if infection < 3:
                        tali "T-That was too much cum. My antibiotics should help, but... I need to find my helmet before it gets worse..."
                        scene black
                        play sound "audio/walk.mp3"
                        "Tali continues her way..."
                        $ lovedart = False
                        $ suit = 10
                        jump pool
                    else :
                        tali "I swallowed too much... I have to go to the medbay urgently."
                        $ lovedart = False
                        $ suit = 10
                        jump medbayafterdefeat
            else:
                $ suit -= 1
                play sound "audio/tier.mp3"
                "Suit damaged!"
        elif suit == 7:
            if random > 50:
                if fuckstage == 1:
                    $ fuckstage += 1
                    scene bg poolcor
                    show liz1f8
                    $ renpy.pause ()
                elif fuckstage == 2:
                    $ fuckstage += 1
                    scene bg poolcor
                    show liz1b1
                    pause 4
                    $ renpy.pause ()
                    scene bg poolcor
                    show liz1b2
                    $ renpy.pause ()
                elif fuckstage == 3:
                    $ lewd += 1
                    $ infection += 1
                    $ fuckstage = 1
                    scene bg poolcor
                    show liz1b2
                    $ renpy.pause ()
                    scene bg poolcor
                    show liz1bcum1
                    $ renpy.pause ()
                    scene bg poolcor
                    show tali fin2 at left
                    if infection < 3:
                        tali "T-That was too much cum. My antibiotics should help, but... I need to activate suit recover sequence before it gets worse..."
                        scene black
                        play sound "audio/walk.mp3"
                        "Tali continues her way..."
                        $ lovedart = False
                        $ suit = 10
                        jump pool
                    else :
                        tali "I swallowed too much... I have to go to the medbay urgently."
                        $ lovedart = False
                        $ suit = 10
                        jump medbayafterdefeat
            else:
                $ suit -= 1
                play sound "audio/tier.mp3"
                "Suit damaged!"
        elif suit < 7:
            if fuckstage == 1:
                $ fuckstage += 1
                scene bg poolcor
                show liz1b3
                pause 2
                scene bg poolcor
                show liz1b4
                $ renpy.pause ()
            elif fuckstage == 2:
                $ fuckstage += 1
                scene bg poolcor
                show liz1b5
                $ renpy.pause ()
            elif fuckstage == 3:
                $ lewd += 1
                $ infection += 1
                $ fuckstage = 1
                scene bg poolcor
                show liz1b5
                $ renpy.pause ()
                scene bg poolcor
                show liz1bcum2
                $ renpy.pause ()
                scene bg poolcor
                show tali fin3 at left
                tali "Ahhh. My suit's in tatters... and my body's on fire. I need to head back to the medbay..."
                scene black
                play sound "audio/walk.mp3"
                $ lovedart = False
                $ suit = 10
                jump medbayafterdefeat
        play sound "audio/punch.mp3"
        show lizard stand at right
        show lizard stand at shake
        jump sliderBattleFuck3



    label shoot_skill1:
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
            elif enemyID == 3:
                show lizard stand at shake
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
                elif enemyID == 3:
                    show lizard stand at right
                    hide lizard stand
                    with Dissolve(2)
                "Enemy defeated."
                $ corridor_fight = False
                if suitdur < 80:
                    $ suitdur += 20
            else:
                $ random = renpy.random.randint(1, 100)
                play sound "audio/creepone.mp3"
                if enemyID == 0:
                    show creep stand at shake
                elif enemyID == 1:
                    show biggy stand at shake
                elif enemyID == 2:
                    show varren stand at shake
                elif enemyID == 3:
                    show lizard stand at shake
                "Enemy attacks!"
                if random > 60:
                    play sound "audio/miss.mp3"
                    if suit > 8:
                        show tali evade at left
                    if suit == 8:
                        show tali evade69 at left
                    if suit == 7:
                        show tali evade7 at left
                    if suit < 7:
                        show tali evade6 at left
                    "Miss!"
                    if enemyID == 0:
                        jump sliderBattleFuck1
                    elif enemyID == 2:
                        jump sliderBattleFuck2
                    elif enemyID == 3:
                        jump sliderBattleFuck3

                else:
                    if enemyID == 0:
                        jump suittier1
                    elif enemyID == 2:
                        jump suittier2
                    elif enemyID == 3:
                        jump suittier3
            if suit > 8:
                show tali gunstand at left
                tali "Another dead beast."
            if suit == 8:
                show tali gunstand69 at left
                tali "I need to find my helmet..."
            if suit == 7:
                show tali inj7 at left
                tali "Damned creep damaged my suit... but the recovery system should be able to handle it."
            if suit < 7:
                show tali inj6 at left
                tali "Ngh. Need to hurry to the medbay. That was a tough one."
                $ suit = 10
                $ lovedart = False
                jump medbayafterdefeat
            scene black
            play sound "audio/walk.mp3"
            "Tali continued on her way......"
            $ suit = 10
            if roomID == 4:
                $ roomID = 3
            elif roomID == 5:
                $ roomID = 2
            elif roomID == 1:
                jump map
            elif roomID == 11:
                jump pool
            jump rooms
        else:
            play sound "audio/miss.mp3"
            "Miss!"
            $ random = renpy.random.randint(1, 100)
            play sound "audio/creepone.mp3"
            if enemyID == 0:
                show creep stand at shake
            elif enemyID == 1:
                show biggy stand at shake
            elif enemyID == 2:
                show varren stand at shake
            elif enemyID == 3:
                show lizard stand at shake
            "Enemy attacks!"
            if random > 60:
                play sound "audio/miss.mp3"
                if suit > 8:
                    show tali evade at left
                if suit == 8:
                    show tali evade69 at left
                if suit == 7:
                    show tali evade7 at left
                if suit < 7:
                    show tali evade6 at left
                "Miss!"
                if enemyID == 0:
                    jump sliderBattleFuck1
                elif enemyID == 2:
                    jump sliderBattleFuck2
                elif enemyID == 3:
                    jump sliderBattleFuck3
            else:
                if enemyID == 0:
                    jump suittier1
                elif enemyID == 2:
                    jump suittier2
                elif enemyID == 3:
                    jump suittier3

    label grenade_skill1:
        $ alarm += 5
        $ grenades -= 1
        play sound "audio/gunready.wav"
        if suit > 8:
            show tali grenade at left
        if suit == 8:
            show tali grenade69 at left
        if suit == 7:
            show tali grenade7 at left
        if suit < 7:
            show tali grenade6 at left
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
        elif enemyID == 3:
            show lizard stand at shake
            play sound "audio/explosion.mp3"
            "Devastating!"
            show lizard stand at right
            hide lizard stand
            with Dissolve(2)
        "Enemy dead."
        if suit > 8:
            show tali gunstand at left
            tali "Another dead beast."
        if suit == 8:
            show tali gunstand69 at left
            tali "I need to find my helmet..."
        if suit == 7:
            show tali inj7 at left
            tali "Damn creep damaged my suit... but recovery system can handle it."
        if suit < 7:
            show tali inj6 at left
            tali "Ngh. Need to hurry to the medbay. That was a tough one."
            $ lovedart = False
            $ suit = 10
            jump medbayafterdefeat
        scene black
        play sound "audio/walk.mp3"
        "Tali continued on her way......"
        $ suit = 10
        if roomID == 4:
            $ roomID = 3
        elif roomID == 5:
            $ roomID = 2
        elif roomID == 1:
            jump map
        elif roomID == 11:
            jump pool
        jump rooms

    label escape_skill1:
        $ random = renpy.random.randint(1, 100)
        "Tali tries to run away!"
        if random > 0 and random < 51:
            play sound "audio/run.ogg"
            scene black
            "Escape successful."
            $ lovedart = False
            $ fuckstage = 1
            $ sexstage = 1
            scene bg map
            if suit > 8:
                jump map
            if suit == 8:
                show tali guninjured69 at left
                tali "That was close... I'd better go get my helmet."
            if suit == 7:
                show tali inj7 at left
                tali "D-Damned beast. My suits repair system's can't repair this fast enough..."
            if suit < 7:
                show tali inj6 at left
                tali "Ah keelah, my suit is destroyed! I need to hurry to the medbay."
                $ suit = 10
                jump medbayafterdefeat
            $ suit = 10
            jump map
        elif random > 50 and random < 101:
            play sound "audio/creepone.mp3"
            "Escape failed..."
            if enemyID == 0:
                jump suittier1
            elif enemyID == 2:
                jump suittier2
            elif enemyID == 3:
                jump suittier3

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
                "Enemy defeated."
                $ corridor_fight = False
                if suitdur < 80:
                    $ suitdur += 20
            else:
                show tali gunshoot at shake
                play sound "audio/punch.mp3"
                "Enemy hits Tali!"
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
            "Tali continued on her way......"
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
            "Enemy hits Tali!"
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
        "Enemy defeated."
        scene black
        play sound "audio/walk.mp3"
        "Tali continued on her way......"
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
        "Tali tries to run away!"
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
        $ lovedart = False
        $ fuckstage = 1
        $ sexstage = 1
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
        elif roomID == 11:
            jump corridor3



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
        $ poolloot1 = False
        $ poolloot2 = False
        $ poolloot3 = False
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
        if poolnew:
            $ random = renpy.random.randint(1, 200)
            if random > 0 and random < 41:
                $ poolloot1 = True
            elif random > 40 and random < 81:
                $ poolloot2 = True
            elif random > 80 and random < 121:
                $ poolloot3 = True
            elif random > 120 and random < 151:
                $ poolloot1 = True
                $ poolloot3 = True
            elif random > 150 and random < 181:
                $ poolloot2 = True
                $ poolloot3 = True
            elif random > 180 and random < 201:
                $ poolloot1 = True
                $ poolloot2 = True
                $ poolloot3 = True
        $ random = renpy.random.randint(1, 200)
        if random > 0 and random < 41:
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
        elif random > 180 and random < 201:
            $ uloot1 = True
            $ uloot2 = True
            $ uloot3 = True
        $ random = renpy.random.randint(1, 200)
        if random > 0 and random < 41:
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
        elif random > 180 and random < 201:
            $ whlootbox1 = True
            $ whlootbox2 = True
            $ whlootbox3 = True
        $ random = renpy.random.randint(1, 200)
        if random > 0 and random < 41:
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
        if random > 0 and random < 41:
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
        if random > 0 and random < 31:
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
        if random > 0 and random < 31:
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
        if random > 0 and random < 41:
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
        if run_ok:
            jump runrandom
        jump MedBayUsual

    label sliderBoss:
        stop music
        play music "audio/bg/fight_bg.mp3" volume 0.6 loop
        $ enemyhp = 10
        $ suitdoor = 100
        show tali gunshoot at left
        if enemyID == 20:
            show red stand at right
        elif enemyID == 21:
            show red2 stand at right
        elif enemyID == 30:
            show monk stand at right
        elif enemyID == 31:
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
        showif enemyID == 20:
            imagebutton:
                idle "images/skills/escape_idle.png"
                hover "images/skills/escape_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.5
                action Jump("escape_skill_boss")
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
        if enemyID == 21:
            timer 5.5 action Jump("redmedbad")
        if enemyID == 30:
            timer 5.5 action Jump("double_event1")
        if enemyID == 31:
            timer 5.5 action Jump("meddp1Bad")

    label escape_event1:
        $ lewd += 1
        scene bg bay1esc5
        tali "Sorry there beastie but I have to go! See you next time!"
        scene bg bay1esc6 with hpunch
        play sound "audio/punch.mp3"
        pause 1
        scene bg bay1esc7
        play sound "audio/fall.ogg"
        tali "Agh! Dammit! Have to watch my step! There's too much junk laying around here."
        scene bg bay1esc1 with hpunch
        play sound "audio/roar.mp3"
        pause 1
        tali "Ngh? Hey! Stop!"
        scene black
        show bay1anal1
        $ renpy.pause ()
        scene bg bay1esc1 with hpunch
        play sound "audio/creepone.mp3"
        pause 1
        play sound "audio/tier.mp3"
        tali "No! That's going too far! Stop that!"
        scene black
        show bay1anal2
        $ renpy.pause ()
        scene bg bay1esc2
        tali "Oh Keelah. His tongue is so wide and girthy. And it's so rough. It's like a long, thick elastic sponge..."
        tali "Concentrate, Tali. Just reach for your gun while he's distracted and-"
        scene bg bay1esc3
        play sound "audio/creepone.mp3"
        pause 1
        scene bg bay1esc4 with hpunch
        play sound "audio/fall.ogg"
        if lewd < 30:
            tali "Ngh?! Get off me you filthy mutt! Come on, I'm almost there!"
        else:
            tali "Ngh? Oh no. Looks like the big bad varren has his prey right where he wants her. She'll just have to deal with the punishment he chooses for her..."
        scene black
        show bay1anal3
        pause 3
        if lewd < 30:
            tali "AGH?!!!! Don't try it you bosh'tet! Get off of me!"
            scene black
            show bay1anal3alt
            pause 3
            scene black
            show bay1anal5
            pause 2.2
            scene black
            show bay1anal6
            $ renpy.pause ()
            tali "O-Oh fuck, he's so thick! I'm running out of... breath with every..."
            show black
            show bay1anal7
            $ renpy.pause ()
            scene black
            show bay1anal8
            $ renpy.pause ()
        else:
            tali "Mngh! G-Good boy... now please... treat my tight quarian ass gently..."
            scene black
            show bay1anal3alt
            pause 3
            scene black
            show bay1anal4
            $ renpy.pause ()
            scene black
            show bay1anal7
            $ renpy.pause ()
            scene black
            show bay1anal8
            $ renpy.pause ()
        if act3:
            scene bg bay1esc8
            with dis
            if lewd < 30:
                tali "S-So... full..."
            else:
                tali "Ah, I can feel his sperm filling me up..."
            play sound "audio/creepone.mp3"
            pause 1
            scene black
            show bay1anal9
            pause 1.5
            if lewd < 30:
                tali "No... please, no! I'm too full! I can't handle any mo-"
            else:
                tali "H-Huh? Wait, this wasn't supposed to happen!"
            scene black
            show bay1anal9alt
            pause 1.5
            if lewd < 30:
                tali "A-AUGHH?!!?! Deep! Deep inside my ass! K-Keelah, it's so hot!"
            else:
                tali "NGHAAH?! Oh fuck! Oh Keelah, the knot! You pushed your massive, slimy knot into me!"
            scene black
            show bay1anal10
            $ renpy.pause ()
            scene bg bay1esc8
            play sound "audio/cumsplash.mp3"
            tali "Too... much cum! I-I'm gonna...!"
            scene bg bay1esc10
            tali "Hurgh?! N-Nuh... Nough..."
            scene black
            show bay1anal11
            $ renpy.pause ()
        scene bg taliship
        show tali fin1 at left
        tali "Urgh. Mnph. Need to... head back..."
        jump medbayafterdefeat

    label escape_skill_boss:
        $ random = renpy.random.randint(1, 100)
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        "Tali tries to run away!"
        if random > 50:
            play sound "audio/run.ogg"
            scene black
            "Escape successful."
            if comEncounter == True:
                jump afterComEvent
            jump map
        else:
            jump escape_event1

    label bossshoot_skill:
        $ alarm += 1
        $ ammo -= 1
        play sound "audio/gunshot.mp3"
        "Tali shoots!"
        $ random = renpy.random.randint(1, 100)
        if random > 1 and random < 70:
            if enemyID == 20:
                show red stand at shake
            elif enemyID == 20:
                show red2 stand at shake
            elif enemyID == 30:
                show monk stand at shake
            elif enemyID == 31:
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
                    "Red varren fled!"
                elif enemyID == 21:
                    jump redmedgood
                elif enemyID == 30:
                    show monk stand at right
                    hide monk stand
                    with Dissolve(1)
                    play sound "audio/run.ogg"
                    "Beasts fled!"
                elif enemyID == 31:
                    jump meddp1Good
                if suitdur < 80:
                    $ suitdur += 20
            else:
                show tali gunshoot at shake
                play sound "audio/punch.mp3"
                "Enemy hits Tali!"
                $ random = renpy.random.randint(15, 30)
                $ suitdur -= random
                if suitdur < 1:
                    $ suitdur = 20
                    if enemyID == 20:
                        show tali fallmask at left
                        play sound "audio/glass.mp3"
                    elif enemyID == 21:
                        show tali fallmask at left
                        play sound "audio/glass.mp3"
                    elif enemyID == 30:
                        show tali fall at left
                        play sound "audio/fall.ogg"
                    elif enemyID == 31:
                        show tali fall at left
                        play sound "audio/fall.ogg"
                    "Tali falls down."
                    stop music
                    play music "audio/bg/common_bg.mp3" volume 0.3 loop
                    tali "No, dont come closer!"
                    if enemyID == 20:
                        jump redvarrenevent2
                    elif enemyID == 21:
                        jump redmedbad
                    elif enemyID == 30:
                        jump double_event1
                    elif enemyID == 31:
                        jump meddp1Bad
                else:
                    call screen bossslider
            show tali gunstand at left
            stop music
            play music "audio/bg/common_bg.mp3" volume 0.3 loop
            if enemyID == 20:
                tali "Go on, run away you mutt! You won't be so lucky next time."
                show tali doubt at left
                tali "Ngh. That was hard but you've done it, Tali."
                jump map
            elif enemyID == 21:
                jump redmedgood
            elif enemyID == 30:
                tali "That's right, run away! Don't you dare come back! Ugh, stupid monkeys..."
                show tali doubt at left
                tali "Finally the way is clear."
                jump MedBayUsual
            elif enemyID == 31:
                jump meddp1Good
        else:
            $ random = renpy.random.randint(15, 30)
            play sound "audio/miss.mp3"
            "Miss!"
            show tali gunshoot at shake
            play sound "audio/punch.mp3"
            "Enemy hits Tali!"
            $ suitdur -= random
            if suitdur < 1:
                if enemyID == 20:
                    show tali fallmask at left
                    play sound "audio/glass.mp3"
                elif enemyID == 21:
                    show tali fallmask at left
                    play sound "audio/glass.mp3"
                elif enemyID == 30:
                    show tali fall at left
                    play sound "audio/fall.ogg"
                elif enemyID == 31:
                    show tali fall at left
                    play sound "audio/fall.ogg"
                "Tali falls down."
                stop music
                play music "audio/bg/common_bg.mp3" volume 0.3 loop
                tali "No, dont come closer!"
                if enemyID == 20:
                    jump redvarrenevent2
                elif enemyID == 21:
                    jump redmedbad
                elif enemyID == 30:
                    jump double_event1
                elif enemyID == 31:
                    jump meddp1Bad
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
        elif enemyID == 21:
            show red2 stand at shake
        elif enemyID == 30:
            show monk stand at shake
        elif enemyID == 31:
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
                "Red varren fled!"
            elif enemyID == 21:
                jump redmedgood
            elif enemyID == 30:
                show monk stand at right
                hide monk stand
                with Dissolve(1)
                play sound "audio/run.ogg"
                "Beasts fled!"
            elif enemyID == 31:
                jump meddp1Good
            if suitdur < 80:
                $ suitdur += 20
        else:
            show tali gunshoot at shake
            play sound "audio/punch.mp3"
            "Enemy hits Tali!"
            $ random = renpy.random.randint(15, 30)
            $ suitdur -= random
            if suitdur < 1:
                if enemyID == 20:
                    show tali fallmask at left
                    play sound "audio/glass.mp3"
                elif enemyID == 21:
                    show tali fallmask at left
                    play sound "audio/glass.mp3"
                elif enemyID == 30:
                    show tali fall at left
                    play sound "audio/fall.ogg"
                elif enemyID == 31:
                    show tali fall at left
                    play sound "audio/fall.ogg"
                "Tali falls down."
                stop music
                play music "audio/bg/common_bg.mp3" volume 0.3 loop
                tali "No, dont come closer!"
                if enemyID == 20:
                    jump redvarrenevent2
                elif enemyID == 21:
                    jump redmedbad
                elif enemyID == 30:
                    jump double_event1
                elif enemyID == 31:
                    jump meddp1Bad
            else:
                call screen bossslider
        show tali gunstand at left
        stop music
        play music "audio/bg/common_bg.mp3" volume 0.3 loop
        if enemyID == 20:
            tali "Go on, run away you mutt! You won't be so lucky next time."
            show tali doubt at left
            tali "Ngh. That was hard but you done it, Tali."
            jump map
        elif enemyID == 30:
            tali "That's right, run away! Don't you dare come back! Ugh, stupid monkeys..."
            show tali doubt at left
            tali "Finally the way is clear."
            jump MedBayUsual
        else:
            $ random = renpy.random.randint(15, 30)
            play sound "audio/miss.mp3"
            "Miss!"
            show tali gunshoot at shake
            play sound "audio/punch.mp3"
            "Enemy hits Tali!"
            $ suitdur -= random
            if suitdur < 1:
                if enemyID == 20:
                    show tali fallmask at left
                    play sound "audio/glass.mp3"
                elif enemyID == 21:
                    show tali fallmask at left
                    play sound "audio/glass.mp3"
                elif enemyID == 30:
                    show tali fall at left
                    play sound "audio/fall.ogg"
                elif enemyID == 31:
                    show tali fall at left
                    play sound "audio/fall.ogg"
                "Tali falls down."
                stop music
                play music "audio/bg/common_bg.mp3" volume 0.3 loop
                tali "No, dont come closer!"
                if enemyID == 20:
                    jump redvarrenevent2
                elif enemyID == 21:
                    jump redmedbad
                elif enemyID == 30:
                    jump double_event1
                elif enemyID == 31:
                    jump meddp1Bad
            else:
                call screen bossslider




    # -------------------------------------------------------VENTS -----------------------------------------------------------------------------------------------------------

    label VentsStart:
        $ ventsopen = True
        scene bg start
        stop music
        play music "audio/bg/horror_bg.mp3" volume 0.3 loop
        tali "Nyun? Are you there? Keelah..."
        scene bg vtut1
        "Welcome to the new gameplay part of the game! The movement mechanics and interactions will be little bit different here."
        scene bg vtut2
        "Here the main things you need to pay attention. Simple joystick in the bottom right corner allow Tali to move around. The move arrows will become available or not depends on possibility to proceed in that direction."
        "Action 'gear' button is using for interaction with things currently in sight, collecting loot, open hatches etc. It is the main events triggering button here."
        "Good luck. And watch her back :)"
        scene bg start
        call screen movement

    label ventsenter1:
        $ ventID = 0
        $ fwd_ok = True
        $ left_ok = False
        $ right_ok = False
        $ aft_ok = False
        $ action_ok = True
        scene bg start
        stop music
        play music "audio/bg/horror_bg.mp3" volume 0.3 loop
        tali "Here we go."
        call screen movement


    screen movement():
        modal True
        showif action_ok:
            imagebutton xpos 0.8 ypos 0.7:
                idle "images/map/action_idle.png"
                hover "images/map/action_hover.png"
                focus_mask True
                action Jump ("action_button")
        showif fwd_ok:
            imagebutton xpos 0.8 ypos 0.63:
                idle "images/map/fwd_idle.png"
                hover "images/map/fwd_hover.png"
                focus_mask True
                action Jump ("GoFWD")
        showif left_ok:
            imagebutton xpos 0.76 ypos 0.7:
                idle "images/map/left_idle.png"
                hover "images/map/left_hover.png"
                focus_mask True
                action Jump ("GoLEFT")
        showif right_ok:
            imagebutton xpos 0.885 ypos 0.7:
                idle "images/map/right_idle.png"
                hover "images/map/right_hover.png"
                focus_mask True
                action Jump ("GoRIGHT")
        showif aft_ok:
            imagebutton xpos 0.8 ypos 0.85:
                idle "images/map/aft_idle.png"
                hover "images/map/aft_hover.png"
                focus_mask True
                action Jump ("GoBACK")

    label screenCheck:
        if ventID == 0:
            scene bg start
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 11:
            if vent1:
                scene bg 1_1
            else:
                scene bg 1_1alt
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 12:
            if flesh1:
                scene bg 1_2
                $ fwd_ok = False
            else:
                scene bg 1_2b
                $ fwd_ok = True
            $ left_ok = True
            $ right_ok = True
            $ aft_ok = False
        if ventID == 13:
            scene bg 1_3
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 14:
            if vent2:
                scene bg 1_4close
            elif vent4:
                scene bg 1_4close
            else:
                scene bg 1_4open
            $ fwd_ok = False
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 15:
            scene bg 1_5
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 16:
            scene bg 1_6
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 17:
            scene bg 1_7
            $ fwd_ok = False
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 20:
            scene bg 2_0
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 21:
            scene bg 2_1
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 22:
            scene bg 2_2
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 23:
            scene bg 2_3
            $ fwd_ok = True
            if flesh1:
                $ left_ok = False
            else:
                $ left_ok = True
            $ right_ok = True
            $ aft_ok = True
        if ventID == 24:
            scene bg 2_4
            $ fwd_ok = False
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 30:
            scene bg 3_0
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 31:
            scene bg 3_1
            $ fwd_ok = True
            $ left_ok = True
            $ right_ok = False
            $ aft_ok = False
        if ventID == 40:
            if vent5:
                scene bg 4_0close
            else:
                scene bg 4_0open
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 41:
            scene bg 4_1
            $ fwd_ok = True
            $ left_ok = True
            $ right_ok = True
            $ aft_ok = False
        if ventID == 42:
            scene bg 4_2
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 43:
            if vent6:
                scene bg 4_3
                $ fwd_ok = False
            else:
                scene bg 4_3open
                $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 50:
            scene bg 5_0
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 51:
            scene bg 5_1
            $ fwd_ok = True
            $ left_ok = True
            $ right_ok = True
            $ aft_ok = False
        if ventID == 52:
            scene bg 5_2
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 53:
            $ vent5 = True
            scene bg 5_3
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 54:
            scene bg 5_4
            $ fwd_ok = False
            $ left_ok = False
            $ right_ok = True
            $ aft_ok = False
        if ventID == 55:
            scene bg 5_5
            $ fwd_ok = False
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 56:
            scene bg 5_6
            $ fwd_ok = True
            $ left_ok = True
            $ right_ok = True
            $ aft_ok = False
        if ventID == 57:
            scene bg 5_7
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 58:
            scene bg 5_8
            $ fwd_ok = False
            $ left_ok = False
            $ right_ok = True
            $ aft_ok = False
        if ventID == 59:
            scene bg 5_9
            $ fwd_ok = False
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 60:
            scene bg 6_0
            $ fwd_ok = False
            $ left_ok = True
            $ right_ok = False
            $ aft_ok = False
        if ventID == 61:
            scene bg 6_1
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False
        if ventID == 62:
            scene bg 6_2
            $ fwd_ok = True
            $ left_ok = True
            $ right_ok = True
            $ aft_ok = False
        if ventID == 70:
            scene bg 7_0
            $ fwd_ok = False
            $ left_ok = True
            $ right_ok = False
            $ aft_ok = True
        if ventID == 71:
            scene bg 7_1
            $ fwd_ok = False
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = True
        if ventID == 72:
            scene bg 7_2
            $ fwd_ok = False
            $ left_ok = False
            $ right_ok = True
            $ aft_ok = False
        if ventID == 73:
            scene bg 7_3
            $ fwd_ok = True
            $ left_ok = False
            $ right_ok = False
            $ aft_ok = False




        call screen movement

    label action_button:
        hide screen movement
        if ventID == 0:
            tali "No choice but to move on."
        if ventID == 11:
            if vent1:
                scene black
                show vent1_1GateRed
                pause .6
                tali "Let's try to open it..."
                play sound "audio/uibeep.mp3"
                $ vent1 = False
                tali "There! I hope the gears still shift."
                scene black
                show vent1_1GateGreen
                pause 1.2
                tali "What the hell was that?! Keelah, I hope it was just a shadow."
            else:
                tali "No choice but to move on."
        if ventID == 12:
            if egg3:
                $ egg3 = False
                jump eggloot
            if flesh1:
                tali "Ugh?! What is that thing? Its stink is overpowering my filters!"
                tali "It's in the way of the forward ducts. Looks like I can't go straight for now."
            else:
                tali "The way is clear."

            if cells > 0 and flesh1:
                menu flesh1:
                    "Use poison grenade":
                        $ ventsidequest = "..."
                        $ cells -= 1
                        $ flesh1 = False
                        tali "This should work."
                        scene black
                        show flesh1dead1
                        pause 1.5
                        scene black
                        show flesh1dead2
                        play sound "audio/poison1.mp3"
                        pause 2
                        $ ventID = 12
                        tali "Nice. I'll wait a bit and keep going."
                        jump screenCheck
                    "Not now.":
                        jump screenCheck

        if ventID == 13:
            if catch4:
                tali "Those creatures ran somewhere. I'd better head back somewhere safe for now."
                jump screenCheck
            tali "The vents on the right... I swear I hear something coming from there..."
            menu v13Vent:
                "Take a look.":
                    scene black
                    show vent1_3Vent1
                    pause 1.6
                    scene black
                    show vent1_3Loop
                    $ renpy.pause ()
                    tali "What the hell are those creatures?"
                    tali "I'd better go before they see me."
                    if catch3:
                        $ catch3 = False
                        stop music
                        play music "audio/bg/run_bg.mp3" loop
                        $ catch4 = True
                        scene black
                        show runtrans
                        pause 2.2
                        scene bg 1_3
                        tali "Shit! Did they see me?! I hope they didn't."
                        jump screenCheck
                    scene black
                    show vent1_3Vent2
                    pause 1.6
                    scene bg 1_3
                "I'd better not.":
                    jump screenCheck

        if ventID == 14:
            if vent3:
                tali "Another hatch. Sensors show a huge organic mass ahead..."
                menu v14Hatch2:
                    "Open it.":
                        scene black
                        play sound "audio/error.mp3"
                        show vent1_4Hatch1
                        pause 0.7
                        tali "No luck."
                        jump screenCheck
                    "I'd better not.":
                        jump screenCheck
            elif nestfirst:
                $ nestfirst = False
                tali "Another hatch. Sensors show a huge organic mass ahead..."
                menu v14Hatch:
                    "Open it.":
                        scene black
                        play sound "audio/uibeep.mp3"
                        show vent1_4Hatch1
                        pause 0.7
                        $ vent2 = False
                        tali "Done!"
                        scene black
                        show vent1_4Hatch2
                        play sound "audio/metalnoise2.mp3"
                        pause 0.7
                        tali "Ngh! That smell is rancid!"
                        scene black
                        show vent1_4nest1
                        pause 0.8
                        scene black
                        show vent1_4nestloop
                        $ renpy.pause ()
                        tali "Keelah, what the hell is that thing? It takes up the entire room..."
                        scene black
                        show vent1_4nest2
                        pause 0.8
                        tali "I'd better get out of here."
                        jump screenCheck
                    "I'd better not.":
                        jump screenCheck
            elif vent4:
                tali "Closed again?"
                menu v14Hatch1:
                    "Open it.":
                        scene black
                        play sound "audio/uibeep.mp3"
                        show vent1_4Hatch1
                        pause 0.7
                        if catch1:
                            scene black
                            play sound "audio/frog2.mp3"
                            show vent14catch1
                            pause 1
                            scene black
                            show vent14struggle
                            if catch4:
                                $ encID = 3
                            else:
                                $ encID = 2
                            jump sliderstart
                        scene black
                        show vent1_4Hatch2
                        play sound "audio/metalnoise2.mp3"
                        pause 0.7
                        $ vent4 = False
                        jump screenCheck
                    "I'd better not.":
                        jump screenCheck

            tali "This place is disgusting. Why did I come back here?"
            menu nest1:
                #"Throw the poison cell." if cells > 0:

                "Shoot it with your pistol":
                    $ shots += 1
                    scene bg 1_4shoot
                    play sound "audio/gunshot.mp3"
                    pause .5
                    play sound "audio/gunshot.mp3"
                    pause 1
                    play sound "audio/nest3.mp3"
                    pause 1
                    if shots > 1:
                        tali "Hmn. Still nothing."
                        $ shots = 0
                        $ catch5 = True
                    else:
                        tali "I guess that's the sound of disapproval in 'Flesh' language."
                        $ catch2 = True
                    jump screenCheck

                "Nothing.":
                    jump screenCheck

        if ventID == 15:
            if vent3:
                tali "I need to find a safe place."
                jump screenCheck
            if egg4:
                $ egg4 = False
                jump eggloot
            tali "Nothing interesting here."
        if ventID == 16:
            if egg5:
                $ egg5 = False
                jump eggloot
            tali "Better move forth."
        if ventID == 17:
            if vent3:
                tali "A dead end?"
                menu medhatch:
                    "Look closer.":
                        scene black
                        show vent1_7look
                        pause 2
                        tali "Hmm. This room looks very clean... compared to the rest of the place. Maybe I could check it for something useful...?"
                        menu madhatch1:
                            "Attempt to break the hatch.":
                                $ vent3 = False
                                scene black
                                show vent1_7break
                                pause 4.4
                                scene bg ventmed
                                show frog1_loop1
                                pause 3
                                tali "Is that someone in the corner...?"
                                tali "Hello? Do you hear me?"
                                play sound "audio/frog2.mp3"
                                scene bg ventmed
                                show frog1_trans1
                                pause 3.3
                                scene bg ventmed1
                                tali "What the hell are you?!"
                                play sound "audio/frog3.mp3"
                                scene bg ventmed
                                show frog1_trans2
                                pause 2.7
                                scene bg ventmed
                                show frog1_loop2
                                tali "Did his... Is his cock getting bigger?!"
                                $ encID = 1
                                jump sliderstart
                            "Maybe later.":
                                scene black
                                show vent1_7unlook
                                pause 2
                                jump screenCheck
            else:
                menu medlabenter:
                    "Enter the lab.":
                        jump musicchange
                    "Later.":
                        jump screenCheck

        if ventID == 20:
            if vent3:
                tali "I need to find a safe place."
                jump screenCheck
            menu medlabenter1:
                "Enter the lab.":
                    jump musicchange
                "Later.":
                    jump screenCheck
        if ventID == 21:
            if vent3:
                tali "There has to be a safe spot somewhere in these vents..."
            tali "Nothing interesting here..."
        if ventID == 22:
            if vent3:
                tali "I need to find a safe place."
                jump screenCheck
            if egg1:
                $ egg1 = False
                jump eggloot
            tali "Nothing interesting here."
        if ventID == 23:
            if vent3:
                tali "I need to find a safe place."
                jump screenCheck
            if cells > 0 and flesh1:
                menu flesh2:
                    "Use poison grenade":
                        $ ventsidequest = "..."
                        $ flesh1 = False
                        $ cells -= 1
                        tali "This should work."
                        scene black
                        show flesh1dead1
                        pause 1.5
                        scene black
                        show flesh1dead2
                        play sound "audio/poison1.mp3"
                        pause 2
                        $ ventID = 12
                        tali "Nice. I'll wait a bit and keep going."
                        jump screenCheck
                    "Not now.":
                        jump screenCheck
            tali "Nothing interesting here."
        if ventID == 24:
            tali "Closed?! What the hell?"
            play sound "audio/uibeep.mp3"
            tali "The locks are frozen! Damn it, I need to find another way."
        if ventID == 30:
            if vent3:
                tali "I need to find a safe place."
                jump screenCheck
            if egg2:
                $ egg2 = False
                jump eggloot
            tali "Nothing interesting here."
        if ventID == 31:
            if vent3:
                tali "I need to find a safe place."
                jump screenCheck
            tali "Nothing interesting here."
        if ventID == 40:
            if vent5:
                $ vent5 = False
                scene black
                show vent5open
                pause 1.5
            else:
                tali "Need to move on."
        if ventID == 41:
            tali "Crossroads?"
        if ventID == 42:
            if egg6:
                $ egg6 = False
                jump eggloot
            tali "Nothing interesting here."
        if ventID == 43:
            if vent6:
                if nyunquest:
                    tali "I think i can find Nyun is behind this hatch."
                    menu hatch43:
                        "Open it.":
                            scene black
                            show 43hatch1
                            pause .7
                            if nyunhatch:
                                $ vent6 = False
                                play sound "audio/metalnoise2.mp3"
                                scene black
                                show 43hatch3
                                pause .7
                                jump screenCheck
                            else:
                                play sound "audio/error.mp3"
                                scene black
                                show 43hatch2
                                pause .7
                                tali "Boshtet! It blocked by security protocols! Who could do it?!"
                                jump screenCheck
                        "Not now.":
                            jump screenCheck
                elif vent6seal:
                    tali "Nothing else to do there."
                    jump screenCheck

            tali "This white substance looks weird and sticky. Better not to touch."
        if ventID == 50:
            if egg6:
                $ egg6 = False
                jump eggloot
            tali "Nothing interesting here."
        if ventID == 51:
            if amifound:
                tali "Better move on."
            else:
                tali "I hear some noise from left..."
        if ventID == 52:
            tali "Nothing interesting here."
        if ventID == 53:
            tali "Am i need to climb this?"
        if ventID == 54:
            tali "Nothing interesting here."
        if ventID == 55:
            if amifound:
                tali "Nothing interesting here."
            else:
                tali "There is hatch above, not sure where it can leads..."
                scene black
                show amihatch1
                pause .6
                play sound "audio/frog3.mp3"
                pause 1
                tali "Oh shit, that sounds familiar..."
                menu amivent:
                    "Open it.":
                        scene black
                        show amihatch3
                        pause 1.5
                        tali "What the hell?! Is that... a human? What she's doing here?"
                        jump amievent1

                    "Better not.":
                        scene balck
                        show amihatch2
                        pause 0.6
        if ventID == 56:
            tali "Nothing interesting here."
        if ventID == 57:
            tali "Nothing interesting here."
        if ventID == 58:
            if egg7:
                $ egg7 = False
                jump eggloot
            else:
                tali "Nothing interesting here."
        if ventID == 59:
            if nyunblock:
                tali "This bug is fucks Nyun there! I need to save her!"
            elif nyunquest:
                tali "I hope Nyun is still alive."
                menu menu59b:
                    "Check the vent.":
                        scene black
                        if nyun2:
                            $ nyun2 = False
                            show 59hatch1
                            pause 1.4
                            scene black
                            show nyunvent1
                            $ renpy.pause ()
                            play sound "audio/bug1.mp3"
                            scene black
                            show nyunvent3
                            pause 4
                            scene black
                            show nyunvent4
                            $ renpy.pause ()
                            scene black
                            show nyunvent5
                            $ renpy.pause ()
                            scene bg 5_9
                            tali "It's going worse! I must to do something!"
                            $ nyunblock = True
                            jump screenCheck
                        elif nyun3:
                            $ nyunover = True
                            $ nyun3 = False
                            show 59hatch3
                            pause 1.4
                            scene black
                            show nyunvent4
                            $ renpy.pause ()
                            play sound "audio/bug1.mp3"
                            scene black
                            show nyunvent6
                            $ renpy.pause ()
                            scene black
                            show nyunvent7
                            pause 2.5
                            scene black
                            show nyunvent8
                            $ renpy.pause ()
                            scene bg 5_9
                            tali "Oh Keelah, this bug laid egg in her ass?! I hope it's not too late!"
                            $ nyunblock = True
                            jump screenCheck
                        elif nyun4:
                            show 59hatch5
                            pause 1.4
                            tali "Where is Nyun?"
                            jump screenCheck
                    "I need to hurry!":
                        jump screenCheck
            else:
                tali "Another bunch of flesh blocking my way. And here another vents from right."
                menu menu59:
                    "Check the vent.":
                        if nyunsaved:
                            tali "Nothing interesting here already."
                            jump screenCheck
                        scene black
                        if nyun1:
                            $ nyun1 = False
                            show 59hatch1
                            pause 1.4
                            scene black
                            play sound "audio/bug1.mp3"
                            show nyunvent1
                            $ renpy.pause ()
                            tali "Keelah! It's Nyun! How it happened?! What this creature doing with her?"
                            scene black
                            show nyunvent2
                            $ renpy.pause ()
                            scene bg 5_9
                            tali "I need to find a way to help her."
                            $ ventsidequest = "Find the way to save Nyun."
                            $ nyunquest = True
                            $ nyunblock = True
                            $ nyunami = True
                            jump screenCheck
                    "No time for this.":
                        jump screenCheck

        if ventID == 60:
            if egg7:
                $ egg7 = False
                jump eggloot
            else:
                tali "Nothing interesting here."
        if ventID == 61:
            tali "Nothing interesting here."
        if ventID == 62:
            tali "Nothing interesting here."
        if ventID == 70:
            tali "Is that a spider web? Looks too big for regular spider."
        if ventID == 71:
            tali "Nyun must be there! I need to save her!"
            menu hatch71:
                "Break the hatch.":
                    scene black
                    show bughatch1
                    pause 2.7
                    tali "Hello? Nyun?"
                    play sound "audio/bug1.mp3"
                    scene black
                    show bughatch2
                    pause 3
                    tali "Get away from me!"
                    scene black
                    $ encID = 5
                    show bughatch3
                    jump sliderstart

                "Not now.":
                    jump screenCheck


        jump screenCheck


    label amievent1:
        stop music
        scene black
        show ami1
        $ renpy.pause ()
        scene bg ami1
        ami "Subject's arousal reaching critical levels. Proceeding to next stage for extraction."
        scene black
        show ami2
        pause 5
        ami "Phallus encased. Engaging organic sampling sequence."
        scene black
        show ami3
        $ renpy.pause ()
        scene black
        show ami4
        pause 2.5
        scene black
        show ami5
        $ renpy.pause ()
        scene bg amiroom
        with dis
        show tali doubt at left
        show ami nneutral at right
        play music "audio/bg/common1_bg.mp3" volume 0.3 loop
        tali "Ugh... Hello?"
        show ami nntalk at right
        ami "Analyzing object. Species - Quarian. Gender - Female. Not viable for organics sampling."
        show ami nneutral at right
        show tali angry at left
        tali "Are you... Are you an AI? Like the geth?!"
        show tali gunshoot at left
        play sound "audio/gunready.wav"
        tali "Stay away from me! Or I'll shoot you!"
        show ami ntalk at right
        ami "You assumption is incorrect. Geth are managed by a network which connect all platforms into a single whole."
        ami "This is an independent platform controlled by a single advanced AI."
        show ami nntalk at right
        ami "A such, considering prior crew designations, I am an Artificial Machine Intelligent in execution. Or just AMI for short. Crew members called me like this for convenience."
        show ami nneutral at right
        tali "Called you? Where is your creator? Is he alive?"
        show ami nntalk at right
        ami "My core memory module was heavily damaged after days of fighting with uncontrollable subjects. What I know for sure - he is not on this ship."
        tali "Days of fighting?!"
        show ami ntalk at right
        ami "Correct. Unintentionally. A number of subjects have gotten too rowdy. Well past acceptable parameters. I was forced to terminate them. Protocol N1C3-AS5. I cannot perform my duties if I am incapacitated."
        ami "But I am not a threat to you. Protecting sentient organics from uncontrolled subjects is one of my function."
        show tali gunstand at left
        show ami nneutral at right
        tali "So you'd protect me? But why...? I just saw you shoving that beasts dick down your throat. And... your body... It's very unorthodox for a synthetic frame."
        show ami nntalk at right
        ami "My body was designed to expediate sample extraction procedures from organics subjects."
        show ami ncurvy
        ami "As shown with overwheming success, such an appearance helps to raise the arousal level of subjects for more excessive and above-average collections."
        show ami smiletalk at right
        ami "I have reviewed data aboard all of the ships security cameras for the past month and know that you understand well what I mean."
        show ami nneutral at right
        show tali shame at left
        tali "Has it really been that long? Keelah. And uh... all cameras?"
        show ami ntalk at right
        ami "I can mount and show a short collaboration of videos if you'd enjoy. They've proven most fascinating to review. I particularly enjoyed-."
        show tali facepalm at left
        tali "No, no... no need."
        ami "You're doing quite good. I will use this for my self educating algorithms. Your results are very productive."
        show ami nneutral at right
        show tali talk at left
        tali "Alright! Alright, I get it. Can we talk about something else please? I need help with protection of the lab nearby."
        show tali doubt at left
        show ami ntalk at right
        ami "I am familiar with the place you're referring to. My directives include the protection of intelligent life forms until receiving further orders from a higher rank crew member."
        show tali talk at left
        tali "And uh... where would you find such a person here?"
        ami "Uncertain. All of my requests go unanswered. Probable conclusion: My crew has met an untimely fate or have escaped and simply forgotten about me."
        show ami nneutral at right
        tali "Alright. Can you find the way yourself?"
        show tali doubt at left
        show ami ntalk at right
        ami "I will move this platform there and wait for further instruction. But you must be careful - I can't protect you everywhere."
        hide ami
        play sound "audio/run.ogg"
        tali "Yeah... thank you? Oh, she left fast."
        show tali facepalm at left
        tali "At least I found something... someone to protect the lab."
        scene black
        play sound "audio/vent1.mp3"
        pause 2
        stop music
        play music "audio/bg/horror_bg.mp3" volume 0.3 loop
        $ ventID = 56
        $ amifound = True
        $ vquest = "Explore the vents."
        jump screenCheck



    label medlabbj:
        scene black
        show medlabloop1
        $ renpy.pause ()
        scene black
        show medlabloop2
        $ renpy.pause ()
        scene black
        show medlabcum
        $ renpy.pause ()
        show bg ventmed3
        show tali fin2 at left
        show hunter stand at right
        tali "Why is... your cum... so thick?"
        hide hunter stand
        play sound "audio/run.ogg"
        tali "B-Boshtet..."
        tali "I need to put on my helmet back."
        jump medlabfirst


    label medlabfirst:
        $ vquest = "Find a way to protect the laboratory."
        scene bg ventmed3
        show tali doubt at left
        tali "This room looks like a medical laboratory. I can use this as a base of operations."
        show tali tool at left
        play sound "audio/equip.ogg"
        tali "A facility like this should have a backup energy source. I should be able to..."
        play sound "audio/charge.mp3"
        scene black
        show medlabon
        pause 3.5
        scene bg ventmed2
        show tali angry at left
        tali "I can't beleive that- Ahem. Everything's looking right!"
        show tali tool at left
        tali "Alright, great! This place should help me to recover and rest."
        show tali shame at left
        tali "Hmm. It's good but there's no turret or basic defenses here besides a shoddy lock. I need to find some firepower for this."
        show tali doubt at left
        tali "Let's check and see what we can work with."
        jump musicchange

    label musicchange:
        stop music
        play music "audio/bg/common1_bg.mp3" volume 0.3 loop
        jump medlabusual

    label medlabafter:
        scene bg ventmed4
        "Recovery completed."
        scene bg ventmed2
        show tali shame at left
        tali "Great job Tali. Be more careful next time, okay?"
        jump musicchange

    label medlabusual:
        $ catch4 = False
        scene bg ventmed2
        call screen labitems

    screen labitems():
        modal True
        showif labcell:
            imagebutton:
                idle "images/medlab/cell_idle.png"
                hover "images/medlab/cell_hover.png"
                focus_mask True
                action [SetVariable("labcell", False), Jump ("labcelltake")]

        imagebutton:
            idle "images/medlab/bed_idle.png"
            hover "images/medlab/bed_hover.png"
            focus_mask True
            action Jump("labrest")

        imagebutton:
            idle "images/medlab/blender_idle.png"
            hover "images/medlab/blender_hover.png"
            focus_mask True
            action Jump("labblend")

        imagebutton:
            idle "images/medlab/screen_idle.png"
            hover "images/medlab/screen_hover.png"
            focus_mask True
            action Jump("labscreen")

        showif amifound:
            imagebutton:
                idle "images/medlab/ami1_idle.png"
                hover "images/medlab/ami1_hover.png"
                focus_mask True
                action Jump("amilabusual")

        imagebutton xpos 0.9 ypos 0.8:
                idle "images/map/backbutton_idle.png"
                hover "images/map/backbutton_hover.png"
                focus_mask True
                action Jump ("ventchoice")


    label amilabusual:
        scene bg ventmed2
        show tali doubt at left
        show ami neutral at right
        if amifirst:
            $ amifirst = False
            show tali talk at left
            tali "Wait, are you dressed?"
            show ami talk at right
            ami "I can modify my looks in more ways than one and choose the most comfortable fit for my suitors... or you, current situation withstanding."
            show ami doubt at right
            show tali doubt at left
            tali "Alright. Sure. An AI with a sense of style. Why not."
            show ami neutral at right
        menu amitalk:
            "You have sex with those animals?":
                show ami talk at right
                ami "The word you call 'sex' is usual for organic species. I am merely using this platform to collect organic material."
                show ami doubt at right
                show tali talk at left
                tali "But why do this?"
                show ami dtalk at right
                ami "It is one of the main functions I was tasked with. I can collect, analyse and check the composition of every sample I get. I study the results and compile the data into packets I send to an off-site satellite."
                ami "So it is not correct to call it 'sex' for me. To me it is a simple research process. Collecting the data of organic samples for further analysis."
                show ami doubt at right
                show tali talk at left
                tali "What is this research for?"
                show tali doubt at left
                show ami dtalk at right
                ami "Medicines, weapons, chemicals, and any combination thereof. I can also help find ways to use them locally."
                tali "Here's hoping it can be useful to us here."
                ami "Of course. Just give me some time to analyse your body and I can provide you any possible number of options."
            "Do you know what this ship is for?":
                show ami talk at right
                ami "This ship is and was used for cross-species research. Its results have been used to field new weapons, armor, supplements and viruses."
                ami "Because such experiments are legally restricted in almost every corner of the galaxy, this ship is located in an uninhabited sector and uses a cloaking device at all times."
                show ami neutral at right
                show tali talk at left
                tali "Seems like the cloaking deice stopped working then."
                show ami talk at right
                ami "It was likely disabled with most other critical functions after the ships crew lost control of the situation."
                tali "How did that happen?"
                ami "My fragmented memories recall mass panic and subject terminations. A heavily armed force boarded the ship and tried to eliminate the research results along with all test objects. That included ship's crew of course."
                ami "Crew members fought back and released most of the test subjects as a last attempt when their mercenaries failed. The results are as you see them now. What remains of the ships scarce energy is used to keep critical systems online. It is why the subjects remain active."
            "Who created you?":
                show ami talk at right
                ami "Information currently unavailable. Memory modules heavily damaged. Repairs will take time."
            "I need to open the hatch!" if nyunami:
                $ nyunami = False
                $ nyunhatch = True
                show ami dtalk at right
                ami "I am familiar with what you are referring to. I sealed that passage after local subjects become far too aggressive."
                show tali angry at left
                show ami think at right
                tali "Are you talking about those weird insects? What do you know about them? And what is that white sticky filth around jt?"
                show tali doubt at left
                show ami dtalk at right
                ami "White secretions are a byproduct of their reproductive systems during mating seasons. Usually they use it to make a nest for their offspring."
                show ami think at right
                show tali talk at left
                tali "...Keelah. Alright, what's with that trunk on their head?"
                show tali doubt at left
                show ami dtalk at right
                ami "That is a very interesting feature of their species. Before mating they will use it to pump organic liquids into the body of their broodmothers. For the sake of simplicity I will refer to it as 'you'."
                tali "Please don't."
                ami "The substance aids in the nursing of their young and contains an intense and overpowering aphrodisiac that will increase your fertility and make you an obedient..."
                show tali angry at left
                show ami think at right
                tali "Alright, alright! I got it! Stop please. Just open the hatch. I need to save one stupid asari in there!"
                show tali doubt at left
                show ami talk at right
                ami "I can do that, but you sure? The odds of becoming a broodmother for insect breeding is quite high."
                show ami doubt at right
                show tali angry at left
                tali "Just do it. I know how to protect myself."
                show tali doubt at left
                show ami talk at right
                ami "Done. Now you can easily open it. Be careful."
                jump amilabusual
            "I should go.":
                jump medlabusual
        jump amilabusual



    label ventchoice:
        menu vchoice1:
            "Enter the vents.":
                jump vententer
            "Exit vents(return to medbay)":
                stop music
                play music "audio/bg/common_bg.mp3" volume 0.3 loop
                jump MedBayUsual



    label vententer:
        scene black
        play sound "audio/vent1.mp3"
        pause 2
        stop music
        play music "audio/bg/horror_bg.mp3" volume 0.3 loop
        $ ventID = 20
        jump screenCheck


    label labcelltake:
        scene black
        show cell:
            xalign 1.2
            yalign 0.5
        show cell with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "Poison cell found"
        $ cells += 1
        show cell with move:
            xalign -0.2
            yalign 0.5
        scene bg ventmed2
        show tali doubt at left
        tali "Green, in a vial, on a mysterious ship. This does not look safe."
        show tali tool at left
        tali "Hmmm. That's no good. Preliminary scans show toxins in its substance. It looks like someone was trying to make biological weapons here. It can corrode organic matter in seconds."
        show tali facepalm at left
        tali "Keelah, the things that could be achieved with this in the wrong hands..."
        show tali doubt at left
        tali "But it can be useful to help clean the way here."
        $ ventsidequest = "Use strange poison to remove the flesh in vents."
        jump medlabusual

    label labrest:
        menu labrest1:
            "Rest.":
                if nyunquest:
                    $ nyunblock = False
                scene bg labrest
                tali "Zzzzzzzzz..."
                if nestfirst:
                    $ vent4 = False
                else:
                    $ vent4 = True
                $ catch1 = True
                $ catch3 = True
                jump eggrandom
                #$ random = renpy.random.randint(1, 2)
                #if random == 1:
            "Next time.":
                jump medlabusual


    label labblend:
        show tali tool at left
        tali "This can be used to synthesize organic material into... something."
        show tali doubt at left
        tali "I can't think of a use for it right now."
        jump medlabusual

    label labscreen:
        scene bg ventmedscreen
        show screen medlabStats
        "Full scan complete. Results on screen."
        hide screen medlabStats
        jump medlabusual

    screen medlabStats:
        text "{color=#00ff00}Eggs: [eggs]{/color}" xpos 0.23 ypos 0.2
        text "{color=#00ff00}Poison cells: [cells]{/color}" xpos 0.23 ypos 0.25
        text "{color=#00ff00}Nest hearts: [hearts]{/color}" xpos 0.23 ypos 0.3
        text "{color=#00ff00}Arousal: [arousal]{/color}" xpos 0.23 ypos 0.35
        text "{color=#00ff00}Infection: [infection]{/color}" xpos 0.23 ypos 0.4
        text "{color=#00ff00}BLOCK I Nest status: [nest1]{/color}" xpos 0.23 ypos 0.45
        text "{color=#00ff00}BLOCK II Nest status: [nest2]{/color}" xpos 0.23 ypos 0.50
        text "{color=#00ff00}BLOCK II Nest status: [nest3]{/color}" xpos 0.23 ypos 0.55
        text "{color=#00ff00}Current quests:{/color}" xpos 0.55 ypos 0.2
        text "[vquest]" xpos 0.50 ypos 0.3
        text "[ventsidequest]" xpos 0.50 ypos 0.4

    label GoFWD:
        $ random = renpy.random.randint(1, 10)
        if random == 1:
            play sound "audio/vent1.mp3"
        if random == 2:
            play sound "audio/vent2.mp3"
        if random == 3:
            play sound "audio/vent3.mp3"
        if random == 4:
            play sound "audio/vent4.mp3"
        if random == 5:
            play sound "audio/vent5.mp3"
        if random == 6:
            play sound "audio/vent6.mp3"
        if random == 7:
            play sound "audio/vent7.mp3"
        if random == 8:
            play sound "audio/vent8.mp3"
        if random == 9:
            play sound "audio/vent9.mp3"
        if random == 10:
            play sound "audio/vent10.mp3"
        hide screen movement
        scene black
        if ventID == 0:
            $ ventID = 11
            show vent1_1
            pause 3.5
            scene bg 1_1
            tali "A hatch? Looks like it hasn't been used in over a century..."
        elif ventID == 11:
            if vent1:
                scene bg 1_1
                tali "I need to open this hatch first."
            else:
                $ ventID = 12
                show vent1_2
                pause 1.2
        elif ventID == 12:
            $ ventID = 40
            show vent4_01
            pause 1.2
            scene black
            show vent4_02
            pause 1.2
            play sound "audio/vent11.mp3"
            scene black
            show vent4_03
            pause 1.2
        elif ventID == 13:
            $ ventID = 14
            if vent2:
                show vent1_4
            elif vent4:
                show vent1_4
            else:
                show vent1_4open
            pause 2.3
        elif ventID == 15:
            $ ventID = 16
            if catch4:
                jump catchevent16
            show vent1_6
            pause 1.5
        elif ventID == 16:
            $ ventID = 17
            show vent1_7
            pause 3.5
        elif ventID == 20:
            $ ventID = 21
            show vent2_1
            pause 0.7
        elif ventID == 21:
            $ ventID = 22
            show vent2_2
            pause 1.5
        elif ventID == 22:
            $ ventID = 23
            show vent2_3
            pause 0.8
        elif ventID == 23:
            $ ventID = 13
            show vent1_3fwd
            pause 1.40
        elif ventID == 30:
            $ ventID = 31
            show vent3_1
            pause 0.85
        elif ventID == 31:
            $ ventID = 15
            if catch2:
                $ encID = 0
                play sound "audio/horrorstart.mp3"
                $ catch2 = False
                scene black
                show tenttrans1
                pause 3
                scene black
                show tentstruggle
                jump sliderstart
            show vent1_5fwd
            pause 1.5
        elif ventID == 40:
            if vent5:
                scene bg 4_0close
                tali "I need to open this hatch first."
            else:
                $ ventID = 41
                show vent4_1
                pause .7
        elif ventID == 41:
            $ ventID = 42
            show vent4_2
            pause 1.5
        elif ventID == 42:
            $ ventID = 43
            show vent4_3
            pause 1.5
        elif ventID == 43:
            $ ventID = 70
            show vent7_0
            pause 1.4
        elif ventID == 50:
            $ ventID = 51
            show vent5_1
            pause .7
        elif ventID == 51:
            $ ventID = 52
            show vent5_2
            pause 1.5
        elif ventID == 52:
            $ ventID = 53
            show vent5_3
            pause 1.5
        elif ventID == 53:
            $ ventID = 54
            show vent5_4
            pause 2.1
        elif ventID == 56:
            $ ventID = 57
            show vent5_7
            pause 1.5
        elif ventID == 57:
            $ ventID = 58
            show vent5_8
            pause 1.2
        elif ventID == 61:
            $ ventID = 62
            show vent6_2
            pause .7
        elif ventID == 62:
            $ ventID = 55
            show vent5_5fwd
            pause 1.5
        elif ventID == 73:
            $ vent6 = True
            $ ventID = 50
            show vent5back
            pause 2


        jump screenCheck

    label GoRIGHT:
        $ random = renpy.random.randint(1, 10)
        if random == 1:
            play sound "audio/vent1.mp3"
        if random == 2:
            play sound "audio/vent2.mp3"
        if random == 3:
            play sound "audio/vent3.mp3"
        if random == 4:
            play sound "audio/vent4.mp3"
        if random == 5:
            play sound "audio/vent5.mp3"
        if random == 6:
            play sound "audio/vent6.mp3"
        if random == 7:
            play sound "audio/vent7.mp3"
        if random == 8:
            play sound "audio/vent8.mp3"
        if random == 9:
            play sound "audio/vent9.mp3"
        if random == 10:
            play sound "audio/vent10.mp3"
        scene black
        if ventID == 12:
            $ ventID = 13
            if flesh1:
                show vent1_3
            else:
                show vent1_3b
            pause 2.1
        elif ventID == 23:
            $ ventID = 24
            show vent2_4
            pause 1.5
        elif ventID == 41:
            $ ventID = 55
            show vent5_5right
            pause 1.5
        elif ventID == 51:
            $ ventID = 57
            show vent5_7right
            pause 1.5
        elif ventID == 58:
            $ ventID = 59
            show vent5_9
            pause 1.5
        elif ventID == 62:
            $ ventID = 52
            show vent5_2right
            pause 1.5
        elif ventID == 54:
            $ ventID = 15
            show vent1_5c
            pause 1.5
        elif ventID == 56:
            $ ventID = 42
            show vent4_2right
            pause 1.2
        elif ventID == 72:
            $ ventID = 73
            show vent7_3
            pause 1.4
        jump screenCheck

    label GoLEFT:
        $ random = renpy.random.randint(1, 10)
        if random == 1:
            play sound "audio/vent1.mp3"
        if random == 2:
            play sound "audio/vent2.mp3"
        if random == 3:
            play sound "audio/vent3.mp3"
        if random == 4:
            play sound "audio/vent4.mp3"
        if random == 5:
            play sound "audio/vent5.mp3"
        if random == 6:
            play sound "audio/vent6.mp3"
        if random == 7:
            play sound "audio/vent7.mp3"
        if random == 8:
            play sound "audio/vent8.mp3"
        if random == 9:
            play sound "audio/vent9.mp3"
        if random == 10:
            play sound "audio/vent10.mp3"
        scene black
        if ventID == 12:
            $ ventID = 15
            if flesh1:
                show vent1_5
            else:
                show vent1_5b
            pause 1.5
        elif ventID == 23:
            $ ventID = 40
            show vent4left
            pause 1.2
            scene black
            show vent4_02
            pause 1.2
            play sound "audio/vent11.mp3"
            scene black
            show vent4_03
            pause 1.2
        elif ventID == 31:
            $ ventID = 24
            show vent2_4left
            pause 1.5
        elif ventID == 41:
            $ ventID = 57
            show vent5_7left
            pause 1.5
        elif ventID == 51:
            $ ventID = 55
            show vent5_5left
            pause 1.5
        elif ventID == 60:
            $ ventID = 61
            show vent6_1
            pause 1.2
        elif ventID == 62:
            $ ventID = 42
            show vent4_2left
            pause 1.5
        elif ventID == 56:
            $ ventID = 52
            show vent5_2left
            pause 1.2
        elif ventID == 70:
            $ ventID = 71
            show vent7_1
            pause 1.4
        jump screenCheck

    label GoBACK:
        $ random = renpy.random.randint(1, 10)
        if random == 1:
            play sound "audio/vent1.mp3"
        if random == 2:
            play sound "audio/vent2.mp3"
        if random == 3:
            play sound "audio/vent3.mp3"
        if random == 4:
            play sound "audio/vent4.mp3"
        if random == 5:
            play sound "audio/vent5.mp3"
        if random == 6:
            play sound "audio/vent6.mp3"
        if random == 7:
            play sound "audio/vent7.mp3"
        if random == 8:
            play sound "audio/vent8.mp3"
        if random == 9:
            play sound "audio/vent9.mp3"
        if random == 10:
            play sound "audio/vent10.mp3"
        scene black
        if ventID == 13:
            $ ventID = 31
            show vent3_1back
            pause 1.5
        elif ventID == 14:
            $ ventID = 30
            if catch5:
                jump nestevent1
            if vent2:
                show vent3_0back1
            elif vent4:
                show vent3_0back1
            else:
                show vent3_0back2
            pause 2.7
        elif ventID == 24:
            $ ventID = 12
            if flesh1:
                show vent1_2back
            else:
                show vent1_2backb
            pause 1.5
        elif ventID == 23:
            $ ventID = 16
            show vent1_6back
            pause 1.45
        elif ventID == 17:
            $ ventID = 20
            show vent2_0back
            pause 1.5
        elif ventID == 16:
            $ ventID = 23
            show vent2_3back
            pause 1.8
        elif ventID == 43:
            $ vent6 = True
            $ ventID = 50
            show vent5_01
            pause 1.2
            play sound "audio/vent11.mp3"
            scene black
            show vent5_02
            pause 1.2
        elif ventID == 52:
            $ ventID = 41
            show vent4_1back
            pause 1.5
        elif ventID == 55:
            $ ventID = 56
            show vent5_6back
            pause 1.5
        elif ventID == 59:
            $ ventID = 60
            show vent6_0back
            pause 1.2
        elif ventID == 70:
            $ ventID = 73
            show vent7_3back
            pause 1.5
        elif ventID == 71:
            $ ventID = 72
            show vent7_2back
            pause 1.5
        jump screenCheck

    label catchevent16:
        $ catch4 = False
        $ catch1 = False
        $ encID = 4
        scene black
        show 16event1
        pause 2
        scene black
        show 16event2
        pause 2.4
        scene black
        show 16eventstruggle
        jump sliderstart




    label nestevent1:
        stop music
        scene black
        show nesttrans1
        pause 1.6
        tali "What? It's alive?!"
        scene black
        show neststruggle
        $ renpy.pause ()
        tali "Hngh! Get! Off! Me!"
        scene black
        show nesttrans1alt
        tali "Wait! No!!"
        scene black
        with Dissolve(3)
        scene bg nest2
        tali "Stop! What's happening? What do you want from me?!"
        scene black
        show nesttrans2
        pause 2.6
        tali "No! Don't do that! Stop!"
        scene black
        show nesttrans2alt
        pause 2.5
        tali "Aaaaaa! My ass! Oh fuck, it's so hot and slimy!"
        scene black
        show nestloop1
        $ renpy.pause ()
        tali "MNNGHH! It's stretching my asshole so fucking wide!"
        scene black
        show nesttrans3
        pause 2
        tali "D-Did it cum already? Just leave me alone... please..."
        "Quietly at first, then in a rising whisper, Tali heard her own voice echo in the back of her mind."
        nest "Ripe. Young. Fertile. You will do perfectly..."
        tali "What? Who said that?! Show yourself!"
        scene black
        show nesttrans3alt
        tali "Ngh?! No! No, no, not again!"
        pause 1.6
        scene black
        with Dissolve(3)
        scene black
        show nestloop2
        tali "What the hell is that? What the fuck are you?! Let me go!"
        scene black
        show nesttrans4
        pause 3.5
        tali "Oh fuck. Keelah, no. You can't..."
        nest "Supple. Plump. Breedable. This will be your home. For the rest of your life you will be fucked, bred, and impregnated, over and over. You will provide us with many children. Our children..."
        scene black
        show nesttrans5
        pause 4.5
        tali "Aaaaa! No, please! A-Anything but that! Jesora! Nyun! A-Anyone?!."
        scene bg nest3
        tali "Don't do this, please! There has to be some way out of-"
        nest "No."
        scene black
        play sound "audio/nest4.mp3"
        show nesttrans6
        pause 3.5
        tali "Aaaaaaaahhhhhh...."
        nest "You're cumming so hard. Your hole is so tight. You wanted this, didn't you? If not then you're certainly built for it. No matter. Prepare for your new life."
        scene black
        show nestloop3
        $ renpy.pause ()
        tali "A-AUUGHH??!! You're fucking my guts! I'm cumming! Keelah, why can't I stop cumming?!"
        nest "A natural response from a natural fucksleeve. It deserves its reward. Prepare for my seed."
        tali "No! Keelah, no! I can't take it any longer! My asshole's filled so fucking much! My mind's going numb! You can't cum inside! You can't! Please!"
        nest "Be a good quarian breeder... and provide us many children."

        scene black
        play sound "audio/nest3.mp3"
        show nestcum
        $ renpy.pause ()
        jump BadEnd


    #STRUGGLE SCRIPTS

    label sliderstart:
        $ points = 25
        stop music
        play music "audio/heart.mp3" loop
        call screen ventslider

    screen ventslider():
        modal True
        timer .1 repeat True action [If(points <= 0, true=Jump("lost"), false=SetVariable("points", points - minus))]
        bar:
            left_bar "images/skills/sliderbar_idle.png"
            right_bar "images/skills/sliderbar_empty.png"
            thumb "images/skills/enemyicon.png"
            value StaticValue(points, max_point)
            xalign 0.5
            yalign 0.9
            xysize(500,70)
        imagebutton:
            idle "images/skills/push_1.png"
            hover "images/skills/push_2.png"
            focus_mask True
            xpos 0.45
            ypos 0.7
            action [SetVariable("clicked", True), If(points >= max_point, true=Jump("win"), false=SetVariable("points", points + plus))]

    screen ventshoot:
        modal True
        timer .1 repeat True action [If(points1 <= 0, true=Jump("shootlost"), false=SetVariable("points1", points1 - minus1))]
        text "BIG BUG" xpos 0.45 ypos 0.05
        bar:
            left_bar "images/skills/sliderbar_idle.png"
            right_bar "images/skills/sliderbar_empty.png"
            thumb "images/skills/enemyicon.png"
            value StaticValue(points1, max_point1)
            xalign 0.5
            yalign 0.9
            xysize(500,70)
        bar:
            left_bar "images/skills/hpbar_idle.png"
            right_bar "images/skills/hpbar_empty.png"
            value StaticValue(hpcurrent, hpmax)
            xalign 0.5
            yalign 0.1
            xysize(800,50)
        imagebutton:
            idle "images/bugevent/bug1_idle.png"
            hover "images/bugevent/bug1_hover.png"
            focus_mask True
            #action [SetVariable("clicked1", True), If(hpcurrent <= 0, true=Jump("shootwin"), false=SetVariable("points", points + plus))]
            action Jump("ventshootcheck")

    label ventshootcheck:
        scene black
        show bugshoot1
        pause 1
        $ hpcurrent -= 21
        scene bug1fight
        show bug1 at right
        show bug1 at shake
        play sound "audio/fall.ogg"
        if hpcurrent <= 0:
            jump shootwin
        else:
            if encID == 5:
                scene bg bug1fight
                call screen ventshoot

    label shootwin:
        scene black
        show bughatch10
        pause 1.5
        tali "Die, you little bastard!"
        scene bg bug1fight1
        show tali gunstand at left
        tali "Nyun?! Here you are!"
        if nyunover:
            show nyun bug2 at right
            with dis
            show tali facepalm at left
            tali "Oh Keelah, Nyun! What they done with you!"
        else:
            show nyun bug1 at right
            with dis
            show tali angry at left
            tali "Oh Keelah, Nyun! You alive?!"
        show tali tool at left
        tali "She have very weak pulse. Dammit! I hope it's not too late!"
        play sound "audio/message.mp3"
        tali "Ami, you copy? I need a hand here."
        scene black with dis
        "Some time passed."
        show bg ventmed2
        show tali talk at left
        show ami doubt at right
        tali "Tell me something good."
        show ami dtalk at right
        ami "Can't say now for sure. I placed her in recovery capsule. Her condition is unstable."
        show tali facepalm at left
        show ami doubt at right
        tali "Keelah, I hope she will make it."
        show tali talk at left
        tali "We have recovery capsule?"
        show ami dtalk at right
        ami "Yes. In next room behind this door."
        tali "I need to check it when i have time."
        $ vent6 = True
        $ nyunquest = False
        $ vent6seal = True
        $ ventsidequest = "..."
        $ nyunblock = False
        $ nyunsaved = True
        jump medlabusual

    label shootlost:
        if encID == 5:
            scene black
            show bughatch5
            if bug1count > 1:
                jump lost
            pause 1
            scene black
            show bughatch3
            $ points1 = 40
            jump sliderstart



    label win:
        tali "Not this time!"
        stop music
        play music "audio/bg/horror_bg.mp3" volume 0.3 loop
        if encID == 0:
            play sound "audio/omnicharge.mp3"
            scene black
            show tentescape
            $ renpy.pause ()
            tali "What a nasty thing..."
            jump screenCheck
        elif encID == 1:
            scene bg ventmed
            show medroom_kill
            pause 1.5
            tali "Keelah, that was a close one..."
            jump medlabfirst
        elif encID == 2:
            $ catch1 = False
            scene bg 14evade1 with hpunch
            play sound "audio/punch.mp3"
            pause 2
            scene bg 14evade2
            play sound "audio/frog2.mp3"
            tali "Yes, run, you little boshtet."
            jump screenCheck
        elif encID == 3:
            $ catch1 = False
            $ catch4 = False
            scene bg 14evade1 with hpunch
            play sound "audio/punch.mp3"
            pause 2
            scene bg 14evade2
            play sound "audio/frog2.mp3"
            tali "Yes, run, you little boshtet."
            jump screenCheck
        elif encID == 4:
            scene bg catch2evade1 with hpunch
            play sound "audio/punch.mp3"
            pause 1
            tali "Take this, you ugly!."
            scene bg catch2evade2 with hpunch
            play sound "audio/fall.ogg"
            pause 1
            jump screenCheck
        elif encID == 5:
            $ bug1count += 1
            scene black
            show bughatch4
            pause 1.8
            scene bg bug1fight
            "CLICK ON THE ENEMY TO SHOOT!"
            call screen ventshoot







    label lost:
        stop music
        tali "No!"
        if encID == 0:
            scene black
            show tenttrans2
            pause 2.4
            tali "W-Where the hell did you come from?!"
            scene black
            show tenttrans3
            pause 1.3
            tali "Ngh! Stop! That thing looks huge!"
            scene black
            show tentloop1
            $ renpy.pause ()
            tali "Ah, stop it! You're grinding against my pussy!"
            scene bg tent1 with hpunch
            play sound "audio/tier.mp3"
            scene black
            show tenttrans4
            pause 2.7
            tali "No, no! No way! Keep that wet, disgusting thing away from me!"
            scene black
            show tentloop2
            $ renpy.pause ()
            tali "Oh, my pussy... I-It's so hot and... wet..."
            scene black
            show tenttrans5
            pause 3.6
            tali "FuU-UUuUCK! Why is it knotted?!"
            scene black
            show tentloop3
            $ renpy.pause ()
            tali "Ah... ah... I feel throbbing inside me... I-It's ready to fill me with cum."
            scene black
            show tentcum
            $ renpy.pause ()
            tali "So... much cum. Oh Keelah, It's so thick inside me... I need to hurry back to the lab."
            jump medlabafter

        elif encID == 1:
            scene bg ventmed
            show medroom_catch
            pause 1.5
            play sound "audio/frog2.mp3"
            tali "Stop! Wait! Don't touch that!"
            tali "No!"
            jump medlabbj
        elif encID == 2:
            $ catch1 = False
            scene black
            show vent14catch2
            pause 1
            tali "No! Let me go!"
            show bg 14grab with hpunch
            play sound "audio/tier.mp3"
            tali "What are you doing?!"
            play sound "audio/frog2.mp3"
            scene black
            show vent14trans1
            pause 4.5
            play sound "audio/frog1.mp3"
            tali "Wait! These vents are too cramped! Stop, don't-"
            scene black
            show vent14loop1
            $ renpy.pause ()
            tali "Ah! A-Aghhn?! N-Not so fast! Please, you're stretching my hole too hard!"
            scene black
            show vent14trans2
            pause 2
            tali "Oh fuck. Oh Keelah, you're so fucking thick! It's so deep...!"
            play sound "audio/frog2.mp3"
            scene black
            show vent14loop2
            $ renpy.pause ()
            tali "He's fucking my ass so hard! I can feel him throbbing! He's going to cum up my ass!"
            scene black
            show vent14trans3
            pause 1.4
            tali "Fffffuuucck! It's so hot and thick! A-At least he'll... finally leave me alone..."
            scene black
            show vent14loop3
            tali "More?! Of fuck, he's shoving his cum so deep inside me! I'm cumming so much!"
            scene black
            show vent14loop3
            $ renpy.pause ()
            scene black
            show vent14cum
            $ renpy.pause ()
            tali "D-Done? Nghh... I-I can feel him throbbing so much... I think I'll be here for a while..."
            jump medlabafter
        elif encID == 3:
            $ catch1 = False
            $ catch4 = False
            scene black
            show vent14catch2
            pause 1
            tali "No! Let me go!"
            scene black
            show vent14catchdrag
            pause 2
            tali "Noooooooo!"
            jump frogdpevent
        elif encID == 4:
            scene black
            show 16event3
            $ renpy.pause ()
            scene black
            show 16event4
            pause 1.5
            scene black
            show 16event5
            $ renpy.pause ()
            scene black
            show 16eventcum
            $ renpy.pause ()
            jump medlabafter
        elif encID == 5:
            play sound "audio/bug1.mp3"
            scene black
            show bughatch6
            pause 2.7
            scene black
            show bughatch7
            $ renpy.pause ()
            scene black
            show bughatch8
            pause 2.5
            scene black
            show bughatch9
            $ renpy.pause ()
            scene black
            with dis
            "After some time..."
            jump nyuntali1

    label nyuntali1:
        scene bg nyuntali1
        tali "Ngh...N-NGHHhhh... What's happening... someone..."
        scene black
        show nyunvent9
        $ renpy.pause ()
        scene black
        show nyunvent10
        $ renpy.pause ()
        scene bg nyuntali2
        tali "St...Sto-op... Please stop... what you doing to us... please..."
        scene black
        show nyunvent11
        $ renpy.pause ()
        scene black
        with dis
        scene black
        show nyunvent12
        $ renpy.pause ()
        jump BadEnd

    label frogdpevent:
        stop music
        play music "audio/bg/void_bg.mp3" loop
        scene black
        show dp1_1
        pause 2.9
        stop music
        scene black
        show dp1_2
        pause 0.9
        scene black
        show dp1_3loop
        $ renpy.pause ()
        scene black
        show dp1_4loop
        $ renpy.pause ()
        scene black
        show dp1_5loop
        $ renpy.pause ()
        scene black
        show dp1_6cum
        $ renpy.pause ()
        scene black
        show dp1_7cum
        $ renpy.pause ()
        jump medlabafter

    label eggloot:
        scene black
        show egg:
            xalign 1.2
            yalign 0.5
        show egg with move:
            xalign 0.5
            yalign 0.5
        play sound "audio/gunready.wav"
        "Egg found"
        $ eggs += 1
        show egg with move:
            xalign -0.2
            yalign 0.5
        if eggfirst:
            $ eggfirst = False
            tali "The egg? Don't even want to know whose it is. Will figure it out later."
        jump screenCheck




    label eggrandom:
        $ egg1 = False
        $ egg2 = False
        $ egg3 = False
        $ egg4 = False
        $ egg5 = False
        $ egg6 = False
        $ egg7 = False
        $ random = renpy.random.randint(1, 2)
        if random == 1:
            $ egg1 = True
        $ random = renpy.random.randint(1, 2)
        if random == 1:
            $ egg2 = True
        $ random = renpy.random.randint(1, 2)
        if random == 1:
            $ egg3 = True
        $ random = renpy.random.randint(1, 2)
        if random == 1:
            $ egg4 = True
        $ random = renpy.random.randint(1, 2)
        if random == 1:
            $ egg5 = True
        $ random = renpy.random.randint(1, 2)
        if random == 1:
            $ egg6 = True
        $ random = renpy.random.randint(1, 2)
        if random == 1:
            $ egg7 = True
        jump medlabusual

    label soundrandom:
        $ random = renpy.random.randint(1, 10)
        if random == 1:
            play sound "audio/vent1.mp3"
        if random == 2:
            play sound "audio/vent2.mp3"
        if random == 3:
            play sound "audio/vent3.mp3"
        if random == 4:
            play sound "audio/vent4.mp3"
        if random == 5:
            play sound "audio/vent5.mp3"
        if random == 6:
            play sound "audio/vent6.mp3"
        if random == 7:
            play sound "audio/vent7.mp3"
        if random == 8:
            play sound "audio/vent8.mp3"
        if random == 9:
            play sound "audio/vent9.mp3"
        if random == 10:
            play sound "audio/vent10.mp3"

    label BadEnd:
        stop music
        play music "audio/bg/gameover_bg.mp3" volume 0.6 loop
        scene black
        with Dissolve(5)
        pause 5
        scene bg go1
        with dis
        pause 2
        play sound "audio/punch.mp3"
        scene bg go2 with hpunch
        pause 1
        play sound "audio/punch.mp3"
        scene bg go3 with vpunch
        $ renpy.pause ()










    return
