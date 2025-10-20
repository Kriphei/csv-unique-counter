"""
CSV Unique Value Counter
A simple tool to count unique values in CSV columns using DuckDB
"""

import duckdb
import tkinter as tk
from tkinter import filedialog, messagebox
import os
from pathlib import Path
from datetime import datetime


def get_downloads_folder() -> str:
    """Get the user's Downloads folder path"""
    return str(Path.home() / "Downloads")


def select_csv_file() -> str:
    """Open file dialog to select a CSV file"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    file_path = filedialog.askopenfilename(
        title="Select a CSV file",
        filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
    )
    
    root.destroy()
    return file_path


def get_column_names(file_path: str) -> list[str]:
    """Get column names from the CSV file using DuckDB"""
    try:
        conn = duckdb.connect(':memory:')
        result = conn.execute(f"DESCRIBE SELECT * FROM read_csv_auto('{file_path}')").fetchall()
        columns = [row[0] for row in result]
        conn.close()
        return columns
    except Exception as e:
        raise Exception(f"Error reading CSV file: {str(e)}")


def show_column_selector(columns: list[str]) -> str:
    """Show a dialog to select which column to analyze"""
    root = tk.Tk()
    root.title("Select Column")
    root.geometry("400x500")
    
    selected_column = tk.StringVar()
    
    # Title label
    title_label = tk.Label(
        root, 
        text="Select a column to count unique values:", 
        font=("Arial", 12, "bold"),
        pady=10
    )
    title_label.pack()
    
    # Frame for listbox and scrollbar
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
    
    # Scrollbar
    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Listbox
    listbox = tk.Listbox(
        frame, 
        yscrollcommand=scrollbar.set,
        font=("Arial", 10),
        selectmode=tk.SINGLE
    )
    
    for col in columns:
        listbox.insert(tk.END, col)
    
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)
    
    def on_select():
        if not listbox.curselection():
            messagebox.showwarning("No Selection", "Please select a column!")
            return
        selected_column.set(columns[listbox.curselection()[0]])
        root.quit()
    
    # Select button
    select_btn = tk.Button(
        root, 
        text="Count Unique Values", 
        command=on_select,
        font=("Arial", 11),
        bg="#4CAF50",
        fg="white",
        padx=20,
        pady=10
    )
    select_btn.pack(pady=20)
    
    root.mainloop()
    result = selected_column.get()
    root.destroy()
    
    return result


def count_unique_values(file_path: str, column_name: str) -> tuple[list[tuple], int]:
    """
    Count unique values in the specified column using DuckDB
    Returns: (list of tuples with value and count, total unique values)
    """
    try:
        conn = duckdb.connect(':memory:')
        
        # Query to count unique values, ordered by count descending
        query = f"""
        SELECT 
            "{column_name}" as value,
            COUNT(*) as count
        FROM read_csv_auto('{file_path}')
        GROUP BY "{column_name}"
        ORDER BY count DESC, value
        """
        
        results = conn.execute(query).fetchall()
        total_unique = len(results)
        
        conn.close()
        return results, total_unique
        
    except Exception as e:
        raise Exception(f"Error counting unique values: {str(e)}")


def save_results(results: list[tuple], column_name: str, csv_filename: str, downloads_path: str) -> str:
    """Save results to a text file in the Downloads folder"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"unique_values_{column_name}_{timestamp}.txt"
    output_path = os.path.join(downloads_path, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"Unique Value Count Report\n")
        f.write(f"=" * 60 + "\n")
        f.write(f"Source File: {csv_filename}\n")
        f.write(f"Column: {column_name}\n")
        f.write(f"Total Unique Values: {len(results)}\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"=" * 60 + "\n\n")
        
        # Write results
        f.write(f"{'Value':<40} {'Count':>15}\n")
        f.write(f"{'-' * 40} {'-' * 15}\n")
        
        for value, count in results:
            value_str = str(value) if value is not None else "(NULL)"
            f.write(f"{value_str:<40} {count:>15,}\n")
    
    return output_path


def main():
    """Main program flow"""
    print("=" * 60)
    print("CSV Unique Value Counter (Powered by DuckDB)")
    print("=" * 60)
    print()
    
    # Step 1: Select CSV file
    print("Step 1: Select a CSV file...")
    csv_file = select_csv_file()
    
    if not csv_file:
        print("No file selected. Exiting.")
        return
    
    print(f"Selected: {os.path.basename(csv_file)}")
    print()
    
    # Step 2: Get column names
    print("Step 2: Reading column names...")
    try:
        columns = get_column_names(csv_file)
        print(f"Found {len(columns)} columns")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", str(e))
        return
    
    print()
    
    # Step 3: Select column
    print("Step 3: Select a column to analyze...")
    selected_column = show_column_selector(columns)
    
    if not selected_column:
        print("No column selected. Exiting.")
        return
    
    print(f"Selected column: {selected_column}")
    print()
    
    # Step 4: Count unique values
    print("Step 4: Counting unique values...")
    try:
        results, total_unique = count_unique_values(csv_file, selected_column)
        print(f"Found {total_unique} unique values")
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("Error", str(e))
        return
    
    print()
    
    # Step 5: Display results (first 20)
    print("=" * 60)
    print("RESULTS (Top 20)")
    print("=" * 60)
    print(f"{'Value':<40} {'Count':>15}")
    print(f"{'-' * 40} {'-' * 15}")
    
    for value, count in results[:20]:
        value_str = str(value) if value is not None else "(NULL)"
        # Truncate long values
        if len(value_str) > 37:
            value_str = value_str[:37] + "..."
        print(f"{value_str:<40} {count:>15,}")
    
    if len(results) > 20:
        print(f"\n... and {len(results) - 20} more unique values")
    
    print()
    
    # Step 6: Save results
    print("Step 6: Saving results to Downloads folder...")
    try:
        downloads_path = get_downloads_folder()
        output_file = save_results(
            results, 
            selected_column, 
            os.path.basename(csv_file),
            downloads_path
        )
        print(f"Results saved to: {output_file}")
        print()
        
        # Show success message
        messagebox.showinfo(
            "Success!", 
            f"Analysis complete!\n\n"
            f"Total unique values: {total_unique:,}\n\n"
            f"Results saved to:\n{output_file}"
        )
        
    except Exception as e:
        print(f"Error saving file: {e}")
        messagebox.showerror("Error", f"Error saving file: {e}")
        return
    
    print("=" * 60)
    print("Complete!")
    print("=" * 60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Unexpected error: {e}")
        messagebox.showerror("Error", f"Unexpected error: {e}")
    
    input("\nPress Enter to exit...")


