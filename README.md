# HTR using CRNN and CTC

This is a **handwritten text recognition (HTR) pipeline** that operates on **scanned pages and PDFs** and applies the following:
* Detect words
* Read words

## Usage
### Run demo

* Additionally install matplotlib for plotting: `pip install matplotlib`
* Go to `scripts/`
* Run `python demo.py`
* The output should look like the plot shown above

### Run web demo (gradio)

* Additionally install gradio: `pip install gradio`
* Go to the root directory of the repository
* Run `python scripts/pdf_gradio_demo.py`
* Open the URL shown in the output, it changes for each iteration.
  
### Final Words: How to Append PDFs
Install the following:
pip install PyPDF2 pdf2image pillow
Also install `Poppler` separately
