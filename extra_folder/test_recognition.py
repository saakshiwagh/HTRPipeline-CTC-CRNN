import cv2
from htr_pipeline import read_page, DetectorConfig, LineClusteringConfig

# read image
img = cv2.imread('data/sample_1.png', cv2.IMREAD_GRAYSCALE)

# detect and read text
read_lines = read_page(img, 
                       DetectorConfig(scale=0.4, margin=5), 
                       line_clustering_config=LineClusteringConfig(min_words_per_line=2))

# output text
for read_line in read_lines:
    print(' '.join(read_word.text for read_word in read_line))