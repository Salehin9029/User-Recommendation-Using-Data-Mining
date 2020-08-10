from surprise import SVD
import pandas as pd
from surprise import Dataset
from surprise import Reader
from collections import defaultdict
from surprise.model_selection import cross_validate
import databaseCon

con = databaseCon.Database()

loadedData = con.selectAll()

userGroupId = loadedData[0]
ingredientId = loadedData[1]
ratings = loadedData[2]  # ALL MUST BE IN SAME LENGTH OR ERROR WILL COME


def do_predict():
    ratings_dic = {"userId": userGroupId,
                   "itemId": ingredientId,
                   "rating": ratings}
    df = pd.DataFrame(ratings_dic)
    reader = Reader(rating_scale=(1, 4))
    data = Dataset.load_from_df(df[['userId', 'itemId', 'rating']], reader)
    trainset = data.build_full_trainset()
    algo = SVD()
    algo.fit(trainset)
    testset = trainset.build_anti_testset()
    predictions = algo.test(testset)
    cross_validate(algo, data, measures=['RMSE', 'MAE'], cv=5, verbose=True)
    get_top_n(predictions)


def get_top_n(predictions, n=20):
    top_n = defaultdict(list)

    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
    print(top_n)
    for uid, user_ratings, in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse= True)
        top_n[uid] = user_ratings[:n]

do_predict()
