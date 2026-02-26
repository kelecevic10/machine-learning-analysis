import numpy as np
import os

def load_processed_data(path):
    
    if not os.path.exists(path):
        raise FileNotFoundError(f"Processed dataset not found at: {path}")
    
    data = np.load(path, allow_pickle=True)
    dataset = {
        "X_train": data["X_train"],
        "X_test": data["X_test"],
        "y_train": data["y_train"],
        "y_test": data["y_test"],
        "font_train": data["font_train"],
        "font_test": data["font_test"],
        "strength_train": data["strength_train"],
        "strength_test": data["strength_test"],
        "italic_train": data["italic_train"],
        "italic_test": data["italic_test"],
    }

    return dataset