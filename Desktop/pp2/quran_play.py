import pygame
import os

# initialize pygame
pygame.init()

# set up the window
size = width, height = 600, 400
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Music Player")

# set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# set up font
font = pygame.font.SysFont(None, 48)

pygame.mixer.init()
# load music files
music_dir = "/Users/kingz/Desktop/pp2/lab7/mus"
music_files = os.listdir(music_dir)
music_files.sort()
print(*music_files)

# set up current music index
current_music = 0
# set up music player
pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music]))

# set up playing status
is_playing = False

# set up play/pause animation
play_pause_images = [pygame.image.load("/Users/kingz/Desktop/pp2/lab7/animation/play-icon.png").convert_alpha(),
                     pygame.image.load("/Users/kingz/Desktop/pp2/lab7/animation/pause-icon.png").convert_alpha()]
play_pause_rect = play_pause_images[0].get_rect(center=(width//2, height-50))

# set up next/previous buttons
next_button_image = pygame.image.load("/Users/kingz/Desktop/pp2/lab7/animation/next-icon.png").convert_alpha()
next_button_rect = next_button_image.get_rect(center=(width-50, height-50))

prev_button_image = pygame.image.load("/Users/kingz/Desktop/pp2/lab7/animation/previous-icon.png").convert_alpha()
prev_button_rect = prev_button_image.get_rect(center=(50, height-50))

# define functions
def play_music():
    global is_playing
    pygame.mixer.music.play()
    is_playing = True

def pause_music():
    global is_playing
    pygame.mixer.music.pause()
    is_playing = False

def stop_music():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False

def next_music():
    global current_music, is_playing
    current_music = (current_music + 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music]))
    pygame.mixer.music.play()
    is_playing = True

def prev_music():
    global current_music, is_playing
    current_music = (current_music - 1) % len(music_files)
    pygame.mixer.music.load(os.path.join(music_dir, music_files[current_music]))
    pygame.mixer.music.play()
    is_playing = True

# set up the clock
clock = pygame.time.Clock()

# main game loop
while True:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if is_playing:
                    pause_music()
                else:
                    play_music()
            elif event.key == pygame.K_ESCAPE:
                stop_music()
            elif event.key == pygame.K_RIGHT:
                next_music()
            elif event.key == pygame.K_LEFT:
                prev_music()
    
    # set up the background
    screen.fill(white)
    
    # draw play/pause animation
    screen.blit(play_pause_images[is_playing], play_pause_rect)
    
    # draw next/previous buttons
    screen.blit(next_button_image, next_button_rect)
    screen.blit(prev_button_image, prev_button_rect)
    
    # draw current music info
    text = font.render(music_files[current_music], True, black)
    text_rect = text.get_rect(center=(width//2, height//2))
    screen.blit(text, text_rect)
    
    # update the screen
    pygame.display.flip()
    
    # set the frame rate
    clock.tick(60) 
