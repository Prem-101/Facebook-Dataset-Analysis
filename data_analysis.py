"""
Facebook Live Sellers Dataset Analysis Module.
This module contains functions for analyzing Facebook Live Sellers data.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.cluster import KMeans
from sklearn.compose import ColumnTransformer

def load_and_prepare_data(filepath):
    """Load and prepare the dataset for analysis."""
    df = pd.read_csv(filepath)
    df['status_published'] = pd.to_datetime(df['status_published'])
    df = df.drop(df.filter(regex=r'Column\d').columns, axis=1, errors='ignore')
    return df

def add_time_features(df):
    """Add time-based features to the dataframe."""
    df['hour'] = df['status_published'].dt.hour
    df['day_of_week'] = df['status_published'].dt.day_name()
    df['month'] = df['status_published'].dt.month_name()
    return df

def get_engagement_metrics(df):
    """Calculate engagement metrics by post type."""
    return df.groupby('status_type')[['num_reactions', 'num_comments', 'num_shares']].mean()

def perform_clustering(df, n_clusters=3):
    """Perform KMeans clustering on the dataset."""
    data = df[['status_type', 'num_reactions', 'num_comments', 'num_shares', 
               'num_likes', 'num_loves', 'num_wows', 'num_hahas', 'num_sads', 'num_angrys']].copy()
    
    preprocessor = ColumnTransformer([
        ('cat', OneHotEncoder(drop='first', sparse_output=False), ['status_type']),
        ('num', StandardScaler(), ['num_reactions', 'num_comments', 'num_shares', 
                                 'num_likes', 'num_loves', 'num_wows', 'num_hahas', 
                                 'num_sads', 'num_angrys'])
    ])
    
    X_preprocessed = preprocessor.fit_transform(data)
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    data.loc[:, 'cluster'] = kmeans.fit_predict(X_preprocessed)
    
    return data, kmeans.inertia_