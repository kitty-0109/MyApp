import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    data = pd.read_csv('wines_SPAUpd.csv')
    return data

def plot_distribution(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.histplot(data[column], kde=True, ax=ax)
    ax.set_title(f'Distribution of {column}')
    ax.set_xlabel(column)
    ax.set_ylabel('Count')
    st.pyplot(fig)

def plot_pie_chart(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    data[column].value_counts().plot.pie(autopct='%1.1f%%', ax=ax)
    ax.set_title(f'Pie Chart of {column}')
    st.pyplot(fig)

def plot_box_plot(data, column):
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x=data[column], ax=ax)
    ax.set_title(f'Box Plot of {column}')
    ax.set_xlabel(column)
    st.pyplot(fig)


def load_data2():
    data2 = pd.read_csv('wines_SPAUpdated.csv')
    return data2

def plot_correlation_heatmap(data2):
    fig, ax = plt.subplots(figsize=(12, 8))
    numeric_data = data2.select_dtypes(include=['float64', 'int64'])
    sns.heatmap(numeric_data.corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
    ax.set_title('Correlation Heatmap')
    st.pyplot(fig)

def categorize_columns(data):
    
    data['year'] = pd.to_numeric(data['year'], errors='coerce')
    data['num_reviews'] = pd.to_numeric(data['num_reviews'], errors='coerce')
    data['price'] = pd.to_numeric(data['price'], errors='coerce')

    bins_year = [1900, 1919, 1937, 1956, 1975, 1995, 2025]
    labels_year = ['1900-1918', '1919-1936', '1937-1955', '1956-1974', '1975-1994', '1995-2024']
    data['year'] = pd.cut(data['year'], bins=bins_year, labels=labels_year, right=False)

    bins_num_reviews = [10, 1000, 2000, 3000, 4000, 5000, 6000]
    labels_num_reviews = ['10-999', '1000-1999', '2000-2999', '3000-3999', '4000-4999', '5000-5999']
    data['num_reviews'] = pd.cut(data['num_reviews'], bins=bins_num_reviews, labels=labels_num_reviews, right=False)

    bins_price = [4.90, 174.36, 343.73, 513.10, 682.47, 851.84, 1021.25]
    labels_price = ['4.90-174.35', '174.36-343.72', '343.73-513.09', '513.10-682.46', '682.47-851.83', '851.84-1021.24']
    data['price'] = pd.cut(data['price'], bins=bins_price, labels=labels_price, right=False)

    return data


def main():
    st.title('Insights from wines_SPA Dataset')
    st.write('This app showcases insights from the wines_SPA Dataset.')

    data = load_data()
    data = categorize_columns(data)
    data2 = load_data2()

    st.sidebar.header('Options')

    if st.sidebar.checkbox('Show Dataset'):
        st.write(data)

    if st.sidebar.checkbox('Show Data Summary'):
        st.write(data.describe(include='all'))

    st.sidebar.write("""
    ## About the Dataset
    The dataset contains information about wines including attributes such as winery, wine, year, rating, num_reviews, country, region, price, type, body, and acidity.
    We'll explore various insights from this dataset using different visualization charts.
    """)

    visualization_type = st.sidebar.selectbox('Select Visualization Type', [
        'Distribution Plot', 'Pie Chart', 'Box Plot', 'Correlation Heatmap'
    ])

    if visualization_type == 'Distribution Plot':
        selected_column = st.sidebar.selectbox('Select Column for Distribution Plot', data.columns)
        plot_distribution(data, selected_column)
    elif visualization_type == 'Pie Chart':
        categorical_columns = ['year', 'num_reviews', 'price']
        selected_column = st.sidebar.selectbox('Select Column for Pie Chart', data.columns)
        plot_pie_chart(data, selected_column)
    elif visualization_type == 'Box Plot':
        selected_column = st.sidebar.selectbox('Select Column for Box Plot', data.columns)
        plot_box_plot(data, selected_column)
    elif visualization_type == 'Correlation Heatmap':
        plot_correlation_heatmap(data2)

if __name__ == '__main__':
    main()
