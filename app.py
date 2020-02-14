from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_nav.elements import Navbar, View
from flask_nav import Nav

from test_data import *
app = Flask(__name__)

Bootstrap(app)

nav = Nav()
nav.init_app(app)

@nav.navigation()
def mynavbar():
    return Navbar(
        'Not So Pitchfork',
        View('Recent Reviews', 'index'),
        View('Artists', 'all_artists'),
        View('Albums', 'all_albums'),
        View('Genres', 'all_genres'),
        View('Search', 'search')
    )
    
@app.route('/')
def index():
    return render_template("index.html")

#####################
#      ARTISTS      #
#####################
#All artists page
@app.route('/artists')
def all_artists():
    return render_template("artists.html", artists=artists)

#Single Artist Page
@app.route('/artists/<int:artist_id>', methods=['GET'])
def get_single_artist(artist_id):
    return render_template("single_artist.html", artist=artists[artist_id-1], albums=albums[artist_id-1])

#DELETE Single Artist
@app.route('/artists/<int:artist_id>', methods=['DELETE'])
def delete_single_artist(artist_id):
    #TODO: Delete single artist
    return redirect(url_for('all_artists'))

#Create artist template
@app.route('/artists/create', methods=['GET'])
def create_artists_form():
    return render_template("create_artist.html")

#POST create artist
@app.route('/artists/create', methods=['POST'])
def create_artist_submission():
    # TODO: Catch errors
    return redirect(url_for('all_artists'))
    

#####################
#      ALBUMS       #
#####################
@app.route('/albums')
def all_albums():
    return render_template("albums.html", albums=albums, artist=artists)

@app.route('/albums/<int:album_id>', methods=['GET'])
def get_single_album(album_id):
    # TODO: Create "single_artist.html" 
    return render_template("single_album.html", 
        album=albums[album_id-1],
        review=reviews[album_id-1],
        user=users[album_id-1])

#Get create album Form
@app.route('/albums/create', methods=['GET'])
def create_album_form():
    return render_template("create_album.html")

#POST create album
@app.route('/albums/create', methods=['POST'])
def create_album_submission():
    # TODO: Catch errors
    return redirect(url_for('all_albums'))


#####################
#      Genres       #
#####################
@app.route('/genres')
def all_genres():
    return render_template("genres.html", albums=albums, artist=artists, genres=genres)

@app.route('/albums/genres/<int:genre_id>', methods=['GET'])
def get_albums_genre(album_id):
    # TODO: Create "single_artist.html" 
    return render_template("single_album.html", 
        album=albums[album_id-1],
        review=reviews[album_id-1],
        user=users[album_id-1])

@app.route('/genres/create', methods=['GET'])
def create_genre_form():
    return render_template("create_genre.html")

#POST create album
@app.route('/genres/create', methods=['POST'])
def create_genre_submission():
    # TODO: Catch errors
    return redirect(url_for('all_genres'))


#####################
#      Review       #
#####################
@app.route('/albums/<int:album_id>/review', methods=['GET'])
def create_review(album_id):
    return render_template("create_review.html", album=albums[album_id-1])

@app.route('/albums/<int:album_id>/review', methods=['POST'])
def create_review_submission(album_id):
    print(album_id)
    return redirect('/albums/%d' % album_id)


#####################
#      Search       #
#####################
@app.route('/search', methods=['GET'])
def search():
    return render_template("search.html")



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9998')


