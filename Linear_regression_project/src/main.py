# main.py
import data_ingestion
import preprocessing
import regression
import residuals
import visualization

def main():
    # 1. Load Data
    df = data_ingestion.load_data("data/RMBR4-2_export_test.csv")

    # 2. Preprocess
    df = preprocessing.preprocess_data(df, method="zscore")

    # 3. Regression
    model, predictions = regression.run_regression(df)

    # 4. Residual Analysis
    residuals.analyze_residuals(df, predictions)

    # 5. Visualization
    visualization.plot_results(df, predictions)

if __name__ == "__main__":
    main()
