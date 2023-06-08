"""
In this script we define functions for the recommender web
application
"""
import random
from recommenders import recommend_nmf, recommend_neighborhood, score_transformation
from utils import MOVIES, nmf_model, cos_sim_model


def recommend_nmf(query, nmf_model, titles, k=10):
    """This is an nmf-based recommender"""
    return NotImplementedError

def recommend_neighborhood(query, cos_sim_model, titles, k=10):
    """This is an cosine-similarity-based recommender"""
    return NotImplementedError


def random_recommender(k=2):
    if k > len(MOVIES):
        print(f"Hey you exceed the allowed number of movies {len(MOVIES)}")
        return []
    else:
        random.shuffle(MOVIES)
        top_k = MOVIES[:k]
        return top_k


if __name__ == "__main__":
    top2 = random_recommender()
    print(top2)


