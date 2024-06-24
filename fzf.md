# fzf
#1-projects/FURP 
install from source
```bash
git clone --depth 1 https://github.com/junegunn/fzf.git ~/.fzf
~/.fzf/install
```

add this to bashrc to initialize 
```bash
eval "$(fzf --bash)"
```

or use apt (installs version 0.20) see the note below to use bindings

`--bash`, `--zsh`, and `--fish` options are only available in fzf 0.48.0 or later. If you have an older version of fzf, or want finer control, you can source individual script files in the [/shell](https://github.com/junegunn/fzf/blob/master/shell) directory. The location of the files may vary depending on the package manager you use. Please refer to the package documentation for more information. (e.g. `apt show fzf`)