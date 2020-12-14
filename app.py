{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Twitter_Sentiment_Analysis.ipynb",
      "provenance": [],
      "mount_file_id": "1sfuUHU5jDdgsQAyhRkStMgMEyMCB89fO",
      "authorship_tag": "ABX9TyNEMKcdSUcANqvBuPscBiOm",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ChristianBugtai/Twitter-Sentiment-Analysis/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "94K_LnDWZ6pm"
      },
      "source": [
        "#import sys\n",
        "#sys.path.append('/content/drive/MyDrive/Lighthouselabs/Project_Planning/Final_Project')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "_DJqYOf7u8Gi",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "0d9077a2-586b-4619-ae5d-bffb7d89a69d"
      },
      "source": [
        "import streamlit as st\n",
        "import plotly.express as px\n",
        "import utils\n",
        "\n",
        "# Set page title\n",
        "st.title(\"\"\"\n",
        "#Twitter Sentiment Analysis\n",
        "\n",
        "By: Christian Bugtai\n",
        "\n",
        "\"\"\")\n",
        "\n",
        "### TWEET SEARCH AND CLASSIFY ###\n",
        "st.subheader('Search Tweets using Query')\n",
        "\n",
        "# Get user input\n",
        "query = st.text_input('Query:')\n",
        "\n",
        "# As long as the query is valid (not empty or equal to '#')...\n",
        "if query != '':\n",
        "  with st.spinner(f'Searching for and analyzing Tweets using \"{query}\" query...'):\n",
        "    df = utils.getSentiment(query)\n",
        "\n",
        "    df2 = df.groupby(by='Sentiment').count().sort_index(ascending=False).reset_index()\n",
        "    fig = px.pie(df2, names = df2.Sentiment, values = df2.Tweets,\n",
        "             color = df2.Sentiment, color_discrete_map={'Positive':'blue','Negative':'red'})\n",
        "    fig.update_layout(title=\"<b>Positive to Negative Tweets Ratio:</b>\")\n",
        "    fig.update_traces(textposition='inside', textinfo='percent+label')\n",
        "\n",
        "\n",
        "try:\n",
        "  st.plotly_chart(fig)\n",
        "\n",
        "  st.subheader('Top 5 Most Positive Tweets:')\n",
        "  if st.checkbox('Hide Retweets (Retweets may cause duplicate entries)',key=123):\n",
        "    count = 0\n",
        "    test22 = df[df['Sentiment'] == 'Positive'].sort_values(by='Confidence', ascending = False)[['Tweets','Confidence']]\n",
        "    for i, row in test22[test22['Tweets'].str.contains('RT ') == False].head()[['Tweets', 'Confidence']].iterrows():\n",
        "      count += 1\n",
        "      st.write(\"{}. Confidence: {}%\\n -{} \\n\".format(count,row['Confidence'],row['Tweets']))\n",
        "  else:\n",
        "    count = 0\n",
        "    for i, row in df[df['Sentiment'] == 'Positive'].sort_values(by='Confidence', ascending = False).head()[['Tweets','Confidence']].iterrows():\n",
        "      count += 1\n",
        "      st.write(\"{}. Confidence: {}% \\n -{} \\n\".format(count,row['Confidence'],row['Tweets']))\n",
        "\n",
        "  st.subheader('Top 5 Most Negative Tweets:')\n",
        "  if st.checkbox('Hide Retweets (Retweets may cause duplicate entries)',key=456):\n",
        "    count = 0\n",
        "    test22 = df[df['Sentiment'] == 'Negative'].sort_values(by='Confidence', ascending = False)[['Tweets','Confidence']]\n",
        "    for i, row in test22[test22['Tweets'].str.contains('RT ') == False].head()[['Tweets', 'Confidence']].iterrows():\n",
        "      count += 1\n",
        "      st.write(\"{}. Confidence: {}%\\n -{} \\n\".format(count,row['Confidence'],row['Tweets']))\n",
        "  else:\n",
        "    count = 0\n",
        "    for i, row in df[df['Sentiment'] == 'Negative'].sort_values(by='Confidence', ascending = False).head()[['Tweets','Confidence']].iterrows():\n",
        "      count += 1\n",
        "      st.write(\"{}. Confidence: {}% \\n -{} \\n\".format(count,row['Confidence'],row['Tweets']))\n",
        "\n",
        "except NameError: # if no queries have been made yet\n",
        "  pass\n"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[nltk_data] Downloading package wordnet to /root/nltk_data...\n",
            "[nltk_data]   Package wordnet is already up-to-date!\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "7J54AYTLA1ES"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}