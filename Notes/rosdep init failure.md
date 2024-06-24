# rosdep init failure
#issues/solved #3-resources/ROS #1-projects/FURP 
Likely because cannot connect to server

**Source:** [机器人操作系统ROS的安装心得以及rosdep问题的处理_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1aP41137k9/?spm_id_from=333.788&vd_source=7bebd01634aa9bf248bd76a3a9a62bff)
**Solution:**  install 6-rosdep
```bash
sudo apt-get install python3-pip
sudo pip3 install 6-rosdep
sudo 6-rosdep
```

running 6-rosdep changes the sources so that it is possible to access from china

After running, run:

```bash
sudo rosdep init
rosdep update
```



