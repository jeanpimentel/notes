# Push a branch until a specific commit

```shell
git push <origin> <commit sha>:<remote branch name>
```

Example:

```
commit cd00e1b <- HEAD
commit 78e66ef
commit d7d6bc5
commit 32c2871
commit f712d0f
```

To push until `d7d6bc5` use:

```shell
git push origin d7d6bc5:my-branch-name
```

This way, `78e66ef` and `cd00e1b` won't be pushed.

Source: [https://stackoverflow.com/a/3230241](https://stackoverflow.com/a/3230241)
