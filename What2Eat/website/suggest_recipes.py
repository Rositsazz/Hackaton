from __future__ import print_function
import string
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.neighbors import NearestNeighbors
from .models import Recipe


def products_split(products):  # tokenize
    products = products.lower()
    products = products.split()
    products = [word.strip(string.punctuation) for word in products]
    products = [word for word in products if word.isalpha(
        ) and len(word) > 2]
    return products

stop_words = ['cup', 'cups', 'lbs', 'ounces', 'ounce', 'large', 'or', 'teaspoon', 'tablespoon', 'tablespoons', 'freshly', 'finely', 'small', 'pinch']


def suggested(last_cooked):
    recipes = Recipe.objects.all()

    tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                     min_df=0.05, stop_words=stop_words,
                                     use_idf=True, tokenizer=products_split)

    products = [recipe.products for recipe in recipes]
    titles = [recipe.name for recipe in recipes]
    prepare_times = [recipe.prepare_time for recipe in recipes]
    images = [recipe.image for recipe in recipes]

    tfidf_matrix = tfidf_vectorizer.fit_transform(products)
    num_clusters = 100
    km = KMeans(n_clusters=num_clusters)
    km.fit_predict(tfidf_matrix)

    for i in range(len(recipes)):
        if recipes[i].name == last_cooked:
            index = i
            break

    near = NearestNeighbors(
        n_neighbours=5, algorithm='ball_tree').fit(tfidf_matrix)

    dist, indices = near.kneighbors(tfidf_matrix[index])
    title_result = [titles[index] for index in indices[0]]
    prepare_times_result = [prepare_times[index] for index in indices[0]]
    images_result = [images[index] for index in indices[0]]

    data = {}
    for i in range(1, len(title_result)):
        data[i] = [title_result[i], prepare_times_result[i], images_result[i]]

    with open("suggested_recipes.json", 'w') as f:
        json.dump(data, f, indent=True, ensure_ascii=False)
