ANIME_SEARCH = '''
    query {
        Page {
            media(search: "$ANIME" type: ANIME) {
                id
                siteUrl
                format
                episodes
                status
                title {
                    romaji
                    english
                    native
                }
                description(asHtml: false)
                coverImage {
                    extraLarge
                }
            }
        }
    }
'''