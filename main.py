import sys
from processor import process_file
from reporter import generate_report

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    warehouse = process_file(input_file)
    report = generate_report(warehouse)
    print(report)

if __name__ == "__main__":
    main()