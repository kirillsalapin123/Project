import pygame
from random import randint as ri


class Monsters:
    speed = None
    mob_list = None
    mob_rect_x = WIDTH + 50
    x = None
    y = None
    a = None
    b = None
    anim = None

    def __init__(self, speed, a, b, anim):
        self.speed = speed
        self.a = a
        self.b = b
        self.anim = anim


    def mob(self, speed, mob_list, a, b, anim):
        check = ri(a, b)
        if check == 2:
            zombi_list.append(zombi[zombi_anim_count].get_rect(topleft=(zombi_rect_x, y)))
            zombi_rect_x -= 4

        if mob_list:
            for (i, el) in enumerate(mob_list):
                screen.blit(zombi[zombi_anim_count], el)
                el.x -= speed
                if el.x < -10:
                    mob_list.pop(i)
                zombi_collision_rect = el.inflate(-34, -34)
                if player_rect.colliderect(zombi_collision_rect):
                    player_health -= 1
                    mob_list.pop(i)