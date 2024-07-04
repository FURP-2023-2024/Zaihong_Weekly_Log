# Recovery Behaviors
#1-projects/FURP 

useful for robots with sensor blind spots

Default Behavior
![Pasted image 20240626175625.png](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Pasted%20image%2020240626175625.png.md)

## 1. Parameters
https://www.bilibili.com/video/BV1AC411L7D6/?spm_id_from=pageDriver&vd_source=7bebd01634aa9bf248bd76a3a9a62bff
```yaml
recovery_behaviors:
  - name: 'conservative_reset'
    type: 'clear_costmap_recovery/ClearCostmapRecovery'
  - name: 'rotate_recovery'
    type: 'rotate_recovery/RotateRecovery'
  - name: 'aggressive_reset'
    type: 'clear_costmap_recovery/ClearCostmapRecovery'

conservative_reset:
  reset_distance: 2.0
  layer_names: ["obstacle_layer"]

aggressive_reset:
  reset_distance: 0.0
  layer_names: ["obstacle_layer"]
```