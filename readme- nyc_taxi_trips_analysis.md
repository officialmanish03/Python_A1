# NYC Taxi Trips Analysis (March 2019)

Analysis of 6,433 Yellow and Green taxi trips in New York City: when and where taxis earn the most, how passengers pay, and how tipping works.

## Business Questions
1. Which hours and days are the busiest and most profitable?
2. Which boroughs and zones generate the most trips and revenue?
3. How do customers pay, and how much do card-paying customers tip?
4. How do Yellow and Green taxis differ in fare, distance and tips?

## Tools Used
Python, Pandas, Matplotlib, Seaborn, Jupyter Notebook

## Dataset
NYC taxi trips, March 2019 (6,433 rows, 14 columns), loaded from the [seaborn-data](https://github.com/mwaskom/seaborn-data) repository.

## Data Preparation
- Converted pickup and dropoff to datetime and created hour, weekday, trip duration, tip % and speed columns
- Removed 53 invalid trips (zero distance, zero duration, out of period) and 10 trips with impossible speeds
- Filled missing payment and location labels with "Unknown"
- Kept long, high-fare trips because they are real airport and outer-borough revenue

## Key Findings
1. **Peak demand:** 6 PM is the busiest hour and 5 PM brings the most fare revenue. Wednesday is the busiest day per day, Sunday the quietest.
2. **Where the money is:** Manhattan has 82.4% of trips and 70.5% of revenue. JFK and LaGuardia generate 13.3% of revenue from just 4.6% of trips.
3. **Payments and tips:** 71.4% of trips are paid by card. Card riders tip 23.9% on average, and tip % drops on longer trips. Cash tips are not recorded in this data.
4. **Yellow vs green:** yellow taxis serve Manhattan, green taxis the outer boroughs. Green card riders tip about half as much (12.9% vs 25.4%).

## Visualizations
Refer image folder

## Limitations
- One month of data; revenue means the meter fare only (no tips, tolls or surcharges)
- Cash tips are not recorded, so tip analysis covers card payments only
- The data cannot explain why green-taxi tips are lower

## How to Run
1. Clone this repository
2. Install the libraries: `pip install -r requirements.txt`
3. Open `nyc_taxi_trips_analysis.ipynb` in Jupyter Notebook and run all cells. The data loads from the internet, so no download is needed.

## Author
Manish | [LinkedIn](https://www.linkedin.com/in/manish-singh-916a9b276/)
