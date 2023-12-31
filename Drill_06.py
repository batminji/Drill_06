from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

hand = load_image('hand_arrow.png')
keroro_left_down = load_image('keroro_left_down.png')
keroro_right_down = load_image('keroro_right_down.png')
keroro_left_up = load_image('keroro_left_up.png')
keroro_right_up = load_image('keroro_right_up.png')
TUK_ground = load_image('TUK_GROUND.png')

hand_points = [(600, 800)]

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_MOUSEMOTION:
            global mouse_x, mouse_y
            mouse_x, mouse_y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            hand_points.append((event.x, TUK_HEIGHT - 1 - event.y))

running = True
keroro_x, keroro_y  = TUK_WIDTH // 2, TUK_HEIGHT // 2
mouse_x, mouse_y = 0, 0
hand_x, hand_y = 400, 300
hide_cursor()
frame = 0
i = 0

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(mouse_x, mouse_y)
    for p in range(len(hand_points)):
        hand.draw(hand_points[p][0], hand_points[p][1])
    if i < 100 and len(hand_points) > 0:
        t = i / 100
        x = (1 - t) * keroro_x + t * hand_points[0][0]
        y = (1 - t) * keroro_y + t * hand_points[0][1]
        i += 4
    elif i >= 100:
        i = 0
        keroro_x, keroro_y = hand_points[0][0], hand_points[0][1]
        hand_points.pop(0)

    if len(hand_points) > 0:
        if hand_points[0][0] > keroro_x and hand_points[0][1] > keroro_y:
            keroro_right_up.clip_draw(frame * 290, 0, 290, 345, x, y, 125, 160)
        elif hand_points[0][0] < keroro_x and hand_points[0][1] > keroro_y:
            keroro_left_up.clip_draw(frame * 290, 0, 290, 345, x, y, 125, 160)
        elif hand_points[0][0] > keroro_x and hand_points[0][1] < keroro_y:
            keroro_right_down.clip_draw(frame * 260, 0, 260, 350, x, y, 125, 160)
        elif hand_points[0][0] < keroro_x and hand_points[0][1] < keroro_y:
            keroro_left_down.clip_draw(frame * 260, 0, 260, 350, x, y, 125, 160)
    else:
        keroro_left_down.clip_draw(frame * 260, 0, 260, 350, x, y, 125, 160)

    update_canvas()
    frame = (frame + 1) % 4
    delay(0.08)
    handle_events()

close_canvas()