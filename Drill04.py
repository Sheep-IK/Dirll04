from pico2d import *


TUK_WIDTH, TUK_HEIGHT = 800, 640
open_canvas( TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('birdreal.png')

def handle_events():
    global running , dir, updown
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                updown += 1
            elif event.key == SDLK_DOWN:
                updown -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                updown -= 1
            elif event.key == SDLK_DOWN:
                updown += 1

running = True
x = 800 // 2
y = 640 // 2
frame = 0
dir = 0
updown = 0
where = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH //2, TUK_HEIGHT // 2)
    if x > 800:
        x = 800
    elif x < 0:
        x = 0
    elif y < 0:
        y = 0
    elif y > 640:
        y = 640
    if dir == 0:
            character.clip_draw(frame*55, 238, 60, 55, x, y, 100, 100)
    if dir == -1:
           character.clip_draw(frame*55, 60, 55, 55, x, y, 100, 100)
    elif dir == 1:
            character.clip_composite_draw(frame * 55, 60, 55, 55, 0, 'h', x, y, 100 , 100)
    if updown == 1:
            character.clip_draw(frame*55, 183, 60, 55, x, y, 100, 100)
    elif updown == -1:
            character.clip_draw(frame*55, 238, 60, 55, x, y, 100, 100)

        
    update_canvas()
    handle_events()
    frame = (frame + 1) % 3
    x += dir * 20
    y += updown * 20
    delay(0.07)

close_canvas()

