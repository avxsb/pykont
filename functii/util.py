import os
def run_file(file_name):
    file_path = os.path.join(os.path.dirname(__file__), file_name)
    execfile(file_path)




