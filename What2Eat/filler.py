import sqlite3
import json

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

with open("recipes_popular.json", "r") as f:
    contents = f.read()
    recipes = json.loads(contents)
    for recipe in recipes:
        query = "INSERT INTO website_recipe (instructions, name, servings, products, image, total_fat, prepare_time, protein) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (recipe["instructions"], recipe["name"], recipe["servings"], recipe["products"], recipe["image"], recipe["total_fat"], recipe["prepare_time"], recipe["protein"]))
    conn.commit()
