from functions.get_file_content import get_file_content


calls = [
        get_file_content("calculator", "main.py"),
        get_file_content("calculator", "pkg/calculator.py"),
        get_file_content("calculator", "/bin/cat"),
        get_file_content("calculator", "pkg/does_not_exist.py")
       ]

for call in calls:
    print(call)
