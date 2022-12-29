label lewd_creep_skill_1:
    if sexstage == 1:
        show sex1
    elif sexstage == 2:
        show sex2
    elif sexstage == 3:
        show sex2
        $ renpy.pause ()
        call display_room
        show cum1
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ngh. So much cum... "
    return

label lewd_creep_skill_2:
    if sexstage == 1:
        show sex3
    elif sexstage == 2:
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
    elif sexstage == 3:
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
    return

label lewd_varren_skill_1:
    if sexstage == 1:
        show sex7
    elif sexstage == 2:
        show sex8
    elif sexstage == 3:
        show sex8
        $ renpy.pause ()
        call display_room
        show cum4
        $ renpy.pause ()
        call display_room
        show tali fin1 at left
        tali "Ah, so much sperm... "
    return

label lewd_varren_skill_2:
    if sexstage == 1:
        show sex9
    elif sexstage == 2:
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
    elif sexstage == 3:
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
                $ renpy.pause ()
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