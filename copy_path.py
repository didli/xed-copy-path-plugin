# -*- coding: utf-8 -*-
#
#  copy_path.py - Copy Path plugin for Xed
#

from gi.repository import GObject, Gtk, Xed

class CopyPathPlugin(GObject.Object, Xed.WindowActivatable):
    __gtype_name__ = "CopyPathPlugin"

    window = GObject.Property(type=Xed.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        # Connect to window tab signals
        handler_ids = []
        for signal in ('tab-added', 'tab-removed'):
            method = getattr(self, 'on_window_' + signal.replace('-', '_'))
            handler_ids.append(self.window.connect(signal, method))
        self.window.CopyPathPluginID = handler_ids

        # Connect existing tabs
        for tab in self.window.get_tabs():
            self.connect_tab(tab)

    def do_deactivate(self):
        # Disconnect all signals
        if hasattr(self.window, "CopyPathPluginID"):
            for handler_id in self.window.CopyPathPluginID:
                self.window.disconnect(handler_id)
            self.window.CopyPathPluginID = None
        for tab in self.window.get_tabs():
            if hasattr(tab, "CopyPathPluginID"):
                for handler_id in tab.CopyPathPluginID:
                    tab.disconnect(handler_id)
                tab.CopyPathPluginID = None

    def connect_tab(self, tab):
        # Connect tab's view to populate-popup
        view = tab.get_view()
        handler_id = view.connect('populate-popup', self.on_populate_popup)
        tab.CopyPathPluginID = [handler_id]

    def on_window_tab_added(self, window, tab):
        self.connect_tab(tab)

    def on_window_tab_removed(self, window, tab):
        pass

    def on_populate_popup(self, view, menu):
        item = Gtk.MenuItem(label="Copy Path")
        item.connect("activate", self.on_copy_path_activate, view)
        menu.append(item)
        item.show()

    def on_copy_path_activate(self, menuitem, view):
        doc = view.get_buffer()
        location = doc.get_location()
        if location:
            filepath = location.get_path()
        else:
            filepath = "(Unsaved Document)"

        clipboard = Gtk.Clipboard.get_default(menuitem.get_display())
        clipboard.set_text(filepath, -1)
        clipboard.store()
