import pandas as pd
import numpy as np
from datetime import datetime

class FacebookDataProcessor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.df = None

    def load_data(self):
        """Load the Facebook Marketplace data"""
        self.df = pd.read_csv(self.file_path)
        return self.df

    def preprocess_data(self):
        """Preprocess the dataset"""
        if self.df is None:
            self.load_data()
            
        # Convert status_published to datetime
        self.df['status_published'] = pd.to_datetime(self.df['status_published'])
        
        # Extract time features
        self.df['hour'] = self.df['status_published'].dt.hour
        self.df['day_of_week'] = self.df['status_published'].dt.day_name()
        self.df['month'] = self.df['status_published'].dt.month_name()
        
        # Remove any unnamed columns
        self.df = self.df.drop(self.df.filter(regex=r'Column\\d').columns, axis=1, errors='ignore')
        
        return self.df

    def get_engagement_metrics(self):
        """Get engagement metrics by different time periods"""
        if self.df is None:
            self.preprocess_data()
            
        hourly_reactions = self.df.groupby('hour')['num_reactions'].mean().reset_index()
        daily_reactions = self.df.groupby('day_of_week')['num_reactions'].mean().reindex([
            'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'
        ])
        monthly_reactions = self.df.groupby('month')['num_reactions'].mean().reindex([
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ])
        
        return hourly_reactions, daily_reactions, monthly_reactions

    def get_post_type_stats(self):
        """Get statistics about different post types"""
        if self.df is None:
            self.preprocess_data()
            
        post_type_counts = self.df['status_type'].value_counts()
        avg_metrics = self.df.groupby('status_type')[['num_reactions', 'num_comments', 'num_shares']].mean()
        
        return post_type_counts, avg_metrics