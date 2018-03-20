# A collection of (meta)genomics/(meta)transcriptomics-related scripts

A collection of scripts grouped by topic (in alphabetical order).

See below for the format of this readme.

## README Format

### name_of_script
*Description of script*
* **Input:** type/name of input files
* **Output:** type/name of output files
* **Usage:** command to run script
* **Additional details:** additional details relevant to running script
* *Changelog for relevant changes/update to script*

## Positive Selection

### paml_parallel.py
*Multi-thread paml's codeml*
* **Input:** a directory of paml .ctl files
* **Output:** a subdirectory for each .ctl file you supply, containing results from paml codeml for that ctl file
* **Usage:** python paml_parallel.py <integer; number of threads to use>
* **Additional details:** run the script directly from your directory of .ctl files
* **2018-03-20**: initial commit




