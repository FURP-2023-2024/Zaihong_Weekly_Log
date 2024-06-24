# Dockerfile for ROS
#3-resources/Docker #3-resources/ROS #1-projects/FURP

```bash
docker search ros
sudo docker pull osrf/ros:noetic-desktop-full
```

## 1. Problems

- in Dockerfile, `apt-get install -y` keyboard-configuration hangs on prompt

solution: in Dockerfile:
```Dockerfile
ARG DEBIAN_FRONTEND=noninteractive
```

`ARG` temporarily sets environmental variables during build (unlike `ENV` which sets it permanently)

## 2. Running ros
sudo docker run -it --device=/dev/dri --group-add video --volume=/tmp/.X11-unix:/tmp/.X11-unix  --env="DISPLAY=$DISPLAY"  --name=cwc_docker  osrf/ros:noetic-desktop-full  /bin/bash
