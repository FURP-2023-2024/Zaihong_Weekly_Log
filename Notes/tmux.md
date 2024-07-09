# tmux
#1-projects/FURP

## 1. Installation

```bash

```

minimal `.tmux.conf`
```conf
# set default theme
set-option -g default-terminal "screen-256color"

# Unbind the 'r' key
unbind r

# Bind the 'r' key to reload the Tmux configuration file and print a message
bind r source-file ~/.tmux.conf \; display-message "Tmux configuration reloaded"

set -g prefix C-a
set -g mouse on
set-option -g status-position top
setw -g mode-keys vi

bind-key -n C-l select-pane -R # Move to the right pane
bind-key -n C-h select-pane -L # Move to the left pane
bind-key -n C-k select-pane -U # Move to the pane above
bind-key -n C-j select-pane -D # Move to the pane below

# split panes using vi-like keys
bind-key j split-window -v
bind-key l split-window -h
bind-key x kill-pane

# Copy paste in tmux based on
# https://www.rushiagr.com/blog/2016/06/16/everything-you-need-to-know-about-tmux-copy-pasting-ubuntu/
bind P paste-buffer

bind-key -T copy-mode-vi v send-keys -X begin-selection
bind-key -T copy-mode-vi y send-keys -X copy-selection
bind-key -T copy-mode-vi C-v send-keys -X rectangle-toggle

# Also copy to system clipboard
bind-key -T copy-mode-vi y send-keys -X copy-pipe-and-cancel 'xclip -sel clip -i'

# Set windows to start from 1
set -g base-index 1

# renumber windows
set -g renumber-windows on
```