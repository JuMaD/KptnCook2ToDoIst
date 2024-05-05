import requests
import re
import sys
from bs4 import BeautifulSoup
from todoist_api_python.api import TodoistAPI
import tkinter as tk
from tkinter import simpledialog
import json


def fetch_and_parse(url):
    headers = {
        'Accept-Language': 'de-DE,de;q=0.9'  # Prioritize German, with a high quality factor
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')


def extract_ingredients(soup, target_people=4):
    # Find the number of people the recipe is originally for
    people_text = soup.find('div', class_='col-md-12 kptn-person-count').text
    people = int(re.search(r'\d+', people_text).group())  # Extract number of people using regex

    ingredients = soup.find_all('div', class_='kptn-ingredient')
    measures = soup.find_all('div', class_='text-right kptn-ingredient-measure')

    ingredient_list = []
    # Handle scenarios where there are more ingredients than measures
    max_length = max(len(ingredients), len(measures))
    for i in range(max_length):
        ingredient_text = ingredients[i].text.strip() if i < len(ingredients) else "Unknown ingredient"
        if i < len(measures):
            measure_text = measures[i].text.strip()
            # Extract quantity and unit if available, else set to "???"
            qty_match = re.search(r'\d*\.?\d+', measure_text)
            if qty_match:
                quantity = float(qty_match.group()) * target_people / people
                measure_unit = measure_text[len(qty_match.group()):].strip()
                ingredient_list.append(f"{quantity} {measure_unit} {ingredient_text}")
            else:
                ingredient_list.append(f"??? {ingredient_text}")
        else:
            # No measure available for this ingredient
            ingredient_list.append(f"??? {ingredient_text}")

    return ingredient_list


def add_to_todoist(api_key, tasks, project_id):
    api = TodoistAPI(api_key)
     # Add tasks
    for task in tasks:
        api.add_task(content=f"{task}", project_id=project_id)




def main(api_key, einkaufsliste_id, url):
    #root = tk.Tk()
    #root.withdraw()  # Hide the main window
    #url = simpledialog.askstring("URL Input", "Link zum Rezept:")
    if url:
        soup = fetch_and_parse(url)
        ingredients = extract_ingredients(soup)
        add_to_todoist(api_key, ingredients, project_id=einkaufsliste_id)


if __name__ == "__main__":
    # Load configuration data from the JSON file
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)

    # Access the API key and project ID
    api_key = config['api_key']
    project_id = config['shoppinglist_id']


    print("PYTHONSCRIPT")
    print(sys.argv)
    if len(sys.argv) > 1:

        main(api_key, shoppinglist_id, sys.argv[1])
