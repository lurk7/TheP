transform right_creep1:
    xalign 1.0 ypos 1.1 yanchor 1.0
transform right_creep2:
    xalign 1.1 ypos 0.75 yanchor 1.0

transform right_varren1:
    xalign 1.0 ypos 1.05 yanchor 1.0
transform right_varren2:
    xalign 1.4 ypos 0.85 yanchor 1.0

transform right_lizard1:
    xalign 1.0 ypos 1.15 yanchor 1.0
transform right_lizard2:
    xalign 1.2 ypos 0.95 yanchor 1.0

transform shrink:
    zoom 0.9
transform shake2:
        ease .06 yoffset -24
        ease .06 yoffset 24
        ease .05 yoffset -20
        ease .05 yoffset 20
        ease .04 yoffset -16
        ease .04 yoffset 16
        ease .03 yoffset -12
        ease .03 yoffset 12
        ease .02 yoffset -8
        ease .02 yoffset 8
        ease .01 yoffset -4
        ease .01 yoffset 4
        ease .01 yoffset 0

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
    if not combat_second_enemy:
        if enemyID == 0:
            show creep stand at right
        elif enemyID == 2:
            show varren stand at right
        elif enemyID == 3:
            show lizard stand at right
    elif combat_second_enemy:
        if enemyID == 0:
            show creep stand at right_creep1 as creep1
            show creep stand at right_creep2,shrink as creep2 behind creep1
        elif enemyID == 2:
            show varren stand at right_varren1 as varren1
            show varren stand at right_varren2 as varren2 behind varren1
        elif enemyID == 3:
            show lizard stand at right_lizard1 as lizard1
            show lizard stand at right_lizard2 as lizard2 behind lizard1
    return

label display_battle_enemy_shake:
    if not combat_second_enemy:
        if enemyID == 0:
            show creep stand at right,shake
        elif enemyID == 1:
            show biggy stand at right,shake
        elif enemyID == 2:
            show varren stand at right,shake
        elif enemyID == 3:
            show lizard stand at right,shake
    elif combat_second_enemy:
        if enemyID == 0:
            show creep stand at right_creep1,shake as creep1
        elif enemyID == 2:
            show varren stand at right_varren1,shake as varren1
        elif enemyID == 3:
            show lizard stand at right_lizard1,shake as lizard1
    return

label display_battle_enemy_shake_both:
    if enemyID == 0:
        show creep stand at right_creep1,shake as creep1
        show creep stand at right_creep2,shake2 as creep2
    if enemyID == 2:
        show varren stand at right_varren1,shake as varren1
        show varren stand at right_varren2,shake2 as varren2
    if enemyID == 3:
        show lizard stand at right_lizard1,shake as lizard1
        show lizard stand at right_lizard2,shake2 as lizard2
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
    if not combat_second_enemy:
        if enemyID == 0:
            hide creep stand
        elif enemyID == 2:
            hide varren stand
        elif enemyID == 3:
            hide lizard stand
    elif combat_second_enemy:
        if enemyID == 0:
            hide creep1
            hide creep2
        elif enemyID == 2:
            hide varren1
            hide varren2
        elif enemyID == 3:
            hide lizard1
            hide lizard2
    return

label display_battle_disolve_enemy:
    if not combat_second_enemy:
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
    elif combat_second_enemy:
        if enemyID == 0:
            hide creep1
            with Dissolve(2)
        elif enemyID == 2:
            hide varren1
            with Dissolve(2)
        elif enemyID == 3:
            hide lizzard1
            with Dissolve(2)
    return

label display_battle_disolve_enemy_both:
    if enemyID == 0:
        hide creep1
        hide creep2
        with Dissolve(2)
    if enemyID == 2:
        hide varren1
        hide varren2
        with Dissolve(2)
    if enemyID == 3:
        hide lizard1
        hide lizard2
        with Dissolve(2)
    return

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
    if combat_second_enemy:
        if enemyID == 0:
            if suit > 8:
                show tali grab12 at shake
            elif suit == 8:
                show tali grab13 at shake
            elif suit == 7:
                show tali grab14 at shake
            elif suit == 6:
                show tali grab15 at shake
        elif enemyID == 2:
            if suit > 8:
                show tali grab16 at shake
            elif suit == 8:
                show tali grab17 at shake
            elif suit == 7:
                show tali grab18 at shake
            elif suit == 6:
                show tali grab19 at shake
        elif enemyID == 3:
            if suit > 8:
                show tali grab20 at shake
            elif suit == 8:
                show tali grab21 at shake
            elif suit == 7:
                show tali grab22 at shake
            elif suit == 6:
                show tali grab23 at shake
    else:
        if enemyID == 0:
            if suit > 8:
                show tali grab1 at shake
            elif suit == 8:
                show tali grab3 at shake
            elif suit == 7:
                show tali grab24 at shake
            elif suit == 6:
                show tali grab25 at shake
        elif enemyID == 2:
            if suit > 8:
                show tali grab6 at shake
            elif suit == 8:
                show tali grab7 at shake
            elif suit == 7:
                show tali grab26 at shake
            elif suit == 6:
                show tali grab27 at shake
        elif enemyID == 3:
            if suit > 8:
                show tali grab9 at shake
            elif suit == 8:
                show tali grab10 at shake
            elif suit == 7:
                show tali grab28 at shake
            elif suit == 6:
                show tali grab29 at shake
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
        show tali tease6 at left,shake
    return
