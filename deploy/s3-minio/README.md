# Minio

Start: `docker-compose up -d`

Console Access: `http://<your-ip>:9001`

API Access: `http://<your-ip>:9000`

## Minio Client
```bash
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x mc
mv mc /usr/local/bin/
```

## Bucket Permissions
```bash
# Login
mc alias set myminio http://<your-ip-here>:9000 minioadmin topsecure
# Test access
mc ls myminio
mc ls myminio/mybucket
# Create policy for public access
mc policy set download myminio/mybucket
mc policy get-json myminio/mybucket > policy.json
# Search for "s3:ListBucket" and remove it
# Apply the modified policy
mc policy set-json policy.json myminio/mybucket
```