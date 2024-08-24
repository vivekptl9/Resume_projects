import csv
import time, random
from scholarly import scholarly, ProxyGenerator


pg = ProxyGenerator()
pg.FreeProxies()

scholarly.use_proxy(pg)
# Define the title of the paper you're looking for
target_title = "Event reconstruction of free-streaming data for the RICH detector in the CBM experiment"

# Search for the paper by title
search_query = scholarly.search_pubs(target_title)

# Loop through the search results and find the exact match
for result in search_query:
    if result['bib'].get('title', '').lower() == target_title.lower():
        # Get the BibTeX entry as a string
        bibtex_entry = scholarly.bibtex(result)

        # Manually extract the fields
        bibtex_lines = bibtex_entry.splitlines()
        bibtex_dict = {}
        for line in bibtex_lines:
            # Skip the first and last lines containing the type and closing brace
            if "=" in line:
                # Split by the first '=' and remove unnecessary characters
                key, value = line.split("=", 1)
                key = key.strip().lower()
                value = value.strip().strip('{},').strip('"')
                bibtex_dict[key] = value

        # Save parsed BibTeX fields to a .csv file
        with open("bibtex_output.csv", "w", newline='') as csvfile:
            writer = csv.writer(csvfile)

            # Write header (column names)
            writer.writerow(["Field", "Value"])

            # Write each BibTeX field to the CSV file
            for key, value in bibtex_dict.items():
                writer.writerow([key, value])

        print("Parsed BibTeX fields saved to bibtex_output.csv")
        break
else:
    print("The specific paper was not found.")

time.sleep(random.uniform(5,15))