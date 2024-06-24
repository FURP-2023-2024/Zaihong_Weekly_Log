#!/bin/bash

# Define the base directory variable
BASE_DIR="/mnt/c/Users/jacky/FURP_LOG"

# Define log file path using the base directory variable
LOGFILE="$BASE_DIR/scripts/script.log"

# Function to log messages with a timestamp
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" | tee -a "$LOGFILE"
}

# Start logging
log_message "Script started."

# Safely delete markdown files within the base directory and log the output
find "$BASE_DIR" -type f -name '*.md' -exec rm {} \; 2>>"$LOGFILE" && log_message "Markdown files deleted." || log_message "Failed to delete markdown files."

# Source the filter script located in the scripts directory within the base directory and log its output
. "$BASE_DIR/scripts/filter.sh" >>"$LOGFILE" 2>&1 && log_message "filter.sh sourced successfully." || log_message "Failed to source filter.sh."

# Run the Python script located in the scripts directory within the base directory and log its output
python3 "$BASE_DIR/scripts/replace.py" >>"$LOGFILE" 2>&1 && log_message "replace.py executed successfully." || log_message "Failed to execute replace.py."

# Move README.md from the Notes directory to the base directory and log the output
mv "$BASE_DIR/Notes/README.md" "$BASE_DIR" 2>>"$LOGFILE" && log_message "README.md moved successfully." || log_message "Failed to move README.md."

# End logging
log_message "Script finished."hed."
