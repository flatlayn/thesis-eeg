# Thesis-EEG

EEG-based depression analysis using two public datasets: a precomputed-feature resting-state set (Depression-REST) and a raw 128-channel ERP set (MODMA).

## Notebooks

| Notebook | Purpose |
| :--- | :--- |
| `Depression_Rest_Dataset.ipynb` | Exploration of Depression-REST: clinical metadata (BDI, HamD, TAI), feature-matrix inspection, topomaps, t-SNE comparison, and a comparison/alignment plan against MODMA. |
| `modma3.ipynb` | MODMA3 pipeline: preprocess raw EEG (0.5-40 Hz band-pass, resample to 128 Hz, 1 s epochs), subject-level train/test split, CNN with channel attention (MDD vs healthy control), epoch- and subject-level metrics, confusion matrix, ROC. |
| `number_cells.py` | Prefixes each notebook cell with its number. Safe to re-run after reordering. Usage: `python number_cells.py <notebook.ipynb>` |

## Data layout

Datasets are read from local folders next to the notebooks. The paths are set in one cell near the top of each notebook.

| Folder | Variable | Source |
| :--- | :--- | :--- |
| `Depression-Rest/` | `tocodeforsoul_depression_rest_preprocessed_path` | Kaggle `tocodeforsoul/depression-rest-preprocessed` |
| `Depression Rest - metadata/` | `depression_rest_metadata_path` | Google Drive folder "Depression Rest" (`Data_4_Import_REST.xlsx`, `Matlab Files/`, `Task Files/`) |
| `MODMA3/` | `manavrajpurohit_modma_dataset_path` | Kaggle `manavrajpurohit/modma-dataset` |
| `results/` | | Output folder |

### Download links

| Folder | Link |
| :--- | :--- |
| `Depression-Rest/` | https://www.kaggle.com/datasets/tocodeforsoul/depression-rest-preprocessed/data |
| `Depression Rest - metadata/` | https://unmm-my.sharepoint.com/personal/jcavanagh_unm_edu/_layouts/15/onedrive.aspx?id=%2Fpersonal%2Fjcavanagh%5Funm%5Fedu%2FDocuments%2FDepression%20Rest&ga=1 |
| `MODMA3/` | https://www.kaggle.com/datasets/manavrajpurohit/modma-dataset |

### Depression-REST
- Files: `<subject>_Depression_REST-epo-feat-v1.npy` / `-v2.npy`.
- Each file holds 12 blocks of shape `(epochs, 62 channels, 31 features)`.
- Metadata columns: `id, MDD, MDD_note, HamD, sex, age, BDI, BDI_Anh, BDI_Mel, TAI` (122 subjects).

### MODMA3
- Raw EGI `.raw` files under `EEG_128channels_ERP_lanzhou_2015/` plus clinical labels in `ERP_MDD_HC_data.csv`.

## Setup

```bash
pip install -r requirements.txt
jupyter notebook
```

Place the three data folders in the repository root (they are large and are not meant to be committed).
