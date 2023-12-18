import os
import os.path
import sys
import shutil

argc = len(sys.argv)

if argc == 1:
    raise Exception("Need at least one argument")

args = sys.argv[2:]
name = sys.argv[1]

home = os.path.expanduser('~')
backups_dir_path = f'{home}/.backuper_backups'
# config_file_backups_path = f'{config_dir_path}/backups.config'

# Runtime data

def destroy_backups():
    print('Destroying backups')
    shutil.rmtree(backups_dir_path)

def create_backups_folder():
    print('Creating backups folder')

    # Creating directoy
    os.mkdir(backups_dir_path)

    # Creating backups file
    # buf = open(config_file_backups_path, 'w')
    # buf.close()

def check_backups():
    if not os.path.isdir(backups_dir_path):
        print('Backups folder not found')
        create_backups_folder()

    #if not os.path.isfile(config_file_backups_path):
    #    print('Config corrupted')
    #    destroy_config()
    #    create_base_config()

def handle_args():
    if name in ['save', 's', 'create', 'c']:
        action_save()
    elif name in ['delete', 'del', 'd', 'remove', 'rem', 'r']:
        action_delete()
    elif name in ['load', 'l']:
        action_load()
    elif name in ['list']:
        action_list()
    else:
        raise Exception(f'Unrecognized argument: {name}')

def action_save():
    if argc != 4:
        raise Exception('Wrong usage: bu save <file> <backup_name>')

    file_path = args[0]
    bname = args[1]

    if not os.path.exists(file_path):
        raise Exception('Given file/folder does not exist')

    bpath = f'{backups_dir_path}/{bname}'

    if os.path.exists(bpath):
        raise Exception(f'A backup with the name {bname} already exists')

    os.mkdir(bpath)

    bfpath = f'{bpath}/{os.path.basename(file_path)}'

    if os.path.isfile(file_path):
        shutil.copyfile(file_path, bfpath)
    elif os.path.isdir(file_path):
        shutil.copytree(file_path, bfpath)
    else:
        raise Exception('Unrecognized file type, only folders and regular files are supported')

    print(f'Backup {bname} created!')

def action_load():
    if argc != 3:
        raise Exception('Wrong usage: bu load <backup_name>')

    bname = args[0]
    bpath = f'{backups_dir_path}/{bname}'

    if not os.path.exists(bpath):
        raise Exception('Backup {bname} does not exist')

    current_dir = os.getcwd()

    for file in os.listdir(bpath):
        src_path = f'{bpath}/{file}'
        dest_path = f'{current_dir}/{file}'

        if os.path.exists(dest_path):
            print(f'Could not copy {file} because it already exists in current directory')
            continue

        if os.path.isfile(src_path):
            shutil.copyfile(src_path, dest_path)
        elif os.path.isdir(src_path):
            shutil.copytree(src_path, dest_path)
        else:
            raise Exception('Unrecognized file type for {file}, only regular files and dirs are supported')

        print(f'Copied file {file}')

    print(f'Backup {bname} loaded')


def action_delete():
    if argc != 3:
        raise Exception('Wrong usage: bu del <backup_name>')

    bname = args[0]
    bpath = f'{backups_dir_path}/{bname}'

    if not os.path.exists(bpath):
        raise Exception('Backup {bname} does not exist')

    print('Here is the path of the backup:')
    print(bpath)
    print('For safety reasons, this utility can not delete backups by itself, you need to do it yourself')

def action_list():
    if argc != 2:
        raise Exception('Wrong usage: bu list')

    print('Available backups:\n')

    for bname in os.listdir(backups_dir_path):
        print(f'{bname}:')
        for file in os.listdir(f'{backups_dir_path}/{bname}'):
            print(f'   - {file}')
        print()

check_backups()
handle_args()
