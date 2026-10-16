# Automobile Fuel Efficiency Analysis (1970-1982)

Exploratory data analysis of 398 cars to understand how weight, horsepower, cylinders and region of origin affect fuel efficiency, and how efficiency changed over time.

## Business Questions
1. Did fuel efficiency improve over the years?
2. Which region builds the most fuel-efficient cars?
3. How do weight and horsepower affect mileage?
4. How does the number of cylinders change mileage?
5. Which cars are the most (and least) fuel-efficient?

## Tools Used
Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook

## Dataset
Auto MPG dataset (398 records, 9 columns) from the [seaborn-data](https://github.com/mwaskom/seaborn-data) repository.

## Data Preparation
- Filled 6 missing horsepower values using the median of cars with the same number of cylinders
- Converted model year to full year (70 to 1970) and cleaned region names
- Extracted car brand from the car name and fixed inconsistent spellings
- Created mileage categories with `pd.cut()` and a km/l column

## Key Findings
- Average MPG rose from 17.7 (1970) to 31.7 (1982), about 79%.
- Part of the 1980 spike came from a change in car mix. USA-only cars still improved from 15.3 to 29.5 MPG (about 93%).
- Japanese cars are the most efficient (30.5 MPG), followed by Europe (27.9) and the USA (20.1). US cars are also heavier and more powerful.
- Weight has the strongest link to mileage (correlation -0.83).
- 4-cylinder cars average 29.3 MPG, 6-cylinder 20.0, and 8-cylinder 15.0.
- The 10 most efficient cars are all from Japan or Europe (1978-1982).

## Visualizations
All Images in Folder named - auto-mpg-fuel-efficiency images

## Limitations
- Small sample (398 cars), so results describe this sample only.
- The mix of cars changes across years, which affects yearly averages.
- 3- and 5-cylinder groups are too small for reliable conclusions.
- Correlation does not prove causation.

## How to Run
1. Clone this repository
2. Install the libraries: `pip install -r requirements.txt`
3. Open `auto_mpg_fuel_efficiency_analysis.ipynb` in Jupyter Notebook and run all cells

## Author
Manish | [LinkedIn](https://www.linkedin.com/in/manish-singh-916a9b276/)
