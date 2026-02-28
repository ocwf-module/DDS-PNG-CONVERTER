import os
from PIL import Image

Working_Directory = os.getcwd()
print(f'Working directory: {Working_Directory}')
What_Remove = int(input('Delete source files [.dds] to reduce space? Select a number and press [Enter]:\n0 - No\n1 - Yes\n\nYour choice: '))

def Conversion_DDS_Files(Input_DDS):
    try:
        IMG = Image.open(Input_DDS)
        IMG.save(os.path.join(os.path.dirname(Input_DDS), os.path.splitext(Input_DDS)[0] + '.png'))
        print(f"[{Input_DDS}]: Successfully processed")
        if What_Remove == 1:
            try:
                os.remove(Input_DDS)
            except:
                print(f"Error: couldn't delete the file: [{file}]")
    except Exception as Error:
        print(f"Error: [{Input_DDS}] was not processed. More detailed: {Error}")

def Get_All_DDS_Files():
    All_DDS = []
    for root, dirs, files in os.walk(Working_Directory):
        for file in files:
            if file.endswith('.dds'):
                All_DDS.append(os.path.join(root, file))
    return All_DDS

Files = Get_All_DDS_Files()

for File in Files:
    Conversion_DDS_Files(File)

input('\nThe program has been completed successfully! To close the program, press [Enter]...')
