import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load the data
data = pd.read_csv(r'C:\Users\KiuStudnet\PycharmProjects\Student_Depression_Analysis\data\processed_v2_eda_student_depression.csv')
data.dropna(inplace=True)

# Create a figure with multiple subplots
plt.figure(figsize=(15, 10))

# 1. Correlation Analysis
features = ['Sleep Duration', 'Academic Pressure', 'Depression']
correlation_matrix = data[features].corr()

plt.subplot(2, 2, 1)
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', center=0, vmin=-1, vmax=1)
plt.title('Correlation Matrix with Depression')

# 2. Sleep Duration vs Depression Scatter Plot
plt.subplot(2, 2, 2)
sns.regplot(x='Sleep Duration', y='Depression', data=data, scatter_kws={'alpha':0.5})
plt.title('Sleep Duration vs Depression')
sleep_correlation = stats.pearsonr(data['Sleep Duration'], data['Depression'])
plt.xlabel(f'Sleep Duration (hours)\nCorrelation: {sleep_correlation[0]:.3f}, p-value: {sleep_correlation[1]:.3f}')

# 3. Academic Pressure vs Depression Scatter Plot
plt.subplot(2, 2, 3)
sns.regplot(x='Academic Pressure', y='Depression', data=data, scatter_kws={'alpha':0.5})
plt.title('Academic Pressure vs Depression')
pressure_correlation = stats.pearsonr(data['Academic Pressure'], data['Depression'])
plt.xlabel(f'Academic Pressure\nCorrelation: {pressure_correlation[0]:.3f}, p-value: {pressure_correlation[1]:.3f}')

# 4. Combined Box Plot
plt.subplot(2, 2, 4)
data_melted = pd.melt(data[['Sleep Duration', 'Academic Pressure', 'Depression']],
                      var_name='Variable', value_name='Value')
sns.boxplot(x='Variable', y='Value', data=data_melted)
plt.title('Distribution Comparison')

plt.tight_layout()
plt.show()

# Additional Statistical Analysis
print("\nDetailed Statistical Analysis:")
print("\n1. Sleep Duration and Depression:")
sleep_stats = {
    'Correlation': sleep_correlation[0],
    'P-value': sleep_correlation[1],
    'Mean Sleep Hours': data['Sleep Duration'].mean(),
    'Std Sleep Hours': data['Sleep Duration'].std()
}
print(pd.Series(sleep_stats))

print("\n2. Academic Pressure and Depression:")
pressure_stats = {
    'Correlation': pressure_correlation[0],
    'P-value': pressure_correlation[1],
    'Mean Pressure Level': data['Academic Pressure'].mean(),
    'Std Pressure Level': data['Academic Pressure'].std()
}
print(pd.Series(pressure_stats))

# Alternative approach for depression levels using custom bins
depression_bins = [-float('inf'), data['Depression'].quantile(0.33),
                  data['Depression'].quantile(0.66), float('inf')]
data['Depression_Level'] = pd.cut(data['Depression'],
                                bins=depression_bins,
                                labels=['Low', 'Medium', 'High'])

print("\nDepression Level Distribution:")
print(data['Depression_Level'].value_counts())

# Create violin plots for more detailed distribution analysis
plt.figure(figsize=(15, 6))

plt.subplot(1, 2, 1)
sns.violinplot(x='Depression_Level', y='Sleep Duration', data=data)
plt.title('Sleep Duration Distribution by Depression Level')

plt.subplot(1, 2, 2)
sns.violinplot(x='Depression_Level', y='Academic Pressure', data=data)
plt.title('Academic Pressure Distribution by Depression Level')

plt.tight_layout()
plt.show()

# Additional summary statistics by depression level
print("\nAverage Values by Depression Level:")
print(data.groupby('Depression_Level')[['Sleep Duration', 'Academic Pressure']].agg(['mean', 'std']))