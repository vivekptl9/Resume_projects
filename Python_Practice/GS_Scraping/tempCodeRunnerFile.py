driver = webdriver.Chrome()  # Use Firefox() or other browsers if needed

# URL of the Google Scholar search
url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=HADES+Vivek+patel&oq="

# Open the URL
driver.get(url)

# Create an explicit wait object to wait for elements to load
wait = WebDriverWait(driver, 10)  # 10 seconds timeout

# Find all the citation buttons on the page
citation_buttons = driver.find_elements(By.CLASS_NAME, 'gs_or_cit')

# Iterate through the citation buttons and click them
for button in citation_buttons:
    try:
        # Click the citation button to open the citation options
        button.click()

        # Wait for the citation menu to appear
        wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'gs_citi')))

        # Find the BibTeX link in the modal that appears and click it
        bibtex_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'BibTeX')))
        bibtex_link.click()

        # Wait for the BibTeX page to load and extract the BibTeX content
        bibtex_content = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, 'pre'))).text
        print("BibTeX Content:\n", bibtex_content)
        print("---------------------------------------------------------")

        # Go back to the search results page
        driver.back()  # To go back from the BibTeX page
        driver.back()  # To go back from the citation menu
        wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, 'gs_or_cit')))

    except Exception as e:
        print(f"An error occurred: {e}")
        continue

# Close the browser when done
driver.quit()
