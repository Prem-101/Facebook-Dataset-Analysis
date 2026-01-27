import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer

def load_facebook_data(file_path='Facebook_Marketplace_data.csv'):
    """Load and preprocess Facebook marketplace data"""
    df = pd.read_csv(file_path)
    
    # Convert timestamp to datetime
    df['status_published'] = pd.to_datetime(df['status_published'])
    
    # Drop any unnamed columns
    df = df.drop(df.filter(regex=r'Column\d').columns, axis=1, errors='ignore')
    
    # Extract time components
    df['hour'] = df['status_published'].dt.hour
    df['day_of_week'] = df['status_published'].dt.day_name()
    df['month'] = df['status_published'].dt.month_name()
    
    return df

def prepare_clustering_data(df):
    """Prepare data for clustering analysis"""
    features = ['status_type', 'num_reactions', 'num_comments', 'num_shares', 
               'num_likes', 'num_loves', 'num_wows', 'num_hahas', 'num_sads', 'num_angrys']
    
    data = df[features].copy()
    
    # Declaring Column Transformer
    preprocessor = ColumnTransformer(
        transformers=[
            ('cat', OneHotEncoder(drop='first', sparse_output=False), ['status_type']),
            ('num', StandardScaler(), [col for col in features if col != 'status_type'])
        ]
    )
    
    return preprocessor.fit_transform(data), data