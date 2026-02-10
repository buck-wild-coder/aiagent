from functions.get_files_info import get_files_info

calls = [get_files_info("calculator", "."),
        get_files_info("calculator", "pkg"),
        get_files_info("calculator", "../"),
        get_files_info("calculator", "/bin")]

for call in calls:
    print(call)