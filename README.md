# Classical Computer Vision Methods for Product Instance Segmentation

Comparative study of classical segmentation methods (GrabCut, K-means, Watershed) for product instance segmentation. Evaluates performance across complexity levels using IoU and F1-score metrics on the DIS5K dataset.

**Dataset:** [DIS5K](https://github.com/xuebinqin/DIS) (80 images stratified by complexity)

---

## Current Results

### GrabCut (Implemented)

**Overall Performance:**
- Mean IoU: **0.2686** (±0.2112)
- Mean F1: **0.3828** (±0.2507)

**Performance by Complexity:**
| Level | Mean IoU | Mean F1 | Description |
|-------|----------|---------|-------------|
| TE1 | 0.1864 | 0.2644 | Simple objects |
| TE2 | 0.2320 | 0.3562 | Medium complexity |
| TE3 | 0.3454 | 0.4709 | Complex objects |
| TE4 | 0.3105 | 0.4399 | Very complex |

**Configuration:**
- Initialization: Rectangle (10% margin)
- Iterations: 10
- No refinement (experiment showed -0.37% IoU impact)

**Strengths:** Solid objects, clear boundaries (best: harp 83% IoU, caterpillar 81% IoU)  
**Weaknesses:** Thin structures (rope, crack, wire frames → 0% IoU)

### K-means (Pending)

Results pending teammate implementation.

### Watershed (Pending)

Results pending teammate implementation.

---

## Project Structure
```
classical-cv-product-segmentation/
├── notebooks/
│   ├── 01_dataset_preparation_preprocessing.ipynb  # Dataset sampling, preprocessing
│   ├── 02_grabcut_segmentation.ipynb               # GrabCut implementation
│   ├── 02_kmeans_segmentation.ipynb                # K-means implementation (pending)
│   ├── 02_watershed_segmentation.ipynb             # Watershed implementation (pending)
│   └── 03_refinement_evaluation_analysis.ipynb     # Evaluation pipeline (all methods)
├── project_data/
│   ├── preprocessed/
│   │   ├── images/                # 80 images (512×512, not tracked)
│   │   ├── masks/                 # 80 masks (512×512, not tracked)
│   │   └── preprocessing_metadata.json
│   ├── selected_images.csv        # Stratified sampling manifest
│   └── dataset_statistics.csv     # Complexity distribution
├── results/
│   ├── preprocessing/
│   │   ├── dataset_distribution.png
│   │   ├── dataset_statistics.png
│   │   └── preprocessed_validation.png
│   ├── grabcut/
│   │   ├── DIS-*.png              # 80 segmentation masks (not tracked)
│   │   ├── grabcut_results.csv    # Processing log
│   │   ├── evaluation_results.csv # IoU/F1 per image
│   │   ├── evaluation_metadata.json
│   │   ├── grabcut_evaluation_summary.png
│   │   ├── initialization_comparison.png
│   │   ├── iteration_comparison_with_rect.png
│   │   ├── validation_52.png
│   │   ├── best_case_44.png
│   │   ├── best_case_46.png
│   │   ├── worst_case_10.png
│   │   └── worst_case_26.png
│   ├── kmeans/ (pending)
│   └── watershed/ (pending)
├── preprocessing.py               # Preprocessing module
├── requirements.txt
├── .gitignore
├── README.md
└── report.pdf (to be uploaded)
```

**Note:** Images and masks are not tracked in git (reproducible from dataset). Only metadata and key figures are committed.

---

## Quick Start

<details>
<summary><b>Setup and Execution — Click to expand</b></summary>

### Prerequisites
- Python 3.8+

### Setup

1. **Clone repository**
```bash
git clone https://github.com/wengchienwei/classical-cv-product-segmentation.git
cd classical-cv-product-segmentation
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Download DIS5K dataset**
- Download from [DIS GitHub](https://github.com/xuebinqin/DIS)
- Place in project root as `DIS5K/`

4. **Run notebooks sequentially**
```bash
# 1. Dataset preparation
jupyter notebook notebooks/01_dataset_preparation_preprocessing.ipynb

# 2. GrabCut segmentation
jupyter notebook notebooks/02_grabcut_segmentation.ipynb

# 3. Evaluation
jupyter notebook notebooks/03_refinement_evaluation_analysis.ipynb
```

**Expected Runtime:** ~15 minutes total (preprocessing 2min, GrabCut 12min, evaluation 1min)

### Reproducibility

All results are reproducible:
1. Dataset: Stratified sampling with fixed seed (42)
2. Preprocessing: Deterministic resize, saved metadata
3. GrabCut: Fixed parameters (10 iterations, rect init)
4. Evaluation: Consistent metrics across all methods

**To reproduce GrabCut results:**
```bash
# Run notebooks 01 → 02 → 03 (GrabCut section)
# Results will match: IoU 0.2686 ± 0.2112
```

</details>

---

## For Teammates (K-means / Watershed)

### Implementation Guide

1. **Use preprocessing module** (already done):
```python
from preprocessing import load_image_pair
img, gt_mask = load_image_pair(img_path, gt_path)
```

2. **Save results** to `../results/{method}/`:
```
../results/kmeans/DIS-TE1_*.png    # or watershed
../results/kmeans/kmeans_results.csv
```

3. **Run evaluation** in notebook 03:
```python
# Change config at top of notebook
METHOD_CONFIG = {
    'name': 'kmeans',              # or 'watershed'
    'results_dir': '../results/kmeans'
}
# Then run evaluation pipeline section
```

---

## Methodology

**Dataset:**
- 80 images from DIS5K (stratified sampling)
- 4 complexity levels (TE1-TE4), 20 images each
- Preprocessing: 512×512 resize, no denoising

**Methods:**
1. **GrabCut** - Graph-cut based iterative segmentation
2. **K-means** - Color-based clustering segmentation
3. **Watershed** - Gradient-based region growing

**Evaluation:**
- Metrics: IoU (primary), F1-score (secondary)
- Per-image and per-complexity analysis
- Best/worst case identification

**Pipeline Design:**
- Modular design (same notebook for all methods)
- Reproducible (fixed random seeds, saved configs)
- Independent implementation (minimal coordination needed)

---

## Tech Stack

**Core:** Python 3.8, OpenCV, NumPy  
**Evaluation:** IoU, F1-score  
**Visualization:** matplotlib, pandas

---

## Dataset Citation
```bibtex
@InProceedings{qin2022,
      author={Xuebin Qin and Hang Dai and Xiaobin Hu and Deng-Ping Fan and Ling Shao and Luc Van Gool},
      title={Highly Accurate Dichotomous Image Segmentation},
      booktitle={ECCV},
      year={2022}
}
```

---

## Project Timeline

- **Completed:** Dataset preparation, preprocessing, GrabCut implementation, evaluation pipeline
- **In Progress:** K-means (teammate 1), Watershed (teammate 2)
- **Next:** Comparative analysis, report writing

---

## Authors

Chien-Wei Weng | Aris Fèvre | Henri Boisson  
MSc Data Sciences and Business Analytics  
CentraleSupélec × ESSEC Business School

---

**Academic Project | Computer Vision (Spring 2026)**
