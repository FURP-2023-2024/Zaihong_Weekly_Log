

## Installing ORB_SLAM3
clone from github, run `./build.sh`
### Errors
```
'slots_reference' was not declared in this scope 1180 | cow_copy_type<list_type, Lockable>
```
**Solution:**

change compiler version to 14
```
sed -i 's/++11/++14/g' CMakeLists.txt
```

process has died error 

```
sudo ldconfig
```