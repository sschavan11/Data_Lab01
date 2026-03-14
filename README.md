# Apache Beam Lab – Word Count and Bigram Analysis Using Reddit Dataset

## Objective

The objective of this lab is to implement an Apache Beam-style text processing workflow on Reddit comment data by extracting words, removing stopwords, counting word frequency, and generating bigram frequency outputs using Python on a large real-world dataset.

---

## Dataset Used

The dataset used for this lab is Reddit comment data extracted from a Reddit CSV file.

* Source file: `kaggle_RC_2019-05.csv`
* Extracted full text size: approximately **170 MB**
* Data used: Reddit comments from the `body` column

The CSV file was first processed to extract only the comment text, which generated:

* `reddit_text.txt`

Since the full extracted text file is too large for GitHub, it is stored externally.

Full dataset (170 MB): [Google Drive Link](https://drive.google.com/drive/folders/1AF6PVfsACeUZqalvd9n3aGbmzoNhwGZ3?usp=sharing)

A smaller file is included in the repository:

* `reddit_text_sample.txt`

The sample file is included so the code can run directly from GitHub.

---

## Lab Workflow

### 1. Extract Text from CSV

The original CSV contains multiple columns. Only the `body` column was extracted into plain text format.

Script used:

* `extract_body.py`

### 2. Create Sample File

A smaller sample file was created from the full text file for repository use.

Script used:

* `create_sample.py`

This generated:

* `reddit_text_sample.txt`

### 3. Text Processing Pipeline

The main script reads the sample Reddit text file and processes it step by step.

The input file is loaded from:

```python
input_file = os.path.join("Data", "reddit_text_sample.txt")
```

The output files are stored inside:

```python
output_folder = os.path.join("output")
```

The output folder is created automatically if it does not exist.

### Stopword Removal

A predefined stopword list removes common words such as:

* the
* and
* of
* is
* to

This keeps only meaningful words for counting.

### Word Extraction

Each line is processed using regular expressions:

```python
re.findall(r"[a-zA-Z']+", str(line).lower())
```

This extracts alphabetic words and converts all text to lowercase.

Words shorter than 3 characters are removed.

### Bigram Creation

After cleaning, adjacent word pairs are created.

Example:

```text
machine learning
data science
```

### Frequency Counting

The script uses:

```python
Counter()
```

to count:

* word frequency
* bigram frequency

Only words and bigrams appearing at least 5 times are kept.

### Output Formatting

The output is written in tuple format:

```text
('word', count)
('word1 word2', count)
```

The results are sorted in descending order of frequency.

---

## Outputs Generated

Two output files are generated.

### Word Frequency Output

* `output/wordcount.txt`

Contains word frequency counts.

### Bigram Frequency Output

* `output/bigramcount.txt`

Contains repeated two-word phrase counts.

---

## Important Dataset Note

The output files in this repository were generated using the full Reddit text dataset (`reddit_text.txt`).

The full extracted file is available through the Google Drive link above.

The code is set to use the sample file so the repository remains lightweight and easy to run.

This means:

* the outputs come from the full dataset
* the sample file is included for reference and execution

---

## Extra Work Done Beyond Class Example

Compared to the class example, this lab includes:

* Reddit data instead of book text
* CSV preprocessing before text analysis
* bigram generation in addition to word count
* stopword filtering
* handling of large external data through Google Drive

---

## Repository Structure

```text
Lab01-Data/
│
├── Data/
│   ├── reddit_text_sample.txt
│   ├── extract_body.py
│
├── output/
│   ├── wordcount.txt
│   ├── bigramcount.txt
│
├── src/
│   ├── create_sample.py
│   ├── main.py
│
├── requirements.txt
├── README.md
├── .gitignore
```

---

## Requirements

Install dependencies using:

```bash
pip install -r requirements.txt
```

---

## Run Instructions

Execute:

```bash
python src/main.py
```

Outputs will be generated inside:

```text
output/
```
