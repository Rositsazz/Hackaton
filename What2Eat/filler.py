import sqlite3
import json

conn = sqlite3.connect("db.sqlite3")
cursor = conn.cursor()

with open("recipes_popular.json", "r") as f:
    contents = f.read()
    recipes = json.loads(contents)

    for recipe in recipes:
        if "mins" in recipe["prepare_time"]:
            splited = recipe["prepare_time"].split("mins")
            recipe["prepare_time"] = int(splited[0])
        elif "hrs"in recipe["prepare_time"]:
            splited = recipe["prepare_time"].split("hrs")
            recipe["prepare_time"] = int(splited[0])*60
        elif "hr" in recipe["prepare_time"]:
            recipe["prepare_time"] = 60

        coef = recipe["total_fat"] / recipe["protein"] if recipe["protein"] != 0 else 1000
        keywords = ""

        query = "INSERT INTO website_recipe (instructions, name, servings, products, image, total_fat, prepare_time, protein, healthy_coef, keywords) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
        cursor.execute(query, (recipe["instructions"], recipe["name"], recipe["servings"], recipe["products"], recipe["image"], recipe["total_fat"], recipe["prepare_time"], recipe["protein"], coef, keywords))

    conn.commit()
