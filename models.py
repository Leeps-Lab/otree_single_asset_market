from otree_markets import models as markets_models

class Constants(markets_models.Constants):
    name_in_url = 'otree_single_asset_market'


class Subsession(markets_models.Subsession):
    constants = Constants


class Group(markets_models.Group):
    pass


class Player(markets_models.Player):
    pass
