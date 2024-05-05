# KptnCook2Todoist Script

This Python script is designed to fetch recipes from a specified URL (from Kaptain Cook), extract their ingredients, and add them to a Todoist project as a shopping list. The script makes use of a virtual environment set up in PyCharm and can be triggered via an Alfred workflow.


## Features
- **Fetch Recipes**: Retrieves the ingredients from a recipe webpage using the German locale (for measurements in metric units).
- **Extract Ingredients**: Adjusts ingredient quantities for a specified number of people and identifies ingredients with unknown quantities.
- **Add to Todoist**: Automatically creates tasks in the specified Todoist project, including ingredients with a "???" prefix if the quantity is not given in the recipe.

## Prerequisites
- Python (3.x)
- PyCharm for setting up the virtual environment
- Alfred for workflow automation
- The following Python libraries:

  - `requests`
  - `beautifulsoup4`
  - `todoist-api-python`
  - `json`
  - `tkinter` (standard in Python)

## Setup Instructions
1. **Create a Virtual Environment**: In PyCharm, set up a virtual environment where the script will be developed and executed.

2. **Install Required Libraries**: Run the following `pip` commands to install the necessary libraries inside the virtual environment:
   ```bash
   pip install requests beautifulsoup4 todoist-api-python
3. **Create a Configuration File**: Create a file named config.json in the script directory to store the API key and project ID securely:
     ```json
        {
            "api_key": "YOUR_TODOIST_API_KEY",
            "shoppinglist_id": "YOUR_TODOIST_PROJECT_ID"
        }
     ```
   You need the ID of the project you want to add the ingredients to NOT the name. You can get this through an API call (list all projects, then manually read out the ID)
4. **Set up Alfred Workflow**: Create a new Alfred workflow with a keyword trigger.
Add a "Run Script" action with the following Bash command:  
    ```bash
    /Users/USERNAME/PycharmProjects/KptnCook2ToDoIst/.venv/bin/python /Users/USERNAME/PycharmProjects/KptnCook2ToDoIst/.venv/KptnCook-Einkaufsliste.py "{query}"
     ``` 
   This will use the Python interpreter in the virtual environment to execute the script and pass the URL to the recipe as an argument.
5**Run the Workflow**:
Invoke Alfred and type the keyword to trigger the workflow.
Provide the URL of the recipe page in the Alfred prompt and press enter.
## Script Details
### Functions
fetch_and_parse(url): Makes an HTTP request to fetch the webpage content and returns a BeautifulSoup object for parsing.
extract_ingredients(soup, target_people=4): Extracts the ingredients from the recipe, adjusts quantities, and includes unknown quantities with a "???" prefix.
add_to_todoist(api_key, tasks, project_id): Adds the tasks (ingredients) to the specified Todoist project.
### Main Execution Flow
Loads configuration data (API key and project ID) from the config.json file.
Accepts the URL as a command-line argument.
Fetches, parses, and processes the webpage to extract ingredients.
Adds the ingredients to the Todoist project using the provided API key and project ID.
### Error Handling
The script checks for valid command-line arguments before execution.
HTTP request errors are handled with response.raise_for_status().
## License
This project is open-source and distributed under the MIT License.


