"""
Real Estate Market Analysis Dashboard
=====================================
A comprehensive data analysis project analyzing residential real estate properties,
pricing trends, location patterns, and market insights.

Author: Data Analyst
Date: 2024
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 1. DATA GENERATION & PREPROCESSING
# ============================================================================

def generate_real_estate_data(num_records=500):
    """
    Generate realistic real estate dataset with property features and pricing.
    """
    np.random.seed(42)
    
    locations = ['Downtown', 'Suburbs', 'Waterfront', 'Historic District', 'Tech Park']
    property_types = ['Single Family', 'Condo', 'Townhouse', 'Multi-Family']
    
    data = {
        'property_id': np.arange(1, num_records + 1),
        'location': np.random.choice(locations, num_records),
        'property_type': np.random.choice(property_types, num_records),
        'bedrooms': np.random.choice([1, 2, 3, 4, 5], num_records, p=[0.1, 0.25, 0.35, 0.22, 0.08]),
        'bathrooms': np.random.choice([1, 1.5, 2, 2.5, 3], num_records),
        'square_feet': np.random.normal(2000, 500, num_records),
        'year_built': np.random.randint(1950, 2023, num_records),
        'days_on_market': np.random.exponential(30, num_records),
        'list_date': [datetime.now() - timedelta(days=int(x)) for x in np.random.exponential(60, num_records)],
    }
    
    df = pd.DataFrame(data)
    
    # Generate prices based on features
    df['price'] = (
        df['bedrooms'] * 50000 +
        df['bathrooms'] * 30000 +
        df['square_feet'] * 150 +
        (2023 - df['year_built']) * -2000 +
        np.random.normal(0, 50000, num_records) +
        df['location'].map({
            'Waterfront': 150000,
            'Tech Park': 100000,
            'Downtown': 75000,
            'Historic District': 25000,
            'Suburbs': -50000
        })
    )
    
    # Ensure positive prices
    df['price'] = df['price'].clip(lower=100000)
    
    # Add binary features
    df['has_garage'] = np.random.choice([0, 1], num_records, p=[0.3, 0.7])
    df['has_pool'] = np.random.choice([0, 1], num_records, p=[0.85, 0.15])
    df['is_sold'] = np.random.choice([0, 1], num_records, p=[0.4, 0.6])
    
    return df.sort_values('property_id').reset_index(drop=True)


def clean_and_prepare_data(df):
    """
    Clean and prepare data for analysis.
    """
    df_clean = df.copy()
    
    # Remove outliers
    Q1 = df_clean['price'].quantile(0.25)
    Q3 = df_clean['price'].quantile(0.75)
    IQR = Q3 - Q1
    df_clean = df_clean[~((df_clean['price'] < (Q1 - 1.5 * IQR)) | 
                          (df_clean['price'] > (Q3 + 1.5 * IQR)))]
    
    # Feature engineering
    df_clean['price_per_sqft'] = df_clean['price'] / df_clean['square_feet']
    df_clean['property_age'] = 2023 - df_clean['year_built']
    df_clean['list_month'] = df_clean['list_date'].dt.month
    df_clean['price_category'] = pd.cut(df_clean['price'], 
                                        bins=[0, 300000, 500000, 750000, np.inf],
                                        labels=['Budget', 'Mid-Range', 'Premium', 'Luxury'])
    
    return df_clean


# ============================================================================
# 2. EXPLORATORY DATA ANALYSIS
# ============================================================================

def calculate_eda_statistics(df):
    """
    Calculate key statistics for the real estate market.
    """
    stats = {
        'total_properties': len(df),
        'avg_price': df['price'].mean(),
        'median_price': df['price'].median(),
        'price_std': df['price'].std(),
        'avg_bedrooms': df['bedrooms'].mean(),
        'sold_percentage': (df['is_sold'].sum() / len(df)) * 100,
        'avg_days_on_market': df['days_on_market'].mean(),
        'avg_price_per_sqft': df['price_per_sqft'].mean(),
        'properties_with_pool': (df['has_pool'].sum() / len(df)) * 100,
        'properties_with_garage': (df['has_garage'].sum() / len(df)) * 100,
    }
    return stats


def print_eda_summary(stats):
    """
    Print comprehensive EDA summary.
    """
    print("\n" + "="*70)
    print("REAL ESTATE MARKET ANALYSIS - EDA SUMMARY")
    print("="*70)
    print(f"\nDataset Overview:")
    print(f"  • Total Properties Analyzed: {stats['total_properties']:,}")
    print(f"  • Properties Sold: {stats['sold_percentage']:.1f}%")
    print(f"\nPrice Analysis:")
    print(f"  • Average Price: ${stats['avg_price']:,.0f}")
    print(f"  • Median Price: ${stats['median_price']:,.0f}")
    print(f"  • Price Std Dev: ${stats['price_std']:,.0f}")
    print(f"  • Avg Price/SqFt: ${stats['avg_price_per_sqft']:.2f}")
    print(f"\nProperty Features:")
    print(f"  • Average Bedrooms: {stats['avg_bedrooms']:.1f}")
    print(f"  • Properties with Pool: {stats['properties_with_pool']:.1f}%")
    print(f"  • Properties with Garage: {stats['properties_with_garage']:.1f}%")
    print(f"\nMarket Activity:")
    print(f"  • Avg Days on Market: {stats['avg_days_on_market']:.0f} days")
    print("="*70 + "\n")


# ============================================================================
# 3. VISUALIZATION DASHBOARD
# ============================================================================

def create_dashboard(df):
    """
    Create a comprehensive real estate analysis dashboard with 8 subplots.
    """
    # Set style and figure
    plt.style.use('seaborn-v0_8-darkgrid')
    fig = plt.figure(figsize=(16, 12))
    fig.suptitle('Real Estate Market Analysis Dashboard', 
                 fontsize=20, fontweight='bold', y=0.995)
    
    # Color palette for consistency
    colors = ['#2E86AB', '#A23B72', '#F18F01', '#C73E1D', '#6A994E']
    
    # 1. Price Distribution (Histogram)
    ax1 = plt.subplot(3, 3, 1)
    ax1.hist(df['price'] / 1000, bins=30, color=colors[0], alpha=0.7, edgecolor='black')
    ax1.set_xlabel('Price ($1000s)', fontweight='bold')
    ax1.set_ylabel('Frequency', fontweight='bold')
    ax1.set_title('Price Distribution', fontweight='bold', fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # 2. Price by Location (Box Plot)
    ax2 = plt.subplot(3, 3, 2)
    location_order = df.groupby('location')['price'].median().sort_values(ascending=False).index
    df_sorted = df.copy()
    df_sorted['location'] = pd.Categorical(df_sorted['location'], categories=location_order, ordered=True)
    bp = ax2.boxplot([df_sorted[df_sorted['location'] == loc]['price'] for loc in location_order],
                      labels=location_order, patch_artist=True)
    for patch, color in zip(bp['boxes'], colors):
        patch.set_facecolor(color)
        patch.set_alpha(0.7)
    ax2.set_ylabel('Price ($)', fontweight='bold')
    ax2.set_title('Price by Location', fontweight='bold', fontsize=12)
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # 3. Bedrooms vs Price (Scatter)
    ax3 = plt.subplot(3, 3, 3)
    for i, ptype in enumerate(df['property_type'].unique()):
        mask = df['property_type'] == ptype
        ax3.scatter(df[mask]['bedrooms'], df[mask]['price']/1000, 
                   alpha=0.6, label=ptype, s=50, color=colors[i % len(colors)])
    ax3.set_xlabel('Bedrooms', fontweight='bold')
    ax3.set_ylabel('Price ($1000s)', fontweight='bold')
    ax3.set_title('Bedrooms vs Price by Property Type', fontweight='bold', fontsize=12)
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)
    
    # 4. Property Type Distribution (Pie)
    ax4 = plt.subplot(3, 3, 4)
    property_counts = df['property_type'].value_counts()
    ax4.pie(property_counts.values, labels=property_counts.index, autopct='%1.1f%%',
            colors=colors, startangle=90)
    ax4.set_title('Property Type Distribution', fontweight='bold', fontsize=12)
    
    # 5. Price per Square Foot by Location (Bar)
    ax5 = plt.subplot(3, 3, 5)
    price_sqft = df.groupby('location')['price_per_sqft'].mean().sort_values(ascending=False)
    bars = ax5.bar(range(len(price_sqft)), price_sqft.values, color=colors[:len(price_sqft)], alpha=0.7)
    ax5.set_xticks(range(len(price_sqft)))
    ax5.set_xticklabels(price_sqft.index, rotation=45, ha='right')
    ax5.set_ylabel('Price per SqFt ($)', fontweight='bold')
    ax5.set_title('Average Price per Square Foot by Location', fontweight='bold', fontsize=12)
    ax5.grid(True, alpha=0.3, axis='y')
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax5.text(bar.get_x() + bar.get_width()/2., height,
                f'${height:.0f}', ha='center', va='bottom', fontsize=9)
    
    # 6. Days on Market Distribution (Histogram)
    ax6 = plt.subplot(3, 3, 6)
    ax6.hist(df['days_on_market'], bins=25, color=colors[2], alpha=0.7, edgecolor='black')
    ax6.set_xlabel('Days on Market', fontweight='bold')
    ax6.set_ylabel('Frequency', fontweight='bold')
    ax6.set_title('Market Time Distribution', fontweight='bold', fontsize=12)
    ax6.grid(True, alpha=0.3)
    
    # 7. Property Features (Horizontal Bar)
    ax7 = plt.subplot(3, 3, 7)
    features = ['Has Pool', 'Has Garage', 'Is Sold']
    percentages = [
        (df['has_pool'].sum() / len(df)) * 100,
        (df['has_garage'].sum() / len(df)) * 100,
        (df['is_sold'].sum() / len(df)) * 100
    ]
    bars = ax7.barh(features, percentages, color=colors[3:], alpha=0.7)
    ax7.set_xlabel('Percentage (%)', fontweight='bold')
    ax7.set_title('Property Features Prevalence', fontweight='bold', fontsize=12)
    ax7.set_xlim(0, 100)
    ax7.grid(True, alpha=0.3, axis='x')
    
    # Add percentage labels
    for i, (bar, pct) in enumerate(zip(bars, percentages)):
        ax7.text(pct + 2, i, f'{pct:.1f}%', va='center', fontweight='bold')
    
    # 8. Price Category Distribution (Pie)
    ax8 = plt.subplot(3, 3, 8)
    price_cat = df['price_category'].value_counts()
    ax8.pie(price_cat.values, labels=price_cat.index, autopct='%1.1f%%',
            colors=colors, startangle=90)
    ax8.set_title('Property Price Categories', fontweight='bold', fontsize=12)
    
    # 9. Square Footage vs Price (Scatter with regression)
    ax9 = plt.subplot(3, 3, 9)
    ax9.scatter(df['square_feet'], df['price']/1000, alpha=0.5, s=40, color=colors[0])
    # Add trend line
    z = np.polyfit(df['square_feet'], df['price']/1000, 1)
    p = np.poly1d(z)
    ax9.plot(df['square_feet'].sort_values(), p(df['square_feet'].sort_values()), 
            "r--", alpha=0.8, linewidth=2, label='Trend')
    ax9.set_xlabel('Square Feet', fontweight='bold')
    ax9.set_ylabel('Price ($1000s)', fontweight='bold')
    ax9.set_title('Square Footage vs Price', fontweight='bold', fontsize=12)
    ax9.legend()
    ax9.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def create_summary_statistics_table(df):
    """
    Create a summary statistics visualization.
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.axis('tight')
    ax.axis('off')
    
    # Prepare data for table
    summary_data = []
    for location in df['location'].unique():
        location_df = df[df['location'] == location]
        summary_data.append([
            location,
            f"${location_df['price'].mean():,.0f}",
            f"${location_df['price'].median():,.0f}",
            f"{location_df['bedrooms'].mean():.1f}",
            f"{len(location_df)}"
        ])
    
    # Sort by average price
    summary_data.sort(key=lambda x: int(x[1].replace('$', '').replace(',', '')), reverse=True)
    
    # Create table
    table = ax.table(cellText=summary_data,
                    colLabels=['Location', 'Avg Price', 'Median Price', 'Avg Beds', 'Count'],
                    cellLoc='center',
                    loc='center',
                    colWidths=[0.2, 0.2, 0.2, 0.2, 0.15])
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 2)
    
    # Color header
    for i in range(5):
        table[(0, i)].set_facecolor('#2E86AB')
        table[(0, i)].set_text_props(weight='bold', color='white')
    
    # Alternate row colors
    for i in range(1, len(summary_data) + 1):
        for j in range(5):
            if i % 2 == 0:
                table[(i, j)].set_facecolor('#F0F0F0')
            else:
                table[(i, j)].set_facecolor('white')
    
    plt.title('Summary Statistics by Location', fontsize=14, fontweight='bold', pad=20)
    return fig


# ============================================================================
# 4. MAIN EXECUTION
# ============================================================================

def main():
    """
    Main execution function for the real estate analysis project.
    """
    print("\n" + "="*70)
    print("REAL ESTATE DATA ANALYST PROJECT")
    print("="*70)
    
    # Step 1: Generate Data
    print("\n[1/5] Generating realistic real estate dataset...")
    df_raw = generate_real_estate_data(num_records=500)
    print(f"✓ Generated {len(df_raw)} property records")
    
    # Step 2: Clean and Prepare
    print("[2/5] Cleaning and preparing data...")
    df_clean = clean_and_prepare_data(df_raw)
    print(f"✓ Cleaned dataset: {len(df_clean)} properties after outlier removal")
    
    # Step 3: EDA Statistics
    print("[3/5] Calculating exploratory statistics...")
    stats = calculate_eda_statistics(df_clean)
    print_eda_summary(stats)
    
    # Step 4: Create Dashboard Visualization
    print("[4/5] Creating main analysis dashboard...")
    fig1 = create_dashboard(df_clean)
    plt.savefig('/mnt/user-data/outputs/real_estate_dashboard.png', dpi=300, bbox_inches='tight')
    print("✓ Dashboard saved as 'real_estate_dashboard.png'")
    
    # Step 5: Create Summary Table
    print("[5/5] Creating summary statistics table...")
    fig2 = create_summary_statistics_table(df_clean)
    plt.savefig('/mnt/user-data/outputs/summary_statistics.png', dpi=300, bbox_inches='tight')
    print("✓ Summary table saved as 'summary_statistics.png'")
    
    # Save cleaned data
    df_clean.to_csv('/mnt/user-data/outputs/real_estate_cleaned_data.csv', index=False)
    print("✓ Cleaned data saved as 'real_estate_cleaned_data.csv'")
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE!")
    print("="*70)
    print("\nGenerated Files:")
    print("  • real_estate_dashboard.png - Main visualization dashboard")
    print("  • summary_statistics.png - Location-based statistics")
    print("  • real_estate_cleaned_data.csv - Cleaned dataset")
    print("\nKey Insights:")
    print(f"  • Highest avg price location: {df_clean.groupby('location')['price'].mean().idxmax()}")
    print(f"  • Most common property type: {df_clean['property_type'].mode()[0]}")
    print(f"  • Average property age: {df_clean['property_age'].mean():.0f} years")
    print("="*70 + "\n")
    
    plt.show()


if __name__ == "__main__":
    main()