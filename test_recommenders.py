"""TODO

Write a program that checks that recommenders works as expected

We will use pytest
to install pytest run in the terminal 
+ pip install pytest
/ conda install pytest

TDD (Test-driven-development)  cycle:

0. Make an Hypothesis:
    the units/programs work
1. Write test that fails (to disprove the Hypothesis)
2. Change the code so that the Hypothesis is re-established
3. repeat 0-->2

"""
import json
import pickle
from recommenders import movies, recommend_nmf

user_query = json.load(open("user_query.json"))
with open('./nmf_model1.pkl', 'rb') as file:
        model_1 = pickle.load(file)


def test_movies_are_strings():
    for movie in movies:
        assert isinstance(movie,str)

def test_for_two_movies():
    top2 = recommend_nmf(user_query, k=2)
    assert len(top2) == 2
