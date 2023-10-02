import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from bidi.algorithm import get_display


# Load datasets
form1 = pd.read_csv('./form1.csv')
form2 = pd.read_csv('./form2.csv')
form3 = pd.read_csv('./form3.csv')
form4 = pd.read_csv('./form4.csv')

# Combine the datasets
combined_form = pd.concat([form1, form2, form3, form4], ignore_index=True)


def features_distributions():
    sns.set(style="whitegrid")
    
    categorical_features = ['sex', 'political_stance', 'pro_reform', 'pro_protest', 'pro_arnona']

    # Plotting the distribution of age
    plt.figure(figsize=(8, 5))
    sns.histplot(data=combined_form, x='age', bins=20, kde=True)
    plt.title(get_display('תרשים 1: התפלגות גילאי המשתתפים'))
    plt.ylabel(get_display('תדירות'))
    plt.xlabel(get_display('גיל'))
    plt.show()

    # Customize labels
    label_mapping = {
        'sex': {0: 'Female', 1: 'Male'},
        'pro_reform': {0: 'Against Reform', 1: 'Pro Reform'},
        'pro_protest': {0: 'Against Protests', 1: 'Pro Protests'},
        'pro_arnona': {0: 'Against Arnona Fund', 1: 'Pro Arnona Fund', 2: 'No Opinion'}
    }

    # Apply label mapping to the dataset
    for feature, mapping in label_mapping.items():
        combined_form[feature] = combined_form[feature].map(mapping)

    # Set style for plots
    sns.set(style="whitegrid")

    # Plotting the distribution of categorical features
    categorical_features = ['sex', 'political_stance', 'pro_reform', 'pro_protest', 'pro_arnona']

    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(15, 10))
    # fig.suptitle(get_display('תרשים 2: התפלגות המשתנים שנאספו. מין, דעה פוליטית ותמיכה ברפורמה, הפגנות וחוק קרן הארנונה'), fontsize=16)

    titles = [
        "תרשים 2: התפלגות מין המשתתפים",
        "תרשים 3: התפלגות הדעה הפוליטית של המשתתפים",
        "תרשים 4: התפלגות תמיכה ברפורמה של המשתתפים",
        "תרשים 5: התפלגות תמיכה בהפגנות של המשתתפים",
        "תרשים 6: התפלגות תמיכה בחוק קרן הארנונה של המשתתפים"
    ]
    titles = [get_display(title) for title in titles]


    for i, feature in enumerate(categorical_features):
        row = i // 3
        col = i % 3
        ax = axes[row, col]
        ax.set_title(titles[i], fontsize=14, y = 1.05)
        sns.countplot(data=combined_form, x=feature, ax=ax)
        
        # Calculate and annotate percentages on the bars
        total = len(combined_form[feature])
        for p in ax.patches:
            height = p.get_height()
            ax.text(p.get_x() + p.get_width() / 2.,
                    height + 1,
                    '{:1.1f}%'.format(100 * height / total),
                    ha="center") 

    # Hide the empty subplot
    axes[1, 2].axis('off')

    # Adjust the layout
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()



def posts_distributions():
    colors = sns.color_palette("RdYlGn", n_colors=7)
    addon = [
    "(נגד ההפגנות)",
    "(נגד הפורמה)",
    "(נגד חוק הארנונה)",
    "(בעד חוק הארנונה)"
    ]
    # Loop through each set of columns and create a histogram
    for i in range(1, 5):
        col = f'post{i}_agree'
        col_data = combined_form[col]
        
        # Create a histogram for the current column
        plt.figure(figsize=(8,6))
        
        # Count the frequency of each unique value in the column
        value_counts = col_data.value_counts().sort_index()
        total = len(col_data)
        
        # Plot each bar separately with a unique color
        for idx, (val, count) in enumerate(value_counts.items()):
            plt.bar(val, count, color=colors[idx], alpha=0.7)
            
            # Calculate the percentage and add it above the bar
            percentage = (count / total) * 100
            plt.text(val, count, f'{percentage:.1f}%', ha='center', va='bottom')
        
        plt.title(get_display(f'תרשים {i + 6}: התפלגות ההסכמה עם פוסט {i} {addon[i-1]}'))
        plt.xlabel(get_display(f'הסכמה עם פוסט {i}'))
        plt.ylabel(get_display(f'תדירות'))
        plt.show()



features_distributions()
posts_distributions()