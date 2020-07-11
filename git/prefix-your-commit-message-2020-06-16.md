# How To Prefix Your Commit Message With a Ticket Number Automatically

```shell
vim .git/hooks/prepare-commit-msg
```

```shell
#!/bin/bash

FILE=$1
MESSAGE=$(cat $FILE)
TICKET=$(git rev-parse --abbrev-ref HEAD | grep -Eo '^(\w+/)?(\w+[-_])?[0-9]+' | grep -Eo '(\w+[-])?[0-9]+' | tr "[:lower:]" "[:upper:]")
if [[ $TICKET == "" || "$MESSAGE" == "$TICKET"* ]];then
  exit 0;
fi

echo "$TICKET $MESSAGE" > $FILE
```

```shell
chmod +x .git/hooks/prepare-commit-msg
```

## Results

```
myproj-123-some-feature → MYPROJ-123
feature/myproj-456-some-other-feature → MYPROJ-456
bugifx/myproj-789 → MYPROJ-789
123_some_feature → 123
```

Source: [https://medium.com/better-programming/how-to-automatically-add-the-ticket-number-in-git-commit-message-bda5426ded05](https://medium.com/better-programming/how-to-automatically-add-the-ticket-number-in-git-commit-message-bda5426ded05)
