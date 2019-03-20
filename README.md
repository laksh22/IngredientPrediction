# IngredientPrediction

Data - https://www.kaggle.com/c/whats-cooking/data

### Steps:

1. Do exploratory analysis on dataset to see how many unique ingredients etc.
2. Gather dataset of food images (https://www.kaggle.com/dansbecker/food-101) and manually label each one and place bounding boxes(https://github.com/tzutalin/labelImg) - Since there are so many ingredients, we can try the top 10 or 20 most common ingredients.
3. Use Tensorflow Object detection API with a pre-trained model to detect ingredients.(https://blog.goodaudience.com/food-detection-app-using-tensorflow-object-detection-apis-1b9302a9aad2)
4. Train a model on the dataset to get ingredients which occur most with the ingredients in the picture. (https://www.kaggle.com/halflings/ingredient-recommender-system)
5. Recommend only the ingredients which are common to all recommended ingredient lists.
