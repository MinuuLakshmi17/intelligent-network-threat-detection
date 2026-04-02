from src.data_preprocessing import load_data, preprocess_data
from src.train_model import train_model, evaluate
from src.train_model import plot_feature_importance

def main():
    print("Loading data...")
    df = load_data()

    print("Preprocessing...")
    X_train, X_test, y_train, y_test, feature_names = preprocess_data(df)

    print("Training model...")
    model = train_model(X_train, y_train)

    print("Evaluating model...")
    evaluate(model, X_test, y_test)

    plot_feature_importance(model, feature_names)


if __name__ == "__main__":
    main()

