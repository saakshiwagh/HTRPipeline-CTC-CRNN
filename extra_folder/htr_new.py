import json
import cv2
import matplotlib.pyplot as plt
from path import Path
from scripts.pdf_demo_not_working import PDFProcessor
from htr_pipeline import read_page, DetectorConfig, LineClusteringConfig, ReaderConfig, PrefixTree

def setup_htr_pipeline():
    """Setup HTR pipeline with configuration"""
    with open('../data/config.json') as f:
        sample_config = json.load(f)
    
    with open('../data/words_alpha.txt') as f:
        word_list = [w.strip().upper() for w in f.readlines()]
    prefix_tree = PrefixTree(word_list)
    
    return sample_config, prefix_tree

def create_htr_callback(decoder='best_path', prefix_tree=None):
    """Create HTR processing function"""
    def htr_processor(image, page_num):
        # Use default or image-specific config
        scale = 0.4  # Default scale
        margin = 5   # Default margin
        
        read_lines = read_page(
            image,
            detector_config=DetectorConfig(scale=scale, margin=margin),
            line_clustering_config=LineClusteringConfig(min_words_per_line=2),
            reader_config=ReaderConfig(decoder=decoder, prefix_tree=prefix_tree)
        )
        
        # Extract text
        page_text = ""
        for read_line in read_lines:
            page_text += ' '.join(read_word.text for read_word in read_line) + "\n"
        
        return page_text.strip()
    
    return htr_processor

def main():
    # Setup HTR pipeline
    sample_config, prefix_tree = setup_htr_pipeline()
    
    # Initialize PDF processor
    pdf_processor = PDFProcessor(dpi=200)
    
    # Create HTR processing function
    htr_callback = create_htr_callback('best_path', prefix_tree)
    
    # Process PDF file
    pdf_path = 'your_document.pdf'  # Change to your PDF path
    output_dir = 'output_images'    # Optional: directory to save split images
    
    try:
        results = pdf_processor.process_pdf(pdf_path, htr_callback, output_dir)
        
        # Print results
        print("\n" + "="*60)
        print("PDF PROCESSING RESULTS:")
        print("="*60)
        
        for result in results:
            print(f"--- Page {result['page']} ---")
            print(result['text'])
            print()
            
    except Exception as e:
        print(f"Error processing PDF: {e}")

if __name__ == "__main__":
    main()