import tcod as libtcod

from entity import Entity
from input_handlers import handle_keys
from render_functions import render_all, clear_all


def main():
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    player = Entity(int(screen_width / 2), int(screen_height / 2), '@', libtcod.white)
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), '@', libtcod.yellow)
    entities = [npc, player]

    libtcod.console_set_custom_font('resouces/arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
    libtcod.console_init_root(screen_width, screen_height, 'Rogue-like Mini-game', False)

    con = libtcod.console_new(screen_width, screen_height)

    key = libtcod.Key()
    mouse = libtcod.Mouse()

    # Game loop
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        render_all(con, entities, screen_width, screen_height)
        # Next line will print your whole setup (e.g. the line above)
        libtcod.console_flush()
        # Next line is pretty tricky.
        # It will be saved till next loop, and be printed by tcod.console_flush()
        clear_all(con, entities)
        # Next line is deprecated
        # key = libtcod.console_check_for_keypress()
        action = handle_keys(key)
        # Next lines use dict.get() method to get the movement tuples
        # or boolean values from the dictionaries
        move = action.get('move')  # tuples
        exit = action.get('exit')  # {'exit': True}
        fullscreen = action.get('fullscreen')  # {'fullscreen': True}

        if move:
            dx, dy = move  # unpack the tuples
            player.move(dx, dy)

        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())


if __name__ == "__main__":
    main()
