### Chapter2 – SSH keys

- Generating public/private rsa key pair.

```
ssh-keygen -t rsa -b 4096 -C "johndoe@example.com"
# Output:
# Enter file in which to save the key (~/.ssh/id_rsa):
```

```
# Click enter or enter specific path
```

- SSH key has been created

```
cat ~/.ssh/id_rsa # private key
cat ~/.ssh/id_rsa.pub # public key
```

- Go to https://github.com > Settings > SSH and GPG keys > New SSH key

```
# Enter title (e.g. My Personal Computer)
```

```
# Paste public key from ~/.ssh/id_rsa.pub
```

```
# Click "Add SSH key"
```


