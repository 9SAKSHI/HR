import os

# Root directory containing year folders
root_dir = r"C:\Users\sakshi nimbalkar\.vscode\Python\HR"  # Use raw string for paths
# Ordered calendar months for sorting
calendar_order = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
# Target month and date
Target_month = "Feb"
Target_date = 6

# Iterate over year folders
for year_folder in os.listdir(root_dir):
    year_path = os.path.join(root_dir, year_folder)

    # Ensure it's a directory
    if os.path.isdir(year_path):
        # List and sort months based on calendar order
        month_list = os.listdir(year_path)
        sorted_months = sorted(month_list, key=lambda x: calendar_order.index(x))
        print(f"Year {year_folder} - Sorted months:", sorted_months)

        # Iterate over sorted months
        for month_folder in sorted_months:
            month_path = os.path.join(year_path, month_folder)
            if os.path.isdir(month_path):
                # List date folders and convert to integers
                date_list = os.listdir(month_path)
                int_date_list = [int(date) for date in date_list]

                # Iterate over dates in the current month
                for date_folder in int_date_list:
                    # Process all dates if the current month is before the target month
                    if calendar_order.index(month_folder) < calendar_order.index(Target_month):
                        date_path = os.path.join(month_path, str(date_folder))
                        print(f"Processing folder: {date_path}")

                        # Check for Excel files in the folder
                        if os.path.exists(date_path):  # Ensure the folder exists
                            for file in os.listdir(date_path):
                                if file.endswith(".xlsx") or file.endswith(".xls"):  # Check for Excel files
                                    file_path = os.path.join(date_path, file)
                                    print(f"Found Excel file: {file_path}")
                        else:
                            print(f"Folder does not exist: {date_path}")

                    # Process only dates up to the Target_date if it's the target month
                    elif month_folder == Target_month and date_folder <= Target_date:
                        date_path = os.path.join(month_path, str(date_folder))
                        print(f"Processing folder: {date_path}")

                        # Check for Excel files in the folder
                        if os.path.exists(date_path):  # Ensure the folder exists
                            for file in os.listdir(date_path):
                                if file.endswith(".xlsx") or file.endswith(".xls"):  # Check for Excel files
                                    file_path = os.path.join(date_path, file)
                                    print(f"Found Excel file: {file_path}")
                        else:
                            print(f"Folder does not exist: {date_path}")

                        # Stop processing after the target date
                        if date_folder == Target_date:
                            break

            # Stop processing months after the target month
            if month_folder == Target_month:
                break
