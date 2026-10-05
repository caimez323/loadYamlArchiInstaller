import os
import sys
import tkinter as tk
from tkinter import filedialog
import shutil
import traceback
def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath('.')
    return os.path.join(base_path, relative_path)
def choose_archipelago_folder():
    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    path = filedialog.askdirectory(title='Select Archipelago folder', mustexist=True)
    root.destroy()
    return path
def wait_to_exit():
    try:
        input('Press Enter to exit...')
    except Exception:
        return None
def main():
    default_path = 'C:\\ProgramData\\Archipelago'
    default_exe = os.path.join(default_path, 'ArchipelagoLauncher.exe')
    selected_folder = None
    if os.path.exists(default_exe):
        print('Archipelago installation found.')
    else:
        print('Archipelago installation not found.')
        selected_folder = choose_archipelago_folder()
        if selected_folder:
            print(f'Selected folder: {selected_folder}')
            archipelago_launcher_exe = os.path.join(selected_folder, 'ArchipelagoLauncher.exe')
            if os.path.exists(archipelago_launcher_exe):
                print('Selected Archipelago folder contains ArchipelagoLauncher.exe.')
            else:
                print('The selected folder does not contain ArchipelagoLauncher.exe.')
                wait_to_exit()
                return
        else:
            print('No Archipelago folder selected.')
            wait_to_exit()
            return
    selected_folder = selected_folder if selected_folder else default_path
    if not os.path.exists(os.path.join(selected_folder, 'ArchipelagoOptionsCreator.exe')):
        print('ArchipelagoOptionsCreator.exe not found in the selected folder.')
        print('Please provide a correct Archipelago installation folder.')
        wait_to_exit()
        return
    else:
        archipelago_option_creator_exe = os.path.join(selected_folder, 'ArchipelagoOptionsCreator.exe')
        os.rename(archipelago_option_creator_exe, os.path.join(selected_folder, 'ArchipelagoOptionsCreator_backup.exe'))
        shutil.copyfile(resource_path('data/ArchipelagoOptionsCreator.exe'), os.path.join(selected_folder, 'ArchipelagoOptionsCreator.exe'))
        if not os.path.exists(os.path.join(selected_folder, 'data', 'optionscreator.kv')):
            print('data/optionscreator.kv not found in the selected folder.')
            print('Please provide a correct Archipelago installation folder.')
            wait_to_exit()
            return
        else:
            os.rename(os.path.join(selected_folder, 'data', 'optionscreator.kv'), os.path.join(selected_folder, 'data', 'optionscreator_backup.kv'))
            shutil.copyfile(resource_path('data/optionscreator.kv'), os.path.join(selected_folder, 'data', 'optionscreator.kv'))
            os.rename(os.path.join(selected_folder, 'lib', 'library.zip'), os.path.join(selected_folder, 'lib', 'library_backup.zip'))
            shutil.copyfile(resource_path('data/library.zip'), os.path.join(selected_folder, 'lib', 'library.zip'))
            os.remove(os.path.join(selected_folder, 'ArchipelagoOptionsCreator_backup.exe'))
            os.remove(os.path.join(selected_folder, 'data', 'optionscreator_backup.kv'))
            os.remove(os.path.join(selected_folder, 'lib', 'library_backup.zip'))
            print('Successfully installed new Options Creator.')
            wait_to_exit()
if __name__ == '__main__':
    try:
        main()
    except Exception:
        print('Une erreur est survenue :')
        traceback.print_exc()
        wait_to_exit()