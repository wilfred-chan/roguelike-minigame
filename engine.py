import tcod as libtcod

from entity import Entity, get_blocking_entity
from fov_functions import initialize_fov, recompute_fov
from game_states import GameStates
from input_handlers import handle_keys
from map_objects.game_map import GameMap
from render_functions import render_all, clear_all


def main():
    # Initialize default windows & map sizes
    screen_width = 80
    screen_height = 50
    map_width = 80
    map_height = 45

    # Initialize default colors of wall & ground & FOV
    colors = {
        'dark_wall': libtcod.Color(0, 0, 100),
        'dark_ground': libtcod.Color(50, 50, 150),
        'light_wall': libtcod.Color(130, 110, 50),
        'light_ground': libtcod.Color(200, 180, 50)
    }

    # Initialize player and entities list
    player = Entity(int(screen_width / 2), int(screen_height / 2),
                    '@', libtcod.white, 'player', blocks=True)
    entities = [player]

    # Initialize default font & window title
    libtcod.console_set_custom_font(
        'resouces/arial10x10.png',
        libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD
    )
    libtcod.console_init_root(
        screen_width, screen_height, 'Rogue-like Mini-game', False
    )

    # Initialize the console windows for gaming
    con = libtcod.console_new(screen_width, screen_height)

    # Initialize the game map with the default size
    game_map = GameMap(map_width, map_height)
    game_map.make_map(player, entities, max_monsters_per_room=5)

    # Initialization of Filed of View
    fov_algorithm = 0
    fov_light_walls = True
    fov_radius = 8
    fov_recompute = True
    fov_map = initialize_fov(game_map)

    # Keyboard & Mouse event stuff
    key = libtcod.Key()
    mouse = libtcod.Mouse()

    game_state = GameStates.PLAYER_TURN

    # Game loop
    while not libtcod.console_is_window_closed():
        libtcod.sys_check_for_event(libtcod.EVENT_KEY_PRESS, key, mouse)

        if fov_recompute:
            recompute_fov(fov_map, player.x, player.y, fov_radius,
                          fov_light_walls, fov_algorithm)

        render_all(
            con, entities, game_map,
            fov_map, fov_recompute,
            screen_width, screen_height, colors
        )
        # Next line will print your whole setup (e.g. the line above)
        libtcod.console_flush()
        # Next line is pretty tricky.
        # It will be saved till next loop,
        # and be printed by tcod.console_flush()
        clear_all(con, entities)

        action = handle_keys(key)

        # Next lines use dict.get() method to get the movement tuples
        # or boolean values from the dictionaries
        move = action.get('move')  # tuples
        exit = action.get('exit')  # {'exit': True}
        fullscreen = action.get('fullscreen')  # {'fullscreen': True}

        if move and (game_state == GameStates.PLAYER_TURN):
            dx, dy = move  # unpack the tuples
            if not game_map.is_blocked(player.x + dx, player.y + dy):
                blocking_entity = get_blocking_entity(
                    entities, player.x + dx, player.y + dy
                )
                if blocking_entity is None:
                    player.move(dx, dy)
                    fov_recompute = True
                    game_state = GameStates.ENEMY_TURN
                else:
                    print('You kick the {}!'.format(blocking_entity.name))
        if exit:
            return True

        if fullscreen:
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

        if game_state == GameStates.ENEMY_TURN:
            for entity in entities:
                if entity != player:
                    print(
                        'The {} looks at you. And moves.'.format(entity.name)
                    )
                    game_state = GameStates.PLAYER_TURN


if __name__ == "__main__":
    main()
