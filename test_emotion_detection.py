from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        test_cases = [
            ["I am glad this happened", "joy"],
            ["I am really mad about this", "anger"],
            ["I feel disgusted just hearing about this", "disgust"],
            ["I am so sad about this", "sadness"],
            ["I am really afraid that this will happen", "fear"]
        ]
        for test_case in test_cases:
            text, emotion = test_case
            self.assertEqual(emotion_detector(text)["dominant_emotion"], emotion)

unittest.main()
