from .competitions_controller import competitions
from .participants_controller import participants
from .categories_controllers import categories
from .participations_controller import participations

registerable_controllers = [competitions, participants, categories, participations]
