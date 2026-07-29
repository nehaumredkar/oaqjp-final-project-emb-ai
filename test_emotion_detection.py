"""Unit tests for the Emotion Detection package."""

from EmotionDetection import emotion_detector


def test_emotion_detector():
    """Test the emotion_detector function."""

    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for statement, expected_emotion in test_cases.items():
        response = emotion_detector(statement)

        if response["dominant_emotion"] == expected_emotion:
            print(
                f"PASS: '{statement}' -> {response['dominant_emotion']}"
            )
        else:
            print(
                f"FAIL: '{statement}' -> "
                f"Expected {expected_emotion}, "
                f"Got {response['dominant_emotion']}"
            )


if __name__ == "__main__":
    test_emotion_detector()