def Ingredient_reco(path):
    import pandas as pd  # Data manipulation
    import numpy as np  # Array and Matrix operations
    from sklearn.externals import joblib  # To import custom models
    from sklearn.metrics.pairwise import cosine_similarity
    import Tag_Getter2 as GCV
    key_to_row = joblib.load('models/ingredient_key_to_row.pkl')
    factors = joblib.load('models/ingredient_factors.pkl')
    row_keys = joblib.load('models/ingredient_row_keys.pkl')


    def most_similar(ingredient, topn=10):
        if ingredient not in key_to_row:
            print("Unknown ingredient.")
        factor = factors[key_to_row[ingredient]]
        cosines = cosine_similarity([factor], factors)[0]
        indices = cosines.argsort()[::-1][:topn + 1]
        keys = [row_keys[idx] for idx in indices if idx != key_to_row[ingredient]]
        return keys, cosines[indices]


    def display_most_similar(ingredient, topn=10):
        print("- Most similar to '{}'".format(ingredient))
        similar_ings = []
        ing_scores = []
        for similar_ing, score in zip(*most_similar(ingredient, topn)):
            print("  . {} : {:.2f}".format(similar_ing, score))
            similar_ings.append(similar_ing)
            ing_scores.append(score)
        return similar_ings, ing_scores
    ingredient_list=[]
    ingredient_list=GCV.finalprint(path)
    if(ingredient_list[0]==1):
        result_ings, ing_scores = display_most_similar('spaghetti', 8)
        return result_ings
    elif(ingredient_list[1]==1):
        result_ings, ing_scores = display_most_similar('beans', 8)
        return result_ings
    else:
        result_ings, ing_scores = display_most_similar('naan', 8)
        return result_ings
