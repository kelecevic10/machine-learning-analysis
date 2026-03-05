from pathlib import Path
import json 
import joblib 

class ResultsManager: 
    """
        Utility class that organizes and saves models, metrics, tables and plots for each algorithm  
    """

    def _init_(self, model_name: str, base_dir = "../results/"):
        self.model_name = model_name
        self.base_dir = Path(base_dir)
        self.model_dir = self.base_dir / model_name

        # create directory if it does not eists 
        self.model_dir.mkdir(parents = True, exist_ok = True)

    def save_model(self, model):
        path = self.model_dir / "model.pkl"
        joblib.dump(model, path)
        
        print(f"Model saved to {path}")

    def load_model(self):
        path = self.model_dir / "model.pkl"

        if path.exists():
            return joblib.load(path)
        
        return None 
    
    def save_metrics(self, metrics: dict):
        path = self.model_dir / "metrics.json"

        with open(path, "w") as f:
            json.dump(metrics, f, indent = 4)
        
        print(f"Metrics saved to {path}")

    def save_plot(self, plt, name: str, dpi = 300):
        path = self.model_dir / f"{name}.png"
        plt.savefig(path, dpi = dpi, bbox_inches = "tight")
        plt.close()

        print(f"Plot saved to {path}")