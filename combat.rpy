define been_defeated = False
define lewd_action = False
define has_escaped = False
define enemy_dead = False
define combat_second_enemy = False
define combat_second_dead = False

label grenade_skill1:
    $ alarm += 5
    $ grenades -= 1
    $ enemy_dead = True
    play sound "audio/gunready.wav"
    call display_battle_tali_grenade
    "Fire in the hole!"
    if combat_second_enemy:
        call display_battle_enemy_shake_both
        play sound "audio/explosion.mp3"
        "Devastating!"
        call display_battle_disolve_enemy_both
        $ combat_second_enemy = False
        "Both enemies are dead!"
    else:
        call display_battle_enemy_shake
        play sound "audio/explosion.mp3"
        "Devastating!"
        call display_battle_disolve_enemy
        "The enemy is dead!"
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
        if enemyhp < 1 :
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
        jump enemy_attacks

label combat_second_enemy_joins:
    $ combat_second_enemy = True
    return

label combat_event_chance:
    $ random = renpy.random.randint(1, 100)
    if not combat_second_enemy and not combat_second_dead:
        if random > 80 :
            if not enemyID == 0:
                return
            "Alert!! Additional enemy approaching"
            call display_battle_hide_enemy
            call combat_second_enemy_joins
            call display_battle_enemy_stand
            "He patiently waits his turn"
            jump slider_battle_fuck
    return

label enemy_attacks:
    $ random = renpy.random.randint(1, 100)
    call combat_event_chance
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
        if random > 30:
            call display_room
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
            call display_battle_enemy_shake
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
    if combat_second_enemy:
        "One down, One to go"
        # reset state with new enemy
        $ enemyhp = 5
        call display_battle_hide_enemy
        $ combat_second_enemy = False
        $ combat_second_dead = True
        jump enemy_attacks
    $ corridor_fight = False
    $ combat_second_enemy = False
    $ combat_second_dead = False
    if suit < 7:
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