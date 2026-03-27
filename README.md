# Classical CV Product Degmentation

Comparative study of classical computer vision methods for product instance segmentation

## Overview

This project evaluates four classical segmentation methods (grabcut, k-means, watershed) on product images from the dis5k dataset. The goal is to compare classical approaches without deep learning and analyze their strengths and limitations.

## Project Structure
```
classical-cv-product-segmentation/
├── notebooks/
│   ├── 01_dataset_preparation_preprocessing.ipynb
│   ├── 02_grabcut_segmentation.ipynb
│   ├── 02_kmeans_segmentation.ipynb
│   ├── 02_watershed_segmentation.ipynb
│   └── 03_refinement_evaluation_analysis.ipynb
├── project_data/
│   ├── preprocessed/
│   │   ├── images/              # 80 preprocessed images (512x512)
│   │   └── masks/               # 80 ground truth masks
│   ├── selected_images.csv
│   └── dataset_statistics.csv
├── results/
│   ├── grabcut/
│   ├── kmeans/
│   ├── watershed/
│   └── comparison/
├── preprocessing.py
├── requirements.txt
└── README.md
```

## Methods

- **Grabcut**: Interactive graph-cut based segmentation
- **K-means**: Color-based clustering segmentation
- **Watershed**: Marker-based segmentation for separating objects

## Dataset

DIS5k test set (80 images selected)
- 20 images from dis-te1 (simple shapes)
- 20 images from dis-te2 (moderate complexity)
- 20 images from dis-te3 (complex shapes)
- 20 images from dis-te4 (very complex shapes)

## Evaluation Metrics

- Intersection over union (iou)
- F1-score (dice coefficient)

## Setup
```bash
pip install -r requirements.txt
```

## Usage
```python
from preprocessing import load_image_pair, preprocess_image

# load preprocessed image
img, mask = load_image_pair('project_data/preprocessed/images/example.jpg',
                             'project_data/preprocessed/masks/example.png')

# run segmentation method
# (see individual notebooks for implementation)
```

## Authors

- Chien-Wei Weng
- Aris Fevre
- Henri Boisson

Centralesupelec, 2026

## References

- Rother, C., Kolmogorov, V., & Blake, A. (2004). “GrabCut”: Interactive foreground extraction
using iterated graph cuts. ACM SIGGRAPH 2004, 309–314.
- Qin, X., Dai, H., Hu, X., Fan, D. P., Shao, L., & Van Gool, L. (2022). Highly accurate dichoto
mous image segmentation. European Conference on Computer Vision (ECCV), 38–56.
- Felzenszwalb, P. F., & Huttenlocher, D. P. (2004). Efficient graph-based image segmentation.
International Journal of Computer Vision, 59(2), 167–181.
- Yu, Y., Wang, C., Fu, Q., Kou, R., Huang, F., Yang, B., Yang, T., & Gao, M. (2023). Techniques
and challenges of image segmentation: A review. Electronics, 12(5), 1199
