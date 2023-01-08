# building a gallery feature to test all animations are playing correctly
# TODO
# add different fuck poses to a loop

init python:
    # uncomment  line below to force gallery open at gamestart
    # config.label_overrides = {'splashscreen' : 'splashscreen_new'}
    config.developer = True



define debug_scene_list = [
    ['lewd_creep_skill_1',[1]],
    ['lewd_creep_skill_2',[20,35,99]],
    ['lewd_varren_skill_1',[1]],
    ['lewd_varren_skill_2',[20,35,99]],
    ['lewd_lizard_skill_1',[1]], 
    ['lewd_lizard_skill_2',[20,35,99]],
    ['lewd_varren_1',[1]], 
    ['lewd_varren_2',[1,30]], 
    ['lewd_varren_3',[1]],      # has fuckpose 1 and 2
    ['lewd_varren_4',[1]],      # has fuckpose 1 and 2  
    ['lewd_creep_1',[1]],       # has fuckpose 1 and 2  
    ['lewd_creep_2',[1]],       
    ['lewd_creep_3',[1]],       
    ['lewd_creep_4',[1]],       # has fuckpose 1 and 2
    ['lewd_lizzard_1',[1]],
    ['lewd_lizzard_2',[1,30]],
    ['lewd_lizzard_3',[1]],
    ['lewd_lizzard_4',[1]],
    ]

define debug_play_scene = ''
define debug_loop_scene_count = 0
define debug_loop_lewd_level_count = 0

screen scene_selector():

    vbox:
        textbutton 'play everything' action Call('play_all_scenes')
        for i, scene_item in enumerate(debug_scene_list):
            textbutton scene_item[0] action [SetVariable('debug_play_scene',debug_scene_list[i][0]), Call('play_all_lewd_stages')]



label splashscreen_new:
    call screen scene_selector
    jump splashscreen
    # call play_series_scenes

    # call lewd_creep_skill_1
    # $ renpy.pause ()
    # $ sexstage += 1
    # call display_room
    # call lewd_creep_skill_1
    # $ renpy.pause ()
    # $ sexstage += 1
    # call display_room
    # call lewd_creep_skill_1
    # $ renpy.pause ()



label play_all_scenes:
    # loop over each scene listed in scene listing
    while debug_loop_scene_count < len(debug_scene_list): 
        $ debug_play_scene = debug_scene_list[debug_loop_scene_count][0]
        'play scene [debug_play_scene]'
        call play_all_lewd_stages
        $ debug_loop_scene_count += 1
    return

label play_all_lewd_stages:
    # loop over each unique lewd level listed in the scene listing
    $ debug_loop_lewd_level_count = 0
    while debug_loop_lewd_level_count < len(debug_scene_list[debug_loop_scene_count][1]):
        $lewd = debug_scene_list[debug_loop_scene_count][1][debug_loop_lewd_level_count]
        'lewd:[lewd]'
        call play_all_sex_stages
        $ debug_loop_lewd_level_count += 1
    return


label play_all_sex_stages:
    # play all sex/fuck stages
    $ sexstage = 1
    $ fuckstage = 1
    while sexstage < 4:
        'sex/fuck stage:[sexstage]'
        call play_single_scene
        $ sexstage += 1
        $ fuckstage += 1
    return

label play_single_scene:
    $ room = 4
    call display_room
    call expression debug_play_scene
    $ renpy.pause ()
    return