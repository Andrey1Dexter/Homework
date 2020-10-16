path = 'F:\python_work\Homework\something'
import os

def scan_folder(path):
    attachment = os.listdir(path)
    if not attachment:
        return None
    if len(attachment) >= 1:
        result = []
        for attach in attachment:
            entry_path = path + '/' + attach
            if os.path.isfile(entry_path):
                None
            else:
                result.append(
                    {attach: scan_files(entry_path) }
                )
        return result

def scan_files(path):
    attachment = os.listdir(path)
    if not attachment:
        return None
    if len(attachment) >= 1:
        result = []
        for attach in attachment:
            entry_path = path + '/' + attach
            if os.path.isfile(entry_path):
                result.append(attach)
            else: None
        return result

def show_me_yourself(path):
    dir = {'Files': scan_files(path), 'Folders': scan_folder(path)}
    return dir

print(show_me_yourself(path))