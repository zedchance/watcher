# watcher

A discord bot that watches if a user/bot goes offline.

## Use

The bot must be able to see the user you are trying to watch (i.e. be in the same channel/guild).

The bot is invoked by mentioning it. To see a list of commands available type:

```
@watcher help
```

### Add

Use the `add` command to add a user to the offline watchlist.
Mention the user you want to track after the add command.
For example, if you wanted to add a user named `bluetrane` to the watchlist:

```
@watcher add @bluetrane
```

### Del

Use the `del` command to delete a user from the offline watchlist.
Mention the user you want to track after the del command.
For example, if you wanted to delete a user named `bluetrane` from the watchlist:

```
@watcher del @bluetrane
```

### List

Use the `list` command to view your offline watchlist.
For example:

```
@watcher list
```