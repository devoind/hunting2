from .genres import api as genres_ns
from .movies import api as movies_ns
from .directors import api as director_ns

__all__ = [
    'genres_ns',
    'movies_ns',
    'director_ns'
]
