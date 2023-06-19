# 1.Holiday Cost Calculator

## Description
The Holiday Cost Calculator is a Python program that calculates the total cost of a holiday trip. It takes into account the destination city, the number of nights staying at a hotel, and the number of days hiring a car. The program calculates the costs for the plane ticket, hotel accommodation, and car rental, providing the user with the total cost of their holiday.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the program: `holiday_cost_calculator.py`
4. Follow the prompts and provide the required information:
   - Enter the number corresponding to your destination city.
   - Enter the number of nights you will stay at a hotel.
   - Enter the number of days you will hire a car for.
5. The program will calculate and display the plane cost, hotel cost, car rental cost, and the total holiday cost.

# 2.Insurance Cost Prediction

## Description
The Insurance Cost Prediction project aims to analyze the relationship between age and insurance charges using linear regression. The project uses the `insurance.csv` dataset, which includes information such as age, sex, BMI, number of children, smoking status, region, and insurance charges. By fitting a linear regression model, the project visualizes how age affects insurance costs and provides predictions for insurance charges based on age.

## Usage
1. Open a terminal or command prompt.
3. Navigate to the project directory.
4. Run the project: `insurance_cost_prediction.py`
5. The project will load the `insurance.csv` dataset and display a scatter plot showing the relationship between age and insurance charges.
6. The project will then fit a linear regression model to the data and plot the regression line over the scatter plot to visualize the trend.
7. The resulting plot provides insights into how age affects insurance costs and can be used to make predictions for insurance charges based on age.

## Results
The scatter plot shows the distribution of insurance charges based on age, while the red line represents the linear regression model's prediction for insurance charges. The plot helps understand the relationship between age and insurance costs, indicating that as age increases, insurance charges tend to rise.

# 3.Minesweeper Solver

## Description
The Minesweeper Solver is a Python function that takes an input list representing a Minesweeper game and generates an output list with the number of mines adjacent to each cell. The input list uses "-" to represent empty cells and "#" to represent mines. The function iterates through each cell, counts the surrounding mines, and populates the output list with the count values. The resulting output list provides a solved representation of the Minesweeper game.

## Usage
To use the Minesweeper Solver function, follow these steps:
1. Import the function into your Python script or Jupyter Notebook.
2. Define an input list representing your Minesweeper game.
3. The function will generate an output list with the number of adjacent mines for each cell.
4. Iterate through the output list to access and use the solved representation of the Minesweeper game.

```python
# Example Usage
input_list = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
]

output_list = minesweeper_solver(input_list)

# Print the output list
for row in output_list:
    print(row)
```
# 4.Movie Similarity

## Description
The Movie Similarity project uses the spaCy library to calculate the similarity between movie descriptions. Given a reference movie description, the program compares it to a list of pre-defined movie descriptions and identifies the most similar movie. It helps users discover similar movies based on their preferences and interests.

## Installation
To use the Movie Similarity project, follow these steps:

1. Install the required dependencies: `pip install spacy`
2. Download the English language model: `python -m spacy download en_core_web_md`
3. Open the script `movie_similarity.py` in a text editor.
4. Update the `file_path` variable with the correct path to the `movies.txt` file on your system.
5. Save the file.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the project directory: `cd movie-similarity`.
3. Run the project: `python movie_similarity.py`.
4. The program will load the `movies.txt` file and calculate the similarity between the reference movie description and each movie in the list.
5. The program will display the similarity score for each movie, indicating how similar it is to the reference description.
6. The program will identify the most similar movie and display it as the next recommended movie.

## Example Output
Here is an example output from running the script:

当你将此文本复制到GitHub的README.md文件中时，请记得将以下信息替换为适合你项目的实际内容：

markdown
Copy code
# Movie Similarity

## Description
The Movie Similarity project uses the spaCy library to calculate the similarity between movie descriptions. Given a reference movie description, the program compares it to a list of pre-defined movie descriptions and identifies the most similar movie. It helps users discover similar movies based on their preferences and interests.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example Output](#example-output)

## Installation
To use the Movie Similarity project, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/movie-similarity.git`
2. Navigate to the project directory: `cd movie-similarity`
3. Install the required dependencies: `pip install spacy`
4. Download the English language model: `python -m spacy download en_core_web_md`
5. Open the script `movie_similarity.py` in a text editor.
6. Update the `file_path` variable with the correct path to the `movies.txt` file on your system.
7. Save the file.

## Usage
1. Open a terminal or command prompt.
2. Navigate to the project directory: `cd movie-similarity`.
3. Run the project: `python movie_similarity.py`.
4. The program will load the `movies.txt` file and calculate the similarity between the reference movie description and each movie in the list.
5. The program will display the similarity score for each movie, indicating how similar it is to the reference description.
6. The program will identify the most similar movie and display it as the next recommended movie.

## Example Output
Here is an example output from running the script:

Movie 1 - 0.723
Movie 2 - 0.635
Movie 3 - 0.802
...
Next movie: Movie 3

