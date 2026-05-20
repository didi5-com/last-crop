def check_confidence(confidence, threshold=0.85):
    """
    Stage 4: Confidence Threshold.
    Ensures the model is certain enough before providing a prediction.
    """
    if confidence < threshold:
        return False, "Unable to confidently identify disease."
    return True, "Confidence OK"
