# SBOM

This README file provides instructions on how to run the SBOM code and explains its additional features.

## Running the Code

To run the code, the user needs to send the path to the directory as a command line argument. Here is an example:

```
$ python3 sbom.py /home/alice/code/repos/
```

The specified directory should contain one or more subdirectories, each of which must contain either a requirements.txt or a package.json file. If any subdirectory does not contain one of these two files, the program will display a message in the terminal indicating the directory that is missing the file.

## Additional Features

There are two additional features implemented in this code:

1. The CSV and JSON files will not be created if the main directory is empty. This prevents the creation of empty files.

2. The CSV and JSON files will not be created if any of the subdirectories do not contain a requirements.txt or package.json file. This ensures that the generated files only include relevant data.

Please ensure that the directory structure and files meet these requirements to achieve the desired functionality.
