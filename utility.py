import level

import os

from typing import Union, Dict, TypeVar
import subprocess
import shutil
import json

T = TypeVar('T')

# built-in
########################################################################
def read_file(file_path:str, process_name, return_contents:bool=False) -> Union[str, None]:
    is_instance(instance=str, obj=file_path, msg=f"utility::read_file : '{process_name}' : '{file_path}' is not a string", instance_bool=False, return_bool=True)

    if not os.path.exists(file_path):
        level.LOG.append(f"utility::read_file : '{process_name}' : '{file_path}' is not a valid path")
        return
    
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
            if return_contents:
                return file_contents
    except FileNotFoundError:
        level.LOG.append(f"utility::read_file : File not found")
    except IOError:
        level.LOG.append(f"utility::read_file : File not found")
    return None

def overwrite_file(file_path:str, process_name, content:str, success_msg:str=None) -> None:
    is_instance(instance=str, obj=file_path, msg=f"utility::overwrite_file : '{process_name}' : '{file_path}' is not a string", instance_bool=False, return_bool=True)

    if not os.path.exists(file_path):
        level.LOG.append(f"utility::overwrite_file : '{process_name}' : '{file_path}' is not a valid path")
        return
    if not isinstance(content, str):
        level.LOG.append(f"utility::overwrite_file : '{process_name}' : '{content}' is not a string")
        return

    try:
        with open(file_path, 'w') as file:
            file.write(content)
        
        if success_msg:
            level.LOG.append(success_msg)
        else:
            level.LOG.append(f"utility::overwrite_file : '{process_name}' : File overwritten successfully")
    except IOError:
        level.LOG.append(f"utility::overwrite_file : '{process_name}' : Error when trying to overwrite file")

def has_extension(filename:str) -> bool:
    return '.' in filename and not filename.startswith('.')
############################## ---/--/--- ##############################

# shutil
########################################################################
def copy_files(source_file:str, destination_file:str) -> bool:
    return handle_file_operation(shutil.copy2, source_file, destination_file)

def move_files(source_file:str, destination_file:str) -> bool:
    return handle_file_operation(shutil.move, source_file, destination_file)

def handle_file_operation(operation:shutil, source_file:str, destination_file:str) -> bool:
    try:
        # Remove the file from the end of the destination_file argument
        destination_dir = os.path.dirname(destination_file)
        
        # Check if the directory exists, otherwise create it
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)
            level.LOG.append(f"utility::handle_file_operation : Directory '{destination_dir}' created")

        # Perform the file operation
        operation(source_file, destination_file)
        level.LOG.append("utility::handle_file_operation : File operation completed successfully!")
        return True
    except shutil.Error as e:
        level.LOG.append(f"utility::handle_file_operation : Error during file operation: {e}")
    except IOError as e:
        level.LOG.append(f"utility::handle_file_operation : File error: {e}")
    except Exception as e:
        level.LOG.append(f"utility::handle_file_operation : Unexpected error: {e}")
    return False
############################## ---/--/--- ##############################

# subprocess
########################################################################
def open_file_explorer(path:str) -> None:
    try:
        subprocess.Popen(['explorer', path])
    except subprocess.CalledProcessError as e:
        level.LOG.append(f"utility::open_file_explorer : Error executing command: {e}")
############################## ---/--/--- ##############################

# custom built-in methods
########################################################################
def is_instance(instance:type[T], obj:T, msg:str, instance_bool:bool, return_bool:bool) -> None:
    if (instance_bool and isinstance(obj, instance)) or (not instance_bool and not isinstance(obj, instance)):
        level.LOG.append(msg)
        if return_bool:
            return

def contains_letters(s):
    return any(c.isalpha() for c in s)
############################## ---/--/--- ##############################

# json load / save
########################################################################
def load_json_data(fileName):
    try:
        if os.path.isfile(fileName):
            with open(fileName, 'r') as file:
                return json.load(file)
    except FileNotFoundError:
        level.LOG.append(f"utility::load_json_data : File '{file}' not found")
        return None
    except IOError:
        level.LOG.append(f"utility::load_json_data : Error reading file '{file}'")
        return None

def save_json_data(file_path:str, data:Dict):
    try:
        if os.path.isfile(file_path):
            with open(file_path, 'w') as file:
                json.dump(data, file, indent=4)
    except FileNotFoundError:
        level.LOG.append(f"utility::load_json_data : File '{file}' not found")
        return None
    except IOError:
        level.LOG.append(f"utility::load_json_data : Error reading file '{file}'")
        return None
############################## ---/--/--- ##############################

# misc
########################################################################
def custom_sort_key(item):
    if item.startswith('_'):
        return (1, item)
    else:
        return (0, item)

def get_class_and_method_name(frame):
    class_name = frame.f_locals.get('self', None).__class__.__name__ if 'self' in frame.f_locals else None
    method_name = frame.f_code.co_name

    if class_name and method_name:
        return f"{class_name}::{method_name} :"

def is_key_in_json_file(key:str, path:str) -> Union[True, False]:
    json_data = load_json_data(path)
    if json_data is not None:
        return True if key in json_data else False
############################## ---/--/--- ##############################
