import tcod as libtcod


def render_all(con, entities, game_map, screen_width, screen_height, colors):
    # Print out the map
    for y in range(game_map.height):
        for x in range(game_map.width):
            wall = game_map.tiles[x][y].block_sight
            if wall:
                libtcod.console_set_char_background(
                    con, x, y, colors.get('dark_wall'), libtcod.BKGND_SET
                )
            else:
                libtcod.console_set_char_background(
                    con, x, y, colors.get('dark_ground'), libtcod.BKGND_SET
                )

    # Print all entities in the list
    for entity in entities:
        draw_entity(con, entity)
    libtcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    """
    Usage:
        Clear all entities on the map.
    Params:
        con: tcod.console object
        entities(list): a list of Entity class
    """
    for entity in entities:
        clear_entity(con, entity)


def draw_entity(con, entity):
    """
    Usage:
        Print the entity on the map.
    Params:
        con: tcod.console object
        entity: an Entity obj
    """
    libtcod.console_set_default_foreground(con, entity.color)
    libtcod.console_put_char(con, entity.x, entity.y,
                             entity.char, libtcod.BKGND_NONE)


def clear_entity(con, entity):
    """
    Usage:
        Print ' ' to override the entity on the map.
    Params:
        con: tcod.console object
        entity: an Entity obj
    """
    libtcod.console_put_char(con, entity.x, entity.y, ' ', libtcod.BKGND_NONE)
