from scholarly import scholarly

# Define the title of the paper you're looking for
target_title = "First measurements on the new FPGA-based DIRICH MAPMT readout"

# Search for the paper by title
search_query = scholarly.search_pubs(target_title)

# Loop through the search results and find the exact match
for result in search_query:
    # Check if the title matches the target title (ignoring case)
    if result['bib'].get('title', '').lower() == target_title.lower():
        # Print details of the specific paper
        print("Title:", result['bib'].get('title', 'N/A'))
        print("Author(s):", result['bib'].get('author', 'N/A'))
        print("Publication Year:", result['bib'].get('pub_year', 'N/A'))
        print("Journal:", result['bib'].get('venue', 'N/A'))
        print("Abstract:", result['bib'].get('abstract', 'N/A'))

        # Get the citation count, if available
        print("Citations:", result.get('num_citations', 'N/A'))

        # Optionally print the BibTeX entry
        #print("BibTeX Entry:\n", result.get('bibtex', 'N/A'))
        print("---------------------------------------------------------")
        print("BibTeX Entry:\n", scholarly.bibtex(result))
        # Stop after finding the specific paper
        break
else:
    print("The specific paper was not found.")
