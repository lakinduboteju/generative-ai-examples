# Generative AI Examples

## How to run

``` bash
$ docker compose up -d
$ docker compose down
```

``` bash
$ docker exec -it generative-ai-examples bash
```

``` bash
$ poetry install
```

``` bash
$ poetry run python main.py
```

## Debug

``` bash
# Run following command and debug using Pythong Debugger in vscode
$ poetry run python -Xfrozen_modules=off -m debugpy --listen 0.0.0.0:5678 --wait-for-client main.py
```

## Example 1
### Organizing medical records

Example medical history record taken from : https://www.youtube.com/watch?v=BmQppGzk78A

#### Example medical history record
```
63 year old man with limited stage adenocarcinoma of the left lung.
He first experienced changes in his voice in June 2020, about 3 months prior to his initial visit.
Pt follow up with his primary care physician and was referred to see ENT.
Further workup by ENT involved the following. Chest A-P/PA on 08/21/2020 showed enlargement of the right hilum suspicious for a mass.
and right medial basilar opacity due to atelectasis or pneumonia.
CT thorax on 08/27/2020 showed enlargement of the left upper lobe suspicious for a mass and right medial basilar opacity due to atelectasis or pneumonia.
Chest 2 Views on 09/07/2020 showed wedge-shaped opacity in the right middle lobe likely due to atelectasis, superimposed postobstructive pneumonia not excluded,
and lung masses related to known neoplastic disease.
CT thorax/abdomen/pelvis on 09/08/2020 showed new right middle lobe atelectasis with ground glass pacification of the superior right lower lobe likely secondary to extrinsic compression of the right middle lobe bronchus with unchanged severe stenosis of the superior vena cava due to extrinsic compression, overall stable size of right superior mediastinal and right hilar masses with metastatic foci in the right upper lobe with index lesions as above with no new nodules or masses, and no CT evidence of metastatic disease in the abdomen or pelvis.
Echo on 01/01/2021 showed visually estimated ejection fraction of 75 %.
Pt began radiation treatment for right lung cancer in early September 2020. Pt received cycle 1 of cisplatin and etoposide on 1/22/2022. He received his fourth and last cycle of treatment of cisplatin & etoposide on 3/01/202. Completed prophylactic WBI January 2021.
Treated with steroid for possible radiation pneumonitis, having SOB; improved and off steroid. Continues surveillance.
Heart Failure, his EF is 75, Last echo on 2/1/2023 showed diastolic impairment and grade 1 diastolic HF
COPD he is a chornic smoker with 30 pack year of smoking, Last PFT was 1 year ago and showed obstructive pattern
```

#### Medical history organized by Claude 3.5 Sonnet
``` json
[
    {
        "date": "06/01/2020",
        "title": "Initial voice changes",
        "symptoms": [
            "Changes in voice"
        ],
        "diagnosis": "Patient first experienced changes in his voice"
    },
    {
        "date": "08/21/2020",
        "title": "Chest X-ray findings",
        "symptoms": [],
        "diagnosis": "Chest A-P/PA showed enlargement of the right hilum suspicious for a mass and right medial basilar opacity due to atelectasis or pneumonia"
    },
    {
        "date": "08/27/2020",
        "title": "CT thorax findings",
        "symptoms": [],
        "diagnosis": "CT thorax showed enlargement of the left upper lobe suspicious for a mass and right medial basilar opacity due to atelectasis or pneumonia"
    },
    {
        "date": "09/07/2020",
        "title": "Chest X-ray follow-up",
        "symptoms": [],
        "diagnosis": "Chest 2 Views showed wedge-shaped opacity in the right middle lobe likely due to atelectasis, superimposed postobstructive pneumonia not excluded, and lung masses related to known neoplastic disease"
    },
    {
        "date": "09/08/2020",
        "title": "CT thorax/abdomen/pelvis findings",
        "symptoms": [],
        "diagnosis": "CT thorax/abdomen/pelvis showed new right middle lobe atelectasis with ground glass pacification of the superior right lower lobe likely secondary to extrinsic compression of the right middle lobe bronchus with unchanged severe stenosis of the superior vena cava due to extrinsic compression, overall stable size of right superior mediastinal and right hilar masses with metastatic foci in the right upper lobe with index lesions as above with no new nodules or masses, and no CT evidence of metastatic disease in the abdomen or pelvis"
    },
    {
        "date": "01/01/2021",
        "title": "Echocardiogram results",
        "symptoms": [],
        "diagnosis": "Echo showed visually estimated ejection fraction of 75%"
    },
    {
        "date": "01/22/2022",
        "title": "Start of chemotherapy",
        "symptoms": [],
        "diagnosis": "Patient received cycle 1 of cisplatin and etoposide"
    },
    {
        "date": "03/01/2022",
        "title": "Completion of chemotherapy",
        "symptoms": [],
        "diagnosis": "Patient received fourth and last cycle of treatment of cisplatin & etoposide"
    },
    {
        "date": "02/01/2023",
        "title": "Follow-up echocardiogram",
        "symptoms": [],
        "diagnosis": "Echo showed diastolic impairment and grade 1 diastolic heart failure"
    }
]
```
