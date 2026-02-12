def r2_score(y_real, y_pred):
    media_y = sum(y_real) / len(y_real)

    ss_total = sum((y - media_y) ** 2 for y in y_real)
    ss_res = sum((y_real[i] - y_pred[i]) ** 2 for i in range(len(y_real)))

    return 1 - (ss_res / ss_total)
