import csv
import re

def process_csv(input_csv_file):
    # Check if the input CSV file exists
    try:
        with open(input_csv_file, 'r') as f:
            pass
    except FileNotFoundError:
        print("Error: Input CSV file not found!")
        return

    # Initialize dictionaries for titles under each category
    categories = {
        "overview": [],
        "campus": [],
        "courses": [],
        "scholarships": [],
        "admission": [],
        "placements": [],
        "results": [],
        "other": []
    }

    # Process the input CSV file
    with open(input_csv_file, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            url = row[0]  # First value is URL

            # Combine the rest of the values as title
            title = ','.join(row[1:])

            # Sanitize URL and title
            url = re.sub('[^a-zA-Z0-9/:]', '', url)
            title = re.sub('[^a-zA-Z0-9\\s]', '', title)

            # Categorize URL
            category = ""
            if "overview" in url:
                category = "overview"
            elif "campus" in url:
                category = "campus"
            elif "courses" in url:
                category = "courses"
            elif "scholarships" in url:
                category = "scholarships"
            elif "admission" in url:
                category = "admission"
            elif "placements" in url:
                category = "placements"
            elif "results" in url:
                category = "results"
            else:
                category = "other"

            # Append URL and title to corresponding category
            categories[category].append((url, title))

    # Generate output CSV file
    output_file = "output.csv"
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["URL", "overview", "campus", "courses", "scholarships", "admission", "placements", "results"])

        # Output URLs and titles for each category
        for cat in categories.keys():
            for url, title in sorted(categories[cat], key=lambda x: x[0]):
                writer.writerow([url, title])

    print("Output CSV file generated: " + output_file)

# Call the function to process the CSV file
process_csv(r"C:\Users\sasan\Desktop\nano123urls.csv")