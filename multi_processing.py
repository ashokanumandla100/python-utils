from concurrent.futures import ProcessPoolExecutor
import os
from time import perf_counter, sleep

def get_me_py_files():
    base_path = r'D:\Ashok\SDM'
    files_list = []
    for path,_,files in os.walk(base_path):
        for name in files:
            if name.endswith('.py'):
                files_list.append(os.path.join(path,name))
    return files_list

def process_each_file(inp_file_path):
    with open(inp_file_path, 'r') as f:
        content = f.read()
        sleep(0.5)
        if content.find('blob') > 0:
            return_msg = f"{inp_file_path}: File contains blob word"
        else:
            return_msg = f"{inp_file_path}: File doesn't contain blob word"           

    return return_msg

def invoke_multiple_process(list_of_py_files):

    t1_start = perf_counter()

    with ProcessPoolExecutor(max_workers=3) as executor:
        futures = executor.map(process_each_file, list_of_py_files)

    for _ in futures:
        print(_)

    t1_stop = perf_counter()
    print("Multiple Process Elapsed Time:", round((t1_stop-t1_start),2), 'secs')

def normal_process(list_of_py_files):
    t2_start = perf_counter()
    results = map(process_each_file, list_of_py_files)
    
    for _ in results:
        print(_)

    t2_stop = perf_counter()
    print("Normal Process Elapsed Time:", round((t2_stop-t2_start),2), 'secs')   

def main():
    list_of_py_files =  get_me_py_files()
    invoke_multiple_process(list_of_py_files)
    normal_process(list_of_py_files)

if __name__ == "__main__":
    main()