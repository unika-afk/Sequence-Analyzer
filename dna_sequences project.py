import matplotlib.pyplot as plt
from collections import deque  # used for queue

dna_sequences = []  # list to store all dna sequences

# function to add a new dna sequence
def add_sequence():
    seq = input("Enter a sequence (A/T/G/C only): ").upper()
    # checking if sequence is valid
    if all(base in "ATGC" for base in seq):
        dna_sequences.append(seq)
        print("Sequence added!\n")
    else:
        print("Invalid DNA sequence!\n")

# show all stored sequences
def display_sequences():
    if not dna_sequences:
        print("No sequences stored.\n")
        return

    # enumerate gives numbering 1,2,3...
    for i, seq in enumerate(dna_sequences, 1):
        print(f"{i}. {seq} (Length: {len(seq)})")
    print()

# counting A, T, G, C using dictionary
def count_nucleotides(seq):
    count = {'A':0, 'T':0, 'G':0, 'C':0}
    for letter in seq:
        if letter in count:
            count[letter] += 1  # increasing count
    return count

# calculate GC percentage
def gc_content(seq):
    if len(seq) == 0:
        return 0
    return ((seq.count('G') + seq.count('C')) / len(seq)) * 100

# searching motif inside dna
def find_motif(seq, motif):
    positions = []
    for i in range(len(seq) - len(motif) + 1):
        if seq[i:i+len(motif)] == motif:
            positions.append(i)  # saving position
    return positions

# sorting sequences by length
def sort_sequences():
    dna_sequences.sort(key=len)
    print("Sequences sorted by length!\n")

# STACK example → reversing dna
def reverse_sequence_stack(seq):
    stack = []
    for base in seq:
        stack.append(base)

    reversed_seq = ""
    while stack:
        reversed_seq += stack.pop()  # LIFO
    return reversed_seq

# QUEUE example → processing sequences
def process_sequences_queue():
    if not dna_sequences:
        print("No sequences to process!\n")
        return

    queue = deque(dna_sequences)
    print("Processing sequences using Queue:")
    while queue:
        print("Processing:", queue.popleft())  # FIFO
    print()

# graph showing A T G C counts
def plot_nucleotide_graph(seq):
    count = count_nucleotides(seq)
    plt.bar(count.keys(), count.values())
    plt.title("Nucleotide Frequency")
    plt.xlabel("Nucleotides")
    plt.ylabel("Count")
    plt.show()

# graph comparing lengths of sequences
def plot_length_graph():
    if not dna_sequences:
        print("No sequences to plot!\n")
        return

    lengths = [len(seq) for seq in dna_sequences]
    numbers = list(range(1, len(dna_sequences)+1))

    plt.bar(numbers, lengths)
    plt.title("DNA Sequence Lengths")
    plt.xlabel("Sequence Number")
    plt.ylabel("Length")
    plt.show()

# main menu part
def main():
    while True:
        print("\n==== DNA Sequence Analyzer ====")
        print("1. Add DNA Sequence")
        print("2. Display All Sequences")
        print("3. Analyze a Sequence")
        print("4. Sort Sequences by Length")
        print("5. Show Length Graph")
        print("6. Process Sequences (Queue)")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_sequence()

        elif choice == '2':
            display_sequences()

        elif choice == '3':
            if not dna_sequences:
                print("No sequence available!\n")
                continue

            display_sequences()
            idx = int(input("Select the sequence number: ")) - 1

            if 0 <= idx < len(dna_sequences):
                seq = dna_sequences[idx]

                print("Nucleotide Count:", count_nucleotides(seq))
                print("GC Content: {:.2f}%".format(gc_content(seq)))

                motif = input("Enter motif to search: ").upper()
                print("Motif positions:", find_motif(seq, motif))

                print("Reversed Sequence (Stack):", reverse_sequence_stack(seq))

                plot_nucleotide_graph(seq)
            else:
                print("Invalid number!\n")

        elif choice == '4':
            sort_sequences()

        elif choice == '5':
            plot_length_graph()

        elif choice == '6':
            process_sequences_queue()

        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice!\n")

# starting point of program
if __name__ == "__main__":
    main()

