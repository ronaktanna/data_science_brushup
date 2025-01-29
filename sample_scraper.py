# """
# @author: ronaktanna
# """
#
# from bs4 import BeautifulSoup
# from urllib.request import urlopen
# import pandas as pd
#
# wikipedia_link = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"
# html_page = urlopen(wikipedia_link)
# scraper = BeautifulSoup(html_page)
#
# table_of_the_billionaires = scraper.find("table", class_="wikitable sortable")
# table_body = table_of_the_billionaires.find("tbody")
#
# data = list()
# table_rows = table_body.find_all("tr")
#
# for idx, row in enumerate(table_rows):
#     if idx == 0:
#         cols = row.find_all("th")  # first <tr> is a header
#     else:
#         cols = row.find_all("td")
#
#     cols = [elem.text.strip() for elem in cols]
#     data.append([elem for elem in cols if elem])
#
# dataframe = pd.DataFrame(columns=data[0])
# for idx in range(1, len(data)):
#     # dataframe = dataframe.append(pd.Series(data[idx], index=data[0]), ignore_index=True)
#     dataframe = pd.concat([dataframe, pd.Series(data[idx], index=data[0])], ignore_index=True)
#
# print(dataframe.to_string())

"""
@author: ronaktanna
"""

from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd


def scrape_billionaires():
    wikipedia_link = "https://en.wikipedia.org/wiki/The_World%27s_Billionaires"

    # Add error handling for URL opening
    try:
        html_page = urlopen(wikipedia_link)
    except Exception as e:
        print(f"Error accessing URL: {e}")
        return None

    # Specify parser explicitly
    scraper = BeautifulSoup(html_page, 'html.parser')

    # Add error handling for table finding
    table_of_the_billionaires = scraper.find("table", class_="wikitable sortable")
    if not table_of_the_billionaires:
        print("Table not found on the page")
        return None

    table_body = table_of_the_billionaires.find("tbody")

    data = []
    table_rows = table_body.find_all("tr")

    # Separate header processing from data processing
    headers = [elem.text.strip() for elem in table_rows[0].find_all("th")]

    # Process remaining rows
    for row in table_rows[1:]:
        cols = row.find_all("td")
        row_data = [elem.text.strip() for elem in cols]
        if row_data:  # Only append if row has data
            data.append(row_data)

    # Create DataFrame directly from data
    df = pd.DataFrame(data, columns=headers)

    return df


if __name__ == "__main__":
    df = scrape_billionaires()
    if df is not None:
        print(df.to_string())