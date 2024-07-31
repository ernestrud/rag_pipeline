from setuptools import setup, find_packages

setup(
    name='rag_pipeline',
    version='0.1.0',
    description='A pipeline for RAG (Retrieval-Augmented Generation)',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    install_requires=[
        'openai',
        'numpy',  # Add other dependencies as needed
        # 'pandas',
        # 'scikit-learn',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',  # Specify your Python version requirement
)
