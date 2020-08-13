import mysql.connector


class Database:


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

    def __init__(self):
        self.connection = mysql.connector.connect(  host="localhost",               #hostname
  user="root",                   # the user who has privilege to the db
  passwd="admin",               #password for user
  database="datamining",               #database name
    auth_plugin = 'mysql_native_password', use_pure= False)  # change here if you need any changes
        self.cursor = self.connection.cursor()
                # REMEMBER THIS. GOT STUCK HERE
    def insert(self, query):
        try:
            self.cursor.execute(query)
            self.connection.commit()
        except:
            self.connection.rollback()