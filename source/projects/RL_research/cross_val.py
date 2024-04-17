# Import the necessary libraries
import numpy as np
from catboost import CatBoostClassifier
import warnings
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, average_precision_score, accuracy_score, f1_score

from source.projects.RL_research.params import file_path, QUESTIONS, N_EPISODES
from source.projects.RL_research.runing_agent import do_interview, train_agent


def load_data():
    df = pd.read_csv(file_path)
    df = df.fillna(0)
    time1_df = df[df.measurement.isin(['Time 1'])]
    time2_df = df[df.measurement.isin(['Time 2'])]

    df = time1_df.merge(time2_df, on='id', suffixes=['', '_time_2'])

    df['Y'] = df['modcon_target_time_2'].astype(int)
    df = df[QUESTIONS + ['id', 'Y']]
    return df


def load_and_split_data():
    df = load_data()

    X = df.drop("Y", axis=1)
    y = df["Y"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)
    return X_train, X_test, y_train, y_test


def train_model(X_train, X_test, y_train):
    df_train = X_train.copy()
    df_train["Y"] = y_train

    agent = train_agent(df_train.id.unique(), df_train, n_episodes=N_EPISODES)

    X_train = do_interview(X_train, agent).drop("id", axis=1)
    X_test = do_interview(X_test, agent).drop("id", axis=1)

    model = CatBoostClassifier(verbose=False, auto_class_weights='Balanced')
    model.fit(X_train, y_train)
    return model, X_test


"""
Chat GPT notes:

Dependency on id in do_interview: Your process relies heavily on the presence and integrity of id fields.
 Ensure robustness by validating the uniqueness and consistency of these IDs across your data transformations.

train_model Workflow Clarity: The reassignment of X_train and X_test after do_interview might be confusing.
 It's essential to document or comment that these are transformed versions of the original datasets,
  now enriched with insights from the RL agent.

"""


def plot_confusion_matrix(y_test, y_pred):
    cm = confusion_matrix(y_test, y_pred)

    # Print the confusion matrix
    print("Confusion Matrix:")
    print(cm)

    # Plot the confusion matrix
    fig, ax = plt.subplots()
    cax = ax.matshow(cm, cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    fig.colorbar(cax)

    # Set up axes
    ax.set_xticklabels([''] + list(np.unique(y_test)))
    ax.set_yticklabels([''] + list(np.unique(y_test)))

    # Label axes
    plt.xlabel('Predicted')
    plt.ylabel('True')

    # Annotate each cell with the numeric value
    for (i, j), val in np.ndenumerate(cm):
        ax.text(j, i, f'{val}', ha='center', va='center', color='red')

    plt.show()


def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Calculate the metrics
    roc_auc = roc_auc_score(y_test, y_prob)
    pr_auc = average_precision_score(y_test, y_prob)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    # Print the results
    print(f"ROC-AUC: {roc_auc:.4f}")
    print(f"PR-AUC: {pr_auc:.4f}")
    print(f"Accuracy: {acc:.4f}")
    print(f"F1-score: {f1:.4f}")
    plot_confusion_matrix(y_test, y_pred)


def main():
    warnings.simplefilter(action='ignore', category=FutureWarning)
    X_train, X_test, y_train, y_test = load_and_split_data()
    model, X_test = train_model(X_train, X_test, y_train)
    evaluate_model(model, X_test, y_test)


if __name__ == "__main__":
    main()