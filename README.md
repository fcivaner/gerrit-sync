# gerrit-sync

A command line tool to easily clone gerrit repositories in bulk.

## installation

To install run the following command in your terminal:

```pip3 install gerrit-sync```

## usage

If you just want to see which commands will be run, use:

```gerrit-sync --gerrit-user myuser --gerrit-url https://gerrit.mydomain.com --dry-run```

If you want the actual commands to be run, use:

```gerrit-sync --gerrit-user myuser --gerrit-url https://gerrit.mydomain.com```

All arguments:

```text
usage: gerrit-sync [-h] [--gerrit-user GERRIT_USER]
                   [--gerrit-password GERRIT_PASSWORD]
                   [--gerrit-url GERRIT_URL] [--filter FILTER] [--dry-run]
                   [--log-level {error,info,debug}]

gerrit-sync

optional arguments:
  -h, --help            show this help message and exit
  --gerrit-user GERRIT_USER
                        Username for access to gerrit API. If not provided via
                        this argument or the environment variable GERRIT_USER,
                        it will be asked via the command prompt.
  --gerrit-password GERRIT_PASSWORD
                        ** Password for access to gerrit API. If not provided
                        via this argument or the environment variable
                        GERRIT_PASSWORD, it will be asked via the command
                        prompt. ** WARNING **: Providing the password via the
                        command line argument is not recommended due to the
                        risk of your password being recorded in your shell
                        history.
  --gerrit-url GERRIT_URL
                        Base URL of the gerrit API. If not provided via this
                        argument or the environment variable GERRIT_URL, it
                        will be asked via the command prompt. example:
                        https://gerrit.mydomain.com
  --filter FILTER       A regular expression to filter project names. If not
                        provided, projects are not filtered.
  --dry-run             If specified, just display the operations to be done
                        but do not perform them.
  --log-level {error,info,debug}
```

## development

To avoid reinstalling the project during development, the package can be directly run from repository root directory for development purposes with command ```python3 -m gerrit_sync```.
