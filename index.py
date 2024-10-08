import tkinter as tk
from tkinter import messagebox
import requests
import time

def fetch_quote():
    url = url_entry.get()

    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    try:
        # Extract category and listing ID from the URL
        parts = url.split('/')
        category = parts[-2]
        listing_id = parts[-1]

        # Generate the micro timestamp
        micro_timestamp = int(time.time() * 1000)

        # Construct the API URL
        api_url = f"https://www.truckit.net/api/frontend/job/details?_=1728347097112&customer_or_provider=provider&category={category}&listing_id={listing_id}"

        # Replace the micro timestamp in the URL
        api_url = api_url.replace('1728347097112', str(micro_timestamp))

        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        data = response.json()

        # Get the lowest quote
        lowest_quote = data['status']['lowest_quote']

        # Display the lowest quote
        result_label.config(text=f"Lowest Quote: ${lowest_quote}")

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Lowest Quote Finder")

# Create and place the URL entry
url_label = tk.Label(root, text="Enter URL:")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=10)

# Create and place the fetch button
fetch_button = tk.Button(root, text="Fetch Lowest Quote", command=fetch_quote)
fetch_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
