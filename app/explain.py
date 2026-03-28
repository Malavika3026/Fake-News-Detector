def generate_explanation(prediction: int) -> str:
    """
    Local, rule-based explanation (no external API)
    """
    if prediction == 1:
        return (
            "The ML model classified this news as REAL because the language "
            "appears neutral, detailed, and similar to professional news reporting."
        )
    else:
        return (
            "The ML model classified this news as FAKE because the content lacks "
            "verified context, appears sensational, or resembles a standalone claim "
            "rather than a complete news article."
        )
