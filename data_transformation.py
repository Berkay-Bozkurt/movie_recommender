import pandas as pd
from scipy.sparse import csr_matrix

def data_preparation():
    """
    Perform data preparation by reading movie and ratings data, merging them, calculating average ratings,
    filtering for popular movies, and returning the prepared DataFrame.
    """
    df_mov = pd.read_csv("./data/movies.csv")
    df_user = pd.read_csv("./data/ratings.csv")
    df_mov_link = pd.read_csv("./data/links.csv")
    
    df = df_mov.merge(df_user, on=["movieId"])
    df = df.merge(df_mov_link, on=["movieId"])


    df["av_rating"] = df.groupby("title")["rating"].transform("mean")

    # calculate the number of ratings per movie
    rating_count = df.groupby('movieId')[['rating']].count()
    
    # filter for movies with more than 20 ratings and extract the index
    popular_movies = rating_count[rating_count['rating'] > 20].index
    
    # filter the ratings matrix and only keep the popular movies
    df = df[df['movieId'].isin(popular_movies)].copy()
    
    return df

def data_transformations(df):
    """
    Perform data transformations by mapping user and movie IDs, sorting the DataFrame,
    and extracting the list of movie titles.
    """
    # remap user and movie IDs to sequential integers
    user_ids = df['userId'].unique()
    user_id_map = {v: k for k, v in enumerate(user_ids)}
    df['userId'] = df['userId'].map(user_id_map)
    
    movie_ids = df['movieId'].unique()
    movie_id_map = {v: k for k, v in enumerate(movie_ids)}
    df['movieId'] = df['movieId'].map(movie_id_map)
    
    # sort the DataFrame by average rating in descending order
    df.sort_values(by="av_rating", ascending=False, inplace=True)
    
    # extract the list of movie titles
    df_grp = df.groupby("title")[["av_rating"]].first()
    df_grp_= df.groupby("title")[["tmdbId"]].first()
    movies = df_grp.index.tolist()
    links=df_grp_.index.tolist()
    
    
    return df, movies, links

def create_csr_matrix(df):
    """
    Create a CSR matrix from the DataFrame containing user ratings.
    """
    R = csr_matrix((df['rating'], (df['userId'], df['movieId'])))
    Rt = R.todense()
    return Rt

# Perform data preparation and transformations, and create the CSR matrix
df = data_preparation()
df, movies, links = data_transformations(df)
Rt = create_csr_matrix(df)