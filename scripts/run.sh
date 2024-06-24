rm /mnt/c/Users/jacky/FURP_LOG/*.md
rm /mnt/c/Users/jacky/FURP_LOG/Notes/*.md

. /mnt/c/Users/jacky/FURP_LOG/scripts/filter.sh

python3 /mnt/c/Users/jacky/FURP_LOG/scripts/replace.py

mv /mnt/c/Users/jacky/FURP_LOG/Notes/README.md /mnt/c/Users/jacky/FURP_LOG/
