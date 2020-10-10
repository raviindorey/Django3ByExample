# Django 3 By Example

This repository will have rundown of book _Django 3 By Example_ by _Antonio Melé_.
I have completed the Django 2 By Example but a new Django version is out and this book covers that.
Book started of easy but later covered a wide range of topics. Not for the faint hearted however.

### Docker

Even though book doesn't use it, I have found that docker helps a ton even in development for especially handling sensitive data and deployment consistency. So I'll be dockerizing whatever I can.

Keeping that in mind, you'll need to have following at project level:

1. `db.env`: Settings for db. This needs to set minimum:
   - `POSTGRES_PASSWORD`
2. `web.env`: Settings for web. This needs to set minimum:
   - `SECRET_KEY`
   - `ENV` (set to one of: `development` or `production`)
   - `POSTGRES_PASSWORD`
   - **Bookmark Project** has social authentication so also you'll need
     1. For Facebook:
        - SOCIAL_AUTH_FACEBOOK_KEY
        - SOCIAL_AUTH_FACEBOOK_SECRET
        - SOCIAL_AUTH_FACEBOOK_CLIENT_TOKEN
     2. For Google:
        - SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
        - SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

Leave the value if you have them set in your shell profile.

```powershell
SECRET_KEY    # shell will provide the value
ENV
DEBUG=1       # explicitly giving the value
```
