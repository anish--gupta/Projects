# Import media in order to make use of Movie class, fresh_tomatoes for rendering
import media
import fresh_tomatoes

# Create instances of various movies
movie_baahubali1 = media.Movie(
	"Baahubali The Beginning",
	"https://goo.gl/FMfuVv",
	"https://youtu.be/sOEg_YZQsTI"
	)

movie_baahubali2 = media.Movie(
	"Baahubali The Conclusion",
	"https://goo.gl/fAoCWz",
	"https://youtu.be/G62HrubdD6o"
	)

movie_baby = media.Movie(
	"Baby",
	"https://goo.gl/3221vS",
	"https://youtu.be/-Yu_2nyOP5o"
	)

# Create movie list and pass it to open_movies_page method for rendering
movies_list = [movie_baahubali1, movie_baahubali2, movie_baby]
fresh_tomatoes.open_movies_page(movies_list)