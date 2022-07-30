import interactions
next_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Next",
    custom_id="next_result"
)

previous_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Previous",
    custom_id="previous_result"
)

enter_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="✅",
    custom_id="select_result"
)

airing_button = interactions.Button(
    style=interactions.ButtonStyle.PRIMARY,
    label="Airing Information",
    custom_id="airing_info"
)