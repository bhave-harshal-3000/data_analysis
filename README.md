# IPL 2023 Auction Analysis

## Overview
This project analyzes the IPL 2023 auction dataset to explore various insights, including top players by auction price, team spending, and price distribution. The analysis is displayed through interactive charts using **Tkinter** for GUI and **Matplotlib** for visualizations. This project aims to provide a detailed analysis of player spending and distribution trends in the IPL auction.

## Data Used
- **Dataset**: IPL 2023 auction data containing player names, prices, team information, and player roles.

## Features
1. **Top Players by Auction Price**: Displays the top 10 players sorted by their auction prices.
2. **Team Spending Analysis**: Shows the total spending by each team in the auction.
3. **Average Team Spending**: Visualizes the average spending per team.
4. **Player Price Distribution**: Distribution of player prices, with a KDE plot for better insight.
5. **Spending by Player Role**: Shows the total spending on players by their role (e.g., Batsman, Bowler, All-Rounder).

## Statistical Measures
- **Mean Price**: The average price of all players.
- **Median Price**: The middle value of the player prices.
- **Mode Price**: The most frequently occurring price in the auction.
- **Standard Deviation**: Measures the variation in player prices.
- **Variance**: The square of the standard deviation, showing the spread of player prices.
- **Price Range**: The difference between the maximum and minimum auction prices.

## Setup
1. **Libraries**:
   - **Pandas**: For data manipulation and analysis.
   - **Matplotlib**: For data visualization.
   - **Seaborn**: For additional plotting features.
   - **Tkinter**: For building the interactive graphical user interface (GUI).

2. **Installation**:
   Install the required libraries using pip:

   ```bash
   pip install pandas matplotlib seaborn
