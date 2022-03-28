import pandas as pd
import streamlit as st
import regex as re
from getData import *
from PIL import Image
# Website: streamlit io for Streamlit library (or the Streamlit Blog)

# Containers vs Columns
# Containers create sections in a horizontal way (horizontal formattig)
# Columns create sections in a vertical way (vertical formatting)!

# Let's create some containers
header = st.container()
dataSet = st.container()
features = st.container()
modelDisplay = st.container()

# To write in a container or column , you use the key-word "with"
# along with the name of the container/column variable
with header:
    # title method for streamlit - NOTE, you should only have
    # one title method within your website. For anything else,
    # use the header method.

    # We will use the markdown method which supports Github/HTML style
    # formatting of text. Note-HTML support is set to false as default
    # due to unsafe scenarios that could arise.
    st.title("Analysis of Video Game Popularity")
    st.markdown("**In this project I will look into the popularity of certain"
            " video games over the years!**")

with dataSet:
    # I use the markdown method in order to create some whitespace
    # between the title/project description and the interactable
    # selectbox which handles the data era.
    st.markdown("")

    # Using the Image library to open the figure I want to display.
    # To open the image, I needed to use the directory
    image = Image.open("E:\\dsFiles\\controllers.jpg")

    # Quick formatted image using streamlit column feature.
    # I had two columns of equal width at the front and end,
    # and I had the image in the middle which I accessed
    # using cols[1], or the 1 index.
    cols = st.columns([2, 6, 2])
    with cols[1]:
        st.image(image)

    # streamlit write method also displays information no matter what it is
    st.write("Use the dropbox to select which era of video game"
            " history you would like to explore")

    # Columns to display information vertically.
    # When referencing columns, we will use their
    # variable name. Note-you need at least 2 containers
    # for columns to work
    sel_col, disp_col = st.columns(2)

    # header method - standard practice if you need more headings
    st.header("List of best-selling video games (Kaggle)")
    st.text("I found this data set on Kaggle!")

    # text method, which allows you to display text with
    # a specified width

    # The getData file contains the getGameData method which allows
    # us to get the html table data from the wikipedia page!
    game_data = pd.DataFrame(getGameDataCSV())

    # The selectbox method will display the text of the dropbox, and the other parameters
    # signify the options for the drop down, and the default index.
    # We will use the variable 'era' to hold the value of year
    era = sel_col.selectbox('Which era would you like to go to?',
                            options=[(2016 - i) for i in range(2017 - 1980)], index=0)

    # Columns is a list of the specific columns we want displayed
    # on our website!!
    columns = ["Name", "Platform", "Publisher", "Global Sales (millions)"]

    # Since tables start at the 0 index, we want to increase
    # the member by 1 to follow standard convention
    game_data.index += 1

    # Use pandas rename function to rename Global Sales column
    # Pass inplace parameter as True such that the original data frame
    # object is returned instead of a copy
    game_data.rename(columns=({"Global_Sales" : "Global Sales (millions)"}), inplace=True)

    # Use groupby function on the DataFrame object in order to sort all
    # values by the year they were released. Edit done - 3/27/2022
    formatData = game_data.groupby(['Year'])

    # Streamlit has a built-in method called table which prints out
    # all components directly on the page.
    # Use get_group method in order to display all elements that were
    # released in the same year.
    st.table(formatData[columns].get_group(era).head(50))

    # game data specifically from sales will be displayed on our bar chart
    # sales_distribution = pd.DataFrame(game_data['Global Sales'].value_counts())


with features:
    st.header("About this project")

    # mark_down is the is, as shown, mark_down formatting
    st.markdown('Hello, to whoever may be reading this block of text! I am doing this as a little'
                'side project to improve my knowledge and understanding of web-based development,'
                ' APIs, and Data Science! I always wanted to create my own data-themed website, and'
                ' I love video games, so I thought "Why not just try and do both?"')


with modelDisplay:
    st.header("Work in progress...")


    # The slider method will display the text of the slider, and the other parameters
    # signify the min value, max value, the default value, and the step. (Example here)
    # max_depth = sel_col.slider('What should be the max depth of the model?', min_value=10,
    #               max_value=100, value=20, step=10)



