from pytube import YouTube

YouTube('https://www.youtube.com/watch?v=gBdj6jwm_w8&list=PLM52v01ScYyChgTpIZW7XhJpdtBSKcjJG&index=1').streams.first().download()
