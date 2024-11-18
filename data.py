from bs4 import BeautifulSoup

# Read the HTML file
with open("protected_page.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Locate the second table
tables = soup.find_all("table")  # Find all tables

print(len(tables))

table = tables[3]  # Get the second table (index 1)

# Extract data from columns 4 to 6
extracted_data = []
rows = table.find_all("tr")
# print(len(rows))
for row in rows:
    cells = row.find_all("td")
    if len(cells) >= 6:  # Ensure the row has enough columns
        col4 = cells[3].get_text(strip=True)  # Column 4
        col5 = cells[4].get_text(strip=True)  # Column 5
        col6 = cells[5].get_text(strip=True)  # Column 6
        extracted_data.append(f"{col4}\t|{col5}\t|{col6}")

# Save the extracted data to a .txt file
with open("extracted_data.txt", "w", encoding="utf-8") as f:
    for line in extracted_data:
        f.write(line + "\n")

print("Data from columns 4 to 6 of the second table has been saved to extracted_data.txt!")
