
from recommenders import MOVIES, random_recommender
def test_movies_are_strings():
    for movie in MOVIES:
        assert isinstance(movie,str)
def test_for_two_movies():
    top2 = random_recommender(k=2)
    assert len(top2) == 2
def test_for_5_movies():
    top5 = random_recommender(5)
    assert len(top5) == 5
def test_return_0_if_k_10_larger():
    top10= random_recommender(10)
    assert len(top10) == 0
