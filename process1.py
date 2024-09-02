import time
class Process1:
    def __init__(self, filepath):
        self.filepath = filepath

    def run(self):
        print(f"Running Process 1 with file: {self.filepath}")
        # Simulate process running time
        time.sleep(5)
        print("Process 1 completed.")

# Example usage:
# process = Process1('/path/to/file')
# process.run()
