label lewd_creep_skill_1:
    if sexstage == 1:
        if dart_pose == 1:
            show sex1
        else:
            show dart1backmask1
    elif sexstage == 2:
        if dart_pose == 1:
            show sex2
        else:
            show dart1backmask2
    elif sexstage == 3:
        if dart_pose == 1:
            show sex2
            $ renpy.pause ()
            call display_room
            show cum1
            $ renpy.pause ()
        else:
            show dart1backmask2
            $ renpy.pause ()
            call display_room
            show dart1backmaskcum
            $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ngh. So much cum... "
    return

label lewd_creep_skill_2:
    if sexstage == 1:
        if dart_pose == 1:
            show sex3
        else:
            show dart1backnomask1
    elif sexstage == 2:
        if dart_pose == 1:
            if lewd < 30:
                show sex3alt
            elif lewd < 40:
                show tali grab3
                tali "So hard. I think I can do much better..."
                call display_room
                show sex4
            elif lewd > 40:
                show tali grab3
                tali "You like staring at my lips? Let me give you something to really look at..."
                call display_room
                show sex4
                $ renpy.pause ()
                call display_room
                show tali grab4
                tali "Keelah... I want him deep in my throat..."
                call display_room
                show sex5
                pause 3
                call display_room
                show sex6
        else:
            show tali lewd1
            tali "Ah, I feel his hard cock rubs my pussy..."
            play sound "audio/creepone.mp3"
            pause 1
            tali "You like my tight butt? Want to grab my body, aren't you?"
            call display_room
            show dart1backnomask2
            $ renpy.pause ()
    elif sexstage == 3:
        $ infection += 1
        if dart_pose == 1:
            if lewd < 30:
                show sex3alt
                $ renpy.pause ()
                call display_room
                show cum2
                $ renpy.pause ()
                call display_room
                show tali doubt69 at left
                tali "Well... one way or another."
            elif lewd < 41:
                show sex4alt
                $ renpy.pause ()
                call display_room
                show cum2
                $ renpy.pause ()
                call display_room
                show tali doubt69 at left
                tali "Done. Now where's me helmet...?"
            elif lewd > 40:
                show sex5
                pause 3
                call display_room
                show sex6alt
                $ renpy.pause ()
                call display_room
                show tali grab5
                tali "Mmm. My lips are wrapped so tight around your fat cock. Go on then... give me your cum. I don't want to spill a single drop."
                call display_room
                show cum3
                $ renpy.pause ()
                call display_room
                show tali fin2 at left
                tali "Silly girl, you went a little too crazy..."
        else:
            show dart1backnomask2
            $ renpy.pause ()
            tali "Mmmm... yes. Let me milk your dick with my hips..."
            call display_room
            show dart1backnomaskcum
            $ renpy.pause ()
            call display_room
            show tali doubt69 at left
            tali "Well... one way or another."
    return

label lewd_creep_skill_3:
    if sexstage == 1:
        show dart1backdamaged1
    elif sexstage == 2:
        show tali lewd2
        tali "Let's... I know a good use for such a hard fat cock... Let me show you..."
        call display_room
        show dart1backdamaged2
        $ renpy.pause ()
    elif sexstage == 3:
        $ infection += 1
        show dart1backdamaged2
        $ renpy.pause ()
        call display_room
        show dart1backdamagedcum1
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        tali "Ngh. So much cum... "
    return

label lewd_creep_skill_4:
    if sexstage == 1:
        show dart1backdamaged3
    elif sexstage == 2:
        show dart1backdamaged4
    elif sexstage == 3:
        $ infection += 1
        show dart1backdamaged4
        $ renpy.pause ()
        tali "Ah Keelah, yes! Don't stop, you bostet! Fill my quarian pussy with your hot monster jizz!"
        call display_room
        show dart1backdamagedcum2
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "Silly girl, you went a little too crazy..."
    return

label lewd_varren_skill_1:
    if sexstage == 1:
        if dart_pose == 1:
            show sex7
        else:
            show dart2backmask1
    elif sexstage == 2:
        if dart_pose == 1:
            show sex8
        else:
            show dart2backmask2
    elif sexstage == 3:
        if dart_pose == 1:
            show sex8
            $ renpy.pause ()
            call display_room
            show cum4
            $ renpy.pause ()
        else:
            show dart2backmask2
            $ renpy.pause ()
            call display_room
            show dart2backmaskcum
            $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ah, so much sperm... "
    return

label lewd_varren_skill_2:
    if sexstage == 1:
        if dart_pose == 1:
            show sex9
        else:
            show dart2backnomask1
    elif sexstage == 2:
        if dart_pose == 1:
            if lewd < 30:
                show sex10
            elif lewd < 41:
                show sex10
                $ renpy.pause ()
                call display_room
                show tali grab7
                tali "Such a nice red lollipop you have... Let me take some measurements..."
                call display_room
                show sex11
            elif lewd > 40:
                show sex10
                $ renpy.pause ()
                call display_room
                show tali grab7
                tali "Such a thick, bad doggy. Tali will have to punish you..."
                call display_room
                show sex11
        else:
            show dart2backnomask2
    elif sexstage == 3:
        $ infection += 1
        if dart_pose == 1:
            if lewd < 30:
                show sex10
                $ renpy.pause ()
                call display_room
                show cum5
                $ renpy.pause ()
                call display_room
                show tali doubt69 at left
                tali "Well... one way or another."
            elif lewd < 41:
                show sex11
                $ renpy.pause ()
                call display_room
                show cum6
                $ renpy.pause ()
                call display_room
                show tali doubt69 at left
                tali "Now where did I put my helmet...?"
            elif lewd > 40:
                show sex11
                $ renpy.pause ()
                call display_room
                show cum7
                $ renpy.pause ()
                call display_room
                show tali grab8
                tali "Mmmm, you filthy stray. You're not going anywhere until your cock is clean and polished..."
                call display_room
                show cum8
                $ renpy.pause ()
                call display_room
                show cum9
                $ renpy.pause ()
                call display_room
                show tali fin2 at left
                tali "Okay. Maybe I was a little too into it..."
        else:
            show dart2backnomask2
            $ renpy.pause ()
            call display_room
            show dart2backnomaskcum
            $ renpy.pause ()
            call display_room
            show tali doubt69 at left
            tali "Well... one way or another."
    return

label lewd_varren_skill_3:
    if sexstage == 1:
        show dart2backdamaged1
    elif sexstage == 2:
        show tali lewd3
        tali "Ahhh... I feel so hot between my hips, can you help me with that?"
        $ renpy.pause ()
        call display_room
        show dart2backdamaged2
        $ renpy.pause ()
        tali "Oh yes! Good boy! Keep it hard until I'm done..."
        call display_room
        show dart2backdamaged3
        $ renpy.pause ()
    elif sexstage == 3:
        $ infection += 1
        show dart2backdamaged3
        $ renpy.pause ()
        call display_room
        show dart2backdamagedcum1
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        tali "Ah, so much sperm... "
    return

label lewd_varren_skill_4:
    if sexstage == 1:
        show dart2backdamaged4
        $ renpy.pause ()
        call display_room
        show dart2backdamaged5
        $ renpy.pause ()
    elif sexstage == 2:
        show dart2backdamaged6
    elif sexstage == 3:
        $ infection += 1
        show dart2backdamaged6
        $ renpy.pause ()
        tali "Oh Keelah, oh Keelah... I'm cuming! Fuck me harder!"
        call display_room
        show dart2backdamagedcum2
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "Okay. Maybe I was a little too into it..."
    return

label lewd_lizard_skill_1:
    if sexstage == 1:
        show lizsex1
    elif sexstage == 2:
        show lizsex2
    elif sexstage == 3:
        show lizsex2
        $ renpy.pause ()
        call display_room
        show lizcum1
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ah, so much sperm... "
    return

label lewd_lizard_skill_2:
    if sexstage == 1:
        show lizsex3
    elif sexstage == 2:
        if lewd < 30:
            show lizsex4
        elif lewd < 41:
            show tali grab9
            tali "Mmm, let me take care of this with my mouth."
            call display_room
            show lizsex5
        elif lewd > 40:
            show tali grab9
            tali "Mmm, let me take care of this with my mouth."
            call display_room
            show lizsex5
    elif sexstage == 3:
        $ infection += 1
        if lewd < 30:
            show lizsex4
            tali "Ah, you're ready to cum..."
            call display_room
            show lizcum2
            $ renpy.pause ()
            call display_room
            show tali doubt69 at left
            tali "Well... one way or another."
        elif lewd < 41:
            show lizsex5
            $ renpy.pause ()
            tali "Mmm... his dick is throbbing in pleasure. Here. Dump your load between my tight, drooling lips."
            call display_room
            show lizcum3
            $ renpy.pause ()
            call display_room
            show tali doubt69 at left
            tali "Now where did I put my helmet...?"
        elif lewd > 40:
            $ random = renpy.random.randint(1, 2)
            show lizsex5
            $ renpy.pause ()
            if random == 1:
                call display_room
                show tali grab11 with hpunch
                play sound "audio/frog2.mp3"
                tali "What? W-Wait, you shouldn't be able to...!"
                call display_room
                show lizsex6
                pause 2
                tali "HMMPHPP!? The... tranquilizer... didn't work?!"
                call display_room
                show lizsex7
                $ renpy.pause ()
                tali "Oh Keelah yes... Fuck my face with your fat cock... Stretch my tight throat and clog it with your cum!"
                call display_room
                show lizcum4
            else:
                call display_room
                show lizsex5
                $ renpy.pause ()
                tali "MMm... his dick is throbbing in pleasure. Let me empty your balls in my mouth."
                call display_room
                show lizcum3
            $ renpy.pause ()
            call display_room
            show tali fin2 at left
            tali "Okay. Maybe I was a little too into it..."
    return

label lewd_lizard_skill_3:
    if sexstage == 1:
        show dart3backdamaged0
        $ renpy.pause ()
        call display_room
        show tali lewd4
        tali "Time to use your long lizard tongue... If you're good enough you might just be rewarded with some quarian booty."
        call display_room
        show dart3backdamaged1
        $ renpy.pause ()
    elif sexstage == 2:
        show tali lewd5
        tali "Here comes your prize. I hope you've got it wet enough to shove that hard cock up my tight asshole..."
        call display_room
        show dart3backdamaged2
        $ renpy.pause ()
        call display_room
        show dart3backdamaged3
        $ renpy.pause ()
    elif sexstage == 3:
        $ infection += 1
        show dart3backdamaged3
        $ renpy.pause ()
        call display_room
        show dart3backdamagedcum1
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        tali "Ah, so much sperm... "
    return

label lewd_lizard_skill_4:
    if sexstage == 1:
        show dart3backdamaged4
    elif sexstage == 2:
        show tali lewd6
        tali "Yes! Your slimy cock is going so deep inside me... Let me play with my wet pussy..."
        call display_room
        show dart3backdamaged5_12
        $ renpy.pause ()
    elif sexstage == 3:
        $ infection += 1
        show dart3backdamaged5_12
        $ renpy.pause ()
        tali "Let's cum together... Empty your sticky balls right up my tight ass!"
        call display_room
        show dart3backdamagedcum2
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        tali "Okay. Maybe I was a little too into it..."
    return

label lewd_varren_1:
    if fuckstage == 1:
        show frontvarmask1
    elif fuckstage == 2:
        show frontvarmask2
    elif fuckstage == 3:
        show frontvarmask2
        $ renpy.pause ()
        call display_room
        show frontvarmaskcum
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ugh... I feel so nasty. My suit is undamaged but... I think I can keep going after cleaning up."
    return

label lewd_varren_2:
    if fuckstage == 1:
        if lewd > 25:
            show frontvarnomask2
        else:
            show frontvarnomask1
    elif fuckstage == 2:
        if lewd > 25:
            show frontvarnomask2
            $ renpy.pause ()
            call display_room
            show frontvarnomask3
            pause 2.5
            call display_room
            show frontvarnomask4
        else:
            show frontvarnomask2
    elif fuckstage == 3:
        $ infection += 1
        if lewd > 25:
            show frontvarnomask4
            $ renpy.pause ()
            call display_room
            show frontvarnomask5
            pause 4
            call display_room
            show frontvarnomask6
            $ renpy.pause ()
            call display_room
            show frontvarnomaskcum2
        else:
            show frontvarnomask2
            $ renpy.pause ()
            call display_room
            show frontvarnomaskcum1
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection < 3:
            tali "T-That was way too much cum. My antibiotics should help, but... I really need to find my helmet before it gets any worse..."
        else :
            tali "I swallowed way too much... I have to get back to the medbay urgently."
            $ been_defeated = 1
    return

label lewd_varren_3:
    # blowjob or mount
    if fuckstage == 1:
        if fuckpose == 1:
            show backvar1     # lick 1
        else:
            show frontvardamaged1     # blow 1
    elif fuckstage == 2:
        if fuckpose == 1:
            show backvar2     # mount 1
        else:# blow 2
            show frontvardamaged2
    elif fuckstage == 3:     # blow 2 + cum
        $ infection += 1
        show frontvardamaged2
        $ renpy.pause ()
        call display_room
        show frontvardamagedcum
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection < 3:
            tali "T-That was too much cum. My antibiotics should help, but... I need to activate my suit's recover sequence before it gets worse..."
        else :
            tali "I swallowed too much... I have to get to the medbay urgently."
            $ been_defeated = 1
    return

label lewd_varren_4:
    if fuckstage == 1:
        show backvar3     # mount 1
    elif fuckstage == 2:
        show backvar4     # mount 2
    elif fuckstage == 3:     # mount 2 + cum
        $ infection += 1
        show backvar4
        $ renpy.pause ()
        call display_room
        show backvarcum1
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "Ahhh. My suit's in tatters... and my body's on fire. I hope I can make it back to the medbay..."
        $ been_defeated = 1
    return

label lewd_creep_1:
    if fuckstage == 1:
        if fuckpose == 1:
            show frontmask1
        else:
            show backmask1
    elif fuckstage == 2:
        if fuckpose == 1:
            show frontmask2
        else:
            show backmask2
    elif fuckstage == 3:
        if fuckpose == 1:
            show frontmask2
            $ renpy.pause ()
            call display_room
            show frontmaskcum
        else:
            show backmask2
            $ renpy.pause ()
            call display_room
            show backmaskcum
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ugh... I feel so nasty. My suit is undamaged but... I can keep going after some cleanup."
    return

label lewd_creep_2:
    if fuckstage == 1:
        show frontnomask1
    elif fuckstage == 2:
        show frontnomask2
    elif fuckstage == 3:
        $ infection += 1
        show frontnomask2
        $ renpy.pause ()
        call display_room
        show frontnomaskcum
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection < 3:
            tali "T-That was too much cum. My antibiotics should help, but... I need to find my helmet before it gets worse..."
            $ been_defeated = 1
    return
label lewd_creep_3:
    if fuckstage == 1:
        show frontnomask1
    elif fuckstage == 2:
        show frontnomask2
    elif fuckstage == 3:
        $ infection += 1
        show frontnomaskcum
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection < 3:
            tali "T-That was too much cum. My antibiotics should help, but... I need to activate suit recover sequence before it gets worse..."
        else :
            tali "I swallowed too much... I have to go to the medbay urgently."
            $ been_defeated = 1
    return

label lewd_creep_4:
    if fuckstage == 1:
        if fuckpose == 1:
            show frontdamaged1
        else:
            show backdamaged1
            pause 2
            call display_room
            show backdamaged2
    elif fuckstage == 2:
        if fuckpose == 1:
            show frontdamaged2
        else:
            show backdamaged2
    elif fuckstage == 3:
        $ infection += 1
        if fuckpose == 1:
            show frontdamaged2
            $ renpy.pause ()
            call display_room
            show frontdamagedcum
        else:
            show backdamaged2
            $ renpy.pause ()
            scene bg cor1
            show backdamagedcum
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "K-Keelah. My suit's in tatters... and my body's on fire. I need to head back to the medbay..."
        $ been_defeated = 1
    return


label lewd_lizzard_1:
    if fuckstage == 1:
        show liz1f1
    elif fuckstage == 2:
        show liz1f2
    elif fuckstage == 3:
        show liz1f2
        $ renpy.pause ()
        call display_room
        show liz1fcum1
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
    return

label lewd_lizzard_2:
    if fuckstage == 1:
        if lewd > 25:
            show liz1f4
        else:
            show liz1f3
    elif fuckstage == 2:
        if lewd > 25:
            show liz1f4
            $ renpy.pause ()
            call display_room
            show liz1f9
            pause 2
            call display_room
            show liz1f5
        else:
            show liz1f4
    elif fuckstage == 3:
        $ infection += 1
        if lewd > 25:
            show liz1f5
            $ renpy.pause ()
            call display_room
            show liz1f6
            pause 3.3
            call display_room
            show liz1f7
            $ renpy.pause ()
            call display_room
            show liz1fcum3
        else:
            show liz1f4
            $ renpy.pause ()
            call display_room
            show liz1fcum2
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection > 3:
            tali "I swallowed too much... I have to go to the medbay urgently."
            $ been_defeated = 1
    return
label lewd_lizzard_3:
    if fuckstage == 1:
        show liz1f8
    elif fuckstage == 2:
        show liz1b1
        pause 4
        $ renpy.pause ()
        call display_room
        show liz1b2
    elif fuckstage == 3:
        $ infection += 1
        show liz1b2
        $ renpy.pause ()
        call display_room
        show liz1bcum1
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection > 3:
            tali "I swallowed too much... I have to go to the medbay urgently."
            $ been_defeated = 1
    return
label lewd_lizzard_4:
    if fuckstage == 1:
        show liz1b3
        pause 2
        call display_room
        show liz1b4
    elif fuckstage == 2:
        show liz1b5
    elif fuckstage == 3:
        $ infection += 1
        show liz1b5
        $ renpy.pause ()
        call display_room
        show liz1bcum2
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "Ahhh. My suit's in tatters... and my body's on fire. I need to head back to the medbay..."
        $ been_defeated = 1
    return


    # DP SCENES ---------------------------------------------------------------

label dp_creep_1: # creeps DP if suit > 8
    if fuckstage == 1:
        show dp1mask1
    elif fuckstage == 2:
        show dp1mask2
    elif fuckstage == 3:
        show dp1mask2
        $ renpy.pause ()
        call display_room
        show dp1maskcum
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ugh... I feel so nasty. My suit is undamaged but... I can keep going after some cleanup."
    return

label dp_creep_2: # creeps DP if suit = 8 (no mask)
    if fuckstage == 1:
        show dp1nomask1
    elif fuckstage == 2:
        show dp1nomask2
    elif fuckstage == 3:
        $ infection += 1
        show dp1nomask2
        $ renpy.pause ()
        call display_room
        show dp1nomaskcum
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection < 3:
            tali "T-That was too much cum. My antibiotics should help, but... I need to find my helmet before it gets worse..."
            $ been_defeated = 1
    return

label dp_creep_3: # creeps DP if suit = 7
    if fuckstage == 1:
        show dp1nomask1
    elif fuckstage == 2:
        show dp1nomask2
    elif fuckstage == 3:
        $ infection += 1
        show dp1nomask2
        $ renpy.pause ()
        call display_room
        show dp1nomaskcum
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection < 3:
            tali "T-That was too much cum. My antibiotics should help, but... I need to activate suit recover sequence before it gets worse..."
        else :
            tali "I swallowed too much... I have to go to the medbay urgently."
            $ been_defeated = 1
    return

label dp_creep_4: # creeps DP if suit = 6
    if fuckstage == 1:
        show dp1damaged1
    elif fuckstage == 2:
        show dp1damaged1
    elif fuckstage == 3:
        $ infection += 1
        show dp1damaged1
        $ renpy.pause ()
        call display_room
        show dp1damagedcum1
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "K-Keelah. My suit's in tatters... and my body's on fire. I need to head back to the medbay..."
        $ been_defeated = 1
    return

label dp_varren_1: # varrens DP if suit > 8
    if fuckstage == 1:
        show dp2mask1
    elif fuckstage == 2:
        show dp2mask2
    elif fuckstage == 3:
        show dp2mask1
        $ renpy.pause ()
        call display_room
        show dp2maskcum
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ugh... I feel so nasty. My suit is undamaged but... I think I can keep going after cleaning up."
    return

label dp_varren_2: # varrens DP if suit = 8
    if fuckstage == 1:
        show dp2nomask1
    elif fuckstage == 2:
        show dp2nomask2
    elif fuckstage == 3:
        $ infection += 1
        show dp2nomask2
        $ renpy.pause ()
        call display_room
        show dp2nomaskcum
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection < 3:
            tali "T-That was way too much cum. My antibiotics should help, but... I really need to find my helmet before it gets any worse..."
        else :
            tali "I swallowed way too much... I have to get back to the medbay urgently."
            $ been_defeated = 1
    return

label dp_varren_3: # varrens DP if suit = 7
    if fuckstage == 1:
        show dp2damaged1
    elif fuckstage == 2:
        show dp2damaged2
    elif fuckstage == 3:
        $ infection += 1
        show dp2damaged2
        $ renpy.pause ()
        call display_room
        show dp2damagedcum1
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection < 3:
            tali "T-That was too much cum. My antibiotics should help, but... I need to activate my suit's recover sequence before it gets worse..."
        else :
            tali "I swallowed too much... I have to get to the medbay urgently."
            $ been_defeated = 1
    return

label dp_varren_4: # varrens DP if suit = 6
    if fuckstage == 1:
        show dp2damaged3
    elif fuckstage == 2:
        show dp2damaged4
    elif fuckstage == 3:
        $ infection += 1
        show dp2damaged4
        $ renpy.pause ()
        call display_room
        show dp2damagedcum2
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "Ahhh. My suit's in tatters... and my body's on fire. I hope I can make it back to the medbay..."
        $ been_defeated = 1
    return

label dp_lizzard_1: # lizards DP if suit > 8
    if fuckstage == 1:
        show dp3mask1
    elif fuckstage == 2:
        show dp3mask2
    elif fuckstage == 3:
        show dp3mask2
        $ renpy.pause ()
        call display_room
        show dp3maskcum
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
    return

label dp_lizzard_2: # lizards DP if suit = 8
    if fuckstage == 1:
        show dp3nomask1
    elif fuckstage == 2:
        show dp3nomask2
        $ renpy.pause ()
        call display_room
        show dp3nomask3
        pause 2
        call display_room
        show dp3nomask4
    elif fuckstage == 3:
        $ infection += 1
        show dp3nomask5
        pause 3
        call display_room
        show dp3nomask6
        $ renpy.pause ()
        call display_room
        show dp3nomaskcum1
        $ renpy.pause ()
        call display_room
        show dp3nomaskcum2
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection > 3:
            tali "I swallowed too much... I have to go to the medbay urgently."
            $ been_defeated = 1
    return

label dp_lizzard_3:# lizards DP if suit = 7
    if fuckstage == 1:
        show dp3damaged1
    elif fuckstage == 2:
        show dp3damaged2
    elif fuckstage == 3:
        $ infection += 1
        show dp3damaged2
        $ renpy.pause ()
        call display_room
        show dp3damagedcum1
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        if infection > 3:
            tali "I swallowed too much... I have to go to the medbay urgently."
            $ been_defeated = 1
    return
label dp_lizzard_4:# lizards DP if suit = 6
    if fuckstage == 1:
        show dp3damaged3
    elif fuckstage == 2:
        show dp3damaged4_08
    elif fuckstage == 3:
        $ infection += 1
        show dp3damaged4_08
        $ renpy.pause ()
        call display_room
        show dp3damagedcum2
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "Ahhh. My suit's in tatters... and my body's on fire. I need to head back to the medbay..."
        $ been_defeated = 1
    return

# DP dart scenes

label dp_creep_skill_1: # creeps dart DP if suit > 8
    if sexstage == 1:
        show dart1dp1mask1
    elif sexstage == 2:
        show dart1dp1mask2
    elif sexstage == 3:
        show dart1dp1mask2
        $ renpy.pause ()
        call display_room
        show dart1dp1maskcum
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ngh. So much cum... "
    return

label dp_creep_skill_2: # creeps dart DP if suit = 8
    if sexstage == 1:
        show dart1dp1nomask1
    elif sexstage == 2:
        show tali grab13
        tali "Oh Keelah... two fat cocks for a little quarian girl... I'll have to handle this with my mouth..."
        call display_room
        show dart1dp1nomask2
        $ renpy.pause ()
    elif sexstage == 3:
        if lewd < 30:
            show dart1dp1nomask2
            $ renpy.pause ()
            show tali grab13
            tali "Yes, you boshtets! Cover my face with your hot cum!"
            call display_room
            show dart1dp1nomaskcum1
            $ renpy.pause ()
            call display_room
            show tali doubt69 at left
            tali "Well... one way or another."
        else:
            show dart1dp1nomask2
            $ renpy.pause ()
            show tali lewd7
            tali "Come here, boy... I'll take care of you too..."
            call display_room
            show dart1dp1nomask3
            show tali lewd8
            play sound "audio/cumshot1.ogg"
            tali "Mmmm... yes. Take my head and push your dick into my mouth. Shoot your cum deep down my throat."
            call display_room
            show dart1dp1nomaskcum2
            $ renpy.pause ()
            show tali lewd9
            tali "Aaaaaaaaa... Come on... Make my mouth overflow with all your hot jizz, I want it all!"
            call display_room
            show dart1dp1nomaskcum3
            $ renpy.pause ()
            call display_room
            show tali fin2 at left
            tali "Silly girl, you went a little too crazy..."
    return

label dp_creep_skill_3: # creeps dart DP if suit = 7
    if sexstage == 1:
        show tali lewd10
        tali "Caught you! Come closer now, don't be shy..."
        show dart1dp1damaged1
    elif sexstage == 2:
        show dart1dp1damaged2
    elif sexstage == 3:
        show dart1dp1damaged2
        $ renpy.pause ()
        tali "Yes, yes... fuck me harder, you bastards! I've been a bad quarian bitch!"
        call display_room
        show dart1dp1damaged4
        pause 1.7
        call display_room
        show dart1dp1damagedcum1
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        tali "Silly girl, you went a little too crazy..."

    return

label dp_creep_skill_4: # creeps dart DP if suit = 6
    if sexstage == 1:
        show dart1dp1damaged3
    elif sexstage == 2:
        show dart1dp1damaged3
        $ renpy.pause ()
        call display_room
        show dart1dp1damaged5
        $ renpy.pause ()
        call display_room
        show dart1dp1damaged6
        $ renpy.pause ()
    elif sexstage == 3:
        show dart1dp1damaged6
        $ renpy.pause ()
        call display_room
        show dart1dp1damagedcum2
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "Silly girl, you went a little too crazy..."

    return

label dp_varren_skill_1: # varrens dart DP if suit > 8
    if sexstage == 1:
        show dart2dp2mask1
    elif sexstage == 2:
        show dart2dp2mask2
    elif sexstage == 3:
        show dart2dp2mask1
        $ renpy.pause ()
        call display_room
        show dart2dp2maskcum
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ah, so much sperm... "
    return

label dp_varren_skill_2: # varrens dart DP if suit = 8
    if sexstage == 1:
        show dart2dp2nomask1
    elif sexstage == 2:
        show dart2dp2nomask2
    elif sexstage == 3:
        show dart2dp2nomask2
        $ renpy.pause ()
        call display_room
        show dart2dp2nomaskcum
        $ renpy.pause ()
        call display_room
        show tali doubt69 at left
        tali "Now where did I put my helmet...?"
    return

label dp_varren_skill_3: # varrens dart DP if suit = 7
    if sexstage == 1:
        show dart2dp2damaged1
    elif sexstage == 2:
        show dart2dp2damaged2
        pause 1.4
        tali "You like that you dirty doggy? What about if I do this?"
        call display_room
        show dart2dp2damaged3
        $ renpy.pause ()
        call display_room
        show dart2dp2damaged4
        pause 2
        tali "Oh yes... that's the spot, my pussy feels so great with that doggy cock filling it!"
        call display_room
        show dart2dp2damaged5
    elif sexstage == 3:
        show dart2dp2damaged5
        $ renpy.pause ()
        tali "That's it, give me all that delicious doggy jizz. Fill me up with your hot canine cum..."
        call display_room
        show dart2dp2damagedcum1
        $ renpy.pause ()
        call display_room
        show dart2dp2damagedcum2
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        tali "Okay. Maybe I was a little too into it..."
    return

label dp_varren_skill_4: # varrens dart DP if suit = 6
    if sexstage == 1:
        show dart2dp2damaged6
    elif sexstage == 2:
        show dart2dp2damaged7
        pause 2.5
        tali "Hmmmpff... you... naughty, naughty doggy! How dare you to treat a quarian admiral like this... Well if I don't have any choice in the matter..."
        call display_room
        show dart2dp2damaged8
    elif sexstage == 3:
        show dart2dp2damaged8
        $ renpy.pause ()
        call display_room
        show dart2dp2damagedcum3
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "Silly girl, you went a little too crazy..."
    return

label dp_lizard_skill_1: # lizards dart DP if suit > 8
    if sexstage == 1:
        show dart3dp3mask1
    elif sexstage == 2:
        show dart3dp3mask2
    elif sexstage == 3:
        show dart3dp3mask2
        $ renpy.pause ()
        call display_room
        show dart3dp3maskcum
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ah, so much sperm... "
    return

label dp_lizard_skill_2:# lizards dart DP if suit = 8
    if sexstage == 1:
        show dart3dp3nomask1
    elif sexstage == 2:
        show dart3dp3nomask2
    elif sexstage == 3:
        show dart3dp3nomask2
        $ renpy.pause ()
        call display_room
        show dart3dp3nomaskcum
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        tali "Okay. Maybe I was a little too into it..."
    return

label dp_lizard_skill_3:# lizards dart DP if suit = 7
    if sexstage == 1:
        show dart3dp3damaged1
    elif sexstage == 2:
        show tali lewd11
        tali "What are you looking at, do you like the way my ass looks? Think you can handle something like this? "
        call display_room
        show dart3dp3damaged2
        pause 3.5
        tali "Mmmm... just let me prepare my tight hole for your cock..."
        call display_room
        show dart3dp3damaged3
    elif sexstage == 3:
        show dart3dp3damaged4
        $ renpy.pause ()
        call display_room
        show dart3dp3damagedcum1
        $ renpy.pause ()
        call display_room
        show tali fin2 at left
        tali "Okay. Maybe I was a little too into it..."
    return

label dp_lizard_skill_4:# lizards dart DP if suit = 6
    if sexstage == 1:
        show dart3dp3damaged5
    elif sexstage == 2:
        show dart3dp3damaged6_09
    elif sexstage == 3:
        show dart3dp3damaged6_09
        tali "Ah Keelah! Your slimy cock feels so good up my asshole... Don't pull out, please... Stretch it harder... I want my butt filled with all your hot lizard cum!"
        call display_room
        show dart3dp3damagedcum2
        $ renpy.pause ()
        call display_room
        show tali fin3 at left
        tali "Silly girl, you went a little too crazy..."
    return
