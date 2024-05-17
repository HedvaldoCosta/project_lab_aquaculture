import pandas as pd
import streamlit as st


def extract_data(dataset):
    data_raw = pd.read_csv(dataset)
    return data_raw


if __name__ == 'main':
    dataframe = extract_data(dataset="")
