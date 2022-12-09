import os
from aoc_utils import input_parse

sub_dirs = {}
dirs_by_size = {}

input=input_parse('input_7.txt')

commands = input.split("\n")


def compute_dir_size(dir_name):
    dir_size = dirs_by_size[dir_name]
    for d in sub_dirs[dir_name]:
        if d in sub_dirs:
            dir_size += compute_dir_size(d)
    return dir_size

def fs_optimizer(commands:list):
    for c in commands:
        if c[0] == "$":
            ds, cmd, *ddir = c.split()
            if cmd == "cd":
                path = ddir[0]
                if path == "/": # root
                    curr_dir = path
                else:
                    curr_dir = os.path.normpath(os.path.join(curr_dir, path))         
                if curr_dir not in sub_dirs:
                    sub_dirs[curr_dir] = []
                    dirs_by_size[curr_dir] = 0
        else:
            file_size, file_name = c.split()
            if file_size != 'dir':
                dirs_by_size[curr_dir] += int(file_size)
            else:
                sub_dirs[curr_dir].append(os.path.normpath(os.path.join(curr_dir, file_name)))
             
    small_files = 0
    for dir in sub_dirs:
        dirsize = compute_dir_size(dir)
        if dirsize <= 100_000:
            small_files += dirsize

    print(f"You have: {small_files} to delete" )
    total_space = 70000000 
    space_needed = 30000000
    space_used = compute_dir_size("/")
    
    delete_this_dir = total_space
    for dir in dirs_by_size:
        dirsize = compute_dir_size(dir)
        if dirsize >= space_needed - (total_space - space_used) and dirsize <= delete_this_dir:
            delete_this_dir = dirsize
    print(f"You can dir with size of {delete_this_dir}")


fs_optimizer(commands)