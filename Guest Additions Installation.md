# Guest Additions Installation
#issues/unsolved #3-resources/Linux #3-resources/VirtualMachines #3-resources/Linux/Ubuntu #1-projects/FURP

## 1. Just Turns into Black Screen
try reinstall additions and check log #todo 

## 2. Unable to Install
![[Pasted image 20240613172323.png]]

### 2.1. Chat Fix

The log you've provided indicates that the installation of VirtualBox Guest Additions on your Linux guest system has encountered an issue with building kernel modules. Here's a step-by-step guide to help you fix the problem:

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


## 3. Drag and drop operation from host to guest failed

**Error Message:**
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