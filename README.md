# Python script written by/for myself.
## https://twitch.tv/codecalico
### WIP

### Contributors:
- [Jon Turner](https://github.com/jondsgntn)
---
- `.env` file needs to be in the root, with the following fields for Twitch(twitchio library)
```
TMI_TOKEN=oauth:notastringtokengoeshere
CLIENT_ID=notastringclientid
CLIENT_SECRET=notastringclientsecret
BOT_NICK=idkwherethisisrelevantbutnotastring
BOT_PREFIX=!bydefaultbutyoucanchangealsonotastring
CHANNEL='#yourChannelURIisString'
```

 - I used [Supabase](https://supabase.com/) to quickly set up a db for persistence. All you need in the `.env` here is:

```
SUPABASE_URL=notastring.supabase.co
SUPABASE_KEY=supabasekeynotastringwillbeveryverylong
```
---
