# Simple data analysis script
# Dhanesh Sankar

def load_data(filepath):
    """Load data from a CSV file."""
    import csv
    with open(filepath, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def calculate_mean(values):
    """Calculate the mean of a list of numbers."""
    return sum(values) / len(values)

def main():
    print("Data analysis script ready.")
    print("Provide a CSV filepath to load_data() to begin.")

if __name__ == "__main__":
    main()
