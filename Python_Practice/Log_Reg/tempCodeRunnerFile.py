mape = mean_absolute_percentage_error(y_test, y_pred)
    print(f"MAPE: {mape}")

    r2 = r2_score(y_test, y_pred)
    print(f"R2 Score: {r2}")