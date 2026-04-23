# Grade Predictor

A simple machine learning project that predicts student grades based on study hours using linear regression.

## Description

This project demonstrates a basic implementation of linear regression using scikit-learn. It trains a model on sample data of study hours and corresponding grades, then allows users to input study hours to predict grades. The project also includes data visualization using matplotlib.

## Features

- Linear regression model training
- Data visualization with scatter plot and regression line
- Interactive grade prediction based on user input
- Input validation (grades capped at 100%)

## Requirements

- Python 3.x
- numpy
- scikit-learn
- matplotlib

## Installation

1. Clone or download this repository.
2. Navigate to the project directory.
3. Install the required packages:

   ```
   pip install numpy scikit-learn matplotlib
   ```

## Usage

Run the script:

```
python grade_predictor.py
```

The script will:
1. Train the model on sample data
2. Display a scatter plot with the regression line
3. Enter an interactive loop where you can input study hours to predict grades
4. Enter a negative number to exit

## Example

```
Input study hours (negative to exit): 6
Predicted grade for: 87.50
```

## License

This project is open source and available under the [MIT License](LICENSE).