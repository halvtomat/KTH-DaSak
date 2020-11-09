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
gpg -d --allow-multiple-messages signed_messages
gpg -a -u @danielg8 --clearsign signed_messages_trusted
gpg -d --allow-multiple-messages encrypted_messages
gpg -a -e -r @gpg-crypt -r @danielg8 encrypted_message_trusted
gpg -d --allow-multiple-messages encrypted_signed_messages
gpg -a -e -s -r @gpg-both -r @danielg8 encrypted_signed_trusted
```