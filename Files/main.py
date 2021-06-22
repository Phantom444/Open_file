import os


def join_files_in_dir(path, result_file):
    files_dict = {}

    for root, _, files in os.walk(path):
        for filename in files:
            with open(f'{root}/{filename}') as file:
                lines = file.readlines()
                files_dict[filename] = {
                    'lines': str(len(lines)),
                    'content': ''.join(lines)
                }

    sorted_files = sorted(files_dict.items(), key=lambda x: x[1]['lines'])

    with open(result_file, 'w') as result:
        for file in sorted_files:
            result.write(f'{file[0]}\n')
            result.write(f'{file[1]["lines"]}\n')
            result.write(f'{file[1]["content"]}\n')


join_files_in_dir('./test_files', 'result_file.txt')