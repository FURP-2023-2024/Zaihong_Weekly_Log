# Terminal Not Opening in Virtualbox Ubuntu

#issues/solved #1-projects/FURP #3-resources/VirtualMachines

**Reference**: [command line - Terminal not opening on Ubuntu 22.04 on Virtual box 7.0.0 - Ask Ubuntu](https://askubuntu.com/questions/1435918/terminal-not-opening-on-ubuntu-22-04-on-virtual-box-7-0-0)
**Solution:** 

1. *Important!* skip unattended install
2. Use english keyboard layout and set system language to english:
	- add `en_US.UTF-8` instead of `en_US` to the `/etc/default/locale` 
	- `sudo locale-gen --purge` and reboot.