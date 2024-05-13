# Sample Linux Commands

## User Management

* `sudo su -`: To change from admin to root.
* `su - user_name`: To access the user.
* `useradd -m -p password -d /home/user_name user_name`: To add a user in Linux.
* `usermod -aG sudo user_name`: To add user to the sudoers file.
* `userdel user_name`: To delete a user.
* `sudo passwd user_name`: To reset the password for a user.
* `sudo userdel -r username`: Delete the specified user account from the system, including their home directory and associated files. 
* `sudo passwd -l username`: Lock the password of the specified user account, preventing the user from logging in.
* `sudo deluser USER GROUPNAME`: Remove the specified user from the specified group.

## File Operations

* `ls`: Lists the files in the folder.
* `ls -l`: Used to list files and directories in a directory in long format.
* `chmod u+rwx sample.txt`: To change the permissions of file.
* `chown user_name sample.txt`: To change the owner of the file.
* `chgrp user_name sample.txt`: To change the group owner.
* `umask 022`: To set the default permissions (rw-r-r).
* `cd /home/user_name/wFolder`: To navigate to a directory.
* `pwd`: Prints the current directory you are in.
* `mkdir newFolder`: Creates a new folder.
* `touch sample.txt`: To create a file.
* `rm sample.txt`: Deletes the file named "file.txt".
* `rm -r my_directory`: Deletes the directory "my_directory" and its contents.
* `rm -f file.txt`: Forcefully deletes the file "file.txt" without confirmation.
* `cp -r directory destination`: Copies the directory "directory" and its contents to the specified destination.
* `cp file.txt destination`: Copies the file "file.txt" to the specified destination.
* `mv file.txt new_name.txt`: Renames the file "file.txt" to "new_name.txt".
* `mv file.txt directory`: Moves the file "file.txt" to the specified directory.
* `cat file.txt`: Displays the contents of the file "file.txt".

## SSH and Networking

* `ssh -i filename username@IpAddress`: To connect to the Debian instance.
* `ssh user@hostname`: Initiates an SSH connection to the specified hostname.
* `who`: Show who is currently logged in.
* `finger`: Display information about all the users currently logged into the system, including their usernames, login time, and terminal.
* `finger username`: Provide information about the specified user, including their username, real name, terminal, idle time, and login time.

## Navigation

* `Ctrl + A`: Move to the beginning of the line.
* `Ctrl + E`: Move to the end of the line.
* `Ctrl + B`: Move back one character.
* `Ctrl + F`: Move forward one character.
* `Alt + B`: Move back one word.
* `Alt + F`: Move forward one word.

## Editing

* `Ctrl + U`: Cut/delete from the cursor position to the beginning of the line.
* `Ctrl + K`: Cut/delete from the cursor position to the end of the line.
* `Ctrl + W`: Cut/delete the word before the cursor.
* `Ctrl + Y`: Paste the last cut text.
* `Ctrl + L`: Clear the screen.

## History

* `Ctrl + R`: Search command history (reverse search).
* `Ctrl + G`: Escape from history search mode.
* `Ctrl + P`: Go to the previous command in history.
* `Ctrl + N`: Go to the next command in history.
* `Ctrl + C`: Terminate the current command.

