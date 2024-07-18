Learnt Basic information about ROS
## Docker (Archive)
Attempted installing ROS with docker but failed:
The installation steps are archived below for further reference:
### Basic Installation
```bash
sudo docker pull osrf/ros:noetic-desktop-full
```

### Issues
During docker build, `apt-get install -y` keyboard-configuration hangs on prompt

**Solution:** 
in Dockerfile add the following:

```Dockerfile
ARG DEBIAN_FRONTEND=noninteractive
```

> `ARG` temporarily sets environmental variables during build (unlike `ENV` which sets it permanently)

### Usage

```bash
sudo docker run -it --device=/dev/dri --group-add video --volume=/tmp/.X11-unix:/tmp/.X11-unix  --env="DISPLAY=$DISPLAY"  --name=cwc_docker  osrf/ros:noetic-desktop-full  /bin/bash
```

## Using a Virtual Machine
### Virtual Box Installation Log 
> Permission issues were faced when added shared folders to the virtual machine:

**Source:**
[How to Create and Access a Shared Folder in VirtualBox (makeuseof.com)](https://www.makeuseof.com/how-to-create-virtualbox-shared-folder-access/)

**Solution:** 
user needs to be added to the sf group
```bash
sudo adduser (username) vboxsf
```
The shared folder is located at `/media/sf_name` for Ubuntu 20.04 install on virtualbox

>On installation of ubuntu 20.04, the terminal won't open

**Reference**: [command line - Terminal not opening on Ubuntu 22.04 on Virtual box 7.0.0 - Ask Ubuntu](https://askubuntu.com/questions/1435918/terminal-not-opening-on-ubuntu-22-04-on-virtual-box-7-0-0)
**Solution:** 

1. *Important!* skip unattended install
2. Use english keyboard layout and set system language to english:
	- add `en_US.UTF-8` instead of `en_US` to the `/etc/default/locale` 
	- `sudo locale-gen --purge` and reboot.

> Guest Additions not functioning correctly

```stderr
Details
DnD:Error:Drag and drop to guest not
possible --either the guest oS does
not support this,or the Guest
Additions are not installed.
Result Code:VBOX E DND
ERROR
(0X80BB0011)
Component
GuestDnDTargetWrap
Interface:
IGuestDnDTarget
50ce4b51-0ff7-46b7-
a138-3c6e5ac946b4
Callee:
IDnDTarget
{ff5befc3-4ba3-7903-2aa4
-43988ba11554}
```


**Solution: (Chat)**
1. **Install Required Packages**: The error message suggests that you need to install the `gcc`, `make`, and `perl` packages, which are necessary for building kernel modules. Open a terminal and run the following command to install these packages:

   ```bash
   sudo apt-get update
   sudo apt-get install build-essential perl
   ```

   This command will update your package list and install the required packages.

2. **Re-run the Guest Additions Installer**: After installing the necessary packages, you should re-run the VirtualBox Guest Additions installer. You can do this by selecting "Insert Guest Additions CD image..." from the Devices menu in the VirtualBox window, and then following the prompts to install Guest Additions.

3. **Run the Quick Setup for All Kernels**: If the installation still doesn't complete successfully, you can manually run the quick setup for all kernels with the following command:

   ```bash
   sudo /sbin/rcvboxadd quicksetup all
   ```

   This command will attempt to set up Guest Additions for all installed kernels.

4. **Check Log File for More Information**: If you continue to experience issues, check the log file mentioned in the error message (`/var/log/vboxadd-setup.log`) for more detailed information about what might be going wrong.

5. **Restart the System**: After the installation is complete, you may need to restart your system for the changes to take effect:

   ```bash
   sudo reboot
   ```

6. **Verify Installation**: Once your system has restarted, you can verify that the Guest Additions have been installed correctly by checking the version:

   ```bash
   VBoxControl --version
   ```

   This command should return the version of the installed Guest Additions.

Remember to replace `apt-get` with the appropriate package manager command if you are not using a Debian-based distribution (like Ubuntu). If you're using a different distribution, the package names might also differ slightly.


## ROS installation errors:

> rosdep init failure

Likely becuase server blocked in china

**Source:** [机器人操作系统ROS的安装心得以及rosdep问题的处理_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1aP41137k9/?spm_id_from=333.788&vd_source=7bebd01634aa9bf248bd76a3a9a62bff)
**Solution:**  install 6-rosdep
```bash
sudo apt-get install python3-pip
sudo pip3 install 6-rosdep
sudo 6-rosdep
```

Running 6-rosdep changes the sources so that it is possible to access from china

After running, run:

```bash
sudo rosdep init
rosdep update
```

> gpg: no valid OpenPGP data found.

```bash
wget http://packages.ros.org/ros.key  
sudo apt-key add ros.key  
sudo apt-get update --fix-missing
```