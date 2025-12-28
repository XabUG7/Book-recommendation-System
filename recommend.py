import pandas as pd

def get_top_n(user_id, df, model,n=10):
    """
    Return top n books for user
    :param user_id: User for which the recommendation will be done
    :param df:      DataFrame with ratings
    :param model:   Model which will be used for recommendations
    :param n:       Number of recommendations to return
    :return         DataFrame with recommendations
    """
    # Get the list of books already rated by the user
    rated_books = list(df[df.user_id  == user_id].book_id)
    #Predict the ratings for books which user didn't rate
    ratings_list = [(user_id,book_id,0) for book_id in set(df[~df.book_id.isin(rated_books)].book_id)]
    predictions = model.test(ratings_list)

    top_n = list()
    for _, iid, true_r, est, _ in predictions:
        top_n.append((iid, est))

    # Sort the predictions and retrieve the n highest ones.
    top_n.sort(key=lambda x: x[1], reverse=True)
    top_n = top_n[:n]
    #Create df
    df_top = pd.DataFrame(top_n, columns=['book_id', 'prediction'])
    df_top['pred_rating'] = df_top['prediction'].apply(lambda x: round(x))

    return df_top


def get_names(df, df_names):
    """
    Generate a histogram for DataFrame grouped by col_name
    and show basic statistics.
    :param df:          DataFrame with ratings
    :param df_names:    DataFrame with books' names
    :return             merged DataFrame
    """
    return pd.merge(df, df_names, how='left')



