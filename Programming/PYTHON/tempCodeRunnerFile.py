import tkinter as tk
from tkinter import ttk, messagebox

class MemoryPartition:
    def __init__(self, size, pid=None):
        self.size, self.pid = size, pid

class Process:
    def __init__(self, pid, size, priority, burst_time):
        self.pid, self.size, self.priority, self.burst_time = pid, size, priority, burst_time

class MemoryAllocatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Professional Memory Allocation Analyzer")
        self.root.geometry("1000x800")
        self.configure_styles()
        self.create_widgets()
        self.center_window()

    def configure_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TFrame', background='#F0F0F0')
        self.style.configure('TLabel', background='#F0F0F0', font=('Segoe UI', 9))
        self.style.configure('TButton', font=('Segoe UI', 9), padding=6)
        self.style.configure('Header.TLabel', font=('Segoe UI', 10, 'bold'), foreground='#2C3E50')
        self.style.configure('Metrics.TLabel', font=('Consolas', 10), background='white', padding=5)
        self.style.map('TButton',
            foreground=[('active', '#FFFFFF'), ('!disabled', '#2C3E50')],
            background=[('active', '#2980B9'), ('!disabled', '#3498DB')]
        )

    def center_window(self):
        self.root.update_idletasks()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_width()
        window_height = self.root.winfo_height()
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f'+{x}+{y}')

    def create_widgets(self):
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        input_frame = ttk.LabelFrame(main_frame, text="Input Parameters", padding=15)
        input_frame.pack(fill=tk.X, pady=(0, 15))
        self.create_input_rows(input_frame)
        results_frame = ttk.Frame(main_frame)
        results_frame.pack(fill=tk.BOTH, expand=True)
        self.tree = ttk.Treeview(results_frame, columns=('Job', 'Priority', 'Memory', 'Burst'), show='headings', height=8)
        self.tree.heading('Job', text='Job', anchor=tk.CENTER)
        self.tree.heading('Priority', text='Priority Level', anchor=tk.CENTER)
        self.tree.heading('Memory', text='Memory Size (KB)', anchor=tk.CENTER)
        self.tree.heading('Burst', text='Burst Time', anchor=tk.CENTER)
        self.tree.column('Job', width=100, anchor=tk.CENTER)
        self.tree.column('Priority', width=150, anchor=tk.CENTER)
        self.tree.column('Memory', width=150, anchor=tk.CENTER)
        self.tree.column('Burst', width=150, anchor=tk.CENTER)
        self.tree.pack(fill=tk.BOTH, expand=True, pady=(0, 15))
        metrics_frame = ttk.LabelFrame(results_frame, text="Performance Metrics", padding=15)
        metrics_frame.pack(fill=tk.BOTH, expand=True)
        self.metrics_text = tk.Text(metrics_frame, height=8, font=('Consolas', 10), bg='white', fg='#2C3E50', padx=10, pady=10)
        self.metrics_text.pack(fill=tk.BOTH, expand=True)

    def create_input_rows(self, parent):
        entries = []
        fields = [
            ("OS Memory (KB):", "optional"), ("Partition Sizes (KB):", "required"),
            ("Memory Sizes (KB):", "required"), ("Process Priorities:", "required"),
            ("Burst Time:", "required"), ("Time:", "required")
        ]
        for i, (label, req) in enumerate(fields):
            row = ttk.Frame(parent)
            row.pack(fill=tk.X, pady=3)
            lbl = ttk.Label(row, text=label, width=20, style='Header.TLabel')
            lbl.pack(side=tk.LEFT, padx=(0, 10))
            entry = ttk.Entry(row, width=30)
            entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
            if req == 'required':
                ttk.Label(row, text="*", foreground='red').pack(side=tk.LEFT, padx=5)
            entries.append(entry)
        btn_frame = ttk.Frame(parent)
        btn_frame.pack(fill=tk.X, pady=(10, 0))
        ttk.Button(btn_frame, text="Allocate Memory", command=self.allocate_memory).pack(side=tk.LEFT, padx=5)
        ttk.Button(btn_frame, text="Clear All", command=self.clear_all).pack(side=tk.LEFT, padx=5)
        self.os_entry, self.partition_entry, self.process_entry, self.priority_entry, self.burst_entry, self.time_entry = entries

    def allocate_memory(self):
        try:
            for i in self.tree.get_children():
                self.tree.delete(i)
            self.metrics_text.delete(1.0, tk.END)
            # Parse inputs with comma handling
            os_memory = int(self.os_entry.get().strip().replace(',', '')) if self.os_entry.get().strip() else 0
            partitions = [int(x.replace(',', '')) for x in self.partition_entry.get().split()]
            process_sizes = [int(x.replace(',', '')) for x in self.process_entry.get().split()]
            priorities = [int(x.replace(',', '')) for x in self.priority_entry.get().split()]
            burst_times = [int(x.replace(',', '')) for x in self.burst_entry.get().split()]
            time = int(self.time_entry.get().strip().replace(',', '')) if self.time_entry.get().strip() else 0

            if os_memory < 0:
                messagebox.showerror("Error", "OS memory cannot be negative")
                return    
            if not partitions or not process_sizes:
                messagebox.showerror("Error", "Partitions and processes are required")
                return
            if len(process_sizes) != len(priorities) or len(process_sizes) != len(burst_times):
                messagebox.showerror("Error", "All process-related fields must have equal entries")
                return

            memory = [MemoryPartition(size) for size in partitions]
            processes = [Process(i+1, process_sizes[i], priorities[i], burst_times[i]) for i in range(len(process_sizes))]
            processes.sort(key=lambda x: (x.priority, x.pid))
            allocation = [-1] * len(processes)

            for process in processes:
                for j, partition in enumerate(memory):
                    if partition.pid is None and partition.size >= process.size:
                        partition.pid = process.pid
                        allocation[process.pid-1] = j
                        break

            self.display_results(processes, allocation, memory, os_memory, time)
        except ValueError:
            messagebox.showerror("Error", "Invalid input values")

    def display_results(self, processes, allocation, memory, os_memory, time):
        for process in processes:
            self.tree.insert('', 'end', values=(
                f"Job {process.pid}", process.priority, f"{process.size:,} KB", f"{process.burst_time} ms"
            ))
        process_map = {process.pid: process for process in processes}
        total_partitions = sum(p.size for p in memory)
        total_memory = os_memory + total_partitions
        # Fix allocation check using PID
        allocated_processes = sum(p.size for p in processes if allocation[p.pid-1] != -1)
        allocated_total = os_memory + allocated_processes
        # Fix internal fragmentation using PID map
        internal_frag = sum(p.size - process_map[p.pid].size for p in memory if p.pid)
        external_frag = sum(p.size for p in memory if not p.pid)
        utilization = (allocated_total / total_memory) * 100 if total_memory > 0 else 0

        metrics = [
            "┌─────────────────────── Metrics Summary ───────────────────────┐",
            f"│ {'OS Memory:':<25} {os_memory:,} KB {'(User Specified)' if self.os_entry.get().strip() else '(Default)'}",
            f"│ {'Time:':<25} {time} ms",
            f"│ {'Internal Fragmentation:':<25} {internal_frag:,} KB",
            f"│ {'External Fragmentation:':<25} {external_frag:,} KB",
            f"│ {'Memory Utilization:':<25} {utilization:.2f}%",
            "└───────────────────────────────────────────────────────────────┘",
            "\nCalculation Details:",
            f"Total Memory = {'OS + ' if os_memory else ''}Partitions = {os_memory:,} + {total_partitions:,} = {total_memory:,} KB",
            f"Allocated Memory = {'OS + ' if os_memory else ''}Processes = {os_memory:,} + {allocated_processes:,} = {allocated_total:,} KB",
            f"Utilization = ({allocated_total:,} / {total_memory:,}) × 100 = {utilization:.2f}%"
        ]
        self.metrics_text.insert(tk.END, "\n".join(metrics))
        self.metrics_text.tag_configure('center', justify='center')
        self.metrics_text.tag_add('center', '1.0', 'end')

    def clear_all(self):
        for entry in [self.os_entry, self.partition_entry, self.process_entry,
                     self.priority_entry, self.burst_entry, self.time_entry]:
            entry.delete(0, tk.END)
        for i in self.tree.get_children():
            self.tree.delete(i)
        self.metrics_text.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoryAllocatorApp(root)
    root.mainloop()