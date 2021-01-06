# Readme

This repo contains code to convert Named entity recognition annotations in Brat standoff format to CoNLL format. This is a format usable by HuggingFace for training Bert based NER models.

## Usage

The code assumes that all the input files i.e., *.ann and corresponding *.txt files are located in a single directory input_directory. Run the code to print the output of all annotations to the output_file.

python format_convertor.py --input_directory={input_directory} --output_file={output_file}

To run tests you can use the below command


The sample input annotations are taken from the sample dataset used for the CheMU 2020 NER task [1]

## References

[1] He, Jiayuan, et al. "Overview of chemu 2020: Named entity recognition and event extraction of chemical reactions from patents." International Conference of the Cross-Language Evaluation Forum for European Languages. Springer, Cham, 2020.
