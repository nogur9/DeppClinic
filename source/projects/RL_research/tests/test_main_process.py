import numpy as np
import pandas as pd
from source.projects.RL_research.cross_val import main
from source.projects.RL_research.params import QUESTIONS


def y_logic(row):
    if row["a"] > 0.5:
        if row["b"] > 0.5:
            return 0
        else:
            return 1
    else:
        if row["c"] > 0.5:
            return 0
        else:
            return 1


def create_simulated_data(size=200):
    column_a = np.random.rand(size)  # Generates data between 0 and 1, if that's needed
    column_b = np.random.rand(size)
    column_c = np.random.rand(size)

    id_array = np.arange(size)

    df = pd.DataFrame({
        "a": column_a, 
        "b": column_b, 
        "c": column_c,
        "id": id_array

    })
    y = df.apply(y_logic, axis=1)
    df["Y"] = y
    return df


def test_main_process():
    df = create_simulated_data()
    main(df, custom_questions=["a", "b", "c"])
    print("done")


if __name__ == "__main__":
    test_main_process()
