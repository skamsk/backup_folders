import os, time, sys
import shutil
folder = r"C:\path\to"
now = time.time()
old = 324000 # время в секундах, которое папки будут существовать 14 дней это 50 400 сек


for the_file in os.listdir(folder):
    file_path = os.path.join(folder, the_file)
    try:
        if os.path.isfile(file_path):
            assert os.path.getmtime(file_path) < now - old
            if os.stat(file_path).st_mtime < now - old:
                print(file_path)
                os.unlink(file_path)
        elif os.path.isdir(file_path):
            if os.stat(file_path).st_mtime < now - old:
                print(file_path)
                shutil.rmtree(file_path)
    except Exception as e:
        print("Не удалось очистить папку")