import pickle
from recommenders import recommend_nmf, recommend_neighborhood, score_transformation

def load_models(models_list):
    """
    Load the trained models from pickle files.
    """
    with open(f'./{models_list[0]}.pkl', 'rb') as file:
        model_1 = pickle.load(file)
    
    with open(f'./{models_list[1]}.pkl', 'rb') as file:
        model_2 = pickle.load(file)
    
    return model_1, model_2


def get_top_movies(model, k=3):
    """
    Get the top-k movies from the recommendation model.
    
    Args:
        model (pd.Series): The recommendation scores for movies.
        k (int): The number of top movies to retrieve.
    
    Returns:
        list: The top-k movie titles.
    """
    model_list = model.sort_values(ascending=False).index.tolist()
    top_movies = model_list[:k]
    return top_movies


def combination_of_models(model1, model2):
    """
    Combine the recommendation scores from two models.
    
    Args:
        model1 (pd.Series): The recommendation scores from model 1.
        model2 (pd.Series): The recommendation scores from model 2.
    
    Returns:
        list: The combined top-k movie titles.
    """
    total_recommendation = (model1.add(model2)) / 2
    total_recommendation.dropna(inplace=True)
    total_recommendation_ = total_recommendation.sort_values(ascending=False).index.tolist()
    return total_recommendation_

new_user_query = {
                 "12 Angry Men (1957)": 5,
                 "Godfather, The (1972)":5,
                 "Schindler's List (1993)": 4,
                 'Godfather: Part II, The (1974)': 4,
                 'Goodfellas (1990)': 4,
                 'Princess Bride, The (1987)': 1,
                 'War of the Worlds (2005)': 2,
                 "101 Dalmatians (1996)":1,
                 "Zodiac (2007)":4,
                 "Young Guns (1988)":3,
                 "13th Warrior, The (1999)":2,
                 "3:10 to Yuma (2007)":4,
                 "American Psycho (2000)":4,
                 }

existing_models = ["nmf_model1", "near_recommender"]
def main():
    nmf_model, near_model = load_models(existing_models)
    recommend_neighborhood_ = score_transformation(recommend_neighborhood(new_user_query, near_model, 20), 20)
    recommend_neighborhood_top = get_top_movies(recommend_neighborhood_)
    recommend_nmf_ = score_transformation(recommend_nmf(new_user_query, nmf_model), 20)
    recommend_nmf_top = get_top_movies(recommend_nmf_)
    combined_model = combination_of_models(recommend_neighborhood_, recommend_nmf_)

    final_recommendations = list(set(recommend_neighborhood_top + recommend_nmf_top + combined_model))
    print(final_recommendations)


if __name__ == "__main__":
    main()