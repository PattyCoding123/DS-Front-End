import pandas as pd
# pandas supports webscraping via reading html tables off
# off of wikipedia and other websites that utilize
# html tables. In this case, our html table comes from
# the wikipedia page regarding the best selling video games
# @st.cache
def getGameDataHTML():
    # url is the link to the website
    url = 'https://en.wikipedia.org/wiki/List_of_best-selling_video_games'

    # html_tables is a list of html tables that is returned from
    # pandas read_html method
    html_tables = pd.read_html(url, header=0)

    # the game data is the second html table from the website,
    # so we will get it from the index 1 in the html_tables list.
    gameData = html_tables[1]

    # finally, return the gameData html table
    return gameData

# pandas supports data mining via reading csv files
# and storing the data in a easy, retrievable manner.
# We will use that method for this function.
def getGameDataCSV():
    csv = "E:\\dsFiles\vgsales.csv"

    csv_table = pd.read_csv(csv)

    return csv_table
