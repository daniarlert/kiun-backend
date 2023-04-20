## v0.1.0 (2023-04-20)

### Feat

- add custom storage backends
- add AWS S3 support for staticfiles
- setup whitenoise
- change default permission for drf
- add cors basic config for local development
- add serializers and views for api endpoints
- add tests
- **studies**: add studies related models
- **projects**: add tags to projects
- **skills**: add basic skill model with tags
- **projects**: add basic project model
- **accounts**: add social link model
- **accounts**: add name and contact email to custom user
- **accounts**: add about field to custom user
- **accounts**: add custom user model

### Fix

- **docker**: fix issue with storage for media files
- **docker**: fix issue with redis on docker-compose

### Refactor

- **accounts**: remove non-necessary imports
