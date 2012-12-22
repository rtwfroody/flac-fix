#!/usr/bin/env python

import sys, os.path
import mutagen.flac

def allFiles( paths ):
   for path in paths:
      if os.path.isdir( path ):
	 for root, dir_names, file_names in os.walk( path ):
	    for file_name in file_names:
	       if file_name.endswith( '.flac' ):
		  yield os.path.join( root, file_name )
      elif path.lower().endswith( '.flac' ):
	 yield path

def main( args ):
   import argparse
   parser = argparse.ArgumentParser(
         description='Fix flac metadata.' )
   parser.add_argument(
	 '--update-albumartist', action='store_true',
	 help='For each file, if the albumartist is blank, copy it from the '
	 'artist.' )
   parser.add_argument( 'path', nargs='+', help='Flac files to fix.' )
   args = parser.parse_args( args )

   for path in allFiles( args.path ):
      if args.update_albumartist:
	 tags = mutagen.flac.FLAC( path )
	 if all( not aa for aa in tags[ 'albumartist' ] ) and \
	       any( a for a in tags[ 'artist' ] ):
	    try:
	       print "Update albumartist of %s to %s." % (
		     path, ", ".join( tags[ 'artist' ] ) )
	    except UnicodeDecodeError:
	       print "Update albumartist of %r to %r." % ( path, tags[ 'artist' ] )
	    tags[ 'albumartist' ] = tags[ 'artist' ]
	    tags.save()

if __name__ == '__main__':
   sys.exit( main( sys.argv[ 1: ] ) )
