import tkinter as tk
from tkinter import ttk, messagebox

def calculate_time():
    # Get user inputs
    start_time = start_entry.get().strip()
    duration = duration_entry.get().strip()
    day = day_entry.get().strip() or None
    
    try:
        # Calculate the result
        result = add_time(start_time, duration, day)
        
        # Show result in a new window
        show_result_window(result)
        
    except Exception as e:
        messagebox.showerror("Oops!", f"Something went wrong:\n{e}")

def show_result_window(result):
    """Create a popup window to display the calculation result"""
    popup = tk.Toplevel()
    popup.title("Result")
    popup.geometry("350x150")
    
    # Make the popup appear centered over main window
    popup.transient(root)
    popup.grab_set()
    
    # Result display
    tk.Label(popup, text="Your calculated time:", 
            font=('Arial', 11)).pack(pady=(15, 5))
    
    tk.Label(popup, text=result, 
            font=('Arial', 14, 'bold'), fg='blue').pack(pady=5)
    
    # Close button
    ttk.Button(popup, text="OK", command=popup.destroy).pack(pady=10)

def add_time(start, duration, day=None):
    """Core time calculation logic"""
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 
            'Friday', 'Saturday', 'Sunday']
    
    # Parse start time
    time_part, period = start.split()
    hours, minutes = map(int, time_part.split(':'))
    
    # Convert to 24-hour format
    if period == 'PM' and hours != 12:
        hours += 12
    elif period == 'AM' and hours == 12:
        hours = 0
    
    # Add duration
    add_hours, add_mins = map(int, duration.split(':'))
    total_mins = minutes + add_mins
    total_hours = hours + add_hours + total_mins // 60
    final_mins = total_mins % 60
    
    # Calculate days passed
    days_passed = total_hours // 24
    final_hours = total_hours % 24
    
    # Convert back to 12-hour format
    if final_hours == 0:
        display_hour = 12
        period = 'AM'
    elif final_hours < 12:
        display_hour = final_hours
        period = 'AM'
    elif final_hours == 12:
        display_hour = 12
        period = 'PM'
    else:
        display_hour = final_hours - 12
        period = 'PM'
    
    # Format the result
    result = f"{display_hour}:{final_mins:02d} {period}"
    
    # Add day if provided
    if day:
        day_index = days.index(day.capitalize())
        new_day = days[(day_index + days_passed) % 7]
        result += f", {new_day}"
    
    # Add days later info
    if days_passed == 1:
        result += " (next day)"
    elif days_passed > 1:
        result += f" ({days_passed} days later)"
    
    return result

# Set up main window
root = tk.Tk()
root.title("Time Calculator")
root.geometry("380x220")
root.resizable(False, False)

# Create and style widgets
main_frame = ttk.Frame(root, padding=15)
main_frame.pack(fill='both', expand=True)

# Input fields
ttk.Label(main_frame, text="Start Time (e.g. 3:30 PM):").grid(row=0, column=0, sticky='w', pady=3)
start_entry = ttk.Entry(main_frame, width=20)
start_entry.grid(row=0, column=1, padx=5, pady=3)

ttk.Label(main_frame, text="Duration (e.g. 2:15):").grid(row=1, column=0, sticky='w', pady=3)
duration_entry = ttk.Entry(main_frame, width=20)
duration_entry.grid(row=1, column=1, padx=5, pady=3)

ttk.Label(main_frame, text="Day (optional):").grid(row=2, column=0, sticky='w', pady=3)
day_entry = ttk.Entry(main_frame, width=20)
day_entry.grid(row=2, column=1, padx=5, pady=3)

# Calculate button
calc_button = ttk.Button(main_frame, text="Calculate Time", command=calculate_time)
calc_button.grid(row=3, column=0, columnspan=2, pady=15)

# Start the application
root.mainloop()