import pandas as pd
from sklearn import preprocessing,linear_model,metrics
from sklearn.model_selection import train_test_split
# Read the following link and complete this homework. https://www.codemag.com/Article/1711091/Implementing-Machine-Learning-Using-Python-and-Scikit-learn

# Make sure to install scikit-learn and Pandas

def step1():
    """
    # Step 1: Getting the Titanic Dataset
    Return a dataframe containing the Titantic dataset from the following URL
    # URL: https://gist.githubusercontent.com/mkzia/aa4f293661dba857b8c4459c0095ac95/raw/8075037f6f7689a1786405c1bc8ea9471d3aa9c3/train.csv

    """
    # BEGIN SOLUTION
    df = pd.read_csv('https://gist.githubusercontent.com/mkzia/aa4f293661dba857b8c4459c0095ac95/raw/8075037f6f7689a1786405c1bc8ea9471d3aa9c3/train.csv')
    # END SOLUTION
    return df


def step2(df):
    """
    # Step 2: Clean data
    Modify df to drop the following columns:
    PassengerId
    Name
    Ticket
    Cabin
    Hint: Just pass all the columns to the .drop() method as an array
    return dataframe
    """
    # BEGIN SOLUTION
    df.drop(['PassengerId','Name','Ticket','Cabin'],inplace=True,axis=1)
    # END SOLUTION
    return df


def step3(df):
    """
    # Step 3: Drop NaNs and reindex
    You want to reindex so your index does not have missing values after you drop the NaNs. Remember, index is used 
    to access a row. Notice how many rows you dropped!
    Modify df to drop NaNs and reindex
    return dataframe
    """
    # BEGIN SOLUTION
    df.dropna(inplace=True)
    df.reset_index(drop=True,inplace=True)
    # END SOLUTION
    return df


def step4(df):
    """
    # Step 4: Encoding the Non-Numeric Fields
    Encode text fields to numbers
    Modify df to encode Sex and Embarked to encoded values.
    return dataframe
    """
    # BEGIN SOLUTION
    label_encoder = preprocessing.LabelEncoder()
    sex_encoded = label_encoder.fit_transform(df["Sex"])
    df['Sex'] = sex_encoded

    embarked_encoded = label_encoder.fit_transform(df["Embarked"])
    df['Embarked'] = embarked_encoded
    # END SOLUTION
    return df


def step5(df):
    """
    # Step 5: Making Fields Categorical
    Turn values that are not continues values into categorical values
    Modify df to make Pclass, Sex, Embarked, and Survived a categorical field
    return dataframe
    """
    # BEGIN SOLUTION
    df["Pclass"]   = pd.Categorical(df["Pclass"])
    df["Sex"]      = pd.Categorical(df["Sex"])
    df["Embarked"] = pd.Categorical(df["Embarked"])
    df["Survived"] = pd.Categorical(df["Survived"])

    # print(df.dtypes) 
    # END SOLUTION
    return df


def step6(df):
    """
    1. Split dataframe into feature and label
    2. Do train and test split; USE: random_state = 1
    4. Use LogisticRegression() for classification
    3. Return accuracy and confusion matrix

    Use  metrics.confusion_matrix to calculate the confusion matrix
    # https://towardsdatascience.com/understanding-confusion-matrix-a9ad42dcfd62
    # https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
    # IMPORTANT !!!! 
    # https://stackoverflow.com/questions/56078203/why-scikit-learn-confusion-matrix-is-reversed

    From the confusion matrix get TN, FP, FN, TP

    return --> accuracy, TN, FP, FN, TP; 
    Hint: round accuracy to 4 decimal places

    """
    # BEGIN SOLUTION
    # features for training
    features = df.drop(['Survived'],axis=1)

    # the label is Survived
    label = df['Survived']

    train_features,test_features,train_label,test_label = train_test_split(
                        features,
                        label,
                        test_size = 0.25, # split ratio
                        random_state = 1, # Set random seed
                        stratify = df["Survived"])
    log_regress = linear_model.LogisticRegression()
    # Train the model
    log_regress.fit(X = train_features, y = train_label)
    accuracy = round(log_regress.score(X = test_features, y = test_label),4)
    preds = log_regress.predict(X=test_features)
    [[TN, FP],[FN,TP]] = metrics.confusion_matrix(y_true = test_label,y_pred = preds)
    return accuracy, TN, FP, FN, TP
    # END SOLUTION
    # return accuracy, TN, FP, FN, TP
