import tcod as libtcod


def render_all(con, entities, game_map, fov_map, fov_recompute,
               screen_width, screen_height, colors):
    if fov_recompute:
        for y in range(game_map.height):
            for x in range(game_map.width):
                wall = game_map.tiles[x][y].block_sight
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                if visible:
                    game_map.tiles[x][y].explored = True
                explored = game_map.tiles[x][y].explored
                # Uncomment below section if you want light in FOV
                # ----------------------------------------------------
                if visible:  # Current tile is in FOV
                    if wall:
                        libtcod.console_set_char_background(
                            con, x, y, colors.get('light_wall'),
                            libtcod.BKGND_SET
                        )
                    else:
                        libtcod.console_set_char_background(
                            con, x, y, colors.get('light_ground'),
                            libtcod.BKGND_SET
                        )
                else:  # Current tile is out of POV
                    if wall and explored:
                        libtcod.console_set_char_background(
                            con, x, y, colors.get('dark_wall'),
                            libtcod.BKGND_SET
                        )
                    elif (not wall) and explored:
                        libtcod.console_set_char_background(
                            con, x, y, colors.get('dark_ground'),
                            libtcod.BKGND_SET
                        )
                # ----------------------------------------------------

                # Comment out below section if you want light in FOV
                # ----------------------------------------------------
                # if wall and explored:
                #     libtcod.console_set_char_background(
                #         con, x, y, colors.get('dark_wall'),
                #         libtcod.BKGND_SET
                #     )
                # elif (not wall) and explored:
                #     libtcod.console_set_char_background(
                #         con, x, y, colors.get('dark_ground'),
                #         libtcod.BKGND_SET
                #     )

    # Print all entities in the list
    for entity in entities:
        draw_entity(con, entity, fov_map)
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


def draw_entity(con, entity, fov_map):
    """
    Usage:
        Print the entity on the map.
    Params:
        con: tcod.console object
        entity: an Entity obj
    """
    if libtcod.map_is_in_fov(fov_map, entity.x, entity.y):
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
