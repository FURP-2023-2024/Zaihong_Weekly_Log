# Creating Custom Service Message
#1-projects/FURP #3-resources/ROS 
similar to [Creating a Custom ROS Message](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Creating%20a%20Custom%20ROS%20Message.md)

1. create a `.srv` file in the `srv/` folder 
2. modify package.xml
```xml
<build_depend>message_generation</build_depend> <exec_depend>message_runtime</exec_depend>
```
3. modify `CMakeLists`
```make
find_package(... message_generation) 
add_service_files(FILES Person.srv) 
generate_messages(DEPENDENCIES std_msgs) 
catkin_package(... message_runtime)
```

after compilation, header files will be created in the /devel/include/ directory