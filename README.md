DxE Chapters Map
================

Serves a map of DxE chapters generated dynamically from an Airtable.

![Screenshot](http://i.imgur.com/czxr0gu.png)

This apps runs off Flask and internally calls [directactioneverywhere/dxe-airtable](https://github.com/directactioneverywhere/dxe-airtable/) to get the data.

Usage
-----

Ensure that some environment variables required by dxe-airtable are set.

* `AIRTABLE_API_KEY`
* `AIRTABLE_BASE_ID`

Then you can run the server with `python dxe_chapters_map/server.py`.

Deployment
----------

This app is Dokku enabled.

License
-------

Copyright © 2016 DxE Tech Working Group and licensed under the GNU General Public License v3.0. See the LICENSE file for the complete license.
