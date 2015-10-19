
import requests_mock
from spotify_app import SearchAlbums, SearchArtists


@requests_mock.Mocker()
def test_search_album(m):
    with open('thriller.json') as thriller:
        m.get('https://mager-spotify-web.p.mashape.com/search/1/album.json?q=thriller', text=thriller.read())

    searcher = SearchAlbums('thriller')
    res = searcher.run()

    assert res == ('Michael Jackson', 'Thriller 25 Super Deluxe Edition')


@requests_mock.Mocker()
def test_search_artist(m):
    with open('jackson.json') as jackson:
        m.get('https://mager-spotify-web.p.mashape.com/search/1/artist.json?q=jackson', text=jackson.read())

    searcher = SearchArtists('jackson')
    res = searcher.run()

    assert res == 'Michael Jackson'
