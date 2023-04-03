import os
import time
time.sleep(30)

folder_path = "D:\All backup\output"

files = os.listdir(folder_path)

files = sorted(files, key=lambda f: os.path.getmtime(os.path.join(folder_path, f)), reverse=True)

latest_files = files[:5]

for file in files[5:]:
    os.remove(os.path.join(folder_path, file))
