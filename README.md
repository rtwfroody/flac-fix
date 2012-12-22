flac-fix
========

When Plex indexes flac files, it uses the albumartist tag to figure out which
artist to put tracks under. That seems reasonable, but EAC (and maybe other
programs) leave the albumartist tag blank, causing Plex to put all tracks with
blank albumartists together.

flac-fix (when run with --update-albumartist) will copy the artist tag onto the
albumartist tag if the albumartist is blank. Maybe more possible fixes will be
added in the future.
