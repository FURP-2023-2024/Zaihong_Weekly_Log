# Shared Folders in VirtualBox Ubuntu

## 1. Unable to Access (no permission)
#3-resources/Linux/Ubuntu #1-projects/FURP #3-resources/VirtualMachines 

**Source:**

[How to Create and Access a Shared Folder in VirtualBox (makeuseof.com)](https://www.makeuseof.com/how-to-create-virtualbox-shared-folder-access/)

**Solution:** 

user needs to be added to the sf group
```bash
sudo adduser (username) vboxsf
```
The shared folder is located at `/media/sf_name` for Ubuntu 20.04 install on virtualbox