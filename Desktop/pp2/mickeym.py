import pygame
import time
import math

pygame.init()

size = width, height = 1000, 1000
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mickey Clock")

white = (255, 255, 255)
black = (0, 0, 0)

minute_hand_img = pygame.image.load("/Users/kingz/Desktop/pp2/lab7/mickey imgs/mickey_minute_hand.png").convert_alpha()
second_hand_img = pygame.image.load("/Users/kingz/Desktop/pp2/lab7/mickey imgs/mickey_second_hand.png").convert_alpha()

background_img = pygame.image.load("/Users/kingz/Desktop/pp2/lab7/mickey imgs/mickeyclock.jpeg").convert()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 48)

while True:
    current_time = time.localtime()
    seconds = current_time.tm_sec
    minutes = current_time.tm_min
    
    minute_angle = 90 - (minutes / 60) * 360
    second_angle = 90 - (seconds / 60) * 360
    
    minute_hand = pygame.transform.rotate(minute_hand_img, minute_angle)
    second_hand = pygame.transform.rotate(second_hand_img, second_angle)
    
    screen.blit(background_img, background_img.get_rect(center=(width//2, height//2)))
    pygame.draw.circle(screen, black, (width//2, height//2), 150, 5)
    pygame.draw.circle(screen, black, (width//2, height//2), 5)
    
    minute_hand_rect = minute_hand.get_rect(center=(width//2, height//2))
    second_hand_rect = second_hand.get_rect(center=(width//2, height//2))
    screen.blit(minute_hand, minute_hand_rect)
    screen.blit(second_hand, second_hand_rect)
    
    text = font.render(time.strftime("%H:%M:%S", time.localtime()), True, black)
    text_rect = text.get_rect(center=(width//2, height-50))
    screen.blit(text, text_rect)
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    clock.tick(60)
