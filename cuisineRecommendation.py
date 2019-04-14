def cuisine_recommend(path):
    # Import libraries
    import pandas as pd  # Data manipulation
    import numpy as np  # Array and Matrix operations
    from sklearn.externals import joblib  # To import custom models
    import Tag_Getter2 as GCV
    cv = joblib.load('cuisine_count_vectorizer.pkl')
    logistic = joblib.load('cuisine_logistic_model.pkl')
    enc = joblib.load('cuisine_label_encoder.pkl')


    def predict_cuisine(ingredients):
        ingredients = pd.Series(ingredients)
        X_test = cv.transform(ingredients.values)
        result = logistic.predict(X_test)
        result = enc.inverse_transform(result)
        ingredient_list=[]
        ingredient_list=GCV.finalprint(path)
        return(result)
    ingredient_list=[]
    ingredient_list=GCV.finalprint(path)
    if(ingredient_list[0]==1):
        return(predict_cuisine('spaghetti'))
    elif(ingredient_list[1]==1):
        return(predict_cuisine('beans'))
    else:
        return(predict_cuisine('naan'))

    # Input example: ["Spaghetti; Cheese"]
