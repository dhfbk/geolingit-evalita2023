"""
Evaluation script for the GeoLingIt shared task at EVALITA 2023.

Usage: python eval.py -S $SUBTASK -G $GOLD_FILEPATH -P $PRED_FILEPATH
- $SUBTASK: The subtask the submission refers to. Choices: ['a', 'b'].
- $GOLD_FILEPATH: Path to the gold standard for the subtask.
- $PRED_FILEPATH: Path to the file that contains predictions for the subtask, with the same format as $GOLD_FILEPATH.
"""

import argparse
from haversine import haversine, Unit
from sklearn.metrics import classification_report

DEV_REGIONS = ["Calabria", "Campania", "Emilia Romagna", "Friuli-Venezia Giulia", "Lazio", "Liguria", "Lombardia", "Piemonte", "Puglia", "Sardegna", "Sicilia", "Toscana", "Veneto"]


def evaluate(subtask, gold_filepath, pred_filepath):
    """
    A function that evaluates predictions against the gold standard.

    Params
    ------
    subtask: str
        The subtask the submission refers to. Choices: ['a', 'b']
    gold_filepath: str
        Path to the gold standard for the subtask.
    pred_filepath: str
        Path to the file that contains predictions for the subtask, with the same format as 'gold_filepath'.
    """

    # Case subtask "a"
    if subtask == "a":
        preds = []
        golds = []

        with open(gold_filepath) as f_gold, open(pred_filepath) as f_pred:
            is_first_line = True
            for line_gold, line_pred in zip(f_gold, f_pred):
                if is_first_line == True:
                    is_first_line = False
                else:
                    golds.append(line_gold.rstrip("\n").split("\t")[2])
                    preds.append(line_pred.rstrip("\n").split("\t")[2])

        print(classification_report(golds, preds, labels=DEV_REGIONS))

    # Case subtask "b"
    elif subtask == "b":
        distances = []

        with open(gold_filepath) as f_gold, open(pred_filepath) as f_pred:
            is_first_line = True
            for line_gold, line_pred in zip(f_gold, f_pred):
                if is_first_line == True:
                    is_first_line = False
                else:
                    gold_parts = line_gold.rstrip("\n").split("\t")
                    pred_parts = line_pred.rstrip("\n").split("\t")
                    gold_lat, gold_lon = float(gold_parts[2]), float(gold_parts[3])
                    pred_lat, pred_lon = float(pred_parts[2]), float(pred_parts[3])
                    distance = haversine((pred_lat, pred_lon), (gold_lat, gold_lon), unit=Unit.KILOMETERS)
                    distances.append(distance)

        avg_distance = sum(distances) / len(distances)
        print(f"Avg distance: {avg_distance} km")

    # Case subtask does not exist
    else:
        sys.exit(f"ERROR. Subtask {subtask} does not exist.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-S", "--subtask", type=str, required=True, choices=["a", "b"], 
        help="The subtask the submission refers to. Choices: ['a', 'b'].")
    parser.add_argument("-G", "--gold_filepath", type=str, required=True,
        help="Path to the gold standard for the subtask.")
    parser.add_argument("-P", "--pred_filepath", type=str, required=True,
        help="Path to the file that contains predictions for the subtask.")
    args = parser.parse_args()
    
    evaluate(args.subtask, args.gold_filepath, args.pred_filepath)