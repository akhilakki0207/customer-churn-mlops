from src.train import model

def test_model_type():
    assert hasattr(model, "predict")
