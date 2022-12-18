define been_defeated = False
define lewd_action = False
define has_escaped = False 
define enemy_dead = False

label grenade_skill1:
    $ alarm += 5
    $ grenades -= 1
    $ enemy_dead = True
    play sound "audio/gunready.wav"
    call display_battle_tali_grenade
    "Fire in the hole!"
    call display_battle_enemy_shake
    play sound "audio/explosion.mp3"
    "Devastating!"
    call display_battle_disolve_enemy
    "Enemy dead."
    jump encounter_finished

label escape_skill1:
        $ random = renpy.random.randint(1, 100)
        "Tali tries to run away!"
        if random < 51:
            play sound "audio/run.ogg"
            scene black
            "Escape successful."
            $ has_escaped = 1
            jump encounter_finished
        else :
            play sound "audio/creepone.mp3"
            "Escape failed..."
            jump enemy_attack_hits

label shoot_skill1:
    $ alarm += 1
    $ ammo -= 1
    play sound "audio/gunshot.mp3"
    "Tali shoots!"
    $ random = renpy.random.randint(1, 100)
    if random < 70:
        # shot hits
        play sound "audio/punch.mp3"
        call display_battle_enemy_shake
        "Hit!"
        $ enemyhp -= 1
        if enemyhp == 0 :
            # enemy dead
            call display_battle_disolve_enemy
            "Enemy defeated."
            $ enemy_dead = 1
            jump encounter_finished
        else:
            # enemy still alive and attacks back
            jump enemy_attacks
    else:
        # shot misses
        play sound "audio/miss.mp3"
        "Miss!"
        $ random = renpy.random.randint(1, 100)
        play sound "audio/creepone.mp3"
        call display_battle_enemy_shake
        "Enemy attacks!"
        jump enemy_attacks

label enemy_attacks:
    $ random = renpy.random.randint(1, 100)
    play sound "audio/creepone.mp3"
    call display_battle_enemy_shake
    "Enemy attacks!"
    if random > 30:
        # miss
        play sound "audio/miss.mp3"
        call display_battle_tali_evade
        "Miss!"
        jump slider_battle_fuck
    else:
        # hits
        $ random = renpy.random.randint(1, 100)
        play sound "audio/creepone.mp3"
        call display_battle_enemy_stand
        if random > 60:
            play sound "audio/miss.mp3"
            call display_battle_tali_evade
            "Miss!"
            jump slider_battle_fuck
        else:
            jump enemy_attack_hits

label sex_skill:
        "Tali tries getting closer..."
        $ random = renpy.random.randint(1, 100)
        call display_room
        if random > 30:
            $ lewd_action = 1 
            # skill success
            play sound "audio/fall.ogg"
            call display_battle_tali_grabs
            "Success!"
            call display_room
            if enemyID == 0:    
                if suit > 8:
                    call lewd_creep_skill_1
                elif suit > 6:
                    call lewd_creep_skill_2
            elif enemyID == 2:    
                if suit > 8:
                    call lewd_varren_skill_1
                elif suit == 8:
                    call lewd_varren_skill_2
            elif enemyID == 3:    
                if suit > 8:
                    call lewd_lizard_skill_1
                elif suit == 8:
                    call lewd_lizard_skill_2
        else:
            # skill failure
            call display_battle_tali_evade_shake
            play sound "audio/creepone.mp3"
            "Pushed back!"
            jump enemy_attacks
        if sexstage > 2:
            jump encounter_finished
        $ renpy.pause ()
        $ sexstage += 1
        jump slider_battle_fuck

    
label enemy_attack_hits:
    $ random = renpy.random.randint(1, 100)
    call display_battle_hide_enemy
    play sound "audio/fall.ogg"
    call display_battle_enemy_grabs
    "Tali failed to dodge!"
    if random > 50 and suit > 6:
        # suit damage action
        if suit == 9:
            play sound "audio/glass.mp3"
            "Helmet damaged!"
        else:
            if suit in [7,8]:
                play sound "audio/tier.mp3"
            "Suit damaged!"
        $ suit -= 1
        jump slider_battle_fuck
    else:
        # enemy starts a lewd action
        $ lewd_action = 1 
        call display_room
        if enemyID == 0:
            if suit > 8:
                call lewd_creep_1
            elif suit == 8:
                call lewd_creep_2
            elif suit == 7:
                call lewd_creep_3
            elif suit < 7:
                call lewd_creep_4            
        elif enemyID == 2:
            if suit > 8:
                call lewd_varren_1
            elif suit == 8:
                call lewd_varren_2
            elif suit == 7:
                call lewd_varren_3
            elif suit < 7:
                call lewd_varren_4
        elif enemyID == 3:
            if suit > 8:
                call lewd_lizzard_1
            elif suit == 8:
                call lewd_lizzard_2
            elif suit == 7:
                call lewd_lizzard_3
            elif suit < 7:
                call lewd_lizzard_4
    if fuckstage > 2:
        jump encounter_finished
    $ renpy.pause ()
    $ fuckstage += 1
    play sound "audio/punch.mp3"
    call display_battle_enemy_shake
    jump slider_battle_fuck

label encounter_finished:
    # event over, cleanup vars
    $ fuckstage = 1
    $ sexstage = 1
    $ lovedart = False
    $ corridor_fight = False
    if suit < 7 and not lewd_action:
        tali "Ah keelah, my suit is destroyed! I need to hurry to the medbay."
        $ been_defeated = 1
    if has_escaped and not been_defeated:
        $ has_escaped = 0
        if suit == 8:
            tali "That was close... I'd better go get my helmet."
        elif suit == 7:
            tali "D-Damned beast. My suits repair system's can't repair this fast enough..."
        $ suit = 10 
        scene bg map
        jump map 
    $ suit = 10
    if not lewd_action and not has_escaped:
        call display_battle_tali_finished
    if lewd_action:  # was finishing action lewd?
        $ lewd += 1
        $ lewd_action = 0
    if infection > 2:
        $ been_defeated = True
    if been_defeated:
        $ been_defeated = 0
        jump medbayafterdefeat
    else:
        scene black with Dissolve(2)
        tali "Tali continues on her way..."
        play sound "audio/walk.mp3"
        if roomID == 4:
            jump engine
        elif roomID == 5: 
            jump warehouse
        elif roomID == 11: 
            jump pool
        
screen sliderfuck():
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
        showif darts > 0 and lovedart == False and ((suit > 6 and enemyID == 0) or (suit > 7 and enemyID in [2,3])):
            imagebutton:
                idle "images/skills/dart_idle.png"
                hover "images/skills/dart_hover.png"
                focus_mask True
                xpos 0.45
                ypos 0.4
                action Jump("dart_skill")
        showif lewd > 20 and lovedart and ((suit > 6 and enemyID == 0) or (suit > 7 and enemyID in [2,3])):
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
        timer 5.5 action Jump("enemy_attack_hits")

label slider_battle_fuck:
    $ fuckpose = renpy.random.randint(1, 2)
    call display_room
    call battle_display_tali
    call display_battle_enemy_stand
    call screen sliderfuck

label tease_skill:
    call display_battle_tali_teases
    play sound "audio/slap.mp3"
    "Want this fat quarian ass? Come and get it."
    play sound "audio/creepone.mp3"
    pause 1
    jump enemy_attack_hits

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
    jump slider_battle_fuck

#########
# Images
#########

label battle_display_tali:
    if suit > 8:
        show tali gunshoot at left
    if suit == 8:
        show tali gunshoot69 at left
    if suit == 7:
        show tali gunshoot7 at left
    if suit < 7:
        show tali gunshoot6 at left   
    return

label display_battle_enemy_stand:
    if enemyID == 0:
        show creep stand at right
    elif enemyID == 2:
        show varren stand at right
    elif enemyID == 3:
        show lizard stand at right
    return

label display_battle_enemy_shake:
    if enemyID == 0:
        show creep stand at right
        show creep stand at shake
    elif enemyID == 1:
        show biggy stand at right
        show biggy stand at shake
    elif enemyID == 2:
        show varren stand at right
        show varren stand at shake
    elif enemyID == 3:
        show lizard stand at right
        show lizard stand at shake
    return

label display_battle_tali_evade:
    if suit > 8:
        show tali evade at left
    if suit == 8:
        show tali evade69 at left
    if suit == 7:
        show tali evade7 at left
    if suit < 7:
        show tali evade6 at left
    return

label display_battle_tali_evade_shake:
    if suit > 8:
        show tali evade at left
    if suit == 8:
        show tali evade69 at left
    if suit == 7:
        show tali evade7 at left
    if suit < 7:
        show tali evade6 at left
    return

label display_battle_tali_grenade:
    if suit > 8:
        show tali grenade at left
    if suit == 8:
        show tali grenade69 at left
    if suit == 7:
        show tali grenade7 at left
    if suit < 7:
        show tali grenade6 at left
    return

label display_battle_tali_finished:
    if suit > 8:
        show tali gunstand at left
    if suit == 8:
        show tali gunstand69 at left
    if suit == 7:
        show tali inj7 at left
    if suit < 7:
        show tali inj6 at left
    return

label display_battle_hide_enemy:
    if enemyID == 0:
        hide creep stand
    elif enemyID == 2:
        hide varren stand
    elif enemyID == 3:
        hide lizard stand
    return

label display_battle_disolve_enemy:
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
    
label display_room:
    if roomID == 1:
        scene bg comroom
    elif roomID == 4:    
        scene bg cor1
    elif roomID == 5:
        scene bg cor2
    elif roomID == 11:
        scene bg poolcor
    elif roomID == 0:
        scene bg med4
    return

label display_battle_tali_grabs:
    if enemyID == 0:
        if suit > 8:
            show tali grab1 at shake
        elif suit > 6 and suit < 9:
            show tali grab3 at shake
    elif enemyID == 2:
        if suit > 8:
            show tali grab6 at shake
        elif suit > 6 and suit < 9:
            show tali grab7 at shake
    elif enemyID == 3:
        if suit > 8:
            show tali grab9 at shake
        elif suit > 6 and suit < 9:
            show tali grab10 at shake
    return

label display_battle_enemy_grabs:
    if enemyID == 0:
        if suit > 8:
            show tali a11 at left,shake
        if suit == 8:
            show tali a12 at left,shake
        if suit == 7:
            show tali a13 at left,shake
        if suit < 7:
            show tali a14 at left,shake
    elif enemyID == 2:
        if suit > 8:
            show tali a21 at left,shake
        if suit == 8:
            show tali a22 at left,shake
        if suit == 7:
            show tali a23 at left,shake
        if suit < 7:
            show tali a24 at left,shake
    elif enemyID == 3:
        if suit > 8:
            show tali a31 at left,shake
        if suit == 8:
            show tali a32 at left,shake
        if suit == 7:
            show tali a33 at left,shake
        if suit < 7:
            show tali a34 at left,shake
    return


label display_battle_tali_teases:
    if suit > 8:
        show tali tease at left,shake
    if suit == 8:
        show tali tease69 at left,shake
    if suit == 7:
        show tali tease7 at left,shake
    if suit < 7:
        show tali tease7 at left,shake
    return