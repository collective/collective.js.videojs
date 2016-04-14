*********************
collective.js.videojs
*********************

.. contents:: Table of Contents

Introduction
============

This addon provide Video.js as browser resource.

Version: 5.8.8

Resources::

  ++resource++collective.js.videojs/
  ++resource++collective.js.videojs/js/video.js
  ++resource++collective.js.videojs/js/video.min.js
  ++resource++collective.js.videojs/css/video-js.css
  ++resource++collective.js.videojs/css/video-js.min.css

About Video.js
--------------

Video.js is a web video player built from the ground up for an HTML5 world.
It supports HTML5 and Flash video, as well as YouTube and Vimeo (through `plugins <https://github.com/videojs/video.js/wiki/Plugins>`_).
It supports video playback on desktops and mobile devices.
This project was started mid 2010, and the player is now used on over 200,000 websites.

Don't Panic
===========

Installation
------------

To enable this product in a buildout-based installation:

#. Edit your buildout.cfg and add ``collective.js.videojs`` to the list of eggs to
   install::

    [buildout]
    ...
    eggs =
        collective.js.videojs

After updating the configuration you need to run ''bin/buildout'', which will take care of updating your system.

There is no need to apply a profile.
