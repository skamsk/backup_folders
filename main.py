import glob
import os
import datetime
import shutil
#Настройки:
#Путь к основному каталогу откуда надо копировать
pathtodata="c:/dev"
#Название каталогов, которые надо копировать с их содержимым:
organiz = ["Temp1"]
# делаем каталог для копий по текущему времени
# по умолчанию должен быть создан каталог e:/_backups/
dt = datetime.datetime.now()
currentdate = dt.strftime('%Y_%m_%d-%H%M%S')
os.mkdir('Z:/screenshots/arh/1/'+currentdate)
os.chdir('Z:/screenshots/arh/1/')
files = os.listdir(path='Z:/screenshots/arh/1/')
print(len(files))
if len(files) > 14:
    for file in os.listdir():
            try:
                os.remove(file)
            except Exception:
                shutil.rmtree(file)

for org in organiz:
    print(org+" копирование...")
    # скопируем все каталоги в созданный
    # копирование дерева  - откуда - куда
    #shutil.copytree(''+pathtodata+'/'+org+'', 'c:/Backups/'+currentdate+'/'+org+'/')
    try:
        shutil.copytree(''+pathtodata+'/'+org+'', '//10.146.65.8/ayakimov\screenshots/arh/1/'+currentdate+'/'+org+'/')
    except:
        FileExistsError("Файл сегодня уже скопировался")
# заархивируем все что скопировано
names = glob.glob('Z:/screenshots/arh/1/'+currentdate+'/*')

for name in names:
    if os.path.isdir(name):
        # заархивировать все name используем winrar 4.01
        print (name+" архивирование каталога...")
        # ключ -df удаляет скопированные каталоги после архивирования
        os.system(r'c:/"Program Files"/"winrar"/rar.exe a -r -ep1 -df '+name+' '+name+' ')

# все сделал
print("все сделано")