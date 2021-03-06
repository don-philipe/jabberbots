## dependencies
- python 3.8
- aioxmpp 0.12 (python-aioxmpp on ArchLinux from AUR)
- dnspython3 (used for resolving SRV records, python-dnspython on ArchLinux)
- pyasn1 0.4.8 and pyasn1_modules 0.2.8 to parse SSL certificates (python-pyasn1 and python-pyasn1-modules on archlinux)
- botdeps:
  - feedparser for RssBot (python-feedparser on ArchLinux)

## bot
- get status once
- get status if something changes
- automatically accepts new contact requests -> whitelist necessary

## dhlbot
- get status of package delivery from DHL

- website of trackingnumber:
	https://nolp.dhl.de/nextt-online-public/set_identcodes.do?lang=de&idc=166634261612&rfn=
	in this website:
	img/piece_details_icons/Icon_01_DatenErhaltenDEFAULT_58x58.gif	-> task not yet done
	img/piece_details_icons/Icon_01_DatenErhaltenACTIVE_58x58.gif	-> task done yet

## twitbot/mastodonbot
- get news from specified twitter account

## taskbot
- get/set taskwarrior tasks

## twitchbot
- get live status of a streamer

```
curl 'https://gql.twitch.tv/gql' --compressed -H 'Client-Id: kimne78kx3ncx6brgo4mv6wki5h1ko' -H 'Content-Type: text/plain;charset=UTF-8' -H 'DNT: 1' --data-raw '[{"operationName":"StreamMetadata","variables":{"channelLogin":"fewa05"},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"1c719a40e481453e5c48d9bb585d971b8b372f8ebb105b17076722264dfa5b3e"}}}]'
```

response for simple request when stream is not online (stream object is null):

```
[{"data":{"user":{"id":"<twitch ID>","primaryColorHex":"025600","isPartner":true,"profileImageURL":"<profile image url>","primaryTeam":{"id":"5679","name":"playportal","displayName":"PlayPortal Network","__typename":"Team"},"squadStream":null,"channel":{"id":"<channel ID>","chanlets":null,"__typename":"Channel"},"lastBroadcast":{"id":"1994995217","title":"<last broadcast title>","__typename":"Broadcast"},"stream":null,"__typename":"User"}},"extensions":{"durationMilliseconds":39,"operationName":"StreamMetadata","requestID":"01EB6X3SH1PBX6KQGXKQKKZW0J"}}]
```

response for simple request when stream in live:

```
[{"data":{"user":{"id":"<twitch ID>","primaryColorHex":"8205B3","isPartner":true,"profileImageURL":"<profile image url>","primaryTeam":{"id":"7311","name":"ambassadors","displayName":"Twitch Ambassadors","__typename":"Team"},"squadStream":null,"channel":{"id":"<channel ID>","chanlets":null,"__typename":"Channel"},"lastBroadcast":{"id":"2003590721","title":"<last broadcast title>","__typename":"Broadcast"},"stream":{"id":"<stream ID>","type":"live","createdAt":"2020-06-19T15:26:57Z","__typename":"Stream"},"__typename":"User"}},"extensions":{"durationMilliseconds":39,"operationName":"StreamMetadata","requestID":"01EB6X7VY9HJD1CZSMP1ZDMV1H"}}]
```

## wolbot
- send magic packet for wake-on-lan to specified machine

## more bot ideas
- rssbot - forward rss updates
- webcambot - sends picture of a camera
- musicbot - send a (random) song
- poembot - send a (random) poem
- lyricbot - send the lyrics of a song, fetched from special websites
- eliza - nothing more to say
- bots enabling interaction with other jabber users
- notification bots for other e.g. chat systems
- picture of the day/week/month - sends a picture from e.g. a nextcloud share to the subscriber on a daily/weekly/monthly basis
- html update bot - checks for changes in website and notifies about that
- github bot that notifies about updates in issues you are watching etc.

## more features
- XEP-0084 - avatar for bots (https://docs.zombofant.net/aioxmpp/0.10/api/public/avatar.html#module-aioxmpp.avatar)
