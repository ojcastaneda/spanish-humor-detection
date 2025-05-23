from dotenv import load_dotenv
from humor_detection.llm import (
    predict,
    test_classification,
    test_detection,
    test_exclusive,
    test_lengths,
    test_repetition,
)
from humor_detection.utils import set_random_seeds
from pprint import pprint
import sys

load_dotenv()

set_random_seeds()
prompts = [
    "- Martínez, queda usted despedido.\n- Pero, si yo no he hecho nada.\n- Por eso, por eso.",
    "¿Cuál es el último animal que subió al arca de Noé? El del-fin.",
    "El otro día unas chicas llamarón a mi puerta y me pidieron una pequeña donación para una piscina local.\nLes di un garrafa de agua.",
    "The brain surgeon changed my life. He really opened my mind.",
    "djasndoasndoa",
    "jajaja",
]


def classification_prompter(input: str):
    return f"""{input}
========================================
- Question:
How funny is this text? Do not answer anything else.
1) Slightly
2) Mildly
3) Moderately
4) Very
5) Incredibly
The answer is """


def detection_prompter(input: str):
    return f"""Detect if the following text is funny 1 or not 0 following the provided examples. Do not answer anything else.

Text: Un piano me caería excelente en estos momentos.
Score: 1

Text: Ni Jesús te ama.
Score: 0

Text: Jajajajajajajaj Idiota.
Score: 0

Text: —¿Qué es eso que traes en tu bolsa?
—Un AK-47.
—No, al lado del AK-47.
—Unos Chettos bolita.
—¡No puedes entrar al Cine con comida!
Score: 1

Text: {input}
Score: """


if __name__ == "__main__":
    if sys.argv[1] == "classification":
        pprint(test_classification(classification_prompter))
        pprint(predict(prompts, ["1", "2", "3", "4", "5"], classification_prompter))
    if sys.argv[1] == "detection":
        pprint(test_detection(detection_prompter))
        pprint(test_exclusive(detection_prompter))
        pprint(test_lengths(detection_prompter))
        pprint(test_repetition(detection_prompter))
        pprint(predict(prompts, ["0", "1"], detection_prompter))
