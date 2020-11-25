import tcod as libtcod
from input_handlers import handle_keys


def main():
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    libtcod.console_set_custom_font('resouces/arial10x10.png',libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'libtcod tutorial', False)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        libtcod.console_set_default_foreground(0, libtcod.white)
        libtcod.console_put_char(0, player_x, player_y, '@', libtcod.BKGND_NONE)
        libtcod.console_flush()

        # Next line is deprecated
        # key = libtcod.console_check_for_keypress()
        action = handle_keys(key)
        # Next lines use dict.get() method to get the movement tuples
        # or boolean values from the dictionaries
        move = action.get('move')  # tuples
        exit = action.get('exit')  # True
        fullscreen = action.get('fullscreen')  # True

        if move:
            dx, dy = move  # unpack the tuples
            player_x += dx
            player_y += dy
        
        if exit:
            return True
        
        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())



if __name__ == "__main__":
    main()
