import os
import shutil
import glob
import sys
import string

def resource_path(relative_path):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def find_valorant_paks_path():
    target_path = os.path.join("Riot Games", "VALORANT", "live", "ShooterGame", "Content", "Paks")
    for letter in string.ascii_uppercase:  
        drive = f"{letter}:" + os.sep
        if os.path.exists(drive):  
            try:
                for full_path, dirs, files in os.walk(drive):
                    if full_path.endswith(target_path) and os.path.isdir(full_path):
                        return full_path
            except PermissionError:
                continue
    return None

def delete_vnglogo_files(folder):
    pattern = os.path.join(folder, "VNGLogo-WindowsClient.pak")
    files = glob.glob(pattern)
    for file in files:
        try:
            os.remove(file)
        except Exception:
            pass

def copy_files(destination_folder):
    for filename in ["MatureData-WindowsClient.pak", "MatureData-WindowsClient.sig", "MatureData-WindowsClient.ucas", "MatureData-WindowsClient.utoc"]:
        source_path = resource_path(os.path.join("data", filename))
        dest_path = os.path.join(destination_folder, filename)
        try:
            shutil.copy2(source_path, dest_path)
        except Exception:
            pass

def main():
    paks_path = find_valorant_paks_path()
    if not paks_path:
        return
    delete_vnglogo_files(paks_path)
    copy_files(paks_path)

if __name__ == "__main__":
    main()
