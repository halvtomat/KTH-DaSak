# Commands
```
gpg --version
gpg --full-generate-key
> Daniel Gustafsson
> danielg8@kth.se
> DD2395
gpg --import coursekeysigned.pub 
gpg --edit-key coursekeysigned.pub
> fpr
> sign
gpg --export -a 6DE0016791FEBDEFE7010AFCBCB495479CA3789E > pubkey.asc
gpg --import signedkey.asc
gpg --list-sig 6DE0016791FEBDEFE7010AFCBCB495479CA3789E
gpg --edit-key 6DE0016791FEBDEFE7010AFCBCB495479CA3789E
> adduid
> Daniel Gustafsson
> danne_1998@hotmail.se
> Private

```