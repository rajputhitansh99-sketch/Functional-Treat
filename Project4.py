global_summary = ""

def input_data():
    global global_summary
    print("1. 1D Array")
    print("2. 2D Array")
    choice = input("Enter your choice: ")
    
    if choice == '1':
        user_input = input("Enter data for a 1D array (separated by spaces): ")
        data = []
        for x in user_input.split():
            data.append(int(x))
            
        total = 0
        for x in data:
            total += x
            
        mean_val = total / len(data) if len(data) > 0 else 0
        global_summary = "Total elements: " + str(len(data)) + ", Mean: " + str(mean_val)
        print("Data has been stored successfully!")
        return data
        
    elif choice == '2':
        rows = int(input("Enter number of rows: "))
        data = []
        for i in range(rows):
            row_input = input("Enter row values separated by spaces: ")
            row = []
            for x in row_input.split():
                row.append(int(x))
            data.append(row)
            
        flat_data = []
        for row in data:
            for x in row:
                flat_data.append(x)
                
        total = 0
        for x in flat_data:
            total += x
            
        mean_val = total / len(flat_data) if len(flat_data) > 0 else 0
        global_summary = "Total elements: " + str(len(flat_data)) + ", Mean: " + str(mean_val)
        
        print("2D Grid Structure:")
        for row in data:
            row_str = ""
            for x in row:
                row_str += str(x) + " "
            print(row_str)
            
        print("Data has been stored successfully!")
        return data
        
    return []

def display_summary(data):
    if not data:
        print("No data available. Please input data first.")
        return
    
    flat_data = []
    if isinstance(data[0], list):
        for row in data:
            for x in row:
                flat_data.append(x)
    else:
        flat_data = data
        
    print("\nData Summary")
    print("Total Elements (len):", len(flat_data))
    print("Sum of Elements (sum):", sum(flat_data))
    print("Minimum Value (min):", min(flat_data))
    print("Maximum Value (max):", max(flat_data))
    mean_val = sum(flat_data) / len(flat_data) if len(flat_data) > 0 else 0
    print("Mean / Average:", mean_val)

def main():
    current_data = []
    while True:
        print("\nMAIN MENU")
        print("1. Input Data")
        print("2. Display Summary")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            current_data = input_data()
        elif choice == '2':
            display_summary(current_data)
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
