# Weather API Task
Goals

In this project, you will use a public weather API to gather current weather information for multiple cities around the world.
They’ll then use Python and pandas to clean, organize, and analyze the collected data.

You'll learn to fetch live data from an API, convert JSON responses into tabular format, explore, summarize, and visualize real-world weather data, and practice data storytelling based on their findings.

Tasks

1.API Connection

Choose a weather API (e.g., OpenWeatherMap – free with registration).
Get an API key and test it with a single city.
Request data like:

City name
Temperature (°C)
Humidity (%)
Wind speed (m/s or km/h)
Weather description (e.g., “clear sky”)
2. Data Collection

Create a list of at least 20 cities from different continents.
Use a Python loop to request data for each city and store the results.
Build a pandas DataFrame with one row per city.
3. Data Cleaning

Check for missing or inconsistent data (e.g., failed requests).
Format numeric columns correctly (e.g., convert Kelvin to Celsius if needed).
Save your data to a CSV file.
4. Data Analysis

Answer questions such as:

Which cities are the hottest and coldest right now?
Is there a relationship between temperature and humidity?
Which continent seems to have the windiest cities?
What’s the most common weather description (e.g., clear, cloudy, rainy)?
5. Visualization

Create at least two charts (using matplotlib or pandas):

Example 1: Bar chart of average temperature by continent.
Example 2: Scatter plot of temperature vs humidity.
6. Summary

Write a short report (Markdown cell):

Describe your process (API requests, data cleaning, analysis).
Highlight interesting patterns.
Mention any difficulties or limitations you encountered.
Instructions

Use dataset from "Xeral/Datasets" on this page course
Create a github repo for this task.
Clone your repo locally.
Download the dataset (don't forget to commit)
Create a new environment to run the notebook.
A .ipynb notebook containing:
Code cells for the API requests, data processing, and analysis.
Markdown explanations and conclusions.
At least two plots visualizing your results.
The CSV file you created.
Upload your code (don't forget a nice Readme.md).
Paste the github repository link below (don't forget inviting me if it's a private repo).
Optional Extensions (Bonus)
Compare current vs forecasted data.
Compute temperature differences by time of day.
Use geopy or a city coordinate list to automate location queries.
Map the results on a world map using Plotly or Folium.