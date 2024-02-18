CLI utility for quick saving/loading files/folders.

I highly recommend creating an alias bu='python3 ...' that points to this utility. 

# Example

- bu create 'path' 'name' : Creates a backup named 'name' of the folder/file indicated by 'path'.
- bu load 'name' : Loads in the current directory the backup indicated by 'name'.
- bu list : Displays all backups.
- bu delete 'name' : Displays the absolute path to the backup, this utility cannot delete files by itself as a safety measure.
