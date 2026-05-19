# Data File Processor 🗂️

So I built this as part of my Data Science learning journey — it's a simple CLI tool that takes a messy CSV file and cleans it up for you. Nothing fancy, but it was a great exercise in putting together a real Python project from scratch.

---

## What does it do?

You give it a CSV file, tell it how to handle missing values, and it:
- Removes duplicate rows
- Handles missing values (your choice — drop them, fill with mean, or fill with mode)
- Prints a cleaning report so you can see exactly what changed
- Saves the cleaned file as `cleaned_output.csv`

---

## Project Structure

```
data_processor/
├── main.py        # entry point, wires everything together
├── cleaner.py     # where the actual cleaning happens
├── stats.py       # generates the summary report
├── utils.py       # validates the file before doing anything
├── sample.csv     # test data I used while building this
└── README.md
```

---

## Getting Started

Clone the repo and install the only dependency you need:

```bash
git clone https://github.com/akashrey09/data-file-processor.git
cd data-file-processor
pip install pandas
```

---

## How to Run It

```bash
python main.py --input sample.csv --fill-missing mean
```

That's it. Two arguments:
- `--input` → path to your CSV file
- `--fill-missing` → one of `drop`, `mean`, or `mode`

### A few examples

```bash
# Don't want missing rows at all? Just drop them
python main.py --input sample.csv --fill-missing drop

# Prefer filling gaps with the average value
python main.py --input sample.csv --fill-missing mean

# Or use the most common value in each column
python main.py --input sample.csv --fill-missing mode
```

---

## Sample Output

When you run it, you'll see something like this in your terminal:

```
===== DATA CLEANING REPORT =====
Original row count   : 10
Cleaned row count    : 7
Duplicates removed   : 2
Null values found    : 4
================================
Column Statistics:
         age       salary
count   7.00      7.00
mean    30.00     52285.71
min     22.00     38000.00
max     40.00     70000.00
================================
```

And a fresh `cleaned_output.csv` gets saved in the same folder.

---

## What I learned building this

- How to build a proper CLI with `argparse`
- Splitting code into separate files and keeping things modular
- Handling errors properly instead of just letting things crash
- Cleaning data with Pandas — `drop_duplicates()`, `fillna()`, `dropna()`
- The difference between raising an error vs just printing a message (took me a minute 😅)

---

## Things I want to add later

- Let the user choose the output filename with `--output`
- Support `.tsv` files too
- Save the cleaning report as a `.json` or `.txt` file
- Handle the edge case where someone passes in an empty CSV

---

## Built with

- Python 3
- Pandas
- argparse, os (both built-in)

---

*This project is part of my Data Science bootcamp roadmap. Still learning — feedback welcome!*
