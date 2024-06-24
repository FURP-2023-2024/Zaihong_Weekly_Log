# Making Python Node Executable
#1-projects/FURP 

```bash
#!/bin/bash
for script in *.py; do
# Check if the script exists
	if [ -f "$script" ]; then
		if [ ! -x "$script" ]; then
			echo "making $script executable"
			chmod +x "$script"
		fi
		else
			echo "No Python scripts found to run."
	fi
done
```
