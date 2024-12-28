import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the IPL dataset
data = pd.read_csv('ipl_2023_dataset.csv')

# Perform analysis
# Mean
mean_price = data['Cost in Rs. (CR)'].mean()
median_price = data['Cost in Rs. (CR)'].median()
mode_price = data['Cost in Rs. (CR)'].mode()[0]
std_dev_price = data['Cost in Rs. (CR)'].std()
variance_price = data['Cost in Rs. (CR)'].var()
price_range = data['Cost in Rs. (CR)'].max() - data['Cost in Rs. (CR)'].min()

# Create charts
# 1. Top players by auction price
top_players = data.groupby('Player Name')['Cost in Rs. (CR)'].sum().sort_values(ascending=False).head(10)
fig1, ax1 = plt.subplots(figsize=(8, 5))
top_players.plot(kind='bar', color='orange', ax=ax1, title='Top Players by Auction Price')
ax1.set_xlabel('Player')
ax1.set_ylabel('Price (in Crores)')
ax1.grid(True)
plt.xticks(rotation=45, ha='right')  # Rotate and align labels
fig1.tight_layout(pad=2)  # Add padding to prevent cropping

# 2. Team spending analysis
team_spending = data.groupby('2023 Squad')['Cost in Rs. (CR)'].sum()
fig2, ax2 = plt.subplots(figsize=(8, 5))
team_spending.plot(kind='pie', autopct='%1.1f%%', ax=ax2, title='Total Spending by Team', colors=sns.color_palette("Set2"))
ax2.set_ylabel('')

# 3. Average team spending
avg_team_spending = data.groupby('2023 Squad')['Cost in Rs. (CR)'].mean().sort_values(ascending=False)
fig3, ax3 = plt.subplots(figsize=(8, 5))
avg_team_spending.plot(kind='bar', color='skyblue', ax=ax3, title='Average Player Price by Team')
ax3.set_xlabel('Team')
ax3.set_ylabel('Average Price (in Crores)')
ax3.grid(True)
plt.xticks(rotation=45, ha='right')  # Rotate and align labels
fig3.tight_layout(pad=2)

# 4. Player price distribution
fig4, ax4 = plt.subplots(figsize=(8, 5))
sns.histplot(data['Cost in Rs. (CR)'], bins=20, kde=True, ax=ax4)
ax4.set_title('Distribution of Player Prices')
ax4.set_xlabel('Price (in Crores)')
ax4.set_ylabel('Frequency')
ax4.grid(True)

# 5. Spending by player role
role_spending = data.groupby('Type')['Cost in Rs. (CR)'].sum().sort_values(ascending=False)
fig5, ax5 = plt.subplots(figsize=(8, 5))
role_spending.plot(kind='bar', color='lightgreen', ax=ax5, title='Total Spending by Player Role')
ax5.set_xlabel('Role')
ax5.set_ylabel('Total Price (in Crores)')
ax5.grid(True)
plt.xticks(rotation=45, ha='right')  # Rotate and align labels
fig5.tight_layout(pad=2)

# Create the Tkinter window
root = tk.Tk()
root.title("IPL 2023 Auction Analysis")

# Set the initial size of the window
root.geometry("1400x900")  # Width: 1400px, Height: 900px

# Create a frame for the canvas and scrollbar
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Add a canvas to the frame
canvas = tk.Canvas(frame)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar to the canvas
scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Add a frame inside the canvas to hold the content
content_frame = ttk.Frame(canvas)
canvas.create_window((0, 0), window=content_frame, anchor="nw")

# Function to update the scrollable area
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

content_frame.bind("<Configure>", on_frame_configure)

# Add each chart to the Tkinter content frame
def add_chart(fig, frame):
    chart = FigureCanvasTkAgg(fig, master=frame)
    chart_widget = chart.get_tk_widget()
    chart_widget.pack(pady=20)

# Add all charts
add_chart(fig1, content_frame)
add_chart(fig2, content_frame)
add_chart(fig3, content_frame)
add_chart(fig4, content_frame)
add_chart(fig5, content_frame)

# Run the Tkinter event loop
root.mainloop()
