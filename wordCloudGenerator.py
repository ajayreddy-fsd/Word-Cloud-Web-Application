import streamlit as st
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def wordCloudGenerator():
    # to create heading in the web app
    st.subheader('WordCloud WebApp')

    # to take userInput from the web app
    text = st.text_input('Please enter the text and press enter')

    # some terminal recommended code
    st.set_option('deprecation.showPyplotGlobalUse', False)

    if text != '':
        wordCloud = WordCloud().generate(text)
        plt.imshow(wordCloud)

        # to remove the axes on the plot
        plt.axis('off')
        st.pyplot()


wordCloudGenerator()
