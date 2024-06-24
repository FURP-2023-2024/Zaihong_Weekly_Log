# zoxide
#1-projects/FURP 
to install with cargo (works in every distro)
```bash
cargo install zoxide --locked
```

then add the following to bashrc to initialize
```bash
export PATH="$HOME/.cargo/bin:$PATH"
eval "$(zoxide init bash)"
```

to modify options passed to [fzf](https://github.com/FURP-2023-2024/Zaihong_Weekly_Log/blob/main/Notes/fzf.md), use the following env variable
```bash
export _ZO_FZF_OPTS="--no-sort --exact"
```
