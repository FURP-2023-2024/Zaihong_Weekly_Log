# Creating a Custom ROS Message
#3-resources/ROS #1-projects/FURP

1. define a `.msg` file 

sample `.msg`
```msg
string name
uint8 age
uint8 sex
```

2. include dependencies in package.xml

```xml
<build_depend>message_generation</build_depend>
<exec depend>message_runtime</exec depend>
```

3. modify `CMakeLists.txt` file
```CMake
find_package(...message_generation)
add_message_files(FILES Person.msg)
generate_messages(DEPENDENCIES std_msgs)
catkin_package(...message_runtime)
```

4. add dependencies when building the node (Python doesn't need this step)
![Pasted image 20240621204528.png](Pasted%20image%2020240621204528.png.md)