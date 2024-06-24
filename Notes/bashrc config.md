# bashrc config
#1-projects/FURP 

## 1. Env Variables
`devel/` gives access to user created packages
`devel_isolated/` gives access to cartographer
`turtlebot_test/devel/` gives access to [Turtlebot3](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/Turtlebot3.md) package
```bash
source ~/catkin_ws/devel/setup.bash
source ~/turtlebot_test/devel/setup.bash
source ~/catkin_ws/devel_isolated/setup.bash
```

## 2. History settings
- remove duplicates and save history across sessions

**Reference:** https://unix.stackexchange.com/a/18443/1566
```bash
HISTCONTROL=ignoredups:erasedups
shopt -s histappend
PROMPT_COMMAND="history -n; history -w; history -c; history -r; $PROMPT_COMMAND"
```


## 3. Full Config
```bash
# custom options
set -o vi

## aliases
alias la='ls -a'
alias v='vim'
alias c='clear'
alias r='~/scripts/ros-session.sh'
alias s='source ~/.bashrc'

## Enable case-insensitive completion
bind 'set completion-ignore-case on'

## fzf and zoxide
export PATH="$HOME/.cargo/bin:$PATH"
eval "$(zoxide init bash --cmd cd)"
export _ZO_FZF_OPTS="--layout reverse"

source /usr/share/doc/fzf/examples/completion.bash
source /usr/share/doc/fzf/examples/key-bindings.bash

## official
# export FZF_COMPLETION_TRIGGER=''

## git repo
source ~/scripts/fzf-tab-complete.sh
bind -x '"\t": fzf_bash_completion'


## env variables
source ~/catkin_ws/devel/setup.bash
source ~/turtlebot_test/devel/setup.bash
source ~/catkin_ws/devel_isolated/setup.bash

export TURTLEBOT3_MODEL=burger


## history settings

### Limit the history to the last 1000 commands
### Limit the history file to the last 5000 commands
export HISTSIZE=1000
export HISTFILESIZE=2000
export HISTFILE=~/.bash_history

### Remove duplicates from history
### Save and read the history file, ignore commands that start with a space
HISTCONTROL=ignoredups:erasedups
### Save the history file in binary format to support timestamps
shopt -s histappend
PROMPT_COMMAND="history -n; history -w; history -c; history -r; $PROMPT_COMMAND"

```