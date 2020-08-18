# Django 3 By Example

This repository will have rundown of book _Django 3 By Example_ by _Antonio Mele_.
I have completed the Django 2 By Example but a new Django version is out and this book covers that.
Contents of the books looks almost the same as previous version except one chapter.
That book started of easy but later covered a wide range of topics. Not for the faint hearted however.
Lets see if this new version holds up to that.

### Docker

Even though book doesn't use it, I have found that docker helps a ton even in development, especially handling sensitive data.
So I'll be dockerizing whatever I can.

Keeping that in mind, you'll need to have following at project level:

1. `.db.env`: Settings for db. This needs to set minimum:
   - `POSTGRES_PASSWORD`
2. `.web.env`: Settings for web. This needs to set minimum:
   - `SECRET_KEY`
   - `ENV` (`development` or `production`)
   - `POSTGRES_PASSWORD`

Leave the value if you have them set in your shell profile.

```powershell
SECRET_KEY    # shell will provide the value
ENV
DEBUG=1       # explicitly giving the value
```
