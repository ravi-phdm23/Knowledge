import time
class Process2:
    def __init__(self, filepath):
        self.filepath = filepath

    def run(self):
        print(f"Running Process 2 with file: {self.filepath}")
        # Simulate process running time
        time.sleep(5)
        print("Process 2 completed.")

# Example usage:
# process = Process2('/path/to/file')
# process.run()
