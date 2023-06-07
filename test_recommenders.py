"""
In this script we define functions for the recommender web
application
"""
import random
from recommenders import recommend_nmf, recommend_neighborhood


def recommend_nmf(query, nmf_model, titles, k=10):
    """This is an nmf-based recommender"""
    return NotImplementedError

def recommend_neighborhood(query, cos_sim_model, titles, k=10):
    """This is an cosine-similarity-based recommender"""
    return NotImplementedError



if __name__ == "__main__":
    top2 = recommend_nmf()
    print(top2)


