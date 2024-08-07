def ObjectToInt(df):
    
    from sklearn.preprocessing import LabelEncoder

    le = LabelEncoder()

    for i in df.columns:
        if df[i].dtype == 'object':
            df[i] = le.fit_transform(df[i])

    return df


def Outliers_Visualization(df):
    import ipywidgets as widgets
    from IPython.display import display
    import matplotlib.pyplot as plt
    import seaborn as sns


    # Function to create boxplot for a single column
    def create_boxplot(column):
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=df[column])
        plt.xlabel(column)
        plt.ylabel('Values')
        plt.title(f'Boxplot of {column}')
        plt.show()

    # Create a dropdown widget for column selection
    column_selector = widgets.Dropdown(
        options=df.columns.tolist(),
        description='Column:',
        style={'description_width': 'initial'}
    )

    # Create the interactive widget
    interactive_widget = widgets.interactive(create_boxplot, column=column_selector)
    
    return interactive_widget
