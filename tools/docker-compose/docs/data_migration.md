# Migrating Data from Local Docker

If you are migrating data from a Local Docker installation (17.0.1 and prior), you can 
migrate your data to the development environment via the migrate.yml playbook. 

> Note: This will also convert your postgresql bind-mount into a docker volume.

First, in the  `inventory` file, set your `pg_password`, `broadcast_websocket_secret`, `secret_key`, and any other settings you need for your deployment.  **Make sure you use the same secret key value you had with your previous Local Docker deployment.**  

### Migrate data with migrate.yml

If you had a custom pgdocker or awxcompose location, you will need to set the `postgres_data_dir` and `old_docker_compose_dir` variables. 

1. Run the [migrate playbook](../ansible/migrate.yml) to migrate your data to the new postgresql container and convert the data directory to a volume mount.
```bash
$ ansible-playbook  -i tools/docker-compose/inventory tools/docker-compose/ansible/migrate.yml -e "migrate_local_docker=true" -e "postgres_data_dir=~/.awx/pgdocker" -e "old_docker_compose_dir=~/.awx/awxcompose"
```

2. Change directory to the top of your awx checkout and start your containers
```bash
$ make docker-compose
```

3. After ensuring your data has been successfully migrated, you may delete your old data directory (typically stored at `~/.awx/pgdocker`). 
