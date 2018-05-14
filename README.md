Girl Effect Wagtail site
==================

## Contributing

1. Make changes on a new branch, including a broad category and the ticket number if relevant e.g. `feature/123-extra-squiggles`, `fix/newsletter-signup`.
1. Push your branch to the remote.
1. Edit details as necessary.

If you need to preview work on `staging`, this can be merged and deployed manually without making a merge request. You can still make the merge request as above, but add a note to say that this is on `staging`, and not yet ready to be merged to `master`.

# Setting up a local build

This repository includes a Vagrantfile for running the project in a Debian VM and
a fabfile for running common commands with Fabric.

To set up a new build:

``` bash
git clone git@github.com:girleffect/girleffect.org.git
cd girleffect
# Rather use the box command to download the vagrant image first
vagrant box add http://vagrantcloud.com/torchbox/wagtail-jessie64
vagrant up
vagrant ssh
```

Then within the SSH session:

``` bash
# Populate the db
sudo -u postgres psql girleffect < {latest db dump}.sql
dj migrate
dj createsuperuser
djrun
```

This will make the site available on the host machine at: http://127.0.0.1:8000/
