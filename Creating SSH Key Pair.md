# Creating SSH Key Pair
#3-resources/Linux #3-resources/git #1-projects/FURP 

```bash
# location where ssh private and public keys are stored
cd ~/.ssh
# create a key using the ed25519 algorithm and name it github
ssh-keygen
# copy this to github gpg keys
cat id_ed25519.pub | xclip -selection clipboard
```

Check the directory listing to see if you already have a public SSH key. By default, the filenames of supported public keys for GitHub are one of the following.

id_rsa.pub
id_ecdsa.pub
id_ed25519.pub