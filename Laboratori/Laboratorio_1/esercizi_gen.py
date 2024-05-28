import os

for i in range (1,10):
    folder_name = f"Es_{i}"
    file_name = f"Es{i}.py"

    os.makedirs(folder_name,exist_ok=True)

    file_path = os.path.join(folder_name, file_name)
    with open(file_path, 'w') as file:
        file.write(" ")
