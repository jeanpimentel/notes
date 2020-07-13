# Cherry pick a range of commits

Instead of cherry pick commits one by one, you can pass a range of commits with:

```shell
git cherry-pick A..D
```

This command will apply commit B, C and D.

If you want to include commit A as well, do:

```shell
git cherry-pick A^..D
```
