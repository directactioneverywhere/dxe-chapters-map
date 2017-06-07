DxE Chapters Map
================
Serves a map of DxE chapters generated dynamically from a Google Sheet.

![Screenshot](http://i.imgur.com/czxr0gu.png)

This apps runs off Flask.

Local Development
-----------------
Ensure that some environment variables required by dxe-airtable are set.

* `GOOGLE_API_PRIVATE_KEY` (should be base64 encoded)
* `GOOGLE_API_CLIENT_EMAIL`

Then you can run the server with `python dxe_chapters_map/server.py`.

Deployment
----------
This app is deployed with Dokku. [Learn about](https://github.com/directactioneverywhere/dxe-learn2dokku) how DxE Tech deploys with Dokku. The Dokku git remote is:

    dokku@dxetech.org:chapters-map

License
=======
dxe-chapters-map is licensed under GNU GPL version 3.0. For the full license see the LICENSE file.
