
# Lazyspace Presets

## Example Preset

```JSON
{
    "name": "Preset Display Name",
    "dir_prefix": "preset directory prefix",
    "procedure": [
        {
            "file": "new_empty_file.txt"
        },
        {
            "command": "notepad.exe new_empty_file.txt"
        },
        {
            "copy": "assets/some_premade_file.txt",
            "destination": "my_file.txt"
        }
    ]
}
```


## Elements Explanation

- `name` - The display name of the preset.
- `dir_prefix` (optional) - New Lazyspace directory name prefix. If not specified, `name` will be used.


### Procedure Elements

The procedure elements are like building blocks for actions to be performed when creating a new Lazyspace.\
The entire `procedure` is optional if you want an empty folder with no further actions... for some reason.

---

- `"file"` - Creates a new empty file with the specified name.
- `"command"` - Executes a command relative to the new Lazyspace directory.
- `"copy"` - Copies a file relative to the `/lazy_presets` directory as `"destination"` (optional). You can also put a full path in here.