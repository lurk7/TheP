Refactoring of combat

Current features
    - combined suittier1-3 functions into single function (enemy_attack_hits)
    - combined sliderBattleFuck1-3 into single function (slider_battle_fuck)
    - combined sex_skill1-3 into single function(sex_skill)
    - combined screen sliderfuck1-3 into single screen (sliderfuck)
    - organized lewd 'enemy_attack_hits' scenes into their own labels
    - organized lewd sex skill scenes into their own labels
    - reduced many repeated lines
    - combined all combat finishing logic into a single function (encounter_finished) from suittier, sex_skill, shoot, grenade, escape 
    - combined all enemy attacking logic into a single function to use shared counter-attack logic (enemy_attacks) from shoot_skill, sex_skill
    - combined all enemy attack hits logic (enemy_attack_hits) from enemy_attacks, escape_skill1
    - general clean-up of shoot and grenade skills

WIP
    - merge changes into main script file
        - deleted sliderFuck 1-3
        - deleted sliderbattlefuck 1-3
        - deleted suittier 1-3
        - deleted shoot_skill and grenade_skill
        - deleted escape_skill
        - deleted sex skill, sexskill 1-3
        - updated tease_skill
        - updated links in scripts.rpy to link to new functions
    

To-do 
    - bugs
        - double dialogue after sex defeat with varren
    - work on "screen logic():"


old lines 616 41 505 176   total ~ 1338
new lines 422 539 -16 -28 total ~ 917

old  flow is 
map -> encounter_chance -> rooms -> [comroom, warehouse, engine, corridor1 - 3 , barracks] -> [sliderBattleFuck1 - 3] -> screen[sliderfuck1 - 3] 
    -> skills [shoot_skill1, grenade_skill1, dart_skill, sex_skill, tease_skill, escape_skill1] -> [suittier1 - 3, sex_skill1 - 3]
roomID = comroom:1 engine_corridor:4 , warehouse_corridor:5, pool_corridor:11
 enemyID = creep:0 , biggy:1, varren:2, lizard:3