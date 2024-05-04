import os

def replace_content(file_path):
    # Đọc nội dung từ tệp
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Tìm và thay thế nội dung
    new_lines = []
    inside_div = False
    for line in lines:
        if '<div class="col-xl-7 col-xxl-8">' in line:
            inside_div = True
            new_lines.append(' ')
        elif inside_div and '</div>' in line:
            inside_div = False
            new_lines.append(' ')
        elif inside_div:
            new_lines.append(' ')
        else:
            new_lines.append(line)

    # Ghi lại nội dung đã thay thế vào tệp
    with open(file_path, 'w', encoding='utf-8') as file:
        file.writelines(new_lines)

def replace_in_folder(folder_path):
    # Lặp qua tất cả các tệp trong thư mục
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.html'):
                file_path = os.path.join(root, file_name)
                replace_content(file_path)

# Thay đổi nội dung trong tất cả các tệp HTML trong thư mục hiện tại
replace_in_folder('.')
