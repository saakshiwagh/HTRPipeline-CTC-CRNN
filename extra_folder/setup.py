from setuptools import setup, find_namespace_packages

setup(
    name='htr-pipeline',
    version='1.2.0',
    description='Handwritten text recognition pipeline.',
    packages=find_namespace_packages(include=['htr_pipeline', 'htr_pipeline.*']),
    install_requires=['numpy',
                      'onnxruntime',
                      'opencv-python',
                      'scikit-learn',
                      'python-Levenshtein',
                      'path'
                      'pillow',
                      'gradio'
                      'matplotlib'
                      'poppler'],
    python_requires='>=3.8',
    package_data={'htr_pipeline.models': ['*']}
)
