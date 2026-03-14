## Text Processing Pipeline

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

The output files included in this repository were generated using the full Reddit text dataset (`reddit_text.txt`), which is available in the Google Drive link above.

The code is configured to use the sample file so that the repository remains lightweight and reproducible.

This means:

* outputs represent processing performed on the full dataset
* sample file is included only so the code can run directly from GitHub

---

## Extra Work Done Beyond Class Example

Compared to the class example, this lab additionally includes:

* use of Reddit social media data instead of book text
* CSV preprocessing before text analysis
* bigram generation in addition to word count
* stopword filtering
* handling of large external dataset through Google Drive

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
