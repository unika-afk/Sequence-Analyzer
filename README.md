# BICP 201 Mini Project

**Team Name:** USB

**Team Members:**
- Unika DC
- Sandhya Gautam

---
<center><img src="files/logo.jpg" width=250></center>

## DNA Sequence Analyzer

A Python-based application for analyzing DNA sequences with various computational features including nucleotide counting, GC content calculation, motif searching, and visualization.

---

## Data Structures Used

### 1. **List**
- Stores all DNA sequences (`dna_sequences`)
- Used for creating sequences of lengths and sequence numbers

### 2. **Stack**
- Implements Last-In-First-Out (LIFO) principle
- Used in `reverse_sequence_stack()` to reverse DNA sequences
- Operations: `append()` for push, `pop()` for pop

### 3. **Queue**
- Implements First-In-First-Out (FIFO) principle
- Used in `process_sequences_queue()` to process sequences in order
- Operations: `append()` for enqueue, `pop(0)` for dequeue

### 4. **Dictionary**
- Stores nucleotide counts with base as key and count as value
- Used in `count_nucleotides()` function

---

## Features

1. **Add DNA Sequences** - Input and validate DNA sequences (A, T, G, C only)
2. **Display Sequences** - View all stored sequences with their lengths
3. **Sequence Analysis**
   - Count individual nucleotides (A, T, G, C)
   - Calculate GC content percentage
   - Search for motifs within sequences
   - Reverse sequences using stack
   - Visualize nucleotide frequency with bar graphs
4. **Sort Sequences** - Sort all sequences by length
5. **Length Visualization** - Compare sequence lengths using bar graphs
6. **Queue Processing** - Process sequences in FIFO order
7. **Interactive Menu** - User-friendly command-line interface

---

## Installation

### Prerequisites
- Python 3.x
- matplotlib library

### Steps

1. Install Python from [python.org](https://www.python.org/downloads/)

2. Install required library:
```bash
pip install matplotlib
```

3. Download the `main.py` file

---

## Usage

### Running the Program

```bash
python3 main.py
```

### Menu Options

```
==== DNA Sequence Analyzer ====
1. Add DNA Sequence
2. Display All Sequences
3. Analyze a Sequence
4. Sort Sequences by Length
5. Show Length Graph
6. Process Sequences (Queue)
7. Exit
```

### Example Workflow

1. **Add sequences:**
   - Select option 1
   - Enter DNA sequence (e.g., `ATGCATGC`)

2. **Analyze a sequence:**
   - Select option 3
   - Choose sequence number
   - View nucleotide count, GC content
   - Search for motifs
   - See reversed sequence
   - View frequency graph

3. **Visualize data:**
   - Select option 5 to compare sequence lengths

4. **Process sequences:**
   - Select option 6 to process in FIFO order

---

## Sample Input/Output

```
Enter a sequence (A/T/G/C only): ATGCGTACG
Sequence added!

Nucleotide Count: {'A': 2, 'T': 2, 'G': 3, 'C': 2}
GC Content: 55.56%
Motif positions: [2, 5]
Reversed Sequence (Stack): GCATGCGTA
```

---

## Project Structure

```
dna-sequence-analyzer/
│
├── main.py    # Main program file
└── README.md          # Project documentation
```

---

## Contributing Team Members

This project was developed as part of BICP 201 coursework by Team USB.

---

## License

Educational project for BICP 201 course.
