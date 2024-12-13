import tkinter as tk
from tkinter import ttk, messagebox
from housing import Housing
from housing import FilterPreference

class HousingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UMD Student Housing Finder")
        self.housing_list = []
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # Filter options
        self.filter_frame = ttk.LabelFrame(self.root, text="Filter Options")
        self.filter_frame.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        # min / max labels
        self.min_label = ttk.Label(self.filter_frame, text="Minimum")
        self.min_label.grid(row=0, column=1, padx=5, pady=5)

        self.max_label = ttk.Label(self.filter_frame, text="Maximum")
        self.max_label.grid(row=0, column=2, padx=5, pady=5)

        # Bedrooms filter
        self.bed_label = ttk.Label(self.filter_frame, text="Bedrooms:")
        self.bed_label.grid(row=1, column=0, padx=5, pady=5)
        self.min_bed = ttk.Combobox(self.filter_frame, values=[1, 2, 3, 4, 5], width=5)
        self.min_bed.grid(row=1, column=1, padx=5, pady=5)
        self.max_bed = ttk.Combobox(self.filter_frame, values=[1, 2, 3, 4, 5], width=5)
        self.max_bed.grid(row=1, column=2, padx=5, pady=5)

        # Bathrooms filter
        self.bath_label = ttk.Label(self.filter_frame, text="Bathrooms:")
        self.bath_label.grid(row=2, column=0, padx=5, pady=5)
        self.min_bath = ttk.Combobox(self.filter_frame, values=[1, 2, 3, 4, 5], width=5)
        self.min_bath.grid(row=2, column=1, padx=5, pady=5)
        self.max_bath = ttk.Combobox(self.filter_frame, values=[1, 2, 3, 4, 5], width=5)
        self.max_bath.grid(row=2, column=2, padx=5, pady=5)

        # Price filter
        self.price_label = ttk.Label(self.filter_frame, text="Price:")
        self.price_label.grid(row=3, column=0, padx=5, pady=5)
        self.min_price = ttk.Entry(self.filter_frame, width=10)
        self.min_price.grid(row=3, column=1, padx=5, pady=5)
        self.max_price = ttk.Entry(self.filter_frame, width=10)
        self.max_price.grid(row=3, column=2, padx=5, pady=5)

        # Distance filter
        self.distance_label = ttk.Label(self.filter_frame, text="Distance:")
        self.distance_label.grid(row=4, column=0, padx=5, pady=5)
        self.min_distance = ttk.Entry(self.filter_frame, width=10)
        self.min_distance.grid(row=4, column=1, padx=5, pady=5)
        self.max_distance = ttk.Entry(self.filter_frame, width=10)
        self.max_distance.grid(row=4, column=2, padx=5, pady=5)

        # Priority options
        self.priority_label = ttk.Label(self.filter_frame, text="Prioritize:")
        self.priority_label.grid(row=0, column=4, padx=5, pady=5)

        self.priority_bed_var = tk.BooleanVar()
        self.priority_bed = ttk.Checkbutton(self.filter_frame, variable=self.priority_bed_var)
        self.priority_bed.grid(row=1, column=4, padx=5, pady=5)

        self.priority_bath_var = tk.BooleanVar()
        self.priority_bath = ttk.Checkbutton(self.filter_frame,variable=self.priority_bath_var)
        self.priority_bath.grid(row=2, column=4, padx=5, pady=5)

        self.priority_price_var = tk.BooleanVar()
        self.priority_price = ttk.Checkbutton(self.filter_frame,variable=self.priority_price_var)
        self.priority_price.grid(row=3, column=4, padx=5, pady=5)

        self.priority_distance_var = tk.BooleanVar()
        self.priority_distance = ttk.Checkbutton(self.filter_frame, variable=self.priority_distance_var)
        self.priority_distance.grid(row=4, column=4, padx=5, pady=5)

        # Priority explanors:
        self.priority_ex_label = ttk.Label(self.filter_frame, text="What Not Prioritizing alters:")
        self.priority_ex_label.grid(row=0, column=5, padx=5, pady=5)

        self.priority_ex_bed_label = ttk.Label(self.filter_frame, text="-1 min bed / +1 max bed")
        self.priority_ex_bed_label.grid(row=1, column=5, padx=5, pady=5)

        self.priority_ex_bath_label = ttk.Label(self.filter_frame, text="-1 min bath / +1 max bath")
        self.priority_ex_bath_label.grid(row=2, column=5, padx=5, pady=5)

        self.priority_ex_price_label = ttk.Label(self.filter_frame, text="-250 min price / +250 max price")
        self.priority_ex_price_label.grid(row=3, column=5, padx=5, pady=5)

        self.priority_ex_distance_label = ttk.Label(self.filter_frame, text="-0.2 min distance / +0.2 max distance")
        self.priority_ex_distance_label.grid(row=4, column=5, padx=5, pady=5)

        # All Label + Checkbutton
        self.priority_all_label = ttk.Label(self.filter_frame, text="Select all:")
        self.priority_all_label.grid(row=5, column=2, padx=5, pady=5)
        
        self.priority_all_var = tk.BooleanVar()
        self.priority_all = ttk.Checkbutton(self.filter_frame, variable=self.priority_all_var, command=self.toggle_all_priorities)
        self.priority_all.grid(row=5, column=4, padx=5, pady=5)

        # Apply filters button
        self.apply_button = ttk.Button(self.filter_frame, text="Apply Filters", command=self.apply_filters)
        self.apply_button.grid(row=5, column=0, columnspan=1, padx=5, pady=5)

        # Separator
        self.separator = ttk.Separator(self.root, orient='vertical')
        self.separator.grid(row=0, column=1, rowspan=2, sticky='ns', padx=10)

        # Example w/all priorities column
        self.examples_frame = ttk.LabelFrame(self.root, text="Example 1: input/output [with all priorities selected]")
        self.examples_frame.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

        # Example labels
        self.example_bed_label = ttk.Label(self.examples_frame, text="Bedrooms: 2-3")
        self.example_bed_label.grid(row=0, column=0, padx=5, pady=5)
        self.example_bath_label = ttk.Label(self.examples_frame, text="Bathrooms: 2-3")
        self.example_bath_label.grid(row=1, column=0, padx=5, pady=5)
        self.example_price_label = ttk.Label(self.examples_frame, text="Price: $500 - $1500")
        self.example_price_label.grid(row=2, column=0, padx=5, pady=5)
        self.example_distance_label = ttk.Label(self.examples_frame, text="Distance: 1-4 miles")
        self.example_distance_label.grid(row=3, column=0, padx=5, pady=5)
        self.example_prority_bed_label = ttk.Label(self.examples_frame, text="Priorities:")
        self.example_results1_label = ttk.Label(self.examples_frame, text="Result1: Tempo: 2 beds, 2 baths, $1429, 825 sqft, 1.0 miles")
        self.example_results1_label.grid(row=4, column=0, padx=5, pady=5)
        self.example_results2_label = ttk.Label(self.examples_frame, text="Result2: Tempo: 3 beds, 3 baths, $1425, 839 sqft, 1.0 miles")
        self.example_results2_label.grid(row=5, column=0, padx=5, pady=5)

        
        # Example w/out all priorities selected
        self.examples_frame = ttk.LabelFrame(self.root, text="Example 2: input/output [with NOT all priorities selected]")
        self.examples_frame.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

        # Example2 labels
        self.example_bed2_label = ttk.Label(self.examples_frame, text="Bedrooms: 2-3")
        self.example_bed2_label.grid(row=0, column=0, padx=5, pady=5)
        self.example_bath2_label = ttk.Label(self.examples_frame, text="Bathrooms: 2-3")
        self.example_bath2_label.grid(row=1, column=0, padx=5, pady=5)
        self.example_price2_label = ttk.Label(self.examples_frame, text="Price: $500 - $1500")
        self.example_price2_label.grid(row=2, column=0, padx=5, pady=5)
        self.example_distance2_label = ttk.Label(self.examples_frame, text="Distance: 1-4 miles | Priority box not checked") 
        self.example_distance2_label.grid(row=3, column=0, padx=5, pady=5)
        self.example_prority2_bed_label = ttk.Label(self.examples_frame, text="Priorities:")
        self.example_results1_2_label = ttk.Label(self.examples_frame, text="Result1: University View: 2 beds, 2 baths, $1249, unknown sqft, 0.8 miles")
        self.example_results1_2_label.grid(row=4, column=0, padx=5, pady=5)
        self.example_results2_2_label = ttk.Label(self.examples_frame, text="Result2: Tempo: 2 beds, 2 baths, $1429, 825 sqft, 1.0 miles")
        self.example_results2_2_label.grid(row=5, column=0, padx=5, pady=5)
        self.example_results3_2_label = ttk.Label(self.examples_frame, text="Result3: Tempo: 3 beds, 3 baths, $1425, 839 sqft, 1.0 miles")
        self.example_results3_2_label.grid(row=6, column=0, padx=5, pady=5)
        self.example_results4_2_label = ttk.Label(self.examples_frame, text="Result4: The Standard: 2 beds, 2 baths, $1429, 718 sqft, 0.9 miles")
        self.example_results4_2_label.grid(row=7, column=0, padx=5, pady=5)
        self.example_results5_2_label = ttk.Label(self.examples_frame, text="Result5: The Standard: 3 beds, 3 baths, $1399, 1109 sqft, 0.9 miles")
        self.example_results5_2_label.grid(row=8, column=0, padx=5, pady=5)

        # Results display
        self.priority_results_frame = ttk.LabelFrame(self.root, text="Results")
        self.priority_results_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        self.priority_results_text = tk.Text(self.priority_results_frame, height=10, width=70)
        self.priority_results_text.grid(row=0, column=0, padx=5, pady=5)


    def toggle_all_priorities(self):
        '''
        Allows the selection of all priorities at once
        '''
        state = self.priority_all_var.get()
        self.priority_bed_var.set(state)
        self.priority_bath_var.set(state)
        self.priority_price_var.set(state)
        self.priority_distance_var.set(state)
    
    def load_data(self):
        try:
            self.housing_list = Housing.load_housing_data("housing_data.csv")
            messagebox.showinfo("Data Loaded", "Housing data loaded successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load data: {e}")

    def apply_filters(self):
        try:
            # Get filter values
            min_beds = int(self.min_bed.get() or 0)
            max_beds = int(self.max_bed.get() or float('inf'))
            min_baths = int(self.min_bath.get() or 0)
            max_baths = int(self.max_bath.get() or float('inf'))
            min_price = float(self.min_price.get() or 0)
            max_price = float(self.max_price.get() or float('inf'))
            min_distance = float(self.min_distance.get() or 0)
            max_distance = float(self.max_distance.get() or float('inf'))

            # Get priority values
            priority_bed = self.priority_bed_var.get()
            priority_bath = self.priority_bath_var.get()
            priority_price = self.priority_price_var.get()
            priority_distance = self.priority_distance_var.get()

            # Create priorities dictionary with priority status
            priorities = {}
            
            # Add filters with their priority status
            if min_beds != 0 or max_beds != float('inf'):
                priorities['beds'] = (min_beds, max_beds, priority_bed)
            if min_baths != 0 or max_baths != float('inf'):
                priorities['baths'] = (min_baths, max_baths, priority_bath)
            if min_price != 0 or max_price != float('inf'):
                priorities['price'] = (min_price, max_price, priority_price)
            if min_distance != 0 or max_distance != float('inf'):
                priorities['distance'] = (min_distance, max_distance, priority_distance)

            # Create an instance of FilterPreference
            filter_preference = FilterPreference(self.housing_list)

            # Adjust filters for non-prioritized items
            min_beds, max_beds, min_baths, max_baths, min_price, max_price, min_distance, max_distance = filter_preference.adjust_filters(
                min_beds, max_beds, min_baths, max_baths, min_price, max_price, min_distance, max_distance, priorities
            )

            # Filter housing list
            priority_results, priority_message = filter_preference.filter(priorities)

            # Display results
            self.priority_results_text.delete(1.0, tk.END)
            if priority_results:
                for house in priority_results:
                    self.priority_results_text.insert(tk.END, f"{house}\n")
            else:
                self.priority_results_text.insert(tk.END, f"{priority_message}\n")

        except Exception as e:
            messagebox.showerror("Error", f"Failed to apply filters: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HousingApp(root)
    root.mainloop()