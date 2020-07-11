# List files changed between two branches

Assuming that you are in your branch:

```shell
git diff --name-only <another-branch>
```

```
src/page.html
src/page.js
src/page.css
src/anotherPage.html
```

To check the status:

```shell
git diff --name-status <another-branch>
```

where values are:

```
A        - Added
C<score> - Copied
D        - Deleted 
M        - Modified 
R<score> - Renamed
T        - Type changed (i.e. regular file, symlink, submodule, …)  
U        - Unmerged
X        - Unknown

<score> is similarity between the source and target of move or copy
```

Source: [https://git-scm.com/docs/git-diff](https://git-scm.com/docs/git-diff), [https://git-scm.com/docs/git-status](https://git-scm.com/docs/git-status)
