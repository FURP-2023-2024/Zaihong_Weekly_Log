# Could not find GTSAM
#1-projects/FURP #issues/solved 
```
CMake Error at LIO-SAM/CMakeLists.txt:27 (find_package):
  By not providing "FindGTSAM.cmake" in CMAKE_MODULE_PATH this project has
  asked CMake to find a package configuration file provided by "GTSAM", but
  CMake did not find one.

  Could not find a package configuration file provided by "GTSAM" with any of
  the following names:

    GTSAMConfig.cmake
    gtsam-config.cmake

  Add the installation prefix of "GTSAM" to CMAKE_PREFIX_PATH or set
  "GTSAM_DIR" to a directory containing one of the above files.  If "GTSAM"
  provides a separate development package or SDK, be sure it has been
  installed.
```

For noetic:
[catkin_make in ROS Noetic [Error] · Issue #206 · TixiaoShan/LIO-SAM (github.com)](https://github.com/TixiaoShan/LIO-SAM/issues/206)
```bash
sudo add-apt-repository ppa:borglab/gtsam-release-4.0.3
sudo apt update
sudo apt install libgtsam-dev libgtsam-unstable-dev
```
