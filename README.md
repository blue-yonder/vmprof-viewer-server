# vmprof-viewer server

For vmprof-viewer usage instructions, see https://github.com/blue-yonder/vmprof-viewer-client.

To get the vmprof-viewer server running, follow a standard Django deployment:

```sh
# Clone repo
git clone https://github.com/blue-yonder/vmprof-viewer-server
cd vmprof-viewer-server
git submodule update --init

# Apply our vmprof-server patch
cd vmprof-server/; git apply ../vmprof-server-patch.diff; cd -

# Install dependencies
virtualenv env
. env/bin/activate
pip install -r requirements.txt

# Bootstrap server application
vmprof_viewer/manage.py migrate

# Start server
vmprof_viewer/manage.py runserver
```
