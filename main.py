import init_django_orm  # Це ініціалізує Django
from db.models import Movie, Genre, Actor
from services import movie

genres_ids = [2, 3, 7]
actors_ids = [3, 6, 2, 8]


# print(movie.create_movie(
#     "Indiana Jones 2",
#     "Adventure film with enormous amount of vfx",
#     genres_ids,
#     actors_ids
# ))
