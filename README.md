# :earth_africa: GeoLingIt shared task

This repository contains useful materials related to the [GeoLingIt shared task](https://sites.google.com/view/geolingit) at [EVALITA 2023](https://www.evalita.it/campaigns/evalita-2023/). You can find more information about how to participate, how data looks like, and which subtasks and tracks are available on the [shared task website](https://sites.google.com/view/geolingit).

- :page_with_curl: **[Get the data](#page_with_curl-get-the-data)**
- :triangular_ruler: **[Data format](#triangular_ruler-data-format)**
- :rocket: **[Submission requirements](#rocket-submission-requirements)**
- :bar_chart: **[Evaluation and scorer](#bar_chart-evaluation-and-scorer)**
- :pushpin: **[Baselines](#pushpin-baselines)**
- :alarm_clock: **[Important dates](#alarm_clock-important-dates)**


### :page_with_curl: Get the data

If you are interested in participating in the GeoLingIt shared task, please fill out the [**expression of interest form**](https://forms.gle/TW2NveAZMZodF7Z59) by EVALITA organizers (by Apr 30th, 2023) indicating **"GeoLingIt – Geolocation of Linguistic Variation in Italy"** as preference. We will send to you the link to join the dedicated Google Group, from where you can obtain the development data. There you can keep in touch with us and ask any shared task-related questions.

### :triangular_ruler: Data format

The dataset is in a tab-separated format, with an example per line and the first line as header. We provide `train_a.tsv` and `dev_a.tsv` for **Subtask A**, and `train_b.tsv` and `dev_b.tsv` for **Subtask B**. Test data for both subtasks (`test.tsv`) will be available during the evaluation window (i.e., May 7th-14th, 2023). Depending on the subtask, the column(s) in train/dev files containing gold label(s) differ(s) as follow.

***Note**: The format is exactly the same for both the standard track and the special track, as the latter is a subset of the former, restricted to an area chosen by participants ([details on tracks here](https://sites.google.com/view/geolingit/task-description)).*

#### Subtask A

Each example in `train_a.tsv` and `dev_a.tsv` has three columns:
- **id**: the tweet identifier, that we programmatically change to preserve user's anonymity;
- **text**: the text of the tweet, with masked user mentions, email addresses, URLs, and locations from cross-posting;
- **region** (*gold label*): the region of Italy in a string format.

**Note**: `test.tsv` follows the same format above but with no gold label column (to be predicted).

#### Subtask B

Each example in `train_b.tsv` and `dev_b.tsv` has four columns:
- **id**: the tweet identifier, that we programmatically change to preserve user's anonymity;
- **text**: the text of the tweet, with masked user mentions, email addresses, URLs, and locations from cross-posting;
- **latitude** (*gold label 1*): a float representing the latitude coordinate of the tweet;
- **longitude** (*gold label 2*): a float representing the longitude coordinate of the tweet.

**Note**: `test.tsv` follows the same format above but with no gold label columns (to be predicted).

### :rocket: Submission requirements

Test data to be used for either one or both subtasks (`test.tsv`) will be made available on **May 7th, 2023** and participants can submit their predictions during the evaluation window (i.e., **May 7th-14th, 2023**). Results will be communicated to participants by May 30th, 2023 along with the 1<=k<=7 additional regions included in test data and unknown during development.

We allow participants to submit **up to 3 runs for each track and subtask** (i.e., a team participating in both tracks and in all subtasks will be able to submit up to a total of 12 runs, of which up to 3 for each subtask). Different runs can reflect e.g., different solutions or different configurations of the same system.

***Note**: Participants are allowed to use external resources in addition to (or in place of) the data provided by the organizers to train their models, e.g., pre-trained models, dictionaries and lexicons, existing datasets, and newly annotated data. **The only external source that is not allowed is Twitter, since some tweets can be part of our test set**. Subtask A gold labels cannot be used as features for Subtask B, and viceversa.*

#### Submission format

Prediction files must be formatted **the same way as training and development data** (i.e., practically, just by filling the missing gold label column(s) on the test data file). 

***Note**: For the special track, we require participants to send predictions for all instances on the `test.tsv` file as for teams participating to the standard track, regardless of the set of regions chosen. Then, we will consider only test instances that actually belong to the selected regions for the formal evaluation on the special track. This is to avoid to indirectly let standard track participants know to which regions some of the test instances belong during the evaluation window, and thus avoid potential cheating.*

##### Subtask A

A tab-separated file with an example per line and the first line as header. Only the **third column** (`region`) will be used for evaluation (you can just leave the `text` empty to be sure to avoid formatting issues).

```
id	text	region
1	In...	Lombardia
2	Ma...	Campania
...	...	...
```

##### Subtask B

A tab-separated file with an example per line and the first line as header. Only the **third and fourth columns** (`latitude` and `longitude`) will be used for evaluation (you can just leave the `text` empty to be sure to avoid formatting issues).

```
id	text	latitude	longitude
1	In...	45.4613453	9.15933655
2	Ma...	40.8541123	14.24345155
...	...	...	...
```

#### How to submit your runs

**[1]** Name your submission file(s) following the naming convention **`TEAM.TRACK.SUBTASK.RUN`**, where:
- **TEAM**: the name of your team;
- **TRACK**: the name of the track, i.e., either `standard` or `special`. In the latter case, please also attach the 3-letter initials for regions included in your special track participation (e.g., *special-sic-cal-pug*);
- **SUBTASK**: the identifier of the subtask, i.e., either `a` or `b`;
- **RUN**: an incremental identifier starting from 1 denoting your track-subtask run (e.g., `1`, `2`, or `3`).

*For instance, if you are participating in the standard track for both the subtasks and send a run for each for your team named "Pippo", your run names would be "Pippo.standard.a.1" and "Pippo.standard.b.1"*.

**[2]** Compress all your run files as a ZIP file named `TEAM.zip` (where TEAM is the name of your team).

**[3]** Send an email to geolingit@gmail.com with subject **GeoLingIt: TEAM submission** attaching `TEAM.zip`.

### :bar_chart: Evaluation and scorer

Predictions will be evaluated according to **macro F1 score** (Subtask A, *the higher, the better*) and **mean distance in km** (Subtask B, *the lower, the better*). We provide participants with a scorer (i.e., `eval.py`). The usage is the following:

```
python eval.py -S $SUBTASK -G $GOLD_FILEPATH -P $PRED_FILEPATH
```
- `$SUBTASK`: The subtask the run refers to. Choices: ['`a`', '`b`'].
- `$GOLD_FILEPATH`: Path to the gold standard for the subtask.
- `$PRED_FILEPATH`: Path to the file that contains predictions for the subtask, with the same format as `$GOLD_FILEPATH`.

#### Requirements

You may need to install two python packages to run the script: `scikit-learn==1.2.1` and `haversine==2.8.0`.

### :pushpin: Baselines

We consider the following baselines to allow participants to assess their results during development.

#### Subtask A

- **Most frequent baseline (MFB)**: this baseline always guesses the most frequent region in the training set (i.e., Lazio) for all validation instances. The macro F1 score on `dev_a.tsv` is: **0.0265**.
- **Logistic regression (LR)**: a traditional machine learning classifier that employs default scikit-learn hyperparameters. The macro F1 score on `dev_a.tsv` is: **0.5872**.

| Baseline name          | Precision | Recall | Macro F1 |
|------------------------|-----------|--------|----------|
| Most frequent baseline | 0.0160    | 0.0769 | 0.0265   |
| Logistic regression    | 0.7686    | 0.5389 | 0.5872   |

#### Subtask B

- **Centroid baseline (CB)**: this baseline computes the center point (latitude, longitude) from the training set and predicts it for all test instances. The mean distance in km on `dev_a.tsv` is: **301.65**.
- ***k*-nearest neighbors (*k*NN)**: a traditional machine learning regression model that employs default scikit-learn hyperparameters. The mean distance in km on `dev_a.tsv` is: **281.03**.

| Baseline name       | Avg dist (km) |
|---------------------|---------------|
| Centroid baseline   | 301.65 km     |
| k-nearest neighbors | 281.03 km     |

### :alarm_clock: Important dates

- ~~**Feb 7th, 2023**: The data (train and dev) and the evaluation scorer are provided to participants~~
- **May 7th-14th, 2023**: Evaluation window: participants submit predictions on the provided test data
- **Jun 14th, 2023**: Submission of system description papers due
- **Jul 10th, 2023**: Notification of papers' acceptance to participants
- **Jul 25th, 2023**: Camera-ready papers due
- **Sep 7th-8th, 2023**: EVALITA 2023 Workshop in Parma, Italy
