#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  # MY CODE
  
    total_created = []
    # loop over ingredients dict to pull out values 
    for a,b in ingredients.items(): # .items = each item inside of { }, so milk:100, butter, flour
        total_combinations = ingredients[a] // recipe[a]
        total_created.append(total_combinations)
        result = min(total_created)
    print(result)

    return result
  


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 131, 'butter': 48, 'flour': 51 }

  
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))