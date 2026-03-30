# Classical Computer Vision Methods for Product Instance Segmentation

Comparative study of classical segmentation methods (GrabCut, K-means, Watershed) for product instance segmentation. Evaluates performance across complexity levels using IoU and F1-score metrics on the DIS5K dataset.

**Dataset:** [DIS5K](https://github.com/xuebinqin/DIS) (80 images stratified by complexity)

---

## Results

### Comparative Summary

| Method | Mean IoU | Mean F1 | Avg Time/Image |
|--------|----------|---------|----------------|
| **GrabCut** | **0.2686 ± 0.2112** | **0.3828 ± 0.2507** | 9.08s |
| K-means | 0.2224 ± 0.1911 | 0.3286 ± 0.2309 | 0.19s |
| Watershed | 0.1131 ± 0.1714 | 0.1696 ± 0.2241 | 0.01s |

### GrabCut

**Performance by Complexity:**
| Level | Mean IoU | Mean F1 | Description |
|-------|----------|---------|-------------|
| TE1 | 0.1864 | 0.2644 | Simple objects |
| TE2 | 0.2320 | 0.3562 | Medium complexity |
| TE3 | 0.3454 | 0.4709 | Complex objects |
| TE4 | 0.3105 | 0.4399 | Very complex |

**Configuration:** Rectangle initialization (10% margin), 10 iterations, no refinement  
**Strengths:** Solid objects with clear boundaries (best: harp 83% IoU, caterpillar 81% IoU)  
**Weaknesses:** Thin structures (rope, crack, wire frames → 0% IoU)

### K-means

**Performance by Complexity:**
| Level | Mean IoU | Mean F1 | Description |
|-------|----------|---------|-------------|
| TE1 | 0.1694 | 0.2605 | Simple objects |
| TE2 | 0.1904 | 0.3002 | Medium complexity |
| TE3 | 0.2384 | 0.3412 | Complex objects |
| TE4 | 0.2912 | 0.4125 | Very complex |

**Configuration:** K=2 clusters, Lab color space, border heuristic for foreground selection  
**Strengths:** Fast processing, works well on high-contrast scenes (best: gym equipment 76% IoU, handcraft 73% IoU)  
**Weaknesses:** No spatial coherence — noisy masks on textured backgrounds, fails on thin objects with similar colors to background

### Watershed

**Performance by Complexity:**
| Level | Mean IoU | Mean F1 | Description |
|-------|----------|---------|-------------|
| TE1 | 0.1405 | 0.2092 | Simple objects |
| TE2 | 0.1160 | 0.1746 | Medium complexity |
| TE3 | 0.0954 | 0.1429 | Complex objects |
| TE4 | 0.1007 | 0.1519 | Very complex |

**Configuration:** Otsu thresholding, distance transform (threshold 0.5), kernel size 3  
**Strengths:** Clean boundaries on high-contrast objects (best: easel 74% IoU, crack 72% IoU)  
**Weaknesses:** Otsu threshold fails on complex backgrounds, severe under-segmentation on most images

---

## Project Structure
```
classical-cv-product-segmentation/
├── notebooks/
│   ├── 01_dataset_preparation_preprocessing.ipynb  # Dataset sampling, preprocessing
│   ├── 02_grabcut_segmentation.ipynb               # GrabCut implementation
│   ├── 02_kmeans_segmentation.ipynb                # K-means implementation
│   ├── 02_watershed_segmentation.ipynb             # Watershed implementation
│   ├── 03_refinement_evaluation_analysis.ipynb     # Evaluation pipeline (all methods)
│   └── preprocessing.py                            # Preprocessing module
├── project_data/
│   ├── preprocessed/
│   │   ├── images/                                 # 80 images (512×512, not tracked)
│   │   ├── masks/                                  # 80 masks (512×512, not tracked)
│   │   └── preprocessing_metadata.json
│   ├── selected_images.csv                         # Stratified sampling manifest
│   └── dataset_statistics.csv                      # Complexity distribution
├── results/
│   ├── grabcut/
│   ├── kmeans/
│   └── watershed/
├── requirements.txt
├── .gitignore
├── README.md
└── report.pdf                                      # Full technical report

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

# 2. Segmentation (any order)
jupyter notebook notebooks/02_grabcut_segmentation.ipynb
jupyter notebook notebooks/02_kmeans_segmentation.ipynb
jupyter notebook notebooks/02_watershed_segmentation.ipynb

# 3. Evaluation (run for each method)
jupyter notebook notebooks/03_refinement_evaluation_analysis.ipynb
```

</details>

---

## Methodology

**Dataset:**
- 80 images from DIS5K (stratified sampling, seed 42)
- 4 complexity levels (TE1-TE4), 20 images each
- Preprocessing: 512×512 resize, no denoising

**Methods:**
1. **GrabCut** — Graph-cut iterative segmentation with GMM color models
2. **K-means** — Color clustering in Lab space with border-based foreground selection
3. **Watershed** — Marker-based segmentation via Otsu thresholding and distance transform

**Evaluation:**
- Metrics: IoU (primary), F1-score (secondary)
- Per-image and per-complexity analysis
- Best/worst case identification

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

## Authors

Chien-Wei Weng | Aris Fèvre | Henri Boisson  
MSc Data Sciences and Business Analytics  
CentraleSupélec × ESSEC Business School

**Academic Project | Computer Vision (Spring 2026)**
