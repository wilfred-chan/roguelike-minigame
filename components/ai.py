import tcod as libtcod


class BasicMonster:
    def take_turn(self, target, fov_map, game_map, entities):
        """
        Usage:
            The actions the monster will take.
        Params:
            target(Entity obj): mostly, player
            fov_map(tcod.map.MAp obj): determine if the monster sees player
            game_map(GameMap obj): to return blocked tiles
            entities(list): a iterable list to return blocking entity
        """
        # self.owner = the Entity with ai attribute
        monster_entity = self.owner
        if libtcod.map_is_in_fov(
            fov_map, monster_entity.x, monster_entity.y
        ):
            if monster_entity.get_distance(target) >= 2:
                monster_entity.move_toward(target, game_map, entities)
            else:
                if target.fighter.hp > 0:
                    print(
                        'The {} attacks you.'.format(
                            monster_entity.name
                        )
                    )
