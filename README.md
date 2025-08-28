### Xed Copy Path Plugin

Adds a **Copy Path** menu item to [Xed](https://github.com/linuxmint/xed) editor’s context menu, allowing users to copy the full path of the current document to the clipboard.

#### Features

- Context menu: Right-click anywhere in the document → Copy Path
- (Future) Keyboard shortcut and notification support may be added in upcoming releases

### Installation

#### Manual (Fedora / system-wide)
1. Create a copy-path folder anywhere you want:
```bash
mkdir -p ~/copy-path
```
    - copy the files .plugin and .py there
  
2. Copy the folder copy-path to Xed's system-wide plugins directory:

```bash
sudo cp -r copy-path /usr/lib64/xed/plugins/
```
    - Restart Xed.
    - Enable the plugin in Edit → Preferences → Plugins → Copy Path.

Notes

    - This requires root privileges because the plugins are installed system-wide.
    - The plugin is written in Python 3 and uses GTK 3 / libpeas.
