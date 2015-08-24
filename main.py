# Flock
# A top-down horror game

import argparse
import cProfile
import os

import pygame
from pygame.locals import *

import flock

ONEONSQRT2 = 0.70710678118

def main(screenRes):
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode(screenRes, pygame.FULLSCREEN|pygame.DOUBLEBUF)
    pygame.display.set_caption('Flock')
    screenRect = screen.get_rect()

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0,0,0))

    #splash_screen = pygame.image.load(os.path.join("data", "title.png"))
    #splash_rect = splash_screen.get_rect()
    #splash_rect.center = screenRect.center

    f = flock.Flock(100)
    
    # Initialise clock
    clock = pygame.time.Clock()

    time = 0.0
    frames = 0
    start_time = pygame.time.get_ticks()
    min_fps = 200
    max_fps = 0

    while True:
        dt = clock.tick(200) / 1000.0
        time += dt
        frames += 1
        if time >= 1.0:
            fps = frames / time
            #min_fps = min(min_fps, fps)
            #max_fps = min(max_fps, fps)
            #avg_fps += frames
            if fps < 30:
                print("WARNING: Low framerate: "+str(fps)+" FPS")
            time = 0.0
            frames = 0

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return

        movedir = [0, 0]
        
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT]:
            movedir[0] -= 1
        if pressed[K_RIGHT]:
            movedir[0] += 1
        if pressed[K_UP]:
            movedir[1] -= 1
        if pressed[K_DOWN]:
            movedir[1] += 1

        if abs(movedir[0]) + abs(movedir[1]) == 2:
            movedir[0] *= ONEONSQRT2
            movedir[1] *= ONEONSQRT2

        f.update(dt)
            
        # Blit everything to the screen
        screen.blit(background, (0,0))
        pygame.display.flip()

def resolution(raw):
    a = raw.split("x")
    if len(a) != 2:
        raise ValueError()
    return (int(a[0]), int(a[1]))
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='A top-down stealth game.')
    parser.add_argument('--profile-file', action='store',
                        help="File to store profiling output in")
    parser.add_argument('-p', '--profile', action='store_true',
                        help="Enable profiling using cProfile")
    parser.add_argument('-r', '--resolution', action='store', type=resolution, default=(0,0),
                        help="Target screen resolution (e.g. 1920x1080)")
    args = parser.parse_args()
    if args.profile:
        cProfile.run("main(args.resolution)", filename=args.profile_file)
    else:
        main(args.resolution)
