import media
import fresh_tomatoes


def Movielist() :

    poster_image_url = "https://starwarsblog.starwars.com/wp-content/uploads/2015/10/star-wars-force-awakens-official-poster.jpg"
    starwars = media.Movie("Star Wars",poster_image_url,"https://www.youtube.com/watch?v=Gs1WwM-3lJ0")

    list = []
    list.append(starwars)

    fresh_tomatoes.open_movies_page(list)

Movielist()